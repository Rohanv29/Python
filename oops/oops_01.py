# class student:
#     def display(self):
#         print("Hello world")
# s1=student()
# s1.display()

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(name,age)
#     def display(self):
#         print("Hello world")
# s1=student("Rohan",18)
# s1.display()    

# class student:
#     def __init__(self):
#         self.__marks=90
#     def show(self):
#         print(self.__marks)
# s=student()
# s.show()


# class parent:
#     def show(self):
#         print("Parent Class")
# class Child(parent):
#     pass
# c=Child()
# c.show()

# class Animal:
#     def sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bank")
# d=Dog()
# d.sound()

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side
# s=Square(5)
# print(s.area())

