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
        db = MyDB()
        # db = DB()
