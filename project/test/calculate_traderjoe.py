


# FOR YEAR
time_days              = 12 *31
start                  = 1000 #$
APR                    = 600  #%
profit_return_to_pool  = 10
reenter_counter        = 142*12
percent_from_one_enter = APR/reenter_counter/100


pool_fee      = 1.67 + 1.6
pool_fee      = 1 + 0.82
take_profit   = 0.5
swap_fee      = (start/2)*1.1*0.003


new_sum, profit, sums = 0, 0, []

    
for i in range(reenter_counter):
    
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
    
    # if i == 0: 
    #     new_sum = start*percent_from_one_enter 
    #     fees = swap_fee + pool_fee
    #     sums.append(start-fees)
    #     profit += percent_from_one_enter*start
    # else:
    #     new_sum = sums[-1] + sums[-1] * percent_from_one_enter
    #     fees = swap_fee + pool_fee
    #     sums.append(new_sum-fees)
        
        
 


counter = 0
for i in sums: 
    counter += 365/reenter_counter
    print(f'balance {counter:.2f} = {i:.2f}  +{i*100/start-100:.2f}%')
    if counter >= time_days: 
        break
    