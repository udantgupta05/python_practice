print("Program to display the Powers of 2 till the user wants")

print("")

num = int(input("Enter the limit till you want to see the list: "))

result = list(map(lambda x : 2 ** x, range(0, num+1)))

print(result)