"""One cofactor mutation; source only, standalone before mathematical imports."""
import os
import sys

JOB = 'f10-r2-fullunit-modular-mutation-v1'
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
    need(positive['schema']=='f10-r2-fullunit-modular89-receipt/v1'
         and positive['status']=='FULL_SPECIAL_UNIT_CHECKED_NO_SOURCE_OUTCOME'
         and positive['science_outcome']=='NONE' and positive['mode']=='check'
         and positive['prime']=='89' and positive['root']=='0'
         and positive['root_registration_sha256']==args['--root-registration-sha256']
         and positive['baseline_sha256']==BASE and positive['baseline_bytes']=='1652675', 'positive receipt bindings')
    expected={'ccc3d2ddfca98f7faaed9df323fb90ec183b437b3c6b0bfcde0820186e667023',
              'c49b7dfabe6dc8cc5b7aaea485171a6b709fc6158f180ae1157afd90b3cf4b1f',
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

    labels=['Psi5','Psi6','Psi7']+['K1_'+str(i) for i in range(1,7)]+['K0_'+str(i) for i in range(1,9)]+['K1_0-U*K0_0']
    weights=[5,6,7,13,12,11,10,9,8,15,14,13,12,11,10,9,8,19]
    caps=[25,24,23]+[12]*15
    need(face['scale']=='z=s^2; s invertible' and face['guard']=='omega=W*t5*s^8'
         and face['targets']==['K1_0-U*s^5','K0_0-s^7']
         and face['rows']==labels[:-1]+['K1_0-U*s^5','K0_0-s^7'],'full source cover')
    rows=doc['rows']
    need(type(rows) is dict and set(rows)=={'Psi','K1','K0'},'row keys')
    need(all(type(rows[k]) is list and len(rows[k])==length
             for k,length in (('Psi',3),('K1',7),('K0',9))),'all source slots')
    total_terms=0
    def source(row,h):
        nonlocal total_terms
        need(type(row) is list and len(row)<=4096,'source row cap')
        total_terms+=len(row); need(total_terms<=50000,'source aggregate cap')
        out={}; previous=None
        for pair in row:
            need(type(pair) is list and len(pair)==2,'source pair')
            ex,dense=pair
            need(type(ex) is list and len(ex)==6
                 and all(type(s) is str and s in [str(i) for i in range(17)] for s in ex),'source exponents')
            need(type(dense) is list and len(dense)==7,'source dense seven')
            e=tuple(int(s) for s in ex); values=[rat(s) for s in dense]
            need(any(values) and (previous is None or previous<e),'source canonical sparse')
            previous=e
            need(e[4]==e[5]==0 and e[0]+2*e[1]+3*e[2]+5*e[3]==h,'whole weight/support')
            # Test EVERY denominator before the fixed root and z=1 projection.
            residues=[mod(q) for q in values]
            key=(e[0],e[1],e[2])
            out[key]=(out.get(key,0)+residues[0])%89
        return {e:c for e,c in out.items() if c}
    psis=[source(row,h) for row,h in zip(rows['Psi'],(5,6,7))]
    k1=[source(row,14-i) for i,row in enumerate(rows['K1'])]
    k0=[source(row,16-i) for i,row in enumerate(rows['K0'])]
    u=source(doc['source']['U'],3)
    mixed=dict(k1[0])
    for e,c in u.items():
        for f,d in k0[0].items():
            key=(e[0]+f[0],e[1]+f[1],e[2]+f[2])
            mixed[key]=(mixed.get(key,0)-c*d)%89
    mixed={e:c for e,c in mixed.items() if c}
    generators=psis+k1[1:]+k0[1:]+[mixed]
    need(len(generators)==18,'all eighteen generators')
    def weight(e): return e[0]+2*e[1]+3*e[2]
    for gen,h in zip(generators,weights):
        need(all(weight(e)<=h and (weight(e)-h)%5==0 for e in gen),'full generator degree/class')
    cert=load(cert_raw)
    need(dump(cert)==cert_raw and type(cert) is dict and set(cert)==
         {'schema','baseline_sha256','prime','root','specialization','variables','weights','cut','modulus','cofactors'},
         'full certificate canonical keys')
    need(cert['schema']=='f10-r2-fullunit-modular89/v1' and cert['baseline_sha256']==BASE
         and cert['prime']=='89' and cert['root']=='0' and cert['specialization']=='z=1'
         and cert['variables']==['Y1','Y2','Y3'] and cert['weights']==['1','2','3']
         and cert['cut']=='30' and cert['modulus']==doc['field']['P7'],'full certificate binding')
    cof=cert['cofactors']
    need(type(cof) is list and len(cof)==18,'all cofactor slots')
    decoded=[]; count=0
    for slot,obj in enumerate(cof):
        need(type(obj) is dict and set(obj)=={'generator','terms'} and obj['generator']==labels[slot],
             'cofactor indexed label')
        terms=obj['terms']
        need(type(terms) is list and len(terms)<=754,'cofactor bound')
        count+=len(terms); need(count<=754,'total cofactor bound')
        out=[]; previous=None
        for pair in terms:
            need(type(pair) is list and len(pair)==2,'cofactor pair')
            ex,c=pair
            need(type(ex) is list and len(ex)==3
                 and all(type(s) is str and s in [str(i) for i in range(31)] for s in ex),'cofactor exponents')
            e=tuple(int(s) for s in ex)
            need(previous is None or previous<e,'cofactor order')
            previous=e
            need(type(c) is str and c in [str(i) for i in range(1,89)],'nonzero canonical residue')
            need(weight(e)<=caps[slot] and (weight(e)+weights[slot])%5==0,'cofactor degree/class')
            out.append((e,int(c)))
        decoded.append(out)
    identity={}
    for terms,gen in zip(decoded,generators):
        for e,c in terms:
            for f,d in gen.items():
                key=(e[0]+f[0],e[1]+f[1],e[2]+f[2])
                need(weight(key)<=30 and weight(key)%5==0,'whole input product bound')
                identity[key]=(identity.get(key,0)+c*d)%89
    need({e:c for e,c in identity.items() if c}=={(0,0,0):1},'input full polynomial identity')
    slot=next((i for i in range(18) if generators[i] and decoded[i]),None)
    need(slot is not None,'nonzero generator/cofactor pair')
    index=0  # EXISTING first term, never insertion of a constant.
    original=load(cert_raw)
    old_terms=original['cofactors'][slot]['terms']
    ex,old_string=cof[slot]['terms'][index]
    old_value=int(old_string); new_value=(old_value+1)%89
    if new_value:
        cof[slot]['terms'][index]=[list(ex),str(new_value)]
    else:
        del cof[slot]['terms'][index]
    changed=dump(cert)
    need(changed!=cert_raw and len(changed)<=2097152,'changed bounded bytes')
    restored=load(changed); restored['cofactors'][slot]['terms']=old_terms
    need(dump(restored)==cert_raw,'inverse restores WHOLE input bytes')
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
    for path,digest in positive['sources'].items():
        need(sha(read(path,1048576))==digest,'positive source postpin')
    write(args['--output'],changed,2097152)
    receipt={'schema':'f10-r2-fullunit-modular-mutation/v1','status':'ONE_COFACTOR_MUTATED_UNCHECKED',
             'science_outcome':'NONE','job_tag':JOB,'root_registration_sha256':args['--root-registration-sha256'],
             'sources':sources,'baseline_sha256':BASE,'baseline_bytes':'1652675',
             'input':{'path':args['--certificate'],'sha256':sha(cert_raw),'bytes':str(len(cert_raw))},
             'output':{'path':args['--output'],'sha256':sha(changed),'bytes':str(len(changed))},
             'selection':{'slot':str(slot),'generator':labels[slot],'index':str(index),
                          'exponents':list(ex),'old':old_string,'new':str(new_value),
                          'term_deleted':new_value==0,'old_length':str(len(old_terms)),
                          'new_length':str(len(cof[slot]['terms']))},
             'inverse_edit_restores_whole_input_bytes':True,'checker_run':False}
    write(args['--receipt'],dump(receipt),32768)


if __name__ == '__main__':
    main()
