user = input(f"Enter 'F' for Fahrenheit to Celsius,\n 'C' for Celsius to Fahrenheit,\n or 'quit' to exit: ")

if user == 'quit':
    print()
    print('Exiting the temperature converter')

while user != 'quit':    
    
    if user.upper() == 'F':
    
        far = float(input('Enter temperature in Fahrenheit: '))
        cel = (far - 32) * (5/9)
        print(f'{far}°F is {cel:.2f}°C')
    
    elif user.upper() == 'C':
    
        cel = float(input('Enter temperature in Celcius: '))
        far = (cel * (9/5)) + 32
        print(f'{cel}°C is {far:.2f}°F')
    
    elif user == 'quit':
    
        print()
        print('Exiting the temperature converter')
        break
    
    else:
    
        print("Invalid choice. Please enter 'F', 'C', or 'quit'.")
    
    print()
    user = input(f"Enter 'F' for Fahrenheit to Celsius,\n 'C' for Celsius to Fahrenheit,\n or 'quit' to exit: ")