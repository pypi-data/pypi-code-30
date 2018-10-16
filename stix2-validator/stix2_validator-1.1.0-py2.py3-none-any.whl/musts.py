"""Mandatory (MUST) requirement checking functions
"""

import re

from dateutil import parser
from six import string_types
from stix2patterns.pattern import Pattern
from stix2patterns.validator import run_validator as pattern_validator

from . import enums
from .errors import JSONError, PatternError
from .output import info
from .util import cyber_observable_check, has_cyber_observable_data

CUSTOM_TYPE_PREFIX_RE = re.compile(r"^x\-.+\-.+$")
CUSTOM_TYPE_LAX_PREFIX_RE = re.compile(r"^x\-.+$")
CUSTOM_PROPERTY_PREFIX_RE = re.compile(r"^x_.+_.+$")
CUSTOM_PROPERTY_LAX_PREFIX_RE = re.compile(r"^x_.+$")


def timestamp(instance):
    """Ensure timestamps contain sane months, days, hours, minutes, seconds.
    """
    ts_re = re.compile(r"^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]+)?Z$")
    timestamp_props = ['created', 'modified']
    if instance['type'] in enums.TIMESTAMP_PROPERTIES:
        timestamp_props += enums.TIMESTAMP_PROPERTIES[instance['type']]

    for tprop in timestamp_props:
        if tprop in instance and ts_re.match(instance[tprop]):
            # Don't raise an error if schemas will catch it
            try:
                parser.parse(instance[tprop])
            except ValueError as e:
                yield JSONError("'%s': '%s' is not a valid timestamp: %s"
                                % (tprop, instance[tprop], str(e)), instance['id'])

    if has_cyber_observable_data(instance):
        for key, obj in instance['objects'].items():
            if 'type' not in obj:
                continue
            if obj['type'] in enums.TIMESTAMP_OBSERVABLE_PROPERTIES:
                for tprop in enums.TIMESTAMP_OBSERVABLE_PROPERTIES[obj['type']]:
                    if tprop in obj and ts_re.match(obj[tprop]):
                        # Don't raise an error if schemas will catch it
                        try:
                            parser.parse(obj[tprop])
                        except ValueError as e:
                            yield JSONError("'%s': '%s': '%s' is not a valid timestamp: %s"
                                            % (obj['type'], tprop, obj[tprop], str(e)), instance['id'])
            if obj['type'] in enums.TIMESTAMP_EMBEDDED_PROPERTIES:
                for embed in enums.TIMESTAMP_EMBEDDED_PROPERTIES[obj['type']]:
                    if embed in obj:
                        for tprop in enums.TIMESTAMP_EMBEDDED_PROPERTIES[obj['type']][embed]:
                            if embed == 'extensions':
                                for ext in obj[embed]:
                                    if tprop in obj[embed][ext] and ts_re.match(obj[embed][ext][tprop]):
                                        try:
                                            parser.parse(obj[embed][ext][tprop])
                                        except ValueError as e:
                                            yield JSONError("'%s': '%s': '%s': '%s' is not a valid timestamp: %s"
                                                            % (obj['type'], ext, tprop, obj[embed][ext][tprop], str(e)), instance['id'])
                            elif tprop in obj[embed] and ts_re.match(obj[embed][tprop]):
                                try:
                                    parser.parse(obj[embed][tprop])
                                except ValueError as e:
                                    yield JSONError("'%s': '%s': '%s' is not a valid timestamp: %s"
                                                    % (obj['type'], tprop, obj[embed][tprop], str(e)), instance['id'])


def modified_created(instance):
    """`modified` property must be later or equal to `created` property
    """
    if 'modified' in instance and 'created' in instance and \
            instance['modified'] < instance['created']:
        msg = "'modified' (%s) must be later or equal to 'created' (%s)"
        return JSONError(msg % (instance['modified'], instance['created']),
                         instance['id'])


