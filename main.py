import math


def sign(x: float) -> int:
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def main() -> None:
    print('Másodfokú egyenlet gyökei')
    print('Kérem az együtthatókat!')
    a: float = float(input('a = '))
    b: float = float(input('b = '))
    c: float = float(input('c = '))
    x1: float
    x2: float
    x: float

    if a != 0:
        if math.sqrt(b) >= 4 * a * c:
            if math.sqrt(b) == 4 * a * c:
                x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
                print(f'x1 = {x1}')
                print(f'x2 = {x2}')
            else:
                x = -(b / 2 * a)
                print(f'x = {x}')
        else:
            print('Nincs valós gyök')
    else:
        if b != 0:
            x = -(c / b)
            print(f'x = {x}')
        else:
            if c != 0:
                print('Az egyenbletben ellentmondás lép fel')
            else:
                print('Az egyenletben azonosság lép fel')


if __name__ == "__main__":
    main()
