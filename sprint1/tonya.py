from datetime import *

def timedelta_days(datetime_str_1, datetime_str_2):
    res = datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S')-datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S')
    return res.days

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')