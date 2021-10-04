from source.exceptions.not_found import NotFoundException
from source.repositories.player import PlayerRepository
import source.commons.message as message


class PlayerBusiness:

    def __init__(self):
        self.player_repository = PlayerRepository()

    def find_all(self):
        result = self.player_repository.find_all()
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def login(self, data):
        result = self.player_repository.login(data)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)

        payload = {
            'logado': True
        }
        self.update(result.id, payload)

        return result

    def logout(self, email):
        result = self.player_repository.logout(email)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)

        payload = {
            'logado': False
        }
        self.update(result.id, payload)

        return result

    def find_by_id(self, player_id):
        result = self.player_repository.find_by_id(player_id)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_by_email(self, email):
        result = self.player_repository.find_by_email(email)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def find_by_nick_name(self, nick_name):
        result = self.player_repository.find_by_nick_name(nick_name)
        if not result:
            raise NotFoundException(None, message.REGISTER_NOT_FOUND)
        return result

    def save(self, data):

        if self.player_repository.find_by_email(data.get('email')):
            return {'error': message.REGISTER_ALREADY_EXIST}
        active = data.get('active') if data.get('active') else True
        return self.player_repository.save(
            data.get('name'),
            data.get('nick_name'),
            data.get('phone_number'),
            data.get('email'),
            data.get('pass'),
            data.get('description'),
            data.get('photo'),
            active,
            True,
        )

    def update(self, field_id, data):
        if not self.player_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        for i in data:
            self.player_repository.update(field_id, i, data[i])
        return []

    def delete(self, field_id):
        if not self.player_repository.find_by_id(field_id):
            raise NotFoundException(None, message.PLAYER_NOT_FOUND)
        self.player_repository.delete(field_id)
        return []
