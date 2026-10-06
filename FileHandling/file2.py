try:
    a=int(input("Enter a Number"))
    b=int(input("Enter another Number"))
    print("result : ",a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid Integers")