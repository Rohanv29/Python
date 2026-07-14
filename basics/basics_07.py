import  keyword
print(keyword.kwlist)
a=input("enter a word")
if a in keyword.kwlist :
    print(True)

else :print(False)