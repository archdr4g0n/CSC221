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
        print('THIS FEATURE IS AVAILABLE TO PREORDER CUSTOMERS ONLY.')
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


main()
