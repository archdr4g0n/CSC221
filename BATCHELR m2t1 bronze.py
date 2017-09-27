import random

def main():
    game()

def game():
    print('I have picked a number between 0 and 100, it is your job to guess it.')
    
    answer = random.randint(1, 100)
    guess = input('Pick a numeric integer. What is your guess? ')
    num_guess = 0
#    print(answer)      #used to check if math is correct        
    while num_guess != 9:
        num_guess += 1  
        if guess != answer:
            if guess.isdigit():
                guess = int(guess)
            elif guess.isalpha():
                print('INVALID INPUT. PICK A NUMERIC INTEGER. (0-99)')
                guess = int(input('NEXT GUESS? '))
            if guess < answer:
                print('The answer is higher!!')       
            elif guess > answer:
                print('The answer is lower!!')
            else:
                print('Congratulations, you found the answer in', num_guess, 'guesses!!!')
                break
            guess = input('What is your guess? ').upper()
        if num_guess == 10:
            print('You have exeeded to allowed number of guesses.')
    cont = input('AGAIN? (Y/N)').upper()
    
    if cont == 'N':
        print('THANK YOU FOR PLAYIING!!')
     
    else:
        main()   
        
    
main()
