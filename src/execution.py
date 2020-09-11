
def get_trade_results(data, trade):
    trade_status = 'Not Initiated'
    entry_idx = -1
    exit_idx = -1
    # First find the entry
    for i in range(len(data)):
        if data.iloc[i]['Low'] <= trade.entry <= data.iloc[i]['High']:
            trade_status = 'Active'
            print('Trade entered at {} on {} (candle#{})'.format(trade.entry, data.index[i], i))
            entry_idx = i
            break

    data_after_entry = data[i:].copy()

    # Check for stop loss
    if trade_status == 'Active':
        for i in range(len(data_after_entry)):
            if data_after_entry.iloc[i]['Low'] <= trade.stop_loss <= data_after_entry.iloc[i]['High']:
                trade_status = 'Closed. Stopped'
                print('Trade stopped at {} on {} (candle#{})'.format(trade.stop_loss, data_after_entry.index[i], i))
                exit_idx = i
                break

    # Check for target
    if trade_status == 'Active':
        for i in range(len(data_after_entry)):
            if data_after_entry.iloc[i]['Low'] <= trade.target <= data_after_entry.iloc[i]['High']:
                trade_status = 'Closed. Target Achieved'
                print('Trade closed at target {} on {} (candle#{})'.format(trade.target, data_after_entry.index[i], i))
                exit_idx = i
                break

    return trade_status

