from datetime import datetime, timedelta


today = datetime.now()
print (f"Today is: {today.strftime('%Y-%m-%d')}")

def earlier_date (n):
    delta = timedelta(days = n)
    result = (today - delta).strftime('%Y-%m-%d')
    print (f"{n} day(s) before was: {result}")


earlier_date(1)
earlier_date(30)