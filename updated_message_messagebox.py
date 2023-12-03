
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

# defaul txt file which store sender, receiver and message
user_message_file = "user_message.txt"


def read_message_receiver_map(file=user_message_file):
    """ Read user_message.txt file and create a dict with receiver, sender and message information.
        For the same receiver received multiple message from different senders, will stor them in the same dict.

    Example:
        >>> read_message_receiver_map(file=user_message_file)

        {'justin': ['gao,gao say hello to justin', 'tom,tom say hi to justin'], 'tom': ['gao,gao say yoho to tom', 'jack,yoyoyoyoyo']}

    Args:
        read_message_receiver_map(file=user_message_file)               # default file is user_message.txt

    Returns:
        dict = {"receiver":['sender, message', 'sender, message']}
    """

    receiver_map = {}

    try:
        with open(file, "r") as file:
            # get each line information from file and create list
            user_message_list = [msg.strip() for msg in file.readlines()]

            for msg in user_message_list:
                # create new list and split to [sender, receiver, message]
                msg = msg.split(",")
                sender = msg[1]  # get sender name
                if sender in receiver_map:  # if sender in the dict, then add message to the value
                    receiver_map[sender].append(msg[0]+","+msg[2])
                else:
                    # if sender not in the dict then add sender and value
                    receiver_map[sender] = [msg[0]+","+msg[2]]

    except FileNotFoundError as erro:
        print("Open message file is wrong ", erro)

    return receiver_map


def receiver_message(input_name):
    """ Check recevied message in the prorgam for input username. 
        Function will pass sender name and received message to print function.

    Example:
        >>> receiver_message(input) # input = "gao"

        # below message are in the file
        # jack,gao,jack say hello to gao
        # peter,gao,peter say yoyoyo to gao

        pass sender "jack" message "jack say hello to gao" to the print function
        pass sender "peter" message "peter say yoyoyo to gao" to the print function


    Args:
        receiver_message(input_name)    # input_name = receiver name       

    Returns:
        call print_receiver_mssage(name, message)
    """

    receiver_dic = read_message_receiver_map()  # get sender,receiver, message dict

    for receiver in receiver_dic.keys():
        if input_name == receiver:  # check if input name is one of the receiver in the dict
            # get message for input name
            received_message = receiver_dic[input_name]

            for item in received_message:
                # create list with [sender, message]
                sender_msg = item.split(",")
                # pass sender, message to print function
                print_receiver_mssage(sender_msg[0], sender_msg[1])


def print_receiver_mssage(sender, message):
    """ print out sender and message.

    Example:
        >>> print_receiver_mssage(jack, message)

        Sender: jack
        Message: jack say hello to gao

    Args:
        print_receiver_mssage(sender, message)

    Returns:
        print out
    """

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
