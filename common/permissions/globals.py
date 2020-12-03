from enum import Enum

PERMISSION_ACCESS = "access"
PERMISSION_ADD = "add"
PERMISSION_CHANGE = "change"
PERMISSION_DELETE = "delete"
PERMISSION_RETRIEVE = "retrieve"
PERMISSION_LIST = "list"


class PermissionSetAction(Enum):
    Read = 1
    Write = 2
    Access = 3
    Approve = 4

    # Pos specific actions
    POS_SaleOperations = 101
    POS_FavoriteOperations = 102
    POS_TerminalOperations = 103
    POS_OtherBranchStocks = 104
    POS_TerminalStatus = 106
    POS_Sales = 107
    POS_ReturnSale = 108
    POS_CancelSale = 109
    POS_SettingsAccess = 110
    POS_TransactionEdit = 111
    POS_CustomPriceEdit = 112

    DASH_TransactionEdit = 201


class PermissionSetGroup(Enum):
    User = 1  # Read/Write
    Professor = 2  # Read/Write
    Student = 3  # Read/Write


class PermissionSet:
    def __init__(self, group, actions):
        self.group = group
        self.actions = actions

    @staticmethod
    def access_perms():
        return [
            PermissionSet(PermissionSetGroup.Professor, [PermissionSetAction.Access]),
            PermissionSet(PermissionSetGroup.Student, [PermissionSetAction.Access])
        ]