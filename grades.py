#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program converts level to percentage grades

def convert_level(level_from_user):
    # process & output

    if level_from_user == "4+":
        percent = 97
    elif level_from_user == "4":
        percent = 91
    elif level_from_user == "4-":
        percent = 83
    elif level_from_user == "3+":
        percent = 78
    elif level_from_user == "3":
        percent = 75
    elif level_from_user == "3-":
        percent = 71
    elif level_from_user == "2+":
        percent = 68
    elif level_from_user == "2":
        percent = 65
    elif level_from_user == "2-":
        percent = 61
    elif level_from_user == "1+":
        percent = 58
    elif level_from_user == "1":
        percent = 55
    elif level_from_user == "1-":
        percent = 51
    elif level_from_user == "R":
        percent = 25
    else:
        percent = -1

    return percent


def main():
    # this function calls other functions
    # input

    print("Welcome!")
    level_from_user = input("Enter a level to convert: ")

    # call function
    converted_percent = convert_level(level_from_user)

    # output
    if converted_percent == -1:
        print("\n-1")
        print("\nThanks for participating!")
    else:
        print("\nThanks for participating!")


if __name__ == "__main__":
    main()
