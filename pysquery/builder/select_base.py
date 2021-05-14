import abc


class SelectBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def select(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def limit(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def offset(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def order_by(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def group_by(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def join(self):
        raise NotImplementedError("You should implement this!")

    @abc.abstractmethod
    def build_select(self):
        raise NotImplementedError("You should implement this!")
