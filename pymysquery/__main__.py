from cleo import Application
from commands import HelloWorldCommand

app = Application()
app.add(HelloWorldCommand())

if __name__ == '__main__':
    app.run()
