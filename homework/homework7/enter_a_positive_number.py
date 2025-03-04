import random


def positive_number():
    while True:
        num = random.randint(-5, 5)
        if num <= 0:
            print("Enter a positive number")
            continue
        else:
            print(f"You entered a positive number {num}")
            break


if __name__ == "__main__":

    positive_number()
