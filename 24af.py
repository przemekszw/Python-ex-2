for x in range(2,11):
    print("*")
    for a in range(x-1):
        if x==9 or x ==10:
            break
        print("*",end='')
        x = x + 1