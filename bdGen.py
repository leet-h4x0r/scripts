import sys

dNames = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
mNames = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# names of days and months in lower and capital cases
# including first-3-word version
dCases = sum(((name.lower(), name[:3].lower(), name, name[:3]) for name in dNames), ())
mCases = sum(((name.lower(), name[:3].lower(), name, name[:3]) for name in mNames), ())

days = ()
months = ()

# generate 1-31 including 01-09
for i in range(1, 32):
    if i < 10:
        days += (str(i),) + ("0" + str(i),)
    else:
        days += (str(i),)

# remove "#" to add names of days in format
#days += dCases


# generate 1-12 including 01-09
for i in range(1, 13):
    if i < 10:
        months += (str(i),) + ("0" + str(i),)
    else:
        months += (str(i),)
months += mCases

# generate year range from command arguments
# including last-2-digit version
# python3 bdGen.py 2000 2000 for single year 2000
years = sum(((str(year)[-2:], str(year)) for year in range(int(sys.argv[1]), int(sys.argv[2]) + 1)), ())

# full birthday
for day in days:
  for month in months:
    for year in years:
      print(day+month+year)

# day and year
for day in dCases:
  for year in years:
    print(day+year)

# month and year
for month in mCases:
  for year in years:
    print(month+year)

for day in dCases:
  print(day)
for month in mCases:
  print(month)
