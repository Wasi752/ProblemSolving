t = int(input())
i = 0
while t > i:
    n = input()
    j = 0
    num = ""
    counter = 0
    while j < len(n):
        if n[j] != " ":
            num = num + n[j]
        elif n[j] == " " and len(num) > 0:
            counter = counter + 1
            num = ""
        j = j + 1
    if n[len(n) - 1] != " ":
        counter = counter + 1 
    print(counter)
    i = i + 1
