tablica = [5,1,9,6,1]
maks = tablica[0]
mini = tablica[0]
for x in tablica:
    if maks < x:
        maks = x
for x in tablica:
    if mini > x:
        mini = x
print(maks-mini)
    
    