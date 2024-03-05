user = input(f"Enter a number to check if it's prime\n(or 'quit' to exit): ").strip()
test = 1

if user == 'quit':
    
    print()
    print('Exiting the prime number program.')

while user != 'quit':
    
    if int(user) == 0:
        
        print(f'{user} is not a prime number.')
        print()
        user = input(f"Enter a number to check if it's prime\n(or 'quit' to exit): ").strip()
        
    if int(user) < 0:
            
        print(f'{user} is not a prime number.')
        print()
        user = input(f"Enter a number to check if it's prime\n(or 'quit' to exit): ").strip()
    
    if int(user) == 1:
        
        print(f'{user} is not a prime number.')
        print()
        user = input(f"Enter a number to check if it's prime\n(or 'quit' to exit): ").strip()
    
    if test != 1:
        
        print()
        user = input(f"Enter a number to check if it's prime\n(or 'quit' to exit): ").strip()
        test = 1
    
    
    while user != 'quit' and int(user) != 1 and int(user) > 0 and int(user) != 0:
        
        if test == 1:
        
            test += 1
            continue
    
        elif test == int(user):
        
            print(f'{user} is a prime number.')
            break
    
        elif test < int(user) and int(user) % test == 0:
        
            print(f'{user} is not a prime number.')
            break
    
        test += 1
    
    if user == 'quit':
        
        print()
        print('Exiting the prime number program.')

        
            
    