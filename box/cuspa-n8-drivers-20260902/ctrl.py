import sys, itertools; sys.path.insert(0,'/tmp/cuspa')
from ledger import *
from fractions import Fraction

def psi_consistency(r):
    """Is there a functional psi on Z^j with psi(ab[k]) = phi_gen[k], and psi(meridian)=1?"""
    import sympy as sp
    j=r['rs_j']
    A=sp.Matrix([r['ab'][k] for k in range(len(r['ab']))])
    b=sp.Matrix([[x] for x in r['phi_gen']])
    sol=A.solve_least_squares(b) if False else None
    # exact solve: psi is j-dim
    aug=A.row_join(b)
    if A.rank()!=aug.rank(): return None
    x=sp.symbols('x0:%d'%j)
    eqs=[sum(A[i,c]*x[c] for c in range(j))-b[i,0] for i in range(A.rows)]
    s=sp.solve(eqs,x,dict=True)
    if not s: return None
    psi=[s[0].get(x[c],x[c]) for c in range(j)]
    vals=set()
    for v in r['dist']:
        vals.add(sp.simplify(sum(sp.Integer(v[c])*psi[c] for c in range(j))))
    return vals

# --- CONTROL A: does MERIDIAN-COUNT ever pass?  search small N, all (p,q)
def search(N, plist):
    hits=[]; tot=0
    reps=list(itertools.permutations(range(N)))
    for (p,q) in plist:
        for A in reps:
            if ppow(A,p)!=ppow(A,p): pass
            for B in reps:
                if ppow(A,p)!=ppow(B,q): continue
                if not is_transitive([A,B],N): continue
                tot+=1
                try: r=full_record(A,B,p,q)
                except Exception: continue
                if r['tors']: continue
                if r['ndist']==r['j'] and abs(r['basis_det'] or 0)==1:
                    hits.append((p,q,A,B,r['j'],r['a'],r['kappa'],r['ndist']))
    return tot,hits

if __name__=='__main__':
    import pickle
    S=pickle.load(open('/tmp/cuspa/surv.pkl','rb'))
    print("== CONTROL: G^ab functional psi, and psi(meridian class) (must be {1})")
    for key in [(2,3),(3,4),(4,3)]:
        r0=S[key][0]; r=full_record(r0['A'],r0['B'],r0['p'],r0['q'])
        print("   cell",key," psi(meridian classes) =", psi_consistency(r))
    print()
    for N in (2,3,4):
        pl=[(p,q) for p in range(2,7) for q in range(2,7) if __import__('math').gcd(p,q)==1]
        tot,hits=search(N,pl)
        print("== CONTROL: N=%d  transitive relation pairs %d ; MERIDIAN-BASIS passes: %d"
              % (N,tot,len(hits)))
        for h in hits[:6]: print("     PASS", h)
