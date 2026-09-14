"""Independent literal-source cover substitution, not a normalized self-generator.

In Q[a1..a20,b1..b59,ell,ell^-1], set k=ell^-6,z=ell^6.
The representation below reduces BOTH ell^6*k-1 and k*z-1 exactly.
No claim of an independent theorem/graph proof; no standalone production CLI.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
from math import comb
import construct as C

def decode(terms,n):
    out={};previous=None
    for c,m in terms:
        key=tuple(m)
        C.need(all(type(i) is int and 0<=i<n for i in key) and key==tuple(sorted(key)),'variable/monomial drift')
        C.need(previous is None or previous<key,'duplicate/noncanonical term');previous=key
        v=C.rational(c);C.need(v!=0,'explicit zero');out[key]=v
    C.need(C.wire(out)==terms,'coefficient wire drift');return out
def records(path):
    h=hashlib.sha256();done=False
    with Path(path).open('rb') as f:
        for line in f:
            C.need(not done,'trailing footer bytes');r=C.strict(line)
            C.need(C.B.canonical(r)==line,'noncanonical JSONL')
            if r['type']=='footer':
                C.need(r.get('complete') is True and r['prefix_sha256']==h.hexdigest(),'footer mismatch');done=True
            else:h.update(line)
            yield r
    C.need(done,'missing complete footer')

# Laurent key=(ordinary coefficient monomial, integer ell exponent).
def add(a,b,ops,scale=1):
    out=dict(a)
    for m,c in b.items():
        out[m]=out.get(m,F(0))+scale*c
        if not out[m]:del out[m]
    return ops.check(out)
def mul(a,b,ops):
    C.need(len(a)*len(b)<=ops.caps['multiply_pairs'],'cover pair cap')
    out={}
    for (m,e),c in a.items():
        for (n,f),d in b.items():
            key=(tuple(sorted(m+n)),e+f);out[key]=out.get(key,F(0))+c*d
            if not out[key]:del out[key]
    return ops.check(out)
def cover(p,power=0):
    out={}
    for m,c in p.items():
        C.need(all(i<=C.Z for i in m),'cover variable range')
        key=(tuple(i for i in m if i<C.K),power-6*m.count(C.K)+6*m.count(C.Z))
        out[key]=out.get(key,F(0))+c
        if not out[key]:del out[key]
    return out
def old_coefficient(p,D,d):
    if not p:return {}
    C.need((D-d)%2==0,'nonzero even coefficient');return cover(p,(D-d)//2)
def check_coefficient(member,D,entry,p,retained):
    C.shape(p,member);degree=sum(entry['point'])
    if degree%2==0:C.need(not p,'odd-parity map drift')
    if entry['name'] in retained:C.need(p==C.mono((retained[entry['name']],)),'retained coordinate drift')
    if member=='B' and entry['point']==[0,15]:C.need(not p,'whole-shear slice drift')
    old=old_coefficient(p,D,degree)
    if 'fixed' in entry:
        C.need(p==C.fixed(member,entry),'normalized fixed face drift')
        value=C.rational(entry['fixed']);want={((),0):value} if value else {}
        C.need(old==want,'original fixed-face pullback mismatch')
    return old
def substitute(p,maps,ops):
    out={}
    for m,c in p.items():
        term={((),0):c}
        for i in m:
            C.need(i in maps,'missing original variable map');term=mul(term,maps[i],ops)
            if not term:break
        out=add(out,term,ops)
    return out
def row_factor(label):
    parts=label.split('/')
    if parts[0]=='J':num=38-int(parts[1])-int(parts[2])
    elif parts[0]=='LIFT':num=(15 if parts[1]=='A' else 25)+int(parts[3])-5*int(parts[2])
    else:return 0
    return None if num%2 else num//2
def verify_row(literal,trace,maps,index,ops):
    label=literal['label'];C.need(trace.get('type')=='row' and trace.get('original_index')==index and trace.get('label')==label,'original row omitted/reordered')
    f=row_factor(label);C.need(trace.get('old_from_new_ell_power')==f,'row factor drift')
    normalized=decode(trace['terms'],81)
    if label.startswith('J/'):C.jshape(normalized)
    if label.startswith(('LIFT/','FIX/')):C.need(not normalized,'identity residual not zero')
    r=C.guard_power(label);C.need(trace.get('guard_power')==r and trace.get('guard_cofactor')==C.wire(C.guard_cofactor(r)),'guard trace drift')
    if label.startswith('GUARD/'):
        C.need(normalized==C.guard(r),'guard equation drift')
        C.need(C.Ops.add(ops,C.guard(r),ops.mul(C.guard(1),C.guard_cofactor(r)),-1)=={},'guard cofactor identity')
    original=substitute(decode(literal['terms'],269),maps,ops)
    if f is None:C.need(not normalized and not original,'wrong-parity row nonzero')
    else:C.need(original==cover(normalized,f),'literal original cover-row mismatch: '+label)
    return len(normalized),not normalized

def check_graph(g,member,s):
    cols=[1,2,3] if (member,s)==('B',15) else list(range((s+4)//5));n=len(cols)
    C.need(g.get('type')=='graph' and g.get('member')==member and g.get('degree')==s and g.get('pivots')==[[i,s-i] for i in cols],'graph index drift')
    inv=[[F(int(c[0]),int(c[1])) for c in row] for row in g['inverse']]
    C.need(len(inv)==n and all(len(row)==n for row in inv),'graph inverse size')
    mat=[[F((-1)**(s-i-t)*comb(s-i,t)) for i in cols] for t in range(n)]
    C.need(all(x.denominator==1 for row in inv for x in row),'nonunit graph inverse')
    C.need(all(sum(mat[i][k]*inv[k][j] for k in range(n))==int(i==j) for i in range(n) for j in range(n)),'graph matrix inverse failure')

def replay_frozen(source,construction,ops):
    C.need(ops.production,'production source replay forbidden locally')
    C.need(C.sha(source)==C.SOURCE,'frozen source hash')
    contract=C.B.make_contract('unequal','rational');_,ret,names=C.layout(contract,ops)
    out=iter(records(construction));head=next(out)
    original=contract['variables']+['lambda2','lambda3']
    C.need(head.get('type')=='header' and head.get('schema')=='jc2.hybrid-affine/v1' and head.get('field')=='Q' and head.get('order')=='dp' and head.get('source_sha256')==C.SOURCE and head.get('desk_sha256')==C.DESK and head.get('target')=='J+5*k^3*g^2/9' and head.get('variables')==names and head.get('original_variables')==original,'normalized header drift')
    maps={};expected_coefficients=[];retained={e['name']:i for i,e in enumerate([e for es in ret for e in es])}
    for w,D,es in zip(('A','B'),(15,25),contract['coefficient_maps']):
        for e in es:
            g=next(out);C.need(g.get('type')=='coefficient_map' and g.get('member')==w and g.get('source_entry')==e,'coefficient metadata drift')
            ops.stage(stage='coefficient_cover',member=w,degree=sum(e['point']),point=e['point'])
            p=decode(g['terms'],81);old=check_coefficient(w,D,e,p,retained)
            if 'variable' in e:maps[e['variable']]=ops.keep(old)
            expected_coefficients.append(dict(type='coefficient',member=w,**e))
    C.need(set(maps)==set(range(267)),'all original coefficient variables required')
    maps[267]={};maps[268]={((),1):F(1)}
    for w,D in [('A',15),('B',25)]:
        for s in range(D-2,0,-2):check_graph(next(out),w,s)
    r=next(out);source_names=[];coefficient_index=rows=terms=zeros=0
    for literal in records(source):
        kind=literal['type']
        if kind=='variable':
            C.need(literal['id']==len(source_names),'literal variable order');source_names.append(literal['name'])
        elif kind=='coefficient':
            C.need(coefficient_index<len(expected_coefficients) and literal==expected_coefficients[coefficient_index],'literal coefficient metadata omission/drift');coefficient_index+=1
        elif kind=='row':
            C.need(source_names==original and coefficient_index==len(expected_coefficients),'incomplete source metadata')
            ops.stage(stage='literal_cover_replay',row=rows,label=literal['label'])
            nt,nz=verify_row(literal,r,maps,rows,ops);terms+=nt;zeros+=nz;rows+=1;r=next(out)
        elif kind not in ('header','footer'):raise ValueError('unexpected original record')
    C.need(rows==803,'803 source rows required')
    C.need(r.get('type')=='row' and r.get('original_index') is None and r.get('label')=='UNIT/kz' and decode(r['terms'],81)==C.guard(1) and r.get('guard_power')==1 and r.get('guard_cofactor')==C.wire(C.const(1)) and r.get('old_from_new_ell_power')==0,'extra mandatory unit guard')
    C.need(not cover(decode(r['terms'],81)),'cover unit relation')
    footer=next(out);C.need(footer.get('type')=='footer' and footer.get('original_rows')==803 and footer.get('rows')==804 and footer.get('zero_original_rows')==zeros and footer.get('terms')==terms+2,'complete count/footer mismatch')
    C.need(next(out,None) is None,'extra output records');C.need(C.sha(source)==C.SOURCE,'source post-replay pin')
    return dict(status='ALL_803_ORIGINAL_ROWS_COVER_TRANSPORTED',rows=804,original_rows=803,terms=terms+2,zero_original_rows=zeros,scope='literal pullback and normalized equations only; no ideal decision; external graph/faithful-cover theorem retained',stats=ops.stats)
