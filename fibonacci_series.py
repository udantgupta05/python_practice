print("Program to display fibonacci series")

print("")

a = 0
b = 1

num = int(input("Enter the number to obtain the Fibonacci Sequence: "))

if num == 1:
  print(a)

else:
  print(a)
  print(b)
  for i in range(2, num):
    c = a + b
    a = b
    b = c
  
    print(c)