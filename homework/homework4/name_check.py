import random


def name_check(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be string")
    if name:
        return f"Добро пожаловать, {name}"
    else:
        return "Пожалуйста авторизуйтесь"


if __name__ == "__main__":

    names = ["Kirill", "Petr", "Dariya", ""]

    name1 = random.choice(names)

    print(name_check(name1))
