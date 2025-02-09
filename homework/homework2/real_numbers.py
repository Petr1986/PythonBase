from math import trunc, ceil, floor


if __name__ == "__main__":


    A, B, C, D, F, G = 5.49, 4.49, 5.51, 4.51, -4.4, -5.5

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"D = {D}")
    print(f"F = {F}")
    print(f"G = {G}")

    print(f"{'':<7} {'int':<5} {'round':<6} {'trunc':<6} {'ceil':<6} {'floor':<6}")

    numbers = [A, B, C, D, F, G]

    for x in numbers:
        if x < 0:
            print(f"{x:<7} {int(x):<5} {round(x):<6} {trunc(x):<6} {ceil(x):<6} {floor(x):<6}")
        else:
            print(f"{x:<8} {int(x):<5} {round(x):<6} {trunc(x):<6} {ceil(x):<6} {floor(x):<6}")
