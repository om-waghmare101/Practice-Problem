# #  71.Wap to print all the integers present in a list. 

# # FIRST WAY
# lst =eval(input("Enter a list: "))
# for i in lst:
#     print(i)

# # SECOND WAY
# lst =eval(input("Enter a list: "))
# for i in range(len(lst)):
#     print(lst[i])


#  72.Wap to find the length of homogenous tuple without len(). 

# tup = eval(input("Enter a Tuple: "))
# length = 0
# for i in tup:
#     length +=1
# print(length)





# #  73.Wap to extract all the even numbers present in a list. 
# lst =eval(input("Enter a list: "))
# for i in range(len(lst)):
#     if lst[i]%2!=0:
#         print(lst[i])




# #  74.Wap to remove duplicates from list  
# lst =eval(input("Enter a list: "))
# lstt = []
# for i in range(len(lst)):
#     if lst[i] not in lstt:
#        lstt.append(lst[i])
# print(lstt)
        



# #  75.Wap to reverse a string without using slicing. 
# # FIRST WAY
# s = input('Enter a String : ')
# e = ""
# for i in range(len(s)-1,0-1,-1):
#      e = e+ s[i]
# print(str(e))   

# # SECOND WAY

# s = input("Enter a String: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)




# #  76.wap to extract all the lowercase characters in a string only if the ascii value is  
# #     even.  
# s = input("Enter a String: ")
# for i in s:
#     if "a"<=i <="z" and ord(i)%2==0:
#         print(i)



#  77.Wap to check whether the last digit of an integer is even or not. 
# n = int(input("Enter a number: "))
# c = 0
# for i in str(n):
#     c = int(i)
# if c % 2 == 0:
#     print("Even")
# # else:
#     print("Odd")

   



# #  78.Wap to extract all the key value pairs from the dictionary only if the keys are of  
# #    string datatype and values are integers. 
# # FIRST WAY
# d = eval(input("Enter a dictionary: "))
# for i in d:
#     if type(i) == str and type(d[i]) == int:
#         print(i, ":", d[i])

# # SECOND WAY
# d = eval(input("Enter a dictionary: "))
# for key in d.keys():
#     if type(key) == str and type(d[key]) == int:
#         print(key, d[key])



# #  79.Wap to extract key value pairs from the dictionary only if both keys and values 
# #     are exactly same.
# d = eval(input("Enter a dictionary: "))
# for i in d:
#     if i==d[i]:
#         print(i, ":", d[i])


# #  80.Wap to get the following output using len function. 
# #      S=’power star’ 
# #      Out={‘power’:5,’star’:4} 
# s = input("Enter a String: ")
# words = s.split()
# d = {}
# for i in range(len(words)):
#     d[words[i]] = len(words[i])
# print(d)


# #  81.Wap to get the following output. 
# #      S=’power star’ 
# #      Out={‘power’:’rewop’,’star’:’rats’} 
# s = input("Enter a String: ")
# words = s.split()
# d = {}
# for i in range(len(words)):
#     d[words[i]] = words[i][::-1]
# print(d)


# #  82. wap to extract all the non default  values from a list. 
# lst = eval(input("Enter a List: "))
# for i in lst:
#     if i:
#         print(i)



# #  83.Wap to check whether the list is homogenous or not.
# lst = eval(input("Enter a List: "))
# same = True
# for i in range(len(lst)):
#     if type(lst[i]) != type(lst[0]):
#           same = False 
#           break
# if same :
#      print("Homogenous")
# else: 
#         print("Not Homogenous")


# #  84.Wap to replace the space by * present in a string .
# s = input("Enter String : ")
# d=""
# for i in range(len(s)):
#     if s[i] ==" ":
#       d = d + "*"
#     else :
#        d = d + s[i]
# print(d)


# #  85.Wap to count the number of occurrence of a specified character. 
# s = input("Enter String: ")
# ch = input("Enter Character: ")
# count = 0
# for i in range(len(s)):
#     if s[i]==ch :
#         count += 1
# print(count)
        



# #  86. Wap to get the following output. 
# #                     S=’always keep smiling’ 
# #                     Out-‘syawla peek gnilims’ 

# #  FIRST WAY 
# s = input("Enter String: ")
# rev = ""
# for i in range(len(s)-1, -1, -1):
#     if s[i] == " ":
#         print(rev, end=" ")
#         rev = ""
#     else:
#         rev = rev + s[i]
# print(rev)

# # SECOND WAY
# s = input("Enter String: ")
# result = ""
# for word in s.split():
#     result = result + word[::-1] + " "
# print(result)


