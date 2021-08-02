from typing import List

from .tables import Table
from ..source import TableLoader


class TableSet:

    def __init__(self, tables: List[Table]):
        self._table_registry = {table.name: table for table in tables}

    def get_table(self, name: str) -> Table:
        try:
            table = self._table_registry[name]
        except KeyError:
            raise ValueError(f"Table '{name}' is not registered within the table set")
        return table

    def load(self, loader: TableLoader):
        for table in self._table_registry.values():
            table.load(loader=loader)


