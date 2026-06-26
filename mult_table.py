print("Program to display Multiplication Table till 10")

print("")

num = int(input("Enter the number: "))

for i in range(1,11):
  mult = num * i
  print(f"{num} x {i} = {mult}")