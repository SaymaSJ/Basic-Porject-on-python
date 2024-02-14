#circle


#Area
def A(r,pi=3.1416):
    return pi*r*r
#Circumference

def P(r,pi=3.1416):
    return 2*pi*r

while True:
    print("Options:")
    print(f"1.Enter circle for cirle) ")
    print(f"2.Enter rectangle for rectangle) ")
    print("Enter 'exit' to end the program")


    user_input=input("=")
    if user_input == "exit":
        break

    if user_input in ("circle"):
       print("Enter c for area of the circle:")
       print("Enter p for Circumference of the circle:")
    
    if user_input in ("c" ,"p"):
       r=int(input("Enter radius: "))


    if(user_input=="c"):
     
     result=A(r,pi=3.1416)
     print("Area of the circle",result)

    elif (user_input=="p"):
    
     result_1=P(r,pi=3.1416)
     print("Circumference of the circle",result_1)

    else:
     print("Invalid input")





# #task_1
# r_1=int(input("Enter the radius of the circle: " ))
# A_1=A(r_1)
# print("The area of the circle is : " ,A_1)

# #task_2
# r_2=5
# A_2=A(r_2)
# print("The area of the circle is : " ,A_2)










# #task_1
# r_1=int(input("Enter the radius of the circle: " ))
# result_1=area_of_circle(r_1,pi=3.1416)
# print("The area of the circle is " ,result_1)

# #task_2
# r_2=5
# result_2=area_of_circle(r_2,pi=3.1416)
# print("The area of the circle is " ,result_2)




# def area_circle(radius, pi=3.1416):
#     return pi * radius * radius

# Example 1: Using the function in different parts of a program
# radius1 = 5
# area1 = area_circle(radius1)
# print("Area of circle with radius", radius1, "is:", area1)

# radius2 = 7
# area2 = area_circle(radius2)
# print("Area of circle with radius", radius2, "is:", area2)