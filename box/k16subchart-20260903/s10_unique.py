#!/usr/bin/env python3
"""S10: Lemma UNIQUE-POWER and its non-uniform exceptions.

Residual variables of the chain sub-chart S_r' = {b4=q_(2,0)=..=q_(t-r-1,0)=0}
are q_(t-r,0),...,q_(t-1,0),b3 with weights t-r,...,t-1,t+1.  The claim is that
q_(t-r,0)^m is the ONLY monomial of weight m(t-r) as an identity in t, and the
finitely many t where a second monomial appears are listed.
"""
def uniform(rv, mv):
    out = []
    def rec(i, e, E, M):
        if i > rv:
            f = mv - E
            if f >= 0 and -M + f == -mv*rv:
                out.append((tuple(e), f))
            return
        for k in range(0, mv+1-E):
            rec(i+1, e+[k], E+k, M+i*k)
    rec(1, [], 0, 0)
    return out


def count_at(rv, mv, tv):
    ws = [tv-i for i in range(1, rv+1)] + [tv+1]
    tgt = mv*(tv-rv)
    n = 0
    def rec(i, rem):
        nonlocal n
        if i == len(ws):
            n += (rem == 0); return
        k = 0
        while k*ws[i] <= rem:
            rec(i+1, rem-k*ws[i]); k += 1
    rec(0, tgt)
    return n


for mv in (3, 4):
    print("--- m=%d" % mv)
    for rv in range(1, 7):
        u = uniform(rv, mv)
        bad = [tv for tv in range(rv+2, 80) if count_at(rv, mv, tv) > 1]
        print("  r=%d uniform monomials=%s ; t with a 2nd monomial: %s"
              % (rv, u, bad))
