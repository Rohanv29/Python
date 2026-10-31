
# import math 
# def total(*args):
#     print(sum(args))

# total(10, 20, 30)

# print(math.isqrt(4))

# t = (10, 20, 30, 20)

# print(t[0])
# print(t[1:3])
# print(t.count(20))
# print(t.index(30))

# d = {"a": 10, "b": 20}

# d["c"] = 30
# d["a"] = 100

# print(d)
# print(d.keys())
# print(d.values())

sentence = "python is easy and python is powerful"
# code here
# freq={}
# for i in sentence:
#     freq[i]=freq.get(i,0)+1
# print(freq)
# print(sorted(freq))

# marks = {
#     "Amit": 82,
#     "Neha": 95,
#     "Ravi": 76,
#     "Priya": 89
# }
# topp=max(marks,key=marks.get)
# print(topp)

numbers = (10, 20, 30, 40, 50, 60, 70)

*first, middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)