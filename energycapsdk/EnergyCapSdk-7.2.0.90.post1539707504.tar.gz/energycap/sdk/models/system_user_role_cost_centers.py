# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SystemUserRoleCostCenters(Model):
    """SystemUserRoleCostCenters.

    :param view:
    :type view: bool
    :param create:
    :type create: bool
    :param edit:
    :type edit: bool
    :param delete:
    :type delete: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
        'create': {'key': 'create', 'type': 'bool'},
        'edit': {'key': 'edit', 'type': 'bool'},
        'delete': {'key': 'delete', 'type': 'bool'},
    }

    def __init__(self, view=None, create=None, edit=None, delete=None):
        super(SystemUserRoleCostCenters, self).__init__()
        self.view = view
        self.create = create
        self.edit = edit
        self.delete = delete
