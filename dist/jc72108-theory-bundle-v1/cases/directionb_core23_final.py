import sys, os, time, pickle, random, re
os.environ["DIRECTIONB_STATE"]="/tmp/directionb_tails_D23.pkl"
sys.path.insert(0,'/Users/dc/code/math/jc72108/cases')
import fastelim as FE
import directionb_residual32_emit as E32
HERE='/Users/dc/code/math/jc72108/cases'
OK=[]
def chk(n,c):
    OK.append((n,bool(c))); print(("PASS " if c else "FAIL ")+n, flush=True)
p=105337
t0=time.time()
r3v, pt = FE.r3_of(p)
eng = FE.Engine(p, r3v)
h32=pt["HW1"]*pow(pt["W1"],p-2,p)%p
hdr, char, eqs = E32.FCparse("directionb_core23_p%d.ms"%p)
# parse emitted rows into dicts over header names
def parse(e):
    d={}
    for t in e.split('+'):
        fs=t.split('*'); c=int(fs[0]); mono={}
        for f in fs[1:]:
            m=re.match(r'([A-Za-z0-9_]+)\^(\d+)',f)
            if m: mono[m.group(1)]=mono.get(m.group(1),0)+int(m.group(2))
            else: mono[f]=mono.get(f,0)+1
        k=tuple(sorted(mono.items()))
        d[k]=(d.get(k,0)+c)%p
    return {k:c for k,c in d.items() if c}
rows=[parse(e) for e in eqs[:70]]
# round-trip: random point (all header vars random; rad consistent)
rng=random.Random(5)
val={nm:rng.randrange(1,p) for nm in hdr}
for nm in FE.RADG: val[nm]=pt[nm]
val["uW1"]=pow(pt["W1"],p-2,p); val["uW2"]=pow(pt["W2"],p-2,p)
val["uA"]=pow((pt["A1"]-pt["A2"])%p,p-2,p)
okrt=all(E32._tiny_parse_eval(eqs[i],val,p)==
         sum(c*__import__('functools').reduce(lambda a,b:a*pow(val[b[0]],b[1],p)%p,k,1) for k,c in rows[i].items())%p
         for i in range(70))
chk("round-trip: emitted D23-core-v2 rows re-parse consistently (70 rows)", okrt)
# fiber variant: fold radgens in ALL 70 rows
xn2nm={}
v21list=pickle.load(open('/tmp/directionb_tails_D21.pkl','rb'))["vars"]
_,names,_,_,_=E32.load_rows()
for vid,xn in names.items(): xn2nm[xn]=v21list[vid]
# regenerate the deterministic x74+ map exactly as the v2 emission did
PIV22=[("tf1_44",(12,2)),("tf2_44",(12,5)),("tf1_46",(14,0)),("tf2_46",(14,3)),
       ("tf1_43",(16,1)),("tf1_48",(16,4)),("tf2_43",(16,7)),("tf2_48",(16,10)),
       ("tf1_45",(18,2)),("tf1_50",(18,5)),("tf2_45",(18,8)),("tf2_50",(18,11)),
       ("tf1_47",(20,0)),("tf1_52",(20,3)),("tf2_47",(20,6)),("tf2_52",(20,9)),
       ("tf1_38",(6,2)),("tf1_40",(8,0)),("tf2_40",(8,3)),("tf1_39",(12,8)),
       ("tf1_41",(14,6)),("tf2_41",(14,9))]
pivlabs=[lab for _,lab in PIV22]
name2xF={v:k for k,v in xn2nm.items()}
nxt=[74]
for lab in [l for l in eng.labs if l in pivlabs or l[0]==22]:
    d0=FE.mp_to_dict(eng.P0[eng.labs.index(lab)])
    for k in sorted(d0):
        for j in range(eng.nt):
            if k[j]:
                nm=eng.vars_[eng.occ[j]]
                if nm not in name2xF:
                    name2xF[nm]="x%d"%nxt[0]; xn2nm["x%d"%nxt[0]]=nm; nxt[0]+=1
def fold(d):
    out={}
    for k,c in d.items():
        v=c; mono={}
        s1w=0; s2w=0
        for nm,e in k:
            if nm=="A1": v=v*pow(pt["A1"],e,p)%p
            elif nm=="A2": v=v*pow(pt["A2"],e,p)%p
            elif nm=="HW1": v=v*pow(h32,e,p)%p; s1w+=e
            elif nm=="HW2": v=v*pow(h32,e,p)%p; s2w+=e
            elif nm=="W1": s1w+=e
            elif nm=="W2": s2w+=e
            elif nm in ("uW1","uW2","uA"): mono[nm]=e
            else: mono[nm]=e
        if s1w: mono["W1"]=mono.get("W1",0)+s1w
        if s2w: mono["W2"]=mono.get("W2",0)+s2w
        kk=tuple(sorted(mono.items()))
        out[kk]=(out.get(kk,0)+v)%p
    return {k:c for k,c in out.items() if c}
def to_reg(d):
    out={}
    for k,c in d.items():
        kk=tuple(sorted((xn2nm.get(nm,nm),e) for nm,e in k))
        out[kk]=(out.get(kk,0)+c)%p
    return out
frowsX=[fold(d) for d in rows]
frowsX=[d for d in frowsX if d]
frows=[to_reg(d) for d in frowsX]
fvars=sorted({nm for d in frowsX for k in d for nm,_ in k})
body=[]
ntf=0
for d in frowsX:
    parts=[]
    for k in sorted(d):
        mono=[nm+("^%d"%e if e>1 else "") for nm,e in k]
        parts.append("%d%s"%(d[k],"*"+"*".join(mono) if mono else ""))
    ntf+=len(d); body.append("+".join(parts))
