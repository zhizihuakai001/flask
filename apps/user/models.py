from datetime import datetime

from ext import db


# 建表类
class User(db.Model):
    # db.Column(类型，约束) 映射表中的列
    '''
    类型
    db.Integer     int
    db.String(15)  varchar(15)
    db.DtaeTime    datetime
    '''
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    username = db.Column(db.String(12) , nullable=False)
    password = db.Column(db.String(12) , nullable=False)
    phone = db.Column(db.String(11) , unique=True)
    rdatetime = db.Column(db.DateTime , default=datetime.now)

    def __str__(self):
        return self.username
