"""
1. welcome
2. get user command
3. check user command
    3.1 sign up
    3.2 log in
    3.3 ask for action
        3.3.1 review message
            a. only review users message
            a. select user #######
            b. print out message
        3.3.2 write message
            a. select user
            b. save message to local file
4. exit 

edge case:

1. send message to myself
2. how to exit
3. new command, delete message?


"""

import login_logout_messagebox as log_action
import updated_message_messagebox as msg_action

welcome_msg = "\nThanks for using MessageBox. This is a small program to help you to leave a message to your favourite person : )\n"
exit_msg = "\nProgram has been terminalted, thanks for using :) \n"
command_error_msg = "\n--- Wrong command ---\n"


def active_signup():
    pass


def active_message():
    pass


def main():
    print(welcome_msg)

    log_msg = log_action.login_get_input()

    if log_msg == log_action.command_signup:
        if log_action.signup() == False:
            msg_msg = msg_action.message_get_input()
            msg_action.signup_command_msg(msg_msg)

    elif log_msg == log_action.command_login:
        if log_action.login() == False:
            msg_msg = msg_action.message_get_input()
            msg_action.login_command_msg(msg_msg)
    else:
        print(command_error_msg)
        print(exit_msg)


main()
