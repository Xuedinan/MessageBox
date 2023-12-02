
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
user_info_file = "user_info.txt"

signup_name = ""
login_name = ""


def read_user_file(file=user_info_file):
    try:
        with open(file, "r") as file:
            user_list = [names.strip().casefold()
                         for names in file.readlines()]
            return user_list
    except FileNotFoundError as erro:
        print("User info file is wrong: ", erro)


def add_user_file(file=user_info_file, message=""):
    try:
        with open(file, "a+") as file:
            return file.writelines(message.casefold())
    except FileNotFoundError as erro:
        print("User info file is wrong: ", erro)


def signup():
    while True:
        global signup_name
        signup_name = input(signup_user_msg)
        for names in read_user_file():

            name = names[:names.index(":")]
            if signup_name == name:
                print(signup_erro_user_msg)
                signup_name = input(signup_user_msg)
            else:
                msg_password = str(input(signup_password_msg))
                user_signup_input = str(
                    signup_name+":"+msg_password)
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
                print(password_msg)
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
