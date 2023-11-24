"""
login check

print out welcome message

using password check

"""

welcome_msg = "\nThanks for using ChatBox. please feel free to leave message for your selected user\n"
exit_msg = "\nProgram has been terminalted, thanks for using :) \n"
options_msg = "Please type in your command:\n \nsignup - creating new account \nlogin - return user login \nexit - exit program\n"
command_signup = "signup"
command_login = "login"
command_exit = "exit"
command_error_msg = "Wrong command"
login_user_msg = "Please enter your username to login: "
login_pass_msg = "Please enter your password to login: "
login_erro_user_msg = "Username is wrong, please doubel check. "
login_erro_pass_msg = "Password is incorrect, please doubel check. "
signup_user_msg = "Please enter username to sign up: "
signup_password_msg = "Please enter password to sign up: "
signup_erro_user_msg = "Username is existed, please different name. "
user_info_file = "user_info.txt"


def read_user_file(file=user_info_file):
    try:
        with open(file, "r") as file:
            user_list = [names.strip() for names in file.readlines()]
            return user_list
    except EOFError as erro:
        print("User info file is wrong: ", erro)


def add_user_file(file=user_info_file, message=""):
    try:
        with open(file, "a+") as file:
            return file.writelines(message)
    except EOFError as erro:
        print("User info file is wrong: ", erro)


def signup():
    while True:
        msg_username = input(signup_user_msg)
        if msg_username in read_user_file():
            print(signup_erro_user_msg)
        else:
            msg_password = str(input(signup_password_msg))
            user_signup_input = str(msg_username+":"+msg_password)
            add_user_file(message="\n" + user_signup_input)
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
        username_msg = input(login_user_msg)
        for names in user_dict.keys():
            if username_msg == names:
                password_msg = input(login_pass_msg)
                if password_msg == user_dict[username_msg]:
                    return False
                else:
                    print(login_erro_pass_msg)
                    print(exit_msg)
                    return False
        else:
            print(login_erro_user_msg)


def login_get_input():
    msg = input(options_msg + "\nYour command: ")
    return msg


def command_log(message):

    if message == command_signup:
        return signup()
    elif message == command_login:
        return login()
    elif message == command_exit:
        return ""
    else:
        print(command_error_msg)
        login_get_input()
