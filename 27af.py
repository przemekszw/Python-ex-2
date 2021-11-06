l = 7
for x in range (1,4):
    for y in range (1,4):
        print(l,"", end="")
        l = l + 1
    l = l - 6    
    print("")
print("-----")

l = 6
while(l!=-3):
    l = l + 1
    print(l, end=" ")
    while(l%3==0):
        print("")
        l = l - 6
        break
    
