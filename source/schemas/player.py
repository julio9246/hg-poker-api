from source.schemas.validation import Validation


class PlayerSchema(Validation):

    @staticmethod
    def save():
        return {
            'name': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'nick_name': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'phone_number': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'email': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'pass': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'description': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'photo': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'active': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'boolean'
            }
        }

    @staticmethod
    def update():
        return {
            'name': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'nick_name': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'phone_number': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'pass': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'description': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'photo': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'active': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'boolean'
            }
        }
