'''
# golabl and local function
x = 10   #Global fun
def fun1():
    y = 20 #localfun
    print("locally, inside fun1, x=", x)
    print("locally, inside fun1, y=", y)
    #print("locally, inside fun1, z=", z)

def fun2():
    z=30   #localfun
    print("locally, inside fun2, x=", x)
    #print("locally, inside fun2, y=", y)
    print("locally, inside fun2, z=", z)


fun1()
fun2()

print("globally, outside the fun, x=", x)
#print("globally, outside the fun, y=", y)
#print("globally, outside the fun, z=", Z)


## chaeck Bank balance
balance = 0

def check_balance():
    print("Total balance in your acc is:", balance)

def deposit_cash(amt):
    global balance
    balance = balance + amt
    print(amt," rs. deposited")

def withdraw_cash(amt):
    global balance
    if balance>= amt:
        balance = balance - amt
        print(amt,"rs.withdraw")
    else:
        print("invalid Balance!")

while True:
    ch = int(input("\n\nENTER CHOICE: \n1.Deposit cash \n2.Withdraw cash \n3.Chech Balance \n4.Exit :-"))
    if ch == 1:
        print("------>1.Deposit Cash")
        d_amt = int(input("Enter amount to deposit:-"))
        deposit_cash(d_amt)
    elif ch == 2:
        print("------>2.Withdraw cash")
        w_amt = int(input("Enter amount to withdraw :-"))
        withdraw_cash(w_amt)
    elif ch == 3:
        print("------>3.Check Balanace :-")
        check_balance()
    elif ch == 4:
        print("------>4.Exit..")
        break
    else:
        print("------>5.Invalid Choice")

'''


## Bank Project

balance = 0

def check_balance():
    print("Toatal Balnace in Your Account:", balance)

def deposite_cash(amt):
    global balance
    balance = balance + amt
    print(amt,"rs.Withdraw")

def withdraw_cash(amt):
    global balance
    if balance>= amt:
        balance = balance - amt
        print(amt,"rs.withdraw")
    else:
        print("Invalid Balance!")

while True:
    ch = int(input("\n\nENTER YOUR CHOICE:-  \n1.Deposite Balance \n2.Withdraw Balance \n3.Check Balance \n4.Exit:- "))
    if ch == 1:
        print("----->1.Deposite Cash")
        d_cash = int(input("Enter Amount to Deposite:-"))
        deposite_cash(d_cash)
    elif ch == 2:
        print("----->2.Withdraw Cash")
        w_cash = int(input("Enter Amount to Withdraw:-"))
        withdraw_cash(w_cash)
    elif ch == 3:
        print("----->3.Check Balance")
        check_balance()
    elif ch == 4:
        print("----->4.Exit...!")
        break
    else:
        print("Invalid Choice..!")
        
    

































































