import pandas as pd
import trade
import execution

TEST_DATA_FILE_1 = './data/ICBK Historical Data.csv'


def load_data(data_file_path):
    data = pd.read_csv(data_file_path, index_col=0, parse_dates=True).sort_index()
    print(data)
    return data


def test_execution_basic_buy_1():
    data = load_data(TEST_DATA_FILE_1)
    buy_trade = trade.Trade(direction='BUY', entry=362.0, quantity=10, target=375, stop_loss=352, fees=0.07)
    trade_log = execution.get_trade_results(data, buy_trade)
    print(trade_log)

def main():
    test_execution_basic_buy_1()


if __name__ == "__main__":
    main()
