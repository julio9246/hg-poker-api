from source.schemas.validation import Validation


class RebuyGameSchema(Validation):

    @staticmethod
    def save():
        return{
            'player_id': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'game_id': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'integer'
            },
            'value': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            }
        }

    @staticmethod
    def update():
        return {
            'value': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            }
        }
