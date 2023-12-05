
import login_logout_messagebox as login

message_command = "Do you want to write new message or review historical message?\n\n Enter: Write (to write new message)\n Enter: Review (to review historical message)\n Enter: Exit (to exit program)\n"
command_error = "----- Command is wrong, please enter correct command key word -----\n"
exit_msg = "\n----- Program has been terminalted, thanks for using :) -----\n"

select_user = "\nPlease enter user name to write message to: "
username_erro = "\n----- Username not exsit, please enter correct username -----\n"
username_list = "\n--- Below users are in the system right now ---\n"

write_command = "write"
write_message_to = "\nWho you want to send message to? \n"
write_message_confirm = "Message sent successfully. \n"
write_command_msg = "Please enter your message: "
write_message_exit = "\n Your message is saved. \n"

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
                msg = msg.split("%&%")
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

    print(f"Sender: {sender.capitalize()}\nMessage: {message.capitalize()}\n")


def write_message_file(file=user_message_file):
    """ Receive str: sender,receiver,message and write on user_message.txt file

    Example:
        >>> write_message_file(file=user_message_file)
        sender: jack
        receiver: tom
        message: jack say hello to tom

        add new line on txt file with: jack,tom,jack say hello to tom

    Args:
        write_message_file(file=user_message_file)          # default file is user_message.txt

    Returns:
        updated on user_message.txt
    """

    try:
        with open(file, "a+") as file:  # add new line on file
            # get sender,receiver,message and write on txt file
            file.write(str(write_username_message(
                user_name_list())).casefold()+"\n")
    except FileNotFoundError as erro:
        print("Open message file is wrong ", erro)


def user_name_list():
    """ Get name list that all registered accounts in the program.

    Example:
        >>> user_name_list()
        ['gao', 'peter', 'jack', ...]

    Args:
        user_name_list()        # call user_info.dict() from login_logout_messagebox.py

    Returns:
        list
    """
    user_info_dict = login.user_info_dict()  # get dict {"name":"password"}
    # only get names from dict and save into list
    name_list = [name for name in user_info_dict.keys()]

    return name_list


def write_username_message(name_list):
    """ ask user to input message for selected receiver, then create str with data structure
        sender(login or signup name),receiver,message 

    Example:
        >>> write_username_message(['tom', 'gao', 'jack'])
        user,gao,user say hello to gao

    Args:
        write_username_message(name_list)        # name list

    Returns:
        str: sender,receiver,message
    """
    user_message = ""
    # ask user to select receiver
    user_name = input(select_user).strip().casefold()

    while user_name not in name_list:  # print out error message when receiverr name is not in the program
        print(username_erro)
        user_name = input(select_user).strip().casefold()

        # check if if user selected login or signup in the program by comparing two global variable
    else:
        if login.login_name != "":
            message_to_user = input(write_command_msg)
            # create str: sender,receiver,message
            user_message = login.login_name + "%&%" + user_name + "%&%" + message_to_user
        elif login.signup_name != "":
            message_to_user = input(write_command_msg)
            # create str: sender,receiver,message
            user_message = login.signup + "%&%" + user_name + "%&%" + message_to_user

        return user_message


def message_get_input():
    """ 
        ask user to input command to review or write or exit prorgam.
    """
    msg = input(message_command + "\nYour command: ")

    return msg


def login_command_msg(message):
    """ 
       when user login program, check user selected command, then call write function, review function or exit program.
    """
    message = message.strip().casefold()

    while message != "exit":  # keep listening for command

        if message == write_command:
            return write_message()
        elif message == review_command:
            return review_message(login.login_name)
        else:
            print(command_error)
            message = input(message_command + "\nYour command: ").casefold()
            continue

    print(exit_msg)


def signup_command_msg(message):
    """ 
       when user signup program, check user selected command, then call write function, review function or exit program.
    """
    message = message.strip().casefold()

    while message != "exit":  # keep listening for command

        if message == write_command:
            return write_message()
        elif message == review_command:
            return print(review_no_message)
        elif message == "exit":
            return
        else:
            print(command_error)
            message = input(message_command + "\nYour command: ").casefold()
            continue


def write_message():
    """ Print usernames in the program then ask user to select a user to write message. 
        Save message in the user_message.txt file.

    Example:
        >>> write_message()
        --- Below users are in the system right now ---

        gao
        xdg
        kkk

        Please enter user name to write message to:

    Returns:
        print out each name in different line, save message
    """
    print(username_list)
    for users in user_name_list():
        users = users.capitalize()
        print(users)

    write_message_file()
    print(write_message_exit)

    # keep listening command
    login_command_msg(message_get_input().strip().casefold())


def review_message(name):
    """
        ask user to input name for review then pass name to receiver_message(name) to review message.
    """
    print(review_messag_from)
    receiver_message(name)

    # keep listening command
    login_command_msg(message_get_input().strip().casefold())
