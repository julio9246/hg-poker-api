import os

APPLICATION_DEBUG = os.environ.get('APPLICATION_DEBUG', True)
APPLICATION_HOST = os.environ.get('APPLICATION_HOST', '0.0.0.0')
APPLICATION_PORT = os.environ.get('APPLICATION_PORT', 5000)

AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')

DATABASE_HOST = os.environ.get('DATABASE_HOST', 'hgpoker.c13gml6mujwk.us-east-2.rds.amazonaws.com')
DATABASE_MAX_CONNECTION = os.environ.get('DATABASE_MAX_CONNECTION', 20)
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'hgpoker')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'pass-hgpoker')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 5432)
DATABASE_PRINT_SQL = os.environ.get('DATABASE_PRINT_SQL', True)
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME', 'postgres')

FLASK_ENV = os.environ.get('FLASK_ENV', 'development')