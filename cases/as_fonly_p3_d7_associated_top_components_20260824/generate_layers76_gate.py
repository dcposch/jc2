#!/usr/bin/env python3
"""Emit the exact F3 gate for layers 7/6 and carry rows 12/11."""
from __future__ import annotations
import os


def term(c, left, right=None):
    c %= 3
    if not c:
        return None
    monomial = left if right is None else f"{left}*{right}"
    return monomial if c == 1 else f"2*{monomial}"


def expression(terms):
    kept = [value for value in terms if value]
    return "+".join(kept) if kept else "0"


TOP = int(os.environ.get("TOP", "7"))
LOW = int(os.environ.get("LOW", str(TOP-1)))
assert 1 <= LOW <= TOP <= 7
DO_PRIMARY = os.environ.get("DO_PRIMARY", "0") == "1"
degrees = tuple(range(TOP, LOW-1, -1))
variables = []
ux, uy, vx, vy = {}, {}, {}, {}
divergence = []
for degree in degrees:
    for prefix in ("u", "v"):
        variables.extend(f"{prefix}{degree}_{i}" for i in range(degree+1))
    for i in range(degree+1):
        j = degree-i
        un, vn = f"u{degree}_{i}", f"v{degree}_{i}"
        if i % 3:
            ux.setdefault((i-1, j), []).append((i, un))
            vx.setdefault((i-1, j), []).append((i, vn))
        if j % 3:
            uy.setdefault((i, j-1), []).append((j, un))
            vy.setdefault((i, j-1), []).append((j, vn))
    for i in range(degree):
        divergence.append(expression([
            term(i+1, f"u{degree}_{i+1}"),
            term(degree-i, f"v{degree}_{i}"),
        ]))


def product(left, right, sign):
    out = {}
    for (i, j), lt in left.items():
        for (k, ell), rt in right.items():
            for lc, lv in lt:
                for rc, rv in rt:
                    out.setdefault((i+k, j+ell), []).append(
                        (sign*lc*rc, lv, rv))
    return out


det = product(ux, vy, 1)
for monomial, terms in product(uy, vx, -1).items():
    det.setdefault(monomial, []).extend(terms)

equations = [value for value in divergence if value != "0"]
for total in range(2*TOP-2, TOP+LOW-3, -1):
    for i in range(total+1):
        value = expression([term(c, left, right)
                            for c, left, right in det.get((i, total-i), [])])
        if value != "0":
            equations.append(value)

print('ring r=3,(' + ','.join(variables) + '),dp;')
print('LIB "primdec.lib"; option(redSB);')
print('ideal I=' + ','.join(equations) + ';')
print('ideal G=std(I);')
print('print("variables/equations/Gsize/dim");')
print(f'print({len(variables)}); print({len(equations)}); print(size(G)); print(dim(G));')
print('list L=minAssGTZ(I);')
print('print("minAss_count"); print(size(L));')
print('ideal origin=' + ','.join(variables) + '; ideal incidence;')
print('for (int k=1; k<=size(L); k++) {')
print('  ideal C=std(L[k]); print("component/dim/size");')
print('  print(k); print(dim(C)); print(size(C));')
print('  print(C);')
print('  incidence=reduce(C,std(origin));')
print('  print("origin_on_minimal_component");')
print('  if (size(incidence)==0) { print(1); } else { print(0); }')
print('}')
print('ideal R=std(radical(I)); ideal IR=reduce(R,G);')
print('print("original_is_radical");')
print('if (size(IR)==0) { print(1); } else { print(0); }')
if DO_PRIMARY:
    print('list PD=primdecGTZ(I); print("primary_count"); print(size(PD));')
    print('ideal qideal; ideal pideal;')
    print('for (int q=1; q<=size(PD); q++) {')
    print(' qideal=std(PD[q][1]); pideal=std(PD[q][2]);')
    print(' print("primary dims/sizes"); print(q); print(dim(qideal));')
    print(' print(size(qideal)); print(dim(pideal)); print(size(pideal));')
    print(' if (q==size(PD)) { print("last_associated_prime"); print(pideal); }')
    print(' incidence=reduce(pideal,std(origin));')
    print(' print("origin_on_associated_prime");')
    print(' if (size(incidence)==0) { print(1); } else { print(0); }')
    print('}')
print('print("PASS-LAYERS76");')
