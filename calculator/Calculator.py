# we are making a calculator project using python 
print("         Calculator       \n")
try: 
    
    a = int(input("enter the first number: "))

    b = int(input("enter the second number: "))

    print("List of operations:")
    print("press: \n '+' for addition \n '-' for substraction \n '*' for multiplication \n '/' for division \n 'e' for exit")

    o = input("Enter operation you want to perform: ")
    match o:
        case '+':
            print(f"{a} + {b} = {a+b}")
        case '-':
            print(f"{a} - {b} = {a-b}")
        case '*': 
            print(f"{a} * {b} = {a*b}")
        case '/':
            print(f"{a} / {b} = {a/b}")
        case 'e':
            print("pogram exited")
        case default:
            print("Some error occured")

except Exception as e:
    print("Enter a valid value of a and b")