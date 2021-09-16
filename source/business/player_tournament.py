from source.exceptions.not_found import NotFoundException
from source.repositories.player_tournament import PlayerTournamentRepository
import source.commons.message as message


class PlayerTournamentBusiness:

    def __init__(self):
        self.player_tournament_repository = PlayerTournamentRepository()

    def find_all(self):
        result = self.player_tournament_repository.find_all()
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_by_id(self, field_id):
        result = self.player_tournament_repository.find_by_id(field_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def save(self, data):
        return self.player_tournament_repository.save(
            data.get('player_id'),
            data.get('tournament_id'),
            data.get('adm')
        )

    def update(self, field_id, data):
        if not self.player_tournament_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        for i in data:
            self.player_tournament_repository.update(field_id, i, data[i])
        return []

    def delete(self, field_id):
        if not self.player_tournament_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        self.player_tournament_repository.delete(field_id)
        return []
