import gladys_compute as compute
import gladys_satellite as satellite
import gladys_user_login as user_login

"""
	Student: Cliff So and Adrian Dang
	Module: gladys_user_interface
	Description: This module lists the menu and interfaces to all other modules. 
	It allows the user to set their current position and destination, calculate 
	the distance between them, and run tests. 
	
"""
# initialize the current position, destination, and distance
x_current_position = int(-1)
y_current_position = int(-1)
x_destination = int(-1)
y_destination = int(-1)
distance = 0


def start():
    """
            logs the user in, and runs the app
    """
    # global userName
    userName = user_login.login()

    run_app(userName, x_current_position, y_current_position,
            x_destination, y_destination, distance)

# function to run tests


def run_tests(user_name):
    """
    Tests some module functions.
    """
    print("Running a few tests:")

    # test if user logged in
    print("User Logged In? ")
    if (user_name.isspace()):
        print("=== No ===")
    else:
        print("=== Yes ====")

    # show current user_name
    print("Current User Name: ", user_name)

    average = compute.gps_average(4, 5)
    print("Average: ", average)

    distance = compute.distance(4, 5, 45, 60)
    print("Distance: ", distance)

# function to print a line


def print_line():
    print("----------------------------------------")

# function to print a command with a description


def print_command(command, desc):
    print("[{}] {}".format(command, desc))

# function to print the current position


def print_current_position(x, y):
    print("Current position: x = {}, y = {}".format(x, y))


# function to print the destination position
def print_destination(x, y):
    print("Destination position: x = {}, y = {}".format(x, y))


# function to print the distance
def print_distance(distance):
    print("Distance: {}".format(distance))

# function to validate user input


def validate_input(user_input):
    """
    Returns True if user_input is an integer between 0 and 99.
    """
    try:
        user_input = int(user_input)
        if 0 <= user_input <= 99:
            return True
        else:
            print("Number must be int and between 0-99")
            return False
    except ValueError:
        print("Invalid input: Please enter an integer.")
        return False


# function to print the menu
def print_menu(x_current_position, y_current_position, x_destination, y_destination, distance):
    """
    Prints the menu.
    """
    print()
    print_current_position(x_current_position, y_current_position)
    print_destination(x_destination, y_destination)
    print_distance(distance)
    print()
    print_command('c', "to set current position")
    print_command('d', "to set destination position")
    print_command('m', "to map - which to tell the distance")
    print_command('t', "to run model tests")
    print_command('q', "to quit")
    print()


def run_app(user_name, x_current_position, y_current_position, x_destination, y_destination, distance):
    """
            runs the app
    """
    # loop until user types q
    user_quit = False
    while (not user_quit):

        # menu

        print_line()
        print("-- Welcome to the Gladys West Map App --")
        print_line()
        print("username: ", user_name)
        print_menu(x_current_position, y_current_position,
                   x_destination, y_destination, distance)

        # get first character of input
        user_input = input("Enter a command:")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]

        # menu choices, use a switch-like if-elif control structure

        # quit
        if first_char == 'q':
            user_quit = True

        # run some tests (this is part 1 of 2)
        elif first_char == 't':
            run_tests(user_name)

        elif first_char == 'c':

            try:
                user_input = int(input("Enter a X position: "))
                if (validate_input(user_input) == True):
                    x_current_position = user_input
                else:
                    continue
            except:
                print("Invalid input: Number must be integer and between 0-99")
                continue

            try:
                user_input = int(input("Enter a Y position: "))
                if (validate_input(user_input) == True):
                    y_current_position = user_input
            except:
                print("Invalid input: Number must be integer and between 0-99")

            # runTests()

        elif first_char == 'd':

            try:
                user_input = int(input("Enter a X position: "))
                if (validate_input(user_input) == True):
                    x_destination = user_input
                else:
                    continue
            except:
                print("Invalid input: Number must be integer and between 0-99")
                continue

            try:
                user_input = int(input("Enter a Y position: "))
                if (validate_input(user_input) == True):
                    y_destination = user_input
            except:
                print("Invalid input: Number must be integer and between 0-99")

            # runTests()

        elif first_char == 'm':
            distance = compute.distance(
                x_current_position, y_current_position, x_destination, y_destination)
            print_line()
            print("distance: ", distance)
            print_line()
            print()
            # run_tests()

        else:
            print("ERROR: " + first_char + " is not a valid command")

    print("\n")
    print("Thank you for using the Gladys West Map App!")
    print("\n")
