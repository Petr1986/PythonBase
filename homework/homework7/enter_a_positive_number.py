def positive_number(input_func, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        print("Enter a positive number ", end="")
        num = int(input_func(""))
        if num <= 0:
            attempts += 1
            print(f"Invalid input! Attempts left: {max_attempts - attempts}")
        else:
            print(f"You entered a positive number {num}")
            return num
    print("Too many invalid attempts. Exiting.")
    return None


if __name__ == "__main__":

    positive_number(input)
