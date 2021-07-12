# import time
#
# print(time.gmtime(0)) #epoch time starts on 1970
#
# # print(time.localtime())
# #
# # print(time.time())  #no. of secomds since epoch
#
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)  #used named tuple time_here.tm_year
# print("Month:", time_here[1], time_here.tm_mon)
# print("date:", time_here[2], time_here.tm_mday)

##Program to measure reaction time
import time
# from time import time as my_timer #time on system can be chnaged while waiting for player to press enter
from time import perf_counter as my_timer #this will show differest time than system
# from time import monotonic as my_timer  #monotonic - time cant go backwards after start.
import random

input("Please enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Please enter to stop")
end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time {}".format(end_time - start_time))
