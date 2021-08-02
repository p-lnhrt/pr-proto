from ...utils import names as n
from .tables import Table, TableLocationInformation
from ...filters import CategoricalColumnFilter

SALES_COLUMNS = [n.F_SALES_CHANNEL, n.F_DISTRIBUTION_CHANNEL, n.F_BRAND, n.F_YEAR_WEEK, n.F_SALES]
MASTER_PRODUCT_COLUMNS = [n.F_SALES_CHANNEL, n.F_DISTRIBUTION_CHANNEL]

sell_in_filters = [
    CategoricalColumnFilter(target_col=n.F_SALES_CHANNEL, retained_values=[n.V_ON_TRADE]),
]

SELL_IN_TABLE = Table(name="sell_in",
                      location_info=TableLocationInformation(local_file_name="sell_in.csv",
                                                             snowflake_table_name="SELL_IN_TABLE"),
                      columns=SALES_COLUMNS,
                      pushed_down_filters=sell_in_filters,
                      transformers=[])

SELL_OUT_TABLE = Table(name="sell_out",
                       location_info=TableLocationInformation(local_file_name="sell_out.csv",
                                                              snowflake_table_name="SELL_OUT_TABLE"),
                       columns=SALES_COLUMNS,
                       pushed_down_filters=[],
                       transformers=[])

MASTER_PRODUCT_COLUMNS = Table(name="master_product",
                               location_info=TableLocationInformation(local_file_name="master_product.csv",
                                                                      snowflake_table_name="MASTER_PRODUCT_TABLE"),
                               columns=MASTER_PRODUCT_COLUMNS,
                               pushed_down_filters=[],
                               transformers=[])
