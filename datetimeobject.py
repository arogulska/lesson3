from datetime import datetime

def datetime_type():
    date_str = "01/01/17 12:10:03.234567"
    date_object = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
    print (repr(date_object))

datetime_type()
