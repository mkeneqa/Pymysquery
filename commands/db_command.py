from cleo import Command
from pymysquery.data.database import Database
import configparser
import pathlib
from pymysquery import MyDB


class DBStartCommand(Command):
    """
    DB Testing

    db_start

    """

    def handle(self):
        self.line("DB Start ...")
        db = MyDB()
        # db.connect(
        #     config.db_user="db_user",
        #     config.db_name="db_name",
        #
        # )
        db.config.host = ''
        # db = DB()
