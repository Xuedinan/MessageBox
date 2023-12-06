"""
Final Project
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Xuedinan Gao

This is the test file for testing all functions that will return value and no requires user input.
All other functions with input request has been tested when build them.

"""

import login_logout_messagebox as log
import updated_message_messagebox as msg


def test_read_user_file():  # testing if can read all username and password in the user info file
    failed = 0

    expected = ['gao:123', 'xdg:123', 'kkk:131', 'tom:123', 'hello:123',
                'siyang:123', 'jack:123', 'justin:123', 'peter:123', 'joyce:123', 'sharon:123']
    actual = log.read_user_file()
    if expected != actual:
        failed += 1
        print("test_read_user_file failed")
        print("expected:", expected)
        print("actual:", actual)

    return failed


def test_user_info_dict():  # testing if function can convert list to dict
    failed = 0

    expected = {'gao': '123', 'xdg': '123', 'kkk': '131', 'tom': '123', 'hello': '123',
                'siyang': '123', 'jack': '123', 'justin': '123', 'peter': '123', 'joyce': '123', 'sharon': '123'}
    actual = log.user_info_dict()
    if expected != actual:
        failed += 1
        print("test_ruser_info_dict")
        print("expected:", expected)
        print("actual:", actual)

    return failed


def test_read_message_receiver_map():  # testing if function can combine all received message for the same user
    failed = 0

    expected = {'justin': ['gao,gao say hello to justin', 'tom,tom say hi to justin'], 'tom': ['gao,gao say yoho to tom', 'jack,yoyoyoyoyo'], 'peter': [
        'gao,hello how are you'], 'jack': ['gao,hello jack this is gao'], 'gao': ['jack,jack say hello to gao', 'peter,peter say yoyoyo to gao'], 'siyang': ['gao,123123123123123123123']}
    actual = msg.read_message_receiver_map()
    if expected != actual:
        failed += 1
        print("test_read_message_receiver_map")
        print("expected:", expected)
        print("actual:", actual)

    return failed


def test_user_name_list():  # testing if can create list with all exsited usernames
    failed = 0

    expected = ['gao', 'xdg', 'kkk', 'tom', 'hello', 'siyang',
                'jack', 'justin', 'peter', 'joyce', 'sharon']
    actual = msg.user_name_list()
    if expected != actual:
        failed += 1
        print("test_user_name_list")
        print("expected:", expected)
        print("actual:", actual)

    return failed


def main():
    failed = 0
    failed += test_read_user_file()
    failed += test_read_message_receiver_map()
    failed += test_user_info_dict()
    failed += test_user_name_list()

    if failed == 0:
        print("All tests passed!")
    else:
        print("Number of tests failed:", failed)


if __name__ == "__main__":
    main()
