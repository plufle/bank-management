from datetime import date, timedelta

def w(x):
    month = x*12
    date_interest = []
    current_date = date.today().isoformat()
    days = 30
    for i in range(0, month):
        days_after = (date.today()+timedelta(days)).isoformat()
        days = days+30
        date_interest.append(days_after)

    return  date_interest

year = int(input('enetr number of yeras : '))
lel = w(year)









