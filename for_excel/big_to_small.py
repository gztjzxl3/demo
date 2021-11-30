# These are only for decimal to other bases' system

def f(x, base):
    quotient, remainder = x // base, x % base
    return quotient, remainder


def transform(x, base):
    rd_li = []
    qt, rd = f(x, base)
    rd_li.append(str(rd))
    while qt != 0:
        qt, rd = f(qt, base)
        rd_li.append(str(rd))
    res = ''.join(rd_li[::-1])
    return res


if __name__ == '__main__':
    base = 2
    res = transform(8, 2)
    print(res)
