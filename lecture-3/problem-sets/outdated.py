#prmpt for a date in month-day-year
#can be #/#/# or str, #, #
#output same date in YYYY-MM-DD format
#if input not valid, prmpt again
#don't need to validate that dates align as
#long as it is less than 31

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

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm,dd,yyyy = date.split("/")
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            mm = (months.index(mm)) + 1
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break