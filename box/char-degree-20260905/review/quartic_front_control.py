#!/usr/bin/env python3
"""Exact leading low-digit remainder and boundary controls over Q."""
from pathlib import Path
import hashlib,json
import sympy as s
z=s.Symbol('z');records=[]
assert s.Rational(1,6)-s.Rational(9,64)==s.Rational(5,192)
for client,k,r,a,b,zpower,wpower,killed in [
 ('99_excluded_r29',33,29,24,9,26,6,True),
 ('99_allowed_r30',33,30,24,9,25,7,False),
 ('108_allowed_r33',36,33,28,8,29,6,False),
]:
 H=z**a*(1+z)**b;d=z**zpower*(1+z)**wpower
 U,rem2=s.div(d*d,H,z);P,rem3=s.div(d*U,H,z)
 assert rem2==0 and rem3==0
 R2=s.rem(d*P/6,H,z);R3=s.rem(U*U,H,z)
 low=s.expand(R2-s.Rational(9,64)*R3)
 witness=s.rem(d**4,H**3,z)
 assert (low!=0)==killed and (witness!=0)==killed
 assert s.expand(low-s.Rational(5,192)*s.rem(U*U,H,z))==0
 # E has target total degree d_target-k.
 Etarget=(5*k-3)-((55 if k==33 else 63)-k)
 Lcut=(6*k-3)-(55 if k==33 else 63)+1
 assert 3*r+1<4*k-2 and 3*r<Etarget and 4*r+1<Lcut
 assert 4*r+1<4*k-2+r and 4*r+1<6*k-3
 records.append({'client':client,'k':k,'r':r,'d':str(d),'square_divisibility':True,
   'cubic_divisibility':True,'quartic_divisibility':not killed,
   'low_band':4*r+1,'low_cut_exclusive':Lcut,'digit_band':3*r,'digit_target_band':Etarget,
   'low_remainder':str(s.factor(low)),'killed_leading_shape':killed})
# The missing extra factor at z=-1 makes the r29 degree requirement exceed32.
assert 26+s.ceiling(s.Rational(3*9,4))==33
record={'status':'PASS','field':'Q','coefficient':'5/192','controls':records,
 'proved99_cutoffs':{'D_inclusive':29,'C_inclusive':60},
 'no_additional108_cutoff':True,'scope':'necessary leading-band equations only',
 'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
