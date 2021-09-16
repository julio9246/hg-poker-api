from py_postgresql_wrapper.configuration import Configuration
from py_postgresql_wrapper.database import Database

import source.commons.environment as environment

CONFIGURATION = Configuration(
    configuration_dict={
        'database': environment.DATABASE_NAME,
        'host': environment.DATABASE_HOST,
        'max_connection': environment.DATABASE_MAX_CONNECTION,
        'password': environment.DATABASE_PASSWORD,
        'port': environment.DATABASE_PORT,
        'print_sql': environment.DATABASE_PRINT_SQL,
        'username': environment.DATABASE_USERNAME
    }
)


def connect():
    return Database(CONFIGURATION)
