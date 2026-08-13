import sys, os
sys.path.insert(0, '/Users/dc/code/math/jc72108/cases')
os.chdir('/Users/dc/code/math/jc72108/cases')
from fractions import Fraction as Fr
from math import gcd
import book_offaxis as B
import book_enum as BE

# GATE 1: on-axis record unchanged
okc, _ = BE.gate()
assert okc
print("GATE on-axis: PASS")

# GATE 2: review's patched state -- remove the refuted M-law (b % gcd(dp,dq))
# from w_closure_off, rerun stage R at td=7 only. (Review BOOK-OFFAXIS-REVIEW
# section 3a mechanical confirmation.)
def w_closure_noML(w0, b):
    W, frontier = {w0}, {w0}
    while frontier:
        nxt = set()
        for w in frontier:
            a, d = w.numerator, w.denominator
            for Delta in range(3, a + 1):
                if a % Delta: continue
                for nu in range(2, Delta):
                    if (Delta - 1) % nu: continue
                    n = (Delta - 1) // nu + 1
                    if n < 2 or (n * nu + 1) % d: continue
                    w2 = Fr(w * n, Delta)
                    if w2 not in W: nxt.add(w2)
            for l in B.divisors(b):
                if l < 2: continue
                cap = l * a * b
                for nu in range(2, cap - l + 1):
                    for c in range(1, (cap - l) // nu + 1):
                        for k in range(1, c + 1):
                            for lex in range(0, (c - k) // l + 1):
                                Sm = l * k + l * lex - c
                                if not (k <= Sm <= k * (l - 1)): continue
                                dq = (1 + k + lex) * nu + 1
                                dp = nu * (l + Sm)
                                E = l * dq - dp
                                if -(-Sm // k) * dq >= dp: continue
                                # M-law REMOVED (refuted R1.4 / G1)
                                kb = Fr(l * w * dq, E)
                                if kb.denominator != 1 or kb < 1: continue
                                w2 = Fr(w * l * (dq - 1), nu * E)
                                if w2 not in W: nxt.add(w2)
        W |= nxt; frontier = nxt
    return W

W2 = w_closure_noML(Fr(3, 2), 2)
print("W_off(3/2,2) patched:", sorted(W2))

# td=7 entry: (2,3) Lambda=(3,4), poles (1,1,2)+(1,2,3), M=(1,2)
cen = B.census(tdmax=7)
d = cen[(2, 7)]
assert len(d['l6']) == 1
al, be, poles = d['l6'][0]
bs = [b for (L, a, b, nu) in poles]
pdata = []
for (L, a, b, nu) in poles:
    w0 = BE.w0_of(al, be, a, b, nu)
    W = sorted(w_closure_noML(w0, b)) if b >= 2 else sorted(B.w_closure_off(w0, b))
    pdata.append({'W': W, 'nu': nu})
print("entry:", B.fmt_entry(al, be, poles), "bs:", bs,
      "W:", [[str(w) for w in p['W']] for p in pdata])

counts = {'DEAD': 0, 'ALIVE': 0, 'OPEN': 0}
alive_cells = []
for tree in set(B.hierarchies(tuple(range(len(bs))))):
    if tree[0] != 'G': continue
    for MG, struct in B.expand2(tree, bs):
        for inter in (True, False):
            if inter and MG == 1: continue
            v = B.cell_verdict(struct, inter, pdata)
            counts[v] += 1
            if v != 'DEAD':
                alive_cells.append((MG, struct, inter, v))
print("td7 patched recount:", counts)
for MG, struct, inter, v in alive_cells:
    print("  LIVE cell:", "MG=", MG, "struct=", struct, "interior=", inter, v)
