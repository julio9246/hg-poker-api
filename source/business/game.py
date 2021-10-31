from source.exceptions.not_found import NotFoundException
from source.repositories.game import GameRepository
import source.commons.message as message
from source.schemas import tournament


class GameBusiness:

    def __init__(self):
        self.game_repository = GameRepository()

    def find_all(self):
        result = self.game_repository.find_all()
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_by_id(self, field_id):
        result = self.game_repository.find_by_id(field_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_game_by_tournament(self, tournament_id):
        result = self.game_repository.find_game_by_tournament(tournament_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def save(self, data):
        return self.game_repository.save(
            data.get('player_id'),
            data.get('tournament_id'),
            data.get('adm')
        )

    def update(self, field_id, data):
        if not self.game_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        for i in data:
            self.game_repository.update(field_id, i, data[i])
        return []

    def delete(self, field_id):
        if not self.game_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        self.game_repository.delete(field_id)
        return []
