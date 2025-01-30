"""There is a Ferris wheel with an even number of cabins in an amusement park.
When cabin #A is at the bottom, then cabin #B is at the top (A < B, A and B are of the same parity).
How many cabins are there in the Ferris wheel?"""

import random

def quantity(a: int, b: int) -> int:
    if not b > a:
        raise ValueError('A should be more than B')
    return (b - a) * 2

if __name__ == "__main__":

    a1 = random.randint(1,10) * 2
    b1 = random.randint(11,20) * 2

    print(f'A = {a1}')
    print(f'B = {b1}')

    result = quantity(a1, b1)

    print('The number of cabins in a Ferris wheel is:', result)
