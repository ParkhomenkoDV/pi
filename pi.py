import decimal

decimal.getcontext().prec = 100


def Leibniz():
    k = 1
    s = 0
    for i in range(1_000_000):
        if i % 2 == 0:
            s += 4 / k
        else:
            s -= 4 / k
        k += 2

    return s


def nilakantha(reps):
    result = decimal.Decimal(3.0)
    op = 1
    for n in range(2, 2 * reps + 1, 2):
        result += 4 / decimal.Decimal(n * (n + 1) * (n + 2) * op)
        op *= -1
    return result


if __name__ == '__main__':
    print(Leibniz())
    print(nilakantha(10_000_000))