def object_marking_circular_refs(instance):
    """Ensure that marking definitions do not contain circular references (ie.
    they do not reference themselves in the `object_marking_refs` property).
    """
    if instance['type'] != 'marking-definition':
        return

    if 'object_marking_refs' in instance:
        for ref in instance['object_marking_refs']:
            if ref == instance['id']:
                yield JSONError("`object_marking_refs` cannot contain any "
                                "references to this marking definition object"
                                " (no circular references).", instance['id'])


def granular_markings_circular_refs(instance):
    """Ensure that marking definitions do not contain circular references (ie.
    they do not reference themselves in the `granular_markings` property).
    """
    if instance['type'] != 'marking-definition':
        return

    if 'granular_markings' in instance:
        for marking in instance['granular_markings']:
            if 'marking_ref' in marking and marking['marking_ref'] == instance['id']:
                yield JSONError("`granular_markings` cannot contain any "
                                "references to this marking definition object"
                                " (no circular references).", instance['id'])


def marking_selector_syntax(instance):
    """Ensure selectors in granular markings refer to items which are actually
    present in the object.
    """
    if 'granular_markings' not in instance:
        return

    list_index_re = re.compile(r"\[(\d+)\]")
    for marking in instance['granular_markings']:
        if 'selectors' not in marking:
            continue

        selectors = marking['selectors']
        for selector in selectors:
            segments = selector.split('.')

            obj = instance
            prev_segmt = None
            for segmt in segments:
                index_match = list_index_re.match(segmt)
                if index_match:
                    try:
                        idx = int(index_match.group(1))
                        obj = obj[idx]
                    except IndexError as e:
                        yield JSONError("'%s' is not a valid selector because"
                                        " %s is not a valid index."
                                        % (selector, idx), instance['id'])
                    except KeyError as e:
                        yield JSONError("'%s' is not a valid selector because"
                                        " '%s' is not a list."
                                        % (selector, prev_segmt), instance['id'])
                else:
                    try:
                        obj = obj[segmt]
                    except KeyError as e:
                        yield JSONError("'%s' is not a valid selector because"
                                        " %s is not a property."
                                        % (selector, e), instance['id'])
                    except TypeError as e:
                        yield JSONError("'%s' is not a valid selector because"
                                        " '%s' is not a property."
                                        % (selector, segmt), instance['id'])
                prev_segmt = segmt


def check_observable_refs(refs, obj_prop, enum_prop, embed_obj_prop, enum_vals,
                          key, instance):
    if embed_obj_prop != '':
        embed_obj_prop = "'" + embed_obj_prop + "' "

    if not isinstance(refs, list):
        refs = [refs]
    for ref in refs:
        try:
            refed_obj = instance['objects'][ref]
        except KeyError:
            yield JSONError("%s in observable object '%s' can't "
                            "resolve %sreference '%s'."
                            % (obj_prop, key, embed_obj_prop, ref),
                            instance['id'])
            continue
        try:
            refed_type = refed_obj['type']
        except KeyError:
            continue
        if refed_type not in enum_vals:
            if len(enum_vals) == 1:
                valids = "'" + enum_vals[0] + "'"
            else:
                valids = "'%s or '%s'" % ("', '".join(enum_vals[:-1]),
                                          enum_vals[-1])
            yield JSONError("'%s' in observable object '%s' must "
                            "refer to an object of type %s."
                            % (obj_prop, key, valids), instance['id'])


