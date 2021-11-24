x=int(input("Enter the Value One\n:"))
y=int(input("Enter the Value Two\n:"))
print("******************")
print("Choice + is Addition")
print("Choice - is Subtraction")
print("Choice * is Multiplication")
print("Choice / is Division")
print("*******************")
choice=input("Enter the Choice\n:")
if (choice=='+'):
    print("Sum is equal to",x+y)
elif(choice=='-'):
    print("Sub is equal to",x-y)
elif(choice=='*'):
    print("Mul is equal to",x*y)
elif(choice=='/'):
    print("Div is equal to",x/y)
else:
    print("Invalid Choice")
print("Simple Calculator  Simple Calculator Simple Calculator Simple Calculator")

