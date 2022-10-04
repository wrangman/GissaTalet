'''
GISSATALET.PY: A number guessing game

__author__  = "Johan Wrangö"
__credits__ = ["Anne Onym", "Pseudo Nyman", "John Noname"]
__version__ = "1.0.3"
__email__   = "johan.wrango@ntig.se"
'''

import random                                   #så jag kan använda slumpfunktioner                                 
import os                                       #för os.system() så jag kan sudda skärmen


def colored(r, g, b, text):                     #funktion för att returnera färgsatt text
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


os.system('color')

while True:                                     #Huvudloop så man kan köra flera spelomgångar. Om denna slutas avslutas spelet.
    os.system('cls||clear')                     

    print(colored(0, 255, 200, """
    ==============================
    G I S S A  T A L E T   1 - 100 
    ====== Du har 7 försök! ======\n\n"""))

    secret_number = random.randint(1, 100)  
    total_guesses = 0

    while total_guesses <= 7:                   #Spelloop: Aktuellt spel
        while True:                             #Input-koll-loop - kollar så man matar in rätt innan programmet fortsätter
            try:
                guess = int(input('Gissa mitt hemliga tal: '))
                break
            except ValueError:
                print(colored(255, 0, 0, 'Du måste skriva ett heltal - pröva igen\n'))
        
        total_guesses += 1
        
        if guess > secret_number:
            print(colored(255, 0, 50, 'För HÖGT'))
        elif guess < secret_number:
            print(colored(255, 0, 0, 'För LÅGT'))
        elif guess == secret_number:
            print(colored(0, 255, 0, f'\nGrattis! Du hittade hemliga talet {secret_number} på ' +
                    str(total_guesses)+' försök!\n\n'))   
            break
    
        if total_guesses == 7: 
            print(colored(255, 0, 100, f'\nTyvärr, du hittade inte mitt hemliga tal: {secret_number}.'))
            break
    
    #Spelet frågar alltid om man vill spela igen efter man vunnit eller förlorat
    try_again = input('Spela igen? (Enter = Ja / N = Nej) ').upper()
    if try_again == 'N' or try_again == 'NEJ':
        print('Tack för du spelade - ses nästa gång!')
        exit()                             #Här kan man använda break istället - men gör såhär för att visa hur man kan avsluta programmet direkt med ett kommando