@cyber_observable_check
def observable_object_references(instance):
    """Ensure certain observable object properties reference the correct type
    of object.
    """
    for key, obj in instance['objects'].items():
        if 'type' not in obj:
            continue
        elif obj['type'] not in enums.OBSERVABLE_PROP_REFS:
            continue

        obj_type = obj['type']
        for obj_prop in enums.OBSERVABLE_PROP_REFS[obj_type]:
            if obj_prop not in obj:
                continue
            enum_prop = enums.OBSERVABLE_PROP_REFS[obj_type][obj_prop]
            if isinstance(enum_prop, list):
                refs = obj[obj_prop]
                enum_vals = enum_prop
                for x in check_observable_refs(refs, obj_prop, enum_prop, '',
                                               enum_vals, key, instance):
                    yield x

            elif isinstance(enum_prop, dict):
                for embedded_prop in enum_prop:
                    if isinstance(obj[obj_prop], dict):
                        if embedded_prop not in obj[obj_prop]:
                            continue
                        embedded_obj = obj[obj_prop][embedded_prop]
                        for embed_obj_prop in embedded_obj:
                            if embed_obj_prop not in enum_prop[embedded_prop]:
                                continue
                            refs = embedded_obj[embed_obj_prop]
                            enum_vals = enum_prop[embedded_prop][embed_obj_prop]
                            for x in check_observable_refs(refs, obj_prop, enum_prop,
                                                           embed_obj_prop, enum_vals,
                                                           key, instance):
                                yield x

                    elif isinstance(obj[obj_prop], list):
                        for embedded_list_obj in obj[obj_prop]:

                            if embedded_prop not in embedded_list_obj:
                                continue
                            embedded_obj = embedded_list_obj[embedded_prop]
                            refs = embedded_obj
                            enum_vals = enum_prop[embedded_prop]
                            for x in check_observable_refs(refs, obj_prop, enum_prop,
                                                           embedded_prop, enum_vals,
                                                           key, instance):
                                yield x


@cyber_observable_check
def artifact_mime_type(instance):
    """Ensure the 'mime_type' property of artifact objects comes from the
    Template column in the IANA media type registry.
    """
    for key, obj in instance['objects'].items():
        if ('type' in obj and obj['type'] == 'artifact' and 'mime_type' in obj):
            if enums.media_types():
                if obj['mime_type'] not in enums.media_types():
                    yield JSONError("The 'mime_type' property of object '%s' "
                                    "('%s') must be an IANA registered MIME "
                                    "Type of the form 'type/subtype'."
                                    % (key, obj['mime_type']), instance['id'])

            else:
                info("Can't reach IANA website; using regex for mime types.")
                mime_re = re.compile(r'^(application|audio|font|image|message|model'
                                     '|multipart|text|video)/[a-zA-Z0-9.+_-]+')
                if not mime_re.match(obj['mime_type']):
                    yield JSONError("The 'mime_type' property of object '%s' "
                                    "('%s') should be an IANA MIME Type of the"
                                    " form 'type/subtype'."
                                    % (key, obj['mime_type']), instance['id'])


@cyber_observable_check
def character_set(instance):
    """Ensure certain properties of cyber observable objects come from the IANA
    Character Set list.
    """
    char_re = re.compile(r'^[a-zA-Z0-9_\(\)-]+$')
    for key, obj in instance['objects'].items():
        if ('type' in obj and obj['type'] == 'directory' and 'path_enc' in obj):
            if enums.char_sets():
                if obj['path_enc'] not in enums.char_sets():
                    yield JSONError("The 'path_enc' property of object '%s' "
                                    "('%s') must be an IANA registered "
                                    "character set."
                                    % (key, obj['path_enc']), instance['id'])
            else:
                info("Can't reach IANA website; using regex for character_set.")
                if not char_re.match(obj['path_enc']):
                    yield JSONError("The 'path_enc' property of object '%s' "
                                    "('%s') must be an IANA registered "
                                    "character set."
                                    % (key, obj['path_enc']), instance['id'])

        if ('type' in obj and obj['type'] == 'file' and 'name_enc' in obj):
            if enums.char_sets():
                if obj['name_enc'] not in enums.char_sets():
                    yield JSONError("The 'name_enc' property of object '%s' "
                                    "('%s') must be an IANA registered "
                                    "character set."
                                    % (key, obj['name_enc']), instance['id'])
            else:
                info("Can't reach IANA website; using regex for character_set.")
                if not char_re.match(obj['name_enc']):
                    yield JSONError("The 'name_enc' property of object '%s' "
                                    "('%s') must be an IANA registered "
                                    "character set."
                                    % (key, obj['name_enc']), instance['id'])


