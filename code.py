def calc():
    n, H, M = [int(el) for el in input().split()]
    ans = 99999
    for _ in range(n):
        h, m = map(int, input().split())
        if h * 60 + m < H * 60 + M:
            ans = min(ans, (24 - H - 1 + h) * 60 + m + 60 - M)
        else:
            ans = min(ans, (h - H) * 60 - M + m)
    print(ans // 60, ans % 60)
 
 
for _ in range(int(input())):
    calc()
