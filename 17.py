text = input("napisz cos: ")
litera = input("podaj litere: ")
licznik = 0

for x in text:
    if x==litera:
        licznik += 1
print(f"Ilosc liter w tekscie wynosi: {licznik}")

text = 'You never get a second chance to make a first impression'
litera = 'e'
licznik = 0

for x in text:
    if x==litera:
        licznik += 1
print(f"Ilosc liter w tekscie wynosi: {licznik}")