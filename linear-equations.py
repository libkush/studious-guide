import sys
import time


class Solve:
    def __init__(self, a1, b1, c1, a2, b2, c2):
        def x(A1, B1, C1, A2, B2, C2):
            if A1 / A2 == B1 / B2 != C1 / C2:
                raise ValueError("Inconsistent pair of equations.")
            elif A1 / A2 == B1 / B2 == C1 / C2:
                raise ValueError("Infinite solutions.")
            return ((B1 * C2) - (B2 * C1)) / ((B2 * A1) - (B1 * A2))

        def y(A1, B1, C1, A2, B2, C2):
            if A1 / A2 == B1 / B2 != C1 / C2:
                raise ValueError("Inconsistent pair of equations.")
            elif A1 / A2 == B1 / B2 == C1 / C2:
                raise ValueError("Infinite solutions.")
            return ((C1 * A2) - (C2 * A1)) / ((B2 * A1) - (B1 * A2))

        formula = f"x = (b₁c₂ − b₂c₁)/(b₂ɑ₁ − b₁ɑ₂)\ny = (c₁ɑ₂ - c₂ɑ₁)/(b₂ɑ₁ − b₁ɑ₂)"
        self.x = x(a1, b1, c1, a2, b2, c2)
        self.y = y(a1, b1, c1, a2, b2, c2)
        self.solved = f"For equations {a1}x {numFormat(b1)}y {numFormat(c1)} = 0 and " + \
                      f"{a2}x {numFormat(b2)}y {numFormat(c2)} = 0:\n\n" + \
                      f"Using the cross multiplication method:\n" + \
                      f"{formula}\n\n" + \
                      f"⇒ x = [({b1})({c2}) - ({b2})({c1})]/[({b2})({a1}) - ({b1})({a2})]\n" + \
                      f"∴ x = ({b1 * c2} - {b2 * c1})/({b2 * a1} - {b1 * a2})\n" + \
                      f"∴ x = {(b1 * c2) - (b2 * c1)}/{(b2 * a1) - (b1 * a2)}\n" + \
                      f"∴ x = {self.x}\n\n" + \
                      f"⇒ y = [({c1})({a2}) - ({c2})({a1})]/[({b2})({a1}) - ({b1})({a2})]\n" + \
                      f"∴ y = ({c1 * a2} - {c2 * a1})/({b2 * a1} - {b1 * a2})\n" + \
                      f"∴ y = {(c1 * a2) - (c2 * a1)}/{(b2 * a1) - (b1 * a2)}\n\n" + \
                      f"x = {self.x} and y = {self.y}\n"


def slowPrint(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)


def numFormat(num):
    if num >= 0:
        return '+' + str(num)
    else:
        return str(num)


slowPrint(
    "The standard form for any linear equation in two variables is ɑ₁x + b₁y + c₁ = 0, where ɑ₁, b₁ and c₁ are "
    "constants (coefficients). Please enter ɑ₁, b₁ and c₁ for the first equation:\n")


def main():
    a1 = float(input("ɑ₁ = "))
    b1 = float(input("b₁ = "))
    c1 = float(input("c₁ = "))

    a2 = float(input("Second equation: \na₂ = "))
    b2 = float(input("ɑ₂ = "))
    c2 = float(input("c₂ = "))

    answer = Solve(a1, b1, c1, a2, b2, c2)

    print(answer.solved)

    print(
        f"For equations {a1}x {numFormat(b1)}y {numFormat(c1)} = 0 and {a2}x {numFormat(b2)}y {numFormat(c2)} = 0:" + \
        f"\nx = {answer.x}\ny = {answer.y}")
    return input("Enter 'q' to exit or enter to continue . . .\n")


q = main()
while q != 'q':
    q = main()
