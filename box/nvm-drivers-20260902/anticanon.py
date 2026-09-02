"""Search the boundary-cluster model for  sum a_i - 3D  > 0   (i.e. Z.K_X > 0)."""
import itertools, sys
sys.path.insert(0,'/tmp/nvm')
from forest import gen_forests, evaluate

def scan(r, cmax, need_dic=True):
    best = (-10**9, None)
    keys = ['L']+list(range(r))
    for par in gen_forests(r):
        for vals in itertools.product(range(cmax+1), repeat=r+1):
            c = dict(zip(keys, vals))
            ev = evaluate(par, c)
            if ev is None: continue
            a, D, m, N = ev
            if N <= 0: continue
            if sum(m[k]*c[k] for k in keys) != N: continue   # consistency
            if need_dic and not any(m[k] == 0 and c[k] > 0 for k in keys): continue
            v = sum(a) - 3*D
            if v > best[0]: best = (v, (par, dict(c), a, D, N, dict(m)))
    return best

if __name__ == "__main__":
    for r in range(1, 7):
        v, dat = scan(r, 3)
        print("r=%d  max(sum a - 3D) = %d   %s" % (r, v, dat[0:2] if dat else None))
        if dat: print("        a=%s D=%d N=%d" % (dat[2], dat[3], dat[4]))
