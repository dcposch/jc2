"""Tiny formal identity control; never constructs a K16 source polynomial."""
import ast
import json
from fractions import Fraction as F
from pathlib import Path
import resource
import signal
import sys
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
signal.alarm(30)
N = 4
def need(ok, message):
    if not ok:
        raise ValueError(message)
def const(c):
    return {(0,)*N: F(c)} if c else {}
def var(i):
    key = tuple(int(j == i) for j in range(N))
    return {key: F(1)}
def add(*items):
    result = {}
    for p in items:
        for e,c in p.items():
            result[e] = result.get(e, F(0)) + c
    return {e:c for e,c in result.items() if c}
def scale(p, c):
    return {e:a*F(c) for e,a in p.items() if a*F(c)}
def mul(p, q):
    result = {}
    for a,c in p.items():
        for b,d in q.items():
            e = tuple(i+j for i,j in zip(a,b))
            result[e] = result.get(e, F(0)) + c*d
    return {e:c for e,c in result.items() if c}
def sq(p):
    return mul(p,p)
x,u,w,z = [var(i) for i in range(N)]  # z stands for W', independent.
E = add(scale(mul(mul(x,w),z),2),scale(sq(w),-1),
        scale(mul(u,w),F(3,2)),scale(w,-1),scale(sq(u),F(-3,16)),
        scale(u,F(3,4)),x)
S = add(u,scale(w,-4),const(-2))
V = add(scale(w,2),const(1))
T = add(scale(u,F(1,2)),scale(V,-1))
rhs = add(scale(mul(mul(x,w),z),F(32,3)),
          scale(sq(w),F(32,3)),scale(w,F(32,3)),
          scale(x,F(16,3)),const(4))
mode = sys.argv[1] if len(sys.argv)>1 else "positive"
need(mode in ("positive","--omit-W","--wrong-x"), "mode")
if mode == "--omit-W":
    rhs = add(rhs,scale(w,F(-32,3)))
if mode == "--wrong-x":
    rhs = add(rhs,scale(x,F(-8,3)))
Delta = add(sq(S),scale(rhs,-1))
K = add(scale(sq(T),3),scale(sq(V),-2),const(-1),scale(x,-4),
        scale(mul(mul(x,add(V,const(-1))),z),-4))
need(S == scale(T,2), "exact old/new coordinate map")
need(Delta == scale(E,F(-16,3)), "changed discriminant identity")
need(Delta == scale(K,F(4,3)), "old/new residual map")
need(K == scale(E,-4), "prior identity")
need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))), "assert gate")
print(json.dumps({"status":"PASS","identities":4,"generic_degree_max":3,
                  "actual_source_constructed":False},sort_keys=True))
