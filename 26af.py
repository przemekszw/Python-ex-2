pin = "0805"
licznik = 0
while(licznik!=3):
    haslo = input("Podaj PIN: ")
    licznik = licznik + 1
    if haslo != pin:
        print("Incorrect...")
        if licznik == 3:
            print("Sorry, your payment card has been blocked.")
    elif haslo == pin:
            print("Podales dobry PIN!")
            break
    
    