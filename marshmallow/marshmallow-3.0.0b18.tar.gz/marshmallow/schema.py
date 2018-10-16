# -*- coding: utf-8 -*-
"""The :class:`Schema` class, including its metaclass and options (class Meta)."""
from __future__ import absolute_import, unicode_literals

from collections import defaultdict, OrderedDict
import functools
import copy
import inspect
import json
import warnings

from marshmallow import base, fields, utils, class_registry, marshalling
from marshmallow.compat import iteritems, iterkeys, with_metaclass
from marshmallow.exceptions import ValidationError, StringNotCollectionError
from marshmallow.orderedset import OrderedSet
from marshmallow.decorators import (
    POST_DUMP,
    POST_LOAD,
    PRE_DUMP,
    PRE_LOAD,
    VALIDATES,
    VALIDATES_SCHEMA,
)
from marshmallow.utils import RAISE, missing, is_collection


def _get_fields(attrs, field_class, pop=False, ordered=False):
    """Get fields from a class. If ordered=True, fields will sorted by creation index.

    :param attrs: Mapping of class attributes
    :param type field_class: Base field class
    :param bool pop: Remove matching fields
    """
    fields = [
        (field_name, field_value)
        for field_name, field_value in iteritems(attrs)
        if utils.is_instance_or_subclass(field_value, field_class)
    ]
    if pop:
        for field_name, _ in fields:
            del attrs[field_name]
    if ordered:
        fields.sort(key=lambda pair: pair[1]._creation_index)
    return fields

# This function allows Schemas to inherit from non-Schema classes and ensures
#   inheritance according to the MRO
def _get_fields_by_mro(klass, field_class, ordered=False):
    """Collect fields from a class, following its method resolution order. The
    class itself is excluded from the search; only its parents are checked. Get
    fields from ``_declared_fields`` if available, else use ``__dict__``.

    :param type klass: Class whose fields to retrieve
    :param type field_class: Base field class
    """
    mro = inspect.getmro(klass)
    # Loop over mro in reverse to maintain correct order of fields
    return sum(
        (
            _get_fields(
                getattr(base, '_declared_fields', base.__dict__),
                field_class,
                ordered=ordered,
            )
            for base in mro[:0:-1]
        ),
        [],
    )


class SchemaMeta(type):
    """Metaclass for the Schema class. Binds the declared fields to
    a ``_declared_fields`` attribute, which is a dictionary mapping attribute
    names to field objects. Also sets the ``opts`` class attribute, which is
    the Schema class's ``class Meta`` options.
    """

    def __new__(mcs, name, bases, attrs):
        meta = attrs.get('Meta')
        ordered = getattr(meta, 'ordered', False)
        if not ordered:
            # Inherit 'ordered' option
            # Warning: We loop through bases instead of MRO because we don't
            # yet have access to the class object
            # (i.e. can't call super before we have fields)
            for base_ in bases:
                if hasattr(base_, 'Meta') and hasattr(base_.Meta, 'ordered'):
                    ordered = base_.Meta.ordered
                    break
            else:
                ordered = False
        cls_fields = _get_fields(attrs, base.FieldABC, pop=True, ordered=ordered)
        klass = super(SchemaMeta, mcs).__new__(mcs, name, bases, attrs)
        inherited_fields = _get_fields_by_mro(klass, base.FieldABC, ordered=ordered)

        # Use getattr rather than attrs['Meta'] so that we get inheritance for free
        meta = getattr(klass, 'Meta')
        # Set klass.opts in __new__ rather than __init__ so that it is accessible in
        # get_declared_fields
        klass.opts = klass.OPTIONS_CLASS(meta, ordered=ordered)
        # Add fields specifid in the `include` class Meta option
        cls_fields += list(klass.opts.include.items())

        dict_cls = OrderedDict if ordered else dict
        # Assign _declared_fields on class
        klass._declared_fields = mcs.get_declared_fields(
            klass=klass,
            cls_fields=cls_fields,
            inherited_fields=inherited_fields,
            dict_cls=dict_cls,
        )
        return klass

    @classmethod
    def get_declared_fields(mcs, klass, cls_fields, inherited_fields, dict_cls):
        """Returns a dictionary of field_name => `Field` pairs declard on the class.
        This is exposed mainly so that plugins can add additional fields, e.g. fields
        computed from class Meta options.

        :param type klass: The class object.
        :param dict cls_fields: The fields declared on the class, including those added
            by the ``include`` class Meta option.
        :param dict inherited_fileds: Inherited fields.
        :param type dict_class: Either `dict` or `OrderedDict`, depending on the whether
            the user specified `ordered=True`.
        """
        return dict_cls(inherited_fields + cls_fields)

    # NOTE: self is the class object
    def __init__(self, name, bases, attrs):
        super(SchemaMeta, self).__init__(name, bases, attrs)
        if name:
            class_registry.register(name, self)
        self._hooks = self.resolve_hooks()

    def resolve_hooks(self):
        """Add in the decorated processors

        By doing this after constructing the class, we let standard inheritance
        do all the hard work.
        """
        mro = inspect.getmro(self)

        hooks = defaultdict(list)

        for attr_name in dir(self):
            # Need to look up the actual descriptor, not whatever might be
            # bound to the class. This needs to come from the __dict__ of the
            # declaring class.
            for parent in mro:
                try:
                    attr = parent.__dict__[attr_name]
                except KeyError:
                    continue
                else:
                    break
            else:
                # In case we didn't find the attribute and didn't break above.
                # We should never hit this - it's just here for completeness
                # to exclude the possibility of attr being undefined.
                continue

            try:
                hook_config = attr.__marshmallow_hook__
            except AttributeError:
                pass
            else:
                for key in iterkeys(hook_config):
                    # Use name here so we can get the bound method later, in
                    # case the processor was a descriptor or something.
                    hooks[key].append(attr_name)

        return hooks


