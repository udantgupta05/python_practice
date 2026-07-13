if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        user_input = input().split()

        if user_input[0] == "insert":
            list.insert(int(user_input[1]), int(user_input[2]))

        elif user_input[0] == "print":
            print(list)

        elif user_input[0] == "remove":
            list.remove(int(user_input[1]))

        elif user_input[0] == "append":
            list.append(int(user_input[1]))

        elif user_input[0] == "sort":
            list.sort()

        elif user_input[0] == "pop":
            list.pop()

        elif user_input[0] == "reverse":
            list.reverse()