# Name:  Aaron Martin


# This file is provided to you as a starting point for the "jokes.py" program of Assignment 2
# of Programming Principles in Semester 1, 2020.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.

# This program allows the user to cycle through all jokes imported from the JSON file.
# The user is able to leave a feeling of laugh or groan on each joke.
# Each laugh or groan is collected as a statistic and recorded into the JSON file.
# This program achieves this function through a graphical user interface.

# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of jokes.py" section of the assignment brief.  

        # Create main window
        self.main = tkinter.Tk()
        self.main.title('Joke Catalogue')
        self.main.resizable(width=True, height=True)
        self.main.configure(bg='RoyalBlue1')

        try:
            f = open('data.txt', 'r')
        except FileNotFoundError:
            f.destroy()
            return
        self.data = json.load(f)
        f.close()
        
        #initialize variable to act as an index.
        self.current_joke = 0

        #Create buttons for main window
        self.b1 = tkinter.Button(self.main, text = 'Laugh', relief = 'raised', padx=5, pady=5, command=lambda: self.rate_joke('laughs'))
        self.b1.pack(side='bottom')
        self.b2 = tkinter.Button(self.main, text = 'Groan', relief = 'raised', padx=5, pady=5, command=lambda: self.rate_joke('groans'))
        self.b2.pack(pady=10)
        self.b2.pack(side='bottom')

        self.show_joke()
        tkinter.mainloop()
        



    def show_joke(self):
        # This method is responsible for displaying the setup and punchline of the current joke in the GUI.
        # See Point 1 of the "Methods in the GUI class of jokes.py" section of the assignment brief.

        # Assign dictionary to variable
        self.joke = self.data[self.current_joke]
        # Create message for main window
        self.lab = tkinter.Message(self.main, text = self.joke['setup'] + ' ' +self.joke['punchline'])
        self.lab.pack()
        



    def rate_joke(self, rating):   
        # This method is responsible for recording the rating of the joke when a button is clicked.
        # See Point 2 of the "Methods in the GUI class of jokes.py" section of the assignment brief.
        self.joker = self.data[self.current_joke]

        # Increasing values for laughs and groans statistic depending on user input.
        if rating == 'laughs':
            self.joker['laughs'] = self.joker['laughs'] + 1
        else:
            self.joker['groans'] = self.joker['groans'] + 1

        f = open('data.txt', 'w')
        json.dump(self.data, f, indent=4)
        f.close()

        # Reset the main window to allow for next joke to be displayed.
        # Not very efficient if there were alot of jokes, was not able to find another way to reset text in main window.
        self.lab.configure(text = '', bg = 'RoyalBlue1')

        # Checks if there are no more jokes
        # Created new window for end of program message.
        if self.current_joke == len(self.data) - 1:
            self.ratingR = tkinter.Tk()
            self.ratingR.title('Rating Recorded')
            self.ratingR.resizable(width=True, height=True)
            self.ratingR.configure(bg='RoyalBlue1')

            self.ratingButton = tkinter.Button(self.ratingR, text = 'OK', relief = 'raised', padx=5, pady=5, command=lambda: self.ratingR.destroy())
            self.ratingButton.pack(side='bottom')
            
            self.ratingMessage = tkinter.Message(self.ratingR, text = 'Thank you for rating.\nThat was the last joke.\nThe program will now end.')
            self.ratingMessage.pack()
            self.main.destroy()
        else:
            # Create another window for next joke message.
            self.current_joke = self.current_joke + 1
            self.ratingR2 = tkinter.Tk()
            self.ratingR2.title('Rating Recorded')
            self.ratingR2.resizable(width=True, height=True)
            self.ratingR2.configure(bg='RoyalBlue1')

            self.ratingButton2 = tkinter.Button(self.ratingR2, text = 'OK', relief = 'raised', padx=5, pady=5, command=lambda: self.ratingR2.destroy())
            self.ratingButton2.pack(side='bottom')
            
            self.ratingMessage2 = tkinter.Message(self.ratingR2, text = 'Thank you for rating\nThe next joke will now appear')
            self.ratingMessage2.pack()

            
            self.show_joke()




# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
