# Name:  Aaron Martin
# Student Number:  10526100

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2020.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.

# This program allows the user to manage a joke catalogue.
# You can add, list, view, delete and search jokes in the catalogue.
# Adding a joke allows you save a joke with a setup and punch line.
# The jokes and any changes made to them are all saved to a data.txt file.

# Import the json module to allow us to read and write data in JSON format.
import json




# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        value = input(prompt)

        try:
            numResponse = int(value)

        except ValueError:
            print(errorMessage)
            continue

        if numResponse >= 0:
            return numResponse
        else:
            print('Please enter a number greater than or equal to 0.')
            continue



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        value = input(prompt)
        strippedValue = value.strip()
        
        if strippedValue != "":
            return strippedValue
        else:
            print('Invalid input, please try again')
            continue


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    f = open('data.txt', 'w')
    json.dump(data_list, f, indent=4)
    f.close()




# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

try:
    f = open('data.txt', 'r')
    data = json.load(f)
    f.close()
except FileNotFoundError:
    data = []




# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Joke Catalogue Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ')

       
    if choice == 'a':
        # Add a new joke.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.

        # Create dictionary to store joke
        dict = {}
        dict["setup"] = input_something("Enter setup of joke: ")
        dict["punchline"] = input_something("Enter punchline of joke: ")
        dict["laughs"] = 0
        dict["groans"] = 0
        data.append(dict)
        save_data(data)
        print("Joke added.")
        

    
    elif choice == 'l':
        # List the current jokes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.

        # Check if data list is empty
        if not data:
            print("No jokes saved")
        else:
            print("List of jokes: ")
            # Loop through each dictionary in data and print the setup for each joke.
            for index, joke in enumerate(data):
                print(index, ") ", joke['setup'])
            

    elif choice == 's':
        # Search the current jokes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No jokes saved")
        else:
            searchTerm = input_something("Enter search term: ")
            searchTerm = searchTerm.lower()
            noMatches = True
            print("Search results: ")
            for index, joke in enumerate(data):
                # Checking if search term is in the setup or punchline in each joke.
                if searchTerm in joke['setup'.lower()] or searchTerm in joke['punchline'.lower()]:
                    print(index, ") ", joke['setup'])
                    noMatches = False

            if noMatches is True:
                print("No matches have been found")


    elif choice == 'v':
        # View a joke.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No jokes saved")
        else:
            searchNumber = input_int("Joke number to view: ")
            noMatches = True
            for index, joke in enumerate(data):
                # Checks user input and matches it with corresponding joke, joke is then printed.
                if searchNumber == index:
                    print(' ', joke['setup'])
                    print(' ', joke['punchline'])
                    if joke['laughs'] == 0 and joke['groans'] == 0:
                        print("  This joke has not been rated")
                    else:
                        print('  Laughs: ', joke['laughs'], '  Groans: ', joke['groans'])
                    noMatches = False
            if noMatches is True:
                print("Invalid index Number")


    elif choice == 'd':
        # Delete a joke.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if not data:
            print("No jokes saved")
        else:
            searchNumber = input_int("Joke number to delete: ")
            noMatches = True
            for index, joke in enumerate(data):
                # Deletes a selected joke based on user input
                if searchNumber == index:
                    del data[searchNumber]
                    print("Joke deleted.")
                    save_data(data)
                    noMatches = False
            if noMatches is True:
                print("Invalid index Number")



    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice")
        
