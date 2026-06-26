print("Program to check if a number is Armstrong")

print("")

low_lim = int(input("Enter the lower limit: "))
hi_lim = int(input("Enter the higher limit: "))
count = 0

for num in range(low_lim, hi_lim + 1):
  order = len(str(num))
  fsum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    fsum = fsum + (digit ** order)
    temp = temp // 10
  
  if fsum == num:
    print(num)
    count = count + 1

print("")

if count == 0:
  print("No Fibonacci Numbers in this range")