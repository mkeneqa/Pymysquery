from ..builder.select_base import SelectBase
from ..builder.crud_base import CrudBase


class Select(SelectBase, CrudBase):
    def select(self):
        pass

    def limit(self):
        pass

    def offset(self):
        pass

    def order_by(self):
        pass

    def group_by(self):
        pass

    def join(self):
        pass

    def build_select(self):
        pass
