from ..utils import names as n
from .tablesets import TableSet
from .tables import SELL_IN_TABLE, SELL_OUT_TABLE, MASTER_PRODUCT_COLUMNS

ON_TRADE_TABLE_SET = TableSet(tables=[SELL_IN_TABLE, SELL_OUT_TABLE, MASTER_PRODUCT_COLUMNS])
OFF_TRADE_TABLE_SET = TableSet(tables=[SELL_IN_TABLE, SELL_OUT_TABLE, MASTER_PRODUCT_COLUMNS])

# Idea: une the name attribute of the table set and a register decorator
TABLE_SET_REGISTRY = {
    n.V_ON_TRADE: ON_TRADE_TABLE_SET,
    n.V_OFF_TRADE: OFF_TRADE_TABLE_SET,
}


def get_table_set(key):
    try:
        table_set = TABLE_SET_REGISTRY[key]
    except KeyError:
        raise KeyError(f"No table set registered under the name '{key}'")
    return table_set
