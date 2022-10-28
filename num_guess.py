from typing import Any
import constants


def main():
    # get number of students
    user_input = int(input("please enter a number : "))
    print("")

    # check if there are too many students
    if user_input == constants.CORRECT_NUMBER:
        print("You are correct!")

    else:
        print("you are wrong!")


if __name__ == "__main__":
    main()
