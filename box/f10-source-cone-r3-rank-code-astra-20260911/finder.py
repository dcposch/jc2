"""UNEXECUTED one-place finder; imports scientific code only after authorization."""
from authority import authorize, TAG


class InvalidPlace(ValueError):
    pass


class NonIntegral(ValueError):
    pass


def solve(ctx):
    import wire
    from fractions import Fraction as Q

    def qadd(a, b):
        return [(a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
                for i in range(max(len(a), len(b)))]

    def qmul(a, b):
        out = [Q(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] += x * y
        return out

    tau = Q(3, 10)
    D = [(1 + tau) * (2 - 3 * tau), -12 * (1 - tau), Q(12)]
    K = [2 * (2 - 3 * tau) * (1 + tau) * (2 + tau) * (3 + tau),
         42 * (1 + tau) * (2 + tau) * (4 * tau - 3), 840 * (1 - tau * tau), Q(-840)]
    G = [tau * (1 + tau) * (2 + tau) * (3 + tau), -30 * tau * (1 + tau) * (2 + tau),
         180 * tau * (1 + tau), -120 * tau]
    septic = qadd(qadd([2 * x for x in qmul(K, K)],
                      [-140 * tau * x for x in qmul(qmul([1 + tau, Q(-6)], K), D)]),
                  [245 * x for x in qmul(G, qmul(D, D))])
    wire.require(len(septic) == 8 and septic[-1] == -245 * 120 * 144 * tau, 'literal septic construction')
    P = [x / septic[-1] for x in septic]
    doc = wire.load(ctx['meta']['baseline']['path'], 134217728,
                    ctx['meta']['baseline']['sha256'])
    rawP, slots, extras, constants = wire.baseline(doc)
    wire.require([Q(a, b) for a, b in rawP] == P, 'actual monic P7')
    del doc

    class Field:
        def __init__(self, place):
            try:
                self.p = wire.integer(place['p'], 2147483647)
                pp = place['phi']
                wire.require(isinstance(pp, list) and 2 <= len(pp) <= 8, 'place degree')
                self.phi = [wire.integer(s, self.p - 1) for s in pp]
            except wire.WireError as exc:
                raise InvalidPlace('place syntax/bound') from exc
            p = self.p
            if p < 2 or (p > 2 and p % 2 == 0):
                raise InvalidPlace('not prime')
            d = 3
            while d * d <= p:
                if p % d == 0:
                    raise InvalidPlace('not prime')
                d += 2
            if self.phi[-1] != 1:
                raise InvalidPlace('nonmonic factor')
            self.f = len(self.phi) - 1
            pbar = [self.rational(x) for x in rawP]
            if self.remainder(pbar, self.phi):
                raise InvalidPlace('factor does not divide literal P7')
            x = self.remainder([0, 1], self.phi)
            h = x
            for i in range(1, self.f + 1):
                h = self.ppow(h, p)
                if i <= self.f // 2 and len(self.gcd(self.plus(h, [-v for v in x]), self.phi)) != 1:
                    raise InvalidPlace('reducible factor')
            if h != x:
                raise InvalidPlace('Frobenius factor failure')
            self.zero = (0,) * self.f
            self.one = (1,) + (0,) * (self.f - 1)

        def clean(self, a):
            a = [x % self.p for x in a]
            while a and a[-1] == 0:
                a.pop()
            return a

        def plus(self, a, b):
            return self.clean([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                               for i in range(max(len(a), len(b)))])

        def remainder(self, a, b):
            a, b = self.clean(a), self.clean(b)
            if not b:
                raise InvalidPlace('zero polynomial divisor')
            inv = pow(b[-1], self.p - 2, self.p)
            while len(a) >= len(b):
                k, c = len(a) - len(b), a[-1] * inv % self.p
                for j in range(len(b)):
                    a[k + j] = (a[k + j] - c * b[j]) % self.p
                a = self.clean(a)
            return a

        def pmul(self, a, b):
            if not a or not b:
                return []
            out = [0] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    out[i + j] = (out[i + j] + x * y) % self.p
            return self.remainder(out, self.phi)

        def ppow(self, a, n):
            out = [1]
            while n:
                if n & 1:
                    out = self.pmul(out, a)
                a = self.pmul(a, a)
                n //= 2
            return self.clean(out)

        def gcd(self, a, b):
            while b:
                a, b = b, self.remainder(a, b)
            return self.clean([x * pow(a[-1], self.p - 2, self.p) for x in a])

        def rational(self, pair):
            n, d = pair
            if d % self.p == 0:
                raise NonIntegral('p-divisible dense denominator')
            return (n % self.p) * pow(d % self.p, self.p - 2, self.p) % self.p

        def element(self, vector):
            a = self.remainder([self.rational(v) for v in vector], self.phi)
            return tuple(a + [0] * (self.f - len(a)))

        def add(self, a, b):
            return tuple((x + y) % self.p for x, y in zip(a, b))

        def sub(self, a, b):
            return tuple((x - y) % self.p for x, y in zip(a, b))

        def mul(self, a, b):
            v = self.pmul(a, b)
            return tuple(v + [0] * (self.f - len(v)))

        def inv(self, a):
            if not any(a):
                raise ValueError('zero field pivot')
            b = self.ppow(a, self.p ** self.f - 2)
            b = tuple(b + [0] * (self.f - len(b)))
            if self.mul(a, b) != self.one:
                raise ValueError('field inverse product')
            return b

    ff = Field(ctx['meta']['place'])
    weights = [8, 9, 10] + list(range(19, 10, -1)) + list(range(22, 10, -1)) + [27]

    def project(poly, weight):
        result = {}
        for ex, vector in poly:
            wire.require(ex[0] + 2 * ex[1] + 3 * ex[2] + 4 * ex[3] == weight, 'full graph homogeneous support')
            result[ex] = ff.element(vector)
        return result

    projected = [project(poly, w) for poly, w in zip(slots, weights)]
    for name, w in (('Hq', 7), ('zeta', 7), ('ell', 23), ('g', 30), ('U', 4)):
        project(extras[name], w)
    for vector in constants.values():
        ff.element(vector)

    def monomials(w):
        result = []
        for i in range(w + 1):
            for j in range((w - i) // 2 + 1):
                for k in range((w - i - 2 * j) // 3 + 1):
                    rem = w - i - 2 * j - 3 * k
                    if rem % 4 == 0:
                        result.append((i, j, k, rem // 4))
        return result

    rows = monomials(30)
    catalogue = [(j, mon) for j in range(25) for mon in monomials(30 - weights[j])]
    wire.require(len(rows) == 297 and len(catalogue) == 1453, 'complete matrix dimensions')
    row_index = {ex: i for i, ex in enumerate(rows)}

    def column(cid):
        j, mon = catalogue[cid]
        out = [ff.zero] * 297
        for ex, value in projected[j].items():
            shifted = tuple(x + y for x, y in zip(ex, mon))
            wire.require(shifted in row_index, 'whole column support')
            out[row_index[shifted]] = value
        return out

    work = [[ff.zero] * 1453 for _ in range(297)]
    for cid in range(1453):
        for i, val in enumerate(column(cid)):
            work[i][cid] = val
    selected, rank = [], 0
    for j in range(1453):
        pivot = next((i for i in range(rank, 297) if any(work[i][j])), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = ff.inv(work[rank][j])
        for k in range(j, 1453):
            work[rank][k] = ff.mul(work[rank][k], inv)
        for i in range(rank + 1, 297):
            factor = work[i][j]
            if any(factor):
                for k in range(j, 1453):
                    work[i][k] = ff.sub(work[i][k], ff.mul(factor, work[rank][k]))
        selected.append(j)
        rank += 1
        if rank == 297:
            break
    if rank != 297:
        return None, rank
    del work
    cols = [column(cid) for cid in selected]
    mat = [[cols[j][i] for j in range(297)] for i in range(297)]
    invmat = [[ff.one if i == j else ff.zero for j in range(297)] for i in range(297)]
    for j in range(297):
        pivot = next((i for i in range(j, 297) if any(mat[i][j])), None)
        if pivot is None:
            raise ValueError('internal chosen-minor failure')
        mat[j], mat[pivot] = mat[pivot], mat[j]
        invmat[j], invmat[pivot] = invmat[pivot], invmat[j]
        inv = ff.inv(mat[j][j])
        mat[j] = [ff.mul(v, inv) for v in mat[j]]
        invmat[j] = [ff.mul(v, inv) for v in invmat[j]]
        for i in range(297):
            if i != j and any(mat[i][j]):
                factor = mat[i][j]
                mat[i] = [ff.sub(a, ff.mul(factor, b)) for a, b in zip(mat[i], mat[j])]
                invmat[i] = [ff.sub(a, ff.mul(factor, b)) for a, b in zip(invmat[i], invmat[j])]
    for i in range(297):
        for j in range(297):
            if mat[i][j] != (ff.one if i == j else ff.zero):
                raise ValueError('internal inverse reduction')
    meta = ctx['meta']
    certificate = {'format': 'r3-rank-inverse-v1', 'job_tag': TAG,
        'baseline_sha256': meta['baseline']['sha256'],
        'qualification_sha256': meta['baseline']['qualification_sha256'],
        'place': meta['place'], 'dimensions': ['297', '1453'],
        'finder_sha256': meta['files']['finder.py']['sha256'],
        'columns': [str(j) for j in selected],
        'inverse': [[[str(c) for c in value] for value in row] for row in invmat]}
    return certificate, rank


def main():
    ctx = authorize('find')
    import wire
    import sys
    try:
        certificate, rank = solve(ctx)
        if certificate is None:
            ctx['finish']('NONDECISION_RANK_DEFICIENT', 'UNFORMED', {'rank': str(rank)})
            print('NONDECISION_RANK_DEFICIENT')
            raise SystemExit(2)
        raw = wire.encode(certificate)
        if len(raw) > 16777216:
            raise OverflowError('certificate byte cap')
        sha = ctx['write_new'](ctx['meta']['artifact']['path'], raw, 16777216)
        ctx['finish']('RANK_CANDIDATE_UNCHECKED', sha, {'rows': '297', 'columns': '1453'})
        print('RANK_CANDIDATE_UNCHECKED')
    except InvalidPlace:
        print('NONDECISION: INVALID_PLACE',file=sys.stderr)
        raise SystemExit(2)
    except NonIntegral:
        print('NONDECISION: NONINTEGRAL_BASELINE',file=sys.stderr)
        raise SystemExit(2)
    except wire.WireError:
        print('NONDECISION: MALFORMED_INPUT',file=sys.stderr)
        raise SystemExit(2)
    except (MemoryError, OverflowError):
        print('NONDECISION: INTERNAL_CAP',file=sys.stderr)
        raise SystemExit(2)


if __name__ == '__main__':
    main()
