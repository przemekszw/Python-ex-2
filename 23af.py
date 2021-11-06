
for x in range(1,10):
    print(f"{x}")
    x = x + 1
    for a in range(x-1):
        if x==10:
            break
        print(f"{x}",end='')