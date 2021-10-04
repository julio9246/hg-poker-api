import math

from source.database import connect


class PlayerTournamentRepository:

    TABLE = 'player_tournament'

    def find_all(self):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'tournament_id',
                        'adm')
                .execute()
                .fetch_all()
            )

    def get_ranking(self, tournament_id):

        comando = f""" select a.photo,
                              a.name,
                              b.position,
                              sum(b.qtd_pontos) as qtd_pontos
                       from player a
                       inner join player_game b on b.player_id = a.id
                       inner join game c on c.id = b.game_id              
                       WHERE c.tournament_id = {tournament_id}  
                       GROUP BY 1,2,3
                       ORDER BY 3 
                    """
        return connect().execute(comando, skip_load_query=True).fetch_all()

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'tournament_id',
                        'adm')
                .where('id', id, operator='=')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    @staticmethod
    def save(player_id, tournament_id, adm):
        with connect() as connection:
            parameters = {
                'player_id': player_id,
                'tournament_id': tournament_id,
                'adm': adm
            }
            return (
                connection
                .execute('''
                    insert into player_tournament (
                        player_id, tournament_id, adm
                    ) values (
                        %(player_id)s,
                        %(tournament_id)s,
                        %(adm)s
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
