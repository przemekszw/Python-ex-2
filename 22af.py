for x in range(1,31):
    if x%5==0 and x%3==0:
           print(f"BINGO",end=' ')
    elif x%3==0:
        print(f"Three",end=' ')
    elif x%5==0:
           print(f"Five",end=' ')
    else:  
       print(x,end=' ')