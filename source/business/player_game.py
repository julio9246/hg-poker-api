from source.exceptions.not_found import NotFoundException
from source.repositories.player_game import PlayerGameRepository
import source.commons.message as message


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
