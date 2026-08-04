"""Monte Carlo probe exploiting linearity of Q -> [P,Q].

For a normalized SystemA (bracket equations only, corners nonvanishing),
sample random P-coefficient vectors a mod p (corner a's nonzero), then the
system becomes linear in the b's: M(a) b = r(a).  Solve mod p; if consistent,
test whether the affine solution space contains b with all corner-b nonzero.

Any hit = explicit mod-p solution of the reduced case (verified by direct
bracket arithmetic) => the mod-p variety is NONEMPTY at this prime, so a GB
run can never return [1] there.  Zero hits over many samples = evidence the
mod-p variety projects nowhere dense / is empty.
"""
import random
from jc import bracket, padd, pneg

def classify(S):
    avars, bvars = [], []
    fixedP, fixedQ = [], []
    for (kind, pt), idx in S.varof.items():
        if kind == "P":
            avars.append(idx)
        elif kind == "Q":
            bvars.append(idx)
    return sorted(avars), sorted(bvars)

def probe(S, p, nsamples=200, seed=1):
    rng = random.Random(seed)
    avars, bvars = classify(S)
    aset, bset = set(avars), set(bvars)
    apos = {v: i for i, v in enumerate(avars)}
    bpos = {v: i for i, v in enumerate(bvars)}
    cornersA = [v for v in S.corner_vars if v in aset]
    cornersB = [v for v in S.corner_vars if v in bset]
    eqs = S.equations[:-1]           # drop t-saturation
    # precompile: eq -> (bilinear terms [(ai,bj,c)], linA [(ai,c)], linB [(bj,c)], const)
    comp = []
    for c in eqs:
        bil, linA, linB, const = [], [], [], 0
        for m, k in c.items():
            vs = list(m)
            ins_a = [v for v in vs if v in aset]
            ins_b = [v for v in vs if v in bset]
            if len(vs) == 0:
                const += k
            elif len(ins_a) == 1 and len(ins_b) == 1 and len(vs) == 2:
                bil.append((ins_a[0], ins_b[0], k))
            elif len(ins_a) == len(vs):
                assert len(vs) == 1, f"non-linear pure-a monomial {m}"
                linA.append((ins_a[0], k))
            elif len(ins_b) == len(vs):
                assert len(vs) == 1, f"non-linear pure-b monomial {m}"
                linB.append((ins_b[0], k))
            else:
                raise AssertionError(f"unexpected monomial {m}")
        comp.append((bil, linA, linB, const))

    def solve_mod(M, rhs):
        """Gauss over F_p. M: list of rows (lists), rhs list. Returns
        (None,None) if inconsistent, else (x0, nullbasis)."""
        n = len(M); mvars = len(M[0]) if n else 0
        A = [row[:] + [rhs[i]] for i, row in enumerate(M)]
        piv = []
        r = 0
        for col in range(mvars):
            sel = next((i for i in range(r, n) if A[i][col] % p), None)
            if sel is None:
                continue
            A[r], A[sel] = A[sel], A[r]
            inv = pow(A[r][col], p - 2, p)
            A[r] = [(x * inv) % p for x in A[r]]
            for i in range(n):
                if i != r and A[i][col]:
                    f = A[i][col]
                    A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
            piv.append(col)
            r += 1
            if r == n:
                break
        for i in range(r, n):
            if A[i][mvars] % p:
                return None, None
        x0 = [0] * mvars
        for i, col in enumerate(piv):
            x0[col] = A[i][mvars]
        free = [c for c in range(mvars) if c not in piv]
        null = []
        for fc in free:
            vec = [0] * mvars
            vec[fc] = 1
            for i, col in enumerate(piv):
                vec[col] = (-A[i][fc]) % p
            null.append(vec)
        return x0, null

    hits, consistent = 0, 0
    witness = None
    for _ in range(nsamples):
        a = {}
        for v in avars:
            a[v] = rng.randrange(1, p) if v in cornersA else rng.randrange(p)
        M = []
        rhs = []
        for bil, linA, linB, const in comp:
            row = [0] * len(bvars)
            for ai, bj, k in bil:
                row[bpos[bj]] = (row[bpos[bj]] + k * a[ai]) % p
            for bj, k in linB:
                row[bpos[bj]] = (row[bpos[bj]] + k) % p
            s = const + sum(k * a[ai] for ai, k in linA)
            M.append(row)
            rhs.append((-s) % p)
        x0, null = solve_mod(M, rhs)
        if x0 is None:
            continue
        consistent += 1
        for _try in range(20):
            b = x0[:]
            for vec in null:
                lam = rng.randrange(p)
                b = [(x + lam * y) % p for x, y in zip(b, vec)]
            if all(b[bpos[cb]] % p for cb in cornersB):
                hits += 1
                witness = (dict(a), {v: b[bpos[v]] for v in bvars})
                break
        if witness:
            break
    return dict(nsamples=nsamples, consistent=consistent, hits=hits,
                witness=witness, cornersA=cornersA, cornersB=cornersB)

def verify_witness(S, p, witness):
    """Substitute the witness into ALL equations (including saturation surrogate)."""
    a, b = witness
    vals = {}
    for (kind, pt), idx in S.varof.items():
        if kind == "P":
            vals[S.varnames[idx]] = a[idx]
        elif kind == "Q":
            vals[S.varnames[idx]] = b[idx]
    vals["t"] = 1  # unused: check bracket equations only
    res = S.substitute(vals)
    return all(v % p == 0 for v in res[:-1])
