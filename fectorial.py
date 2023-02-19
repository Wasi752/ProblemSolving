t = int(input())
i = 0
while i < t:
    n = int(input())
    counter = 1
    for x in range(1, n + 1):
        counter = counter * x
    print(counter)
    i = i + 1
