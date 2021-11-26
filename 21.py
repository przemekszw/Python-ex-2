tablica = [5,1,9,6,1]
max1 = tablica[0]
max2 = tablica[0]
for x in tablica:
        if max1 < x:
            max1 = x
for y in tablica:
        if max2 < y and y != max1:
            max2 = y           
print(max1,max2)
            