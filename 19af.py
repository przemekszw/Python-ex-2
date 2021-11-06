wiek = input("Enter the dog's age in human years: ")
wiek = float(wiek)
if wiek==1 or wiek==2:
    wiek = wiek * 10.5
    print(f"The dog's age in dog’s years is {wiek} years.")
elif wiek>2:
    wiek = 21 + ((wiek - 2) * 4)
    print(f"The dog's age in dog’s years is {wiek} years.")
