from source.exceptions.not_found import NotFoundException
from source.repositories.tournament import TournamentRepository
import source.commons.message as message


class TournamentBusiness:

    def __init__(self):
        self.tournament_repository = TournamentRepository()

    def find_all(self):
        result = self.tournament_repository.find_all()
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_by_id(self, field_id):
        result = self.tournament_repository.find_by_id(field_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def save(self, data):
        active = data.get('active') if data.get('active') else True
        return self.tournament_repository.save(
            data.get('name'),
            data.get('date_start'),
            data.get('date_end'),
            data.get('qtd_games'),
            data.get('qtd_players'),
            data.get('value_by_in'),
            data.get('value_rebuy'),
            data.get('value_total'),
            active
        )

    def update(self, field_id, data):
        if not self.tournament_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        for i in data:
            self.tournament_repository.update(field_id, i, data[i])
        return []

    def delete(self, field_id):
        if not self.tournament_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        self.tournament_repository.delete(field_id)
        return []
