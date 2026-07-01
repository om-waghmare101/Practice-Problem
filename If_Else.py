# '''
# 11. Wap to check whether the data is mutable or not. 
# '''
# a=eval(input("enter data"))
# if type(a) in[list,set,dict]:
#     print("data is mutable")
# else:
#     print("data is immutable")


# '''
# 12. Wap to check whether the given character is digit or not. 
# '''
# a=eval(input("enter data"))
# if type(a)==int:
#     print("character is digit")
# else:
#     print("not digit")


# ''''
# 13. Wap to check whether the given character is special or not. 
# '''
# a=input("enter data")
# if a in "!@#$%^&*()":
#     print("Spacial")
# else:
#     print("Not Special")


# '''
# 4. Wap to check whether a list consists of middle value or not. 
# '''
# a=eval(input("ENTER DATA "))
# if len(a)%2==1:
#     print("Have middle values")
# else:
#     print("dont have middle values")


# '''
# 5. Wap to check whether the number is even or odd. 
# '''
# a= int(input("ENTER A NUMBER "))
# if a%2==0:
#     print("EVEN")
# else:
#     print("ODD")


# '''
# 16. Wap to check whether the given data is mutable or immutable. 
# '''
# a = eval(input("Enter Data: "))
# if type(a) in [list,set,dict]:
#     print("Data is Mutable")
# else:
#     print("Data is Unmutable")



# '''
# 17. Wap to check whether 2 values are pointing to the same memory or not. 
# '''
# a = eval(input("Enter first Data: "))
# b = eval(input("Enter second Data: "))
# if id(a) == id(b):
#     print("Same Memory Location")
# else:
#     print("Different Memory Location")


# '''
# 18. Consider a tuple of length 2 and check whether the tuple is homogenous or not.
# '''
# a = eval(input("Enter Tuple Data: "))
# if type(a[0]) == type(a[1]):
#     print("tuple is homogenous")
# else:
#     print("tuple is heterogenous")


# '''
# 19. Wap to check whether the string is palindrome or not. 
# '''
# a = eval(input("Enter String Data: "))
# b = a[::-1]
# if a==b:
#     print("data is palindrome")
# else:
#     print("data is not palindrome")

# '''
# 20. Wap to check whether the number is positive or negative.
# '''
# a = eval(input("Enter Number : "))
# if a<0:
#     print("Number is negative")
# else:
#     print("number is positive")