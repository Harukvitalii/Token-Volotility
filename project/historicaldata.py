import pandas as pd 
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime

name1 = './marketdata/binance/AVAXUSDT-1m-2022-07'
name2 = './marketdata/binance/AVAXUSDT-1m-2023-02'

# extract the dates from the file names
date1 = datetime.strptime(name1.split('-')[2] + '-' + name1.split('-')[3], '%Y-%m')
date2 = datetime.strptime(name2.split('-')[2] + '-' + name2.split('-')[3], '%Y-%m')

# create a list of datetime objects for each month in the period
periods = []
while date1 <= date2:
    periods.append(date1)
    date1 += relativedelta(months=1)

# format each date back into the desired string format and append the name
names = [f"{name1.split('m-')[0]}m-{period.strftime('%Y-%m')}" for period in periods]

datasets = []
for path in names: 
    data = pd.read_csv(
    f'{path}.csv', 
    names=['open_time', 'open', 'high', 'low', 'close', 'Volume', 'close_time', "q_asset_volume", 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore']
    )

    datasets.append(data)







BASE_RANGE = 15 #%
APR        = 200


def reenter_pool_counter(klines_spot: pd.DataFrame, binrange): 
    range_prices, counter_plus = [], 0
    RANGE = binrange*0.425

    
    for i in range(len(klines_spot)-1): 
        spot = klines_spot.iloc[i+1].tolist()
        # print(spot)

        # time = datetime.strptime(str(int(spot[0])), "%d/%m/%Y %H:%M:%S")
        date = datetime.fromtimestamp(int(spot[0]/1000))
        time = datetime.strftime(date, "%d/%m/%Y %H:%M:%S")

        token_price = float(spot[1])
        if not range_prices: 
            range_prices.append(token_price)
        
        
        if token_price > range_prices[-1]*((100+RANGE)/100):
            range_prices.append(token_price)
            counter_plus +=1
        elif token_price < range_prices[-1]*((100-RANGE)/100):  
            range_prices.append(token_price)
            
        
            
    # print(f'count times out of range: {len(range_prices)}')
    # print(f'up: {counter_plus},   down: {len(range_prices) - counter_plus}')
    
    return len(range_prices), counter_plus, len(range_prices) - counter_plus


def counter_datasets(DFs, binrange): 
    counter_reENTER, minus_counter, plus_counter = 0, 0, 0
    for df in DFs: 
        c1, c2, c3 = reenter_pool_counter(df, binrange=binrange)
        counter_reENTER += c1 
        minus_counter   += c2
        plus_counter    += c3
    
    print(f'FINAL RESULT binRange {binrange}')
    print(f'count times out of range: {counter_reENTER}')
    print(f'Average: {counter_reENTER/len(DFs)}')
    print(f'up: {minus_counter},   down: {plus_counter}   {minus_counter*100/(minus_counter+plus_counter):.3f}% ')
    
    proc  = BASE_RANGE/binrange
    NEW_APR = proc*APR
    return (binrange, counter_reENTER/len(DFs), NEW_APR)

if __name__ == "__main__":
    DFs = [pd.DataFrame(dataset) for dataset in datasets]
    
    # pair2 = pd.DataFrame(pair2)
    range_dataset = []
    for i in range(BASE_RANGE):
        range_dataset.append(counter_datasets(DFs, i+1))
    print(range_dataset)
