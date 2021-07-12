import pytz
import datetime

country = 'europe/moscow'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz_to_display)  #used pytz to create tzinfo object
# print("Time in {} is {}".format(country, local_time))
#
# for x in pytz.all_timezones:
#     print(x)
print(len(pytz.all_timezones))
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tno timezone to define")






