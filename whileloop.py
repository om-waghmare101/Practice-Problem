# #  39.Wap to print python for 5 times. 
# n = 1
# while (n<=5):
#     print("PYTHON")
#     n+=1

# #  40.Wap to print n natural numbers. 
# n = int(input("Enter a number: "))
# i=0
# while i<=n:
#     print(i)
#     i+=1


# # WAP to print first n odd numbers
# n = int(input("Enter a number: "))
# i = 1
# count = 1
# while count <= n:
#     print(i)
#     i += 2
#     count += 1


# #  41.Wap to print multiplication table for n.  
# n = int(input("Enter a number: "))
# i = 1
# while i<=10:
#     print(n ,"*" , i ,"=", i*n)
#     i+=1
   

# #  42.Wap to find the sum of n natural numbers. 
# n = int(input("Enter a number: "))
# i = 1
# b = 0 
# while i <= n:
#     b = b+ i 
#     i+=1
# print(b)


# #  43. Wap to find the product of n natural numbers or factorial of a number.
# n = int(input("Enter a number: "))
# i = 1
# b = 1 
# while i<=n:
#     b = b * i 
#     i +=1 
# print(b)


# #  44.Wap to print all the characters of a string. 
# s = "WORLD"
# i = 0 
# while i<len(s):
#     print(s[i])
#     i+=1


# #  45.Wap to print all the characters present at even index of a string. 
# s = "HELLOWORLD"
# i = 0
# while i < len(s):
#     if i% 2 == 0:
#         print(s[i])
#     i+=1
     

# #  46.Wap to extract all the lowercase characters present in a string. 
# s= "PyThoN"
# i = 0
# while i < len(s):
#     if s[i] ==s[i].lower():
#         print(s[i])
#     i = i +1


# #  47.Wap to extract all the vowels present in a string. 
# s = "HELLOWORLD"
# i = 0 
# while i< len(s):
#     if s[i].lower() in "aeiou":
#         print(s[i])
#     i = 1+i


# #  48.Wap to print factors of a integer number. 
# n = int(input("Enter a Number"))
# i = 1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1


# #  49.Wap to toggle a string. 
# s = "HaPPy"
# i = 0 
# while i<len(s):
#     if s[i] == s[i].upper():
#         print(s[i].lower())
#     else:
#         print(s[i].upper())
#     i+=1


# #  50.Wap to reverse the given number. 
# n = int(input("Enter Number: "))
# rev = 0 
# while n > 0:
#     digit = n%10
#     rev = rev * 10 + digit
#     n = n//10
# print(rev)



# #  51.Wap to find the sum of individual digits of a number. 
# n = int(input("Enter Number: "))
# total = 0
# while n > 0:
#     digit = n % 10
#     total = digit + total 
#     n = n//10
# print(total)



# #  52. Wap to check whether the number is perfect or not. 
# n = int(input("Enter Number : "))
# i=1
# sum = 0
# while i<=n-1:
#     if n%i == 0:
#         print(i)
#         sum = sum + i
#     i+=1
# if sum == n:
#     print ("Perfet Number")
# else:
#     print("Not perfect number")



# #  53.Wap to login to phonepe by entering correct otp. 
# otp = 2345
# value = int(input("Enter OTP: "))

# while value != otp:
#     print("Incorrect OTP")
#     value = int(input("Enter OTP Again: "))
# print("OTP is correct. Login Successful.")



# #  54.Wap to run infinite loop until user enters the correct password. 
# otp = "admin123"
# value = input("Enter OTP: ")

# while value != otp:
#     print("Incorrrect password")
#     value = int(input("Enter password]: "))   
# print("Password is correct")



# #  55.Wap to extaract all the even integers present in a tuple at odd index. 
# c = eval(input("Enter a tuple"))
# i = 0
# while i<len(c):
#     if c[i]%2==0:
#         if i% 2 ==1 :
#             print(c[i])
#     i+=1



# #  56.Wap to remove duplicates from a list without converting into set. 
# c = eval(input("Enter List"))
# i=0
# b=[]
# while i<len(c):
#     if c[i] not in b:
#       b.append(c[i])
#     i += 1
# print(b)


# #  57.Wap to find the sum of all the odd numbers between the given range. 
# i = int(input("Enter 1 number :"))
# n2 = int(input("Enter 2 number :"))
# result = 0 
# while i<=n2:
#     if i%2==1:
#       result = result + i
#     i+=1
# print(result)


# #  58.Wap to find the greatest number in a given list of integers. 
# lst = eval(input("Enter a list : "))
# i = 0
# gratest = lst[0]
# while i<len(lst):
#     if lst[i] >= gratest:
#         gratest = lst[i]
#     i+=1
# print(gratest)



# #  59.Wap to find the sum of cube of a number in a string. 
# s = input("Enter a string :")
# i = 0 
# sum = 0
# while i< len(s):
#     if "0"<= s[i] <= "9" :
#         sum = int(s[i])**3+sum
#     i+=1
# print(sum)



# #  60.Wap to check whether the number is Armstrong or not.
# n = int(input("Enter a number: "))
# original = n
# i = 0
# b = 0
# while n>0:
#     i = n%10
#     b = i**3  + b
#     n=n//10
# if b==original:
#     print(" Number is Armstrongg")
# else: 
#         ("Not Armstrong")




# #  61.Wap to get the following output. 
# #     A=’10011100’   B=’00110101’    out=4(count of positions having same values) 
# A="10011100"  
# B="00110101"
# i = 0 
# count = 0
# while i< len(A):
#     if A[i] == B[i]:
#         count +=1
#     i+=1
# print(count)




#  62.Wap to check the given number is prime or not. 




#  63.Wap  to check whether the number is palindrome or not. 





#  64.Wap to find the HCF of two numbers. 





#  65.Wap to convert binary to decinaml. 







#  66. Wap to convert decimal to binary. 






#  67.Wap to count the number of words in a string. 





#  68.Wap to guess the number. 





#  69.Wap to find the common elements in two sets 






#  70.Wap to find the product of all the digits present in a number. 