"""Two fixed contact-certificate corruptions. STATIC; metadata authorization first."""
import argparse
import copy
import hashlib
import json
import os
import pathlib
import re
import sys
import authority

JOB = 'f10-contact-gram-certificate-20260910'
CODE = {
    'authority.py': '96ca421fe8d82f7035161d35c325db2e1433346db0101ab6bfffe9da6984a141',
    'producer.py': 'afc617ae797661df8cbb1ca1d8a00825a6c607e1fb854754c0230376965f74ee',
    'checker.py': 'ceca0a07f1b2f6433de87bb7327280cb1165703ea9196f6d7e37b953a8631b06'}
BOUNDS = {'R_weight':'52','cofactor_weight':'64','U0_V':'3','U1_V':'3',
          'Uphi_V':'5','rectangle_t':'52','rectangle_v':'52'}
F = None
MAX_BITS = 12000
MAX_TERMS = 20000
RECEIPT_LIMIT = 32768

def need(ok, reason):
    if not ok:
        raise ValueError(reason)

def canonical(obj):
    return (json.dumps(obj,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()

def integer(s, signed=True):
    pattern = r'(0|-?[1-9][0-9]*)' if signed else r'(0|[1-9][0-9]*)'
    need(type(s) is str and len(s)<=4096 and re.fullmatch(pattern,s), 'canonical decimal')
    return int(s)

def rational(pair):
    need(type(pair) is list and len(pair)==2, 'rational pair')
    n,d=integer(pair[0]),integer(pair[1],False)
    need(d>0 and max(abs(n).bit_length(),d.bit_length())<=MAX_BITS,'rational bound')
    f=F(n,d)
    need(f.numerator==n and f.denominator==d,'reduced rational')
    return f

def plus_one(pair):
    f=rational(pair)+1
    need(max(abs(f.numerator).bit_length(),f.denominator.bit_length())<=MAX_BITS,
         'fixed mutation unavailable: coefficient cap')
    result=[str(f.numerator),str(f.denominator)]
    need(max(map(len,result))<=4096,'fixed mutation unavailable: decimal cap')
    return result

def validate(doc):
    keys={'schema','status','reason','science','code','variables','bounds','polynomials','j','bernstein'}
    need(type(doc) is dict and set(doc)==keys and doc['schema']=='f10-contact-gram-certificate/v1','wire schema')
    need(doc['science']==authority.SCIENCE and doc['code']==CODE,'wire science/code')
    need(doc['variables']==['s','p','V'] and doc['bounds']==BOUNDS,'wire bounds')
    need(doc['status'] in ('CANDIDATE','INCONCLUSIVE') and type(doc['reason']) is str
         and len(doc['reason'])<=400,'wire status')
    polys=doc['polynomials']
    need(type(polys) is dict and set(polys)=={'R','U0','U1','Uphi'},'polynomial inventory')
    for name,terms in polys.items():
        need(type(terms) is list and len(terms)<=MAX_TERMS,'term cap')
        prev=None
        for term in terms:
            need(type(term) is list and len(term)==2 and type(term[0]) is list
                 and len(term[0])==3,'term shape')
            e=tuple(integer(k,False) for k in term[0])
            need(prev is None or prev<e,'sorted unique terms')
            prev=e
            need(e[0]+2*e[1]+e[2]<=(52 if name=='R' else 64)
                 and e[2]<={'R':0,'U0':3,'U1':3,'Uphi':5}[name],'term envelope')
            need(rational(term[1])!=0,'zero sparse term')
    j=integer(doc['j'],False)
    need(0<=j<=52,'edge order')
    bern=doc['bernstein']
    need(type(bern) is dict and set(bern)=={'degree_t','degree_v','coefficients'},'dense schema')
    need(integer(bern['degree_t'],False)==52-j and bern['degree_v']=='52','dense degrees')
    rows=bern['coefficients']
    need(type(rows) is list and len(rows)==53-j,'dense row count')
    for row in rows:
        need(type(row) is list and len(row)==53,'dense column count')
        for pair in row:
            rational(pair)

def emit(path,raw):
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o444)
    with os.fdopen(fd,'wb') as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        os.fchmod(stream.fileno(),0o444)
    need(pathlib.Path(path).read_bytes()==raw,'mutation byte readback')

def main():
    p=argparse.ArgumentParser()
    for name in ('job','registration','input','positive-receipt','uphi','bernstein','receipt'):
        p.add_argument('--'+name,required=True)
    a=p.parse_args()
    outputs=[a.uphi,a.bernstein,a.receipt]
    permit=authority.authorize('mutate',a.job,a.registration,outputs,a.input)
    need(a.job==JOB and authority.code_pins()==CODE,'fixed installed code')
    own=str(pathlib.Path(__file__).resolve())
    need(permit['pins'].get(own)==authority.digest(own),'mutator self pin')
    positive=authority.regular(a.positive_receipt)
    need(permit['pins'].get(str(positive))==authority.digest(positive),'positive receipt pin')
    need(positive.stat().st_size<=4096,'positive receipt bound')
    result=authority.strict_json(positive.read_bytes())
    need(result.get('schema')=='f10-contact-gram-check/v1'
         and result.get('status')=='PRESCRIBED_CONTACT_EXCLUDED_BY_CERTIFICATE'
         and result.get('code')==CODE,'positive receipt status/code')
    source=authority.regular(a.input)
    need(source.stat().st_size<=authority.LIMIT-4096,'input size')
    raw=source.read_bytes()
    original_sha=hashlib.sha256(raw).hexdigest()
    need(original_sha==permit['pins'][str(source)]
         and result.get('input_sha256')==original_sha,'positive raw input binding')
    global F
    from fractions import Fraction
    F=Fraction
    doc=authority.strict_json(raw,wire=True)
    validate(doc)
    need(canonical(doc)==raw,'whole original canonical bytes')
    first=copy.deepcopy(doc)
    terms=first['polynomials']['Uphi']
    exists=bool(terms and terms[0][0]==['0','0','0'])
    old=copy.deepcopy(terms[0][1]) if exists else ['0','1']
    new=plus_one(old)
    deleted=new==['0','1']
    if exists:
        if deleted:
            del terms[0]
        else:
            terms[0][1]=new
    else:
        need(len(terms)<MAX_TERMS,'fixed mutation unavailable: term cap')
        terms.insert(0,[['0','0','0'],new])
    validate(first)
    first_raw=canonical(first)
    first['polynomials']['Uphi']=copy.deepcopy(doc['polynomials']['Uphi'])
    need(canonical(first)==raw,'whole cofactor inverse restoration')
    second=copy.deepcopy(doc)
    # One fixed EXISTING entry, no coefficient search or alternate control.
    old_bern=copy.deepcopy(second['bernstein']['coefficients'][0][0])
    new_bern=plus_one(old_bern)
    second['bernstein']['coefficients'][0][0]=new_bern
    validate(second)
    second_raw=canonical(second)
    second['bernstein']['coefficients'][0][0]=old_bern
    need(canonical(second)==raw,'whole Bernstein inverse restoration')
    sha1=hashlib.sha256(first_raw).hexdigest()
    sha2=hashlib.sha256(second_raw).hexdigest()
    need(len({original_sha,sha1,sha2})==3,'genuine distinct mutations')
    receipt={'schema':'f10-contact-gram-mutations/v1','status':'TWO_MUTATIONS_PREPARED_NO_SCIENCE',
             'input_sha256':original_sha,'input_bytes':len(raw),'code':CODE,
             'science':authority.SCIENCE,'mutator_sha256':permit['pins'][own],
             'positive_receipt_sha256':permit['pins'][str(positive)],
             'registration_sha256':permit['registration_sha256'],
             'variants':[
                 {'control':'Uphi+1','path':a.uphi,'sha256':sha1,'bytes':len(first_raw),
                  'constant_existed':exists,'term_deleted':deleted,'old':old,'new':new},
                 {'control':'Bernstein+1','path':a.bernstein,'sha256':sha2,'bytes':len(second_raw),
                  'row':0,'column':0,'old':old_bern,'new':new_bern}],
             'whole_byte_inverse_restored':True}
    rr=canonical(receipt)
    need(len(rr)<=RECEIPT_LIMIT,'mutation receipt bound')
    need(max(len(first_raw),len(second_raw))<=authority.LIMIT-4096,'variant wire bound')
    need(len(raw)+len(first_raw)+len(second_raw)+len(rr)<=authority.LIMIT,'triple artifact budget')
    parents={str(pathlib.Path(v).parent) for v in outputs}
    need(len(parents)==1,'one writer directory')
    parent=pathlib.Path(next(iter(parents)))
    fs=os.statvfs(parent)
    need(fs.f_bavail*fs.f_frsize>=len(first_raw)+len(second_raw)+len(rr)+65536,
         'fixed mutation unavailable: actual aggregate space')
    authority.postcheck(permit)
    emit(a.uphi,first_raw); emit(a.bernstein,second_raw)
    authority.postcheck(permit)
    emit(a.receipt,rr)
    fd=os.open(parent,os.O_RDONLY); os.fsync(fd); os.close(fd)
    print('TWO_MUTATIONS_PREPARED_NO_SCIENCE')
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (ValueError,TypeError,KeyError,RuntimeError,ArithmeticError,MemoryError,OSError) as exc:
        print('INCONCLUSIVE: '+str(exc)[:400],file=sys.stderr)
        raise SystemExit(2)
