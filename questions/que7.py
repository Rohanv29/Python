# s="Python Programming"
# n=len(s)
# vowels=0
# consonants=0
# for ch in s:
#     if(ch in "AEIOUaeiou"):
#         vowels+=1
#     elif(ch == ' '):
#         continue 
#     else:
#         consonants+=1
# print(consonants)        
# print(vowels)

# s="Python Programming"
# freq={}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1

# print(freq)
# s = "Python Programming"
# for i in range(len(s)):
#     repeat = False
#     for j in range(len(s)):
#         if i != j and s[i].lower() == s[j].lower():
#             repeat = True
#             break
#     if not repeat:
#         print(s[i])   # prints original case
#         break




# # WAP to find the square of the number using list comprehensive 
# squares = [i ** 2 for i in range(1, 6)]
# print(squares)
# names=["bhaalu","hathi","saanp","naagin"]
# uppercase=[name.upper() for name in names]
# print(uppercase )
# marks=[54,65,98,35,25,17]
# res=["pass" if mark>40 else "fail" for mark in marks]
# print(res)
# sentence="MY name is Rohann Verma"
# word_len=[len(word) for word in sentence.split()]
# print(word_len)


# student=[
#     ['Rohan',20],
#     ['Rachit',30],
#     ['Abhila',40],
#     ['NINJAAA',50],
#     ['Ishwan',60]
# ]
# print(student[1][1])
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print (matrix)
# for row in matrix:
#     for value in row:
#         print(value, end=' ')
#     print()

# mat = [[[0 for j in range(4)] for i in range(3)]]

# for row in mat:
#     print(row)

mat = [[1,2,3,4],
       [5,6,7,8],
       [9,                                            10,11,12]]

sum = 0

for row in mat:
    for element in row:
        sum += element

print(sum)