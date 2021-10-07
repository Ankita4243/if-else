held=int(input("number is classed held:"))
attend=int(input("number is class attendance:"))
present=(attend/held*100)
if present>75:
    print("allowed to sit in exam")
else:
    print("not allowed to sit in exam")