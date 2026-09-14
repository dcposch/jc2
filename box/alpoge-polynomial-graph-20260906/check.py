#!/usr/bin/env python3
"""Tiny exact controls for a degree-uniform proof, not an ansatz search."""
import argparse
import ast
import json
from pathlib import Path
import resource

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
import sympy as s

args = argparse.ArgumentParser()
args.add_argument('--mutate', action='store_true')
opt = args.parse_args()
x, y, z = s.symbols('x y z')
P = (1+x*y)**3*z+y**2*(1+x*y)*(4+3*x*y)
Q = y+3*x*(1+x*y)**2*z+3*x*y**2*(4+3*x*y)
R = 2*x-3*x**2*y-x**3*z

def require(condition, label):
    if not condition:
        raise RuntimeError('CHECK_FAILED: '+label)

def jac(a,b,u=x,v=y):
    return s.expand(s.diff(a,u)*s.diff(b,v)-s.diff(a,v)*s.diff(b,u))

def top(a):
    p = s.Poly(s.expand(a),x,y)
    d = p.total_degree()
    return s.expand(sum(c*x**i*y**j for (i,j),c in p.terms() if i+j==d))

def check(H, mutate=False):
    d = max(0,s.Poly(H,x,y).total_degree())
    T = x**3*top(H) if d else x**2*(H*x+3*y)
    values = [s.expand(f.subs(z,H)) for f in (P,Q,R)]
    require([top(a) for a in values]==[s.expand(a) for a in (y**3*T,3*y**2*T,-T)], 'three top forms')
    common=s.expand(T*s.diff(T,x))
    expected=[s.expand(-3*y**4*common),s.expand(3*y**2*common),s.expand(6*y*common)]
    minors=[jac(values[0],values[1]),jac(values[0],values[2]),jac(values[1],values[2])]
    if mutate:
        # Actual altered operator: suppress both graph-chain derivatives.
        minors[0]=jac(P,Q).subs(z,H).expand()
    require([top(a) for a in minors]==expected,'graph-chain minor leading forms')
    require([s.Poly(a,x,y).total_degree() for a in minors]==[2*d+9,2*d+7,2*d+6], 'distinct positive degrees')
    return {'H':str(H),'d':int(d),'minor_degrees':[2*d+9,2*d+7,2*d+6]}

require(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'no stripped assertion checks')
rows=[check(H) for H in (s.Integer(0),s.Integer(1),-2*x+3*y+1,x**2+y)]
require(jac(P.subs(x,0),Q.subs(x,0),y,z)==-1,'other graph orientation is not excluded')
require(s.expand(x**3*(-3*y/x)+3*x**2*y)==0,'rational graph can erase the polynomial leader')
if opt.mutate:
    check(x**2+y,mutate=True)
print(json.dumps({'status':'GRAPH_LEADING_CONTROLS_PASS','cases':rows,'x_zero_orientation_J':-1,'proof_is_degree_uniform_not_sampling':True},sort_keys=True))
