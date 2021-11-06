from random import randint
a = input("Guess the numba: ")
a = int(a)
numer = randint(1,6)
if a==numer:
    print(f"True")
    
else:
    print(f"False {numer}")
    
