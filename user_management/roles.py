from rolepermissions.roles import AbstractUserRole


class LeadRecruiter(AbstractUserRole):
    available_permissions = {
        'create_new_users': True,
        'view_recruitment_page': True,
    }

    def __str__(self):
        return "Lead rectruiter"


class Recruiter(AbstractUserRole):
    available_permissions = {
        'view_recruitment_page': True,
    }

    def __str__(self):
        return "Rectruiter"
