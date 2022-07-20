def factorial(n):
    f=1
    while 0<n:
        f=f*n
        n=n-1
    print("factorial",f)
n=int(input("enter the num"))
factorial(n)