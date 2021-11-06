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

    def get_list_all_tournament_by_player_id(self,player_id):
        comando = f""" select t.id,
                              t.name,
                              to_char(t.date_start, 'DD/MM/YYYY') as initial_date,
                              to_char(t.date_end, 'DD/MM/YYYY') as final_date,
                              case
                              when t.date_end > 'today'
                              then 'ABERTO'
                              else 'FECHADO' end as status
                from tournament t   
                inner join player_tournament pt on pt.tournament_id = t.id
                where pt.player_id = {player_id}
                """
        return connect().execute(comando, skip_load_query=True).fetch_all()

    def get_all_tournament_by_id(self, id):
        comando = f""" select t.id,
                              t.name,                              
                              pt.player_id as player_id_adm,
                              to_char(t.date_start, 'DD/MM/YYYY') as initial_date,
                              to_char(t.date_end, 'DD/MM/YYYY') as final_date,
                              case
                              when t.date_end > 'today'
                              then 'ABERTO'
                              else 'FECHADO' end as status,
                              t.qtd_games ,
                              t.qtd_players ,
                              t.value_buyin , 
                              t.value_total as value_total_initial,
                              sum(rg.value) as value_rebuy_total,
                              t.value_total + sum(rg.value) as value_total_final
                        from tournament t    
                        inner join player_tournament pt on pt.tournament_id = t.id and pt.adm = true 
                        inner join game g on g.tournament_id = t.id 
                        inner join rebuy_game rg on rg.game_id = g.id 
                        where t.id = {id}
                        group by 1,2,3,4,5,6,7,8,9,10
                """
        return connect().execute(comando, skip_load_query=True).fetch_all()

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
