import random


def reverse_number(number=None, user_input_func=input):
    if number is None:
        number = random.randint(10, 15)
    reversed_number = str(number)[::-1]
    print("The computer has guessed a number from 10 to 15. Enter it backwards:")
    while True:
        user_print = user_input_func("Your answer: ")
        if user_print == reversed_number:
            print("You win")
            break
        else:
            print("Try again")


if __name__ == "__main__":

    reverse_number()
