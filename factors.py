print("Program to find the factors of a Number")

print("")

def fact(x):
  l = []
  for i in range(1, x + 1):
    if x % i == 0:
      l.append(i)
  
  return l


num = int(input("Enter the number: "))
print("")
print(f"Factors of {num}: {fact(num)}")
