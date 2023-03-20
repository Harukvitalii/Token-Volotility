


# FOR YEAR
time_days              = 5*31
start                  = 500 #$
APR                    = 666  #%
profit_return_to_pool  = 10
profit_return          = False  
reenter_counter        = 193*12
percent_from_one_enter = APR/reenter_counter/100
SOLPRICE = 23


pool_fee      = 0.01
pool_fee      = 0.01
take_profit   = (0.0115 - 0.00442152)*SOLPRICE
swap_fee      = (start*1)*1.1*0.0005


new_sum, profit, sums = 0, 0, []

    
for i in range(reenter_counter):
    if profit_return:
        if i == 0: 
            new_sum = start 
            fees = swap_fee + pool_fee
            sums.append(start-fees)
            profit += percent_from_one_enter*start
        else:
            new_sum = sums[-1]
            fees = swap_fee + pool_fee
            sums.append(new_sum-fees)
            profit += percent_from_one_enter*new_sum
            
        if profit >= profit_return_to_pool: 
            sums[-1] = sums[-1] + profit - take_profit
            profit = 0
    else: 
        if i == 0: 
            new_sum = start*percent_from_one_enter 
            fees = swap_fee + pool_fee + take_profit
            sums.append(start-fees)
            profit += percent_from_one_enter*start
        else:
            new_sum = sums[-1] + sums[-1] * percent_from_one_enter
            fees = swap_fee + pool_fee + take_profit
            sums.append(new_sum-fees)
        
        
 


counter = 0
for i in sums: 
    counter += 365/reenter_counter
    print(f'balance {counter:.2f} = {i:.2f}  +{i*100/start-100:.2f}%')
    if counter >= time_days: 
        break
    