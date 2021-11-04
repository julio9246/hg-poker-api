from source.exceptions.not_found import NotFoundException
from source.repositories.rebuy_game import RebuyGameRepository
import source.commons.message as message


class RebuyGameBusiness:

    def __init__(self):
        self.rebuy_game_repository = RebuyGameRepository()

    def find_all(self):
        result = self.rebuy_game_repository.find_all()
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def get_report_by_game(self, game_id):
        result = self.rebuy_game_repository.get_report_by_game(game_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)

        total = 0
        for r in result:
            total = total + r['value']

        for r in result:
            r['total'] = total

        return result

    def find_by_id(self, field_id):
        result = self.rebuy_game_repository.find_by_id(field_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def save(self, data):
        return self.rebuy_game_repository.save(
            data.get('player_id'),
            data.get('game_id'),
            data.get('value')
        )

    def update(self, field_id, data):
        if not self.rebuy_game_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        for i in data:
            self.rebuy_game_repository.update(field_id, i, data[i])
        return []

    def delete(self, field_id):
        if not self.rebuy_game_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        self.rebuy_game_repository.delete(field_id)
        return []
