
print("******************")
print("Choice 1 is Area of Circle")
print("Choice 2 is Area of rectangle")
print("Choice 3 is Area of square")
print("*******************")
choice=int(input("Enter the Choice\n:"))
if (choice==1):
    r=int(input("Enter radius\n:"))
    print("Area is equal to",3.14**r)
elif(choice==2):
    w=int(input("Enter Width\n:"))
    l=int(input("Enter Length\n:"))
    print("Area is equal to",w*l)
elif(choice==3):
    a=int(input("Enter the Value of side\n:"))
    print("Area is equal to",a*a)

else:
    print("Invalid Choice")
print("===========================")