@cyber_observable_check
def software_language(instance):
    """Ensure the 'language' property of software objects is a valid ISO 639-2
    language code.
    """
    for key, obj in instance['objects'].items():
        if ('type' in obj and obj['type'] == 'software' and
                'languages' in obj):
            for lang in obj['languages']:
                if lang not in enums.LANG_CODES:
                    yield JSONError("The 'languages' property of object '%s' "
                                    "contains an invalid ISO 639-2 language "
                                    " code ('%s')."
                                    % (key, lang), instance['id'])


def types_strict(instance):
    """Ensure that no custom object types are used, but only the official ones
    from the specification.
    """
    if instance['type'] not in enums.TYPES:
        yield JSONError("Object type '%s' is not one of those defined in the"
                        " specification." % instance['type'], instance['id'])

    if has_cyber_observable_data(instance):
        for key, obj in instance['objects'].items():
            if 'type' in obj and obj['type'] not in enums.OBSERVABLE_TYPES:
                yield JSONError("Observable object %s is type '%s' which is "
                                "not one of those defined in the "
                                "specification."
                                % (key, obj['type']), instance['id'])


def properties_strict(instance):
    """Ensure that no custom properties are used, but only the official ones
    from the specification.
    """
    if instance['type'] not in enums.TYPES:
        return  # only check properties for official objects

    defined_props = enums.PROPERTIES.get(instance['type'], [])
    for prop in instance.keys():
        if prop not in defined_props:
            yield JSONError("Property '%s' is not one of those defined in the"
                            " specification." % prop, instance['id'])

    if has_cyber_observable_data(instance):
        for key, obj in instance['objects'].items():
            type_ = obj.get('type', '')
            if type_ not in enums.OBSERVABLE_PROPERTIES:
                continue  # custom observable types handled outside this function
            observable_props = enums.OBSERVABLE_PROPERTIES.get(type_, [])
            embedded_props = enums.OBSERVABLE_EMBEDDED_PROPERTIES.get(type_, {})
            extensions = enums.OBSERVABLE_EXTENSIONS.get(type_, [])
            for prop in obj.keys():
                if prop not in observable_props:
                    yield JSONError("Property '%s' is not one of those defined in the"
                                    " specification for %s objects."
                                    % (prop, type_), instance['id'])
                # Check properties of embedded cyber observable types
                elif prop in embedded_props:
                    embedded_prop_keys = embedded_props.get(prop, [])
                    for embedded_key in obj[prop]:
                        if isinstance(embedded_key, dict):
                            for embedded in embedded_key:
                                if embedded not in embedded_prop_keys:
                                    yield JSONError("Property '%s' is not one of those defined in the"
                                                    " specification for the %s property in %s objects."
                                                    % (embedded, prop, type_), instance['id'])
                        elif embedded_key not in embedded_prop_keys:
                            yield JSONError("Property '%s' is not one of those defined in the"
                                            " specification for the %s property in %s objects."
                                            % (embedded_key, prop, type_), instance['id'])

            # Check properties of embedded cyber observable types
            for ext_key in obj.get('extensions', {}):
                if ext_key not in extensions:
                    continue  # don't check custom extensions
                extension_props = enums.OBSERVABLE_EXTENSION_PROPERTIES[ext_key]
                for ext_prop in obj['extensions'][ext_key]:
                    if ext_prop not in extension_props:
                        yield JSONError("Property '%s' is not one of those defined in the"
                                        " specification for the %s extension in %s objects."
                                        % (ext_prop, ext_key, type_), instance['id'])
                    embedded_ext_props = enums.OBSERVABLE_EXTENSION_EMBEDDED_PROPERTIES.get(ext_key, {}).get(ext_prop, [])
                    if embedded_ext_props:
                        for embed_ext_prop in obj['extensions'][ext_key].get(ext_prop, []):
                            if embed_ext_prop not in embedded_ext_props:
                                yield JSONError("Property '%s' in the %s property of the %s extension "
                                                "is not one of those defined in the specification."
                                                % (embed_ext_prop, ext_prop, ext_key), instance['id'])


