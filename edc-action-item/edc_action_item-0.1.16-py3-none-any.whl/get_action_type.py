from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from .create_or_update_action_type import create_or_update_action_type


def get_action_type(cls, name=None):
    """Returns the ActionType model instance.
    """
    try:
        action_type = cls.action_type_model_cls().objects.get(name=name or cls.name)
    except ObjectDoesNotExist:
        action_type = create_or_update_action_type(**cls.as_dict())
    else:
        # update attrs on existing ActionType instance
        # for this cls.
        axction_type_model_cls = django_apps.get_model(
            'edc_action_item.actiontype')
        fields = [f.name for f in axction_type_model_cls._meta.fields]
        opts = {k: v for k, v in cls.as_dict().items() if k in fields}
        try:
            action_type = cls.action_type_model_cls().objects.get(**opts)
        except ObjectDoesNotExist:
            for k, v in opts.items():
                setattr(action_type, k, v)
            action_type.save()
    return action_type
