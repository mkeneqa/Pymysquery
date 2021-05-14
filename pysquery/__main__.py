from cleo import Application
from pysquery.commands.hello_world_command import HelloWorldCommand

app = Application()
app.add(HelloWorldCommand())

if __name__ == '__main__':
    app.run()
