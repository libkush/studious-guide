import sys
import time
import keyboard


def format(num, suppressOne=True, plus=False):
    if num == 1.0 and suppressOne == True and plus == False:
        return ''
    elif num == 1.0 and suppressOne == True and plus == True:
        return '+'
    elif num == -1.0 and suppressOne == True:
        return '-'
    elif num >= 0.0 and plus == True:
        return '+' + str(int(num))
    else:
        return str(num)


def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)


class Solve:
    def __init__(self, a, b, c):
        # get the discriminator
        D = (b*b) - (4*a*c)

        def isReal(num):
            if num < 0:
                return '∴ D < 0\n∴ The equation has no real roots.'
            elif num == 0:
                return '∴ D = 0\n∴ The equation has identical real roots.'
            elif num > 0:
                return '∴ D > 0\n∴ The equation has distinct real roots.'

        # find the roots x1 and x2 using the quadratic formula
        def root1(a, b, c):
            return (-1*b + D**0.5)/(2 * a)

        def root2(a, b, c):
            return (-1*b - D**0.5)/(2 * a)

        x1 = root1(a, b, c)
        x2 = root2(a, b, c)

        # store the readable formula in a string
        formula = "x = [-b ± √(b² - 4ɑc)]/2ɑ"

        # create string with values of x
        self.values = str(x1) + ', ' + str(x2)

        # checking for real roots
        self.real = f"\n\nChecking if the equation has real roots:\n" + \
            f"Discriminator (D) = b² - 4ɑc\n" + \
            f"∴ D = {b}² - 4({a})({c})\n" + \
            f"∴ D = {format(b*b)} {format(-4*a*c, plus=True, suppressOne=False)}\n" + \
            f"∴ D = {D}\n" + \
            f"{isReal(D)}"

        # create a string containing readable representation of the solution
        self.solved = f"\n\nFor equation {format(a)}x² {format(b, plus=True)}x {format(c, plus=True, suppressOne=False)} = 0:\n\n" + \
            f"Using the quadratic formula,\n" + \
            f"{formula}\n" + \
            f"∴ x = [-({b}) ± √({b}² - 4 x {a} x {c})]/2({a})\n" + \
            f"∴ x = ({-1*b} ± √{(b*b) - (4*a*c)})/{2*a}\n" + \
            f"∴ x = ({-1*b} + {((b*b) - (4*a*c))**0.5})/{2*a}, ({-1*b} - {((b*b) - (4*a*c))**0.5})/{2*a}\n" + \
            f"∴ x = {self.values}\n\n" + \
            f"Using factorization method,\n" + \
            f"{format(a)}x² {format(b, plus=True)}x {format(c, plus=True)} = 0\n" + \
            f"∴ (x {format(-1*x1, suppressOne=False)})(x {format(-1*x2, suppressOne=False)}) = 0\n" + \
            f"∴ x {format(-1*x1, suppressOne=False)} = 0 or x {format(-1*x2, suppressOne=False)} = 0\n" + \
            f"∴ x = {self.values}\n\n"


slowprint("A quadratic equation is of the form ɑx² + bx + c = 0 where ɑ, b and c are constants (coefficients).\nEnter the values of a, b and c:\n")


def main():
    a = float(input("ɑ = "))
    b = float(input("b = "))
    c = float(input("c = "))

    answer = Solve(a, b, c)
    print(answer.real, answer.solved)

    input("Press any key to continue and 0 to exit . . .")

    if keyboard.read_key() == '0':
        exit()
    main()


main()
