t = int(input())
i = 1
while i <= t:
    n = int(input())
    j = 1
    print("Case %d:" %i, end='')
    while j <= n:
        if n % j == 0:
            print(" %d" %j, end='')
        j = j + 1
    print('')
    i = i + 1
