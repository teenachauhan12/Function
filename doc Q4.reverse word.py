def reverse(a):
    b= ''
    i=len(a)
    while i>0:
        b=b+a[i-1]
        i=i-1
    return b
print(reverse('1234abcd'))

