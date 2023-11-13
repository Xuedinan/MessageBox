"""
login check

print out welcome message

using password check

"""

welcome_msg = "\nThanks for using ChatBox. please feel free to leave message for your selected user\n"
options_msg = "Please type in your command:\n \nsignup - creating new account \nlogin - return user login \nexit - exit program\n"
command_signup = "signup"
command_login = "login"
command_exit = "exit"
command_error_msg = "Wrong command"
login_user_msg = "Please enter your username"
login_pass_msg = "Please enter your password"
login_erro_user_msg = "User name is not existing, please doubel check or Signup new account"
login_erro_pass_msg = "Password is incorrect, please doubel check or Signup new account"
signup_user_msg = "Please enter username to sign up"
signup_password_msg = "Please enter password to sign up"


def signup():
    print("signup")


def login():
    print("login")


def get_input():
    msg = input(options_msg + "\nYour command: ")
    return msg


def command_reg(message):

    if message == command_signup:
        return signup()
    elif message == command_login:
        return login()
    elif message == command_exit:
        return
    else:
        print(command_error_msg)
        get_input()


def main():
    print(welcome_msg)
    input = get_input()
    command_reg(input)


main()
