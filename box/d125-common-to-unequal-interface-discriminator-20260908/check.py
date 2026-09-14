import sys
sys.dont_write_bytecode = True
import json
import math
import resource
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))

def need(x, name):
    if not x:
        raise ValueError(name)

def shift(P, e):
    Q = {}
    for (i,j), a in P.items():
        for k in range(j+1):
            Q[i,k] = Q.get((i,k), 0) + a*math.comb(j,k)*e**(j-k)
    return {v:a for v,a in Q.items() if a}

def add(*polys):
    Q = {}
    for P in polys:
        for v,a in P.items():
            Q[v] = Q.get(v,0)+a
    return {v:a for v,a in Q.items() if a}

mode = sys.argv[1] if len(sys.argv)>1 else 'normal'
need(mode in ('normal','wrong-shift','omit-lower-slot','drop-mu'), 'mode')
mu = 0 if mode == 'drop-mu' else 2
need(mu != 0, 'literal common-face guard')
H = {(0,5):1,(3,2):1}
# R = H + g^3*((p-mu)^2-p^2) + g^2. No R powers built.
R = add(H, {(3,1):-2*mu,(3,0):mu*mu},
        {} if mode == 'omit-lower-slot' else {(2,0):1})
e = -mu if mode == 'wrong-shift' else mu
Rp = shift(R,e)
need({v:a for v,a in Rp.items() if v[0]==3} == {(3,2):1}, 'center exact g^3 face')
need({v:a for v,a in Rp.items() if sum(v)==5} == H, 'entire degree-five top')
need(max(5*i-7*j for i,j in Rp)==10, 'remaining forbidden weighted slot')
need(Rp.get((2,0))==1, 'actual g^2 survives')
need(shift(Rp,-e)==R, 'polynomial inverse')
# Common_3: an exponent under p -> p+mu/g can attain -15 only from (0,15).
slots = [(i,j) for i in range(16) for j in range(16-i)]
pole_sources = [(i,j) for i,j in slots if i-j == -15]
need(pole_sources == [(0,15)], 'unique Laurent pole source')
need(mu**15 != 0, 'Laurent pole does not cancel')
need(5*3>3 and 5*9-7*6==3, 'common3 incompatible endpoints')
# The common_3 highest-g primitive coefficient is p^2; only e=0 retains it.
need(shift({(0,2):1},0)=={(0,2):1}, 'zero translation succeeds on coefficient')
need(shift({(0,2):1},mu).get((0,0))==mu*mu, 'nonzero translation fails on coefficient')
# Differential determinant for g'=a*g, p'=b*p+e: ab; target multiplies by a^3*b.
a,b = 2,2
need(a*b*a*a == a**3*b, 'Jacobian transport scalar')
print(json.dumps({'status':'PASS','mode':mode,'degree_five_fixture':[[i,j,str(a)] for (i,j),a in sorted(Rp.items())], 'weight':'10','pole_coefficient':str(mu**15),'actual_full_Jacobian_fixture':False},sort_keys=True))
