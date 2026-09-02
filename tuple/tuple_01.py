t = (10, 20, 30, 40,20,10,40,30)
print(t)
s=("rohan","rachit","yashvi")
print(s)
print(type(s))
print(type(t))
# t.append(10,30)
print(t)

print(t.count(20))
print(t.count(40))

print(t.index(40))


t = (False, False, True, False)

print(any(t))
t = (10, 20, 0, 30)

print(any(t))
names = ("Rohan", "Rachit", "Pushkar")

for i, name in enumerate(names):
    print(i, name)



t = ((10, 20), (30, 40), (50, 60))

print(t)

print(t[0])
print(t[1])
print(t[2])


t1 = (10, 20, 60)
t2 = (10, 20, 40)

print(t1 < t2)

a = ("apple", "banana")
b = ("apple", "cat")

print(a < b)