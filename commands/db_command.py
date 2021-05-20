from cleo import Command
from pymysquery.data.database import Database
import configparser
import pathlib
import config as creds
from pymysquery import MyDB


class DBStartCommand(Command):
    """
    DB Testing

    db_start

    """

    def handle(self):
        self.line("DB Start ...")
        db = MyDB(host=creds.HOST, db_name=creds.DB, db_user=creds.USER, db_passwd=creds.PASSWD)
        # eg: https://github.com/bluerelay/windyquery#select
        db.table('mytable').select('*').where('id', '=', 2)

        # SELECT * FROM mytable WHERE
        # db.table().select().where().equals()

        # db.connect(
        #     config.db_user="db_user",
        #     config.db_name="db_name"
        #
        # )
        # db.config.host = ''
        # db = DB()
