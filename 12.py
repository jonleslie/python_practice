import calendar 

year = input("Enter the year: ")
month = input("Enter the month: ")

print(calendar.monthcalendar(year, month))
print(calendar.month(year, month))