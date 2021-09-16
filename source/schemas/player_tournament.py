from source.schemas.validation import Validation


class PlayerTournamentSchema(Validation):

    @staticmethod
    def save():
        return{
            'player_id': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'tournament_id': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'adm': {
                'empty': False,
                'nullable': False,
                'required': True,
                'type': 'boolean'
            }
        }

    @staticmethod
    def update():
        return {
            'player_id': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'integer'
            },
            'tournament_id': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'integer'
            },
            'adm': {
                'empty': False,
                'nullable': False,
                'required': False,
                'type': 'boolean'
            }
        }
