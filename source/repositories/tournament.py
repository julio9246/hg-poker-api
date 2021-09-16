import math

from source.database import connect


class TournamentRepository:

    TABLE = 'tournament'

    def find_all(self):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'name',
                        'date_start',
                        'date_end',
                        'qtd_games',
                        'qtd_players',
                        'value_buyin',
                        'value_rebuy',
                        'value_total',
                        'active')
                .where('active', True, operator='is')
                .order_by('name')
                .execute()
                .fetch_all()
            )

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'name',
                        'date_start',
                        'date_end',
                        'qtd_games',
                        'qtd_players',
                        'value_buyin',
                        'value_rebuy',
                        'value_total',
                        'active')
                .where('id', id, operator='=')
                .where('active', True, operator='is')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    @staticmethod
    def save(name, date_start, date_end, qtd_games, qtd_players, value_buyin, value_rebuy, value_total, active):
        with connect() as connection:
            parameters = {

                'name': name,
                'date_start': date_start,
                'date_end': date_end,
                'qtd_games': qtd_games,
                'qtd_players': qtd_players,
                'value_buyin': value_buyin,
                'value_rebuy': value_rebuy,
                'value_total': value_total,
                'active': active
            }
            return (
                connection
                .execute('''
                    insert into tournament (
                        name, date_start, date_end, qtd_games, qtd_players, value_buyin, value_rebuy, value_total,active
                    ) values (
                        %(name)s,
                        %(date_start)s,
                        %(date_end)s,
                        %(qtd_games)s,
                        %(qtd_players)s,
                        %(value_buyin)s,
                        %(value_rebuy)s,
                        %(value_total)s,
                        %(active)s,
                    )
                    returning
                        *
                ''', parameters)
                .fetch_one()
            )

    def update(self, tournament_id, field, value):
        with connect() as connection:
            (
                connection
                .update(self.TABLE)
                .set(field, value)
                .where('id', tournament_id, operator='=')
                .execute()
            )

    def delete(self, tournament_id):
        with connect() as connection:
            (
                connection
                .delete(self.TABLE)
                .where('id', tournament_id, operator='=')
                .execute()
            )
