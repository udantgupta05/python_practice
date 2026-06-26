print("Program to swap two variables")

print("")

a = str(input("Write some text: "))
b = str(input("Write some text again: "))

print("")

print("Entered Values are")
print("")
print(f"First Value = {a}")
print(f"Second Value = {b}")
print("")


a,b = b,a

print("Swapped Values are")
print(f"First Value = {a}")
print(f"Second Value = {b}")