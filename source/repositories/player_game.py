import math

from source.database import connect


class PlayerGameRepository:

    TABLE = 'player_game'

    def find_all(self):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'game_id',
                        'qtd_fichas',
                        'qtd_pontos',
                        'position')
                .execute()
                .fetch_all()
            )

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'game_id',
                        'qtd_fichas',
                        'qtd_pontos',
                        'position')
                .where('id', id, operator='=')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    def get_player_game_report(self, player_id):
        comando = f""" select to_char(pg.date, 'DD/MM/YYYY') as date,
                       g.game_number,
                       pg.qtd_pontos ,
                       pg.qtd_fichas,
                       pg."position"
                from player_game pg 
                inner join game g on g.id = pg.game_id
                where pg.player_id = {player_id}
                order by 1

                """
        return connect().execute(comando, skip_load_query=True).fetch_all()

    @staticmethod
    def save(player_id, game_id, qtd_fichas, qtd_pontos, position):
        with connect() as connection:
            parameters = {
                'player_id': player_id,
                'game_id': game_id,
                'qtd_fichas': qtd_fichas,
                'qtd_pontos': qtd_pontos,
                'position': position
            }
            return (
                connection
                .execute('''
                    insert into player_game (
                        player_id, game_id, qtd_fichas, qtd_pontos, position
                    ) values (
                        %(player_id)s,
                        %(game_id)s,
                        %(qtd_fichas)s,
                        %(qtd_pontos)s,
                        %(position)s
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
