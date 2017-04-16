import sys


def who_do_you_know():
    # ask the user for a list of people they know
    string_list = input("Please give me a list of people you know: ")
    # split the string into a list
    names_list = string_list.split(",")
    # return that list
    return names_list


def ask_user(known_ppl):
    # ask user for a name
    input_name = input("Please give me a name: ")
    # see if the name is in the list of people they know
    for name in known_ppl:
        if name == input_name:
            print("Hey you know " + name + "!")


def main():
    """ Get list of names from user, and then ask user if a name is in the list."""
    known_ppl = who_do_you_know()
    ask_user(known_ppl)


if __name__ == "__main__":
    sys.exit(main())
