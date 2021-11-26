tabela = ['Genowefa','Onufry','Celestyna','Alojzy','Pankracy']
naj = len(tabela[0])
for x in tabela:
    dlugosc = len(x)
    if naj < dlugosc:
        naj = dlugosc
        imie = x
print(imie)
