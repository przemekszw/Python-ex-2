def fun(a):
    suma = 0
    while a>=1000:
        a = a - 1000
        suma += 1
    while a>=100:
        a = a - 100
        suma += 1
    while a>=10:
        a = a - 10
        suma += 1
    while a>=1:
        a = a - 1
        suma += 1
    print(f"Suma cyfr {suma}")
fun(5634)
