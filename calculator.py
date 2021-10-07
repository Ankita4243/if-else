a=int(input("Enter any value:"))
b=int(input("Enter any value:"))
operator =(input("Enter any operator:"))
#This function add two no.
if operator=='+'or operator == "add":
     print(a+b)
#This function sub two no.
elif operator =='-'or operator == "substraction":
       print(a-b)
#This function multiply two no.
elif operator =='*'or operator == "multiplication":
       print(a*b)
#This function divide two no.
elif operator =='/'or operator == "division":
       print(a/b)
#This function floor division two function no.
elif operator =='//'or operator == "floor division":
      print(a//b)
#This function exponent two function no. 
elif operator =='**'or operator == "exponent":
    print(a**b)
else:
    print("Enter valid operator")
