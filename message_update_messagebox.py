
import login_logout_messagebox as login

command_error = "Command is wrong, please enter correct command key word"
message_command = "Do you want to write new message or review historical message?\n\n Enter: write (to write new message)\n Enter: review (to review historical message)\n"
select_user = "Please enter user name to write message to: "
username_erro = "Username not exsit, please enter correct username"
username_list = "Below users are in the system right now: \n"
write_command = "write"
write_message_to = "Who you want to send message to? \n"
write_message_confirm = "Message sent successfully. \n"
write_command_msg = "Please enter your message: "
review_command = "review"
review_messag_from = "You received below message: \n"
review_command_msg = "Please enter username to review all the message: "
review_command_empty = "There is incorrect username and there is no message"
user_message_file = "user_message.txt"
test = "This is Test msg"


def read_message_list(file=user_message_file):

    try:
        with open(file, "r") as file:
            user_message_list = [msg.strip() for msg in file.readlines()]

    except EOFError as erro:
        print("Open message file is wrong ", erro)

    return user_message_list


print(read_message_list())


def find_user_message(input_name):
    user_msg_dict = {}
    user_message = read_message_list()

    for msg in user_message:
        name = msg[:msg.index(":")]
        message = msg[msg.index(":") + 1:]

        if name in user_msg_dict:
            user_msg_dict[name].append(message)
        else:
            user_msg_dict[name] = [message]

    if input_name in user_msg_dict:
        message = " ".join("\n").join(user_msg_dict[input_name])
        return message
    else:
        return review_command_empty


def write_message_file(file=user_message_file):
    try:
        with open(file, "a+") as file:
            file.write(str(select_username_message(user_name_list()))+"\n")
    except EOFError as erro:
        print("Open message file is wrong ", erro)


def user_name_list():
    user_info_dict = login.user_info_dict()
    name_list = [name for name in user_info_dict.keys()]

    return name_list


def select_username_message(name_list):
    user_message = ""
    user_name = input(select_user)

    while user_name not in name_list:
        print(username_erro)
        print("Existing users are ", *user_name_list())
        user_name = input(select_user)
    else:
        message_to_user = input(write_command_msg)
        user_message = user_name + ":" + message_to_user

        return user_message


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


def write_message():
    print(username_list)
    print(*user_name_list(), "\n")
    write_message_file()


# write_message()


def review_message():
    print("Existing users are ", *user_name_list())
    user_select = input(review_command_msg)
    messgae = find_user_message(user_select)
    print(messgae)


# review_message()
