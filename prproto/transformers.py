class TableTransformer:

    def __init__(self):
        self._table = None

    def set_table_reference(self, table):
        self._table = table
        return self

    def transform(self):
        raise NotImplementedError
