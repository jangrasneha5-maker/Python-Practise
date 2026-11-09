from datetime import date
current=date.today()
print("current date is",current.day)
print("current month is",current.month)
print("current year is",current.year)


# strftime  wot is this think think
print("\n")
print("let's printdate,mont,year in different format")
format1=current.strftime("%m/%d/%y")
print("format1=",format1)

