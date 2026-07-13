if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    highest = max(arr)

    while highest in arr:
        arr.remove(highest)

    print(max(arr))