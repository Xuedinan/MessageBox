## Final Project


* Name: Xuedinan Gao
* Github Username: DinanG
* Semester: Fall 2023
* Course: CS 5001 


## Project Overview

This is an "email" program called "MessageBox" with Review and Write on the local database, user can leave message to a selected accounts in the program and save the message in the program database.

When the user login back into the program, the user can review the historical message that is received from other users.

It's working like a Email system, send or review message.


## Program run guidance

1. #### Program structure 

- MessageBox inlude 5 files in total

    - Three .py files
        - login_logout_messagebox.py        # stored all functions for login and signup

        - updated_message_messagebox.py         # storeed all functions for review or send message 

        - main_messagebox.py        # main() function

    - Two .txt files
        - user_info.txt         # stored username and password with data format "username:password"

        - user_message.txt      # stored sender, receiver and message information with data format "sender,receiver,message"
    
2. #### How to run or test program? 
    - User could directly run main_messagebox.py and follow instruction to signup account and send message to the accounts in the system. (Review message won't work, because this is new account)

    - User could directly run main_messagebox.py and login program with test account 
        - "username: gao / password: 123" to review the existing message for "gao"

## Interactions with users are

1. User selects login or sign up for program

    - Sign up with user name and credential (signup)
        - Program provide error message when username is invalid or exits
    - Login program with user information (login)

2. Select a audience want to leave message or review message received from other users

    - Provide default users
    - Review message
        - Return empty message when no message exsit
        - Print out historical message for the user

    - User write message to selected user and program save it to database

3. User log out and exit program

Simple work-flow

    1. welcome
    2. get user command
    3. check user command
        3.1 sign up
        3.2 log in
        3.3 ask for action
            3.3.1 review message
                a. only review users message
                b. print out message
            3.3.2 write message
                a. select user
                b. save message to local file
    4. exit 

## Example of test run

1. login with test account "username: gao / password: 123"
2. select review message to "gao"

```
----- Thanks for using MessageBox. This is a small program to help you to leave a message to your favourite person : ) -----

Please type in your command:
 
Signup - creating new account 
Login - return user login 
Exit - exit program

Your command: LoGin
Please enter your Username to login: GaO
Please enter your Password to login: 123
Do you want to write new message or review historical message?

 Enter: Write (to write new message)
 Enter: Review (to review historical message)
 Enter: Exit (to exit program)

Your command: ReView

------ You received below message -----

Sender: Jack
Message: Jack say hello to gao

Sender: Peter
Message: Peter say yoyoyo to gao
```

3. More demo run with testing edge cases
```
----- Thanks for using MessageBox. This is a small program to help you to leave a message to your favorite person : ) -----

Please type in your command:
 
Signup - creating new account 
Login - return user login 
Exit - exit program

Your command: signup
Please enter Username to sign up: gao
----- Username is existed, please select different name. -----
 
Please enter Username to sign up:  
----- Username can not be empty, please try again. -----

Please enter Username to sign up: tester
Please enter Password to sign up:  
----- Password can not be empty, please try again. -----
 
Please enter Password to sign up: 123
----- Password can not be empty, please try again. -----
 
Your account is created. 

Do you want to write new message or review historical message?

 Enter: Write (to write new message)
 Enter: Review (to review historical message)
 Enter: Exit (to exit program)

Your command: asdasdasd
----- Command is wrong, please enter correct command key word -----

Do you want to write new message or review historical message?

 Enter: Write (to write new message)
 Enter: Review (to review historical message)
 Enter: Exit (to exit program)

Your command: WRiTe

--- Below users are in the system right now ---

Gao
Xdg
Kkk
Tom
Hello
Siyang
Jack
Justin
Peter
Joyce
Sharon
Tester

Please enter user name to write message to: I'm not sure

----- Username not exsit, please enter correct username -----


Please enter user name to write message to: jACk
Please enter your message: Hi Jack, this is test message~

 Your message is saved. 

Do you want to write new message or review historical message?

 Enter: Write (to write new message)
 Enter: Review (to review historical message)
 Enter: Exit (to exit program)

Your command: eXIt

----- Program has been terminalted, thanks for using :) -----

```

## What's Next?

1. Design UI and create website
    - Provide easy-to-use uI, like clicking button to active function, not by typing words in the terminal

2. More security for user information by Encrypt and Decrypt password
    - Since user txt file is public, we need to plugin encrypt and decrypt password function, make sure all information is well maintained

3. Provide Forward, Draft, Delete message functions
    - Like real email system, need to add above function into the program.
    - Also consider using different data structures to easily access information from txt file

4. Connect API to provide message translation service
    - This is a "fancy" thought and the easiest way to make program is related to AI. just call API of ChatGPT then translate the message to different languages

5. Use cloud database to store all information
    - This is also related to password security and making sure the message information is well-stored


## Final thought on this assignment

First of all, I've been enjoying this final project. It opened my mind to how to build a program from scratch even if it's just a simple program without fancy features. But I learned a lot during it. I did a few times updates on the whole design as long as I decided to provide different features, I think it's just like a Sprint in the real SWE world. 

Besides learning how to design, how to code, I noted the importance of time management and scope assessment of the whole project. I made my progress smoothly and made sure it was under control. Overall, this is a great experience and practical learning. Thank you for offering it with wide-open flexibility.