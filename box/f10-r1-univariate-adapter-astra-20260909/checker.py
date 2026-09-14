"""DISABLED/UNEXECUTED independent nine-row substitution verifier.
No adapter import or generation path. Shares the exact frozen B arithmetic.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from execution_gate import authorize

def verify(normalized,data):
    from algebra import Ring,Q,ZERO,require
    from math import comb,gcd
    from input_evidence import COVER
    ring=Ring(); one=ring.c(1)
    def nofloat(item):
        require(type(item) is not float,'floating point forbidden')
        if isinstance(item,(dict,list)):
            for val in (item.values() if isinstance(item,dict) else item): nofloat(val)
    nofloat(normalized); nofloat(data)
    # Independent exact wire parser; never accepts integer/float coefficients.
    def parse(wire,kind):
        require(type(wire) is list,'wire list'); out={}; previous=None
        for term in wire:
            require(type(term) is list and len(term)==3,'wire triple')
            exp,num,den=term
            require(type(exp) is list and len(exp)==7 and all(type(e) is int and e>=0 for e in exp),'exponent shape/sign')
            require(exp[6]<7 and exp[3]==0,'fixed B basis, no s coordinate')
            if kind=='B': require(not any(exp[:6]),'coefficient must lie in B')
            elif kind=='parameter': require(not any(exp[3:6]),'parameter-only normalized polynomial')
            key=tuple(exp); require(previous is None or previous<key,'canonical wire ordering'); previous=key
            require(type(num) is str and type(den) is str,'rational strings only')
            n,d=int(num),int(den)
            require(str(n)==num and str(d)==den and n and d>0 and gcd(abs(n),d)==1,'canonical rational')
            out[key]=Q(n,d)
        return out
    require(data['schema']=='F10-R1-NINE-UNIVARIATE/v1' and data['variable']=='T' and data['coefficient_ring']=='Q[v]/p(v), entire algebra','univariate schema/full ring')
    require(normalized['schema']=='F10-R1-NORMALIZED-FOUR-BAND/v1' and normalized['axes']==['x','y','z','s','S','t','v'],'normalized input schema')
    exactmod=[[str(c.numerator),str(c.denominator)] for c in ring.p]
    require(data['modulus']==normalized['modulus']==exactmod,'literal complete modulus, not a factor')
    # Check all named leading witnesses, without asking the product ring to
    # divide by anything. Parent provenance remains separately required.
    units={k:parse(w,'B') for k,w in normalized['units'].items()}
    require(set(units)=={'L','Linv','w','winv','f5','f5inv','a','ainv'},'normalized unit inventory')
    v=ring.atom(6); L=ring.add(ring.c(25),ring.scale(v,-144),ring.scale(ring.pow(v,2),192))
    R=ring.add(ring.c(-195),ring.scale(v,2016),ring.scale(ring.pow(v,2),-6720),ring.scale(ring.pow(v,3),7168))
    ring.eq(units['L'],L,'L definition')
    ring.eq(ring.scale(ring.mul(L,units['w']),112),R,'w definition')
    f5=ring.add(ring.c(Q(-63,8192)),ring.scale(v,Q(35,512)),ring.scale(ring.pow(v,2),Q(-21,128)),ring.scale(units['w'],Q(-21,128)),ring.scale(ring.mul(v,units['w']),Q(21,16)))
    ring.eq(units['f5'],f5,'f5 definition')
    for a,b in (('L','Linv'),('w','winv'),('f5','f5inv'),('a','ainv')): ring.eq(ring.mul(units[a],units[b]),one,'named unit product '+a)
    F,H,a0,b0=[parse(w,'B') for w in normalized['leading']]
    for a,b in zip((F,H,a0,b0),(ring.mul(v,units['winv']),units['winv'],units['winv'],units['f5inv'])): ring.eq(a,b,'leading normalization')
    # Reassemble Phi3/Phi4 from the SEVEN supplied coefficients. Independence
    # here is uniqueness of polynomial coefficients, not the adapter extractor.
    require(set(data['coefficients'])==set('abcdefg'),'all seven compatibility coefficients')
    coeff={k:parse(w,'B') for k,w in data['coefficients'].items()}
    x,y,z=[ring.atom(i) for i in range(3)]
    p3=ring.add(ring.mul(coeff['a'],ring.pow(x,3)),ring.mul(coeff['b'],ring.mul(x,y)),ring.mul(coeff['c'],z))
    p4=ring.add(ring.mul(coeff['d'],ring.pow(x,4)),ring.mul(coeff['e'],ring.mul(ring.pow(x,2),y)),ring.mul(coeff['f'],ring.pow(y,2)),ring.mul(coeff['g'],ring.mul(x,z)))
    ring.eq(p3,parse(normalized['Phi3'],'parameter'),'all Phi3 coefficients')
    ring.eq(p4,parse(normalized['Phi4'],'parameter'),'all Phi4 coefficients')
    ci=parse(data['c_inverse'],'B'); ring.eq(ring.mul(ci,coeff['c']),one,'actual c inverse identity')
    def dense(wire,bound):
        require(type(wire) is list and len(wire)==bound+1,'every univariate coefficient slot including zeros')
        return [parse(w,'B') for w in wire]
    r=dense(data['r'],1)
    ring.eq(r[0],ring.scale(ring.mul(ci,coeff['a']),-1),'affine r constant')
    ring.eq(r[1],ring.scale(ring.mul(ci,coeff['b']),-1),'affine r linear; no b division')
    def add(a,b):
        return [ring.add(a[i] if i<len(a) else {},b[i] if i<len(b) else {}) for i in range(max(len(a),len(b)))]
    def times(a,b):
        out=[{} for _ in range(max(0,len(a)+len(b)-1))]
        for i,c in enumerate(a):
            for j,d in enumerate(b): out[i+j]=ring.add(out[i+j],ring.mul(c,d))
        return out
    def equal(a,b,why):
        for i in range(max(len(a),len(b))): ring.eq(a[i] if i<len(a) else {},b[i] if i<len(b) else {},why)
    def specialize(poly,bound):
        # Independently expand (r0+r1*T)^k by its binomial coefficients;
        # no call to adapter's sparse compose/power substitution loop.
        out=[{} for _ in range(bound+1)]
        for e,c in poly.items():
            j,k=e[1],e[2]
            for h in range(k+1):
                require(j+h<=bound,'homogeneous degree bound')
                term={ZERO[:6]+(e[6],):c*comb(k,h)}
                term=ring.mul(term,ring.mul(ring.pow(r[0],k-h),ring.pow(r[1],h)))
                out[j+h]=ring.add(out[j+h],term)
        return out
    G=[parse(w,'parameter') for w in normalized['G']]
    require(len(G)==9,'all original normalized G slots')
    ring.eq(G[7],p3,'Phi3 normalized index'); ring.eq(G[8],p4,'Phi4 normalized index')
    weights=[7,6,5,8,7,6,5,3,4]
    for poly,w in zip(G,weights): require(all(e[0]+2*e[1]+3*e[2]==w for e in poly),'all G weights')
    H0=parse(normalized['H0'],'parameter'); H1=parse(normalized['H1'],'parameter'); U=parse(normalized['maps']['4'][0],'parameter')
    for poly,w in ((H0,9),(H1,8),(U,2)): require(all(e[0]+2*e[1]+3*e[2]==w for e in poly),'low target weight')
    # Bind retained rows and constants to the actual normalized whole Jhat.
    J=parse(normalized['Jhat'],'source')
    row=lambda h,i:ring.coeff(ring.coeff(J,5,h),4,i)
    for poly,(h,i) in zip(G[:7],[(1,1),(1,2),(1,3),(0,1),(0,2),(0,3),(0,4)]): ring.eq(poly,row(h,i),'whole normalized low-row binding')
    ring.eq(H0,row(0,0),'whole H0 binding'); ring.eq(H1,row(1,0),'whole H1 binding')
    h0,h1,ubar=dense(data['h0'],4),dense(data['h1'],4),dense(data['ubar'],1)
    equal(h0,specialize(H0,4),'original H0 substitution')
    equal(h1,specialize(H1,4),'original H1 substitution')
    equal(ubar,specialize(U,1),'original U substitution')
    equal(specialize(p3,1),[],'Phi3 exactly consumed')
    require(data['consumed_slot']=={'id':'Phi3','image':[]},'consumed slot retained explicitly')
    ids=['E1/S1','E1/S2','E1/S3','E0/S1','E0/S2','E0/S3','E0/S4','P4','P11']; bounds=[3,3,2,4,3,3,2,2,5]
    require([row['id'] for row in data['rows']]==ids,'all nine literal indexed rows, no deduplication')
    polys=[]
    for i,(obj,name,bound) in enumerate(zip(data['rows'],ids,bounds)):
        require(obj['degree_bound']==bound,'fixed row degree envelope')
        got=dense(obj['coefficients'],bound)
        if i<7: want=specialize(G[i],bound)
        elif i==7: want=specialize(p4,bound)
        else: want=add(times(r,h1),[ring.scale(c,-1) for c in times(ubar,h0)])
        equal(got,want,'literal univariate row '+name); polys.append(got)
    guard=data['guard']
    require(set(guard)=={'variable','equation','q','factors'} and guard['variable']=='xi' and guard['equation']=='xi*q(T)-1' and guard['factors']==['r','h0'],'guard equation and both factors retained')
    q=dense(guard['q'],5); equal(q,times(r,h0),'entire guard q=r*h0')
    require(data['cover']==COVER,'literal accepted cubic and unsquared reconstruction contract')
    # r,h0 are not inverted in the polynomial checker. Their inverses occur
    # only in the accepted symbolic localization/cubic contract above.
    return {'status':'PASS-NINE-ROW-ADAPTER-NOT-IDEAL-DECISION','row_slots':9,'guard_factors':['r','h0'],
      'actual_degrees':[max((i for i,c in enumerate(p) if c),default=-1) for p in polys],
      'actual_guard_degree':max((i for i,c in enumerate(q) if c),default=-1),
      'rational_basis_terms':[sum(len(c) for c in p) for p in polys],
      'reconstruction':'accepted symbolic monic cubic cover; no physical-source expansion'}

def main():
    if len(sys.argv)!=6: raise SystemExit('registered AWS only: AUTHORITY NORMALIZED FULL_CHECKER_RECEIPT UNIVARIATE RECEIPT')
    custody=authorize(sys.argv[1],__file__,'check')
    from input_evidence import verified_input
    import hashlib,json
    normal,evidence=verified_input(sys.argv[1],sys.argv[2],sys.argv[3])
    spec=json.loads(Path(sys.argv[1]).read_text()); path=Path(sys.argv[4]).resolve(strict=True); raw=path.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
    if spec['file_sha256'].get(str(path))!=digest: raise RuntimeError('univariate artifact not registered/changed')
    data=json.loads(raw); producer=Path(__file__).with_name('adapter.py').resolve(strict=True)
    if spec['file_sha256'].get(str(producer))!=data.get('implementation_sha256'): raise RuntimeError('adapter implementation binding')
    if data.get('input_evidence')!=evidence: raise RuntimeError('univariate input evidence differs')
    result=verify(normal,data); result.update({'execution':custody,'input_evidence':evidence,'univariate_sha256':digest,'univariate_bytes':len(raw)})
    with open(sys.argv[5],'x',encoding='utf-8') as f: json.dump(result,f,sort_keys=True,separators=(',',':'),allow_nan=False); f.write('\n')
    print(result['status'])

if __name__=='__main__': main()
