i = input("podaj ilosc liczb pierwszych do wyswietlenia: ")
i = int(i)
for x in range (1,i):
    for y in range(2,x+1):
        if x%y==0:
            if x==y:
                print(x,end=" ")
            break

        
    