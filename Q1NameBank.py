# Jahkim Brown-Roopnarine
# ICS 3UO - A
# December 5, 2021
# This program will initially take an input of five strings from a user, as names, and will store them into a list. After
# taking a list of names from the user, it will display a menu that will give the user a set of options. These options will
# include: displaying all names, editing a name, sorting names and adding/deleting a name. After that this list will be stored
# into a list and saved for later use.

currentNB = [] # Global variable initiated to be used throughout the code for the current Name bank that is being edited.
currentNBName = "" # Global variable for the current Name Bank name that is being edited, is used as a key to the dictionary.
nameLibrary = {} # Global variable for the libary, which serves as an overarching dictionary where all name banks are saved to.

# This code functions as a fully operational name bank creator and library generator. The general flow of the code is as
# follows: users are introduced to the program through the basic introductor functions titled 'getName'. This enlists a
# greeting sequence and takes the input of a users name. Then the user is welecomed to the main menu. The entirety of the
# program is ran through the mainMenu() as it acts as central hub for local function calling. Additionally, the getInput
# function is crucial for online documentation, as well as potential user actions for returning to the main menu, or quitting
# the program at any time.
def getInput(prompt, helpString):
    global currentNB
    global currentNBName

    resp = input(prompt)
    if resp == "quit":
        print("\n" + "Thank you for using this Name Bank!")
        quit(0)
    elif resp == "help":
        print(helpString)
        return getInput(prompt, helpString)
    elif resp == "main menu":
        verify = getInput("Are you sure you would like to return to the main menu? If you are currently editing a new Name Bank all current edits will be deleted, and can not be accessed later. (yes/no) ", "It seems like you're having some trouble. Type 'yes' to return to the main menu if you are okay with deleting all name bank data, type 'no' if you would wish to continue where you were in the program.")

        if verify.upper() == "NO":
            print("Okay, you will be able to continue where you left off. ")
            return getInput(prompt, helpString)
        else:
            currentNBName = ""
            currentNB = []

            print("Returning to the main menu...\n")
            mainMenu()
        pass
    else:
        return resp
########################################################################################################################
def getName():
    name  = input("Hi there, what is your name: ")
    print("Hello " + name + "!\n"
          "Welcome to the Name Bank!\n"
          "If at any point you would like the program to terminate, type 'quit'.\n"
          "If at any point you require help, please type 'help'.\n"
          "If at any point you would like to return to the main menu, please type 'main menu'.\n")
    return name


# From the main menu, users are presented with four options to view instructions, create a namebank,
# access their library, or to quit the program. The main menu only ever allows the user to input an integer between 1 and 4
# otherwise it will prompt an error code.
def mainMenu():
    print("Welcome to the Main Menu\n"
          "[1] Name Bank Instructions\n"
          "[2] Create a 5 Name List\n"
          "[3] My Library\n"
          "[4] Exit")
    print("")
    stopper = False
    while not stopper:
        try:
            selection = int(getInput("Enter your selection: ", "It seems like you're having some trouble. Please type a number from one of the options to enter a selection.\n"
                                                                "For instructions for Name Bank usage type '1', to create a 5 name list type '2', to acess your library type '3'\n"
                                                                "to exit the program type '4'.\n"))
            if selection not in range(1,5): # error handling to make sure number is within choices presented.
                raise ValueError
            break
            stopper = True
        except (ValueError, TypeError):
            print("Error detected. Please re-input your selection")
            stopper = False

    if selection == 1:
        getInstructions()
    elif selection == 2:
        enter5Nb()
    elif selection == 3:
        enterLib()
    elif selection == 4:
        print("Exit has been selected\n"
              "Thank you using this Name Bank " + name + "!")
        quit(0)
########################################################################################################################
# The getInstructions function may be called from the menu, if the user chooses the corresponding number - it displays a
# a string of instructions on how to use the progam and then returns the user to the main menu.
def getInstructions():
    print("\n"
          "Name Bank Instructions has been selected.\n"
          "This program will take a list of names inputted by you! Thereafter you will be able to display\n"
          "all names, edit a name, sort names alphabetically, and add or delete name(s)! After you complete a Name Bank, you will\n"
          "be prompted to title your list and save it to your library - more on that in a second.\n"
          "In your library, you will have access to all of your saved Name Banks. Each Name Bank will be titled as you left it,\n"
          "In this feature, you can revisit saved Name Banks, edit names, sort names alphabetically, and add or delete a name!")

    typeAnything = getInput("\nHope that all makes sense! Type enter to dismiss this message and return to the main menu!", "It seems like you're having some trouble, type enter to dismiss this message.")

    while typeAnything == typeAnything:
        mainMenu()
