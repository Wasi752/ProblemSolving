t = int(input())
i = 0
while i < t:
    n = int(input())
    ok = False
    for x in range(1, n):
        if x * x == n:
            ok = True
    if ok == True:
        print('YES')
    else:
        print('NO')
    i = i + 1
    #10000000 = 1 second
    # 2 ^ 31 = 2147483648
    # sqrt() 'Home Work'
