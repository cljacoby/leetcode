import itertools

def factorial(i: int):
    assert(i > 0)
    if i == 1:
        return 1
    else:
        return i * factorial(i -1)

def ncr(n, r):
    """
    Number of combinations of `n` items arragned in groups of `r`.

    C(n,r) = n! / ( r!(n - r)! )
    
    """
    assert(n >= r >= 0)
    f = factorial
    return int(f(n) / (f(r) * f(n - r)))


def combos(n, r, start=0, pre=[]):
    if len(pre) == r:
        return [tuple(pre)]
    out = []
    for i in range(start, len(n)):
        npre = pre.copy()
        npre.append(n[i])
        out.extend(combos(n, r, i+1, npre))
    return out

if __name__ == "__main__":
    iterable = [i for i in 'abcde']
    result = combos(iterable, 3)
    control = list(itertools.combinations(iterable, 3))
    # print(f"result = {result}")
    # print(f"control = {control}")
    assert(result == control)


