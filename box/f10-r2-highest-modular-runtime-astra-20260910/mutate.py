"""One cofactor mutation; source only, standalone before mathematical imports."""
import os
import sys

JOB = 'f10-r2-highest-modular-mutation-v1'
BASE = 'dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587'
ARITH = 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345'


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    need(sys.platform == 'linux', 'Linux only')
    with open('/sys/class/dmi/id/sys_vendor', encoding='ascii') as f:
        need(f.read(128).strip() == 'Amazon EC2', 'AWS only')
    flags = ('--registered-job','--root-registration-sha256','--self-sha256','--arithmetic',
             '--baseline','--certificate','--positive-receipt','--output','--receipt')
    need(len(sys.argv) == 19 and tuple(sys.argv[1::2]) == flags and sys.argv[2] == JOB,
         'exact registered mutation vector')
    args = dict(zip(flags,sys.argv[2::2]))
    for key in ('--root-registration-sha256','--self-sha256'):
        text = args[key]
        need(len(text) == 64 and set(text) <= set('0123456789abcdef') and text != '0'*64, 'external pin')
    import hashlib
    import stat
    def sha(raw):
        return hashlib.sha256(raw).hexdigest()
    me = os.path.abspath(__file__)
    paths = [me]+[args[k] for k in ('--arithmetic','--baseline','--certificate','--positive-receipt','--output','--receipt')]
    need(len(set(paths)) == 7, 'distinct paths')
    for path in paths:
        need(os.path.isabs(path) and os.path.realpath(path) == path and len(path)<=512
             and '\n' not in path and '\r' not in path, 'canonical path')
    def read(path,cap):
        fd = os.open(path,os.O_RDONLY|os.O_NOFOLLOW)
        with os.fdopen(fd,'rb') as f:
            before = os.fstat(f.fileno())
            need(stat.S_ISREG(before.st_mode) and before.st_size<=cap, 'regular bounded input')
            raw = f.read(cap+1)
            after = os.fstat(f.fileno())
            need(len(raw)<=cap and (before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns,before.st_ctime_ns)
                 == (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns,after.st_ctime_ns), 'input drift')
            return raw
    sources = {me:args['--self-sha256'],args['--arithmetic']:ARITH}
    def pins():
        for path,digest in sources.items():
            need(sha(read(path,1048576)) == digest, 'source pin')
    pins()  # Before JSON/Fraction/module or any coefficient-payload read.
    need(not os.path.lexists(args['--output']) and not os.path.lexists(args['--receipt']), 'output collision')
    import json
    import importlib.util
    need(hasattr(sys,'set_int_max_str_digits'), 'integer guard')
    sys.set_int_max_str_digits(4300)
    def pairs(items):
        out = {}
        for k,v in items:
            need(k not in out,'duplicate key'); out[k]=v
        return out
    def number(_):
        raise ValueError('numeric JSON forbidden')
    def load(raw):
        return json.loads(raw.decode('ascii'),object_pairs_hook=pairs,parse_int=number,
                          parse_float=number,parse_constant=number)
    def dump(obj):
        return (json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode('ascii')
    positive_raw=read(args['--positive-receipt'],32768)
    positive=load(positive_raw)
    need(dump(positive)==positive_raw and type(positive) is dict and set(positive)==
         {'schema','status','science_outcome','mode','prime','root','root_registration_sha256',
          'sources','baseline_sha256','baseline_bytes','certificate_sha256'}, 'positive receipt shape')
    need(positive['schema']=='f10-r2-highest-modular89-receipt/v1'
         and positive['status']=='HIGHEST_SPECIAL_PROJECTIVE_CHECKED_NO_SOURCE_OUTCOME'
         and positive['science_outcome']=='NONE' and positive['mode']=='check'
         and positive['prime']=='89' and positive['root']=='0'
         and positive['root_registration_sha256']==args['--root-registration-sha256']
         and positive['baseline_sha256']==BASE and positive['baseline_bytes']=='1652675', 'positive receipt bindings')
    expected={'1e685c413484f90d68db77bba844cb220f0d1b86c33c1d82ac9f587ad76c15f5',
              '8afc9b158483183e1afefef65c5aad54a8a46615b0f3b3d4682812c8dd8d74b2',
              'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'}
    need(type(positive['sources']) is dict and len(positive['sources'])==3
         and set(positive['sources'].values())==expected,'positive source set')
    for path,digest in positive['sources'].items():
        need(os.path.isabs(path) and os.path.realpath(path)==path and sha(read(path,1048576))==digest,'positive current source')
    raw = read(args['--baseline'],15728640)
    need(len(raw)==1652675 and sha(raw)==BASE, 'baseline binding')
    cert_raw = read(args['--certificate'],2097152)
    need(sha(cert_raw)==positive['certificate_sha256'], 'certificate binding')
    spec = importlib.util.spec_from_file_location('_mutation_original_arithmetic',args['--arithmetic'])
    need(spec is not None and spec.loader is not None,'loader')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    Q = m.Q
    def rat(text):
        need(type(text) is str and text.count('/')==1,'rational syntax')
        a,b=text.split('/')
        for s,sign in ((a,True),(b,False)):
            d=s[1:] if sign and s.startswith('-') else s
            need(1<=len(s)<=4096 and d and set(d)<=set('0123456789') and s!='-0'
                 and (len(d)==1 or d[0]!='0'),'canonical integer')
        n,d=int(a),int(b); need(d>0,'positive denominator')
        q=Q(n,d); need((q.numerator,q.denominator)==(n,d),'reduced rational'); return q
    def mod(q):
        d=q.denominator%89; need(d!=0,'dense p-unit denominator')
        i=pow(d,87,89); need(d*i%89==1,'inverse readback')
        return q.numerator%89*i%89
    need(all(89%d for d in range(2,10)),'fixed prime')
    tau=Q(2,7)
    dl=[(1+tau)*(2-3*tau),-12*(1-tau),Q(12)]
    kl=[2*(2-3*tau)*(1+tau)*(2+tau)*(3+tau),42*(1+tau)*(2+tau)*(4*tau-3),840*(1-tau*tau),Q(-840)]
    ga=[tau*(1+tau)*(2+tau)*(3+tau),-30*tau*(1+tau)*(2+tau),180*tau*(1+tau),-120*tau]
    poly=m.qa(m.qs(m.qm(kl,kl),2),m.qa(m.qs(m.qm(m.qm([1+tau,-6],kl),dl),-140*tau),m.qs(m.qm(ga,m.qm(dl,dl)),245)))
    need(len(poly)==8 and poly[-1]==-245*120*144*tau,'literal septic')
    modulus=m.qs(poly,1/poly[-1])
    doc=load(raw); need(dump(doc)==raw,'canonical baseline')
    face=doc['interface']
    need(doc['format']=='r2-reconstruction-19-v1' and doc['job_tag']=='f10-r2-reconstruction-v1'
         and face['variables']==['X1','X2','X3','z','S','vartheta'] and face['weights']==['1','2','3','5','1','2']
         and face['base']=='Q[Z]/P7' and face['basis']==[str(i) for i in range(7)],'source interface')
    need(type(doc['field']['P7']) is list and len(doc['field']['P7'])==8,'modulus shape')
    actual=[rat(s) for s in doc['field']['P7']]; need(actual==modulus,'literal modulus equality')
    residues=[mod(q) for q in actual]; need(residues[0]==0 and residues[1]!=0,'simple fixed root')
    rows=doc['rows']['Psi']; need(type(rows) is list and len(rows)==3,'three rows')
    forms=[]
    for h,row in zip((5,6,7),rows):
        need(type(row) is list and len(row)<=4096,'row bound')
        table={}; previous=None
        for term in row:
            need(type(term) is list and len(term)==2,'sparse pair')
            ex,wire=term
            need(type(ex) is list and len(ex)==6 and all(type(s) is str and s in [str(i) for i in range(17)] for s in ex),'exponents')
            need(type(wire) is list and len(wire)==7,'full basis')
            e=tuple(int(s) for s in ex); coefficients=[rat(s) for s in wire]
            need(any(coefficients) and (previous is None or previous<e),'nonzero/sorted sparse'); previous=e
            need(e[4]==e[5]==0 and e[0]+2*e[1]+3*e[2]+5*e[3]==h,'whole support')
            rr=[mod(q) for q in coefficients]  # Positive-z and all seven coordinates too.
            if e[3]==0: table[(e[1],e[2])]=(table.get((e[1],e[2]),0)+rr[0])%89
        forms.append(table)
    need(forms[0].get((1,1),0) and forms[1].get((3,0),0) and forms[1].get((0,2),0),'same boundary')
    def trim(a):
        a=list(a)
        while a and a[-1]==0: a.pop()
        return a
    def add(a,b):
        return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%89 for i in range(max(len(a),len(b)))])
    def mul(a,b):
        out=[0]*(len(a)+len(b))
        for i,x in enumerate(a):
            for j,y in enumerate(b): out[i+j]=(out[i+j]+x*y)%89
        return trim(out)
    def neg(a): return [(-x)%89 for x in a]
    shapes=({0:2,1:1},{0:3,1:1,2:0},{0:3,1:2,2:0})
    for table,shape in zip(forms,shapes):
        need(all(v in shape and u<=shape[v] for (u,v),value in table.items() if value),'chart shape')
    def line(table,v,d): return trim([table.get((u,v),0) for u in range(d+1)])
    p,q=line(forms[0],0,2),line(forms[0],1,1)
    b3,b1,b0=line(forms[1],0,3),line(forms[1],1,1),line(forms[1],2,0)
    c3,c2,c1=line(forms[2],0,3),line(forms[2],1,2),line(forms[2],2,0)
    f=add(add(mul(mul(q,q),b3),neg(mul(mul(p,q),b1))),mul(b0,mul(p,p)))
    g=add(add(mul(mul(q,q),c3),neg(mul(mul(p,q),c2))),mul(c1,mul(p,p)))
    need(len(f)<=6 and len(g)<=6,'eliminant degree')
    cert=load(cert_raw); need(dump(cert)==cert_raw,'canonical certificate')
    need(type(cert) is dict and set(cert)=={'schema','baseline_sha256','prime','root','chart','modulus','c','d'},'certificate fields')
    need(cert['schema']=='f10-r2-highest-modular89/v1' and cert['baseline_sha256']==BASE
         and cert['prime']=='89' and cert['root']=='0' and cert['chart']=='z=0;X1=1;u=X2;v=X3'
         and cert['modulus']==doc['field']['P7'],'certificate binding')
    def residue_list(a):
        need(type(a) is list and len(a)<=6 and all(type(s) is str and s in [str(i) for i in range(89)] for s in a),'residue array')
        need(not a or a[-1]!='0','canonical trimming')
        return [int(s) for s in a]
    ca,da=residue_list(cert['c']),residue_list(cert['d'])
    identity=add(mul(ca,f),mul(da,g))
    need(all((identity[i] if i<len(identity) else 0)==(1 if i==0 else 0) for i in range(11)), 'input full identity')
    side='c' if f else 'd'; need(f or g,'nonzero selected factor')
    old=list(cert[side]); old0=int(old[0]) if old else 0
    edited=[int(s) for s in old] or [0]; edited[0]=(old0+1)%89
    cert[side]=[str(i) for i in trim(edited)]
    changed=dump(cert); need(changed!=cert_raw and len(changed)<=2097152,'changed bounded certificate')
    restored=load(changed); restored[side]=old
    need(dump(restored)==cert_raw,'inverse restores whole certificate bytes')
    def write(path,data,cap):
        need(len(data)<=cap,'output bound')
        fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o444)
        with os.fdopen(fd,'wb') as f:
            need(f.write(data)==len(data),'short write')
            f.flush(); os.fchmod(f.fileno(),0o444); os.fsync(f.fileno())
        need(read(path,cap)==data,'exclusive output readback')
        dfd=os.open(os.path.dirname(path),os.O_RDONLY|os.O_DIRECTORY)
        try: os.fsync(dfd)
        finally: os.close(dfd)
    pins()
    need(read(args['--baseline'],15728640)==raw and read(args['--certificate'],2097152)==cert_raw
         and read(args['--positive-receipt'],32768)==positive_raw,'payload postpins')
    write(args['--output'],changed,2097152)
    receipt={'schema':'f10-r2-highest-modular-mutation/v1','status':'ONE_COFACTOR_MUTATED_UNCHECKED',
             'science_outcome':'NONE','job_tag':JOB,'root_registration_sha256':args['--root-registration-sha256'],
             'sources':sources,'baseline_sha256':BASE,'baseline_bytes':'1652675',
             'input':{'path':args['--certificate'],'sha256':sha(cert_raw),'bytes':str(len(cert_raw))},
             'output':{'path':args['--output'],'sha256':sha(changed),'bytes':str(len(changed))},
             'selection':{'side':side,'index':'0','old':str(old0),'new':str((old0+1)%89),
                          'old_length':str(len(old)),'new_length':str(len(cert[side]))},
             'inverse_edit_restores_whole_input_bytes':True,'checker_run':False}
    write(args['--receipt'],dump(receipt),32768)


if __name__ == '__main__':
    main()
