import pymysql
import pymysql.cursors
from prodict import Prodict

from ..connection_base import ConnectionBase


class Config(Prodict):
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

    def enable_dict_cursor(self):
        self.cursor_class = pymysql.cursors.DictCursor


class MyDB(ConnectionBase):
    user_cursor_dictionary = False
    CONN = None

    def connect(self):
        # TODO: implement config
        config = Config()
        if self.user_cursor_dictionary:
            self.CONN = pymysql.connect(
                host=config.host,
                port=config.port,
                user=config.db_user,
                password=config.db_passwd,
                db=config.db_name,
                charset=config.charset
            )

            if config.cursor_class is not None:
                self.CONN.cursor(config.cursor_class)

    def connection_handler(self):
        pass

    def disconnect(self):
        pass
