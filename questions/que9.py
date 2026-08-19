# # WAP to input a string and display it
# s=input("Enter a String")
# print(s)
# # wap to find length of the string without using len()
# s=input("Enter a String")
# l=0;
# for char in s:
#     l+=1
# print(l)
def numbers():
    yield 10
    yield 20
    yield 30
g=numbers()
print(next(g)) #output:-10
print(next(g)) #output:20
print(next(g))#output:30