def patterns(instance, options):
    """Ensure that the syntax of the pattern of an indicator is valid, and that
    objects and properties referenced by the pattern are valid.
    """
    if instance['type'] != 'indicator' or 'pattern' not in instance:
        return

    pattern = instance['pattern']
    if not isinstance(pattern, string_types):
        return  # This error already caught by schemas
    errors = pattern_validator(pattern)

    # Check pattern syntax
    if errors:
        for e in errors:
            yield PatternError(str(e), instance['id'])
        return

    type_format_re = re.compile(r'^\-?[a-z0-9]+(-[a-z0-9]+)*\-?$')
    property_format_re = re.compile(r'^[a-z0-9_]{3,250}$')

    p = Pattern(pattern)
    inspection = p.inspect().comparisons
    for objtype in inspection:
        # Check observable object types
        if objtype in enums.OBSERVABLE_TYPES:
            pass
        elif options.strict_types:
            yield PatternError("'%s' is not a valid STIX observable type"
                               % objtype, instance['id'])
        elif (not type_format_re.match(objtype) or
              len(objtype) < 3 or len(objtype) > 250):
            yield PatternError("'%s' is not a valid observable type name"
                               % objtype, instance['id'])
        elif (all(x not in options.disabled for x in ['all', 'format-checks', 'custom-prefix']) and
              not CUSTOM_TYPE_PREFIX_RE.match(objtype)):
            yield PatternError("Custom Observable Object type '%s' should start "
                               "with 'x-' followed by a source unique identifier "
                               "(like a domain name with dots replaced by "
                               "hyphens), a hyphen and then the name"
                               % objtype, instance['id'])
        elif (all(x not in options.disabled for x in ['all', 'format-checks', 'custom-prefix-lax']) and
              not CUSTOM_TYPE_LAX_PREFIX_RE.match(objtype)):
            yield PatternError("Custom Observable Object type '%s' should start "
                               "with 'x-'" % objtype, instance['id'])

        # Check observable object properties
        expression_list = inspection[objtype]
        for exp in expression_list:
            path = exp[0]
            # Get the property name without list index, dictionary key, or referenced object property
            prop = path[0]
            if objtype in enums.OBSERVABLE_PROPERTIES and prop in enums.OBSERVABLE_PROPERTIES[objtype]:
                continue
            elif options.strict_properties:
                yield PatternError("'%s' is not a valid property for '%s' objects"
                                   % (prop, objtype), instance['id'])
            elif not property_format_re.match(prop):
                yield PatternError("'%s' is not a valid observable property name"
                                   % prop, instance['id'])
            elif (all(x not in options.disabled for x in ['all', 'format-checks', 'custom-prefix']) and
                  not CUSTOM_PROPERTY_PREFIX_RE.match(prop)):
                yield PatternError("Cyber Observable Object custom property '%s' "
                                   "should start with 'x_' followed by a source "
                                   "unique identifier (like a domain name with "
                                   "dots replaced by underscores), an "
                                   "underscore and then the name"
                                   % prop, instance['id'])
            elif (all(x not in options.disabled for x in ['all', 'format-checks', 'custom-prefix-lax']) and
                  not CUSTOM_PROPERTY_LAX_PREFIX_RE.match(prop)):
                yield PatternError("Cyber Observable Object custom property '%s' "
                                   "should start with 'x_'" % prop, instance['id'])


def list_musts(options):
    """Construct the list of 'MUST' validators to be run by the validator.
    """
    validator_list = [
        timestamp,
        modified_created,
        object_marking_circular_refs,
        granular_markings_circular_refs,
        marking_selector_syntax,
        observable_object_references,
        artifact_mime_type,
        character_set,
        software_language,
        patterns
    ]

    # --strict-types
    if options.strict_types:
        validator_list.append(types_strict)

    # --strict-properties
    if options.strict_properties:
        validator_list.append(properties_strict)

    return validator_list
