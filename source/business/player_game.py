from source.exceptions.not_found import NotFoundException
from source.repositories.player_game import PlayerGameRepository
import source.commons.message as message
from source.utils.utils import remove_duplicated_data_from_array


class PlayerGameBusiness:

    def __init__(self):
        self.player_game_repository = PlayerGameRepository()

    def find_all(self):
        result = self.player_game_repository.find_all()
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_by_id(self, field_id):
        result = self.player_game_repository.find_by_id(field_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def get_player_game_report(self, data):
        result = self.player_game_repository.get_player_game_report(data['player_id'])
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def game_report(self, tournament_id):
        result = self.player_game_repository.game_report(tournament_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def game_report_by_game_id(self, game_id):
        result = self.player_game_repository.game_report_by_game_id(game_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def game_report_by_tournament_id(self, tournament_id):
        result = self.player_game_repository.game_report_by_tournament_id(tournament_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)

        dic = []
        for r in result:
            dic.append({
                'game_number': r.get('game_number'),
                'date': r.get('date'),
                'game_data': []
            })
        dic = list(remove_duplicated_data_from_array(dic))

        key = 0
        for r in result:
            for d in dic:
                if r.get('game_number') == d.get('game_number') and r.get('date') == d.get('date'):
                    key += 1
                    d.get('game_data').append(
                        {
                            'id': key,
                            'player_name': r.get('player_name'),
                            'player_photo': r.get('player_photo'),
                            'player_qtd_pontos': r.get('player_qtd_pontos'),
                            'player_position': r.get('player_position')
                        }
                    )

        return dic

    def save(self, data):
        return self.player_game_repository.save(
            data.get('player_id'),
            data.get('game_id'),
            data.get('qtd_fichas'),
            data.get('qtd_pontos'),
            data.get('position')
        )

    def update(self, field_id, data):
        if not self.player_game_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        for i in data:
            self.player_game_repository.update(field_id, i, data[i])
        return []

    def delete(self, field_id):
        if not self.player_game_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        self.player_game_repository.delete(field_id)
        return []
