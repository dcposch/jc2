"""UNEXECUTED independent rational certificate checker; no engine/emitter import."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import json, hashlib, re
from fractions import Fraction
from execution_gate import authorize

ARTIFACT='168bdfd3a791f24a6631de66ae4e71c3f209ee9eb0d21fc466f9aa802f5ad576'
NAMES=['u','ell','d0','d1','v0','v1','v2','k1','k2','k3','k4','omega']
ZERO=(0,)*12
IDS=['E1/S'+str(i) for i in range(9)]+['E0/S'+str(i) for i in range(10)]+['GUARD/omega*a*b-1']

class Invalid(Exception): pass

def require(ok,message):
    if not ok: raise Invalid(message)

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def integer(s):
    require(type(s) is str and re.fullmatch(r'-?(0|[1-9][0-9]*)',s) is not None,'integer STRING syntax')
    n=int(s); require(str(n)==s,'canonical integer STRING'); return n

def rational(n,d):
    a,b=integer(n),integer(d); require(a!=0 and b>0,'nonzero rational/positive denominator')
    q=Fraction(a,b); require(q.numerator==a and q.denominator==b,'reduced rational'); return q

def readwire(wire):
    require(type(wire) is list,'wire list'); out={}; prev=None
    for term in wire:
        require(type(term) is list and len(term)==3,'term shape')
        exps,n,d=term
        require(type(exps) is list and len(exps)==12 and all(type(e) is int and e>=0 for e in exps),'exponents')
        e=tuple(exps); require(prev is None or prev<e,'sorted unique wire'); prev=e
        out[e]=rational(n,d)
    return out

def source_rows(data):
    require(data['schema']=='F10-L1-EXACT/v1' and data['variables']==NAMES,'source variable/schema mismatch')
    require([x['id'] for x in data['rows']]==IDS,'twenty source IDs')
    require(data['gauges']=={'beta':0,'gamma':0,'k0':0},'source gauges')
    return [readwire(x['polynomial']) for x in data['rows']]

def parse_transcript(raw):
    require(type(raw) is str,'text transcript'); lines=raw.splitlines()
    require(lines[:3]==['F10-DECISION/1','ARTIFACT|'+ARTIFACT,'RING|Q|dp|'+','.join(NAMES)],'framing/ring')
    pos=3; polynomials={}; order=[]; branch=None
    while pos<len(lines):
        line=lines[pos]; pos+=1
        if line=='DONE':
            require(pos==len(lines),'trailing engine output'); break
        if line.startswith('BRANCH|'):
            require(branch is None and len(order)==20,'branch position')
            require(line in ('BRANCH|UNIT','BRANCH|PROPER'),'unknown branch')
            branch=line.split('|')[1]; continue
        require(line.startswith('POLY|'),'unsupported engine output')
        tag=line[5:]; require(tag not in polynomials,'duplicate polynomial tag'); poly={}
        while pos<len(lines) and lines[pos]!='ENDPOLY':
            cells=lines[pos].split('|'); pos+=1
            require(len(cells)==4 and cells[0]=='TERM','term protocol')
            parts=cells[1].split(','); require(len(parts)==12,'exponent vector width')
            e=tuple(integer(x.strip()) for x in parts); require(all(x>=0 for x in e),'negative exponent')
            require(e not in poly,'duplicate engine monomial'); poly[e]=rational(cells[2],cells[3])
        require(pos<len(lines) and lines[pos]=='ENDPOLY','unfinished polynomial'); pos+=1
        polynomials[tag]=poly; order.append(tag)
    else: raise Invalid('missing DONE')
    require(order[:20]==['ROW/'+str(i) for i in range(20)],'read-back row mapping')
    require(branch is not None,'missing branch')
    if branch=='UNIT': require(order[20:]==['U']+['T/'+str(i) for i in range(20)],'unit dimensions/tags')
    else: require(order[20:]==['G/'+str(i) for i in range(len(order)-20)],'basis dimensions/tags')
    return branch,polynomials

def key(e): return (sum(e),tuple(-x for x in reversed(e)))
def leading(p): return max(p,key=key)
def add(a,b,scale=Fraction(1)):
    r=dict(a)
    for e,c in b.items():
        v=r.get(e,Fraction(0))+scale*c
        if v: r[e]=v
        else: r.pop(e,None)
    return r
def shift(p,e,c=Fraction(1)):
    return {tuple(a+b for a,b in zip(m,e)):v*c for m,v in p.items() if v*c}
def multiply(a,b):
    r={}
    for e,c in a.items(): r=add(r,shift(b,e,c))
    return r
def normal(p,basis):
    work=dict(p); rem={}
    while work:
        e=leading(work); c=work[e]
        for g in basis:
            h=leading(g)
            if all(a>=b for a,b in zip(e,h)):
                step=tuple(a-b for a,b in zip(e,h))
                work=add(work,shift(g,step,c/g[h]),Fraction(-1)); break
        else:
            rem[e]=c; del work[e]
    return rem

def readback(rows,polys):
    require(len(rows)==20,'twenty inputs')
    for i,row in enumerate(rows): require(polys['ROW/'+str(i)]==row,'source row read-back '+str(i))

def check_certificate(rows,branch,polys):
    readback(rows,polys)
    if branch=='UNIT':
        U=polys['U']; require(set(U)=={ZERO} and U[ZERO]!=0,'U must be a nonzero rational unit')
        result={}
        for i,row in enumerate(rows): result=add(result,multiply(row,polys['T/'+str(i)]))
        require(result==U,'source-row cofactor identity')
        return {'verdict':'VERIFIED-UNIT','rational_unit':[str(U[ZERO].numerator),str(U[ZERO].denominator)],'rows':20}
    require(branch=='PROPER','branch')
    basis=[polys['G/'+str(i)] for i in range(len(polys)-20)]
    for g in basis:
        require(bool(g),'zero basis member'); h=leading(g)
        require(h!=ZERO and g[h]==1,'proper monic leading term')
    pairs=0
    for i,f in enumerate(basis):
        a=leading(f)
        for g in basis[:i]:
            b=leading(g); lcm=tuple(max(x,y) for x,y in zip(a,b))
            s=add(shift(f,tuple(x-y for x,y in zip(lcm,a))),
                  shift(g,tuple(x-y for x,y in zip(lcm,b))),Fraction(-1))
            require(not normal(s,basis),'failed S-pair'); pairs+=1
    for i,f in enumerate(rows): require(not normal(f,basis),'failed input containment '+str(i))
    return {'verdict':'VERIFIED-PROPER','basis_members':len(basis),'S_pairs':pairs,'rows':20,
            'scope':'I contained in a certified proper ideal; no equality/dimension claim'}

def main():
    require(len(sys.argv)==5,'certificate AUTH ARTIFACT ENGINE_RECEIPT RESULT')
    custody=authorize(sys.argv[1],__file__,'check'); spec=json.loads(Path(sys.argv[1]).read_text())
    require(sha(sys.argv[2])==ARTIFACT,'artifact hash')
    receiptpath=Path(sys.argv[3]).resolve(strict=True)
    require(spec['file_sha256'].get(str(receiptpath))==sha(receiptpath),'engine receipt registered pin')
    receipt=json.loads(receiptpath.read_text())
    require(receipt['schema']=='F10-ENGINE/1' and receipt['artifact_sha256']==ARTIFACT and receipt['returncode']==0,'engine receipt binding')
    require(receipt['engine_sha256']==spec['engine_sha256'] and receipt['engine_path']==spec['engine_path'],'engine source pin')
    require(receipt['engine_argv']==spec['engine_argv'] and receipt['engine_version']==spec['engine_version'],'engine argv/version binding')
    for k in ('input','stdout','stderr'):
        p=Path(receipt[k+'_path']).resolve(strict=True)
        require(p.parent==Path.cwd() and spec['file_sha256'].get(str(p))==receipt[k+'_sha256']==sha(p),'registered engine output '+k)
    require(Path(receipt['stderr_path']).stat().st_size==0,'nonempty engine stderr')
    rows=source_rows(json.loads(Path(sys.argv[2]).read_text()))
    branch,polys=parse_transcript(Path(receipt['stdout_path']).read_text())
    result=check_certificate(rows,branch,polys)
    result.update({'schema':'F10-EXACT-DECISION/1','execution':custody,'artifact_sha256':ARTIFACT,
                   'engine_receipt_sha256':sha(receiptpath),'raw_witness_sha256':receipt['stdout_sha256']})
    with Path(sys.argv[4]).open('x') as f: json.dump(result,f,sort_keys=True); f.write('\n')

if __name__=='__main__': main()
