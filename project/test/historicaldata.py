import pandas as pd 
from datetime import datetime


pair1 = pd.read_csv(
    './marketdata/binance/AVAXUSDT-1m-2023-02.csv', 
    names=['open_time', 'open', 'high', 'low', 'close', 'Volume', 'close_time', "q_asset_volume", 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore']
    )

pair2 = pd.read_csv(
    './marketdata/binance/SOLUSDT-1m-2023-02.csv', 
    names=['open_time', 'open', 'high', 'low', 'close', 'Volume', 'close_time', "q_asset_volume", 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore']
    )


RANGE = 12 #%


# def main(atomusdt_spot: pd.DataFrame, atomusdt_perp: pd.DataFrame): 
#     rates = []
    
#     for i in range(len(atomusdt_spot)-1): 
#         spot = atomusdt_spot.iloc[i+1].tolist()
#         perp = atomusdt_perp.iloc[i+1].tolist()

#         # time = datetime.strptime(str(int(spot[0])), "%d/%m/%Y %H:%M:%S")
#         date = datetime.fromtimestamp(int(spot[0]/1000))
#         time = datetime.strftime(date, "%d/%m/%Y %H:%M:%S")


#         ration = float(spot[1])*100/float(perp[1]) - 100
#         if abs(ration) > 0.4:
#             print('rate: ', ration)
#             rates.append([abs(ration),time])

#         sorted_rates = sorted(rates)
        
        
        
def reenter_pool_counter(atomusdt_spot: pd.DataFrame): 
    range_prices, counter_plus = [], 0
    
    for i in range(len(atomusdt_spot)-1): 
        spot = atomusdt_spot.iloc[i+1].tolist()
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
            
        
            
    print(f'count times out of range: {len(range_prices)}')
    print(f'up: {counter_plus},   down: {len(range_prices) - counter_plus}')
    



if __name__ == "__main__":
    pair1 = pd.DataFrame(pair1)
    pair2 = pd.DataFrame(pair2)


    reenter_pool_counter(pair1)
