"""DISABLED/UNEXECUTED independent exact 17m certificate checker.
No solver, FLINT, frozen Ring, or precomputed matrix imported or trusted.
AUTHORITY UNIVARIATE FULL_RECEIPT ROOT_ACCEPTANCE CERTIFICATE OUTPUT
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from execution_gate import authorize

def verify(data, certificate):
    # This pure function may only be called inside a separately authorized
    # child (main below, or a future explicitly registered test harness).
    from fractions import Fraction
    from math import gcd
    def need(ok, why):
        if not ok:
            raise ValueError(why)
    def rational(wire, nonzero=False):
        need(type(wire) is list and len(wire) == 2, 'rational pair shape')
        a, b = wire
        need(type(a) is str and type(b) is str, 'canonical rational strings only')
        n, d = int(a), int(b)
        need(str(n) == a and str(d) == b and d > 0 and gcd(abs(n), d) == 1
             and (not nonzero or n != 0), 'canonical reduced rational')
        return Fraction(n, d)
    # Independent dense Q[v] arithmetic, not algebra.py's sparse grouping or
    # polynomial division helper. No division by a coefficient of B occurs.
    def qadd(a, b):
        return [(a[i] if i < len(a) else Fraction(0))
                + (b[i] if i < len(b) else Fraction(0)) for i in range(max(len(a), len(b)))]
    def qscale(a, c):
        return [c * x for x in a]
    def qmul(a, b):
        out = [Fraction(0)] * max(0, len(a) + len(b) - 1)
        for i in range(len(a)):
            for j in range(len(b)):
                out[i + j] += a[i] * b[j]
        return out
    L = list(map(Fraction, [25, -144, 192]))
    R = list(map(Fraction, [-195, 2016, -6720, 7168]))
    E = list(map(Fraction, [39, -360, 960, -512]))
    p = qadd(qadd(qscale(qmul(R, R), 24), qmul(list(map(Fraction, [280, -1344])), qmul(L, R))),
             qscale(qmul(E, qmul(L, L)), 49))
    need(len(p) == 8 and p[7] != 0, 'fixed degree-seven modulus definition')
    need(type(data['modulus']) is list and len(data['modulus']) == 8
         and [rational(x) for x in data['modulus']] == p, 'literal full modulus not a factor')
    monic = [c / p[7] for c in p]
    def bzero():
        return [Fraction(0) for _ in range(7)]
    def bone():
        return [Fraction(1)] + [Fraction(0) for _ in range(6)]
    def badd(a, b):
        return [a[i] + b[i] for i in range(7)]
    def bmul(a, b):
        out = qmul(a, b)
        for k in range(len(out) - 1, 6, -1):
            lead = out[k]
            for i in range(7):
                out[k - 7 + i] -= lead * monic[i]
            out[k] = Fraction(0)
        return (out + bzero())[:7]
    def bparse(wire):
        need(type(wire) is list, 'B coefficient wire list')
        out = bzero(); previous = -1
        for term in wire:
            need(type(term) is list and len(term) == 3, 'B coefficient triple')
            exponents, numerator, denominator = term
            need(type(exponents) is list and len(exponents) == 7
                 and all(type(e) is int for e in exponents)
                 and exponents[:6] == [0] * 6
                 and 0 <= exponents[6] < 7, 'entire B basis coefficient shape')
            k = exponents[6]
            need(k > previous, 'sorted unique B coefficient basis')
            previous = k
            out[k] = rational([numerator, denominator], nonzero=True)
        return out
    def tdense(wire, degree):
        need(type(wire) is list and len(wire) == degree + 1, 'all dense coefficient slots')
        return [bparse(c) for c in wire]
    def tmul(a, b):
        out = [bzero() for _ in range(len(a) + len(b) - 1)]
        for i in range(len(a)):
            for j in range(len(b)):
                out[i + j] = badd(out[i + j], bmul(a[i], b[j]))
        return out
    ids = ['E1/S1', 'E1/S2', 'E1/S3', 'E0/S1', 'E0/S2', 'E0/S3', 'E0/S4', 'P4', 'P11']
    bounds = [3, 3, 2, 4, 3, 3, 2, 2, 5]
    need(data['schema'] == 'F10-R1-NINE-UNIVARIATE/v1' and data['variable'] == 'T'
         and data['coefficient_ring'] == 'Q[v]/p(v), entire algebra', 'literal input schema')
    need(type(data['rows']) is list and len(data['rows']) == 9, 'all nine indexed source rows')
    fs = []
    for index in range(9):
        obj = data['rows'][index]
        need(obj['id'] == ids[index] and type(obj['degree_bound']) is int
             and obj['degree_bound'] == bounds[index], 'literal row order/degree envelope')
        fs.append(tdense(obj['coefficients'], bounds[index]))
    guard = data['guard']
    need(set(guard) == {'variable', 'equation', 'q', 'factors'}
         and guard['variable'] == 'xi' and guard['equation'] == 'xi*q(T)-1'
         and guard['factors'] == ['r', 'h0'], 'guard and both factors retained')
    q = tdense(guard['q'], 5)
    # Additional direct guard-product check independent of prior receipt.
    rp, h0 = tdense(data['r'], 1), tdense(data['h0'], 4)
    need(tmul(rp, h0) == q, 'literal q equals r times h0')
    target = [bone()]
    for _ in range(5):
        target = tmul(target, q)
    need(len(target) == 26, 'q-fifth-power full dense target')
    target += [bzero() for _ in range(5)]
    need(certificate['schema'] == 'F10-LINEAR-CERTIFICATE/v1'
         and type(certificate['rows']) is int and certificate['rows'] == 217
         and type(certificate['columns']) is int and certificate['columns'] == 1638,
         'certificate dimension/schema')
    need(certificate['row_order'] == 'T-degree k=0..30 then v-degree a=0..6'
         and certificate['column_order'] == 'input i=0..8 then multiplier j=0..25 then v-degree ell=0..6',
         'literal certificate basis ordering')
    branch = certificate['branch']
    need(branch in ('UNIT', 'SEPARATOR'), 'certificate branch')
    size = 1638 if branch == 'UNIT' else 217
    need(type(certificate['witness']) is list and len(certificate['witness']) == size,
         'complete rational witness dimension')
    witness = [rational(x) for x in certificate['witness']]
    if branch == 'UNIT':
        total = [bzero() for _ in range(31)]
        for i in range(9):
            # Reconstruct all nine multipliers, all 26 slots, all seven B
            # coefficients, independently of producer matrix construction.
            h = [witness[(i * 26 + j) * 7:(i * 26 + j + 1) * 7] for j in range(26)]
            product = tmul(h, fs[i])
            for k in range(len(product)):
                total[k] = badd(total[k], product[k])
        need(total == target, 'full 217-coordinate sum h_i f_i equals q^5')
        return {'status': 'VERIFIED-GENERIC-ZERO-QUOTIENT', 'branch': branch,
                'checked_coordinates': 217, 'multipliers': 9, 'multiplier_degree_bound': 25,
                'cofactor_contract': '1=xi^5*sum(h_i*f_i)-(xi*q-1)*sum((xi*q)^j,j=0..4)',
                'scope': 'exact 17m generic B[T,q^-1]/I; no source-point or JC2 claim'}
    # Every column is checked, even for zero/duplicate input rows and zero
    # intermediate coefficients. No matrix or solver rank is a verifier input.
    checked = 0
    for i in range(9):
        for j in range(26):
            for ell in range(7):
                basis = bzero(); basis[ell] = Fraction(1)
                value = Fraction(0)
                for k, coefficient in enumerate(fs[i]):
                    reduced = bmul(basis, coefficient)
                    for a in range(7):
                        value += witness[(j + k) * 7 + a] * reduced[a]
                need(value == 0, 'dual column annihilation i=%d j=%d ell=%d' % (i, j, ell))
                checked += 1
    need(checked == 1638, 'every dual column checked')
    value = sum((witness[k * 7 + a] * target[k][a] for k in range(31) for a in range(7)), Fraction(0))
    need(value == 1, 'dual target normalization equals one')
    return {'status': 'VERIFIED-GENERIC-NONZERO-QUOTIENT', 'branch': branch,
            'checked_columns': checked, 'target_coordinates': 217,
            'scope': 'exact 17m finite-etale generic quotient; separator is not a point or character'}

def main():
    if len(sys.argv) != 7:
        raise SystemExit('AUTHORITY UNIVARIATE FULL_RECEIPT ROOT_ACCEPTANCE CERTIFICATE OUTPUT')
    custody = authorize(sys.argv[1], __file__, 'check')
    from evidence import verified, bound, sha, require, write_exclusive
    data, binding, spec = verified(*sys.argv[1:5])
    certificate, certificate_sha = bound(spec, sys.argv[5])
    require(certificate.get('binding') == binding, 'certificate input/receipt/acceptance binding')
    require(certificate.get('solver_sha256') == spec['file_sha256'].get(str(Path(__file__).with_name('solver.py').resolve())),
            'candidate producer pin')
    # Solver rank, status and engine flags are NOT premises of either proof.
    result = verify(data, certificate)
    result.update({'execution': custody, 'binding': binding, 'certificate_sha256': certificate_sha,
                   'checker_sha256': sha(__file__)})
    write_exclusive(sys.argv[6], result)
    print(result['status'])

if __name__ == '__main__':
    main()
