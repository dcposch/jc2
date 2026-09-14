"""Tiny D125 terminal-face filtration check; never imports the classifier."""
from fractions import Fraction
from collections import defaultdict
import resource

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))

def require(value, message):
    if not value:
        raise RuntimeError(message)

def ceil_div(a, b):
    return -((-a) // b)

def columns(removed):
    groups = defaultdict(list)
    for ell in range(-125, 26):
        lo = max(0, ceil_div(ell, 5))
        hi = (125 + ell) // 6
        n = hi - lo + 1
        first = max(0, ceil_div(5 * ell - 5, 12))
        require(0 <= first < n <= 21, 'band bound')
        for b in range(first + int(ell in removed), n):
            a = ell + b
            groups[5*a - 17*b].append((a, b))
    return groups

def matrix(cols):
    entries = []
    rows = set()
    for a, b in cols:
        terms = {}
        for pos, c in [((a+3, b), 4*b-a),
                       ((a+20, b+5), 21*b-6*a)]:
            if c:
                terms[pos] = c
                rows.add(pos)
        entries.append(terms)
    rows = sorted(rows)
    return [[Fraction(col.get(row, 0)) for col in entries] for row in rows]

def rank(mat, width):
    a = [row[:] for row in mat]
    r = 0
    for j in range(width):
        p = next((i for i in range(r, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][j]
        a[r] = [x/pivot for x in a[r]]
        for i in range(r+1, len(a)):
            c = a[i][j]
            if c:
                a[i] = [x-c*y for x,y in zip(a[i], a[r])]
        r += 1
    return r

def profile(removed):
    groups = columns(removed)
    count = total_rank = max_rows = max_cols = 0
    defects = []
    for w, cols in sorted(groups.items()):
        mat = matrix(cols)
        r = rank(mat, len(cols))
        count += len(cols)
        total_rank += r
        max_rows = max(max_rows, len(mat))
        max_cols = max(max_cols, len(cols))
        if r != len(cols):
            defects.append((w, len(cols)-r))
    return count, total_rank, max_rows, max_cols, defects, len(groups)

original_pins = {1, 13, 25}
both = profile(original_pins | {0, 15})
require(both[0] == both[1] == 1760, 'full gauged column rank')
require(both[2] <= 6 and both[3] <= 5, 'tiny block size')
require(not both[4], 'unexpected gauged defect')
restore_constant = profile(original_pins | {15})
require(restore_constant[0] == 1761 and restore_constant[1] == 1760,
        'restored constant nullity')
require(restore_constant[4] == [(0, 1)], 'constant weight')
restore_p = profile(original_pins | {0})
require(restore_p[0] == 1761 and restore_p[1] == 1760, 'restored P nullity')
require(restore_p[4] == [(3, 1)], 'P weight')
restore_both = profile(original_pins)
require(restore_both[0] == 1762 and restore_both[1] == 1760,
        'ungauged nullity two')
require(restore_both[4] == [(0, 1), (3, 1)], 'ungauged defect weights')

# Direct sparse monomial formula, independent of the block indexing above.
def bracket(p, q):
    out = defaultdict(Fraction)
    for (a,b), c in p.items():
        for (i,j), d in q.items():
            out[(a+i-1,b+j-1)] += c*d*(a*j-b*i)
    return {pos:c for pos,c in out.items() if c}

pface = {(4,1):Fraction(1), (21,6):Fraction(1)}
qface = {(1,0):Fraction(-1), (18,5):Fraction(-3),
         (35,10):Fraction(-9,5)}
require(bracket(pface, qface) == {(4,0):Fraction(1)}, 'pinned top bracket')
for cols in columns(original_pins | {0,15}).values():
    for a,b in cols:
        expected = {}
        for pos,c in [((a+3,b),4*b-a), ((a+20,b+5),21*b-6*a)]:
            if c:
                expected[pos] = Fraction(c)
        require(bracket(pface,{(a,b):Fraction(1)}) == expected,
                'independent column derivative')
mutant = dict(qface)
mutant[(18,5)] = Fraction(3)
require(bracket(pface,mutant) != {(4,0):Fraction(1)}, 'sign mutation rejected')
print('D125_DIAGONAL_BLOCKS_PASS', both)
print('RESTORED_GAUGE_CONTROLS_PASS', restore_constant[4], restore_p[4], restore_both[4])
print('TOP_BRACKET_AND_SIGN_MUTATION_PASS')
