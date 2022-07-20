def check_number():
    a=[2,6,18,10,3,75]
    b=[6,19,24,12,3,87]
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print(a[i],b[i],"both are even number")
        else:
            print(a[i],b[i],"both are not even number")
        i+=1

check_number()
