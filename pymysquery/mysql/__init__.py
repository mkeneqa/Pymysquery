from .connection import Connection
from .select import Select
from .crud import Crud


class DB(Select, Crud):

    def __init__(self, host='', port=3306, db_name='', db_user='', db_passwd='', charset='utf8mb4',
                 enable_cursor=False):
        self.db = Connection()
        self.db.config.host = host
        self.db.config.db_name = db_name
        self.db.config.db_user = db_user
        self.db.config.db_passwd = db_passwd
        self.db.config.port = port
        self.db.config.charset = charset
        if enable_cursor:
            self.db.config.enable_dict_cursor()

        self.db.connect()
