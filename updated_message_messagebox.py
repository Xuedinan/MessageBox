
import login_logout_messagebox as login

message_command = "Do you want to write new message or review historical message?\n\n Enter: write (to write new message)\n Enter: review (to review historical message)\n Enter: exit (to exit program)\n"
command_error = "Command is wrong, please enter correct command key word"

select_user = "\nPlease enter user name to write message to: "
username_erro = "Username not exsit, please enter correct username"
username_list = "\n--- Below users are in the system right now ---\n"

write_command = "write"
write_message_to = "\nWho you want to send message to? \n"
write_message_confirm = "Message sent successfully. \n"
write_command_msg = "Please enter your message: "

review_command = "review"
review_messag_from = "\n------ You received below message -----\n"
review_command_msg = "Please enter username to review all the message: "
review_command_empty = "There is incorrect username and there is no message"
review_no_message = "\n---You don't have message since you just created the account---\n"

user_message_file = "user_message.txt"


def read_message_sender_map(file=user_message_file):

    sender_map = {}

    try:
        with open(file, "r") as file:
            user_message_list = [msg.strip() for msg in file.readlines()]
            for msg in user_message_list:
                msg = msg.split(",")
                sender = msg[0]
                if sender in sender_map:
                    sender_map[sender].append(msg[1]+","+msg[2])
                else:
                    sender_map[sender] = [msg[1]+","+msg[2]]

    except FileNotFoundError as erro:
        print("Open message file is wrong ", erro)

    return sender_map


def read_message_receiver_map(file=user_message_file):

    receiver_map = {}

    try:
        with open(file, "r") as file:
            user_message_list = [msg.strip() for msg in file.readlines()]
            for msg in user_message_list:
                msg = msg.split(",")
                sender = msg[1]
                if sender in receiver_map:
                    receiver_map[sender].append(msg[0]+","+msg[2])
                else:
                    receiver_map[sender] = [msg[0]+","+msg[2]]

    except FileNotFoundError as erro:
        print("Open message file is wrong ", erro)

    return receiver_map


print(read_message_receiver_map())


def read_message_list(file=user_message_file):

    try:
        with open(file, "r") as file:
            user_message_list = [msg.strip() for msg in file.readlines()]

    except FileNotFoundError as erro:
        print("Open message file is wrong ", erro)

    return user_message_list


def receiver_message(input_name):

    receiver_dic = read_message_receiver_map()

    for receiver in receiver_dic.keys():
        if input_name == receiver:
            received_message = receiver_dic[input_name]

            for item in received_message:
                sender_msg = item.split(",")
                print_receiver_mssage(sender_msg[0], sender_msg[1])


def print_receiver_mssage(sender, message):
    print(f"Sender: {sender}\nMessage: {message}\n")


def write_message_file(file=user_message_file):
    try:
        with open(file, "a+") as file:
            file.write(str(select_username_message(user_name_list()))+"\n")
    except FileNotFoundError as erro:
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
        if login.login_name != "":
            message_to_user = input(write_command_msg)
            user_message = login.login_name + "," + user_name + "," + message_to_user
        elif login.signup_name != "":
            message_to_user = input(write_command_msg)
            user_message = login.signup + "," + user_name + "," + message_to_user

        return user_message


def message_get_input():
    msg = input(message_command + "\nYour command: ")

    return msg


def login_command_msg(message):
    if message == "write":
        return write_message()
    elif message == "review":
        return review_message(login.login_name)
    elif message == "exit":
        return
    else:
        print(command_error)
        return message_get_input()


def signup_command_msg(message):
    if message == "write":
        return write_message()
    elif message == "review":
        return print(review_no_message)
    elif message == "exit":
        return
    else:
        print(command_error)
        return message_get_input()


def write_message():
    print(username_list)
    for users in user_name_list():
        print(users)

    write_message_file()


def review_message(name):
    print(review_messag_from)
    receiver_message(name)
