#!/usr/bin/env python3
"""Fail-stop p-integrality and exact-row provenance audit for the t=8 gate.

All input files are read-only.  Arithmetic uses Python integers/Fraction.
The complete row syntax is checked to allow division only by integer literals.
The pivot checker evaluates its short arithmetic AST with Fraction, never eval.
"""
import ast
import hashlib
import json
import pathlib
import re
from fractions import Fraction

ROOT = pathlib.Path('/home/ubuntu/jc2')
OUT = ROOT / 'box/k16-t8-gate-20260905'
ROWS = ROOT / 'box/k16rank-20260903/terminal_t8_exact_none.out'
RANK = ROOT / 'box/k16rank-20260903/rank_t8_mod_p32003_b0_parti.sing'
AFFINE = ROOT / 'box/k16t8-20260905/affinewms2_t8_mod_p32003_b0.sing'
PRIMES = [(32003,11288),(32027,23825)]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def short_fraction(expression, yy):
    def visit(node):
        if isinstance(node,ast.Expression): return visit(node.body)
        if isinstance(node,ast.Constant) and isinstance(node.value,int): return Fraction(node.value)
        if isinstance(node,ast.Name) and node.id=='yy': return Fraction(yy)
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub): return -visit(node.operand)
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.UAdd): return visit(node.operand)
        if isinstance(node,ast.BinOp):
            a,b=visit(node.left),visit(node.right)
            if isinstance(node.op,ast.Add): return a+b
            if isinstance(node.op,ast.Sub): return a-b
            if isinstance(node.op,ast.Mult): return a*b
            if isinstance(node.op,ast.Div): return a/b
            if isinstance(node.op,ast.Pow):
                assert b.denominator==1
                return a**b.numerator
        raise AssertionError(ast.dump(node))
    return visit(ast.parse(expression.replace('^','**'), mode='eval'))

def residue(value,p):
    assert value.denominator % p, 'NONINTEGRAL coefficient'
    return value.numerator * pow(value.denominator,-1,p) % p

def scan_denominators(expression):
    # Printed rows use rational scalar coefficients times monomials. Every
    # slash must introduce an integer token, followed by a token boundary.
    assert re.fullmatch(r'[\dA-Za-z_+*/^()\-\s]+',expression)
    names=set(re.findall(r'[A-Za-z_]\w*',expression))
    assert names <= {'yy','b3','b4',*(f'q{i}_0' for i in range(2,8))},names
    matches=list(re.finditer(r'/([0-9]+)(?=[*+\-()\s]|$)',expression))
    assert len(matches)==expression.count('/'), 'unclassified denominator syntax'
    return [int(m.group(1)) for m in matches]

lines=ROWS.read_text().splitlines()
assert 'RECURRENCE_PASS t=8 rows=16' in lines and 'DRIVER_DONE' in lines
rows={}
pivots=[]
for i,line in enumerate(lines):
    m=re.fullmatch(r'TROW band=(\d+)',line)
    if m: rows[int(m[1])]=lines[i+1].strip()
    m=re.fullmatch(r'PIVOT weight=(\d+) band=(\d+) variable=(\w+)',line)
    if m: pivots.append((int(m[1]),int(m[2]),m[3],lines[i+1].strip()))
assert set(rows)==set(range(16))
assert [x[0] for x in pivots]==list(range(1,18))
assert [x[1] for x in pivots]==list(range(32,15,-1))
assert [x[2] for x in pivots]==[*(f'C{i}' for i in range(1,8)),*(f'q{i}_0' for i in range(8,17)),'b2']

row_stats=[]
all_denominators=[]
for k,row in sorted(rows.items()):
    ds=scan_denominators(row)
    all_denominators.extend(ds)
    row_stats.append({'band':k,'sha256':hashlib.sha256(row.encode()).hexdigest(),
                      'denominator_occurrences':len(ds)})

maps=[]
for path in (RANK,AFFINE):
    rr={}
    for line in path.read_text().splitlines():
        m=re.fullmatch(r'poly T(\d+)=(.*);',line)
        if m: rr[int(m[1])]=m[2]
    assert set(rr)==set(range(8,16)),(path,set(rr))
    assert all(rr[k]==rows[k] for k in rr),'EXACT ROW MISMATCH'
    maps.append({'path':str(path.relative_to(ROOT)),'sha256':sha(path),
                 'top_rows_identical_to_exact_dump':list(sorted(rr))})

result={'status':'PASS','exact_rows_file':str(ROWS.relative_to(ROOT)),
        'exact_rows_sha256':sha(ROWS),'row_stats':row_stats,
        'all_row_denominator_occurrences':len(all_denominators),
        'all_row_unique_denominators':len(set(all_denominators)),
        'top_row_denominator_occurrences':sum(x['denominator_occurrences'] for x in row_stats if x['band']>=8),
        'input_maps':maps,'primes':[]}

for p,r in PRIMES:
    assert all(p%d for d in range(2, int(p**0.5)+1)), 'COMPOSITE PRIME'
    assert (3468*r*r-1836*r+234)%p==0
    assert (6936*r-1836)%p!=0
    assert 124848%p!=0 and p>67
    assert all(d%p for d in all_denominators), 'ROW DENOMINATOR NOT UNIT'
    g=Fraction(200,289)*r-Fraction(1800,29478)
    base={'yy':r,'q':17,'2q^2':578,'6q^3':29478,'2':2,
          'g':residue(g,p),'y*g':residue(r*g,p),'q/y':residue(Fraction(17,r),p)}
    assert all(v%p for v in base.values())
    pp=[]
    for weight,band,var,expr in pivots:
        ds=re.findall(r'/([0-9]+)',expr)
        assert len(ds)==expr.count('/') and all(int(d)%p for d in ds)
        value=residue(short_fraction(expr,r),p)
        assert value, ('ZERO PIVOT',p,weight,var)
        pp.append({'weight':weight,'band':band,'variable':var,'value':value})
    result['primes'].append({'p':p,'yy':r,'H_value':0,
       'H_derivative':(6936*r-1836)%p,'H_discriminant_mod_p':124848%p,
       'fixed_integer_denominator_bound':67,'base_units':base,
       'row_denominators_all_units':True,'spine_pivots':pp,'status':'PINT PASS'})

(OUT/'rank-pintegrality.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
