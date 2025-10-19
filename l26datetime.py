from datetime import datetime

# ? Get current date and time

getdatetime = datetime.now()

print(
    f"Current Date and Time: {getdatetime}"
)  # * Current Date and Time: 2025-10-19 17:01:57.310787

print(f"Year: {getdatetime.year}")  # * Year: 2025

print(f"Month: {getdatetime.month}")  # * Month: 10

print(f"Day: {getdatetime.day}")  # * Day: 19

print(f"Hour: {getdatetime.hour}")  # * Hour: 17

print(f"Minutes: {getdatetime.minute}")  # * Minutes: 5

print(f"Seconds: {getdatetime.second}")  # * Seconds: 39

print(f"Microsecond: {getdatetime.microsecond}")  # * Microsecond: 377232

# ? Create a specific datetime

setdatetime = datetime(2000, 3, 25, 13, 30, 45)

print(f"My Birthday: {setdatetime}")  # * My Birthday: 2000-03-25 13:30:45

# ? strftime , Formating Date Time
getnow = datetime.now()
formatdatetime = getnow.strftime("%Y-%B-%d %H-%M-%S")
print(
    "Formatted Date Time = ", formatdatetime
)  # * Formatted Date Time =  2025-10-19 17-13-32

# ? strptime() , Convert a string to datetime

strdate = "2025-October-19 17-13-32"
convertteddate = datetime.strptime(strdate, "%Y-%B-%d %H-%M-%S")

print("Converted Datetime: ", convertteddate)  # * 2025-10-19 17:13:32
