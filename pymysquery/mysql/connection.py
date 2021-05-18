import pymysql
import pymysql.cursors
from prodict import Prodict


from ..connection_base import ConnectionBase
from ..builder.select_base import SelectBase

class _Config(Prodict):
    host: str
    port: int
    db_name: str
    db_user: str
    db_passwd: str
    charset: str
    cursor_class: any

    def init(self):
        self.cursor_class = None
        self.charset = 'utf8mb4'
        self.port = 3306

    def enable_dict_cursor(self):
        self.cursor_class = pymysql.cursors.DictCursor

    def is_ready(self):
        skip_cols = ['charset', 'cursor_class']
        for k, v in self.items():
            if k not in skip_cols:
                if v is None:
                    return False

        return True


class Connection(ConnectionBase):
    user_cursor_dictionary = False
    CONN = None
    config = _Config()

    # def __init__
    # (self, host='', port=3306, db_name='', db_user='', db_passwd='', charset='utf8mb4', enable_cursor=False):
    #     if host:
    #         self.config.host = host
    #
    #     if port:
    #         self.config.port = port
    #
    #     if db_name:
    #         self.config.db_name = db_name
    #
    #     if db_user:
    #         self.config.db_user = db_user
    #
    #     if db_passwd:
    #         self.config.passwd = db_passwd
    #
    #     self.config.charset = charset
    #     if enable_cursor:
    #         self.config.enable_dict_cursor()

    def connect(self):
        # TODO: implement config
        if self.config.is_ready():
            self.CONN = pymysql.connect(
                host=self.config.host,
                port=self.config.port,
                user=self.config.db_user,
                password=self.config.db_passwd,
                db=self.config.db_name,
                charset=self.config.charset
            )

            if self.config.cursor_class is not None:
                self.CONN.cursor(self.config.cursor_class)

            return self.CONN
        else:
            # TODO: Throw exception
            pass

    def connection_handler(self):
        pass

    def disconnect(self):
        pass
