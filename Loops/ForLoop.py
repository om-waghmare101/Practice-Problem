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