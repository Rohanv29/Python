
# mat=[[1,2],[3,4],[5,6]]
# for i in mat:
#     print(i[0])
# wap to find largest elemnt in a list
numbers=[10,50,60,90,70,80]
max=0
for i in numbers:
    if(max<i):
        max=i
print(max)
i = -1
while abs(i) <= len(numbers):
    print(numbers[i])
    i -= 1

