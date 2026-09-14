"""DISABLED/UNEXECUTED nine-row adapter; accepted theorem, provisional backend.
argv AUTHORITY NORMALIZED FULL_CHECKER_RECEIPT OUTPUT. No solve/GCD of rows.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from execution_gate import authorize

def adapt(data):
    from algebra import Ring,Q,require,ZERO
    from input_evidence import COVER
    r=Ring(); one=r.c(1); T=r.atom(0); theta=r.atom(5)
    require(data['schema']=='F10-R1-NORMALIZED-FOUR-BAND/v1' and data['axes']==['x','y','z','s','S','t','v'],'normalized schema/axes')
    require(data['modulus']==[[str(c.numerator),str(c.denominator)] for c in r.p],'fixed modulus')
    def read(wire):
        p=r.read(wire)
        require(all(not any(e[3:6]) for e in p),'normalized parameter-only polynomial')
        return p
    phi3,phi4=read(data['Phi3']),read(data['Phi4'])
    def extract(poly,e):
        out={}
        for key,c in poly.items():
            if key[:3]==e: out[ZERO[:6]+(key[6],)]=c
        return out
    e3=[(3,0,0),(1,1,0),(0,0,1)]; e4=[(4,0,0),(2,1,0),(0,2,0),(1,0,1)]
    require(all(e[:3] in e3 for e in phi3) and all(e[:3] in e4 for e in phi4),'complete compatibility monomial shapes')
    aa,bb,cc=[extract(phi3,e) for e in e3]; dd,ee,ff,gg=[extract(phi4,e) for e in e4]
    # Exact accepted17l inverse formula, not generic inversion of a row.
    F,H,a,b=[read(p) for p in data['leading']]
    require(all(all(not any(e[:6]) for e in p) for p in (F,H,a,b)),'leading B coefficients')
    r.eq(H,a,'normalized H=a')
    ai=read(data['units']['ainv']); r.eq(r.mul(a,ai),one,'a inverse input')
    C=r.add(a,r.mul(H,theta),r.mul(F,r.pow(theta,2)),r.pow(theta,3)); C2=r.pow(C,2)
    es=[r.pow(ai,2)]
    for i in range(1,7):
        es.append(r.scale(r.mul(es[0],r.add(*(r.mul(r.coeff(C2,5,j),es[i-j]) for j in range(1,min(i,6)+1)))),-1))
    l1,l0=[read(p) for p in data['lambda3']]
    integ={}
    for i in range(1,8):
        coefficient=r.sub(r.mul(l1,es[i-1]),r.mul(l0,es[i-2]) if i>=2 else {})
        integ=r.add(integ,r.scale(r.mul(coefficient,r.pow(theta,i)),Q(1,i)))
    ci=r.scale(r.coeff(r.mul(C2,integ),5,7),Q(21,2))
    r.eq(r.mul(cc,ci),one,'actual c inverse product')
    rp=r.scale(r.mul(ci,r.add(aa,r.mul(bb,T))),-1)
    def specialize(poly):
        out={}
        for e,c in poly.items():
            term={ZERO[:6]+(e[6],):c}
            term=r.mul(term,r.pow(T,e[1])); term=r.mul(term,r.pow(rp,e[2]))
            out=r.add(out,term)
        return out
    require(len(data['G'])==9,'all normalized G slots')
    G=[read(p) for p in data['G']]
    r.eq(G[7],phi3,'Phi3 G position'); r.eq(G[8],phi4,'Phi4 G position')
    weights=[7,6,5,8,7,6,5,3,4]
    for p,w in zip(G,weights): require(all(e[0]+2*e[1]+3*e[2]==w for e in p),'G weights')
    h0n,h1n,un=read(data['H0']),read(data['H1']),read(data['maps']['4'][0])
    for p,w in ((h0n,9),(h1n,8),(un,2)): require(all(e[0]+2*e[1]+3*e[2]==w for e in p),'low target weights')
    h0,h1,ubar=map(specialize,(h0n,h1n,un))
    r.eq(specialize(phi3),{},'consumed Phi3 exact zero')
    p4=r.add(dd,r.mul(ee,T),r.mul(ff,r.pow(T,2)),r.mul(gg,rp))
    r.eq(p4,specialize(phi4),'P4 exact projection')
    p11=r.sub(r.mul(rp,h1),r.mul(ubar,h0)); guard=r.mul(rp,h0)
    polys=[specialize(p) for p in G[:7]]+[p4,p11]
    ids=['E1/S1','E1/S2','E1/S3','E0/S1','E0/S2','E0/S3','E0/S4','P4','P11']
    bounds=[3,3,2,4,3,3,2,2,5]
    def wire(poly,bound):
        require(all(not any(e[1:6]) and e[0]<=bound for e in poly),'univariate support/degree')
        return [r.wire(r.coeff(poly,0,i)) for i in range(bound+1)]
    return {'schema':'F10-R1-NINE-UNIVARIATE/v1','coefficient_ring':'Q[v]/p(v), entire algebra','variable':'T','modulus':data['modulus'],
      'coefficients':{k:r.wire(p) for k,p in zip('abcdefg',(aa,bb,cc,dd,ee,ff,gg))},'c_inverse':r.wire(ci),
      'r':wire(rp,1),'h0':wire(h0,4),'h1':wire(h1,4),'ubar':wire(ubar,1),
      'rows':[{'id':name,'degree_bound':bound,'coefficients':wire(p,bound)} for name,bound,p in zip(ids,bounds,polys)],
      'guard':{'variable':'xi','equation':'xi*q(T)-1','q':wire(guard,5),'factors':['r','h0']},
      'consumed_slot':{'id':'Phi3','image':[]},'cover':COVER,
      'scope':'all nine indexed rows, including zero/duplicate/degree-drop slots; no division by b; no factor, solver or ideal claim'}

def main():
    if len(sys.argv)!=5: raise SystemExit('registered AWS only: AUTHORITY NORMALIZED CHECKER_RECEIPT OUTPUT')
    custody=authorize(sys.argv[1],__file__,'build')
    from input_evidence import verified_input
    import hashlib,json
    data,evidence=verified_input(sys.argv[1],sys.argv[2],sys.argv[3])
    out=adapt(data); out['input_evidence']=evidence; out['execution']=custody
    out['implementation_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with open(sys.argv[4],'x',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,separators=(',',':'),allow_nan=False); f.write('\n')
    print('NINE-ROW-ADAPTER-ONLY; NO IDEAL DECISION')

if __name__=='__main__': main()
