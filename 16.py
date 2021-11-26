tabela = [12, 6, 4, 9,3]

for x in tabela:
    x = int(x)
    print(x,end=": ")
    y = 0
    while(y != x):
        y += 1
        print(end="*")
    print()