########################################################################################################################
# The create a namebank function acts as an initializer for creating a namebank. It checks to see if the user is familiar with the program.
# If they are not, they will be sent back to the instructions, and then to the main menu. It then tells the user what they will be doing
# and if the user is satifised, this function will pass a value of 5 to a namecounter variable to be used later in the program for
# creating a name bank.
def enter5Nb():
    print("You have selected the 5-Name Bank mode!\n")

    checkIn = getInput("Firstly, are you familiar with how to use this Name Bank creator? (yes/no) ", "It seems like you're having some trouble. Please type 'yes' if you are familar with the program or 'no' if you are not.")
    if checkIn.upper() == "NO": # captilization for case sensitivity
        print("No worries, I'll send you to take a look at the instructions. Come back through the main menu when you're done giving that a read!")
        getInstructions()

    checkIn2 = getInput("Perfect. Shortly, you will be prompted to enter 5 names into your Name Bank. Is that okay with you? (yes/no) ", "It seems like you're having trouble. Please type 'yes' to continue with program or 'no' if you would not.")
    if checkIn2.upper() == "NO": # captilization for case sensitivity
        print("Okay, No worries I will send you back to the main menu - where you can select another mode or exit the program if you wish!\n")
        mainMenu()

    addNames(5) # the add names function will be explained later - it is a generic function for allowing the user to add names to their name bank - the instructions say to start with five names no matter what, so this uses five names as a default.
########################################################################################################################
# Below are functions for editing, sorting, adding to or deleting from a name bank.

# The below function serves as menu, similar to the first. It will allow a user to edit a name bank in a variety of ways.
# it handles exceptions to ensure an integer is received as input, and that it is range of the options provided. When a selection
# is made by the user it will call a function that will carry out the intended action. However, differently from the first menu
# it is within a while loop, as this menu must repeatedly come up to allow the user to eventually select "7" and ideally save
# the name bank that they have been editing.
def nbOptions():
    flag = False
    while not flag: # within while loop, to repeatedly come up after a function is completed
        print("What would you like to do with your name bank?\n"
              "[1] Display all names\n"
              "[2] Sort by First Name\n"
              "[3] Sort by Last Name\n"
              "[4] Add Name(s)\n"
              "[5] Edit a Name\n"
              "[6] Remove a Name\n"
              "[7] Save Namebank and Return to Main Menu\n"
              "[8] Quit")
        print("")
        stopper = False
        while not stopper:
            try:
                selection = int(getInput("Enter your selection: ","It seems like you're having some trouble. Enter a selection from 1-8 to make a decision."))
                if selection not in range(1, 9): # error handling
                    raise ValueError
                break
                stopper = True
            except (ValueError, TypeError):
                print("Error detected. Please re-input your selection")
                stopper = False

        if selection == 1: # calls different function locations
            displayNames()
        elif selection == 2:
            sortFName()
        elif selection == 3:
            sortLName()
        elif selection == 4:
            addxNames()
        elif selection == 5:
            editNames()
        elif selection == 6:
            removeName()
        elif selection == 7:
            saveNB()
            flag = True
        elif selection == 8:
            print("Exit has been selected\n"
                  "Thank you using this Name Bank " + name + "!")
            quit(0) # will force quit


# This below function displays all names within a name bank. It uses the global variable for a list of currentNB which is a list of lists - those list being individual names which contain
# a first name and last name. This function is repeatedly called to show edits and to show initial inputs made by the user.
def displayNames():
    global currentNB # calls global variable.
    print("\nYour name bank...")
    print("First Name","\t","Last Name") # generic headers

    for name in currentNB: # for every name in the current name bank
        print(name[0],"\t\t",name[1]) # a first name and last name will be printed, displaying all full names
    print("\n")


# This sorts the currentNB that is being edited alphabetically according to first name.
def sortFName():
    global currentNB # calls global variable for list of name bank
    print("Sort by first name Selected.")

    currentNB = sorted(currentNB, key = lambda y: y[0]) # sorts the name bank, by a a key which focuess on the [0] location in lists which are first names.
                                                        # in currentNB there are names which are [firstName, LastName], and 0 is the location of first name, 1 is last name.
    displayNames() # displays new sorting of names


