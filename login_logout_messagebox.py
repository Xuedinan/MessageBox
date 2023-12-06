"""
Final Project
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Xuedinan Gao

Functions for login(check username and password), signup(check, save username and password)

"""

options_msg = "Please type in your command:\n \nSignup - creating new account \nLogin - return user login \nExit - exit program\n"
command_signup = "signup"
command_login = "login"
command_exit = "exit"

login_user_msg = "Please enter your Username to login: "
login_pass_msg = "Please enter your Password to login: "
login_erro_user_msg = "--- Username is wrong, please doubel check. --- \n"
login_erro_pass_msg = "--- Password is incorrect, please doubel check. --- \n"

signup_user_msg = "Please enter Username to sign up: "
signup_password_msg = "Please enter Password to sign up: "
signup_erro_user_msg = "----- Username is existed, please select different name. -----\n "
signup_erro_user_empty_msg = "----- Username can not be empty, please try again. -----\n"
signup_erro_password_empty_msg = "----- Password can not be empty, please try again. -----\n "

signup_account_created = "Your account is created. \n"

# defaul txt file which store username and password
user_info_file = "user_info.txt"

# two global variables for login/signup and review/write message
signup_name = ""
login_name = ""


def read_user_file(file=user_info_file):
    """ Read user_info.txt file and create a list with username and password.

    Example:
        >>> read_user_file(file=user_info_file)

        ['gao:123', 'xdg:123', 'kkk:131', 'wuhu:123123', 'tom:123', 
        'hello:123', 'siyang:123', 'jack:123', 'justin:123', 
        'peter:123', 'kaka:123', 'ronald:123', 'jingjing:123']

    Args:
        file=user_info_file)                # default file is user_info.txt

    Returns:
        list = ['username:password', 'username:password', 'username:password']
    """

    try:
        with open(file, "r") as file:
            user_list = [names.strip().casefold()
                         for names in file.readlines()]  # read every lines of the file and remove spaces
            return user_list
    except FileNotFoundError as erro:
        print("User info file is wrong: ", erro)


def add_user_file(file=user_info_file, message=""):
    """ Open user information file and add username, password into file for new signup user.

    Example:
        >>> add_user_file(file=user_info_file, message="zitong:123")
        write zitong:123 on user_info.txt file with new line

    Args:
        add_user_file(file=user_info_file, message="")              # default file is user_info.txt, default message is none

    Returns:
        write signup information with data structure username:password
    """

    try:
        with open(file, "a+") as file:  # add information to the next line by "a+"
            return file.writelines(message.casefold())
    except FileNotFoundError as erro:
        print("User info file is wrong: ", erro)


def get_input_for_error(erro_message):
    """
    print out error message for invalid username input and keep getting input
    """
    print(erro_message)

    # allow user to add space on their username, no strip()
    signup_name = input(signup_user_msg).casefold()

    return signup_name


def signup():
    """ Function for signup, ask user to provide username and password then pass them to the add_user_file() to save in the user_info.txt file.
        When the input username is exsit in the program, will ask user to enter a new username until get correct username.

        Save username and password with structure as username:password -> pass to user_info.txt

        Function will return booline result for main_messagebox.py main() to run the following program (review, write, etc..)

    Example:
        >>> signup()

        username: gao
        print error message, Username is existed, please select different name.

        username: robert
        password: 123
        pass robert:123 to add_user_file() and return booline

    Args:
        signup()

    Returns:
        booline
    """
    # change global variable signup_name, will use it for review/write functions
    # signup_name defaul value is ""
    global signup_name
    # get input signup username
    signup_name = input(signup_user_msg).casefold()

    all_names = []
    for names in read_user_file():  # get all exsited usernames list
        all_names.append(names.split(":")[0].casefold())

    while True:  # keep requesting username and password, stop when input is valid

        if len(signup_name.strip()) == 0:   # check if username is empty
            signup_name = get_input_for_error(signup_erro_user_empty_msg)

        elif signup_name in all_names:  # check if username is exsited
            signup_name = get_input_for_error(signup_erro_user_msg)

        else:
            # if username is confirmed, then ask for password
            msg_password = str(input(signup_password_msg))

            if len(msg_password.strip()) != 0:  # check if password input is empty
                # save username and password with structure = username:password, add to txt file after below checks
                user_signup_input = str(signup_name+":"+msg_password)
                # add to the user_info.txt when input is not empty
                add_user_file(message="\n" + user_signup_input)
                print(signup_account_created)
                return False
            else:
                # inform user password can not be empty
                print(signup_erro_password_empty_msg)

                while True:  # keep getting password input until it's not empty

                    if len(msg_password.strip()) == 0:  # check if password is empty
                        msg_password = str(input(signup_password_msg))
                        print(signup_erro_password_empty_msg)
                    else:
                        # when username and password are not empty, save them to the txt file
                        user_signup_input = str(signup_name+":"+msg_password)
                        add_user_file(message="\n" + user_signup_input)
                        print(signup_account_created)
                        return False


def user_info_dict():
    """ Create a dict by reading user_info.txt file for existed user information, return dict with {"username":"password"}

    Example:
        >>> user_info_dict()

        {'gao':'123', 'xdg':'123', 'kkk':131'}

    Args:
        user_info_dict()

    Returns:
        user information dict {"username":"password"}
    """
    user_dict = {}
    # get existed user list from user_info.txt file
    user_list = read_user_file()
    for user in user_list:
        user_password = user.strip().split(":")
        # create dict with {"username":"password"}
        user_dict[user_password[0]] = user_password[1]
    return user_dict


def login():
    """ login function, get user input of username, then check if input username is matching the password in the user_info.txt file.
        If input username is not existed in the user_info.txt file, then return error message and break the program.

        If password is correct then login() will return booline result for using in the following message functions (review, write, etc).

    Example:
        >>> user_info_dict()

        username: Tim
        print error message, Username is wrong, please doubel check.

        username: gao
        password: 9999999
        print error message, Password is incorrect, please doubel check.

        username: gao
        password: 123
        return booline

    Args:
        login()

    Returns:
        booline
    """
    user_dict = user_info_dict(
    )  # get dict {"username":"password"} for matching

    while True:  # function will stop when input login information is correct

        # change global variable login_name, will use it for review/write functions
        # login_name defaul value is ""
        global login_name
        login_name = input(login_user_msg).casefold()
        for names in user_dict.keys():
            if login_name == names:  # check if input username is existed in the program
                password_msg = input(login_pass_msg)
                # check if input password is matching in dict {"username":"password"}
                if password_msg == user_dict[login_name]:
                    return False  # return false to exit the loop
                else:
                    print(login_erro_pass_msg)
                    while True:
                        password_msg = input(login_pass_msg)
                        if password_msg == user_dict[login_name]:
                            return False
                        else:
                            print(login_erro_pass_msg)
        else:
            print(login_erro_user_msg)


def get_command_input():
    """ Get user input for selecting command options.
        Signup
        Login
        Exit

    Example:
        >>> get_command_input()

        return "signup"

    Args:
        get_command_input()

    Returns:
        str: signup, login or exit
    """
    msg = input(options_msg + "\nYour command: ")
    return msg
