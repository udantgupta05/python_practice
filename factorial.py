print("Program for factorial of a number")

fact = 1

print("")

num = int(input("Enter the number: "))

print("")

if num == 0:
  print("The factorial of 0 is 1")
  

elif num < 0:
  print("The factorial doesn't exist")
  

elif num > 0:
  for i in range(1, num + 1):
    fact = fact * i


  print(f"The factorial of {num} is {fact}")