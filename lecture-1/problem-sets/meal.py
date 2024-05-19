time = input("What time is it? ")
time = time.split(sep = ":")
new_time = int("".join(time))

if new_time >= 700 and new_time <=800:
    print("Breakfast")
elif new_time >= 1200 and new_time <= 1300:
    print("Lunch")
elif new_time >= 1800 and new_time <= 1900:
    print("Dinner")
else:
    print("")