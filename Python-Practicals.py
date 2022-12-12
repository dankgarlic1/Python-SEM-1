#Q1 WAP to perform following operations on rational and complex numbers 1)Addition 2)Subtraction 3)Division 4)Multiplication
"""
print("1-->Rational Numbers")
print("2-->complex  Numbers")
q=int(input("Please choose rational numbers or complex numbers "))
if q==1 :
 p1 = int(input("Enter your numerator of first rational number"))
 q1 = int(input("Enter your denominator of first rational number"))
 p2 = int(input("Enter your numerator of  second rational number"))
 q2 = int(input("Enter your denominator of  second rational number"))
 print("1-->Addition")
 print("2-->Subtraction")
 print("3-->Multiplication")
 print("4-->division")
 n = int(input())
 if n==1 :
     r1 = (p1*q2) + (p2*q1)
     r2 = (q1*q2)
     print(r1,"/",r2)
 if n==2 :
     r1 = (p1*q2) -(p2*q1)
     r2 = (q1*q2)
     print(r1,"/",r2)
 if n==3 :
     r1 = (p1*p2)
     r2 = (q1*q2)
     print(r1,"/",r2)
 if n==4 :
     r1 = (p1*q2)
     r2 = (p2*q1)
     print(r1,"/",r2)
if q==2 :
#for complex number now
 rl1 = int(input("Enter the real part of your first complex number"))
 im1 = int(input("Enter the imaginary part of your first complex number"))
 cp1 = complex(rl1,im1)
 rl2 = int(input("Enter the real part of your second complex number"))
 im2 = int(input("Enter the imaginary party of your second complex number"))
 cp2 = complex(rl2,im2)
 print("The complex numbers you have chosen are ",cp1," and ",cp2)
 print("1-->Addition")
 print("2-->Subtraction")
 print("3-->Multiplication")
 print("4-->division")
 m = int(input())
 if m==1 :
     cp = complex(rl1+rl2,im1+im2)
     print(cp)
 if m==2 :
     cp = complex(rl1-rl2,im1-im2)
     print(cp)
 if m==3 :
     cp = complex((rl1*rl2)+(im1*im2*(-1)),(rl1*im2)+(im1*rl2))
     print(cp)
 if m==4 :
     cp = complex(((rl1*rl2)+(im1*im2))/(rl1**2+im2**2),((im1*rl2)-(rl1*im2))/(rl2**2+im2**2))
     print(cp)

#Q2 WAP to calculate roots of quadratic equation
print("The quadratic Equation is : ax^2+bx+c=0")
a=int(input("Enter coefficient 'a' "))
b=int(input("Enter coefficient 'b' "))
c=int(input("Enter coefficient 'c' "))
d = (b**2) - (4*a*c)
print("You Discriminant is : " , d)
if d<0 :
    print("Roots of this Quadratic equation are imaginary")
if d==0 :
    print("Roots of this quadratic equation are real and equal")
    root1 = (-b + d**0.5)/2*a
    root2 = (-b - d**0.5)/2*a
    print("Roots of this quadratic equation are : ",root1," and ",root2)
if d>0 :
    print("Roots of this quadratic equation is real and unequal ")
    root1 = (-b + d**0.5)/2*a
    print("Roots of this quadratic equation are : ",root1)

#Q4 WAP to accept a character from user and display whether it is a vowel o consonant
a=str(input("Enter the alphabet you want to check "))
if a== 'a' or a== 'e' or a == 'i' or a== 'o' or a== 'u' or a== 'A' or a== 'E' or a == 'I' or a== 'O' or a== 'U' :
    print(a," is a vowel")
else:
    print(a," is a consonant")
#Q5 WAP to check whether a year is leap year
y = int(input("Enter the year in YYYY format only "))
if y%4==0 :
    if y%100==0 :
        if y%400 :
            print(y," is a Leap Year")
        else:
            print(y," is NOT a Leap Year")
    else:
        print(y," is NOT a Leap Year")
else:
    print(y," is NOT a Leap Year")

#Q6 Write a menu driven program perform following operations
# 1)AREA and CIRCUMFERENCE OF A CIRCLE 2)Perimeter of rectangle 3)Volume and Total surface area of a cuboid
print("1--> AREA and CIRCUMFERENCE OF A CIRCLE")
print("2--> Perimeter of rectangle")
print("3--> Volume and Total surface area of a cuboid ")
n=int(input("Please select the any option from above"))
if n==1 :
    r = float(input("Please enter the radius "))
    print(r," cm")
    Area = 3.1415926*r*r
    Circumference = 2*3.1415926*r
    print("area of the circle : ",Area," Centimeter Squared ")
    print("circumference of the circle : ",Circumference," Cm")
if n==2 :
    l = int(input("Please enter the length of Rectangle"))
    b = int(input("Please enter the breadth of Rectangle"))
    Perimeter = 2*(l+b)
    print("perimeter of the rectangle is : ",Perimeter," Cm")
if n==3 :
    l = int(input("Please enter the length of Cuboid"))
    b = int(input("Please enter the breadth of Cuboid"))
    h = int(input("Please enter the height of Cuboid"))
    total_surface_area= 2*((l*b)+(l*h)+(b*h))
    Volume = l*b*h
    print("Total Surface Area of the cuboid is : ",total_surface_area," Centimeter Squared")
    print("Volume of he cuboid is : ",Volume," Cm")
    """
print("If i share my assignment with you please dont copy it exactly have some dignity and self respect")
print("It is for help and reference,so that you have a rough idea ")
print("Yours Faithfully CR :D")
print()
print()
print()
print()
print("Harshit Raizda AE-1220")




