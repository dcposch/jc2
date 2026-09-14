#!/usr/bin/env python3
"""Own gate controls: exact low-row k-saturation, receiver degree <= 3 only.
Independent of the charged check.py: different variable order, truncated products,
ordered named gates; the runner records the FIRST failing gate per mutation."""
import ast, hashlib, json, resource, subprocess, sys
from fractions import Fraction as F
from pathlib import Path
HERE = Path(__file__).resolve().parent
NAMES = ['g','p','k','a','x','y','e','b21','b12','b03','s','t','al','be','ga','c5','c6']
N = len(NAMES); Z = (0,)*N
class Fail(Exception): pass
def gate(ok, name):
    if not ok: raise Fail(name)
def V(n):
    e = [0]*N; e[NAMES.index(n)] = 1; return {tuple(e): F(1)}
def C(c): return {Z: F(c)} if c else {}
def add(*ps):
    o = {}
    for q in ps:
        for m, c in q.items(): o[m] = o.get(m, 0) + c
    return {m: c for m, c in o.items() if c}
def neg(p): return {m: -c for m, c in p.items()}
def sc(p, c): return {m: c*v for m, v in p.items()} if c else {}
def mul(p, q, cap=None):
    o = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(i+j for i, j in zip(m1, m2))
            if cap is not None and m[0]+m[1] > cap: continue
            o[m] = o.get(m, 0) + c1*c2
    return {m: c for m, c in o.items() if c}
def pw(p, n, cap=None):
    o = C(1)
    for _ in range(n): o = mul(o, p, cap)
    return o
def D(p, n):
    i = NAMES.index(n); o = {}
    for m, c in p.items():
        if m[i]:
            mm = list(m); mm[i] -= 1; o[tuple(mm)] = c*m[i]
    return o
def br(A, B):  # A_g B_p - A_p B_g
    return add(mul(D(A,'g'), D(B,'p')), neg(mul(D(A,'p'), D(B,'g'))))
def gp_coeff(P, i, j):  # coefficient of g^i p^j, as polynomial in the other names
    o = {}
    for m, c in P.items():
        if m[0] == i and m[1] == j:
            mm = (0, 0) + m[2:]; o[mm] = o.get(mm, 0) + c
    return {m: c for m, c in o.items() if c}
def deg_part(P, d): return {m: c for m, c in P.items() if m[0]+m[1] == d}
def ev(P, vals):
    tot = F(0)
    for m, c in P.items():
        t = c
        for i, ex in enumerate(m):
            if ex: t *= vals[NAMES[i]]**ex
        tot += t
    return tot
def subst(P, name, Q):  # substitute polynomial Q for variable name
    i = NAMES.index(name); o = {}
    for m, c in P.items():
        mm = list(m); ex = mm[i]; mm[i] = 0
        term = mul({tuple(mm): c}, pw(Q, ex))
        o = add(o, term)
    return o
def wire(P): return [[list(m), str(c)] for m, c in sorted(P.items())]

