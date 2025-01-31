#calculator Application Project
def add(a,b):
    ans = a+b
    print("add=", ans)

def sub(a,b):
    ans = a-b
    print("sub=", ans)
    
def mul(a,b):
    ans = a*b
    print("mul=", ans)

def div(a,b):
    ans = a/b
    print("div=", ans)

while True:
    ch = int(input("\n\nEnter Choice:\n1.Add \t2.Sub \n3.Mul \t4.div \n5.Exit:-"))
    if ch == 1:
        print("\nEnter for Addition")
        fn = int(input("Enter first Number:"))
        sn = int(input("Enter Second Number:"))
        add(fn,sn)
    elif ch == 2:
        print("\nEnter for Subtraction")
        fn = int(input("Enter first Number:"))
        sn = int(input("Enter Second Number:"))
        sub(fn,sn)
    elif ch == 3:
        print("\nEnter for Subtraction")
        fn = int(input("Enter first Number:"))
        sn = int(input("Enter Second Number:"))
        mul(fn,sn)
    elif ch == 4:
        print("\nEnter for Subtraction")
        fn = int(input("Enter first Number:"))
        sn = int(input("Enter Second Number:"))
        div(fn,sn)
    elif ch == 5:
        print("\nExiting....")
        break
    else:
        print("\nInvalid Choice!")






































    

    

