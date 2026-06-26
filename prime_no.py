import math
print("Program to check if a number is prime")


print("")

num = (int(input("Enter the number: ")))

print("")

if num <= 1:
  print("The number is not prime")

elif num == 2:
  print("The number is prime")

elif num > 1:
  for i in range (2, int(math.sqrt(num)) + 1):
    if num%i == 0:
      print("The number is not prime")
      break

  else:
    print("The number is prime")