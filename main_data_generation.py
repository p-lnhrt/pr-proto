from pathlib import Path

import pandas as pd
import numpy as np

NB_CHANNELS = 2
NB_DIS_CHANNELS_PER_CHANNEL = 2
NB_BRAND_PER_DIS_CHANNEL = 2
NB_YEAR_WEEK_PER_BRAND = 3
NB_ROWS_PER_DIS_CHANNEL = NB_BRAND_PER_DIS_CHANNEL * NB_YEAR_WEEK_PER_BRAND
NB_ROWS_PER_CHANNEL = NB_DIS_CHANNELS_PER_CHANNEL * NB_ROWS_PER_DIS_CHANNEL
NB_ROWS_TOTAL = NB_CHANNELS * NB_ROWS_PER_CHANNEL

DATA_DIR = Path("./data")

if __name__ == "__main__":

    sales_df = pd.DataFrame(data=
    {"sales_channel": ["on_trade"]*NB_ROWS_PER_CHANNEL +
                      ["off_trade"]*NB_ROWS_PER_CHANNEL,
     "distribution_channel": ["BA"]*NB_ROWS_PER_DIS_CHANNEL +
                             ["RS"]*NB_ROWS_PER_DIS_CHANNEL +
                             ["RE"]*NB_ROWS_PER_DIS_CHANNEL +
                             ["SM"]*NB_ROWS_PER_DIS_CHANNEL,
     "brand": (["absolut"]*NB_YEAR_WEEK_PER_BRAND +
               ["absolut"]*NB_YEAR_WEEK_PER_BRAND)*NB_DIS_CHANNELS_PER_CHANNEL*NB_CHANNELS,
     "year_week": [201905, 201906, 201907]*NB_BRAND_PER_DIS_CHANNEL*NB_DIS_CHANNELS_PER_CHANNEL*NB_CHANNELS,
     "sales": np.random.rand(NB_ROWS_TOTAL),
     })

    master_product_df = pd.DataFrame(data={
        "sales_channel": ['on_trade', 'off_trade', 'off_trade'],
        "distribution_channel": ["BA", "RE", "SM"],
    })

    for df, file_name in zip([sales_df, sales_df, master_product_df],
                             ["sell_out.csv", "sell_in.csv", "master_product.csv"]):
        file_path = DATA_DIR / file_name
        df.to_csv(file_path, sep=",", index=False, header=True)
