from cleo import Command
from pysquery.data.database import Database
import configparser
import pathlib
from pysquery import MyDB


class DBStartCommand(Command):
    """
    DB Testing

    db_start

    """

    def handle(self):
        self.line("DB Start ...")
        config = MyConfig()
        db = MyDB()
        # db.connect(
        #     config.db_user="db_user",
        #     config.db_name="db_name",
        #
        # )
        db.config.host = ''
        # db = DB()
