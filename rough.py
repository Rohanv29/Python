# import random
# number=random.randint(1,100)
# while(True):
#     guess=int(input("enter number to start the game"))
#     if(guess<number):
#         print("Wrong anss increase ur number")
#     elif(guess>number):
#         print("Wrong anss decrease ur number")
#     else:
#         print("you guessed right")
#         break
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# for i in range(1,6):
#     for j in range(i):
#         print(chr(97+j),end=" ")
#     print(" ")
# s="Hello World!! 1234"
# alp=0
# let=0
# for i in s:
#     if(i.isalpha() ):
#         alp+=1
#     elif( i.isdigit()):
#         let+=1
# print(let)
# print(alp)

# age=int(input("Enter your Age"))
# try:
#     if age <18:
#         raise ValueError ("age must be atleast 18");
#     print("Eligible to vote ")
# except ValueError as e:
#     print(e)

# marks=int(input("enter the marks"))
# assert 0 <= marks <=100 ,"marks must be bw 0 and 100"
# print("valid marks",marks)


# try:
#     marks=int(input("enter your marks"))
#     if marks<0 or marks >100:
#         raise ValueError ("Must  must be between 0 and 100")
# except  ValueError as e:
#     print("Invalid Input:",e)
# else:
#     print("Valid Marks ",marks)
#     print("Result Displayed Successfully")
# finally:
#     print("Student Marks Verification is Completed")

# class Car:
#     def Start(self):
#         print("Car started")
# c1=Car()
# c1.Start()

# class Student:
#     def _init_(self,name,rollno,branch):
#         self.name=name
#         self.rollno=self.rollno
#         self.branch=self.branch
#     def display(self):
#         print("Name:-",self.name)
#         print("Rollno:-",self.rollno)
#         print("Branch:-",self.branch)
# std1=Student("Rohan",101,"cs-aiml")
# std1.display()

# class abc:
#     x=0
#     def __init__(self,var):
#         abc.x+=1
#         self.var=var
# obj1=abc(15)
# obj2=abc(25)
# obj3=abc(35)
# print(obj1.var)
# print(obj2.var)
# print(obj3.var)

# import math
# class square:
#     def __init__(self,side):
#         self.side=side
#     @classmethod
#     def side_form_area(cls,area):
#         side=math.sqrt(area)
#         return cls(side)
# s1=square.side_form_area(16)
# print(s1.side)

# class Person:
#     def __init__(self,name):
#         self.name=name

# class Student(Person):
#     def __init__(self, name,rollno):
#         super().__init__(name)
#         self.rollno=rollno
#     def display(self):
#         print(self.name,self.rollno)

# class A:
#     def show(self):
#         print("A",end="")
# class B(A):
#      def show(self):
#             print("B",end="")
#             super().show()
# class C(A):
#      def show(self):
#             print("C",end="")
#             super().show()
# class D(B,C):
#      def show(self):
#             print("D",end="")
#             super().show()
# D().show()

# class Animal:
#     def sound(self):
#         print("Some Animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# class Cat(Animal):
#     def sound(Animal):
#         print("Meow")
# a=Animal()
# b=Dog()
# c=Cat()
# print(a.sound())
# print(b.sound())
# print(c.sound())

# class Complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=real
#     def __add__(self,other):
#         return self.real+other.real+self.imag+other.imag
# c1=Complex(1,2)
# c2=Complex(2,3)
# print(c1+c2)

class Student:
    def __init__(self,name,branch,marks):
        self.name=name
        self._branch=branch
        self._marks=marks
    def display(self):
        print("Name:",self.name)
        print("branch",self._branch)
        print("Marks",self._marks)
s1=Student("Rohan","CS_AIML",18)
s1.display()