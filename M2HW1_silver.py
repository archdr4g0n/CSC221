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

# customer service function
def custom_serv():
    customer = [1,'Alice',2,'Bob',7,'Charles',9,'Dennis',10,'Elise',12,'Fred',20,'George',31,'Queue finshed']
    clerk= [5,10,20,25,30]
    time = 31
    queue =[]
    for minute in range(time):
        print (minute)
        arrive = customer.pop(0)
        if arrive == minute:
            client = customer.pop(0)
            print(client,'entered line.')
            queue.append(client)
        elif arrive != minute:
            customer.insert(0,arrive)
        else:
            print('Queue finished')
            main()
        calling = clerk.pop(0)
#        print(queue)
#        print('calling', calling)
        if calling == minute:
            inline = queue.pop(0)
            print('The clerk called,',inline)
        else:
            clerk.insert(0,calling)


main()
