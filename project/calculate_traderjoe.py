


dataset = [(1, 2135.125, 3000.0), (2, 674.625, 1500.0), (3, 326.5, 1000.0), (4, 195.125, 750.0), (5, 129.75, 600.0), (6, 90.875, 500.0), (7, 67.125, 428.57142857142856), (8, 52.375, 375.0), (9, 45.125, 333.33333333333337), (10, 35.125, 300.0), (11, 28.125, 272.7272727272727), (12, 25.0, 250.0), (13, 21.0, 230.76923076923075), (14, 19.625, 214.28571428571428), (15, 17.875, 200.0)]

# FOR YEAR
months        = 1
time_days              = months *31
start                  = 320 #$
profit_return_to_pool  = 10

pool_fee      = 1.2 + 1.2
pool_fee      = 0.6 + 0.4
take_profit   = 0.4
profit_return  = True


def calculate(APR, renter, bins): 
    reenter_counter        = int(renter*12)
    percent_from_one_enter = APR/reenter_counter/100
    minus_percent =renter/2*12



    new_sum, profit, sums = 0, 0, []

        
    for i in range(reenter_counter):
        if profit_return:
            if i == 0: 
                new_sum = start 
                swap_fee      = (start/2)*0.004
                fees = swap_fee + pool_fee
                sums.append(start-fees)
                profit += percent_from_one_enter*start
            else:
                    
                new_sum = sums[-1]
                swap_fee      = (new_sum/2)*0.004
                if i%2: 
                    new_sum -= new_sum * bins * 0.00425
                fees = swap_fee + pool_fee
                sums.append(new_sum-fees)
                profit += percent_from_one_enter*new_sum
                
            if profit >= profit_return_to_pool:
                swap_fee      = (new_sum/2)*0.004
                 
                sums[-1] = sums[-1] + profit - take_profit
                profit = 0
        else: 
            if i == 0: 
                new_sum = start*percent_from_one_enter 
                swap_fee      = (new_sum/2)*0.004
                fees = swap_fee + pool_fee + take_profit
                sums.append(start-fees)
                profit += percent_from_one_enter*start
            else:
                new_sum = sums[-1] + sums[-1] * percent_from_one_enter
                swap_fee      = (new_sum/2)*0.004
                
                fees = swap_fee + pool_fee + take_profit
                sums.append(new_sum-fees)
            
    counter = 0
    for i in sums: 
        counter += 365/reenter_counter
        if counter >= time_days: 
            print(f'balance {counter:.2f} = {i:.2f}  +{i*100/start-100:.2f}%')
            return i*100/start-100        
        
        
for apr_renter in dataset: 
    print(f'APR = {apr_renter[2]}%  renter = {apr_renter[1]} bins = {apr_renter[0]}')
    profit = calculate(apr_renter[2], apr_renter[1], apr_renter[0])
    print(f'profit {profit:.2f}')
    print('-'*10)