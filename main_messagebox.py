"""
1. welcome
2. get user command
3. check user command
    3.1 sign up
    3.2 log in
    3.3 ask for action
        3.3.1 review message
            a. select user
            b. print out message
        3.3.2 write message
            a. select user
            b. save message to local file
4. exit 

"""

import login_logout_messagebox as log_action
import message_update_messagebox as msg_action

welcome_msg = "\nThanks for using MessageBox. This is a small program to help you to leave a message to your favourite person : )\n"
exit_msg = "\nProgram has been terminalted, thanks for using :) \n"
command_error_msg = "Wrong command"


def active_signup():
    pass


def active_message():
    pass


def main():
    print(welcome_msg)

    log_msg = log_action.login_get_input()

    if log_msg == log_action.command_signup:
        # need to check duplicate username

        if log_action.signup() == False:
            msg_msg = msg_action.message_get_input()
            msg_action.command_msg(msg_msg)
    if log_msg == log_action.command_login:
        if log_action.login() == False:
            msg_msg = msg_action.message_get_input()
            msg_action.command_msg(msg_msg)
    else:
        print(command_error_msg)
        print(exit_msg)


main()
