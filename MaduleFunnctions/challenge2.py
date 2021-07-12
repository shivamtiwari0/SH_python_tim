import pytz
import random
import datetime

a = random.randint(1, 500)
for zone in pytz.all_timezones[a:a+9]:
    print(zone, end=", ")


while True:
    choosen_timezone = input("\nEnter your timezone= ")

    if choosen_timezone == '0':
        break
    elif choosen_timezone not in pytz.all_timezones[a:a + 9]:
        pass
    if choosen_timezone in pytz.all_timezones[a:a + 9]:
        local_time = datetime.datetime.now().strftime("%A %x %X")
        utc_time = datetime.datetime.utcnow().strftime("%A %x %X")
        zone_time = datetime.datetime.now(pytz.timezone(choosen_timezone)).strftime("%A %x %X %z")

        print("Local time- {}, UTC Time- {}, You chose zone {} and time there is {}."
              "".format(local_time, utc_time, choosen_timezone, zone_time))



