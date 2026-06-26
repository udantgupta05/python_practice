print("Program to find numbers Divisible by Another Number")

print("")

num = int(input("Enter the number you want to find the numbers of which that are divisible: "))
divisors = []
print("")

for i in range(1, num + 1):
  if num % i == 0:
    divisors.append(i)

print(divisors)