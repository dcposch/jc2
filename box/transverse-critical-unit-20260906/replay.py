#!/usr/bin/env python3
"""Tiny normal-mode controls for the transverse critical-unit identity."""
import resource
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
import json
import sympy as S
X,W,l,m,z,beta,gamma=S.symbols("X W l m z beta gamma")
q0,q1,q2,f0,f1,f2,f3,v0,v1,v2=S.symbols("q0 q1 q2 f0 f1 f2 f3 v0 v1 v2")
def req(ok,msg):
    if not ok: raise ValueError(msg)
def jac(F,G):
    return S.expand(S.diff(F,X)*S.diff(G,W)-S.diff(F,W)*S.diff(G,X))
def at(p):
    return S.expand(p.subs({X:-l/2,W:0}, simultaneous=True))
G=X**2+l*X+m+W*(q0+q1*X+q2*X**2)+W**2*(X**2+1)
C=beta*X+gamma+W*(v0+v1*X+v2*X**2)+W**2*(X+1)
Fbase=f0+f1*X+f2*X**2+f3*X**3+W*(X**3+2)
F=Fbase+C
delta=at(S.diff(G,W))
J=jac(F,G)
Jline=S.expand(J.subs(W,0));j0=Jline.subs(X,0)
tail=S.expand((Jline-j0).subs(X,-l/2))
req(at(S.diff(G,X))==0,"critical point")
req(S.expand(at(jac(C,G))-beta*delta)==0,"evaluation kills V0")
req(S.expand(at(J)-at(S.diff(F,X))*delta)==0,"Jacobian evaluation")
rhs=-(z*j0-1)-z*tail
req(S.expand((1-z*at(S.diff(F,X))*delta)-rhs)==0,"unit ideal identity")
bad_rhs=-(z*j0-1)+z*tail
req(S.expand((1-z*at(S.diff(F,X))*delta)-bad_rhs)!=0,"sign mutation escaped")
Gbad=G+X**3
req(at(S.diff(Gbad,X))!=0,"nonquadratic control did not break hypothesis")
req(S.expand(at(jac(C,Gbad))-beta*at(S.diff(Gbad,W)))!=0,"nonquadratic false extension escaped")
Gzero=X**2+W**2
req(jac(X,Gzero)==2*W,"zero delta control")
req(at(S.diff(Gzero,W))==0,"zero delta expected")
req(jac(X,X**2+W)==1,"actual Keller positive control")
print(json.dumps({"status":"PASS_NORMAL_ONLY","delta":str(delta),"unit_multiplier":str(at(S.diff(F,X))),"symbolic_unit_identity":True,"V0_annihilation":True,"negative_controls":["flipped ideal-identity sign","removed quadratic-line hypothesis","delta0 off Keller locus"],"positive_control":"F=X,G=X^2+W,J=1,delta=1"},sort_keys=True))
