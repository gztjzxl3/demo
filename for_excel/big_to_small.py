# These are only for decimal to smaller base
def f(x, small_base):
    quotient, remainder = x // small_base, x % small_base
    return quotient, remainder


def transform(x, small_base):
    rd_li = []
    qt, rd = f(x, small_base)
    rd_li.append(str(rd))
    while qt != 0:
        qt, rd = f(qt, small_base)
        rd_li.append(str(rd))
    res = ''.join(rd_li[::-1])
    return res


if __name__ == '__main__':
    small_base = 2
    res = transform(8, 2)
    print(res)
