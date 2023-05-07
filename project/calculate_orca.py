


# FOR YEAR
months = 6
time_days              = months *31
start                  = 100 #$
profit_return_to_pool  = 10
profit_return          = False  
# reenter_counter        = 193*12
# percent_from_one_enter = APR/reenter_counter/100
SOLPRICE = 22


pool_fee      = 0.01 + 0.01
take_profit   = (0.0115 - 0.00442152)*SOLPRICE



new_sum, profit, sums = 0, 0, []

def calculate(APR, renter, bins): 
    reenter_counter        = int(renter*12)
    percent_from_one_enter = APR/reenter_counter/100

    new_sum, profit, sums = 0, 0, []

    for i in range(reenter_counter):
        if profit_return:
            if i == 0: 
                new_sum = start 
                swap_fee = (start*1)*(0.0005*2)
                fees = swap_fee + pool_fee
                sums.append(start-fees)
                profit += percent_from_one_enter*start
            else:
                new_sum = sums[-1]
                swap_fee = (new_sum*1)*(0.0005*2)

                      
                fees = swap_fee + pool_fee
                sums.append(new_sum-fees)
                profit += percent_from_one_enter*new_sum
                
            if profit >= profit_return_to_pool: 
                sums[-1] = sums[-1] + profit - take_profit
                profit = 0
        else: 
            if i == 0: 
                new_sum = start*percent_from_one_enter 
                swap_fee = (new_sum*1)*(0.0005*2)
                fees = swap_fee + pool_fee + take_profit
                print(fees)
                sums.append(start-fees)
                profit += percent_from_one_enter*start
                print(profit)
                
            else:
                new_sum = sums[-1] + sums[-1] * percent_from_one_enter
                swap_fee = (new_sum*1)*(0.0005*2)
                fees = swap_fee + pool_fee + take_profit
                # if i//2 == 0:
                #     new_sum -= new_sum * bins * 0.01
                sums.append(new_sum-fees)
            
    counter = 0
    for i in sums: 
        counter += 365/reenter_counter
        if counter >= time_days: 
            print(f'balance {counter:.2f} = {i:.2f}  +{i*100/start-100:.2f}%')
            return i*100/start-100    



dataset = [(1, 669.5, 1000.0), (2, 200.0, 500.0), (3, 96.5, 333.33333333333337), (4, 62.5, 250.0), (5, 38.0, 200.0)]

for apr_renter in dataset: 
    print(f'APR = {apr_renter[2]}%  renter = {apr_renter[1]} bins = {apr_renter[0]}')
    profit = calculate(apr_renter[2], apr_renter[1], apr_renter[0])
    print(f'profit {profit:.2f}')
    print('-'*10)