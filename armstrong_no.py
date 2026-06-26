print("Program to check if a number is Armstrong")

print("")

num = int(input("Enter the number: "))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
  digit = temp % 10
  sum = sum + (digit ** order)
  temp = temp // 10

if sum == num:
  print("It is an Armstrong Number")

else:
  print("Not an Armstrong Number")
