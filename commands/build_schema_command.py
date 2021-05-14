from cleo import Command
from pysquery.data.database import Database
import configparser
import pathlib


class BuildSchemaCommand(Command):
    """
    Will Build Sample Database Schema

    go_build

    """

    def handle(self):
        config = configparser.RawConfigParser()

        project_dir = pathlib.Path.cwd()
        config.read(f'{project_dir}/config.txt')
        host = config.get('database', 'host')
        port = config.get('database', 'port')
        user = config.get('database', 'user')
        password = config.get('database', 'password')
        db = config.get('database', 'db')

        _db = Database(
            the_db=db,
            the_host=host,
            the_passwd=password,
            the_port=port,
            the_user=user
        )

        table = [
            "name VARCHAR(20)",
            "birth DATE",
            "SIN INT(10)"
        ]
        _db.CreateTable(table_name='TestTable', table_cols=table)
        _db.InsertTableValues(db_table='TestTable',
                              cols=['`name`', '`birth`', '`SIN`'],
                              vals=['Ericcson', '1976-05-31', 1425],
                              verbose_print=True)

        _db.InsertDictionaryValues('TestTable', {
            '`name`': 'Jeremiah',
            '`birth`': '1980-04-10',
            '`SIN`': 9890
        }, verbose_print=True)

        # _db.TruncateTable('TestTable')
        # _db.DropTable('TestTable')

        # _db = Database(
        #
        # )
        # name = self.argument('name')

        # if name:
        #     text = 'Hello {}'.format(name)
        # else:
        #     text = 'Hello'
        #
        # if self.option('yell'):
        #     text = text.upper()

        self.line("Go Build!")