def run(mode):
    src = Path(__file__).read_text()
    gate(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(src))), 'assert-free')
    g,p,k,a,x,y,e,b21,b12,b03,s,t,al,be,ga,c5,c6 = [V(n) for n in NAMES]
    d = sc(pw(k,2), F(5,9))
    A1 = mul(a,p); A3 = add(mul(k,mul(pw(g,2),p)), mul(x,mul(g,pw(p,2))), mul(y,pw(p,3)))
    B1 = add(mul(d,g), mul(e,p)); B3 = add(mul(b21,mul(pw(g,2),p)), mul(b12,mul(g,pw(p,2))), mul(b03,pw(p,3)))
    B3u = {} if mode == '--mutate-omit-A1B3' else B3
    J = br(add(A1,A3), add(B1,B3u))
    r0 = gp_coeff(J,0,0); rgp = gp_coeff(J,1,1); rp2 = gp_coeff(J,0,2); rg2 = gp_coeff(J,2,0)
    # G1 constant row
    gate(r0 == neg(mul(d,a)), 'r0-row')
    # G2 the [A1,B3] terms are literally present before a=0
    gate(rgp.get(tuple(mul(a,b21))[0]) == -2 and rp2.get(tuple(mul(a,b12))[0]) == -1, 'A1B3-terms')
    # G3 exact rows
    E_gp = add(sc(mul(k,e),2), sc(mul(d,x),-2), sc(mul(a,b21),-2))
    E_p2 = add(mul(x,e), sc(mul(d,y),-3), neg(mul(a,b12)))
    gate(rgp == E_gp and rp2 == E_p2, 'rows-exact')
    # G4 target: g^2 row cancels exactly; degree-0/2 parts are exactly r0, rg2, rgp, rp2; odd degrees vacuous
    gate(add(rg2, sc(pw(k,3),F(5,9))) == {} and deg_part(J,1) == {} and deg_part(J,3) == {}, 'g2-target')
    gate(len(deg_part(J,0)) == len(r0) and len(deg_part(J,2)) == len(rg2)+len(rgp)+len(rp2), 'low-parts-complete')
    # G5 higher odd parts (generic degree-5 terms) cannot enter total degrees 0/2
    A5 = mul(c5, mul(pw(g,2),pw(p,3))); B5 = mul(c6, mul(g,pw(p,4)))
    J5 = br(add(A1,A3,A5), add(B1,B3u,B5))
    gate(deg_part(J5,0) == deg_part(J,0) and deg_part(J5,2) == deg_part(J,2) and deg_part(J5,4) != deg_part(J,4), 'higher-parts-inert')
    # G6-G8 membership certificates (polynomial identities, no localization)
    h1 = add(sc(e,9), sc(mul(k,x),-5)); h2 = add(pw(x,2), sc(mul(k,y),-3))
    gate(mul(pw(k,2),a) == sc(r0,F(-9,5)), 'cert-k2-a')
    gate(mul(pw(k,3),h1) == add(sc(mul(pw(k,2),rgp),F(9,2)), sc(mul(b21,r0),F(-81,5))), 'cert-k3-h1')
    last = sc(mul(add(mul(x,b21), neg(mul(k,b12))), r0), F(81,25))
    if mode == '--mutate-wrong-sign': last = neg(last)
    cert2 = add(sc(mul(pw(k,3),rp2),F(9,5)), sc(mul(mul(x,pw(k,2)),rgp),F(-9,10)), last)
    gate(mul(pw(k,4),h2) == cert2, 'cert-k4-h2')
    # G9 reverse inclusion I_low subset G, polynomial identities
    gate(r0 == sc(mul(pw(k,2),a),F(-5,9)), 'reverse-r0')
    gate(rgp == add(sc(mul(k,h1),F(2,9)), sc(mul(a,b21),-2)), 'reverse-gp')
    gate(rp2 == add(sc(mul(x,h1),F(1,9)), sc(mul(k,h2),F(5,9)), neg(mul(a,b12))), 'reverse-p2')
    # G10 unguarded low-row countercontrol: k=0, a=x=1, rest 0
    U = {n: F(0) for n in NAMES}; U['a'] = F(1); U['x'] = F(1)
    gate(all(ev(r,U) == 0 for r in (r0,rgp,rp2)), 'unguarded-point-kills-Ilow')
    gate(ev(a,U) == 1 and ev(h2,U) == 1 and ev(h1,U) == 0, 'unguarded-point-misses-G')
    if mode == '--mutate-false-unguarded-equivalence':
        gate(all(ev(q,U) == 0 for q in (a,h1,h2)), 'false-unguarded-equivalence')
    # G11 even-ramified literal low-row solution k=s^2, x=s, y=1/3, e=5s^3/9, a=b21=b12=0 (b03 free)
    R = {'k': pw(s,2), 'x': s, 'y': C(F(1,3)), 'e': sc(pw(s,3),F(5,9)), 'a': {}, 'b21': {}, 'b12': {}}
    def spec(P):
        for n, Q in R.items(): P = subst(P, n, Q)
        return P
    gate(all(spec(r) == {} for r in (r0,rgp,rp2,a,h1,h2)), 'ramified-example')
    # G12 classified centre, truncated to receiver degree <= 3 (never R^3/R^5)
    Rt = add(pw(p,5), mul(pw(g,3),pw(p,2)), mul(add(t,C(3)), mul(g,pw(p,2))), mul(t,pw(p,3)), neg(mul(add(t,C(3)),p)))
    A0 = add(pw(Rt,3,cap=3), mul(al,Rt,cap=3)); B0 = add(pw(Rt,5,cap=1), mul(be,pw(Rt,3,cap=1),cap=1), mul(ga,Rt,cap=1))
    tp3 = add(t,C(3))
    gate(gp_coeff(A0,0,1) == neg(mul(al,tp3)) and gp_coeff(A0,1,2) == mul(al,tp3), 'centre-a01-a12')
    gate(gp_coeff(A0,0,3) == add(neg(pw(tp3,3)), mul(al,t)), 'centre-a03')
    gate(gp_coeff(B0,0,1) == neg(mul(ga,tp3)) and gp_coeff(B0,1,0) == {} and gp_coeff(A0,0,0) == {} and gp_coeff(B0,0,0) == {}, 'centre-e-d')
    a03 = gp_coeff(A0,0,3)
    gate(subst(a03,'al',{}) == neg(pw(tp3,3)) and subst(a03,'t',C(-3)) == sc(al,-3), 'exception-locus')
    return {'status':'PASS','names':NAMES,'rows':{'r0':wire(r0),'r_gp':wire(rgp),'r_p2':wire(rp2),'r_g2':wire(rg2)},
            'G':{'a':wire(a),'h1':wire(h1),'h2':wire(h2)},'centre':{'a01':wire(gp_coeff(A0,0,1)),'a12':wire(gp_coeff(A0,1,2)),
            'a03':wire(a03),'e':wire(gp_coeff(B0,0,1))},'membership_powers':[2,3,4],'assert_nodes':0,'receiver_degree_cap':3,
            'scope':'low rows only; unguarded point is a low-row countercontrol, not a full-source point'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode == '--record':
        expect = {'':None,'--mutate-wrong-sign':'cert-k4-h2','--mutate-omit-A1B3':'A1B3-terms',
                  '--mutate-false-unguarded-equivalence':'false-unguarded-equivalence'}
        recs = []
        for opt in (False, True):
            for m, want in expect.items():
                cmd = [sys.executable] + (['-O'] if opt else []) + [str(Path(__file__).resolve())] + ([m] if m else [])
                r = subprocess.run(cmd, capture_output=True, timeout=30, preexec_fn=caps)
                first = r.stderr.decode().strip().splitlines()[-1] if r.stderr else ''
                if want is None:
                    gate(r.returncode == 0, 'positive-run-'+str(opt))
                    (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(r.stdout)
                else:
                    gate(r.returncode == 1 and first == 'FAIL '+want, 'mutation-first-failure:'+m+':'+first)
                recs.append({'optimized':opt,'mutation':m or None,'returncode':r.returncode,'first_failure':first or None,
                             'stdout_sha256':hashlib.sha256(r.stdout).hexdigest()})
        gate((HERE/'witness.json').read_bytes() == (HERE/'witness-O.json').read_bytes(), 'witness-bytes-identical')
        out = {'status':'PASS','runs':recs,'caps':'30 s wall, 25 s CPU, 512 MiB','witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest(),
               'self_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        (HERE/'replay.json').write_text(json.dumps(out, indent=1, sort_keys=True)+'\n')
        print(json.dumps({'status':'PASS','runs':len(recs),'witness_sha256':out['witness_sha256'],'self_sha256':out['self_sha256']}))
    else:
        try:
            print(json.dumps(run(mode), indent=1, sort_keys=True))
        except Fail as ex:
            print('FAIL '+str(ex), file=sys.stderr); sys.exit(1)
