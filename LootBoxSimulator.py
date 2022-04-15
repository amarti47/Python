# CSP1150 Assignment 1
# Author: Aaron Martin - 10526100
# This program is a loot box simulator. 
# It allows the user to purchase gems,
# which allow the user to purchase loot boxes which can then be opened.
# Opening a loot box gives 4 items which can be of 4 different rarities.
# Rarities include: Legendary, Epic, Rare and Common.
# The user can also view their statistics.
# Statistics will show how much money has been spent,
# how many loot boxes have been opened,
# and how many Legendary items they have received.


import random

# Created header for program
headingText = 'Welcome to Loot Box Simulator!'
print('=' * 50)
print('|' + headingText.center(48) + '|')
print('=' * 50)

# Create and initialise variables to 0 or empty
gems = 0
boxes = 0
boxes_opened = 0
total_spent = 0
items = []
userInput = ''

# Function: open_box, Parameter = num_items which is always 4 in this case.
# This function performs the action of opening the loot box and passing 4 items.
# It uses the random function to decide on what rarity that item is.
# Once 4 items are stored in a list, this function returns that list.
def open_box(num_items):
    print('Opening loot box:')
    itemsList = []
    
    # Looping through 4 times to calculate the rarity of 4 items
    for i in range(1, num_items + 1):
        randomNumber = random.randint(1,100) # stores a random integer
        if randomNumber >= 1 and randomNumber <= 5:
            print('   item ' + str(i) + ' of 4... Legendary item!')
            itemsList.append('Legendary') # stores item into itemsList
        elif randomNumber >= 6 and randomNumber <= 15:
            print('   item ' + str(i) + ' of 4... Epic item!')
            itemsList.append('Epic')
        elif randomNumber >= 16 and randomNumber <= 50:
            print('   item ' + str(i) + ' of 4... Rare item!')
            itemsList.append('Rare')
        elif randomNumber >=51 and randomNumber <= 100:
            print('   item ' + str(i) + ' of 4... Common item!')
            itemsList.append('Common')

    return itemsList


# Main section: Loot box menu is created using a while loop
while userInput != '5':
    print('You have ' + str(gems) + ' gems and ' + str(boxes) + ' loot boxes.')
    print('Choose from the following options:\n'
            '   1) Buy Gems (550 gems for just $19.95!)\n'
            '   2) Buy Loot Box (costs 100 gems)\n'
            '   3) Open Loot Box\n'
            '   4) View Statistics\n'
            '   5) Quit')

    userInput = input()

    # Gems are purchased, total amount of gems and money spent is updated
    if userInput == '1':
        gems = gems + 550
        total_spent = round((total_spent + 19.95),2)
        print('Thank you for your purchase')
        
    # Loot box is purchased if user has more than 100 gems   
    elif userInput == '2':
        if gems >= 100:
            gems = gems - 100
            boxes = boxes + 1
            print('Loot box purchased')
        else:
            print('Insufficient gems')

    # Loot box is opened and 4 items are shown to the user
    # function open_box is called
    elif userInput == '3':
        if boxes > 0:
            boxes = boxes - 1
            boxes_opened = boxes_opened + 1
            items.extend(open_box(4))
        else:
            print('Insufficient loot boxes')
            
    # Statistics are shown to the user        
    elif userInput == '4':
        print('Total spent: $' + str(total_spent))
        print('Loot boxes opened: ' + str(boxes_opened))
        # Calculation of legendary item amount and percentage
        # If then else clause was used to prevent calculation error if no loot boxes were opened
        if boxes_opened > 0:
            print('Legendary items: ' + str(items.count('Legendary')) + ' (' + str(round((items.count('Legendary'))/len(items),2)) + '%)')
        else:
            print('Legendary items: 0 (0.0%)')
            
    # Allows user to quit the program, statistics data is wiped    
    elif userInput == '5':
        print('Goodbye')
        break

    # Prevent program from breaking if the wrong input is received
    else:
        print('Invalid choice')
  




            
    


    
