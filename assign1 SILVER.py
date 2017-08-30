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
    
        main()
       
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
    num = input('NEXT NUMBER? ')
    
    while num != 'END':
        if num == 'TEN':
            num = 10
        num = int(num)
        total += num
        num = (input('NEXT NUMBER? '))
        
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
    guess = input('What is your guess? ')
    num_guess = 0
    print(answer)      
    guess = int(guess)        
    while guess != answer:
        num_guess += 1  
        if guess != 'END':
            if guess == 'TEN':
                guess = 10  
            if guess < answer:
                print('The answer is higher!!')       
            elif guess > answer:
                print('The answer is lower!!')  
        guess = input('What is your guess? ')
        guess = int(guess)
    print('Congratulations, you found the answer in ', num_guess, 'guesses!!!')
    cont = input('AGAIN? (Y/N)').upper()
    
    if cont == 'N':
        print('THANK YOU FOR USING THE MARK V ADDINATOR!')
        print('BE SURE TO PRE-ORDER THE MARK VI AT MATHSTOP TODAY!')
        
    else:
        main()   
        
    
main()
