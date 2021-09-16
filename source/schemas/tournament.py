from source.schemas.validation import Validation


class TournamentSchema(Validation):

    @staticmethod
    def save():
        return {
            'name': {
                'empty': False,
                'nullable': False,
                'required': True,
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
            'qtd_games': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'qtd_players': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'value_by_in': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            },
            'value_rebuy': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            },
            'value_total': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
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
            'name': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'date_start': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'date_end': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'string'
            },
            'qtd_games': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'integer'
            },
            'qtd_players': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'integer'
            },
            'value_by_in': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'float'
            },
            'value_rebuy': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'float'
            },
            'value_total': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'float'
            },
            'active': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'boolean'
            }
        }
