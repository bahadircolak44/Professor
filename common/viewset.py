from common.permissions.globals import PERMISSION_RETRIEVE, PERMISSION_LIST, PERMISSION_ADD, PERMISSION_CHANGE, \
    PERMISSION_DELETE, PermissionSetAction, PermissionSet


class BaseViewSet:
    permission_set_group = None

    @classmethod
    def get_permission_sets(cls):
        '''
        default get_permissions method which will be used for auto creating PermissionSet data.
        You can override this method for custom permissions
        :return: dict
        '''
        if not cls.permission_set_group:
            raise Exception("permission_group is not defined for %s" % cls.__class__)

        return {
            PERMISSION_RETRIEVE: [PermissionSet(cls.permission_set_group, [PermissionSetAction.Read])],
            PERMISSION_LIST: [PermissionSet(cls.permission_set_group, [PermissionSetAction.Read])],

            PERMISSION_ADD: [PermissionSet(cls.permission_set_group, [PermissionSetAction.Write])],
            PERMISSION_CHANGE: [PermissionSet(cls.permission_set_group, [PermissionSetAction.Write])],
            PERMISSION_DELETE: [PermissionSet(cls.permission_set_group, [PermissionSetAction.Write])]
        }

