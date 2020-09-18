from typing import Dict

import numpy as np
import pandas as pd

COLUMN_NAMES = ['Instrument', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Open Interest']
OHLC_CONVERSION_DICT: Dict[str, str] = {'Open': 'first',
                       'High': 'max',
                       'Low': 'min',
                       'Close': 'last',
                       'Volume': 'sum',
                       'Open Interest': 'last'}


def load_data(csv_file_path):
    min1_data = pd.read_csv(csv_file_path, header=None, index_col=None,
                            names=COLUMN_NAMES,
                            parse_dates=[['Date', 'Time']])
    # instrument_name = min1_data['Instrument'].unique()[0]
    min1_data.drop('Instrument', axis=1, inplace=True)
    min1_data.set_index('Date_Time', inplace=True)
    return min1_data


def convert_to_15min(min1_data):
    min15_data = min1_data.resample('15min', origin='start').agg(OHLC_CONVERSION_DICT)
    min15_data.dropna(how='any', inplace=True)
    return min15_data


def convert_to_75min(min1_data):
    min15_data = convert_to_15min(min1_data)
    index_dates = pd.Series(np.unique(min15_data.index.date))
    list_of_min75_data_by_date = []
    for idx_date in index_dates:
        idx_date_str = idx_date.strftime(format='%Y-%m-%d')
        min75_data_by_date = min15_data[idx_date_str].resample('75Min', origin='start').agg(OHLC_CONVERSION_DICT)
        list_of_min75_data_by_date.append(min75_data_by_date)

    min75_data = pd.concat(list_of_min75_data_by_date)
    return min75_data
