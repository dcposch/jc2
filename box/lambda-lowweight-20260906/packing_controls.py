#!/usr/bin/env python3
"""Tiny exact-Q controls of exponent storage on the actual 455-variable order."""
import pathlib,json,subprocess,hashlib,tempfile,os
P=pathlib.Path('box/lambda-lowweight-20260906')
c=next(z for z in json.loads((P/'run_cases.json').read_text()) if z['id']=='C455')
names=c['variables']+['T','Z','ss']
def weight(v):
 if v in ['T','Z','ss']:return 1
 if v=='c':return c['n']+c['m']-1
 block,b,a=v.split('_');return (1 if block=='h' else int(block[1:]))*c['K']-int(a)
w=[weight(v) for v in names];b='h_0_2';a='A1_0_3';assert names.index(b)<names.index(a)
src='ring R=0,('+','.join(names)+'),wp('+','.join(map(str,w))+');\n'
src+='list before=ringlist(R);string cfBefore=string(before[1]);string varsBefore=string(before[2]);string orderBefore=string(before[3]);list RL=before;attrib(RL,"maxExp",511);def Packed=ring(RL);setring Packed;list after=ringlist(Packed);\n'
src+='print("FIELD_EQUAL="+string(cfBefore==string(after[1])));print("VARIABLE_ORDER_EQUAL="+string(varsBefore==string(after[2])));print("ORDER_WEIGHTS_EQUAL="+string(orderBefore==string(after[3])));print("VARIABLE_COUNT="+string(nvars(Packed)));print("PACKMASK="+string(attrib(Packed,"maxExp")));\n'
src+=f'poly mon={a}^93;poly mul=mon*mon;poly direct={a}^186;print("EXP186="+string(deg(direct)));print("MULTIPLICATION_EXACT="+string(mul==direct));\n'
src+=f'ideal I={b}^2-{a}^4,{a}*{b};option(redSB);degBound=4;ideal G4=std(I);print("BOUND4_NONZERO="+string(reduce({a}^5,G4)!=0));degBound=5;ideal G5=std(I);print("BOUND5_ZERO="+string(reduce({a}^5,G5)==0));print("LOWER_NONZERO="+string(reduce({a}^4,G5)!=0));print("IDENTITY="+string({a}^5-(-{a}*({b}^2-{a}^4)+{b}*({a}*{b}))==0));degBound=0;ideal GP=std(I);\n'
src+=f'setring R;ideal ID={b}^2-{a}^4,{a}*{b};ideal GD=std(ID);ideal mapped=imap(Packed,GP);print("EXACT_BASES_EQUAL="+string(size(reduce(GD,mapped))==0 && size(reduce(mapped,GD))==0));quit;\n'
r=subprocess.run(['/usr/bin/time','-f','PEAK_KIB=%M','Singular','-q'],input=src,text=True,capture_output=True,timeout=30)
assert r.returncode==0 and '?' not in r.stdout and all(k+'=1' in r.stdout for k in ['FIELD_EQUAL','VARIABLE_ORDER_EQUAL','ORDER_WEIGHTS_EQUAL','MULTIPLICATION_EXACT','BOUND4_NONZERO','BOUND5_ZERO','LOWER_NONZERO','IDENTITY','EXACT_BASES_EQUAL']),r.stdout
assert 'VARIABLE_COUNT=458' in r.stdout and 'PACKMASK=511' in r.stdout and 'EXP186=186' in r.stdout
out={'status':'PASS','installed_backend':'Singular 4.3.2 x86_64','syntax':'list RL=ringlist(R); attrib(RL,"maxExp",511); def Packed=ring(RL); setring Packed; emit every polynomial only now','variables':458,'source_variable_order_sha256':hashlib.sha256(json.dumps(names).encode()).hexdigest(),'source_weights_sha256':hashlib.sha256(json.dumps(w).encode()).hexdigest(),'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'emitted_control_sha256':hashlib.sha256(src.encode()).hexdigest(),'stdout':r.stdout,'stderr':r.stderr,'storage_mask':511,'safe_power_guard_capacity':255,'largest_requested_B':93,'conservative_intermediate_exponent_bound':186,'degree_argument':'All selected generators are homogeneous of positive weighted degree <=B. Required S-polynomials and all reductions remain at weight <=B. Pair lcm weights before rejection are <=2B, and even temporary products from these pairs have exponents <=2B<=186. The 511 mask has signed power-guard capacity255. No exponent is truncated or quotiented. Reject any OVERFLOW/error; never interpret it as zero.','packing_estimate':'For 458 variables on 64-bit: 16-bit default stores4 exponents/word; 9-bit mask511 stores7. Exponent-array words fall from ceil(458/4)=115 to ceil(458/7)=66, excluding fixed overhead. Total RSS reduction is not guaranteed.','primary_sources':['https://github.com/Singular/Singular/blob/spielwiese/doc/reference.doc','https://github.com/Singular/Singular/blob/spielwiese/libpolys/polys/monomials/ring.cc','https://github.com/Singular/Singular/blob/spielwiese/kernel/GBEngine/kstd2.cc']}
fd,tmp=tempfile.mkstemp(prefix='.packing-controls-',dir=P)
with os.fdopen(fd,'w') as f:json.dump(out,f,indent=1);f.write('\n');f.flush();os.fsync(f.fileno())
os.replace(tmp,P/'packing-controls.json');print(r.stdout,r.stderr)
