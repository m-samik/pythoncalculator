print("\t=========Welcome to your Calculator========")
while(1):
    option = input("Enter the operation you wish to perform: ")
    def cal(arg):
        if arg == "end":
            exit()
        elif arg in ['+', '-', '*', '/', '√']:
            print("Enter two numbers")
            num1 = int(input("First Number: "))
            num2 = int(input("Second Number: "))
            if arg == "+":
                print("Addition= ",num1+num2)
            elif arg == "-":
                print("Subraction= ",num1-num2)
            elif arg == "*":
                print("Multiplication= ",num1*num2)
            elif arg == "/":
                print("Division= ",num1/num2)
        else:
            print("OOPS, you entered invalid operation")
    cal(option)
