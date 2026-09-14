#!/usr/bin/env python3
"""Independent exact replay and small highest-face controls; no solve."""
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import socket
import time

def require(ok, why):
    if not ok:raise ValueError(why)
require(socket.gethostname()=="ip-172-30-0-56","Allocated worker")
require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","EC2")
require(os.environ.get("JC2_REGISTERED_JOB")=="linear-c-filtered-pilot-astra-20260906","Registered")
require(Path.cwd()==Path("/home/ubuntu/linear-c-root-replay-20260906"),"Owned root replay scratch")
import sympy as S
from flint import fmpq_mat, fmpq
started=time.monotonic()
raw=Path("delta2_stage8.strongest.json").read_bytes()
require(hashlib.sha256(raw).hexdigest()=="778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea","Source pin")
source=json.loads(raw)
cert_raw=Path("filtered_basis_certificate.json").read_bytes()
cert=json.loads(cert_raw)
require(hashlib.sha256(cert_raw).hexdigest()=="c2b5965278e0fa30f0490b7f5a019434abe5291e50b748d3a3c0795c8175f906","Certificate pin")
names=cert["source_variables"]
old={n:{} for n in names}
for r,z,e in source["maps"]["A3"]:
    expr=S.sympify(e)
    recovered=S.Integer(0)
    for n in expr.free_symbols:
        c=S.diff(expr,n)
        require(c.is_Rational is True,"Source nonlinear or non-Q")
        q=Q(int(c.p),int(c.q))
        old[str(n)][(98-int(r)-int(z),int(z))]=q
        recovered+=c*n
    require(S.expand(expr-recovered)==0,"Source affine offset")
def decode(a):return {(i,j):Q(c) for i,j,c in a}
def plus(a,b):
    out=dict(a)
    for p,c in b.items():out[p]=out.get(p,Q(0))+c
    return {p:c for p,c in out.items() if c}
def scale(a,c):return {p:v*c for p,v in a.items() if v*c}
def derivative(a,k):
    out={}
    for p,c in a.items():
        if p[k]:
            q=list(p);q[k]-=1;out[tuple(q)]=c*p[k]
    return out
def multiply(a,b):
    out={}
    for p,c in a.items():
        for q,d in b.items():
            r=p[0]+q[0],p[1]+q[1];out[r]=out.get(r,Q(0))+c*d
    return {p:c for p,c in out.items() if c}
def bracket(a,b):
    return plus(multiply(derivative(a,0),derivative(b,1)),
                scale(multiply(derivative(a,1),derivative(b,0)),-1))
basis=cert["basis"]
for i,n in enumerate(names):require(old[n]==decode(cert["source_columns"][i]),"Source columns")
U=[[fmpq(0) for _ in basis] for _ in names]
for j,item in enumerate(basis):
    p={}
    for n,c in item["source_combination"].items():
        p=plus(p,scale(old[n],Q(c)))
        U[names.index(n)][j]=fmpq(c)
    require(p==decode(item["polynomial"]),"Basis reconstruction")
det=fmpq_mat(U).det()
require(bool(det),"Source transformation determinant")
r=cert["minor"]["size"]
require(r==189 and len(basis)==192,"Census")
Gtop=decode(cert["G_top"])
declared={(row["row"],row["column"]):decode(row["terms"]) for row in cert["selected_matrix_entries"]}
actual={}
for j,item in enumerate(basis):
    C=decode(item["polynomial"])
    Cx,Cw=derivative(C,0),derivative(C,1)
    for i,left in enumerate(basis[:r]):
        p,q=left["selected_J_row"]
        value={}
        for deriv,col,sgn in [(Cx,1,1),(Cw,0,-1)]:
            for (a,b),c in deriv.items():
                u,v=p-a,q-b
                if col==0:u+=1
                else:v+=1
                if min(u,v)<0 or u+v>66:continue
                c*=sgn*(u if col==0 else v)
                if u+v==66:c*=Gtop.get((u,v),0);key=(-1,-1)
                else:key=(u,v)
                value[key]=value.get(key,Q(0))+c
        value={p:c for p,c in value.items() if c}
        require(value==declared.get((i,j),{}),"Universal derivative coefficient mismatch")
        if value:actual[i,j]=value
        if j<r:
            if i<j:require(not value,"Universal forbidden upper entry")
            if i==j:require(value=={(-1,-1):Q(1)},"Universal diagonal")