class SchemaOpts(object):
    """class Meta options for the :class:`Schema`. Defines defaults."""

    def __init__(self, meta, ordered=False):
        self.fields = getattr(meta, 'fields', ())
        if not isinstance(self.fields, (list, tuple)):
            raise ValueError('`fields` option must be a list or tuple.')
        self.additional = getattr(meta, 'additional', ())
        if not isinstance(self.additional, (list, tuple)):
            raise ValueError('`additional` option must be a list or tuple.')
        if self.fields and self.additional:
            raise ValueError(
                'Cannot set both `fields` and `additional` options'
                ' for the same Schema.',
            )
        self.exclude = getattr(meta, 'exclude', ())
        if not isinstance(self.exclude, (list, tuple)):
            raise ValueError('`exclude` must be a list or tuple.')
        self.dateformat = getattr(meta, 'dateformat', None)
        self.datetimeformat = getattr(meta, 'datetimeformat', None)
        if hasattr(meta, 'json_module'):
            warnings.warn(
                'The json_module class Meta option is deprecated. Use render_module instead.',
                DeprecationWarning,
            )
            render_module = getattr(meta, 'json_module', json)
        else:
            render_module = json
        self.render_module = getattr(meta, 'render_module', render_module)
        self.ordered = getattr(meta, 'ordered', ordered)
        self.index_errors = getattr(meta, 'index_errors', True)
        self.include = getattr(meta, 'include', {})
        self.load_only = getattr(meta, 'load_only', ())
        self.dump_only = getattr(meta, 'dump_only', ())
        self.unknown = getattr(meta, 'unknown', RAISE)


