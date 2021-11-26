tablica = [5,4,3,2,6,5]
tablica2 = [5,4,3,2,6,5]
n = len(tablica)
i = 0
while tablica[i-1] == tablica2[i-1]:
    i = i + 1
    if i>=n:
        print("Tablice sa identyczne")
        break
    
    
    