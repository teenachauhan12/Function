numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
print (max(numbers_list))




a=[1,2,3,4,5,6]
print(len(a))




def say_hello(name):
    print("Hello ", name)
    print("How are you?")
say_hello("Aatif")





def add_numbers(number1, number2):
    print("I will add two numbers.")
    print(number1 + number2)
add_numbers(120, 50)
num_x = 134
name = "Rinki"
add_numbers(num_x, name)









def say_hello_language(name, language):
    if language == "hindi":
        print("Namaste ", name)
        print("Aap kaise ho?")
    elif language == "punjabi":
        print("Sat sri akaal ", name)
        print("Tuhada ki haal hai?")
    else:
        print("Hello ", name)
        print("How are you?")
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")





def say_hello_people(name_x, name_y, name_z, name_a):
    print("Namaste ", name_x) 
    print("Alah hafiz ", name_y) 
    print("Bonjour ", name_z)  
    print("Hello ", name_a) 
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")





def icecream(*flavours):
 for flavour in flavours:
  print("i love"+flavour)

icecream("chocolate", "butterscotch","vanilla","strawberry")





def attendance(name,status="absent"):
    print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh")




def greet(names):
    for name in names:
        print("Welcome", name)


greet("Rinki", "Vishal", "Kartik", "Bijender")














