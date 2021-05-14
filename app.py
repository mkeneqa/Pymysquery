from cleo import Application
import logging
from pysquery.commands import hello_world_command,build_schema_command

tasks = [
    hello_world_command.HelloWorldCommand(),
    build_schema_command.BuildSchemaCommand()
]

app = Application()
for task in tasks:
    app.add(task)

if __name__ == '__main__':
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG,
        format="%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s"
    )
    app.run()

