c=0
def add():
    a=float(input("Enter 1st Number : "))
    b=float(input("Enter 2nd number : "))
    print(a+b)
def subt():
    a=float(input("Enter 1st Number : "))
    b=float(input("Enter 2nd number : "))
    print(a-b)
def div():
    a=float(input("Enter dividend : "))
    b=float(input("Enter divisor : "))
    if b==0:
        print("Cannot divide by zero")
        return 0
    else:
        print(a/b)
def mult():
    a=float(input("Enter 1st Number : "))
    b=float(input("Enter 2nd number : "))
    print(a*b)
def evod():
    a=int(input("Enter your number : "))
    if (a%2==0):
        print("Even")
    else:
        print("Odd")
def perc():
    a=float(input("Enter 1st Number : "))
    b=float(input("Enter 2nd number : "))
    print(a/b*100,"%")
while c!=7:
    print("-----Calculator-----\nPlease select an option")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Check Even/Odd\n6. Calculate Percentage\n7. Exit")
    c=int(input())
    if c==1:
        add()
    elif c==2:
        subt()
    elif c==3:
        mult()
    elif c==4:
        div()
    elif c==5:
        evod()
    elif c==6:
        perc()
    elif c==7:
        continue
    else:
        print("Enter a valid choice!/n")
print("Exit successful")