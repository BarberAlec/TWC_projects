import time

# Task for Alphas:
# > Make a function to ask the user for thier year of birth and month of birth
# > Make another function to calculate what age they are... should you give name or
#    calender number of month ('April' or 04 ?)

def intro():
    '''
    parametre: None
    returns: user_name: string, name of user
    '''
    user_name = raw_input('Hello what is you name: ')
    print "Hello " + user_name + ", the date is " + str(time.ctime())

    return user_name

def animal_preference(animal_1, animal_2):
    '''
    parametre: animal_1: string, name of first animal
    parametre: animal_2: string, name of first animal
    returns: user_name: name of user
    '''
    pref_animal = raw_input('Do you prefer ' + animal_1 + ' or ' + animal_2 + ' more? ')
    # Extra task, make function to make sure user gives correct response!

    return pref_animal

def end_conv(user_name, fav_animal):
    '''
    parametre: user_name: string, name of user
    returns: None
    '''
    print "Goodbye " + user_name + " of the " + fav_animal + ", it has been a pleasure!"

    # nothing to return 

def main():
    person_name = ''
    favourite_animal = ''
    
    choice_1 = 'turkeys'
    choice_2 = 'parrots'

    # Start Conversation
    person_name = intro()

    # Ask user about animals that they like
    favourite_animal = animal_preference(choice_1,choice_2)

    # End the conversation
    end_conv(person_name, favourite_animal)

main()