# MessageBox

Name: Xuedinan Gao
Semester: CS 5001 Fall 2023 
Topic: Final Project

This is a simple message box program with R/W on the local database, user can leave message to a selected audience in the program and save the message in the program database.
When the user logs back into the program, the user can review the historical message for selected audience.

Interactions with users are

    - User selects login or sign up for program
        - Sign up with user name and credential
            - Program provide error message when username is invalid or exsits
        - Login prorgam with user information

    - Select a audience want to leave message or review message
        - Defual 5 users
        - Option: keep new signed up users name
        - Review message
            - Return empty message when no message exsit for selected audience
            - Print out history message for selected user
                - Option: provide English and Chinese options.

        - User write message and program save it to database
            - Option: using ChatGPT to save with English and Chinese text

    - User log out and exit program
