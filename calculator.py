choice = int(input("enter you choice: "))
num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))
if choice == 1:
    print("add: ",num1 + num2)
elif choice == 2:
    print("sub: ",num1 - num2)
elif choice == 3:
    print("multiply: ",num1*num2)
elif choice == 4:
    print("divide : ",num1/num2)
elif choice == 5:
    print("modules: ",num1%num2)
else:
    print("try again later")