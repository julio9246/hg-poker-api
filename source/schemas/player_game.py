from source.schemas.validation import Validation


class PlayerGameSchema(Validation):

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
            'qtd_fichas': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            },
            'qtd_pontos': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            },
            'position': {
                'min': 0,
                'nullable': False,
                'required': True,
                'type': 'float'
            }
        }

    @staticmethod
    def update():
        return {
            'qtd_fichas': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'float'
            },
            'qtd_pontos': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'float'
            },
            'position': {
                'min': 0,
                'nullable': False,
                'required': False,
                'type': 'float'
            }
        }
