#1st solution
from datetime import datetime
date_format = "%d/%m/%Y"
breakUp = datetime.strptime('23/10/2017', date_format)
today = datetime.strptime('20/06/2020', date_format)
daysFree = today - breakUp
print(daysFree)


#2nd solution
from datetime import date

now = date(2020, 6, 20)
exodus = date(2017, 10, 23)
freeFor = now - exodus
print(freeFor)