##Tracy Batchelor
##M2T1- Guessing game
##18 Sep 2017
##csc-221
import random

def main():
    print('Here are your choices ')
    print('1 = Find the number ')
    print('2 = Pick the number ')
    pick = input('Pick a game: ')
    if pick == '1':
        guess_game()
    elif pick == '2':
        computer_guess_game()

# game 1
def guess_game():
    print('I have picked a number from 1 to 100, it is your job to guess it.')
    
    answer = random_guess()
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
            print('You have exeeded 10 guesses.')
    cont = input('AGAIN? (Y/N)').upper()
    
    if cont == 'N':
        print('THANK YOU FOR PLAYIING!!')
     
    else:
        main()
# picks random number
def random_guess():
    answer = random.randint(1, 100)
    return answer

# cyber compare
def comp_compare(guess, choice):
    if guess < choice:
        print('Cyber: The answer is higher!!')       
    elif guess > choice:
        print('Cyber: The answer is lower!!')
    else:
        print('Congratulations, you found the answer in', num_guess, 'guesses!!!')
        break
    
# makes a bisectional guess
def pick_number(lower,higher):
    guess = int((higher - lower) / 2) + lower
    print ('The computer picked ', guess)
    return guess

#compares the guess to the answer
def compare_answer():
#    global guess
    decide = input('Should the computer guess higher or lower? (H/L)').upper()
    if decide == 'H':
        print('I will tell the compter to pick a higher number')
        var = 'lower'
        return var
    elif decide == 'L':
        print('I will tell the computer to pick a lower number')
        var = 'higher'
        return var
    else:
        print("Invalid choice. Please pick 'H' or 'L'")
        compare_answer()

#game 2    
def computer_guess_game():
    lower = 1
    higher = 100
    answer = int(input('Pick a number from 1 to 100 '))
    counter = 0
#    if answer.isalpha():
#        print('INVALID INPUT. PICK A NUMERIC INTEGER. (1 to 100)')
#        answer = int(input('Choose again? '))
    guess = 0
    while answer != guess:    
        print ('The computer will try to guess it')
        counter += 1
        if counter == 9:
            print("The computer didn't guess the number. You cheated")
            break
        guess = pick_number(lower, higher)
        if guess == answer:
            print('The computer has guessed the number in', counter,'guesses.')
            break
        compare = compare_answer(guess)
        if compare =='lower':
            lower = guess
        elif compare =='higher':
            higher = guess
            
    cont = input('AGAIN? (Y/N)').upper()
    if cont == 'N':
        print('THANK YOU FOR PLAYIING!!')
    else:
        main()
        
# game 3
def comp_vs_cyber():
    print('The computer will play a cyber opponent.')
    print('Cyber, choose your number')
    choice = random_guess()
    print('Cyber: I have chosen my number.')
    while choice != guess:    
        print ('The computer will try to guess it')
        counter += 1
        if counter == 9:
            print("The computer didn't guess the number. You cheated")
            break
        guess = pick_number(lower, higher)
        if guess == answer:
            print('The computer has guessed the number in', counter,'guesses.')
            break
        compare = compare_answer(guess)
        if compare =='lower':
            lower = guess
        elif compare =='higher':
            higher = guess
            
    cont = input('AGAIN? (Y/N)').upper()
    if cont == 'N':
        print('THANK YOU FOR PLAYIING!!')
    else:
        main()
main()