# Identical to previous function, but it sorts by last name alphabetically.
def sortLName():
    global currentNB
    print("Sort by last name Selected.")

    currentNB = sorted(currentNB, key = lambda y: y[1])
    displayNames()


# This function displays the index for the namebank and is useful for showing the user numbers that they may choose from
# that correspond with a name for editing. Is not directly called from any menu, but is used as display in other functions.
def displayNbInd():
    global currentNB # calls global variable for list of name bank
    print("\n")
    print("\t","First Name",'\t',"Last Name")

    for index in range(len(currentNB)): # for index in range of the length of the current namebank, or for a number of every name within the total length of a namebank.
        print(index+1,"\t", currentNB[index][0],"\t\t",currentNB[index][1]) # this will print a number corresponding to the name (python indexes start at zero) I add one to index so it makes inuitive sense to user. Will display starting at 1, then 2, and so on.
                                                                            # this will will then print all first names and last names for each iteration of for loop using location in list [0] for first names [1] for last names.
    print("\n")


# Function that allows users to edit a name. Will call the function that displays names with index for numbers to correspond to list
# so that the program may find which list needs editing. Runs a try and except loop for handeling exceptions to make sure integer
# is inputed and so that it is a valid option given the length of the index. Also handles errors to make sure that the same name is not inputted twice.
def editNames():
    global currentNB
    print("Edit a name has been selected.")
    stopper = False
    while not stopper:
        displayNbInd()
        try:
            selection = int(getInput("Enter the number for the name you would like to edit: ", "It seems like you're having some trouble. Enter a number that corresponds to a name that you wish to edit."))
            if selection not in range (1,len(currentNB)+1): # added 1 to index earlier so that it displays starting from 1, so adds 1 now to the length, to make sure range for user options is accurate
                raise ValueError
            break
            stopper = True
        except(ValueError, TypeError):
            print("Error detected. Please reinput your entry.")

    stopperA = False
    while not stopperA: # loop for handling a possible exception
        try:
            firstName = getInput("Enter a new First Name: ","It seems like you're having some trouble. Type in a name a press enter to add it into you Name Bank")
            lastName = getInput("Enter a new Last Name: ", "It seems like you're having some trouble. Type in a name a press enter to add it into you Name Bank")
            name = [firstName, lastName]

            nameFound = False # checks to make sure name that is inputted has not already been inputted in list
            for currentName in currentNB: # for all names that are in the name bank
                if currentName[0] == firstName and currentName[1] == lastName: # will check that is not identical
                    nameFound = True # if name found is identical, then boolean for for loop is set to true for error handling.

            if nameFound == True: # error raised for same name
                raise TypeError

            break
            stopperA = True
        except(TypeError):
            print("You have already entered this name. Please enter another name")

    currentNB[selection-1] = name # will change old name in list to new name inputted
    displayNames() # will display changes made to the user


# Very similar to edit name function. Instead of editing, it will remove a name that a user selects at a given location
# within the list.
def removeName():
    global currentNB
    print("Remove a name has been selected. ")
    stopper = False
    while not stopper:
        displayNbInd() # displays index with names corresponding
        try:
            selection = int(getInput("Enter the number for the name you would like to remove: ","It seems like you're having some trouble. Enter a number that corresponds to a name that you wish to remove."))
            if selection not in range (1,len(currentNB)+1): # assures selection is in appropriate range, as mentioned earlier.
                raise ValueError
            break
            stopper = True
        except(ValueError, TypeError): # assures that a intenger is inputted
            print("Error detected. Please reinput your entry.")

    del currentNB[selection-1] # selection gives location in list, and removes that name from the list.
    displayNames() # displays changes made by the user.


# Function to add a given variable amount of names to the current name bank. Will ask user to input a valid integer that is
# greater than zero and is also not equal to zero. Will then pass this number to a function for adding names.
def addxNames():
    stopper = False
    while not stopper:
        try:
            addedNames = int(getInput("How many names would you like to add to your Name Bank: ","It seems like you're having trouble. Please input how many names you would like to enter into your Name Bank."))
            if addedNames <= 0:
                raise ValueError
            stopper = True
        except(ValueError, TypeError):
            print("Error detected. Please reinput your entry.")

    addNames(addedNames) # passing addedNames to addNames


