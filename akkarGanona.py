t = int(input())
i = 0
while i < t:
    bakka = input()
    borna = input()
    counter = 0
    for char in bakka:
        if char == borna:
            counter = counter + 1
    print("Mot Borna of '{}' in '{}' = {}".format(borna, bakka, counter))
    i = i + 1
