def even_odd(limit):
    for i in range(0, limit):
        if i==0:
            print(i,end=" ")
            print("EVEN")   
        elif i%2==0:
            print(i,end=" ")
            print("EVEN")
        else:
            print(i,end=" ")
            print("ODD")
print(even_odd(3))
