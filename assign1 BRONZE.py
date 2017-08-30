def main():
    print('MARK V ADDINATOR ONLINE')
    print('MAKE SELECTION:')
    print ('A: ADD')
    print ('B: ADD MORE')
    print ('C: GAME')
    choice = input()
    
    if choice == 'A' or 'a':
        add2()
        
        
       


# add two numbers
def add2():
    num1 = int(input('FIRST NUMBER? '))
    num2 = int(input('SECOND NUMBER? '))
    total = num1 + num2
    print('SUM: ',total)
    cont = input('AGAIN? (Y/N)')
    
    if cont != 'Y':
        print('THANK YOU FOR USING THE MARK V ADDINATOR!')
        print('BE SURE TO PRE-ORDER THE MARK VI AT MATHSTOP TODAY!')
        exit
    else:
        main()   
     


main()
