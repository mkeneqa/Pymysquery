import abc
import contextlib


class ConnectionBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError("You should implement this!")

    @contextlib.contextmanager
    def connection_handler(self):
        # implement context manager
        pass
