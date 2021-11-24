x=int(input("Enter the First number\n:"))
y=int(input("Enter the Second Number\n:"))
z=int(input("Enter the Third number\n:"))
if(x>y):
    if(x>z):
        print(x,"is greater")
    else:
        print(z,"is greater")
else:
    if(y>z):
        print(y,"is greater")
    else:
        print(z,"is greater")
        
