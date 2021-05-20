from ..builder.select_base import SelectBase
from ..builder.crud_base import CrudBase


class Select(SelectBase, CrudBase):

    def select(self, coloumns: str):
        return self

    def where(self):
        return self

    def where_in(self):
        return self

    def or_where(self):
        return self

    def table(self, name: str):
        return self

    def limit(self):
        return self

    def offset(self):
        return self

    def order_by(self):
        return self

    def group_by(self):
        pass

    def join(self):
        pass

    def build_select(self):
        pass
