import math

from source.database import connect


class GameRepository:

    TABLE = 'game'

    def find_all(self):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'tournament_id',
                        'game_number',
                        'localization',
                        'date_start',
                        'date_end',
                        'qtd_rebuy_limit')
                .execute()
                .fetch_all()
            )

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'tournament_id',
                        'game_number',
                        'localization',
                        'date_start',
                        'date_end',
                        'qtd_rebuy_limit')
                .where('id', id, operator='=')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    @staticmethod
    def save(tournament_id, game_number, localization, date_start, date_end, qtd_rebuy_limit):
        with connect() as connection:
            parameters = {
                'tournament_id': tournament_id,
                'game_number': game_number,
                'localization': localization,
                'date_start': date_start,
                'date_end': date_end,
                'qtd_rebuy_limit': qtd_rebuy_limit
            }
            return (
                connection
                .execute('''
                    insert into game (
                        tournament_id, game_number, localization, date_start, date_end, qtd_rebuy_limit
                    ) values (
                        %(tournament_id)s,
                        %(game_number)s,
                        %(localization)s,
                        %(date_start)s,
                        %(date_end)s,
                        %(qtd_rebuy_limit)s 
                    )
                    returning
                        *
                ''', parameters)
                .fetch_one()
            )

    def update(self, field_id, field, value):
        with connect() as connection:
            (
                connection
                .update(self.TABLE)
                .set(field, value)
                .where('id', field_id, operator='=')
                .execute()
            )

    def delete(self, field_id):
        with connect() as connection:
            (
                connection
                .delete(self.TABLE)
                .where('id', field_id, operator='=')
                .execute()
            )
