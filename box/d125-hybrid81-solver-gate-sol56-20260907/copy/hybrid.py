"""Literal hybrid81 adapter only. No reconstruction, CAS, execution or authority."""
from collections import Counter
from fractions import Fraction as F
import re
import exact as E

CONSTRUCTION_SHA='4ea526b2680ef41154332be3059ae5543c2678fdf8fb6a95d02176e8eb929272'
ORIGINAL_SHA='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac'
TARGET='J+5*k^3*g^2/9'
INPUT_BYTES=2*1024**2

def rational(pair):
    E.need(isinstance(pair,list) and len(pair)==2 and all(isinstance(x,str) for x in pair),'rational pair')
    c=F(*map(int,pair));E.need(pair==[str(c.numerator),str(c.denominator)],'noncanonical rational')
    return c

def decode(terms,n):
    E.need(isinstance(terms,list),'term list');out={};last=None
    for entry in terms:
        E.need(isinstance(entry,list) and len(entry)==2,'term record')
        coeff,m=entry;E.need(isinstance(coeff,list) and len(coeff)==2,'Q wire')
        a,b=map(rational,coeff);E.need(b==0,'golden coefficient/splitting forbidden')
        E.need(isinstance(m,list) and all(type(i)is int and 0<=i<n for i in m),'monomial indices')
        key=tuple(m);E.need(a!=0 and m==sorted(m) and (last is None or last<key),'zero/duplicate/unsorted term')
        out[key]=a;last=key
    return out

def ordinary(p,variables):
    pieces=[]
    for m,c in sorted(p.items()):
        count=Counter(m);factors=[variables[i]+('^'+str(e) if e>1 else '') for i,e in sorted(count.items())]
        coefficient=str(c.numerator) if c.denominator==1 else '('+str(c.numerator)+'/'+str(c.denominator)+')'
        pieces.append(coefficient+('*'+'*'.join(factors) if factors else ''))
    return '+'.join(pieces) if pieces else '0'

def read_hybrid(data,production=False):
    E.need(isinstance(data,bytes),'bytes required')
    if production:E.need(E.digest(data)==CONSTRUCTION_SHA,'frozen hybrid pin drift')
    else:E.need(len(data)<=32768,'tiny byte ceiling')
    rec=[E.strict_json(line) for line in data.splitlines()]
    E.need(len(rec)>=3 and rec[0].get('type')=='header' and rec[-1].get('type')=='footer','hybrid framing')
    h,f=rec[0],rec[-1];prefix=b''.join(E.canonical(r) for r in rec[:-1])
    E.need(prefix+E.canonical(f)==data and f.get('complete')is True and f.get('prefix_sha256')==E.digest(prefix),'canonical footer/hash')
    E.need(h.get('schema')=='jc2.hybrid-affine/v1' and h.get('field')=='Q' and h.get('order')=='dp' and h.get('target')==TARGET,'schema/field/order/target')
    E.need(h.get('source_sha256')==ORIGINAL_SHA,'original source binding')
    variables=h['variables'];E.need(isinstance(variables,list) and variables and len(set(variables))==len(variables),'variables')
    E.need(all(isinstance(v,str) and re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*',v) for v in variables),'variable names')
    rows=[];labels=[];maps=graphs=mapterms=0;phase=0
    for r in rec[1:-1]:
        kind=r.get('type')
        if kind=='coefficient_map':
            E.need(phase==0 and r.get('member') in ('A','B'),'map phase/member')
            m=decode(r['terms'],len(variables));maps+=1;mapterms+=len(m)
        elif kind=='graph':
            E.need(phase<=1 and r.get('member') in ('A','B'),'graph phase/member');phase=1;graphs+=1
        else:
            E.need(kind=='row','unknown/misplaced record');phase=2
            E.need(r.get('original_index')==(len(rows) if len(rows)<f['original_rows'] else None),'literal original index')
            label=r['label'];E.need(isinstance(label,str) and re.fullmatch(r'[A-Za-z0-9_/-]+',label),'unsafe label')
            rows.append(decode(r['terms'],len(variables)));labels.append(label)
            decode(r['guard_cofactor'],len(variables))
            E.need(type(r['guard_power'])is int and r['guard_power']>=0 and (r['old_from_new_ell_power']is None or type(r['old_from_new_ell_power'])is int),'transport metadata')
    E.need(len(labels)==len(set(labels)) and labels[-1]=='UNIT/kz','unique labels/final unit')
    E.need(len(rows)==f['rows']==f['original_rows']+1 and sum(map(len,rows))==f['terms'] and sum(not p for p in rows[:-1])==f['zero_original_rows'] and mapterms==f['coefficient_map_terms'],'complete row/term/map counts')
    if production:
        E.need((len(variables),len(rows),maps,graphs)==(81,804,298,19) and variables[-2:]==['k','z'],'complete hybrid client')
        E.need(len(h['original_variables'])==269 and f['terms']==58684 and f['zero_original_rows']==578,'frozen census')
        E.need(rows[-1]=={():F(-1),(79,80):F(1)},'unit guard drift')
    else:E.need(len(variables)<=8 and len(rows)<=32,'tiny dimension ceiling')
    parts=['ring R=0,('+','.join(variables)+'),dp;\nideal I=\n']
    for i,(label,p) in enumerate(zip(labels,rows)):
        text=ordinary(p,variables);E.need(E.polynomial(text,variables)==p,'literal serializer disagreement')
        parts.append('// '+label+'\n'+text+(';\n' if i==len(rows)-1 else ',\n'))
    result=''.join(parts);E.need(len(result.encode('ascii'))<=INPUT_BYTES,'unchanged2MiB input ceiling')
    return variables,rows,labels,result

def checked_certificate(data,stdout,stderr,production=False):
    variables,rows,labels,unused=read_hybrid(data,production)
    engine,basis,cofactors=E.parse_result(stdout,stderr,variables,E.digest(data))
    mapping=E.engine_map(rows,engine)
    if cofactors is None:verdict=E.proper_certificate(rows,basis,len(variables))
    else:verdict,mapping,unused=E.unit_certificate(rows,engine,cofactors)
    return verdict,mapping,labels
