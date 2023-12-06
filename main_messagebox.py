"""
Final Project
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Xuedinan Gao

Main function for the program, work-flow as below.

1. welcome
2. get user command
3. check user command
    3.1 sign up
    3.2 log in
    3.3 ask for action
        3.3.1 review message
            a. only review login users message
                - new signup user has no message to review
            b. print out message
        3.3.2 write message
            a. select user
            b. save message to local file
4. exit 

"""

import login_logout_messagebox as log_action
import updated_message_messagebox as msg_action

welcome_msg = "\n----- Thanks for using MessageBox. This is a small program to help you to leave a message to your favorite person : ) -----\n"
exit_msg = "\n----- Program has been terminalted, thanks for using :) -----\n"
command_error_msg = "\n----- Wrong command \n"
exit_program = "exit"


def main():
    print(welcome_msg)

    log_msg = log_action.get_command_input()  # get command for login or signup

    # if user is signing up then go through signup process
    if log_msg.casefold() == log_action.command_signup:
        if log_action.signup() == False:
            # ask user to review or write message
            msg_msg = msg_action.message_get_input().strip().casefold()
            # call write or review functions
            msg_action.signup_command_msg(msg_msg)

    # if user is login then go through login process
    elif log_msg.casefold() == log_action.command_login:
        if log_action.login() == False:
            # ask user to review or write message
            msg_msg = msg_action.message_get_input().strip().casefold()
            # call write or review functions
            msg_action.login_command_msg(msg_msg)
    else:
        print(command_error_msg)
        print(exit_msg)


if __name__ == "__main__":
    main()
