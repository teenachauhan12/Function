###multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])

def multiply_list():
    a=[5,10,50,20]
    b=[2,20,3,5]
    i=0
    g=[]
    while i<len(a):
        c=a[i]*b[i]
        g.append(c)
        i+=1
    print(g)
multiply_list()






def sum():
    n=int(input("enter the number fast"))
    n2=int(input("enter the number second"))
    n3=int(input("enter the numnr third"))
    c=n+n2+n3
    print("addition number",c)
    print("average",c/3)
sum()