pathf="%s/directionb_core23_fiber_p%d.ms"%(HERE,p)
with open(pathf,"w") as f:
    f.write(", ".join(fvars+([] if "uW1" in fvars else ["uW1","uW2"]))+"\n%d\n"%p)
    f.write(",\n".join(body+["uW1*W1+%d"%(p-1),"uW2*W2+%d"%(p-1)])+"\n")
txt=open(pathf).read()
chk("fiber D23-core-v2: %d rows, %d terms, %d vars, %dB, paren-free"%(
    len(body)+2,ntf,len(fvars),os.path.getsize(pathf)),
    "(" not in txt and ")" not in txt)
# FILTER-REPLAY closure: regenerate the 12 points, evaluate the fiber
# rows at each with deep vars symbolic -> affine inconsistency
exec(open('/tmp/fiber_filter.py').read().split("# ---- reconstruct")[0].replace("sys.exit(0)","raise SystemExit"))
# pts, gvars, vi available now
DEEP={nm for nm in fvars if nm.rsplit("_",1)[-1] in ("49","53","54")}
D23V=pickle.load(open('/tmp/core23_red.pkl','rb'))[p]
pr={lab:d for lab,d in D23V["pivrows"].items()}
seq=D23V["pivseq"]
def evname(d, assign):
    tot=0
    for (nm,rt),c in d.items():
        m=c
        for v2,e in nm:
            if assign.get(v2) is None: return None
            m=m*pow(assign[v2],e,p)%p
        e1,e2,pw,h1,qw,h2=rt
        m=m*pow(pt["A1"],e1,p)*pow(pt["A2"],e2,p)*pow(h32,h1+h2,p)%p
        m=m*pow(assign["W1"],pw+h1,p)*pow(assign["W2"],qw+h2,p)%p
        tot=(tot+m)%p
    return tot
dead=0
for pi,val2 in enumerate(pts):
    assign={}
    for j,gv in enumerate(gvars):
        if gv.startswith("x"): assign[xn2nm[gv]]=val2[j]
    assign["W1"]=val2[vi["W1"]]; assign["W2"]=val2[vi["W2"]]
    for nm in set(v21list)|DEEP:
        if nm not in assign and nm[:2] in ("tf","tg","uf","vf"):
            assign.setdefault(nm,0)
    # back-solve 22 pivots (name dicts, reverse)
    for nmv,lab in reversed(seq):
        d=pr[lab]
        cp=0; rest=0
        a0=dict(assign); a0[nmv]=0
        for (nmk,rt),c in d.items():
            deg=dict(nmk).get(nmv,0)
            m=c
            ok=True
            for v2,e in nmk:
                if v2==nmv: continue
                m=m*pow(a0[v2],e,p)%p
            e1,e2,pw,h1,qw,h2=rt
            m=m*pow(pt["A1"],e1,p)*pow(pt["A2"],e2,p)*pow(h32,h1+h2,p)%p
            m=m*pow(assign["W1"],pw+h1,p)*pow(assign["W2"],qw+h2,p)%p
            if deg==1: cp=(cp+m)%p
            else: rest=(rest+m)%p
        assign[nmv]=(-rest)*pow(cp,p-2,p)%p
    # affine test on fiber rows: unknowns = DEEP
    ui=sorted(DEEP); uix={nm:i for i,nm in enumerate(ui)}
    M=[]; R=[]
    okaff=True
    for d in frows:
        row=[0]*len(ui); b=0
        for k,c in d.items():
            us=[nm for nm,_ in k if nm in DEEP]
            if len(us)>1 or any(e>1 for nm,e in k if nm in DEEP): okaff=False; break
            m=c
            for nm,e in k:
                if nm in DEEP: continue
                if nm in ("uW1","uW2"): m=m*pow(pow(assign["W"+nm[-1]],p-2,p),e,p)%p
                else: m=m*pow(assign[nm],e,p)%p
            if us: row[uix[us[0]]]=(row[uix[us[0]]]+m)%p
            else: b=(b+m)%p
        if not okaff: break
        M.append(row); R.append((-b)%p)
    if not okaff:
        print("  point %d: NONAFFINE"%pi); continue
    rk=0; inc=False
    for c2 in range(len(ui)):
        prw=next((i for i in range(rk,len(M)) if M[i][c2]),None)
        if prw is None: continue
        M[rk],M[prw]=M[prw],M[rk]; R[rk],R[prw]=R[prw],R[rk]
        iv=pow(M[rk][c2],p-2,p)
        M[rk]=[x*iv%p for x in M[rk]]; R[rk]=R[rk]*iv%p
        for i in range(len(M)):
            if i!=rk and M[i][c2]:
                f2=M[i][c2]
                M[i]=[(a-f2*bb)%p for a,bb in zip(M[i],M[rk])]
                R[i]=(R[i]-f2*R[rk])%p
        rk+=1
    inc=any(not any(M[i]) and R[i] for i in range(len(M)))
    if inc: dead+=1
chk("FILTER-REPLAY closure: %d/12 sampled D21 fiber points "
    "INCONSISTENT against the EMITTED D23-core rows (deep tails "
    "symbolic, affine test through the emission)"%dead, dead==12)
bad=[n for n,c in OK if not c]
print("FINAL TOTAL: %d checks, %d FAIL %s (%.0fs)"%(len(OK),len(bad),bad or "",time.time()-t0))
