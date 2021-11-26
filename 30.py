from random import randint
def rand_elem(tablica):
    n = len(tablica)
    rand = randint(0, n-1)
    print(tablica[rand])
tablica = [5,4,3,2,6,5]
for x in range(3):
    rand_elem(tablica)

