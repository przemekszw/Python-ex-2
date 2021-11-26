table = ['Green','Yellow','Black','Red']
f = open("tekst.txt","w")
for x in table:
    f.write(f"{x}\n")
f.close()
f = open("tekst.txt","r")
print(f.read())