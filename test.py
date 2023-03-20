# define the file names
from dateutil.relativedelta import relativedelta
from datetime import datetime

# define the file names
name1 = 'name-2022-06'
name2 = 'name-2023-05'

# extract the dates from the file names
date1 = datetime.strptime(name1.split('-')[1] + '-' + name1.split('-')[2], '%Y-%m')
date2 = datetime.strptime(name2.split('-')[1] + '-' + name2.split('-')[2], '%Y-%m')

# create a list of datetime objects for each month in the period
periods = []
while date1 <= date2:
    periods.append(date1)
    date1 += relativedelta(months=1)

# format each date back into the desired string format and append the name
names = [f"{name1.split('-')[0]}-{period.strftime('%Y-%m')}" for period in periods]

print(names)