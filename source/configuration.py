import source.commons.environment as environment


class Configuration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfiguration(Configuration):

    DEBUG = True
    TESTING = False


class ProductionConfiguration(Configuration):

    DEBUG = False
    TESTING = False


class TestingConfiguration(Configuration):

    DEBUG = False
    TESTING = True


configuration = {
    'development': DevelopmentConfiguration,
    'production': ProductionConfiguration,
    'testing': TestingConfiguration
}
