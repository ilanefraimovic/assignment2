from app.operations import addition, subtraction, multiplication, division

def calculator():
    print("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")

        if user_input.lower() == "exit":
            print("Exiting..")
            break
        
        try:
            op, num1, num2, = user_input.split()

            num1, num2 = float(num1), float(num2)

        except ValueError:
            print("invalvid input. Format:  <operation> <num1> <num2> ")
            continue
        
        if op == "add":
            result = addition(num1, num2)
        elif op == "subtract":
            result = subtraction(num1, num2)  
        elif op == "multiply":
            result = multiplication(num1, num2)  
        elif op == "divide":
            try:
                result = division(num1, num2) 
            except ZeroDivisionError as e:
                print(e) 
                continue  
        else:
            print(f"Unknown operation '{op}'. Supported operations: add, subtract, multiply, divide.")
            continue 
        print(f"Result: {result}")