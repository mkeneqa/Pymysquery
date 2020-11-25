from cleo import Command
from myapp.data.database import Database
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



        # config.read()

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
