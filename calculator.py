def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error:division by zero not possible"
    else:
        return a/b
def mod(a,b):
    if b==0:
        return "Error:modulus by zero not possible"
    else:
        return a%b 
def sqrt(a):
    return a**0.5   
def power(a,b):
    return a**b
def floor(a):
    return int(a) if a>=0 else int(a)-1
def ceil(a):
    return int(a)+1 if a>=0 else int(a)
def signum(a):
    if a>0:
        return 1
    elif a<0:
        return -1
    else:
        return 0
    
print("\n" + "="*50)
print("              MY PYTHON CALCULATOR")
print("="*50)


history = []
redo = []
while True:
    operator = input("\nEnter operator (+, -, *, /, %, sqrt, ^, floor, ceil, signum, undo, redo, history, exit): ").strip()

    if operator == "exit":
        break

    elif operator == "undo":
        if history:
            last = history.pop()
            redo.append(last)
            print(f"Undo: Removed '{last[0]}' → Result was: {last[1]}")
        else:
            print("Nothing to undo.")
        continue

    elif operator == "redo":
        if redo:
            last = redo.pop()
            history.append(last)
            print(f"Redo: Restored '{last[0]}' → Result: {last[1]}")
        else:
            print("Nothing to redo.")
        continue

    elif operator == "history":
        if not history:
            print("No history yet.")
        else:
            print("\n Calculation History:")
            for index, (expression, result) in enumerate(history, 1):
                print(f"{index}. {expression} = {result}")
        continue

    elif operator in ["sqrt", "floor", "ceil", "signum"]:
        num_1 = float(input("Enter number: "))
        match operator:
            case "sqrt":
                result = sqrt(num_1)
            case "floor":
                result = floor(num_1)
            case "ceil":
                result = ceil(num_1)
            case "signum":
                result = signum(num_1)
        expression = f"{operator}({num_1})"
    
    else:
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        match operator:
            case "+":
                result = add(num_1, num_2)
            case "-":
                result = sub(num_1, num_2)
            case "*":
                result = mul(num_1, num_2)
            case "/":
                result = div(num_1, num_2)
            case "%":
                result = mod(num_1, num_2)
            case "^":
                result = power(num_1, num_2)
            case _:
                print("Invalid operator.")
                continue
        expression = f"{num_1} {operator} {num_2}"

    print(f"Result: {result}")
    history.append((expression, result))
    redo.clear()


print("="*50)