print("Program to determine HCF/GCD of two numbers")
print("")

def hcf(a, b):
  if a > b:
    smaller = b
  
  else:
    smaller = a
  
  for i in range(1, smaller + 1):
    if (a % i == 0) and (b % i == 0):
      h_c_f = i 
  return h_c_f


x = int(input("Enter the First Number: "))
y = int(input("Enter the Second Number: "))

print("")

print(f"HCF/GCD of {x} and {y} is {hcf(x, y)}")