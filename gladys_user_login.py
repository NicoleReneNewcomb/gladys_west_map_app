import re
"""
	Student: Edgar Nunez
	Module: user_login
	Description: This module requires an email to start running the app.
    	If the address is an invalid one, the app doesn't start.

"""

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def is_valid_email(lower_email):
    """ Function to valid if an email is correct. Using regular expressions to get the possible ch in
the correct position, the function also works to validate if there is a "@" and a dot (.) //

Args:
    lowerEmail: _email input already passed to lower case_

Returns:
    Boolean: - True if the email is valid
             - False for an incorrect email address
"""
    if re.fullmatch(regex, lower_email):
        return True
    else:
        return False


def login():
    """ Function that converts the input email in lower case /
       If the email is correct, then it asks for the password /

    Returns:
        userName
    """

    while not (is_valid_email == True):

        email_address = input(
            "\nPlease enter an e-mail to initialize the app: ")
        lower_email = email_address.lower()

        if (is_valid_email(lower_email) == True):
            password = input("Please enter your password: ")
            print("Inicialiting West's App...")
            return lower_email  # = userName

        else:
            print("\nInvalid email address, try again please.")
