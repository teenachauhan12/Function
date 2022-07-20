# n=int(input("enter the num"))
# i=n
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10
# if i==rev:
#     print("palindrome")
# else:
#     print("not palindrom")
#     i=i+1







# name=input("enter the name")
# i=0
# l=len(name)
# while i<=0:
#     if l%2==0:
#         print("even name")
#         break
#     else:
#         print("odd name")
#         break





# a=int(input("enter the num"))
# b=int(input("enter the num"))
# c=int(input("enter the num"))
# if a>b and a>c:
#     print("greater=",a)
# elif b>a and b>c:
#     print("greater=",b)
# else:
#     print("greater=",c)
    





# n=[2,4,6,8,10,2,6,3,4,12]
# i=0
# sum=0
# pro=1
# while i<len(n):
#     if i<5:
#         sum+=n[i]
#     else:
#         pro*=n[i]
#         i+=1
# print("sum=",sum)
# print("pro=",pro)




num=int(input("enter the num"))
l=len(str(num))
if int(str(num)[l-2])%3==0:
    print("d")
else:
    print("not d")











