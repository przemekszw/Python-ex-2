tablica = [4,2,8,4,7,9,5]
mini = tablica[0]
maks = tablica[0]
for x in tablica:
    if x < mini:
        mini = x
for x in tablica:
    if x > maks:
        maks = x
tablica2 = [mini,maks]
print(f"[{tablica2[0]},{tablica2[1]}]")