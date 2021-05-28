import calendar
x = input("Enter date  ")
date = x
def findDay(date):
    day, month, year = (int(i) for i in date.split('/' ))
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])
print(findDay(date))