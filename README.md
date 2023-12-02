# Final Project


* Name: Xuedinan Gao
* Semester: CS 5001 Fall 2023 


## MessageBox

This is a simple message box program with R/W on the local database, user can leave message to a selected accounts in the program and save the message in the program database.

When the user logs back into the program, the user can review the historical message that is received from other users.

It's working like a Email system, send or review message.

## Interactions with users are

1. User selects login or sign up for program

    - Sign up with user name and credential
        - Program provide error message when username is invalid or exsits
    - Login prorgam with user information

2. Select a audience want to leave message or review message received from other users

    - Provide defual users
    - Review message
        - Return empty message when no message exsit
        - Print out historical message for the user
            *- Option: provide English and Chinese options.*

    - User write message to selected user and program save it to database
        *- Option: using ChatGPT to save with English and Chinese text*

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


```
**Pending for decesion**

1. Design UI
2. Provide Welcome Message when open program
3. Local DB or FireBase

```