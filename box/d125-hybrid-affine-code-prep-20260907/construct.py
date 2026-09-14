"""PREP ONLY normalized Hermite-only client. No solver or production authority."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib,json,os,platform,resource,signal,sys,time
import baseline as B

SOURCE='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac'
SOURCE_PATH='/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl'
BASELINE='ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'
DESK='b33d6944976ac934535bcc516bae82c738cd2e957665bfffb2325ec63170aa5a'
NORMALIZATION='53f78754d8e567e145db4038f6f5b39f2f9a56c462178f20b1e94a2f6f0e7e10'
ROOT=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907')
INSTANCE='i-0da0cebfc97c9fd54'
CAPS=dict(wall_seconds=300,cpu_seconds=300,address_bytes=4*1024**3,
          file_bytes=128*1024**2,polynomial_terms=100000,multiply_pairs=1000000,
          retained_terms=1000000,coefficient_bits=4096)
K,Z=79,80

def need(ok,msg):
    if not ok:raise ValueError(msg)
def const(c):
    c=F(c);return {():c} if c else {}
def mono(m,c=1):return {tuple(sorted(m)):F(c)} if c else {}
def rational(w):
    c=B.decode(w);need(not c.b,'rational field only');return c.a
def wire(p):return [[B.F(c).wire(),list(m)] for m,c in sorted(p.items())]
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
def strict(data):
    def pairs(items):
        d={}
        for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
        return d
    return json.loads(data,object_pairs_hook=pairs)

class Ops:
    def __init__(self,caps,deadline,production=False):
        self.caps,self.deadline,self.production=caps,deadline,production
        self.context={};self.stats=dict(operations=0,max_terms=0,max_bits=0,retained_terms=0)
    def stage(self,**kw):
        self.context=kw
        if self.production:print(json.dumps(dict(type='stage',**kw)),file=sys.stderr,flush=True)
    def check(self,p):
        bits=max((max(abs(c.numerator).bit_length(),c.denominator.bit_length()) for c in p.values()),default=0)
        if time.monotonic()>=self.deadline or len(p)>self.caps['polynomial_terms'] or bits>self.caps['coefficient_bits']:
            raise ValueError(json.dumps(dict(error='arithmetic cap',pending_terms=len(p),pending_bits=bits,**self.context)))
        self.stats['operations']+=1;self.stats['max_terms']=max(self.stats['max_terms'],len(p));self.stats['max_bits']=max(self.stats['max_bits'],bits)
        return p
    def add(self,a,b,c=1):
        self.check(a);self.check(b);o=dict(a)
        for m,v in b.items():
            o[m]=o.get(m,F(0))+F(c)*v
            if not o[m]:del o[m]
        return self.check(o)
    def mul(self,a,b):
        pending=len(a)*len(b)
        need(pending<=self.caps['multiply_pairs'],json.dumps(dict(error='pair cap',pending_pairs=pending,**self.context)))
        o={}
        for m,c in a.items():
            for n,d in b.items():
                key=tuple(sorted(m+n));o[key]=o.get(key,F(0))+c*d
                if not o[key]:del o[key]
        return self.check(o)
    def keep(self,p):
        self.check(p);self.stats['retained_terms']+=len(p)
        need(self.stats['retained_terms']<=self.caps['retained_terms'],json.dumps(dict(error='retained cap',pending_terms=self.stats['retained_terms'],**self.context)))
        return p

def inverse(m):
    n=len(m);need(n>0 and all(len(r)==n for r in m),'square matrix')
    a=[[F(x) for x in r]+[F(i==j) for j in range(n)] for i,r in enumerate(m)]
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]),None);need(k is not None,'singular pivot')
        a[j],a[k]=a[k],a[j];d=a[j][j];a[j]=[x/d for x in a[j]]
        for k in range(n):
            if k!=j:
                d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[j])]
    return [r[n:] for r in a]
def columns(member,s):
    return [1,2,3] if (member,s)==('B',15) else list(range((s+4)//5))
def matrix(s,cols):return [[(-1)**(s-i-t)*comb(s-i,t) for i in cols] for t in range(len(cols))]
def fixed(member,entry):
    v=rational(entry['fixed']);p=tuple(entry['point'])
    power={('A',(2,1)):1,('B',(8,5)):1,('B',(1,0)):2}.get((member,p),0)
    return mono((K,)*power,v)
def shape(p,member):
    ids=range(20) if member=='A' else range(20,79)
    allowed={() ,(K,)}|{(i,) for i in ids}
    if member=='B':allowed.add((K,K))
    need(set(p)<=allowed,'affine member support drift '+member)
    need(len(p)<=(22 if member=='A' else 62),'affine term bound')
    den=1 if member=='A' else 9
    need(all((den*c).denominator==1 for c in p.values()),'member denominator drift')
def jshape(p):
    def allowed(m):
        a=[i for i in m if i<20];b=[i for i in m if 20<=i<79];k=m.count(K)
        return len(m)==len(a)+len(b)+k and len(a)<=1 and len(b)<=1 and ((len(a)==1 and len(b)==1 and k==0) or (len(a)==1 and not b and k<=2) or (not a and len(b)==1 and k<=1) or (not a and not b and k<=3))
    need(len(p)<=1362 and all(allowed(m) for m in p),'Jacobian monomial/degree bound')
    need(all((9*c).denominator==1 for c in p.values()),'Jacobian denominator bound')

def layout(contract,ops):
    need(ops.production,'production metadata forbidden locally')
    entries=contract['coefficient_maps'];free=[[e for e in es if 'variable' in e and sum(e['point'])%2] for es in entries]
    piv=[{(i,s-i) for s in range(1,D,2) for i in columns(w,s)} for w,D in [('A',15),('B',25)]]
    ret=[[e for e in es if tuple(e['point']) not in pp and not (w=='B' and e['point']==[0,15])] for w,es,pp in zip(('A','B'),free,piv)]
    need([len(es) for es in free]==[33,94] and [len(pp) for pp in piv]==[13,34] and [len(es) for es in ret]==[20,59],'metadata counts')
    for es,pp in zip(free,piv):need(pp<={tuple(e['point']) for e in es},'pivot not free')
    return piv,ret,[e['name'] for es in ret for e in es]+['k','z']

def liftrow(coeffs,t,e,ops):
    need(ops.production or (len(coeffs)<=8 and max((sum(p) for p in coeffs),default=0)<=7),'full lift forbidden locally')
    out={}
    for (i,j),v in coeffs.items():
        dd=e+i+j-5*t
        if not v or j<t or dd<0 or dd%2:continue
        d=dd//2;r=j-t-d
        if r>=0:out=ops.add(out,v,F((-1)**(j-t)*factorial(j),factorial(t)*factorial(d)*factorial(r)))
    return out
def solve_level(coeffs,member,s,ops):
    cols=columns(member,s);pts=[(i,s-i) for i in cols]
    need(all(not coeffs.get(p,{}) for p in pts),'pivot must initially be zero')
    ops.stage(stage='Hermite',member=member,degree=s,pivots=pts)
    rhs=[liftrow(coeffs,t,5*t-s,ops) for t in range(len(cols))];inv=inverse(matrix(s,cols))
    need(all(c.denominator==1 for r in inv for c in r),'nonunit Hermite inverse')
    values=[]
    for row in inv:
        p={}
        for c,q in zip(row,rhs):p=ops.add(p,q,-c)
        shape(p,member);values.append(ops.keep(p))
    coeffs.update(zip(pts,values))
    return dict(member=member,degree=s,pivots=pts,inverse=[[[str(c.numerator),str(c.denominator)] for c in r] for r in inv])

def reconstruct(contract,ops):
    piv,ret,names=layout(contract,ops);coeffs=[];index=0;graphs=[]
    for w,D,entries,retained in zip(('A','B'),(15,25),contract['coefficient_maps'],ret):
        c={tuple(e['point']):fixed(w,e) if 'fixed' in e else {} for e in entries}
        for e in retained:c[tuple(e['point'])]=mono((index,));index+=1
        for s in range(D-2,0,-2):graphs.append(solve_level(c,w,s,ops))
        for e in entries:
            p=c[tuple(e['point'])];shape(p,w)
            if 'fixed' in e:need(p==fixed(w,e),'fixed coefficient changed')
            if sum(e['point'])%2==0:need(not p,'parity drift')
        coeffs.append(c)
    need(index==79 and not coeffs[1][0,15],'slice/count drift')
    return names,coeffs,graphs

def jrow(a,b,I,J,ops):
    need(ops.production or len(a)*len(b)<=64,'full J forbidden locally')
    out=mono((K,K,K),F(5,9)) if (I,J)==(2,0) else {}
    for (i,j),v in a.items():
        k,l=I+1-i,J+1-j;det=i*l-j*k
        if det and v and b.get((k,l)):out=ops.add(out,ops.mul(v,b[k,l]),det)
    jshape(out);return out
def guard_power(label):
    return {'GUARD/A/2/1':1,'GUARD/B/1/0':2,'GUARD/c':3}.get(label,0)
def guard(r):return {tuple(sorted((K,)*r+(Z,)*r)):F(1),():F(-1)} if r else {}
def guard_cofactor(r):return {tuple(sorted((K,)*j+(Z,)*j)):F(1) for j in range(r)}
def factor(label):
    bits=label.split('/')
    if bits[0]=='J':
        n=int(bits[1])+int(bits[2]);return None if n%2 else (38-n)//2
    if bits[0]=='LIFT':
        _,w,t,e=bits;v=(15 if w=='A' else 25)+int(e)-5*int(t)
        return None if v%2 else v//2
    return 0
def rows(contract,coeffs,ops):
    for w,es,c in zip(('A','B'),contract['coefficient_maps'],coeffs):
        for e in es:
            if 'fixed' in e:yield 'FIX/'+e['name'],ops.add(c[tuple(e['point'])],fixed(w,e),-1)
    for I in range(24):
        for J in range(39-I):
            ops.stage(stage='J',row=[I,J]);yield f'J/{I}/{J}',jrow(*coeffs,I,J,ops)
    for w,D,c in zip(('A','B'),(15,25),coeffs):
        for t in range((D-1)//5+1):
            for e in range(5*t-D,0):
                ops.stage(stage='lift_identity',member=w,row=[t,e]);p=liftrow(c,t,e,ops)
                need(not p,'complete polynomiality identity failure');yield f'LIFT/{w}/{t}/{e}',p
    for g in contract['vertex_guards']:
        need(rational(g['value'])*rational(g['inverse'])==1,'original guard drift')
        yield g['label'],guard(guard_power(g['label']))
    need(rational(contract['scalar']['fixed'])*rational(contract['scalar']['inverse'])==1,'scalar guard drift')
    yield 'GUARD/c',guard(3)

class Stream:
    def __init__(self,path,cap):self.f=Path(path).open('xb');self.cap=cap;self.used=0;self.h=hashlib.sha256()
    def emit(self,r):
        data=B.canonical(r);need(self.used+len(data)<=self.cap,json.dumps(dict(error='output byte cap',label=r.get('label'),pending_bytes=self.used+len(data))))
        self.f.write(data);self.used+=len(data);self.h.update(data)
    def poly(self,r,p):
        estimate=1024+sum(128+(abs(c.numerator).bit_length()+c.denominator.bit_length())//3+12*len(m) for m,c in p.items())
        need(self.used+estimate<=self.cap,json.dumps(dict(error='pre-serialization byte cap',label=r.get('label'),member=r.get('member'),pending_terms=len(p),pending_bytes=self.used+estimate)));self.emit(dict(r,terms=wire(p)))
    def close(self):self.f.flush();os.fsync(self.f.fileno());self.f.close()

def authority_check(a,observed,pins,registration,green):
    need(a.get('schema')=='jc2.hybrid-affine-authority/v1' and a.get('root_green') is True and a.get('construction_only') is True,'explicit authority absent')
    need(a.get('job') and a.get('mode')=='normalized-hermite-only-slice','registered exact mode')
    need(observed['system']=='Linux' and observed['vendor']=='Amazon EC2' and observed['instance']==INSTANCE and observed['cwd']==str(ROOT),'exact EC2 host/cwd')
    need(observed['boot']==a.get('boot_id'),'boot mismatch')
    need(a.get('code_sha256')==pins and a.get('registration_sha256')==registration and a.get('root_green_sha256')==green,'code/registration/GREEN pins')
    need(a.get('source_path')==SOURCE_PATH and a.get('source_sha256')==SOURCE and a.get('desk_sha256')==DESK and a.get('normalization_gate_sha256')==NORMALIZATION,'source/theorem pins')
    for key in ('hybrid_gate_sha256','code_gate_sha256'):
        value=a.get(key,'');need(len(value)==64 and all(c in '0123456789abcdef' for c in value),'new accepted gate pin missing')
    need(a.get('gates_accepted') is True,'unaccepted gates')
    caps=a.get('caps',{});need(set(caps)==set(CAPS) and all(type(caps[k]) is int and 0<caps[k]<=v for k,v in CAPS.items()),'caps drift')
    need(0<a.get('expires_unix',0)-observed['now']<=caps['wall_seconds'],'absolute shared expiry')
    return caps
def authorize(path):
    need(Path.cwd()==ROOT and Path(path).resolve()==ROOT/'authority.json','exact new authority cwd/path')
    a=strict(Path(path).read_bytes())
    obs=dict(system=platform.system(),vendor=Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),instance=Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),cwd=str(Path.cwd()),boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),now=time.time())
    pins={n:sha(ROOT/n) for n in ('construct.py','replay.py','baseline.py')}
    need(pins['baseline.py']==BASELINE,'baseline pin')
    caps=authority_check(a,obs,pins,sha(ROOT/'REGISTRATION.md'),sha(ROOT/'ROOT-GREEN.md'))
    for kind,value in [(resource.RLIMIT_AS,caps['address_bytes']),(resource.RLIMIT_CPU,caps['cpu_seconds']),(resource.RLIMIT_FSIZE,caps['file_bytes']),(resource.RLIMIT_CORE,0)]:resource.setrlimit(kind,(value,value))
    signal.setitimer(signal.ITIMER_REAL,a['expires_unix']-time.time())
    return a,Ops(caps,time.monotonic()+a['expires_unix']-time.time(),True)

def build(a,ops):
    need(ops.production,'production construction forbidden locally')
    started=time.monotonic()
    stream=Stream(ROOT/'construction.jsonl',ops.caps['file_bytes'])
    try:
        contract=B.make_contract('unequal','rational');names,coeffs,graphs=reconstruct(contract,ops)
        stream.emit(dict(type='header',schema='jc2.hybrid-affine/v1',status='PROVISIONAL_NO_POINT_OR_DECISION',variables=names,field='Q',order='dp',source_sha256=SOURCE,desk_sha256=DESK,original_variables=contract['variables']+['lambda2','lambda3'],target='J+5*k^3*g^2/9',authority_sha256=sha(ROOT/'authority.json')))
        for w,es,c in zip(('A','B'),contract['coefficient_maps'],coeffs):
            for e in es:stream.poly(dict(type='coefficient_map',member=w,source_entry=e),c[tuple(e['point'])])
        for g in graphs:stream.emit(dict(type='graph',**g))
        n=terms=zeros=0;used=set()
        for label,p in rows(contract,coeffs,ops):
            r=guard_power(label);stream.poly(dict(type='row',original_index=n,label=label,old_from_new_ell_power=factor(label),guard_power=r,guard_cofactor=wire(guard_cofactor(r))),p)
            n+=1;terms+=len(p);zeros+=not p;used.update(i for m in p for i in m)
        need(n==803,'803 original row count')
        stream.poly(dict(type='row',original_index=None,label='UNIT/kz',old_from_new_ell_power=0,guard_power=1,guard_cofactor=wire(const(1))),guard(1))
        used.update((K,Z))
        stream.emit(dict(type='footer',complete=True,original_rows=n,rows=n+1,zero_original_rows=zeros,terms=terms+2,prefix_sha256=stream.h.hexdigest(),stats=ops.stats,elapsed_seconds=time.monotonic()-started,process_maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,coefficient_map_terms=sum(len(p) for c in coeffs for p in c.values()),unused_residual_coordinates=[i for i in range(81) if i not in used],semantics='all normalized rows; independent original cover replay required'))
    finally:stream.close()

def main():
    need(len(sys.argv)==2,'one authority path only')
    a,ops=authorize(sys.argv[1]);need(sha(SOURCE_PATH)==SOURCE,'source pre-construction pin');build(a,ops)
    import replay
    need(Path(replay.__file__).resolve()==ROOT/'replay.py','replay module path')
    result=replay.replay_frozen(a['source_path'],ROOT/'construction.jsonl',ops)
    with (ROOT/'replay-result.json').open('xb') as f:f.write(B.canonical(result));f.flush();os.fsync(f.fileno())
    print(json.dumps(result))
if __name__=='__main__':main()
