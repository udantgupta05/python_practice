import calendar

try:
  year = int(input("Enter year: "))
  month = int(input("Enter month: "))

  caldr = calendar.month(year,month)
  print(caldr)

except ValueError:
  print("")
  print("Please enter integer values only and values between 1-12 for month")