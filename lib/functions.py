#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Joan")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
    return num1 + num2

add(10, 9)   

def halve(number):
    return number / 2

halve(60)    

def my_function(param):
    print("Running my_function")
    return param + 1

# New code goes here!

my_function_return_value = my_function(1)
# Running my_function
# 2
my_function_return_value
# 2