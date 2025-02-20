import datetime as dt
from collections import defaultdict

def weekday_name(num_weekday):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[num_weekday]

def main():
    weekday_counts = {}

    with open("births.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            line_s = line.strip()
            dt_parts = line_s.split("-")

            
            date = dt.datetime(int(dt_parts[0]), int(dt_parts[1]), int(dt_parts[2]))
            num_weekday = date.weekday()

            weekday = weekday_name(num_weekday)
            if weekday in weekday_counts:
                weekday_counts[weekday] += 1
            else:
                weekday_counts[weekday] = 1

    print(weekday_counts)

main()
