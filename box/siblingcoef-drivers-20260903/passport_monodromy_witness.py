#!/usr/bin/env python3
"""Exact permutation witnesses for the two cyclic bottom Padé systems.

Composition is left action: ``compose(a,b)[i] = a[b[i]]``.  Thus the
printed triples satisfy sigma0 * sigmainf * sigma1 = 1.  The checks use only
integer permutations; the Belyi/Padé interpretation is recorded in the
final printed block.
"""


def inverse(p):
    q = [None] * len(p)
    for i, image in enumerate(p):
        q[image] = i
    assert None not in q
    return q


def compose(a, b):
    return [a[b[i]] for i in range(len(a))]


def cycles(p):
    seen, answer = set(), []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle, point = [], start
        while point not in seen:
            seen.add(point)
            cycle.append(point)
            point = p[point]
        answer.append(tuple(cycle))
    return answer


def long_cycle(degree, length):
    p = list(range(degree))
    for i in range(length):
        p[i] = (i + 1) % length
    return p


def verify(label, sigma0, long_length, expected0, expected_inf):
    degree = len(sigma0)
    sigma1 = long_cycle(degree, long_length)
    sigmainf = compose(inverse(sigma0), inverse(sigma1))
    identity = list(range(degree))
    assert compose(sigma0, compose(sigmainf, sigma1)) == identity

    orbit, todo = {0}, [0]
    while todo:
        point = todo.pop()
        for permutation in (sigma0, sigmainf, sigma1):
            image = permutation[point]
            if image not in orbit:
                orbit.add(image)
                todo.append(image)
    assert len(orbit) == degree

    type0 = sorted(map(len, cycles(sigma0)), reverse=True)
    typeinf = sorted(map(len, cycles(sigmainf)), reverse=True)
    type1 = sorted(map(len, cycles(sigma1)), reverse=True)
    assert type0 == sorted(expected0, reverse=True)
    assert typeinf == sorted(expected_inf, reverse=True)
    assert type1 == sorted([long_length] + [1] * (degree-long_length),
                           reverse=True)
    ramification = sum(length - 1 for datum in (type0, typeinf, type1)
                        for length in datum)
    assert ramification == 2 * degree - 2

    print(label)
    print(" degree =", degree, "transitive orbit =", len(orbit))
    print(" sigma0 cycles =", cycles(sigma0))
    print(" sigmainf cycles =", cycles(sigmainf))
    print(" sigma1 cycles =", cycles(sigma1))
    print(" types =", type0, typeinf, type1)
    print(" product identity = PASS; Riemann--Hurwitz genus zero = PASS")


D108_SIGMA0 = [
    14, 2, 18, 0, 13, 6, 19, 4, 12, 8, 11, 20, 9, 7, 3, 16, 17,
    15, 1, 5, 10,
]

D90_SIGMA0 = [
    37, 13, 34, 30, 8, 29, 35, 4, 24, 22, 31, 39, 9, 2, 16, 33,
    15, 0, 38, 23, 17, 14, 3, 27, 36, 20, 5, 18, 1, 6, 12, 11, 10,
    21, 28, 26, 7, 25, 19, 32,
]


if __name__ == "__main__":
    verify("D108", D108_SIGMA0, 17, [3] * 7, [2] * 10 + [1])
    verify("D90", D90_SIGMA0, 21, [5] * 8, [3] * 13 + [1])
    print()
    print("CORRESPONDENCE")
    print(" sigma0 is monodromy over 0: P has respectively 7 triple or")
    print(" 8 quintuple zero fibres.  sigmainf is over infinity: z=0 is")
    print(" the unique simple pole and G/H supplies the double/triple poles.")
    print(" sigma1 is over 1: its long 17/21-cycle is placed at z=infinity.")
    print(" Hence beta=F^3/(zG^2) or P^5/(zH^3), and in w=1/z")
    print(" ord_0(Fbar^3-Gbar^2)=17 or ord_0(Pbar^5-Hbar^3)=21.")
