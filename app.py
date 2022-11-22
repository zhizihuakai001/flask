from flask_migrate import Migrate # 命令
from flask_script import Manager # 管理命令
from apps.user.models import User
from apps import create_app
from ext import db

app = create_app()

# 创建脚本管理对象
manager = Manager(app)

# 让迁移时，app 和 db 建立联系
migrate = Migrate(app , db)

# 将数据迁移的脚本，命令添加到脚本管理器
# manager.add_command('db', MigrateCommand)


@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
