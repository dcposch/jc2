#!/usr/bin/env python3
"""Exact, independent restricted boundary check; never edits source rows."""
from pathlib import Path
import re

out = Path(__file__).resolve().parent
src = Path('/home/ubuntu/jc2/box/k16rank-20260903/terminal_t8_exact_none.out')
lines = src.read_text().splitlines()
rows = {}
for i, line in enumerate(lines):
    m = re.fullmatch(r'TROW band=(\d+)', line)
    if m:
        rows[int(m.group(1))] = lines[i+1]
assert len(rows) == 16
mapping = {'b4':'0', 'q2_0':'0', 'q3_0':'1', 'q4_0':'0', 'q5_0':'0', 'q6_0':'z', 'q7_0':'0'}
def restrict(poly):
    return re.sub(r'\b(?:b4|q[2-7]_0)\b', lambda m: '('+mapping[m.group(0)]+')', poly)
job = ['ring R=(0,yy),(z,b3),dp;', 'minpoly=3468*yy^2-1836*yy+234;', 'option(redSB);']
for r in range(8):
    job += [f'poly T{r}={restrict(rows[15-r])};',
            f'poly aa{r}=subst(diff(diff(T{r},b3),b3),b3,0)/2;',
            f'poly bb{r}=subst(diff(T{r},b3),b3,0);',
            f'poly cc{r}=subst(T{r},b3,0);',
            f'if(T{r}-aa{r}*b3^2-bb{r}*b3-cc{r}!=0){{print("FAIL quadratic");}}']
for r in range(1,8):
    job += [f'poly B{r}=aa0*bb{r}-aa{r}*bb0;', f'poly C{r}=aa0*cc{r}-aa{r}*cc0;',
            f'print("SUPPORT r={r} Bzero="+string(B{r}==0)+" Czero="+string(C{r}==0));']
job += ['poly D=B3*C6-B6*C3;',
        'print("EXACT_BOUNDARY_MINOR_DEG="+string(deg(D)));',
        'poly Ds=gcd(D,diff(D,z));',
        'print("EXACT_BOUNDARY_GCD_DEG="+string(deg(Ds)));',
        'print("EXACT_BOUNDARY_CONSTANT_NONZERO="+string(subst(D,z,0)!=0));',
        'print("EXACT_A0_NONZERO="+string(aa0!=0));',
        'poly Bcommon=gcd(gcd(D,B3),B6);',
        'print("EXACT_BOUNDARY_BCOMMON_DEG="+string(deg(Bcommon)));',
        'poly W3=aa0*C3^2-bb0*B3*C3+cc0*B3^2;',
        'poly W6=aa0*C6^2-bb0*B6*C6+cc0*B6^2;',
        'poly Wcommon=gcd(gcd(D,W3),W6);',
        'print("EXACT_BOUNDARY_WCOMMON_DEG="+string(deg(Wcommon)));',
        'write(":w '+str(out / 'exact_boundary_minor.txt')+'",string(D/leadcoef(D)));',
        'print("EXACT_BOUNDARY_RESTRICTION_DONE");', 'quit;']
(out/'exact_boundary_restriction.sing').write_text('\n'.join(job)+'\n')
