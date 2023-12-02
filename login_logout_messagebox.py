
options_msg = "Please type in your command:\n \nsignup - creating new account \nlogin - return user login \nexit - exit program\n"
command_signup = "signup"
command_login = "login"
command_exit = "exit"

login_user_msg = "Please enter your username to login: "
login_pass_msg = "Please enter your password to login: "
login_erro_user_msg = "Username is wrong, please doubel check. "
login_erro_pass_msg = "Password is incorrect, please doubel check. "

signup_user_msg = "Please enter username to sign up: "
signup_password_msg = "Please enter password to sign up: "
signup_erro_user_msg = "Username is existed, please different name. "
signup_account_created = "Your account is created. \n"

# defaul txt file which store username and password
user_info_file = "user_info.txt"

# two global variables for login/signup and review/write message
signup_name = ""
login_name = ""


def read_user_file(file=user_info_file):
    """Read user_info.txt file and create a list with username and password.

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
    """Open user information file and add username, password into file for new signup user.

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


def signup():
    """ Function for signup, ask user to provide username and password then pass them to the add_user_file() to save in the user_info.txt file.
        When the input username is exsit in the program, will ask user to enter a new username until get correct username.

        Save username and password with structure as username:password -> pass to user_info.txt

        Function will return booline result for main_messagebox.py main() to run the following program (review, write, etc..)

    Example:
        >>> signup()

        username: gao
        print error message, Username is existed, please different name.

        username: robert
        password: 123
        pass robert:123 to add_user_file() and return booline

    Args:
        signup()                # No args needed

    Returns:
        booline
    """
    while True:
        # change global variable signup_name, will use it for review/write functions
        # signup_name defaul value is ""
        global signup_name

        # get input signup username
        signup_name = input(signup_user_msg)
        for names in read_user_file():

            # get exsited username from user_info.txt and compare with input name
            name = names[:names.index(":")]
            if signup_name == name:
                print(signup_erro_user_msg)
                signup_name = input(signup_user_msg)
            else:
                # if username is confirmed, then ask for password
                msg_password = str(input(signup_password_msg))
                user_signup_input = str(
                    signup_name+":"+msg_password)  # structure = username:password

                # add to the user_info.txt
                add_user_file(message="\n" + user_signup_input)
                print(signup_account_created)
                return False


def user_info_dict():
    user_dict = {}
    user_list = read_user_file()
    for user in user_list:
        user_password = user.strip().split(":")
        user_dict[user_password[0]] = user_password[1]
    return user_dict


def login():
    user_dict = user_info_dict()
    while True:
        global login_name
        login_name = input(login_user_msg)
        for names in user_dict.keys():
            if login_name == names:
                password_msg = input(login_pass_msg)
                if password_msg == user_dict[login_name]:
                    return False
                else:
                    print(login_erro_pass_msg)
                    break
        else:
            print(login_erro_user_msg)


def login_get_input():
    msg = input(options_msg + "\nYour command: ")
    return msg
