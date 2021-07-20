import sys,time
import keyboard

class Solve:
    def __init__(self, a1, b1, c1, a2, b2, c2):
        def x(a1, b1, c1, a2, b2, c2):
            if a1/a2 == b1/b2 != c1/c2:
                raise ValueError("Inconsistent pair of equations.")
            elif a1/a2 == b1/b2 == c1/c2:
                raise ValueError("Infine solutions.")
            return ((b1 * c2) - (b2 * c1))/((b2 * a1) - (b1 * a2)) 
        def y(a1, b1, c1, a2, b2, c2):
            if a1/a2 == b1/b2 != c1/c2:
                raise ValueError("Inconsistent pair of equations.")
            elif a1/a2 == b1/b2 == c1/c2:
                raise ValueError("Infine solutions.")
            return ((c1 * a2) - (c2 * a1))/((b2 * a1) - (b1 * a2))

        formula = f"x = (b₁c₂ − b₂c₁)/(b₂ɑ₁ − b₁ɑ₂)\ny = (c₁ɑ₂ - c₂ɑ₁)/(b₂ɑ₁ − b₁ɑ₂)"
        self.x = x(a1, b1, c1, a2, b2, c2)
        self.y = y(a1, b1, c1, a2, b2, c2)
        self.solved = f"For equations {a1}x {format(b1)}y {format(c1)} = 0 and {a2}x {format(b2)}y {format(c2)} = 0:\n" + \
            f"Using the cross multiplication method:\n" + \
            f"{formula}\n" + \
            f"x = [({b1})({c2}) - ({b2})({c1})]/[({b2})({a1}) - ({b1})({a2})]\n" + \
            f"∴ x = ({b1*c2} - {b2*c1})/({b2*a1} - {b1*a2})\n" + \
            f"∴ x = {(b1*c2) - (b2*c1)}/{(b2*a1) - (b1*a2)}\n" + \
            f"∴ x = {self.x}\n\n" + \
            f"y = [({c1})({a2}) - ({c2})({a1})]/[({b2})({a1}) - ({b1})({a2})]\n" + \
            f"x = {self.x}\ny = {self.y}"


def slowprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

def format(num):
    if num >= 0:
        return '+'+ str(num)
    else: 
        return str(num)

slowprint("The standard form for any linear equation in two variables is ɑ₁x + b₁y + c₁ = 0, where ɑ₁, b₁ and c₁ are constants (coefficients). Please enter ɑ₁, b₁ and c₁ for the first equation:\n")

def main():
    a1 = float(input("ɑ₁ = "))
    b1 = float(input("b₁ = "))
    c1 = float(input("c₁ = "))

    a2 = float(input("Second equation: \na₂ = "))
    b2 = float(input("ɑ₂ = "))
    c2 = float(input("c₂ = "))
    
    print(f"For equations {a1}x {format(b1)}y {format(c1)} = 0 and {a2}x {format(b2)}y {format(c2)} = 0:\nx = {x(a1, b1, c1, a2, b2, c2)}\ny = {y(a1, b1, c1, a2, b2, c2)}")

    input("Press any key to continue and 0 to exit . . .")

    if keyboard.read_key() == '0':
        exit()
    main()

main()
