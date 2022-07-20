def shownumber(a):
    for i in range(0,a):
        if i==0:
            print(i,end=" ")
            print("EVEN")   
        elif i%2==0:
            print(i,end=" ")
            print("EVEN")

        else:
            print(i,end=" ")
            print("ODD")
print(shownumber(4))