# import time
#
# print("The epoch starts on this system at " + time.strftime('%c', time.gmtime(0)))
# print("The current timezone is {} with an offset of {} ".format(time.tzname[0], time.timezone))
# if time.daylight != 0:
#     print("\tDST is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
# print("Localtime is " + time.strftime("%d-%m-%y %H:%M:%S", time.localtime()))
# print("UTC time is " + time.strftime("%d-%m-%y %H:%M:%S", time.gmtime()))

import datetime

print()

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
