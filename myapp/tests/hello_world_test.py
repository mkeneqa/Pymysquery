# -*- coding: utf-8 -*-
import pytest
from cleo.application import Application
from cleo.testers import CommandTester
from myapp.commands.hello_world_command import HelloWorldCommand


def test_execute_hello_world_command():
    application = Application()
    application.add(HelloWorldCommand())
    command = application.find('greet')
    command_tester = CommandTester(command)
    command_tester.execute('Bob')

    assert "Hello Bob" == command_tester.io.fetch_output().rstrip()


def test_execute_hello_world_command_no_params():
    application = Application()
    application.add(HelloWorldCommand())
    command = application.find('greet')
    command_tester = CommandTester(command)
    command_tester.execute()
    assert "Hello" == command_tester.io.fetch_output().rstrip()
