# # for i in range(1,11):
# #     print(i)
# i=1
# while(i<11):
#     print(i)
#     i+=1
# import re
# text="Python Programming Python"
# #result=re.search('Python',text)
# result=re.match('Python',text)
# print(result)


# Key diff between match and search
# re.match() only scans for a match starting at the first char of a string at the first char of a string.match
# # re.search9
# import re 
# st="my roll no is 12 and my friend is 21"
# print(re.findall(r'\d+',st))

# print(re.findall(r'[A-z a-z]',st))
# import re 
# st="my roll no is 12 and my friend is 21"
# print(re.findall(r'\d+',st))

# print(re.findall(r'[aeiou]',st))
# find words having exactly 5characters
 
# st="my roll no is 12 and my friend Rohan is 21"
# print(re.findall(r'\d+',st))

# print(re.findall(r'\b[a-zA-Z]{5}\b',st))
import re
