#area of the circle

def area_of_circle(r,pi=3.1416):
    return pi*r*r

# #task_1
# r_1=int(input("Enter the radius of the circle: " ))
# result_1=area_of_circle(r_1,pi=3.1416)
# print("The area of the circle is " ,result_1)

# #task_2
# r_2=5
# result_2=area_of_circle(r_2,pi=3.1416)
# print("The area of the circle is " ,result_2)


#task_1
r_1=int(input("Enter the radius of the circle: " ))
area_1=area_of_circle(r_1)
print("The area of the circle is : " ,area_1)

#task_2
r_2=5
area_2=area_of_circle(r_2)
print("The area of the circle is : " ,area_2)

