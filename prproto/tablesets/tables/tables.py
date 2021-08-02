import logging
from typing import List

import pandas as pd

from ...source import TableLoader
from ...transformers import TableTransformer
from ...filters import PushDownFilter

LOGGER = logging.getLogger()


class TableLocationInformation:

    def __init__(self, local_file_name: str = None, snowflake_table_name : str = None):
        self._local_file_name = local_file_name
        self._snowflake_table_name = snowflake_table_name

    @property
    def local_file_name(self) -> str:
        if self._local_file_name:
            return self._local_file_name
        else:
            raise ValueError('No value is available for the "local_file_name" attribute')

    @local_file_name.setter
    def local_file_name(self, value):
        self._local_file_name = value

    @property
    def snowflake_table_name(self) -> str:
        if self._snowflake_table_name:
            return self._snowflake_table_name
        else:
            raise ValueError('No value is available for the "local_file_name" attribute')

    @snowflake_table_name.setter
    def snowflake_table_name(self, value):
        self._snowflake_table_name = value


class Table:

    def __init__(self,
                 name: str,
                 location_info: TableLocationInformation,
                 columns: List[str],  # Schema object
                 pushed_down_filters: List[PushDownFilter],
                 transformers: List[TableTransformer]):
        self.name = name
        self.columns = columns
        self.location_infos = location_info
        self.pushed_down_filters = [pd_filter.set_table_reference(table=self) for pd_filter in pushed_down_filters]
        self.transformers = [transformer.set_table_reference(table=self) for transformer in transformers]
        self.data = pd.DataFrame(columns=self.columns)

    def load(self, loader: TableLoader):
        loader.load(table=self)
        LOGGER.info(f"Loaded a DataFrame of shape {self.data.shape} into {self.__class__.__name__}")

    def transform(self):
        for transformer in self.transformers:
            transformer.transform()
