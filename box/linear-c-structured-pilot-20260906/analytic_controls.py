#!/usr/bin/env python3
"""Exact shear/binomial sanity controls; no formal truncation is used as a map."""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import socket
import time
def require(ok,why):
    if not ok:raise ValueError(why)
require(platform.system()=="Linux" and socket.gethostname()=="ip-172-30-0-56","Worker")
require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","EC2")
require(os.environ.get("JC2_REGISTERED_JOB")=="linear-c-structured-pilot-astra-20260906","Registration")
require(Path.cwd()==Path("/home/ubuntu/linear-c-structured-pilot-20260906"),"Owned scratch")
import sympy as S
started=time.monotonic()
h,D,C,a,b,s,E,A,z=S.symbols("h D C a b s E A z")
F=h**3+(3*D+a)*h/2+C
G=h**2-b*h/3+D
subs={h:s+b/6,D:E+b*b/36}
At=a/2+b*b/8
R=C-b*D/4+a*b/12+b**3/54
require(S.expand(G.subs(subs)-s*s-E)==0,"G square completion")
require(S.expand((F-b*G/2).subs(subs)-s**3-(3*E/2+At)*s-R.subs(subs))==0,"Target shear")
series=S.series((1+z)**S.Rational(3,2),z,0,4).removeO()
require(series==1+3*z/2+3*z*z/8-z**3/16,"3/2 binomial coefficients")
half=S.series((1+z)**S.Rational(1,2),z,0,3).removeO()
require(half==1+z/2-z*z/8,"1/2 binomial coefficients")
corr=S.expand(s**3*series.subs(z,E/s**2)+A*s*half.subs(z,E/s**2)-s**3-(3*E/2+A)*s)
require(S.expand(corr-(3*E**2/(8*s)-E**3/(16*s**3)+A*E/(2*s)-A*E**2/(8*s**3)))==0,"Correction signs")
x,w=S.symbols("x w")
H=(x+w)**3*w**8
dbad=x**9*w**25
top=S.cancel(3*dbad**2/(8*H**3))
num,den=S.fraction(top)
require(S.degree(den,x)>0 and S.rem(num,den,x)!=0,"Nonpolynomial homogeneous truncation negative control")
# Exact source top-slot realization of dbad is available from the frozen source:
# B2c_47_13=1, all other B2 parameters0 gives top coefficient X^9 W^25.
raw=Path("delta2_stage8.strongest.json").read_bytes()
require(hashlib.sha256(raw).hexdigest()=="778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea","Source")
data=json.loads(raw)
dtop=0
for r,j,e in data["maps"]["B2"]:
    if int(r)!=31:continue
    p=S.sympify(e);ev=p.subs({n:1 if str(n)=="B2c_47_13" else 0 for n in p.free_symbols})
    dtop+=ev*x**(34-int(j))*w**int(j)
require(S.expand(dtop-dbad)==0,"Negative control attained in actual D top source")
result={"status":"EXACT_ANALYTIC_CONTROLS_PASS","square_completion":True,"target_shear":True,
        "leading_R_correction":"3E^2/(8s)","next_corrections":"-E^3/(16s^3)+AE/(2s)",
        "next_omitted_displayed_term":"-AE^2/(8s^3)",
        "physical_degree_bounds":{"E2_over_s":35,"E3_over_s3":3,"AE_over_s":1,"AE2_over_s3":-31,"E4_over_s5":-29},
        "attained_source_nonpolynomial_highest_truncation":True,
        "formal_series_used_as_source_map":False,"fractional_kernel_polynomiality_assumed":False,
        "solver_launched":False,"wall_seconds":time.monotonic()-started,
        "peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path("analytic_controls.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
print(json.dumps(result,sort_keys=True),flush=True)
