##Tracy Batchelor
##CSC 221
##M1T1 Gold
##11 Sep 2017

import random

def main():
    print('MARK V ADDINATOR ONLINE')
    print('MAKE SELECTION:')
    print ('A: ADD')
    print ('B: ADD MORE')
    print ('C: GAME')
    choice = input().upper()
    
    if choice == 'A':
        add2()
    elif choice == 'B':
        addSeveral()
    elif choice == 'C':
        game()
    
       
# add two numbers
def add2():
    num1 = int(input('FIRST NUMBER? '))
    num2 = int(input('SECOND NUMBER? '))
    
    total = num1 + num2
    print('SUM: ',total)

    cont = input('AGAIN? (Y/N)').upper()
    
    if cont == 'N':
        print('THANK YOU FOR USING THE MARK V ADDINATOR!')
        print('BE SURE TO PRE-ORDER THE MARK VI AT MATHSTOP TODAY!')
        
    else:
        main()   
        
# add several numbers
def addSeveral():
    total = 0
    num = input('NEXT NUMBER? ').upper()
    
    while num != 'END':
        if num == 'TEN' or num =='ten':
            num = 10
        elif num.isalpha():
            print('INVALID INPUT')
            num = input('NEXT NUMBER? ').upper()
        num = int(num)
        total += num
        num = input('NEXT NUMBER? ').upper()
        
    print('SUM: ',total)

    cont = input('AGAIN? (Y/N)').upper()
    
    if cont == 'N':
        print('THANK YOU FOR USING THE MARK V ADDINATOR!')
        print('BE SURE TO PRE-ORDER THE MARK VI AT MATHSTOP TODAY!')
    else:
        main()

def game():
    print('I have picked a number between 0 and 99, it is your job to guess it.')
    print('Enter END if you are a quiter!!!!')
    answer = random.randint(0, 99)
    guess = input('Pick a numeric integer. What is your guess? ')
    num_guess = 0
#    print(answer)      #used to check if math is correct        
    while guess != 'END':
        num_guess += 1  
        if guess != answer:
            if guess == 'TEN' or guess == 'ten':
                guess = 10
            elif guess.isdigit():
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
        
    cont = input('AGAIN? (Y/N)').upper()
    
    if cont == 'N':
        print('THANK YOU FOR USING THE MARK V ADDINATOR!')
        print('BE SURE TO PRE-ORDER THE MARK VI AT MATHSTOP TODAY!')
    else:
        main()   
        
    
main()