require(actual==declared,"No extra matrix declarations")
# Negative control: a single changed selected pivot is rejected.
bad=dict(actual[0,0]);bad[(-1,-1)]+=1
require(bad!={(-1,-1):Q(1)},"Mutated-pivot negative control")
constant=decode(basis[-1]["polynomial"])
require(constant=={(0,0):Q(1)} and not derivative(constant,0) and not derivative(constant,1),"Unused additive constant")
require(all((i,191) not in declared for i in range(r)),"Constant appears in selected rows")

# Source mixing control: two degree-2 input vectors hide a degree-1 basis vector.
v1={(2,0):Q(1),(0,1):Q(1)};v2={(2,0):Q(1),(0,1):Q(-1)}
mixG={(3,0):Q(1),(0,3):Q(1)}
jhi=bracket(plus(v1,v2),mixG);jlo=bracket(plus(v1,scale(v2,-1)),mixG)
require(max(map(sum,jhi))==3 and max(map(sum,jlo))==2 and bool(jlo),"Filtration mixing control")

# Highest-face field-point parametrization, deliberately not a scheme claim.
x,w,aa,bb,cc,eps=S.symbols("x w aa bb cc eps")
H=(x+w)**3*w**8;htop=H**3
ell=aa*x*x+bb*x*w+cc*w*w
D=x*x*(x+w)**5*w**25*ell
C=S.Rational(3,8)*x**4*(x+w)*w**26*ell**2
def jac(f,g):return S.diff(f,x)*S.diff(g,w)-S.diff(f,w)*S.diff(g,x)
require(S.expand(S.Rational(3,4)*D**2-2*htop*C)==0,"Highest-face algebra identity")
require(S.expand(S.Rational(3,2)*D*jac(htop,D)+2*htop*jac(C,htop))==0,"Highest J")
Dsupport={(34-z,z) for r,z,e in source["maps"]["B2"] if int(r)==31}
Csupport={(35-z,z) for r,z,e in source["maps"]["A3"] if int(r)==63}
require(set(S.Poly(S.expand(D),x,w).monoms())<=Dsupport,"Source D top support")
require(set(S.Poly(S.expand(C),x,w).monoms())<=Csupport,"Source C top support")
Drows=[S.sympify(e) for r,z,e in source["maps"]["B2"] if int(r)==31]
Crows=[S.sympify(e) for r,z,e in source["maps"]["A3"] if int(r)==63]
Dv=sorted(set().union(*(e.free_symbols for e in Drows)),key=str)
Cv=sorted(set().union(*(e.free_symbols for e in Crows)),key=str)
require(S.Matrix([[S.diff(e,n) for n in Dv] for e in Drows]).rank()==8,"D top not surjective")
require(S.Matrix([[S.diff(e,n) for n in Cv] for e in Crows]).rank()==7,"C top not surjective")
require(not set(Dv)&set(Cv),"D/C source top coupling")
badD=x**9*w**25
require(S.rem(badD**2,(x+w)**9,x)!=0,"Field divisibility negative control")
nilpotent=S.Rational(3,4)*(eps*badD)**2
require(S.rem(nilpotent,eps**2,eps)==0,"Dual-number highest-face control")
require(S.rem(eps*badD,(x+w)**5,x)!=0,"Dual-number not parametrized")
# Full homogeneous map S_68 -> J(h_top,S_68) is injective; constant-coefficient check.
M=[]
for j in range(69):
    p=S.Poly(jac(x**(68-j)*w**j,htop),x,w)
    M.append([Q(p.coeff_monomial(x**(99-k)*w**k)) for k in range(100)])
rank=fmpq_mat([[fmpq(str(c)) for c in row] for row in M]).rank()
require(rank==69,"Highest-face constant linear injection")
result={"status":"INDEPENDENT_EXACT_REPLAY_PASS","constant_pivots":189,"minor_determinant":"1",
        "source_transform_determinant":str(det),"all_42131_G_linear_terms_recomputed":True,
        "mutated_pivot_negative_control":True,"mixed_homogeneous_source_control":True,
        "remaining_nonconstant_C_parameters":2,"highest_face_field_parametrization":True,
        "top_source_ranks":{"D":8,"C":7},"highest_face_linear_map_rank":69,
        "dual_number_counterexample_to_scheme_parametrization":True,
        "certificate_sha256":hashlib.sha256(cert_raw).hexdigest(),
        "dense_substitution":False,"solver_launched":False,
        "wall_seconds":time.monotonic()-started,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path("verify_filtered_summary.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
print(json.dumps(result,sort_keys=True),flush=True)
