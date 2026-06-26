import math

print("Program to print all prime numbers in a line")

print("")

num = int(input("Enter the number till you want to see all the prime numbers: "))

for n in range(2, num + 1):
    for i in range(2, int(math.sqrt(n))):
      if n % i == 0:
          break

    else:
        print(n)