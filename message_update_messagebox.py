"""
command

selecte user

read

write

chinese version


leave and write message

"""

import login_logout_messagebox as login

command_error = "Command is wrong, please enter correct command key word"
message_command = "Do you want to write new message or review historical message?\n\n Enter: write (to write new message)\n Enter: review (to review historical message)\n"
select_user = "Please enter user name to write message to: "
username_list = "Below users are in the system right now: \n"
write_command = "write"
write_command_msg = "Please enter your message: "
review_command = "review"


def read_message_file(file="user_message.txr"):
    pass


def write_message_file(file="user_message.txr"):
    try:
        with open(file, "a+") as file:
            pass
    except EOFError as erro:
        print("Open message file is wrong ", erro)


def user_name_list():
    user_info_dict = login.user_info_dict()
    name_list = [name for name in user_info_dict.keys()]
    return name_list


def write_message():
    print(username_list)
    print(*user_name_list())
    user_msg = input(select_user)


def review_message():
    pass


def message_get_input():
    msg = input(message_command + "\nYour command: ")
    return msg


def command_msg(message):
    if message == "write":
        return write_message()
    elif message == "review":
        return review_message()
    else:
        print(command_error)
        return message_get_input()
