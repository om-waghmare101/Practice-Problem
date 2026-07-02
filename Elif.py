# # 21. Wap to check whether the char is uppercase, lowercase, digit or special char.
# c = input("Enter Character : ")
# if "A"<= c<="Z":
#     print("Character is in Uppercase")
# elif "a"<=c<="z":
#     print("Character is in Lowercase")
# elif "1"<=c<="9":
#     print("Character is a Digit")
# else:
#     print("Character is a Spacial Character")



# # 22. Wap to check whether the given integer is single digit or two digits or three  
# # digits or more than three digits. 
# a = input("Enter Integer : ")
# if len(a)==1:
#     print("Integer is in single digit")
# elif len(a)==2:
#     print("Integer is in Two digit")
# elif len(a)==3:
#     print("Integer is in Three digit")
# else:
#     print("Integer is more the three digit")


# # 23.Wap to check the given points are lying in which quadrant. 
# degree = int(input("Enter Degree : "))
# if 0<= degree <=90 :
#     print("FIRST QUDRANT")    
# elif 90<degree<=180 :
#     print("SECOND QUDRANT")
# elif 180<degree<=270 :
#     print("THIRD QUDRANT")
# elif 270< degree <=3690 :
#     print("FOURTH QUDRANT")



# # 24. Wap to find the greatest of 3 numbers. 
# a = int(input("Enter Number 1 : "))
# b = int(input("Enter Number 2 : "))
# c = int(input("Enter Number 3 : "))

# if (a>b and a>c):
#     print("First Number is Grater")
# elif(b>a and b>c):
#     print("Second Number is Grater")
# else:
#     print("third Number is Grater")
              


# # 25. Wap to find the smallest of 3 numbers.
# a = int(input("Enter Number 1 : "))
# b = int(input("Enter Number 2 : "))
# c = int(input("Enter Number 3 : "))
# if (a<b and a<c):
#     print("First Number is Smallest")
# elif(b<a and b<c):
#     print("Second Number is Smallest")
# else:
#     print("third Number is Smallest")

  
# # 26.Wap to check the relation between two integer numbers.
# a = int(input("Enter Number 1 : "))
# b = int(input("Enter Number 2 : "))
# if a>b:
#     print("First number is grater")
# elif b>a:
#     print("Second number is grater")
# else:
#     print("Both are equal")


# # 27. Consider a character input if it is uppercase convert it into lowercase, if it is         
# # lowercase convert it into uppercase, if it is digit print the reminder when  it is 
# # divided by 3 else if it is special character print it’s ASCII value. 
# a = input("Enter character  : ")
# if "A"<=a<="Z":
#     print(a.lower())
# elif "a"<=a<="z":
#     print(a.upper())
# elif "0"<=a<= "9":
#     b=int(a)/3
#     print(b)
# else:
#     print("Spacial Character")


# # 28.Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the  
# # given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of  
# # both 3 and 5.

# a = int(input("Enter Number  : "))
# if a%3==0 and a%5==0:
#     print("FIZZBUZZ")
# elif a%3==0:
#     print("FIZZ")
# elif a%5==0:
#     print("BUZZ")
# else:
#     print("Does not divide by 3 and 5")