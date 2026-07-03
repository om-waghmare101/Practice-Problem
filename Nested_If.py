# # 29.Wap to login into the Instagram with valid username and password.(enter       
# #     password only if the user name is valid) 

# user = "user@123"
# pas = "pas@12"
# entry = input("Enter User ID :")
# if entry == user :
#     pasentry = input("Enter Password : ")
#     if pasentry == pas :
#         print("Login Sucessfull!!!")
#     else:
#         print("Incorrect Password")
# else:
#     print("Incorrect User ID")



# # 30. Wap to print the middle value of a list only if it is string. 
# a =eval (input("Enter a list : "))
# if len(a) %2==1:
#     print("Have middle value")
#     b = len(a)//2 
#     if type(a[b])== str:
#         print("its an string and value is ",b)
#     else:
#         print("not a string")
# else:
#     print("Dont Have middle value")




# # 31.Wap to check whether the character is vowel or consonant. 
# a = input("Enter character : ")
# if "a"<=a<="z" or "A" <= a <="Z":
#     if a in "aeiou":
#         print("Its an Vowel")
#     else:
#         print("Its an consonant")
# else:
#     print("Incorrect character")





# # 32.Wap to find the greatest of 4 numbers. 
# a = int(input("Enter Number 1: "))
# b = int(input("Enter Number 2: "))
# c = int(input("Enter Number 3: "))
# d = int(input("Enter Number 4: "))

# if a >= b:
#     if a >= c:
#         if a >= d:
#             print("First number is greatest")
#         else:
#             print("Fourth number is greatest")
#     else:
#         if c >= d:
#             print("Third number is greatest")
#         else:
#             print("Fourth number is greatest")
# else:
#     if b >= c:
#         if b >= d:
#             print("Second number is greatest")
#         else:
#             print("Fourth number is greatest")
#     else:
#         if c >= d:
#             print("Third number is greatest")
#         else:
#             print("Fourth number is greatest")


# # 33. Wap to print the value as it is only if the length of the value is even. 
# a = eval(input("Enter value: "))
# if type(a) in [str, list, tuple, set, dict]:
#     if len(a) % 2 == 0:
#         print(a)
#     else:
#         print("Length is odd")
# else:
#     print("This value has no length")





# 34.Wap to print the last value of a list only if it is palindrome string starting with   
#     vowel. 
a = eval(input("ENTER PROPER DATA: "))
if a[-1]==a[::-1]:
    if a[0] in"aeiou":
        print("Its an vowel",a[-1])
    else:
        print("Not Vowel")
else:
    print("Input Incorrect")



# 35.Wap to print the reversed string only if it is starting with vowel ,ending with     
#     consonant and having a middle value. 





# 36.Wap to find the second greatest of 4 values. 




# # 37.Wap to find the smallest of 4 numbers. 
# a = int(input("Enter Number 1: "))
# b = int(input("Enter Number 2: "))
# c = int(input("Enter Number 3: "))
# d = int(input("Enter Number 4: "))

# if a <= b:
#     if a <= c:
#         if a <= d:
#             print("First number is Smallest")
#         else:
#             print("Fourth number is Smallest")
#     else:
#         if c <= d:
#             print("Third number is Smallest")
#         else:
#             print("Fourth number is Smallest")
# else:
#     if b <= c:
#         if b <= d:
#             print("Second number is Smallest")
#         else:
#             print("Fourth number is Smallest")
#     else:
#         if c <= d:
#             print("Third number is Smallest")
#         else:
#             print("Fourth number is Smallest")




# 38. Write a program to print middle Character of the given string only if it is upper                
#     Case Character.