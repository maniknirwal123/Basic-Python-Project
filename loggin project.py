# Loggin Project using File handling

import datetime

def add(a, b):
    ans = a + b
    print("add", a+b)

def sub(a, b):
    ans = a - b
    print("sub", a-b)
    
def mul(a, b):
    ans = a * b
    print("mul", a*b)
    
def div(a, b):
    ans = a / b
    print("div", a/b)

fh = open("clac_program.txt", "a")
fh.write(f"\n{datetime.datetime.now()}: user started the calc program")

while True:
    ch = int(input("\n\nENTER CHOICE: \n1.Add\t2.Sub\n2.Mul\t3.div\n5.Exit :"))
    if ch == 1:
        print("---->1.ADD")
        fn = int(input("Enter First Number:"))
        sn = int(input("Enter Second Number:"))
        add(fn, sn)
        fh.write(f"\n{datetime.datetime.now()}: user added {fn} and {sn}")
        
    elif ch == 2:
        print("---->2.SUB")
        fn = int(input("Enter First Number:"))
        sn = int(input("Enter Second Number:"))
        sub(fn, sn)
        fh.write(f"\n{datetime.datetime.now()}: user subtracted {fn} and {sn}")

    elif ch == 3:
        print("---->3.MUL")
        fn = int(input("Enter First Number:"))
        sn = int(input("Enter Second Number:"))
        mul(fn, sn)
        fh.write(f"\n{datetime.datetime.now()}: user multipied {fn} and {sn}")

    elif ch == 4:
        print("---->2.DIV")
        fn = int(input("Enter First Number:"))
        sn = int(input("Enter Second Number:"))
        div(fn, sn)
        fh.write(f"\n{datetime.datetime.now()}: user divided {fn} and {sn}")

    elif ch == 5:
        print("---->5.EXIT")
        fh.write(f"\n{datetime.datetime.now()}: user ended the calc program")
        break

    else:
        print("---->Invalid Choice!")
        fh.write(f"\n{datetime.datetime.now()}: user entered invalid choice {ch}")

fh.close()
       
        






        
