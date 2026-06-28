print("Program to convert Decimal to Binary, Octal and Hexadecimal")

print("")

decimal = int(input("Enter the number: "))

print("")

print(f"{bin(decimal)[2:]} in Binary Form")
print("")
print(f"{oct(decimal)[2:]} in Octal Form")
print("")
print(f"{hex(decimal)[2:].upper()} in Hexadecimal Form")