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
        
    

































































