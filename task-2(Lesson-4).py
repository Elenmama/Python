a = list(map(int, input().split()))
b = [a[i] for i in range(1, len(a)) if a[i] > a[i - 1]]
print(b)
