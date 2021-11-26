def bubbleSort(tablica):
    n = len(tablica)
    for x in range(n-1):
        for y in range(0,n-x-1):
            if tablica[y] > tablica[y+1]:
                tablica[y], tablica[y+1] = tablica[y+1], tablica[y]
tablica = [6,8,3,1,0,5,7]
bubbleSort(tablica)
n = len(tablica)
if n%2==0:
    n = n / 2 
    m = n - 1
    n = int(n)
    m = int(m)
    wynik = (tablica[n]+tablica[m])/2
else:
    n = n / 2 - 0.5
    n = int(n)
    wynik = tablica[n]
print(wynik)