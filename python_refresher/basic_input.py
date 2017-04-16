import sys


def who_do_you_know():
    # ask the user for a list of people they know
    string_list = input("Please give me a list of people you know: ")
    # split the string into a list
    names_list = string_list.split(",")
    # convert to ensure spaces do not cause trouble
    names_list_no_spaces = []
    for name in names_list:
        names_list_no_spaces.append(name.strip())
    # return that list
    return names_list_no_spaces


def ask_user():
    # ask user for a name
    input_name = input("Please give me a name: ")
    # see if the name is in the list of people they know
    if input_name in who_do_you_know():
        print("Hey you know " + input_name + "!")


def main():
    """ Get list of names from user, and then ask user if a name is in the list."""
    ask_user()


if __name__ == "__main__":
    sys.exit(main())
