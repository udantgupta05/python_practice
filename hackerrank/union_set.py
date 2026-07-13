eng = int(input(""))
E = set(map(int, input().split()))

fre = int(input())
F = set(map(int, input().split()))

print(len(E.union(F)))
