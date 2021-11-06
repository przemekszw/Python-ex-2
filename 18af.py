kasa = input("Enter the amount in PLN")
kasa = int(kasa)
piec = 0
dwa = 0
jeden = 0

while kasa>=5:
         kasa = kasa - 5
         piec = piec + 1
while kasa>=2 :
    kasa = kasa - 2
    dwa = jeden + 1
while kasa==1:
    kasa = kasa - 1
    jeden = jeden + 1
print(f"5 zl - {piec}")
print(f"2 zl - {dwa}")
print(f"1 zl - {jeden}")