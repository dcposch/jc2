"""Scan pairs (f,g), deg g = deg_y g = n, deg_x g = n' < n, computing BOTH p.150
characteristic data: y-side (Moh's own) and x-side (= the child's, see report Sec.3).

For each pair we record the descent labels that Prop 6.3(2) predicts:
    n' = deg_x g,  m' = deg_x f,  u_s = n' d_s / n,
    M'_i = M_i u_s/d_s  for i <= s-1   (banked closed form / Moh p.207, 5/5)
and then read the child's EXTRA characteristic pair M'_{s'+1} = M~_s.
"""
import sys, json, random, collections
sys.path.insert(0, '/home/ubuntu/jc2/box/child-top-us2-20260905')
from modchar import chardata
from fractions import Fraction as F
from math import comb, gcd

PRIMES = [(1 << 61) - 1, 2147483647, 1000000007]
B0 = [1234567, 98765431, 555555557]
CFG = [(PRIMES[i], B0[i] % PRIMES[i]) for i in range(3)]


def eff(cd):
    """p.174 Definition-Remark: drop M_h if M_h = n-1."""
    n = cd['n']; M = [v for v in cd['M'] if v is not None]
    if cd['truncated']:
        return None
    dropped = M and M[-1] == n - 1
    if dropped:
        M = M[:-1]
    return len(M), M, bool(dropped), (cd['M'][-1] is None)


def stable(f, g, side):
    outs = [chardata(f, g, side, b0, p) for p, b0 in CFG]
    keys = {(tuple(o['M']), tuple(o['d']), o['n'], o['m'], o['truncated']) for o in outs}
    if len(keys) != 1:
        return None
    return outs[0]


def analyse(f, g, label):
    cy = stable(f, g, True); cx = stable(f, g, False)
    if cy is None or cx is None:
        return None
    ey, ex = eff(cy), eff(cx)
    if ey is None or ex is None:
        return None
    s, Ms, dropped, closed_inf_y = ey
    if s < 1 or closed_inf_y:
        return None                       # parent must be birational: chain ends at 1
    n, nt = cy['n'], cx['n']
    ds = cy['d']
    if s > len(ds) - 1 or nt < 2 or nt >= n:
        return None
    d_s = ds[s - 1]
    if (nt * d_s) % n:
        return None
    us = nt * d_s // n
    if us < 1:
        return None
    Mx_raw = cx['M']
    Mx = [v for v in Mx_raw if v is not None]
    child_closed_at_inf = (Mx_raw[-1] is None)
    pred = [F(Mi * us, d_s) for Mi in Ms[:s - 1]]
    low_ok = len(Mx) >= s - 1 and all(p.denominator == 1 and int(p) == o
                                      for p, o in zip(pred, Mx[:s - 1]))
    dx = cx['d']
    dxs = dx[s - 1] if len(dx) >= s else None
    extra = Mx[s - 1:]
    return dict(label=label, n=n, m=cy['m'], M=cy['M'], d=ds, s=s, d_s=d_s,
                Ms=Ms[-1], delta_s_is_m1=(Ms[-1] == n - 2), dropped=dropped,
                nt=nt, mt=cx['m'], Mx=Mx_raw, dx=dx, u_s=us, low_ok=low_ok,
                dxs_eq_us=(dxs == us), extra=extra, nt1=nt - 1,
                child_closed_at_inf=child_closed_at_inf,
                case=('a-infinity' if child_closed_at_inf and len(extra) == 0 else
                      ('b-nt-minus-1' if extra and extra[0] == nt - 1 else
                       ('c-below' if extra else 'none'))))


def mk(terms):
    d = {}
    for (i, j, c) in terms:
        d[(i, j)] = d.get((i, j), 0) + c
    return {k: v for k, v in d.items() if v}


LEAD = {}
for n_ in range(4, 15):
    for U_ in range(1, n_):
        V_ = n_ - U_
        LEAD[(V_, U_)] = [(i, n_ - i, comb(U_, i) * (-1) ** i) for i in range(U_ + 1)]

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 11)
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12
res, seen = [], set()
for n in range(4, NMAX + 1):
    for U in range(2, n):
        for trial in range(200):
            terms = list(LEAD[(n - U, U)])
            for _ in range(random.randint(1, 5)):
                tot = random.randint(1, n - 1)
                i = random.randint(0, min(U, tot)); j = tot - i
                terms.append((i, j, random.choice([-3, -2, -1, 1, 2, 3])))
            g = mk(terms)
            m = random.randint(1, n - 1); mt = random.randint(1, max(1, U))
            ft = [(0, m, 1)]
            for _ in range(random.randint(1, 5)):
                ft.append((random.randint(0, mt), random.randint(0, m),
                           random.choice([-3, -2, -1, 1, 2, 3])))
            ft.append((mt, random.randint(0, max(0, m - 1)), random.choice([1, 2, -1])))
            f = mk(ft)
            key = (tuple(sorted(g.items())), tuple(sorted(f.items())))
            if key in seen:
                continue
            seen.add(key)
            try:
                r = analyse(f, g, f'n{n}U{U}t{trial}')
            except Exception:
                continue
            if r:
                r['g'] = {f'{i},{j}': c for (i, j), c in g.items()}
                r['f'] = {f'{i},{j}': c for (i, j), c in f.items()}
                res.append(r)

json.dump(res, open('/home/ubuntu/jc2/box/child-top-us2-20260905/scan2.json', 'w'), indent=0)
print('pairs analysed:', len(res))
good = [r for r in res if r['low_ok'] and r['u_s'] >= 2 and r['dxs_eq_us']]
print('u_s>=2 AND banked low-level law holds AND d\'_{s\'+1}=u_s :', len(good))
print('  case split:', collections.Counter(r['case'] for r in good))
gd = [r for r in good if r['delta_s_is_m1']]
print('  of those with delta_s=-1 (M_s = n-2, Prop 5.1):', len(gd),
      collections.Counter(r['case'] for r in gd))
for r in (gd or good)[:20]:
    print(f"   n={r['n']} m={r['m']} M={r['M']} d={r['d']} s={r['s']} d_s={r['d_s']} "
          f"Ms=n-2:{r['delta_s_is_m1']} || n'={r['nt']} m'={r['mt']} u_s={r['u_s']} "
          f"M'={r['Mx']} d'={r['dx']} extra={r['extra']} n'-1={r['nt1']} case={r['case']}")
