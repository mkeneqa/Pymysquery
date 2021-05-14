import abc


class CrudBase(metaclass=abc.ABCMeta):
    def table(self):
        return self

    def where(self):
        return self

    def returning(self):
        return None

    def build_select(self):
        return None

    def build_update(self):
        return None

    def build_insert(self):
        return None

    def build_delete(self):
        return None

    def build_crud(self):
        pass
