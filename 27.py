def funkcja(tablica):
    for x in tablica:
        string = ",".join(str(x) for x in tablica)
    print(string)
tablica = [5,4,3,2,6,5]
funkcja(tablica)