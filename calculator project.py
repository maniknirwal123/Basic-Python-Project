'''
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

'''



#non parameterise ,method
def add():

    ans = a+b
    print("add=", ans)

def sub():
    ans = a-b
    print("sub=", ans)

def mul():
    ans = a*b
    print("mul=", ans)

def div():
    ans = a/b
    print("div=", ans)

def mod():
    ans = a%b
    print("mod=", ans)

def power():
    ans = a**b
    print("power=", ans)

def flow_div():
    ans = a%b
    print("flow_div=", ans)
    
while True:
    ch = int(input("\nEnter Choice:\n1.Add \t2.Sub \n3.Mul \t4.Div \n5.Mod \t6.Power \n7.Flow_Div \t8.Exit:"))
    if ch == 1:
        print("\nEnter for Additon:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        add()

    elif ch == 2:
        print("\nEnter for Subtraction:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        sub()

    elif ch == 3:
        print("\nEnter for Multification:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        mul()

    elif ch == 4:
        print("\nEnter for Division:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        div()

    elif ch == 5:
        print("\nEnter for Mod:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        mod()

    elif ch == 6:
        print("\nEnter for Power:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        power()

    elif ch == 7:
        print("\nEnter for Flower Division:")
        a = int(input("Enter first number:"))
        b = int(input("Enter first number:"))
        flow_div()

    elif ch == 8:
        print("Exiting...")
        break
    else:
        print("\nInvalid Choice!")




































    

    

