from cleo import Command
from pysquery.data.database import Database
import configparser
import pathlib


class DbActionCommand(Command):
    """
    Will Build Sample Database Schema

    go_build

    """

    def handle(self):