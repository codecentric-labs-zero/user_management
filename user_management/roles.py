from rolepermissions.roles import AbstractUserRole


class LeadRecruiter(AbstractUserRole):
    available_permissions = {
        'create_new_users': {
            'default': True,
            # label option is not implemented
            # in admin section permission's name is not visible
            # 'label': 'Create new users'
        },
        'view_recruitment_page': {
            'default': True,
            # 'label': 'View recruitment page'
        },
    }


class Recruiter(AbstractUserRole):
    available_permissions = {
        'view_recruitment_page': {
            'default': True,
            # 'label': 'View recruitment page'
        },
    }
