# print("hello world")
# a=10
# b=2
# print(a+b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a*b)


# #Variables
# x=int(5)
# y=str(5.58)
# z=float(5.594)

# print(x)
# print(y)
# print(z)
# x=x+1
# print(type(x))
# print(type(y))
# #assigning
# # x,y,z= "Orange","Apple", "Banana" #Unpacking
# # print(x)
# # print(y)
# # print(x)

# fruits=["Orange","Apple", "Banana"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# #Tupples are Immuatable like frozensets
# equipemnts=["sensors","actuators","control systems"]
# x,y,z=equipemnts
# print(x)
# print(y)
# print(z)

# x = "Sayma"
# y = "is"
# z = "awesome"
# print(x, y, z)

# print(x+y+z)

# x=5 
# y= "John"
# z=6
# print(x,y,z)


# x= "fine"

# def myfunc():# global vairables
#     print("I am " +x)
# myfunc()

# # r=5
# pi=3.1416
# r =int(input("enter r: ", ))

# print(pi*r*r)

# # print(type(r))


# r =int(input("enter r: ", ))
# def area_circle(pi=3.1416):
#     print(pi*r*r)
# area_circle(pi=3.1416)

# def area_circle(radius, pi=3.1416):
#     return pi * radius * radius

# # Example 1: Using the function in different parts of a program
# radius1 = 5
# area1 = area_circle(radius1)
# print("Area of circle with radius", radius1, "is:", area1)

# radius2 = 7
# area2 = area_circle(radius2)
# print("Area of circle with radius", radius2, "is:", area2)

# # Example 2: Testing the function
# def test_area_circle():
#     # Test case 1: Radius = 5
#     assert area_circle(5) == 78.54  # Expected area for radius 5 is approximately 78.54

#     # Test case 2: Radius = 0
#     assert area_circle(0) == 0  # Expected area for radius 0 is 0

#     # Test case 3: Radius = 10, custom pi value
#     assert area_circle(10, pi=3.14) == 314  # Expected area for radius 10 with pi=3.14 is 314

#     print("All tests passed!")

# # Run the test function
# test_area_circle()



# r=6
# print(pi*r*r)
# print(6*6*3.1416)


# print("Both conditions are true")

# input("Please enter a:")
# input("Please enter b:")

# a=int(input("Enter the value for a:"))
# b=int(input("Enter the value for b:"))
# add=a+b
# sub=a-b
# while True:
#     print("Please + for add: ")
#     print("Please - for sub: ")
# user= input( " :")
# if user in ("add") or user =="+" :
#  print(add)
# print(a/b)

# print(a//b)
# print(a**b)
# print(a*b)



# print("Both conditions are true")

# def add(x,y):
#     return x+y
# result=add(2,2)
# print("The sum of the numbers is : ", result)  

# def sub(x,y):
#     return x-y
# x=int(input("Enter the number_1 :"))
# y=int(input("Enter the number_2 : "))

# result=sub(x,y)
# print("The difference between number is : ", result)

#Global Variable

# x=4
# def myfunc():
#     global x
#     x=6
# myfunc()

# print(5+x)

# def zunayed(x,y):
#     return x+y
# result=zunayed(3,4)
# print("sum of numbers:",result)

# result_1=zunayed(5,7)
# print("sum of numbers:",result_1)



# def area_of_circle(r,pi=3.1416): #local_variables
#     return pi*r*r
# r=int(input("enter the number="))
# result=area_of_circle(r)
# print("area of the circle is: ", result)

# r_1=5 #global_variables
# result_1=area_of_circle(r_1)
# print("area of the circle is: ", result_1)

# # while loop
# i=1
# while (i<6):
#     print(i) #print i then the statement under it will excute
#     i+=1
#     break #this command is for break after excution for first time

# i=1
# while(i>-6):
#     print(i)
#     if(i==2):
#         break
#     i-=1

#Continue
# i=0
# while (i<6):
#     i+=1
   
#     if(i==2): 
#      continue
 
#     print(i)

# name=input("Enter your name :")

# if(name==""):
#     print("Name is not entered")

# else:
#   print("your name is: ",name)


# name=input("Enter your name :")

# while(name==""):
#     print("Name is not entered")
#     name=input("Enter your correct name : ")
    
# print("your name is: ",name)
    
# age=int(input("Enter your age :"))

# while(age==0 or age<100):
#     print("Age is not valid")
#     age=int(input("Enter your correct age : "))
    
# print("your age is: ",age)

Food=input("Enter your Food(enter q to eascape) : ")

while not(Food=="q"):
    print("your Favourite food is: ",Food)
    print(Food,"is a very good choice")
    Food=input("Please enter more your Food(enter q to eascape) : ")

while not(Food=="q"):
    print("your another Favourite food is: ",Food)
    Food=input("Please enter more your Food(enter q to eascape) : ")
    
print("bye")




    
    






    
    




   



   
    


 
