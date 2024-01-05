import logging
from datetime import datetime

start_time = "2:13:57"
end_time = "11:46:38"

logging.basicConfig(level=logging.DEBUG)

# convert the times to datetime objects
logging.info("Starting conversion to datetime objects")
converted_start_time = datetime.strptime(start_time, "%H:%M:%S")
converted_end_time = datetime.strptime(end_time, "%H:%M:%S")
logging.info("Finished conversion to datetime objects")


# calculate time time difference
logging.info("Starting calculation of difference between datetime objects")
time_difference = converted_end_time - converted_start_time
logging.info("Done with conversion to datetime objects")

print(time_difference)

# convert the datetime objects to strings
logging.info("Starting conversion to string objects")
string_start_time = datetime.strftime(converted_start_time, "%H:%M:%S")
string_end_time = datetime.strftime(converted_end_time, "%H:%M:%S")
logging.info("Finishing conversion to string objects")

print(string_start_time)
print(string_start_time)