class Config (object):
    DEBUB = True

class DevelopmentConfig (Config):
    SQALCHEMY_ECHO = True

class ProductionConfig (Config):
    DEBUG = False

class TestingConfig (Config):
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}