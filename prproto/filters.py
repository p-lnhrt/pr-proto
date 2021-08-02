import logging
from typing import Any, List

LOGGER = logging.getLogger()


# TODO: PushedDownOperation (assuming SQL query building is commutative)
# TODO: Kind of visitor class, not accept method implemented though.
class PushDownFilter:

    def __init__(self):
        self._table = None

    def set_table_reference(self, table):
        self._table = table
        return self

    def filter_dataframe(self) -> None:
        raise NotImplementedError

    def get_sql_query(self) -> str:
        raise NotImplementedError


class CategoricalColumnFilter(PushDownFilter):

    def __init__(self, target_col: str, retained_values: List[Any]):
        super().__init__()
        self.target_col = target_col
        self.retained_values = retained_values

    def filter_dataframe(self):
        df = self._table.data.copy()
        LOGGER.info(f"Filtering categorical column {self._table.name.upper()}.{self.target_col} "
                    f"(retained values: {', '.join(sorted(self.retained_values))})")
        self._table.data = df[df[self.target_col].isin(self.retained_values)]
        LOGGER.info(f"Filtered categorical column {self._table.name.upper()}.{self.target_col} "
                    f"from shape {df.shape} to shape {self._table.data.shape}")

    def get_sql_query(self):
        return f"WHERE {self.target_col} IN ({','.join(self.retained_values)})"
