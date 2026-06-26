print("Program to find the sum of Natural Numbers")

print("")

sum = 0

num = int(input("Enter the Natural Number till you want to find the sum: "))

print("")

if num < 1:
  print("The number is not Natural")

else:
  for i in range(1, num + 1):
    sum = sum + i

  print(f"The sum of Natural Numbers till {num} is {sum}")