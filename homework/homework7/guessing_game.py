import random


def guessing_game(number):
    answer = "y"
    while answer == "y":
        while True:
            print("Enter your answer: ", end="")  # Выводим перед каждым запросом ввода
            num = int(input())
            if num == number:
                print("You win")
                print(
                    "Let's play again? y/n: ", end=""
                )  # Выводим запрос на повторную игру
                answer = input()
                break
            elif num > number:
                print("The number guessed is less")
            else:
                print("The number guessed is higher")


if __name__ == "__main__":

    number1 = random.randint(1, 10)

    print(guessing_game(number1))
