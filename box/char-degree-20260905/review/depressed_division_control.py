#!/usr/bin/env python3
"""Exact identities for the reduced four-division characteristic emitter."""
import hashlib
import json
from pathlib import Path
import subprocess
import sympy as s

HERE=Path(__file__).resolve().parent
h,D,C,a,b,c,d,e=s.symbols('h D C a b c d e')
F=h**3+(3*D+a)*h/2+C
G=h**2-b*h/3+D
original=s.expand(G**3-F**2+a*G**2+b*F*G+c*F+d*G+e)
HH=h-b/6
A=a+b*b/4
dd=d+b*c/2
p=dd-A*A/3
q=e+c*c/4-A*dd/3+2*A**3/27
v=D+a/3+b*b/18
V=C-b*D/4+a*b/12+b**3/54-c/2
depressed=-2*V*HH**3+(3*v*v/4+p)*HH**2-3*v*V*HH+v**3-V*V+p*v+q
assert s.expand(original-depressed)==0

H,v,U,R,P,R1,Q,R2,W,R3,p,q=s.symbols('H v U R P R1 Q R2 W R3 p q')
before=-3*U*H**3/4+(3*v*v/4+p)*H**2-9*v*U*H/8+v**3-9*U*U/64+p*v+q
upper=3*R/4+p-P/8
digit=Q-R1/8-9*W/64
low=R2-9*R3/64+p*v+q
reduced=upper*H**2+digit*H+low
certificate=(3*H**2/4+v)*(v*v-U*H-R)-H*(v*U-P*H-R1)/8+(v*R-Q*H-R2)-9*(U*U-W*H-R3)/64
assert s.expand(before-reduced-certificate)==0

# Test both parser spellings on the actual local Singular binary. The unsafe
# one must be rejected; the rational prefix is the valid exact expression.
unsafe='ring R=0,(b),dp;poly h=b^2/4;quit;\n'
safe='ring R=0,(b),dp;poly h=(1/4)*b^2;print(h);quit;\n'
bad=subprocess.run(['Singular','-q'],input=unsafe,text=True,capture_output=True)
good=subprocess.run(['Singular','-q'],input=safe,text=True,capture_output=True)
assert 'failed' in bad.stdout and '?' in bad.stdout
assert '?' not in good.stdout and '1/4b2' in good.stdout
(HERE/'singular_fractional_power_negative.out').write_text(bad.stdout+bad.stderr)
(HERE/'singular_rational_prefix_positive.out').write_text(good.stdout+good.stderr)

record={
    'field':'Q','depressed_translation_identity':True,'four_division_identity':True,
    'exact_difference_certificate':str(certificate),
    'division_relations':[str(v*v-U*H-R),str(v*U-P*H-R1),str(v*R-Q*H-R2),str(U*U-W*H-R3)],
    'upper_digit':str(upper),'H_digit':str(digit),'constant_digit':str(low),
    'degree_hypotheses':'H monic deg_y k; deg_y v,V < k; k<characteristic_degree<2k',
    'leader_rule':'deg_y H_digit=characteristic_degree-k, with scalar unit leader',
    'characteristic_cases':[{'k':33,'degree':55,'digit_degree':22},{'k':36,'degree':63,'digit_degree':27}],
    'unsafe_singular_power_rejected':True,'rational_prefix_positive_control':True,
    'self_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'depressed_division_control.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
