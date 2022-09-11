class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '41161704'
    MYSQL_DB = 'flask_api'

config = {
    'development': DevelopmentConfig
}