import datetime
import time
from time import *
from datetime import *
ask = input("<none of this info is shared> Input a date<YR-M in numbers-D>>>")
dt = datetime.strptime(ask, "%Y-%m-%d").date()
print(dt.strftime("%A"))
time.sleep(60)