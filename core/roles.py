from rolepermissions.roles import AbstractUserRole

class TestUser(AbstractUserRole):
    available_permissions = {
        "can_generate_boleto": True,
    } 

