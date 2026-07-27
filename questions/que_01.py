# # calculate Average of three numbers
# x=int(input("enter marks of physics"))
# y=int(input("enter marks of chemistry"))
# z=int(input("enter marks of maths"))
# average=(z+y+x)/3
# print(average)


# degrree to kelvin
# x=int(input("enter temperature in celcius"))
# farenheit=(x*9/5)+32
# print(farenheit)

# n = input("Enter a number: ")
# result = int(n) + int(n * 2) + int(n * 3)
# print(result)

# num = int(input("Enter a four-digit number: "))

# first = num // 1000
# last = num % 10

# print("Sum =", first + last)


pizza = float(input("Enter Pizza price: "))
burger = float(input("Enter Burger price: "))
cold_drink = float(input("Enter Cold Drink price: "))

total_bill = pizza + burger + cold_drink
gst = total_bill * 0.05
grand_total = total_bill + gst

print("\n----- BILL -----")
print("Pizza       :", pizza)
print("Burger      :", burger)
print("Cold Drink  :", cold_drink)
print("----------------")
print("Total Bill  :", total_bill)
print("GST (5%)    :", gst)
print("Grand Total :", grand_total)