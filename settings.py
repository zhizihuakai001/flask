class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123LIyu_01!@43.138.164.129:3306/test'
    # SQLALCHEMY_DATEBASE_UGI = 'mysql+pymysql://root:password@127.0.0.1:3306/flask05'本机数据库连接方法



class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
