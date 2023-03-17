import pandas as pd 
from datetime import datetime


atomusdt_spot = pd.read_csv(
    './marketdata/binance/CHRUSDT-1m-2023-01.csv', 
    names=['open_time', 'open', 'high', 'low', 'close', 'Volume', 'close_time', "q_asset_volume", 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore']
    )

atomusdt_perp = pd.read_csv(
    './marketdata/binance/CHRUSDT-1m-2023-01_PERP.csv', 
    names=['open_time', 'open', 'high', 'low', 'close', 'Volume', 'close_time', "q_asset_volume", 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore']
    )





def main(atomusdt_spot: pd.DataFrame, atomusdt_perp: pd.DataFrame): 
    rates = []
    
    for i in range(len(atomusdt_spot)-1): 
        spot = atomusdt_spot.iloc[i+1].tolist()
        perp = atomusdt_perp.iloc[i+1].tolist()

        # time = datetime.strptime(str(int(spot[0])), "%d/%m/%Y %H:%M:%S")
        date = datetime.fromtimestamp(int(spot[0]/1000))
        time = datetime.strftime(date, "%d/%m/%Y %H:%M:%S")


        ration = float(spot[1])*100/float(perp[1]) - 100
        if abs(ration) > 0.4:
            print('rate: ', ration)
            rates.append([abs(ration),time])

        sorted_rates = sorted(rates)
        
        
        
def time_arb(atomusdt_spot: pd.DataFrame, atomusdt_perp: pd.DataFrame): 
    rates, circle = [], None
    prev = 0
    for i in range(len(atomusdt_spot)-1): 
        spot = atomusdt_spot.iloc[i+1].tolist()
        perp = atomusdt_perp.iloc[i+1].tolist()

        # time = datetime.strptime(str(int(spot[0])), "%d/%m/%Y %H:%M:%S")
        date = datetime.fromtimestamp(int(spot[0]/1000))
        time = datetime.strftime(date, "%d/%m/%Y %H:%M:%S")


        ration = float(spot[1])*100/float(perp[1]) - 100
        if abs(ration) > 1:

            if prev != i - 1:
                if not circle: pass
                else: 
                    rates.append(circle)
                circle = []
                circle.append([abs(ration),time])
                pass 
            else: 
                circle.append([abs(ration),time])
            prev = i
            # print('rate: ', ration)
            # rates.append([abs(ration),time])

        # sorted_rates = sorted(rates)
    count1, count2, count3, count_more = 0, 0, 0, 0
    for i, rate in enumerate(rates):
        print(rate)
        match len(rate): 
            case 1:
                count1 += 1
            case 2: 
                count2+= 1
            case 3: 
                count3 += 1
            case _: 
                count_more +=1 
                
                
    print(f'Oportunities: \n1 minute: {count1}\n2minutes: {count2}\n3minutes: {count3}\nmore then 3 mn: {count_more}')       

        
        









if __name__ == "__main__":
    df_spot = pd.DataFrame(atomusdt_spot)
    df_perp = pd.DataFrame(atomusdt_perp)


    time_arb(df_spot, df_perp)
