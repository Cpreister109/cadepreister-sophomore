from termcolor import colored
import random

final = ''
wrds = "braid basis stick smell slump bring crowd offer allow taste medal slant fever match chair chest union think haunt visit".split()
orig = wrds[random.randint(0,len(wrds)-1)]

for i in range(6):

    guess = input('What is the five letter word?: ').lower()
    guess_list = list(guess)
    orig_list = list(orig)
    
    if guess_list == orig_list:
        for char in guess_list:
            curr_char = colored(char, 'green')
            final += curr_char
        print(f'you guessed the word in {i+1} tries!')
        break
    
    for i in range(5):
        if guess_list[i] == orig_list[i]:
            orig_list[i] = '^'
            guess_list[i] = colored(guess_list[i], 'green')
    
    for i in range(5):
        if guess_list[i] in orig_list and guess_list[i] != orig_list[i]:
            point = orig_list.index(guess_list[i])
            orig_list[point] = '^'
            guess_list[i] = colored(guess_list[i], 'yellow')
    
    final = ''
    
    for new in guess_list:
        final += new
        print(new, end='')
    print()

print(f'Your final guess: {final}')