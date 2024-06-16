#prmpt for a date in month-day-year
#can be #/#/# or str, #, #
#output same date in YYYY-MM-DD format
#if input not valid, prmpt again
#don't need to validate that dates align as
# long as it is less than 31

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthsDict = {}


months.index("March") + 1

val = 0
for i in months:
    val = val + 1
    monthsDict[i] = val


date = input("Date: ").split("/")