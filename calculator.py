def calculator(choice, num1, num2):
    
    """Simple calculator that performs basic arithmetic operations."""


    if choice == '1':

        return num1 + num2
    
    elif choice == '2':

        return num1 - num2
    
    elif choice == '3':

        return num1 * num2
    
    elif choice == '4':

        if num2 != 0:

            return num1 / num2
        
        else:

            return "Error! Division by zero."
        
    else:

        return "Invalid input"

