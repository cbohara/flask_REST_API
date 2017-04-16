import sys


def who_do_you_know():
    # ask the user for a list of people they know
    names = input("Please give me a list of people you know: ")
    # normalized to ensure spaces do not cause trouble
    return [name.strip() for name in names.split(",")]


def ask_user():
    # ask user for a name
    input_name = (input("Please give me a name: ")).strip()
    # see if the name is in the list of people they know
    if input_name in who_do_you_know():
        print("Hey you know " + input_name.title() + "!")


def main():
    """Ask user for a name and then check if that name is in a list of names."""
    ask_user()


if __name__ == "__main__":
    sys.exit(main())
