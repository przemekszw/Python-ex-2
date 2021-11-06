a = input("Podaj a: ")
b = input("Podaj b: ")
a = int(a)
b = int(b)
for x in range(1,a+1):
    for y in range(1,b):
        if y == 1 or x == 1 or y == b or x == a:
            print(end="* ")
        else:
            print(end="  ")
    print("*")

