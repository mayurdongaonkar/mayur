date1 = "2019-06-29" 
date2 = "2019-06-30"

from datetime import datetime

m = datetime.strptime(date1,'%Y-%m-%d').date()
n = datetime.strptime(date1,'%Y-%m-%d').date()

print(abs((m-n).days))

