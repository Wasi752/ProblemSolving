a = int(input())
b = 0
while a > b:
    c = input()
    last = c[-1]
    first = c[0]
    sum = (int(first) + int(last)) * len(c) // 2
    print(sum)
    a = a - 1