class BaseSchema(base.SchemaABC):
    """Base schema class with which to define custom schemas.

    Example usage:

    .. code-block:: python

        import datetime as dt
        from marshmallow import Schema, fields

        class Album(object):
            def __init__(self, title, release_date):
                self.title = title
                self.release_date = release_date

        class AlbumSchema(Schema):
            title = fields.Str()
            release_date = fields.Date()

        # Or, equivalently
        class AlbumSchema2(Schema):
            class Meta:
                fields = ("title", "release_date")

        album = Album("Beggars Banquet", dt.date(1968, 12, 6))
        schema = AlbumSchema()
        data, errors = schema.dump(album)
        data  # {'release_date': '1968-12-06', 'title': 'Beggars Banquet'}

    :param tuple|list only: Whitelist of the declared fields to select when
        instantiating the Schema. If None, all fields are used. Nested fields
        can be represented with dot delimiters.
    :param tuple|list exclude: Blacklist of the declared fields to exclude
        when instantiating the Schema. If a field appears in both `only` and
        `exclude`, it is not used. Nested fields can be represented with dot
        delimiters.
    :param bool many: Should be set to `True` if ``obj`` is a collection
        so that the object will be serialized to a list.
    :param dict context: Optional context passed to :class:`fields.Method` and
        :class:`fields.Function` fields.
    :param tuple|list load_only: Fields to skip during serialization (write-only fields)
    :param tuple|list dump_only: Fields to skip during deserialization (read-only fields)
    :param bool|tuple partial: Whether to ignore missing fields. If its value
        is an iterable, only missing fields listed in that iterable will be
        ignored.
    :param unknown: Whether to exclude, include, or raise an error for unknown
        fields in the data. Use `EXCLUDE`, `INCLUDE` or `RAISE`.

    .. versionchanged:: 3.0.0
        `prefix` parameter removed.

    .. versionchanged:: 2.0.0
        `__validators__`, `__preprocessors__`, and `__data_handlers__` are removed in favor of
        `marshmallow.decorators.validates_schema`,
        `marshmallow.decorators.pre_load` and `marshmallow.decorators.post_dump`.
        `__accessor__` and `__error_handler__` are deprecated. Implement the
        `handle_error` and `get_attribute` methods instead.
        """
    OPTIONS_CLASS = SchemaOpts

    class Meta(object):
        """Options object for a Schema.

        Example usage: ::

            class Meta:
                fields = ("id", "email", "date_created")
                exclude = ("password", "secret_attribute")

        Available options:

        - ``fields``: Tuple or list of fields to include in the serialized result.
        - ``additional``: Tuple or list of fields to include *in addition* to the
            explicitly declared fields. ``additional`` and ``fields`` are
            mutually-exclusive options.
        - ``include``: Dictionary of additional fields to include in the schema. It is
            usually better to define fields as class variables, but you may need to
            use this option, e.g., if your fields are Python keywords. May be an
            `OrderedDict`.
        - ``exclude``: Tuple or list of fields to exclude in the serialized result.
            Nested fields can be represented with dot delimiters.
        - ``dateformat``: Date format for all DateTime fields that do not have their
            date format explicitly specified.
        - ``render_module``: Module to use for `loads` and `dumps`. Defaults to
            `json` from the standard library.
        - ``ordered``: If `True`, order serialization output according to the
            order in which fields were declared. Output of `Schema.dump` will be a
            `collections.OrderedDict`.
        - ``index_errors``: If `True`, errors dictionaries will include the index
            of invalid items in a collection.
        - ``load_only``: Tuple or list of fields to exclude from serialized results.
        - ``dump_only``: Tuple or list of fields to exclude from deserialization
        - ``unknown``: Whether to exclude, include, or raise an error for unknown
            fields in the data. Use `EXCLUDE`, `INCLUDE` or `RAISE`.
        """
        pass

    def __init__(
        self, only=None, exclude=(), many=False, context=None,
        load_only=(), dump_only=(), partial=False, unknown=None,
    ):
        # Raise error if only or exclude is passed as string, not list of strings
        if only is not None and not is_collection(only):
            raise StringNotCollectionError('"only" should be a list of strings')
        if exclude is not None and not is_collection(exclude):
            raise StringNotCollectionError('"exclude" should be a list of strings')
        # copy declared fields from metaclass
        self.declared_fields = copy.deepcopy(self._declared_fields)
        self.many = many
        self.only = only
        self.exclude = exclude
        self.ordered = self.opts.ordered
        self.load_only = set(load_only) or set(self.opts.load_only)
        self.dump_only = set(dump_only) or set(self.opts.dump_only)
        self.partial = partial
        self.unknown = unknown or self.opts.unknown
        self.context = context or {}
        self._normalize_nested_options()
        #: Dictionary mapping field_names -> :class:`Field` objects
        self.fields = self._init_fields()

    def __repr__(self):
        return '<{ClassName}(many={self.many})>'.format(
            ClassName=self.__class__.__name__, self=self,
        )

    @property
    def dict_class(self):
        return OrderedDict if self.ordered else dict

    @property
    def set_class(self):
        return OrderedSet if self.ordered else set

    ##### Override-able methods #####

    def handle_error(self, error, data):
        """Custom error handler function for the schema.

        :param ValidationError error: The `ValidationError` raised during (de)serialization.
        :param data: The original input data.

        .. versionadded:: 2.0.0
        """
        pass

    def get_attribute(self, obj, attr, default):
        """Defines how to pull values from an object to serialize.

        .. versionadded:: 2.0.0

        .. versionchanged:: 3.0.0a1
            Changed position of ``obj`` and ``attr``.
        """
        return utils.get_value(obj, attr, default)

    ##### Serialization/Deserialization API #####

    def dump(self, obj, many=None):
        """Serialize an object to native Python data types according to this
        Schema's fields.

        :param obj: The object to serialize.
        :param bool many: Whether to serialize `obj` as a collection. If `None`, the value
            for `self.many` is used.
        :return: A dict of serialized data
        :rtype: dict

        .. versionadded:: 1.0.0
        .. versionchanged:: 3.0.0b7
            This method returns the serialized data rather than a ``(data, errors)`` duple.
            A :exc:`ValidationError <marshmallow.exceptions.ValidationError>` is raised
            if ``obj`` is invalid.
        """
        # Callable marshalling object
        marshal = marshalling.Marshaller()
        errors = {}
        many = self.many if many is None else bool(many)
        if many and utils.is_iterable_but_not_string(obj):
            obj = list(obj)

        if self._has_processors(PRE_DUMP):
            try:
                processed_obj = self._invoke_dump_processors(
                    PRE_DUMP,
                    obj,
                    many,
                    original_data=obj,
                )
            except ValidationError as error:
                errors = error.normalized_messages()
                result = None
        else:
            processed_obj = obj

        if not errors:
            try:
                result = marshal(
                    processed_obj,
                    self.fields,
                    many=many,
                    accessor=self.get_attribute,
                    dict_class=self.dict_class,
                    index_errors=self.opts.index_errors,
                )
            except ValidationError as error:
                errors = marshal.errors
                result = error.data

        if not errors and self._has_processors(POST_DUMP):
            try:
                result = self._invoke_dump_processors(
                    POST_DUMP,
                    result,
                    many,
                    original_data=obj,
                )
            except ValidationError as error:
                errors = error.normalized_messages()
        if errors:
            exc = ValidationError(
                errors,
                field_names=marshal.error_field_names,
                data=obj,
                valid_data=result,
                **marshal.error_kwargs
            )
            # User-defined error handler
            self.handle_error(exc, obj)
            raise exc

        return result

    def dumps(self, obj, many=None, *args, **kwargs):
        """Same as :meth:`dump`, except return a JSON-encoded string.

        :param obj: The object to serialize.
        :param bool many: Whether to serialize `obj` as a collection. If `None`, the value
            for `self.many` is used.
        :return: A ``json`` string
        :rtype: str

        .. versionadded:: 1.0.0
        .. versionchanged:: 3.0.0b7
            This method returns the serialized data rather than a ``(data, errors)`` duple.
            A :exc:`ValidationError <marshmallow.exceptions.ValidationError>` is raised
            if ``obj`` is invalid.
        """
        serialized = self.dump(obj, many=many)
        return self.opts.render_module.dumps(serialized, *args, **kwargs)

    def load(self, data, many=None, partial=None, unknown=None):
        """Deserialize a data structure to an object defined by this Schema's fields.

        :param dict data: The data to deserialize.
        :param bool many: Whether to deserialize `data` as a collection. If `None`, the
            value for `self.many` is used.
        :param bool|tuple partial: Whether to ignore missing fields. If `None`,
            the value for `self.partial` is used. If its value is an iterable,
            only missing fields listed in that iterable will be ignored.
        :param unknown: Whether to exclude, include, or raise an error for unknown
            fields in the data. Use `EXCLUDE`, `INCLUDE` or `RAISE`.
            If `None`, the value for `self.unknown` is used.
        :return: A dict of deserialized data
        :rtype: dict

        .. versionadded:: 1.0.0
        .. versionchanged:: 3.0.0b7
            This method returns the deserialized data rather than a ``(data, errors)`` duple.
            A :exc:`ValidationError <marshmallow.exceptions.ValidationError>` is raised
            if invalid data are passed.
        """
        return self._do_load(
            data, many, partial=partial, unknown=unknown,
            postprocess=True,
        )

    def loads(
        self, json_data, many=None, partial=None, unknown=None,
        **kwargs
    ):
        """Same as :meth:`load`, except it takes a JSON string as input.

        :param str json_data: A JSON string of the data to deserialize.
        :param bool many: Whether to deserialize `obj` as a collection. If `None`, the
            value for `self.many` is used.
        :param bool|tuple partial: Whether to ignore missing fields. If `None`,
            the value for `self.partial` is used. If its value is an iterable,
            only missing fields listed in that iterable will be ignored.
        :param unknown: Whether to exclude, include, or raise an error for unknown
            fields in the data. Use `EXCLUDE`, `INCLUDE` or `RAISE`.
            If `None`, the value for `self.unknown` is used.
        :return: A dict of deserialized data
        :rtype: dict

        .. versionadded:: 1.0.0
        .. versionchanged:: 3.0.0b7
            This method returns the deserialized data rather than a ``(data, errors)`` duple.
            A :exc:`ValidationError <marshmallow.exceptions.ValidationError>` is raised
            if invalid data are passed.
        """
        data = self.opts.render_module.loads(json_data, **kwargs)
        return self.load(data, many=many, partial=partial, unknown=unknown)

    def validate(self, data, many=None, partial=None):
        """Validate `data` against the schema, returning a dictionary of
        validation errors.

        :param dict data: The data to validate.
        :param bool many: Whether to validate `data` as a collection. If `None`, the
            value for `self.many` is used.
        :param bool|tuple partial: Whether to ignore missing fields. If `None`,
            the value for `self.partial` is used. If its value is an iterable,
            only missing fields listed in that iterable will be ignored.
        :return: A dictionary of validation errors.
        :rtype: dict

        .. versionadded:: 1.1.0
        """
        try:
            self._do_load(data, many, partial=partial, postprocess=False)
        except ValidationError as exc:
            return exc.messages
        return {}

    ##### Private Helpers #####

    def _do_load(
        self, data, many=None, partial=None, unknown=None,
        postprocess=True,
    ):
        """Deserialize `data`, returning the deserialized result.

        :param data: The data to deserialize.
        :param bool many: Whether to deserialize `data` as a collection. If `None`, the
            value for `self.many` is used.
        :param bool|tuple partial: Whether to validate required fields. If its value is an iterable,
            only fields listed in that iterable will be ignored will be allowed missing.
            If `True`, all fields will be allowed missing.
            If `None`, the value for `self.partial` is used.
        :param unknown: Whether to exclude, include, or raise an error for unknown
            fields in the data. Use `EXCLUDE`, `INCLUDE` or `RAISE`.
            If `None`, the value for `self.unknown` is used.
        :param bool postprocess: Whether to run post_load methods..
        :return: A dict of deserialized data
        :rtype: dict
        """
        # Callable unmarshalling object
        unmarshal = marshalling.Unmarshaller()
        errors = {}
        many = self.many if many is None else bool(many)
        unknown = unknown or self.unknown
        if partial is None:
            partial = self.partial
        if self._has_processors(PRE_LOAD):
            try:
                processed_data = self._invoke_load_processors(
                    PRE_LOAD,
                    data,
                    many,
                    original_data=data,
                )
            except ValidationError as err:
                errors = err.normalized_messages()
                result = None
        else:
            processed_data = data
        if not errors:
            result = unmarshal(
                processed_data,
                self.fields,
                many=many,
                partial=partial,
                unknown=unknown,
                dict_class=self.dict_class,
                index_errors=self.opts.index_errors,
            )
            self._invoke_field_validators(unmarshal, data=result, many=many)
            errors = unmarshal.errors
            # Run schema-level validation.
            if self._has_processors(VALIDATES_SCHEMA):
                field_errors = bool(errors)
                self._invoke_schema_validators(
                    unmarshal,
                    pass_many=True,
                    data=result,
                    original_data=data,
                    many=many,
                    field_errors=field_errors,
                )
                self._invoke_schema_validators(
                    unmarshal,
                    pass_many=False,
                    data=result,
                    original_data=data,
                    many=many,
                    field_errors=field_errors,
                )
        # Run post processors
        if not errors and postprocess and self._has_processors(POST_LOAD):
            try:
                result = self._invoke_load_processors(
                    POST_LOAD,
                    result,
                    many,
                    original_data=data,
                )
            except ValidationError as err:
                errors = err.normalized_messages()
        if errors:
            exc = ValidationError(
                errors,
                field_names=unmarshal.error_field_names,
                data=data,
                valid_data=result,
                **unmarshal.error_kwargs
            )
            self.handle_error(exc, data)
            raise exc

        return result

    def _normalize_nested_options(self):
        """Apply then flatten nested schema options"""
        if self.only is not None:
            # Apply the only option to nested fields.
            self.__apply_nested_option('only', self.only, 'intersection')
            # Remove the child field names from the only option.
            self.only = self.set_class(
                [field.split('.', 1)[0] for field in self.only],
            )
        excludes = set(self.opts.exclude) | set(self.exclude)
        if excludes:
            # Apply the exclude option to nested fields.
            self.__apply_nested_option('exclude', excludes, 'union')
        if self.exclude:
            # Remove the parent field names from the exclude option.
            self.exclude = self.set_class(
                [field for field in self.exclude if '.' not in field],
            )
        if self.opts.exclude:
            # Remove the parent field names from the meta exclude option.
            self.opts.exclude = self.set_class(
                [field for field in self.opts.exclude if '.' not in field],
            )

    def __apply_nested_option(self, option_name, field_names, set_operation):
        """Apply nested options to nested fields"""
        # Split nested field names on the first dot.
        nested_fields = [name.split('.', 1) for name in field_names if '.' in name]
        # Partition the nested field names by parent field.
        nested_options = defaultdict(list)
        for parent, nested_names in nested_fields:
            nested_options[parent].append(nested_names)
        # Apply the nested field options.
        for key, options in iter(nested_options.items()):
            new_options = self.set_class(options)
            original_options = getattr(self.declared_fields[key], option_name, ())
            if original_options:
                if set_operation == 'union':
                    new_options |= self.set_class(original_options)
                if set_operation == 'intersection':
                        new_options &= self.set_class(original_options)
            setattr(self.declared_fields[key], option_name, new_options)

    def _init_fields(self):
        """Update fields based on schema options."""
        if self.opts.fields:
            available_field_names = self.set_class(self.opts.fields)
        else:
            available_field_names = self.set_class(self.declared_fields.keys())
            if self.opts.additional:
                available_field_names |= self.set_class(self.opts.additional)

        invalid_fields = self.set_class()

        if self.only is not None:
            # Return only fields specified in only option
            field_names = self.set_class(self.only)

            invalid_fields |= field_names - available_field_names
        else:
            field_names = available_field_names

        # If "exclude" option or param is specified, remove those fields.
        exclude_field_names = set(self.opts.exclude) | set(self.exclude)
        if exclude_field_names:
            # Note that this isn't available_field_names, since we want to
            # apply "only" for the actual calculation.
            field_names = field_names - exclude_field_names

            invalid_fields |= exclude_field_names - available_field_names

        if invalid_fields:
            message = 'Invalid fields for {0}: {1}.'.format(self, invalid_fields)
            raise ValueError(message)

        fields_dict = self.dict_class()
        for field_name in field_names:
            field_obj = self.declared_fields.get(field_name, fields.Inferred())
            self._bind_field(field_name, field_obj)
            fields_dict[field_name] = field_obj

        dump_data_keys = [
            obj.data_key or name for name, obj in iteritems(fields_dict) if not obj.load_only
        ]
        if len(dump_data_keys) != len(set(dump_data_keys)):
            data_keys_duplicates = {x for x in dump_data_keys if dump_data_keys.count(x) > 1}
            raise ValueError('Duplicate data_keys: {}'.format(data_keys_duplicates))

        load_attributes = [
            obj.attribute or name for name, obj in iteritems(fields_dict) if not obj.dump_only
        ]
        if len(load_attributes) != len(set(load_attributes)):
            attributes_duplicates = {x for x in load_attributes if load_attributes.count(x) > 1}
            raise ValueError('Duplicate attributes: {}'.format(attributes_duplicates))

        return fields_dict

    def on_bind_field(self, field_name, field_obj):
        """Hook to modify a field when it is bound to the `Schema`.

        No-op by default.
        """
        return None

    def _bind_field(self, field_name, field_obj):
        """Bind field to the schema, setting any necessary attributes on the
        field (e.g. parent and name).

        Also set field load_only and dump_only values if field_name was
        specified in ``class Meta``.
        """
        try:
            if field_name in self.load_only:
                field_obj.load_only = True
            if field_name in self.dump_only:
                field_obj.dump_only = True
            field_obj._bind_to_schema(field_name, self)
            self.on_bind_field(field_name, field_obj)
        except TypeError:
            # field declared as a class, not an instance
            if (isinstance(field_obj, type) and
                    issubclass(field_obj, base.FieldABC)):
                msg = ('Field for "{0}" must be declared as a '
                       'Field instance, not a class. '
                       'Did you mean "fields.{1}()"?'
                       .format(field_name, field_obj.__name__))
                raise TypeError(msg)

    def _has_processors(self, tag):
        return self._hooks[(tag, True)] or self._hooks[(tag, False)]

    def _invoke_dump_processors(self, tag, data, many, original_data=None):
        # The pass_many post-dump processors may do things like add an envelope, so
        # invoke those after invoking the non-pass_many processors which will expect
        # to get a list of items.
        data = self._invoke_processors(
            tag, pass_many=False,
            data=data, many=many, original_data=original_data,
        )
        data = self._invoke_processors(
            tag, pass_many=True,
            data=data, many=many, original_data=original_data,
        )
        return data

    def _invoke_load_processors(self, tag, data, many, original_data=None):
        # This has to invert the order of the dump processors, so run the pass_many
        # processors first.
        data = self._invoke_processors(
            tag, pass_many=True,
            data=data, many=many, original_data=original_data,
        )
        data = self._invoke_processors(
            tag, pass_many=False,
            data=data, many=many, original_data=original_data,
        )
        return data

    def _invoke_field_validators(self, unmarshal, data, many):
        for attr_name in self._hooks[VALIDATES]:
            validator = getattr(self, attr_name)
            validator_kwargs = validator.__marshmallow_hook__[VALIDATES]
            field_name = validator_kwargs['field_name']

            try:
                field_obj = self.fields[field_name]
            except KeyError:
                if field_name in self.declared_fields:
                    continue
                raise ValueError('"{0}" field does not exist.'.format(field_name))

            if many:
                for idx, item in enumerate(data):
                    try:
                        value = item[field_obj.attribute or field_name]
                    except KeyError:
                        pass
                    else:
                        validated_value = unmarshal.call_and_store(
                            getter_func=validator,
                            data=value,
                            field_name=field_obj.data_key or field_name,
                            index=(idx if self.opts.index_errors else None),
                        )
                        if validated_value is missing:
                            data[idx].pop(field_name, None)
            else:
                try:
                    value = data[field_obj.attribute or field_name]
                except KeyError:
                    pass
                else:
                    validated_value = unmarshal.call_and_store(
                        getter_func=validator,
                        data=value,
                        field_name=field_obj.data_key or field_name,
                    )
                    if validated_value is missing:
                        data.pop(field_name, None)

    def _invoke_schema_validators(
        self,
        unmarshal,
        pass_many,
        data,
        original_data,
        many,
        field_errors=False,
    ):
        for attr_name in self._hooks[(VALIDATES_SCHEMA, pass_many)]:
            validator = getattr(self, attr_name)
            validator_kwargs = validator.__marshmallow_hook__[(VALIDATES_SCHEMA, pass_many)]
            pass_original = validator_kwargs.get('pass_original', False)

            skip_on_field_errors = validator_kwargs['skip_on_field_errors']
            if skip_on_field_errors and field_errors:
                continue

            if pass_many:
                validator = functools.partial(validator, many=many)
            if many and not pass_many:
                for idx, (item, orig) in enumerate(zip(data, original_data)):
                    unmarshal.run_validator(
                        validator,
                        item,
                        orig,
                        self.fields,
                        many=many,
                        index=idx,
                        pass_original=pass_original,
                    )
            else:
                unmarshal.run_validator(
                    validator,
                    data,
                    original_data,
                    self.fields,
                    many=many,
                    pass_original=pass_original,
                )

    def _invoke_processors(
        self,
        tag,
        pass_many,
        data,
        many,
        original_data=None,
    ):
        key = (tag, pass_many)
        for attr_name in self._hooks[key]:
            # This will be a bound method.
            processor = getattr(self, attr_name)

            processor_kwargs = processor.__marshmallow_hook__[key]
            pass_original = processor_kwargs.get('pass_original', False)

            if pass_many:
                if pass_original:
                    data = processor(data, many, original_data)
                else:
                    data = processor(data, many)
            elif many:
                if pass_original:
                    data = [
                        processor(item, original)
                        for item, original in zip(data, original_data)
                    ]
                else:
                    data = [processor(item) for item in data]
            else:
                if pass_original:
                    data = processor(data, original_data)
                else:
                    data = processor(data)
        return data


class Schema(with_metaclass(SchemaMeta, BaseSchema)):
    __doc__ = BaseSchema.__doc__
