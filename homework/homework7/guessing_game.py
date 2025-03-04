import random


def guessing_game():
    answer = "y"
    while answer == "y":
        number = random.randint(1, 10)
        while True:
            num = int(input("Enter your answer: "))
            if num == number:
                print("You win")
                answer = input("Let's play again? y/n: ")
                break
            elif num > number:
                print("The number guessed is less")
            else:
                print("The number guessed is higher")


if __name__ == "__main__":

    print(guessing_game())
