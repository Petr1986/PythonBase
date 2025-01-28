"""The last digit of the three-digit number x was subtracted.
When the result was divided by 10,
and the last digit of the number x was added to the quotient on the left,
the result was 237. Find the number x
Based on the fact that the last digit of the number x was added to the quotient
on the left and 237 was obtained, it follows that the last digit of the number
is 2. Consequently, we can replace adding the digit 2
by adding 200. Based on this, we can form the equation
237 = (x-2)/10 + 200"""

import random

def find_number(y) -> int:
    return int(str(y)[1:] + str(y)[0])

if __name__ == "__main__":

    a = random.randint(10, 10000)

    result = find_number(a)
    print(f'If the result of the expression is equal to: {a}')
    print(f'Meaning х: {result}')
