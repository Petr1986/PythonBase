"""Given positive integers A and B (A > B).
On a segment of length A, the maximum possible number of segments
of length B are placed (without overlapping).
Using the division operation, find the number of segments
B placed on segment A and find the length of the unoccupied part of the segment."""

def calculation(a: int, b: int) -> tuple[int, int]:
    result_quantity = a // b
    result_remainder = a % b
    return result_quantity, result_remainder

if __name__ == "__main__":

    a1, b1 = map(int, input('Введите длину А и В через пробел: ').split())

    remainder, quantity = calculation(a1, b1)

    print(f'В отрезке длинной {a1}, помещается {quantity} отрезков длинны {b1}')
    print('Остаток:', remainder)