
from os import popen


def calculate_sum(a,b): 
    m = b/a 
    sum=m*(m+1)/2
    n=a*sum
    print("Sum of multiples of",a,"upto",b,"=",n) 
calculate_sum(7,49)





















