def funkcja(x,n):
    potega = x**n
    print(potega)
funkcja(5,3)
def power(N, P):
    if P == 0:
        return 1
    elif P == 1:
        return N
    else:
        return (N*power(N, P-1))
N = 5
P = 5
print(power(N, P))