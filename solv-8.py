t = int(input())
i = 1 
while i <= t:
    n1, n2, n3 = map(int, input().split()) # 3 2 1
    if n1 > n2:
        a = n1
        n1 = n2 
        n2 = a # 2 3 1
    if n2 > n3:
        a = n2
        n2 = n3
        n3 = a # 2, 1, 3
    if n1 > n3:
        a = n1
        n1 = n3
        n3 = a  
    if n1 > n2:
        a = n1
        n1 = n2
        n2 = a # 1 2 3
    print("Case %d:" %i, end=' ')
    print( n1, n2, n3)
    i = i + 1