# Generic function for adding names to name bank. Will tell user how many names are being added. Will either be 5 from the first
# initialization or may be a given number as inputted by the user. It will run a loop as long as name counter is greater than
# 0 and will add a name to the name bank for as many times as given. It also assures no exactly identical name is inputted. The
# loop stops when it reaches zero. And names are appended to the list with each iteration.
def addNames(nameCounter):
    global currentNB # uses global variable for the current name bank for editing.
    print("\nYou will now be prompted to enter", nameCounter, "names. Press enter after every prompt to save a name into your Name Bank. Remember you can always change things later!")

    while nameCounter > 0:
        firstName = getInput("Enter a First Name: ", "It seems like, you're having some trouble. Type in a name a press enter to add it into you Name Bank")
        lastName = getInput("Enter a Last Name: ", "It seems like, you're having some trouble. Type in a name a press enter to add it into you Name Bank")
        name = [firstName, lastName]

        nameFound = False # control structure for no identical names previously explained.
        for currentName in currentNB:
            if currentName[0] == firstName and currentName[1] == lastName:
                nameFound = True

        if nameFound == True:
            print("You have already entered this name. Please enter another name")
        else:
            currentNB.append(name) # appends a valid name to the current namebank
            nameCounter -= 1 # decrements with every completed iteration, so that loop runs for intended iterations

    displayNames() # displays edited names
    nbOptions() # calls the name bank options menu, as there is a case where it is not already in the loop - that being
                # on the first calling when it is passed the default 5 names

# saves values to the dictionary for the library.
def saveNB():
    global currentNBName # calls global variable for name of name bank which is a key to dictionary location
    global currentNB # global variable for list of current name bank with all names
    global nameLibrary # calls global variable for dictionary

    if currentNBName == "": # if the current name for the name bank is empty, then a name for it can be made
        currentNBName = getInput("What would you like to name your name bank? ", "It seems like you're a bit stuck. Type in a title for your name bank to save it for later!")

    nameLibrary[currentNBName] = currentNB # will assign a name to the name bank that is being edited and store it in the dictionary as a key.

    currentNBName = "" # will reset name for next iteration
    currentNB = [] # will reset current namebank for next iteration
    print("Your Name Bank has been saved. You will be returned to the main menu. To edit past name banks select 'my library', to make a new name bank select 'create a 5 name list'.\n")


    mainMenu() # returns user to the main menu
########################################################################################################################
# This function allows the user to view their library.
def enterLib():
    global nameLibrary # calls necessary global variables
    global currentNB
    global currentNBName

    print("You have selected the Library Mode")

    if not nameLibrary: # check for boolean to make sure nameLibrary is not empty
        print("Your Name Library is empty. Fill out a Name and come back after :) You will now be returned to the main menu\n")
        mainMenu() # if empty, will return user to the main menu

    keys = list(nameLibrary.keys()) # makes a list of all keys in the name library which is essentially a list of all titles for name banks
    print("Displaying your saved Name Banks...")

    for index in range (len(keys)): # shows index for the length of how many keys are in the dictionary
        print(index+1,"\t",keys[index]) # displays number associatiated with key - python indexes start a 0, adds 1 to be more user intuitive so list may start at 1

    stopper = False
    while not stopper: # gets integer for location of key in the dictionary, so that the program may enter the old name bank for re editing
        try:
            selection = int(getInput("Enter the number for the name bank you would like to edit (type 'main menu' if you wish to go back): ", "It seems like you're having some trouble. Enter a number that corresponds to a Name bank that you wish to edit."))
            if selection not in range(1, len(keys) + 1): # handles exception to make sure choice is valid and avaliable
                raise ValueError
            break
            stopper = True
        except(ValueError, TypeError): # handles variables to assure integer is inputted.
            print("Error detected. Please reinput your entry.")

    key = keys[selection-1] # finds given key as selected by user (subtracts one so it matches with python index, rather than displayed index)
    currentNB = nameLibrary[key] # sets currentNB to the old name bank selected
    currentNbName = key # sets name that is being edited to new key
    print("Loading options for Name Bank editing...\n")

    nbOptions() # user is taken to options to edit their namebank

########################################################################################################################
# Main Code - name is received in introduction, main menu serves as central hub for all other code.
name = getName()
mainMenu()
