# def f1():
#     print("Enter a number")
#     n=int(input())
#     for e in range(1,n+1):
#         print(e**2 ,end=' ')
# print()
# f1()
# def greet():
#     print("Hello World")
# greet()
# def greet_student(name,age,rollno):
#     print("Hello ",name)
#     print(age)
#     print(rollno)
# greet_student("Rohan",18,"29")
# def greet_student(name):
#     print("Hello ",name)
# greet_student("Rohan")

# 1. create say _hello() which prints hello world
# def say_hello():
#     print("Hello World")
# say_hello()

# # 2. create welcome_student(name):
# def welcome_student(name):
#     print("Welcome",name)
# welcome_student("Rohan")

# # 3. create add(a,b) that returns the sum
# def add(a,b):
#     sum=a+b
#     print(sum)
# add(2,3)

# # 4.create cube(number)
# def cube(number):
#     cube=number*number*number
#     print(cube)
# cube(3)
# # create +ve number
# def check(num):
#     if(num<0):
#         print("Negative number")
#     print("Positive number")
# check(5)
# # create fullname
# def name(first,second):
#     name=first+second
#     print(name)
# name("Rohan","Verma")

# length=float(input("Enter length: "))
# breadth=float(input("Enter breadth: "))
# area =length*breadth

# print("Area of rectangle =",area)

# def add(a,b):
#     c=a+b
#     return c
# c=add(5,6)
# print(c)

def maximum(a,b):
    if(a>b):
        return a
    else:
        return b,''
c=maximum(3,5)
print(c)
