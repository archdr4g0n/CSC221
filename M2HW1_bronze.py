##Tracy Batchelor
##M2HW1
##csc-221
##25 Sep 2017

def main():
    print('A: Vowel finder')
    print('B: Driving directions')
    print('C: Customer service')
    print('D: Towers of Hanoi')
    option = input('Choose an option: ').upper()
    if option == 'A':
        vowel_finder()
    elif option == 'B':
        drive_direct()
    elif option =='C':
        custom_serv()

#vowel finder function
def vowel_finder():
    phrase = input('Please enter a phrase: ')
    for char in phrase:
        if char == 'a' or char == 'A':
            print(char)
        elif char == 'e' or char == 'E':
            print (char)
        elif char == 'i' or char == 'I':
            print (char)
        elif char == 'o' or char == 'O':
            print (char)
        elif char == 'u' or char == 'U':
            print(char)
    main()
    
# driving directions function
def drive_direct():
    direction =['home']
    print('Enter end when finished. press enter when done with each direction')
    direct = input('Enter directions from a location to FTCC: ')
    while direct != 'end':# or direct != 'END':
        direction.append(direct)
        direct = input('Next direction to FTCC: ')
    print (direction)
    print('To return to your start point follow these directions.')
    step =''
    while step != 'home':
        step = direction.pop()
        print (step)
    main()


main()
