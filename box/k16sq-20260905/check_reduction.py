#!/usr/bin/env python3
"""Verify that the mod-p row file is the reduction of the exact row file modulo (p, d - droot).
Parses Singular polynomial strings: coefficients are rationals or (a/b*d+c/e) with d the field generator."""
import re, sys
from fractions import Fraction
tag, ptag, p, droot = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
D='/home/ubuntu/jc2/box/k16sq-20260905/'
def polys(fn):
    out={}
    for line in open(fn):
        m=re.match(r'poly (\w+)=(.*);$', line.strip())
        if m: out[m.group(1)]=m.group(2)
    return out
def terms(s):
    # split top-level '+'/'-' outside parentheses
    res=[]; cur=''; depth=0
    for ch in s:
        if ch=='(': depth+=1
        if ch==')': depth-=1
        if ch in '+-' and depth==0 and cur not in ('',):
            res.append(cur); cur=ch
        else: cur+=ch
    res.append(cur); return [r for r in res if r]
def modinv(a,p): return pow(a%p,p-2,p)
def frac_mod(fs,p):
    f=Fraction(fs); return (f.numerator%p)*modinv(f.denominator,p)%p
def coef_mod(cs,p,droot):
    cs=cs.strip()
    if cs.startswith('('): cs=cs[1:-1]
    # sum of pieces like a/b*d, a/b, -c
    tot=0
    for piece in terms(cs):
        if 'd' in piece:
            num=piece.replace('*d','').replace('d','') or '1'
            if num in ('+','-'): num+='1'
            tot+=frac_mod(num,p)*droot
        else: tot+=frac_mod(piece,p)
    return tot%p
def parse(s,p,droot):
    mon={}
    for tm in terms(s):
        sign=1
        if tm.startswith('-'): sign=-1; tm=tm[1:]
        elif tm.startswith('+'): tm=tm[1:]
        # coefficient part: leading parenthesised or numeric
        if tm.startswith('('):
            k=tm.index(')'); c=coef_mod(tm[:k+1],p,droot); rest=tm[k+1:].lstrip('*')
        else:
            m=re.match(r'^(-?\d+(?:/\d+)?)(?:\*)?(.*)$',tm)
            if m and m.group(1) and (m.group(2)=='' or not m.group(1)[-1:].isalpha()):
                c=frac_mod(m.group(1),p); rest=m.group(2)
            else: c=1; rest=tm
        c=(sign*c)%p
        mon[rest]=(mon.get(rest,0)+c)%p
    return {k:v for k,v in mon.items() if v}
def parse_modp(s,p):
    mon={}
    for tm in terms(s):
        sign=1
        if tm.startswith('-'): sign=-1; tm=tm[1:]
        elif tm.startswith('+'): tm=tm[1:]
        m=re.match(r'^(\d+)\*(.*)$',tm)
        if m: c=int(m.group(1)); rest=m.group(2)
        else:
            m2=re.match(r'^(\d+)$',tm)
            if m2: c=int(m2.group(1)); rest=''
            else: c=1; rest=tm
        mon[rest]=(mon.get(rest,0)+sign*c)%p
    return {k:v for k,v in mon.items() if v}
E=polys(D+tag+'_rows.sing'); P=polys(D+ptag+'_rows.sing')
ok=True
for name in sorted(E):
    if name not in P: print("missing in modp:",name); ok=False; continue
    a=parse(E[name],p,droot); b=parse_modp(P[name],p)
    same=(a==b)
    print(f"{name}: exact_terms={len(a)} modp_terms={len(b)} REDUCTION_EQUAL={same}")
    ok=ok and same
print("ALL_ROWS_REDUCE_CORRECTLY", ok)
