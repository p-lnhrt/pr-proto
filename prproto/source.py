from pathlib import Path

import pandas as pd


class TableLoader:

    def __init__(self, config):
        pass

    def load(self, table):
        raise NotImplementedError


class LocalTableLoader(TableLoader):

    def __init__(self, config):
        super().__init__(config=config)
        self.target_dir = Path(config["target_dir"])

    def load(self, table):
        file_path = self.target_dir / table.location_infos.local_file_name
        table.data = pd.read_csv(file_path, sep=",", header=0)
        for pushed_down_filter in table.pushed_down_filters:
            pushed_down_filter.filter_dataframe()


class SnowflakeTableLoader(TableLoader):

    def __init__(self, config):
        super().__init__(config=config)
        # self.engine = build_db_engine(config=config)

    @staticmethod
    def build_query(table):
        # TODO: Would not make sense to move it to the Table class, wouldn't it ?
        query = f"FROM {table.snowflake_table_name} SELECT {','.join(table.columns)}"
        return ', '.join([query, *[pd_filter.get_sql_query() for pd_filter in table.pushed_down_filters]])

    def load(self, table):
        query = self.build_query(table=table)
        table.data = self.engine.execute(query)


