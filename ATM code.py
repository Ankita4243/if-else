print(" * Welcome to State Bank of India * ")
print("please swipe your card")
pin_inp=9697
total_amount=20000
pin=int(input("Enter your pin number:"))
if pin==9796 :
    print("1. Balance Enquiry")
    print("2. Withdraw money")
    print("3. Deposite money") 
    print("4. change your pin")
    print("5. transfer money")
    print("6. Quit")
    trans=int(input("Enter the mode of the transaction(please select the number):"))
    if trans==1:
        print(total_amount,"this is your current balance")
    elif trans==2:
        amt=int(input("Enter amount of money you wish to withdraw:"))
        if amt>100 and amt<10000:
            print("please collect your cash and thank you for using State Bank of India")
            print(total_amount-amt,"this is your current balance ")
            slip=input("Do you want to receipt (yes or no):")
            if slip=="yes":
                print("Here is your receipt.Please collect it.Thank you for using State Bank of India ")
            else:
                print("Thank you for using State Bank of India")
        else:
            print("please enter valid amount to proceed")
    elif trans==3:
        DEP=int(input("enter the amount which you wish to deposite:"))
        if DEP>0:
            print("your money has been successfully deposite.")
        else:
            print("enter valid amount of deposite.")
    elif trans==4:
        pin_1=int(input("Enter your old pin number:"))
        if pin_1==pin_inp:
            pin_2=int(input("enter your new pin number:"))
            print("your new pin has been successfuly updated.")
        else:
            print("enter valid old pin number.")
    elif trans==5:
        AMT=int(input("enter amount of money you wish to transfer:"))
        if AMT>0:
            print("your amount is transfer succesfuly transfer.")
            print(total_amount-1,"this is your current balance")
        else:
            print("please enter valid amount:")
    elif trans==6:
            print("Quit")
    else:
        print("please choose any transaction mode:")
else:
    print("please enter the valid pin.")
         

        
    

        