import abc


class ConnectionBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError("You should implement this!")