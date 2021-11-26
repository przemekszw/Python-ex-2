def bubbleSort(tablica):
    n = len(tablica)
    for x in range(n-1):
        for y in range(0,n-x-1):
            if tablica[y] > tablica[y+1]:
                tablica[y], tablica[y+1] = tablica[y+1], tablica[y]
tablica = [15, 38, 7, 23, 14]
bubbleSort(tablica)
for x in range(len(tablica)):
    print(tablica[x])