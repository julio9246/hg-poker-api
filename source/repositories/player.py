import math

from source.database import connect


class PlayerRepository:

    TABLE = 'player'

    def find_all(self):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'name',
                        'nick_name',
                        'phone_number',
                        'email',
                        'pass',
                        'description',
                        'photo')
                .where('active', True, operator='is')
                .order_by('name')
                .execute()
                .fetch_all()
            )

    def login(self, data):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'name',
                        'nick_name',
                        'phone_number',
                        'email',
                        'pass',
                        'description',
                        'photo')
                .where('email', data['email'], operator='=')
                .where('pass', data['pass'], operator='=')
                .where('active', True, operator='is')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                    .select(self.TABLE)
                    .fields('id',
                            'name',
                            'nick_name',
                            'phone_number',
                            'email',
                            'pass',
                            'description',
                            'photo')
                    .where('id', id, operator='=')
                    .where('active', True, operator='is')
                    .order_by('id')
                    .execute()
                    .fetch_one()
            )

    def find_by_email(self, email):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id')
                .where('email', email, operator='=')
                .execute()
                .fetch_one()
            )

    @staticmethod
    def save(name, nick_name, phone_number, email, password, description, photo, active):
        with connect() as connection:
            parameters = {
                'name': name,
                'nick_name': nick_name,
                'phone_number': phone_number,
                'email': email,
                'pass': password,
                'description': description,
                'photo': photo,
                'active': active
            }
            return (
                connection
                .execute('''
                    insert into player (
                        name, nick_name, phone_number, email, pass, description, photo, active
                    ) values (
                        %(name)s,
                        %(nick_name)s,
                        %(phone_number)s,
                        %(email)s,
                        %(pass)s,
                        %(description)s,
                        %(photo)s,
                        %(active)s
                    )
                    returning
                        *
                ''', parameters)
                .fetch_one()
            )

    def update(self, player_id, field, value):
        with connect() as connection:
            (
                connection
                .update(self.TABLE)
                .set(field, value)
                .where('id', player_id, operator='=')
                .execute()
            )

    def delete(self, player_id):
        with connect() as connection:
            (
                connection
                .delete(self.TABLE)
                .where('id', player_id, operator='=')
                .execute()
            )
