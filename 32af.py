n = 1
for x in range (1,8):
    for y in range (1,8):
        print(n,end=" ")
        n = n + 7
    n = n - 48
    print("")
