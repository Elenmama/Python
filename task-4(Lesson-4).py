a = list(map(int, input().split()))
b = [i for i in a if a.count(i) == 1]
print(b)
