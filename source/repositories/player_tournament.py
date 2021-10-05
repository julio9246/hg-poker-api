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
                        'position',
                        'points_acum',
                        'adm')
                .execute()
                .fetch_all()
            )

    def get_ranking(self, tournament_id):

        comando = f""" select a.id as player_id,
                              a.photo,
                              a.name,
                              b.position,
                              d.name as tournament_name,
                              sum(b.qtd_pontos) as qtd_pontos
                       from player a
                       inner join player_game b on b.player_id = a.id
                       inner join game c on c.id = b.game_id     
                       inner join tournament d on d.id = c.tournament_id         
                       WHERE c.tournament_id = {tournament_id}  
                       GROUP BY 1,2,3,4,5
                       ORDER BY 4 
                    """
        return connect().execute(comando, skip_load_query=True).fetch_all()

    def get_player_tournament(self, data):
        comando = f""" select t.name as tournament_name,
                              pt.points_acum,
                              pt."position" ,
                              t.value_total 
                from player_tournament pt 
                inner join tournament t on pt.tournament_id = t.id 
                where t.id = {data['tournament_id']}
                and   pt.player_id = {data['player_id']}

                """
        return connect().execute(comando, skip_load_query=True).fetch_one()

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'tournament_id',
                        'position',
                        'points',
                        'adm')
                .where('id', id, operator='=')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    @staticmethod
    def save(player_id, tournament_id, position, points_acum, adm):
        with connect() as connection:
            parameters = {
                'player_id': player_id,
                'tournament_id': tournament_id,
                'position': position,
                'points_acum': points_acum,
                'adm': adm
            }
            return (
                connection
                .execute('''
                    insert into player_tournament (
                        player_id, tournament_id, position, points_acum, adm
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
