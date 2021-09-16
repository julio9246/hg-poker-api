from source.schemas.validation import Validation


class GameSchema(Validation):

    @staticmethod
    def save():
        return{
            'tournament_id': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'game_number': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'localization': {
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'date_start': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'date_end': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'qtd_rebuy_limit': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'active': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'boolean'
            }
        }

    @staticmethod
    def update():
        return {
            'game_number': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'integer'
            },
            'localization': {
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'date_start': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'string'
            },
            'date_end': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'qtd_rebuy_limit': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'integer'
            },
            'active': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'boolean'
            }
        }
