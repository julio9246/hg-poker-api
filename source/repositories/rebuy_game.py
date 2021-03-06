import math

from source.database import connect


class RebuyGameRepository:

    TABLE = 'rebuy_game'

    def find_all(self):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'game_id',
                        'value')
                .execute()
                .fetch_all()
            )

    def get_report_by_game(self, game_id):
        comando = f""" select  p.id as player_id,
                            p.name as player_name,
                            p.photo as player_photo,
                            count(rg.player_id) as qtd_rebuy,
                            sum(rg.value) as value

                    from rebuy_game rg
                    inner join player p on p.id = rg.player_id
                    where rg.game_id = {game_id}
                    group by 1,2,3
                    order by 2
                """
        return connect().execute(comando, skip_load_query=True).fetch_all()

    def find_by_id(self, id):
        with connect() as connection:
            return (
                connection
                .select(self.TABLE)
                .fields('id',
                        'player_id',
                        'game_id',
                        'value')
                .where('id', id, operator='=')
                .order_by('id')
                .execute()
                .fetch_one()
            )

    @staticmethod
    def save(player_id, game_id, value):
        with connect() as connection:
            parameters = {
                'player_id': player_id,
                'game_id': game_id,
                'value': value
            }
            return (
                connection
                .execute('''
                    insert into rebuy_game (
                        player_id, game_id, value
                    ) values (
                        %(player_id)s,
                        %(game_id)s,
                        %(value)s
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
