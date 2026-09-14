"""Exactly four ROOT-authorized semantic mutations; STATIC/UNEXECUTED."""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import sys
import authority

ORIGINAL_SHA = '219151792c8ffbbaab2e745fa60bd72e9c05c705fcc2ded992bcd97badf05470'
ORIGINAL_BYTES = 854264
POSITIVE_RECEIPT_SHA = '1a9bb0f58e96fa5a0be086e72a725f3e1f7eabad89248888c3d8acc13323cf44'
FIXTURES = [('U','positive V cancellation'),('R','full cofactor identity'),
            ('j','wrong maximal excluded-edge factor'),('bernstein','full Bernstein expansion')]
Fraction = None

def need(ok, message):
    if not ok:
        raise ValueError(message)

def rational(wire):
    need(Fraction is not None,'authorize before arithmetic')
    need(type(wire) is list and len(wire)==2,'rational pair shape')
    for value in wire:
        need(type(value) is str and len(value)<=4096 and re.fullmatch(r'(0|-?[1-9][0-9]*)',value),
             'canonical rational decimal strings')
    n,d=int(wire[0]),int(wire[1]); need(d>0,'positive denominator')
    value=Fraction(n,d)
    need(value.numerator==n and value.denominator==d,'canonical reduced rational')
    return value

def plus_one(wire):
    value=rational(wire)+1
    need(max(abs(value.numerator).bit_length(),value.denominator.bit_length())<=12000,
         'mutation would leave accepted coefficient bound')
    return [str(value.numerator),str(value.denominator)]

def change_constant(poly):
    need(type(poly) is list,'polynomial wire shape')
    position=None
    for i,term in enumerate(poly):
        if term[0]==['0','0','0']:
            need(position is None,'duplicate constant term')
            position=i
    if position is None:
        poly.insert(0,[['0','0','0'],['1','1']])
        return
    changed=plus_one(poly[position][1])
    if changed==['0','1']:
        del poly[position]
    else:
        poly[position][1]=changed

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--job',required=True)
    parser.add_argument('--registration',required=True)
    parser.add_argument('--input',required=True)
    parser.add_argument('--positive-receipt',required=True)
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--receipt',required=True)
    a=parser.parse_args()
    folder=pathlib.Path(a.output_dir)
    outputs=[pathlib.Path(a.receipt)]+[folder/('mutated-'+name+'.json') for name,_ in FIXTURES]
    permit=authority.authorize('mutate',a.job,a.registration,[str(p) for p in outputs],a.input)
    # No Fraction import, coefficient parse, or mutation precedes accepted authorization.
    global Fraction
    from fractions import Fraction as ExactFraction
    Fraction=ExactFraction
    baseline_path=authority.regular(a.input)
    receipt_path=authority.regular(a.positive_receipt)
    need(permit['pins'].get(str(receipt_path))==POSITIVE_RECEIPT_SHA,'positive receipt authority pin')
    need(baseline_path.stat().st_size==ORIGINAL_BYTES and authority.digest(baseline_path)==ORIGINAL_SHA,
         'literal baseline hash/size')
    need(receipt_path.stat().st_size<=4096 and authority.digest(receipt_path)==POSITIVE_RECEIPT_SHA,
         'literal positive receipt hash')
    positive=authority.strict_json(receipt_path.read_bytes(),wire=True)
    expected_code=authority.code_pins()
    need(positive.get('schema')=='f10-middle-real-check/v1' and positive.get('status')=='CERTIFIED_NONRESONANCE'
         and positive.get('input_sha256')==ORIGINAL_SHA and positive.get('code')==expected_code
         and positive.get('j')=='4' and positive.get('degree_t')=='36' and positive.get('degree_s')=='21',
         'positive baseline metadata binding')
    raw=baseline_path.read_bytes()
    need(hashlib.sha256(raw).hexdigest()==ORIGINAL_SHA,'exact bytes read baseline hash')
    data=authority.strict_json(raw,wire=True)
    need(type(data) is dict and data.get('schema')=='f10-middle-real-certificate/v1'
         and data.get('status')=='CANDIDATE' and data.get('science')==authority.SCIENCE
         and data.get('code')==expected_code and data.get('j')=='4','literal baseline wire binding')
    bern=data['bernstein']
    need(bern['degree_t']=='36' and bern['degree_s']=='21' and len(bern['coefficients'])==37
         and all(len(row)==22 for row in bern['coefficients']),'actual interior/dense envelope')
    fixture_records=[]
    for name,reason in FIXTURES:
        changed=copy.deepcopy(data)
        if name in ('U','R'):
            change_constant(changed['polynomials'][name])
            need(len(changed['polynomials'][name])<=20000,'mutation would leave accepted term bound')
        elif name=='j':
            changed['j']='5'
        else:
            changed['bernstein']['coefficients'][1][1]=plus_one(changed['bernstein']['coefficients'][1][1])
        need(changed!=data,'mutation must actually differ')
        path=folder/('mutated-'+name+'.json')
        authority.postcheck(permit)
        digest,size=authority.emit(path,changed,authority.LIMIT-4096)
        emitted=path.read_bytes()
        need(hashlib.sha256(emitted).hexdigest()==digest and digest!=ORIGINAL_SHA,'changed exact fixture hash')
        need(authority.strict_json(emitted,wire=True)==changed,'full changed fixture read-back')
        # Reconstruct baseline by undoing the single chosen field/subtree, ensuring no other semantic edit.
        restored=copy.deepcopy(changed)
        if name in ('U','R'): restored['polynomials'][name]=data['polynomials'][name]
        elif name=='j': restored['j']=data['j']
        else: restored['bernstein']['coefficients'][1][1]=data['bernstein']['coefficients'][1][1]
        need(restored==data,'only prescribed mutation permitted')
        fixture_records.append({'name':name,'path':str(path),'sha256':digest,'bytes':str(size),
                                'expected_error':reason,'changed':True,'readback':'EXACT'})
    authority.postcheck(permit)
    result={'schema':'f10-middle-real-mutator/v1','status':'FOUR_CHANGED_FIXTURES',
            'original_sha256':ORIGINAL_SHA,'positive_receipt_sha256':POSITIVE_RECEIPT_SHA,
            'code':expected_code,'mutator_sha256':authority.digest(pathlib.Path(__file__).resolve()),
            'fixtures':fixture_records,'scope':'semantic controls only; no theorem or positive rerun'}
    authority.emit(a.receipt,result,8192)
    print('FOUR_CHANGED_FIXTURES')
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (ValueError,TypeError,KeyError,RuntimeError,OSError,ArithmeticError,MemoryError,RecursionError) as exc:
        print('INCONCLUSIVE: '+str(exc)[:400],file=sys.stderr)
        raise SystemExit(2)
