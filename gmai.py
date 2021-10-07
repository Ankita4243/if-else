Gmail=input("you want to create Gmail:")
if Gmail=="yes":
    print("Ok ,I want to create Gmail account") 
    sign_in=input("enter your gmail id:")
    if sign_in=="ankitad@20":
        password=int(input("enter your password:"))
        if password==9697:
            print("successfully sign in")
        else:
            print("incorrect password")
    else:
        print("incorrect user name")

elif Gmail=="no":
         print("enter your information:")
         first_name=input("enter your first_name:")
         last_name=input("enter your last_name:")
         print("created successfuly")
else:
    print("you have already created account")
