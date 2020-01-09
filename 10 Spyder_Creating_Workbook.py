#!/user/bin/env python

# -*- coding: utf-8 -*-
"""
hw2.py

Requirements:
    - python 3
        
How to run:
    python3 hw2.py
"""

x = 3
if x % 3 == 0 :
    print("Fizz")
"""
Documentation:
    - Make any numeric value equal to x 
    - This function will print out "Fizz" if the numeric value is divisible by 3        
"""

x = 5
if x % 5 == 0 :
    print("Buzz")
"""
Documentation:
    - Make any numeric value equal to x 
    - This function will print out "Fizz" if the numeric value is divisible by 5
"""
    
x = 15
if (x % 3 == 0) and (x % 5 ==0):
    print('Fizz Buzz')
elif x % 3 == 0:
    print('Fizz')
elif x % 5 == 0:
    print('Buzz')
"""
Documentation:
    - Make any numeric value equal to x 
    - This function will print out "Fizz" and/or "Buzz" if the numeric value is divisible by 3 and/or 5   
"""


def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 ==0):
        print(str(x) + ' = Fizz Buzz')
    elif x % 3 == 0:
        print(str(x) + ' = Fizz')
    elif x % 5 == 0:
        print(str(x) + ' = Buzz')
    else:
        print(str(x) + "= NOT DIVISIBLE BY 3 OR 5")
    
fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)

"""
Documentation:
    - Type out "fizzbuzz()" and put any numeric value into the paraenthesis 
    - This function will print out "Fizz" and/or "Buzz" if the numeric value is divisible by 3 and/or 5  
    - If its not divisible by 3 or 5, then the function will print out the following:
            * = NOT DIVISIBLE BY 3 OR 5"
"""    