# 87. Wap to get the following output. 
#     In=’push maadi kushi padi’ 
#     Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’} 

# s = input("Enter a string: ")
# words = s.split()
# dect= {}
# empty = 0
# for i in range(len(words)):
#     if i%2!= 0:
#         empty = len(words)//2 
#         dect [i] = words[empty]


# # 88.Wap to toggle a string. 
# s = input("Enter a string: ")
# ts =""
# for i in range(len(s)):
#     if "a"<=s[i]<="z":
#         ts = ts+ s[i].upper()
#     elif "A"<=s[i]<="Z":
#         ts = ts + s[i].lower()
#     else:
#         ts = ts + s[i]
# print(ts)



# # 89.Wap extract upper, lower, digit and special characters present in a string to different. 
# #     output variable.
# s = input("Enter a string: ")
# lower = ""
# upper = ""
# spacial = ""
# digit = ""
# for i in range(len(s)):
#     if "a"<=s[i]<="z":
#         lower = lower + s[i]
#     elif "A"<=s[i]<="Z":
#         upper = upper + s[i]
#     elif"0"<=s[i]<="9":
#         digit = digit + s[i]
#     else:
#         spacial = spacial + s[i]
# print(lower)
# print(upper)
# print(digit)
# print(spacial)





# 90. Wap to get the following output. 
#         S=’hai hello ‘ 
#         Out={‘hai’:’ai’,’hello:’eo’}
# S='hai hello '
# word = S.split( )

# for i in range(len(word)):
#     vowel= ""
#     if word[i] in "aeiou":
#         vowel = vowel + word[i]
#     else :
#         pass
# print(word[i],":",vowel)





# 91. Wap to get the following output. 
#S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']
#         Out=[‘com’,’py’,’html’,’org’]
# S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']
# out = []

# for i in S:
#     word = i.split('.')
#     out.append(word[-1])
# print(out)





# 92. Wap to get the following output. 
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’] 
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’], ’org’:[‘www’]} 

# S = ['jiocinema.com', 'file.py', 'web.html',
#      'amazom.com', 'www.org', 'python.py']
# cat = []
# dom = []
# for i in S:
#     a = i.split('.')
#     if a[-1] not in dom:
#         dom.append(a[-1])
#         cat.append([a[0]])
#     else:
#         cat[dom.index(a[-1])].append(a[0])

# Out = dict(zip(dom, cat))
# print(Out)






#    93.Wap to get the following output. 
#    L=[‘hai’,34,3.4,’hello’,90,’byebye’] 
#   Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’} 
# L=['hai',34,3.4,'hello',90,'byebye'] 
# out = {}
# li=[]

# for i in L:
#     if type(i) == str:
#         li.append((i, i[0] + i[-1]))

# print(dict(li))




# 94.wap to get the following output. 
#   In=’hello’ 
#   Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’} 
# n='hello'
# out = []
# key=[]
# value=[]
# for i in range(len(n)):
#     key.append(i)
#     value.append(n[i])
# out = dict(zip(key,value))
# print(out)



# 95.Wap to extract all the string values present in list only if the string is palindrome.
# li = [1,3,'hello',[1,2,3,],'nitin','human']
# for i in range(len(li)):
#     if type(li[i]) == str : 
#         if li[i] == li[i][::-1]:
#             print(li[i])
   





# 96.Wap to return the positions of vowels present in the given string. 


# 97.Wap to check whether the given collection is having nested collection or not. 


# 98.Wap to count the number of words in a string. 


# 99.Wap to check whether the number is neon number or not. 
#     N=9→9**2=81→8+1=9 


# 100.Wap to find the longest word in a string. 



# 102.wap to print the square of all the integers present in a list. 



# 101.Wap to replace the special character present in a string by space. 


# 103.Wap to extract all the odd number present at even index from a list. 


# 104.Wap to extract all the mutable values present in a tuple. 


# 105.Wap to get the following output. 
#                In=’10100011231’ 
#                Out=’010111000’    ( 0→1 and 1→0 if it is other than 0 &1 ignore) 



# 106.Wap to get the following output. 
#               In=’abacbaacc’ 
#               Out={‘a’:4,’b’:2,’c’:3} 



# 107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype. 



# 108.Wap to get the following output. 
#                   In=’127342’ 
#                   Out=’242173’  (extract even and odd digits separately and concatenate both)



# 109.Wap to checek whether the string is having only lowercase or not using continue. 



# 110.Wap to find the sum square of individual digits of a string.
