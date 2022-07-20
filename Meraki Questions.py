
# Number=[3, 5, 7, 34, 2, 89, 2, 5]
# print(max(Number))





# numbers = [1, 2, 3, 4, 5]
# i=0
# sum=0
# while i<len(numbers):
#     sum=sum+numbers[i]
#     i+=1
# print(sum)




# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# unorder_list.sort()
# print(unorder_list)





# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list.reverse()
# print(reverse_list)


# list = [8, 6, 4, 8, 4, 50, 2, 7]
# print(min(list))


# def sum():
#     print(12+13)
# sum()



# def welcome():
#     print("Welcome to function")
# welcome()



# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()





# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))






# def student_data(student_id, **kwargs):
#     print(f'\nStudent ID: {student_id}')
#     if 'student_name' in kwargs:
#         print(f"Student Name: $ {kwargs['student_name']}")
    
#     if 'student_name' and 'student_class' in kwargs:
#             print(f"\nStudent Name: $ {kwargs['student_name']}")
#             print(f"Student Class: $ {kwargs['student_class']}")

 
# student_data(student_id='SV12', student_name='Jean Garner')

# student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')






# def student(firstname, lastname ='Mark', standard ='Fifth'):
#      print(firstname, lastname, 'studies in', standard, 'Standard')
# student('John')                       
# student('John', 'Gates', 'Seventh')    
# student('John', 'Gates')                 
# student('John', 'Seventh')




#########def check_numbers(x,y):
#     if x%2==0 and y%2==0:
#         print("both are even num")
#     else:
#         print("boht are not even num")

# check_numbers([2,6,18,10,3,75],[6,19,24,12,3,87])







# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print(sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print(sum2)
# print(sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print(number_a)







# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print(sum4)
# print(type(sum4))






# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print("Hello from NavGurukul ;)")
#     return number_sum

# x=add_numbers_more(100,20)
# print("will i reach here?")
# print(x)




# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

# print("Will I be able to print? :-(")

# mon_menu = menu("monday")
# print(mon_menu)
# tues_menu = menu("tuesday")
# print(tues_menu)
# fri_menu = menu("friday")
# print(fri_menu)





# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print("Will I be able to print? :-(")
#     return food
# print("But I'm not sure will print? :'(")
# print(menu("monday"))





# def ask_question():
#     print("once")
# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()







# def info(name, age):
#    print(name + " is " + age + " years old")

# info("Sonu","15")
# info("Sana", "17")
# info("Umesh", "18")





# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


# studentDetails("Nilam","loop","sonu")


# def function_print_lines():
#     print("My name is Rishabh.")
#     print("I am the co-founder of NavGurukul.")
# function_print_lines()




# def add_numbers(num1,num2):
#     print(num1+num2)
# add_numbers(56,12)



# def add_numbers_list(x,y):
#     print("add sam index",x+y)
# add_numbers_list(50,10)
# add_numbers_list(60,20)
# add_numbers_list(10,13)





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



###multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])

# def multiply_list():
#     a=[5,10,50,20]
#     b=[2,20,3,5]
#     i=0
#     g=[]
#     while i<len(a):
#         c=a[i]*b[i]
#         g.append(c)
#         i+=1
#     print(g)
# multiply_list()





# def age(x):
#     if x>=18:
#         print("you are eligible")
#     else:
#         print("not eligible")
# age(18)
# age(16)




# def sum():
#     n=int(input("enter the number fast"))
#     n2=int(input("enter the number second"))
#     n3=int(input("enter the numnr third"))
#     c=n+n2+n3
#     print("addition number",c)
#     print("average",c/3)
# sum()    





# def even_odd(limit):
#     for i in range(0, limit):
#         if i==0:
#             print(i,end=" ")
#             print("EVEN")   
#         elif i%2==0:
#             print(i,end=" ")
#             print("EVEN")
#         else:
#             print(i,end=" ")
#             print("ODD")
# print(even_odd(3))






# def sum_of_numbers(limit):
#     total = 0
#     for i in range(limit):
#         if i % 3 == 0 or i % 5 == 0:
#             total = total + i
#         i = i + 1
#     return total
# userInput = int(input("Enter limiting number: "))
# plusOne = userInput + 1
# print(sum_of_numbers(plusOne))








# def checkSpeed(speed):
#     if speed <= 70:
#         return "OK"
#     else:
#         speed1 = (speed-70)//5
#         if speed1 <= 12:
#             print(f"Point: {speed1}")
#         else:
#             print("License suspended")

# checkSpeed(int(input("Enter speed: ")))








# n=int(input("enter a number "))
# d = dict()
# for x in range(1,n+1):
#     d[x]=x*x
# print(d)






# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")




# def primeorNot(num): 
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)





# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")




# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# print(sumofdigits(123))






# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#                 return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))





# def checkKey():
#     car ={
#         "brand":  "ford",
#         "model":  "mustang",
#         "year":  1964
#     }
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")

# checkKey()






# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# #sum(4,5)
# calculate_sum(4,5)




# def function_multiply(a,b):
#     multiply=a*b
#     return multiply
# print(function_multiply(3,4))




# def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)




# def voter(age):
#     if age > 18:
#         print("eligible")
#     else:
#         print("not eligible")
# voter(20)





# def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print("median")
#         else:
#             print("far")
# distance(20)












