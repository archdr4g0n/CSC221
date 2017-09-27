##Tracy Batchelor
##CSC 221
##M2 Lab
##27 Sep 2017



def main():
    verb_list = [ 'go', 'stop', 'eat', 'drop']
    noun_list = [ 'tree', 'sword', 'apple', 'key', 'north']
    phrase = input('Type in two words, a verb and a noun: ')
    #print(phrase.split(" "))
    
    #make list
    action_list = phrase.split()
    print (action_list)
    verb = action_list[0]
    noun = action_list[1]
    
    # check
    if verb == 'quit':
        print('exiting')
        
    if verb not in verb_list:
        print('verb not in list')
    elif noun not in noun_list:
        print('I don\'t know how to',phrase)
    else:
        execute(verb,noun)
        
# evaluate verb
def execute(verb, noun):
    # print('I will', verb,'the',noun) 
    verbs = {'go':'went', 'eat':'ate', 'stop':'stopped','drop':'dropped'}
    pastTense = verbs[verb]
    print('I ', pastTense, noun)











main()


##x = ‘blue,red,green’
##x.split(“,”)
## 
##[‘blue’, ‘red’, ‘green’]
##>>>
## 
##>>> a,b,c = x.split(“,”)
## 
##>>> a
##‘blue’
## 
##>>> b 
##‘red’
## 
##>>> c
##‘green’
