i = 1
ilosc = -1
suma = 0
while i != 0:
    i = input("Podaj liczbe: ")
    i = int(i)
    suma = suma + i
    ilosc = ilosc + 1
srednia = suma / (ilosc)    
print(f"RESULT: Quantity={ilosc}, Sum={suma}, Mean={srednia}")
    

