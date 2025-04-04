def handler_input_option(lower_limit, upper_limit):
    while True:
        try:
            user_response = int(input("\t    >_: "))
            if lower_limit <= user_response <= upper_limit:
                return user_response
            else:
                print("\t    Only numbers are accepted in the list of menu options")
        except ValueError:
            print("\t    Enter only numbers")


def handler_response_user(min_letters):
    while True:
        try:
            user_response = input("\t    >_: ")
            if user_response is not None and len(user_response) >= min_letters:
                return user_response
            else:
                print(f"\t    Enter valid name, valid data or valid description please")
        except ValueError as e:
            print(e)


def handler_number_response_user():
    while True:
        try:
            user_response = int(input("\t    >_: "))
            if user_response > 0:
                return user_response
            else:
                print("\t    Only numbers greater than zero")
        except ValueError:
            print("\t    Enter only numbers")


def handler_price_value():
    while True:
        try:
            user_response = float(input("\t    >_: "))
            if user_response > 0:
                return user_response
            else:
                print("\t    Only numbers greater than zero")
        except ValueError:
            print("\t    Enter only numbers")


def handler_yorn_response_user():
    while True:
        user_response = input("\t    >_: ")
        if user_response == "yes" or user_response == "y" or user_response == "Yes":
            return True
        elif user_response == "no" or user_response == "n" or user_response == "No":
            return False
        else:
            print('\n\t    Please enter: y(Yes) or n(No)')


def handler_continue_response_user():
    while True:
        user_response = input("\t    >_: ")
        if (user_response == "continue" or user_response == "c" or user_response == "yes"
                or user_response == "Yes" or user_response == "C" or user_response == "y"):
            return True
        elif user_response == "no" or user_response == "n" or user_response == "back":
            return False
        else:
            print('\n\t    Please enter: c(Continue) or n(No)')
