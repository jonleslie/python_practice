from datetime import date

d1 = date(2018, 5, 25)
d2 = date(2018, 4, 9)

delta = d1 - d2

print(delta.days)
