"""DISABLED/UNEXECUTED independent full-source read-back.
Does not import generator, run its Euler recurrence, invert B elements, or solve.
Uses original frozen rows/coefficient arrays plus flat monomial long reduction.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from execution_gate import authorize
SOURCE='168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'

def verify(original,data):
    from algebra import Ring,Q,ZERO,require,matvec
    from math import gcd
    class Flat(Ring):
        def __init__(self):
            # Independent literal expression; no producer dense reducer.
            def plus(a,b):
                out=dict(a)
                for k,c in b.items(): out[k]=out.get(k,Q(0))+c
                return {k:c for k,c in out.items() if c}
            def times(a,b):
                out={}
                for i,c in a.items():
                    for j,d in b.items(): out[i+j]=out.get(i+j,Q(0))+c*d
                return {k:c for k,c in out.items() if c}
            def scale(a,c): return {i:x*c for i,x in a.items() if x*c}
            E={0:Q(39),1:Q(-360),2:Q(960),3:Q(-512)}
            L={0:Q(25),1:Q(-144),2:Q(192)}; R={0:Q(-195),1:Q(2016),2:Q(-6720),3:Q(7168)}
            p=plus(plus(scale(times(R,R),24),times({0:Q(280),1:Q(-1344)},times(L,R))),scale(times(E,times(L,L)),49))
            require(max(p)==7,'fixed modulus degree')
            self.p=[p.get(i,Q(0)) for i in range(8)]; self.lower={i:c/p[7] for i,c in p.items() if i<7}
        def mul(self,a,b):
            out={}
            for e,c in a.items():
                for f,d in b.items():
                    k=tuple(x+y for x,y in zip(e,f)); out[k]=out.get(k,Q(0))+c*d
            out={e:c for e,c in out.items() if c}
            while any(e[6]>=7 for e in out):
                key=max((e for e in out if e[6]>=7),key=lambda e:e[6]); c=out.pop(key)
                for i,d in self.lower.items():
                    f=key[:6]+(key[6]-7+i,); out[f]=out.get(f,Q(0))-c*d
                    if not out[f]: del out[f]
            return out
        def pow(self,a,n):
            require(type(n) is int and n>=0,'nonnegative power')
            out=self.c(1)
            for _ in range(n): out=self.mul(out,a)
            return out
        def inv(self,*args): raise RuntimeError('checker cannot invert product-algebra elements')
        def read(self,wire,width=7):
            require(type(wire) is list,'wire list'); out={}; previous=None
            for term in wire:
                require(type(term) is list and len(term)==3,'term shape')
                e,n,d=term
                require(type(e) is list and len(e)==width and all(type(i) is int for i in e),'exponent type')
                require(all(i>=0 for a,i in enumerate(e) if width!=7 or a!=3),'exponent sign')
                require(width!=7 or (e[6]<7 and e[3]==0),'canonical normalized B[x,y,z,S,t] basis')
                require(type(n) is str and type(d) is str,'exact rational strings')
                a,b=int(n),int(d)
                require(str(a)==n and str(b)==d and a!=0 and b>0 and gcd(abs(a),b)==1,'canonical rational')
                key=tuple(e); require(previous is None or previous<key,'wire ordering/duplicates'); previous=key
                out[key]=Q(a,b)
            return out
    def nofloat(x):
        require(type(x) is not float,'float forbidden')
        if isinstance(x,(dict,list)):
            for y in (x.values() if isinstance(x,dict) else x): nofloat(y)
    nofloat(data); nofloat(original); r=Flat(); one=r.c(1); S,t=r.atom(4),r.atom(5)
    require(data['schema']=='F10-R1-NORMALIZED-FOUR-BAND/v1' and data['source_sha256']==SOURCE,'schema/source')
    require(data['axes']==['x','y','z','s','S','t','v'],'axis order')
    require(original['schema']=='F10-L1-EXACT/v1' and original['variables']==['u','ell','d0','d1','v0','v1','v2','k1','k2','k3','k4','omega'],'original schema/order')
    require(data['modulus']==[[str(c.numerator),str(c.denominator)] for c in r.p],'literal modulus')
    units={k:r.read(w) for k,w in data['units'].items()}
    require(set(units)=={'L','Linv','w','winv','f5','f5inv','a','ainv'},'unit inventory')
    require(all(all(not any(e[:6]) for e in p) for p in units.values()),'units must lie in B')
    v=r.atom(6); L=r.add(r.c(25),r.scale(v,-144),r.scale(r.pow(v,2),192)); R=r.add(r.c(-195),r.scale(v,2016),r.scale(r.pow(v,2),-6720),r.scale(r.pow(v,3),7168))
    r.eq(units['L'],L,'L definition'); r.eq(r.mul(L,units['Linv']),one,'L inverse')
    w,wi,f5,fi=units['w'],units['winv'],units['f5'],units['f5inv']
    r.eq(r.scale(r.mul(L,w),112),R,'w definition'); r.eq(r.mul(w,wi),one,'w inverse')
    expected_f5=r.add(r.c(Q(-63,8192)),r.scale(v,Q(35,512)),r.scale(r.pow(v,2),Q(-21,128)),r.scale(w,Q(-21,128)),r.scale(r.mul(v,w),Q(21,16)))
    r.eq(f5,expected_f5,'f5 partitions'); r.eq(r.mul(f5,fi),one,'f5 inverse')
    F,H,a,b=[r.read(p) for p in data['leading']]
    for got,want in zip((F,H,a,b),(r.mul(v,wi),wi,wi,fi)): r.eq(got,want,'leading definition')
    r.eq(units['a'],a,'a unit'); r.eq(r.mul(a,units['ainv']),one,'a inverse')
    C=r.add(a,r.mul(H,t),r.mul(F,r.pow(t,2)),r.pow(t,3)); D=r.add(*(r.mul(r.read(p),r.pow(t,i)) for i,p in enumerate(data['D'])))
    require(len(data['D'])==6,'D inventory')
    r.eq(r.sub(r.scale(r.mul(C,r.diff(D,5)),4),r.scale(r.mul(r.diff(C,5),D),7)),r.scale(r.pow(t,7),-1),'complete leading ODE')
    maps={k:[r.read(p) for p in val] for k,val in data['maps'].items()}
    require(set(maps)=={'1','2','3','4'} and all(len(v)==8 for v in maps.values()),'four maps inventory')
    for low in maps.values():
        for p,weight in zip(low,[2,4,1,2,1,3,2,1]):
            require(all(e[3]==e[4]==e[5]==0 and e[0]+2*e[1]+3*e[2]==weight for e in p),'normalized map domain/weight')
    def eqz(a,b,why): r.eq(r.at_z_s2(a),r.at_z_s2(b),why)
    def mapping(low):
        u,ell,d0,v0,v1,k1,k2,k3=map(r.at_z_s2,low)
        shift=lambda p,n:r.mul(p,r.atom(3,n))
        return [shift(u,-1),shift(ell,-3),shift(d0,-1),shift(F,-1),shift(v0,-2),shift(v1,-2),shift(H,-2),shift(k1,-3),shift(k2,-3),shift(k3,-3),shift(a,-3),shift(r.mul(w,f5),8),S]
    def pull(wire,low,width): return r.compose(r.read(wire,width),mapping(low)[:width])
    ids=['E1/S'+str(i) for i in range(9)]+['E0/S'+str(i) for i in range(10)]+['GUARD/omega*a*b-1']
    require([x['id'] for x in original['rows']]==ids and data['original_slot_inventory']==ids,'all20 original slots')
    require(data['source_scale_powers']==[-1,-3,-1,-1,-2,-2,-2,-3,-3,-3,-3,8],'original parameter scale inventory')
    oldrows={x['id']:x['polynomial'] for x in original['rows']}
    def source_row(low,h,i): return r.mul(pull(oldrows['E'+str(h)+'/S'+str(i)],low,12),r.atom(3,7-h))
    def rho(low,band,kindex):
        got=r.mul(pull(original['B'][0],low,13),r.atom(3,5))
        return r.sub(r.scale(r.mul(a,r.coeff(got,4,band)),4),r.scale(r.mul(b,r.at_z_s2(low[kindex])),7))
    # Completed matrix bindings come from frozen full source coefficients,
    # not the generator's descending recurrence.
    N1=[[r.read(p) for p in row] for row in data['N1']]; N2=[[r.read(p) for p in row] for row in data['N2']]
    dets=[r.read(p) for p in data['determinants']]
    require(len(dets)==4,'two determinant/inverse pairs')
    for band,N in ((1,N1),(2,N2)):
        for i in range(3):
            low=[{} for _ in range(8)]
            if band==1: low[(2,4,7)[i]]=one
            else:
                q,l,k=[one if j==i else {} for j in range(3)]
                low[0]=r.scale(q,-1); low[3]=r.sub(l,r.mul(F,q)); low[6]=k
            expected=[source_row(low,1,8-band),source_row(low,0,9-band),rho(low,7-band,7 if band==1 else 6)]
            for j in range(3): eqz(N[j][i],expected[j],'source-bound completed matrix')
        inv=[[r.read(p) for p in row] for row in data['N'+str(band)+'inv']]
        require(len(N)==len(inv)==3 and all(len(row)==3 for row in N+inv),'matrix dimensions')
        for i in range(3):
            for j in range(3): r.eq(r.add(*(r.mul(N[i][k],inv[k][j]) for k in range(3))),r.c(i==j),'completed inverse identity')
        det=r.add(*(r.scale(r.mul(N[0][i],r.mul(N[1][j],N[2][k])),sgn) for i,j,k,sgn in ((0,1,2,1),(1,2,0,1),(2,0,1,1),(0,2,1,-1),(1,0,2,-1),(2,1,0,-1))))
        r.eq(dets[2*band-2],det,'literal completed determinant')
        r.eq(r.mul(det,dets[2*band-1]),one,'completed determinant unit witness')
    first=maps['1']; second=maps['2']; third=maps['3']; final=maps['4']
    for i in (0,1,3,5,6): r.eq(first[i],{},'first-map free slots initialized')
    for got,want in zip(matvec(r,N1,[first[i] for i in (2,4,7)]),[{}, {},r.atom(0)]): r.eq(got,want,'first completed backmap')
    c2=[r.read(w) for w in data['c2']]
    for got,want in zip(c2,[source_row(first,1,6),source_row(first,0,7)]): eqz(got,want,'whole second forcing')
    q=r.scale(second[0],-1); l=r.add(second[3],r.mul(F,q)); k=second[6]
    for got,want in zip(matvec(r,N2,[q,l,k]),[r.scale(c2[0],-1),r.scale(c2[1],-1),r.atom(1)]): r.eq(got,want,'second completed backmap')
    for i in (2,4,7): r.eq(first[i],second[i],'first map retained')
    for i in (1,5): r.eq(second[i],{},'second lower slots initialized')
    for number,previous,current,kindex,h,indices,sign in ((3,second,third,5,'h3',(5,6),1),(4,third,final,1,'h4',(4,5),-1)):
        column=[r.read(w) for w in data[h]]; lam=[r.read(w) for w in data['lambda'+str(number)]]; c=[r.read(w) for w in data['c'+str(number)]]
        require(len(column)==len(lam)==len(c)==2,'two-row inventory')
        require(all(all(not any(e[:6]) for e in p) for p in column+lam),'column and inverse lie in B')
        r.eq(r.add(*(r.mul(a,b) for a,b in zip(column,lam))),one,'literal left inverse')
        probe=list(previous); probe[kindex]=r.add(probe[kindex],one)
        for n,(hh,ii) in enumerate(zip((1,0),indices)):
            eqz(c[n],source_row(previous,hh,ii),'full affine forcing including third correction')
            eqz(column[n],r.sub(source_row(probe,hh,ii),source_row(previous,hh,ii)),'full source column')
        r.eq(current[kindex],r.scale(r.add(*(r.mul(a,b) for a,b in zip(lam,c))),-1),'affine elimination')
        for i in range(8):
            if i!=kindex: r.eq(current[i],previous[i],'triangular unchanged map')
        compat=r.scale(r.sub(r.mul(column[0],c[1]),r.mul(column[1],c[0])),sign)
        r.eq(r.read(data['Phi'+str(number)]),compat,'compatibility determinant')
    # Full reconstructed A/B are checked against every original coefficient,
    # and their entire derivative bracket is computed independently.
    require(len(data['A'])==4 and len(data['B'])==6,'whole A/B coefficient lists')
    A=[r.read(p) for p in data['A']]; B=[r.read(p) for p in data['B']]
    for label,polys,total in (('A',A,3),('B',B,5)):
        slotlists=data['coefficient_slots'][label]
        require(len(slotlists)==len(polys),'coefficient slot-list length')
        for j,p in enumerate(polys):
            eqz(p,r.mul(pull(original[label][j],final,13),r.atom(3,total-j)),'original whole '+label+' coefficient')
            require(all(e[4]<=total+1-j if label=='A' else e[4]<=7-j for e in p),'coefficient envelope')
            require(all(e[5]==0 and e[3]==0 for e in p),'ordinary normalized coefficients')
            degree=4 if label=='A' else 7
            require(all(e[0]+2*e[1]+3*e[2]+e[4]==degree-j for e in p),'full coefficient weight')
            require(len(slotlists[j])==degree-j+1 and len(original['coefficient_slots'][label][j])==degree-j+1,'all zero coefficient slots')
            for i,wire in enumerate(slotlists[j]):
                r.eq(r.read(wire),r.coeff(p,4,i),'normalized coefficient slot')
                eqz(r.read(wire),r.mul(pull(original['coefficient_slots'][label][j][i],final,12),r.atom(3,total-j)),'original coefficient slot substitution')
    AA=r.add(*(r.mul(p,r.pow(t,j)) for j,p in enumerate(A))); BB=r.add(*(r.mul(p,r.pow(t,j)) for j,p in enumerate(B)))
    for i,p in enumerate(data['D']): r.eq(r.read(p),r.coeff(B[i],4,7-i),'D is the actual whole-mate leading band')
    U,E=final[:2]; Pi=r.add(r.mul(r.atom(2),t),r.scale(r.mul(U,r.pow(t,2)),-1),r.mul(S,r.pow(t,3)))
    r.eq(r.read(data['Pi']),Pi,'full Pi')
    J=r.add(r.bracket(AA,BB),r.mul(E,r.mul(t,Pi)),r.mul(t,r.pow(Pi,2)))
    r.eq(r.read(data['Jhat']),J,'full target and determinant')
    require(all(e[5]<=7 for e in J),'full bracket t envelope')
    for j in range(2,8): r.eq(r.coeff(J,5,j),{},'entire upper bracket band')
    jacmap=[{'t_degree':h,'S_degree':i,'row':('E'+str(h)+'/S'+str(i)) if h<2 else 'ELIMINATED-ZERO'} for h in range(8) for i in range(10-h)]
    require(data['jacobian_slot_map']==original['jacobian_slot_map']==jacmap,'entire bracket zero-slot map')
    require(set(data['forcing'])=={str(i) for i in range(5)},'all forcing slots')
    for j in range(5): eqz(r.read(data['forcing'][str(j)]),r.mul(pull(original['forcing'][str(j)],final,13),r.atom(3,5-j)),'original full forcing')
    lowids=ids[:-1]; require([p[0] for p in data['low_slot_inventory']]==lowids,'every low slot including zeros')
    for name,wire in data['low_slot_inventory']:
        hh=int(name[1]); ii=int(name.split('/S')[1]); got=r.coeff(r.coeff(J,5,hh),4,ii)
        r.eq(r.read(wire),got,'low slot projection')
        actual=source_row(final,hh,ii)
        if ii==0: actual=r.add(actual,r.mul(r.at_z_s2(U),r.atom(3,5)) if hh else r.atom(3,7))
        eqz(got,actual,'every original residual row and unsquared target')
    r.eq(pull(oldrows[ids[-1]],final,12),{},'full original guard')
    require(data['gauges']==original['gauges']=={'k0':0,'beta':0,'gamma':0},'gauge declaration')
    r.eq(r.coeff(A[0],4,0),{},'A constant gauge'); r.eq(r.coeff(B[0],4,0),{},'B constant gauge'); r.eq(r.coeff(B[3],4,1),{},'mate shear gauge')
    r.eq(r.coeff(A[0],4,4),a,'actual A top'); r.eq(r.coeff(B[0],4,7),b,'actual B top'); r.eq(r.mul(r.mul(w,f5),r.mul(a,b)),one,'top product restoration')
    for key,want in (('a',a),('b',b),('normalized_omega',r.mul(w,f5)),('guard',{})):
        r.eq(r.read(data['restoration'][key]),want,'restoration slot '+key)
    eqz(r.mul(a,r.atom(3,-3)),pull(original['restoration']['a'],final,13),'original a restoration')
    eqz(r.mul(b,r.atom(3,-5)),pull(original['restoration']['b'],final,13),'original b restoration')
    r.eq(pull(original['restoration']['guard'],final,13),{},'original guard restoration slot')
    # Direct normalized inverse S=p*Z^3-z*Z^2+U*Z, tau=Z^-1.
    poles={'A':[[-3,0],[-2,0],[-1,0]],'B':[[-5,0],[-4,0],[-3,0],[-2,0],[-2,1],[-1,0],[-1,1]]}
    require(data['pole_slots']==original['pole_slots']==poles,'ten pole inventory')
    invS=r.add(r.mul(S,r.pow(t,3)),r.scale(r.mul(r.atom(2),r.pow(t,2)),-1),r.mul(U,t))
    for label,polys in (('A',A),('B',B)):
        negative={}
        for j,p in enumerate(polys):
            for e,c in p.items():
                i=e[4]
                if i>=j: continue
                k=list(e); k[4]=0; k[5]=-j
                term=r.mul({tuple(k):c},r.pow(invS,i))
                negative=r.add(negative,{k:c for k,c in term.items() if k[5]<0})
        require(all([e[5],e[4]] in poles[label] for e in negative),'unmapped pole')
        r.eq(negative,{},'whole inverse polynomiality '+label)
    def row(h,i): return r.coeff(r.coeff(J,5,h),4,i)
    for h,i in ((1,8),(0,9),(1,7),(0,8),(1,6),(0,7)): r.eq(row(h,i),{},'all removed zero slots')
    l3=[r.read(p) for p in data['lambda3']]; l4=[r.read(p) for p in data['lambda4']]
    phi3=r.read(data['Phi3']); phi4=r.read(data['Phi4'])
    for got,want in ((row(1,5),r.scale(r.mul(l3[1],phi3),-1)),(row(0,6),r.mul(l3[0],phi3)),(row(1,4),r.mul(l4[1],phi4)),(row(0,5),r.scale(r.mul(l4[0],phi4),-1))): r.eq(got,want,'both retained compatibility read-backs')
    expectedG=[row(1,i) for i in (1,2,3)]+[row(0,i) for i in (1,2,3,4)]+[r.read(data['Phi3']),r.read(data['Phi4'])]
    require(len(data['G'])==9,'nine G inventory')
    for wire,want in zip(data['G'],expectedG): r.eq(r.read(wire),want,'G exact projection')
    r.eq(r.read(data['H0']),row(0,0),'H0 whole constant target'); r.eq(r.read(data['H1']),row(1,0),'H1 whole linear target')
    weights=[1,2,3,0,1,1,0]
    require(data['weights']=={'axes':weights,'G':[7,6,5,8,7,6,5,3,4],'H0':9,'H1':8},'weight inventory')
    for p,weight in list(zip(expectedG,[7,6,5,8,7,6,5,3,4]))+[(row(0,0),9),(row(1,0),8)]:
        require(all(e[3]==e[4]==e[5]==0 and sum(e[i]*weights[i] for i in range(7))==weight for e in p),'B[x,y,z] homogeneous equation')
    measured=[]
    for name,p in list(zip(['G'+str(i+1) for i in range(9)],expectedG))+[('H0',row(0,0)),('H1',row(1,0))]:
        measured.append({'id':name,'terms':len(p),'max_parameter_degree':max((sum(e[:3]) for e in p),default=-1),'max_v_degree':max((e[6] for e in p),default=-1),'max_rational_bits':max((max(abs(c.numerator).bit_length(),c.denominator.bit_length()) for c in p.values()),default=0)})
    return {'status':'PASS-NORMALIZED-REPRESENTATION-NOT-IDEAL-DECISION','original_slots':20,'G_slots':9,'H_slots':2,'full_inverse_poles':10,'full_bracket_bands':8,'measured_rows':measured}

def main():
    if len(sys.argv)!=5: raise SystemExit('registered AWS only: AUTHORITY ORIGINAL NORMALIZED RECEIPT')
    custody=authorize(sys.argv[1],__file__,'check')
    import hashlib,json
    spec=json.loads(Path(sys.argv[1]).read_text()); src=Path(sys.argv[2]).resolve(strict=True); artifact=Path(sys.argv[3]).resolve(strict=True)
    if spec['file_sha256'].get(str(src))!=SOURCE or str(artifact) not in spec['file_sha256']: raise RuntimeError('both artifact pins required')
    backend=Path(__file__).with_name('algebra.py').resolve(strict=True); producer=Path(__file__).with_name('generator.py').resolve(strict=True)
    if str(backend) not in spec['file_sha256'] or str(producer) not in spec['file_sha256']: raise RuntimeError('all source pins required')
    raw,body=src.read_bytes(),artifact.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=SOURCE or hashlib.sha256(body).hexdigest()!=spec['file_sha256'][str(artifact)]: raise RuntimeError('artifact changed')
    parsed=json.loads(body)
    if parsed.get('implementation_sha256')!=spec['file_sha256'][str(producer)]: raise RuntimeError('producer binding')
    out=verify(json.loads(raw),parsed); out.update({'execution':custody,'artifact_sha256':hashlib.sha256(body).hexdigest(),'source_sha256':SOURCE,'artifact_bytes':len(body)})
    with open(sys.argv[4],'x',encoding='utf-8') as f: json.dump(out,f,sort_keys=True,separators=(',',':'),allow_nan=False); f.write('\n')
    print(out['status'])

if __name__=='__main__': main()
