wzrost = input("Podaj wzrost: ")
waga = input("Podaj wage: ")
wzrost = int(wzrost) 
waga = int(waga) 
bmi = (waga/wzrost**2)*10000
print(f"Twoje bmi wynosi: {bmi}")