# -*- coding:utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save, pre_save
from .models import Trash, ExcelTask, VersionHistory
from django.forms.models import model_to_dict
from django.contrib.contenttypes.models import ContentType
from . import signals


@receiver(pre_delete, sender=None)
def save_object_to_trash(sender, **kwargs):
    if sender == Trash:
        return
    instance = kwargs['instance']
    if not hasattr(instance, "id"):
        return
    ctype = ContentType.objects.get_for_model(instance)
    id = instance.id
    name = unicode(instance)
    Trash.objects.update_or_create(
        content_type=ctype,
        object_id=id,
        defaults=dict(
            object_name=name,
            json_data=model_to_dict(instance)
        )
    )


@receiver(signals.to_save_version, sender=None)
def save_object_to_version_history(sender, **kwargs):
    if sender == VersionHistory:
        return
    instance = kwargs['instance']
    exclude_fields = kwargs.get("exclude_fields", [])
    if not hasattr(instance, "id") or instance.id is None:
        return
    ctype = ContentType.objects.get_for_model(instance)
    id = instance.id
    name = unicode(instance)
    data = model_to_dict(instance, exclude=exclude_fields)
    vo = VersionHistory.objects.filter(content_type=ctype, object_id=id).order_by("-version").first()
    if vo:
        if vo.json_data == data:
            return
        version = vo.version + 1
    else:
        version = 1

    VersionHistory.objects.create(
        content_type=ctype,
        object_id=id,
        version=version,
        object_name=name,
        json_data=data
    )


@receiver(post_save, sender=ExcelTask)
def start_excel_task(sender, **kwargs):
    instance = kwargs['instance']
    if instance.status == 0:
        instance.status = 1
        from .tasks import dump_excel_task
        dump_excel_task.delay(instance.id)
        instance.save()
