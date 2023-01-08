a = int(input())
b = 1
while b <= a:
    c = int(input()) # 56789 
    last = c % 10
    while c > 0:
        first = c % 10
        temp = c // 10
        c = temp 
    sum = first + last
    print('Sum = %d' %sum)
    b = b + 1
