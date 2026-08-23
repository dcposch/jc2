import sys, os, time, pickle, re
sys.path.insert(0,'/Users/dc/code/math/jc2/cases')
import directionb_residual32_emit as E32
import r1_fullcore as FC
OK=[]
def chk(n,c):
    OK.append((n,bool(c))); print(("PASS " if c else "FAIL ")+n, flush=True)
p=105337
t0=time.time()
pt=FC.radical_point(p)
h32=pt["HW1"]*pow(pt["W1"],p-2,p)%p
hdr,char,eqs=E32.FCparse("directionb_core23_p%d.ms"%p)
assert char==p and len(eqs)==77
RADG=("A1","A2","W1","HW1","W2","HW2")
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
# identify the Row_22 block: rows containing x74+ deep vars
def hix(d):
    return {nm for k in d for nm,_ in k
            if nm.startswith("x") and int(nm[1:])>=74}
r22=[d for d in rows[38:] if hix(d)]
chk("Row_22 block located in the frozen artifact: %d rows"%len(r22),
    len(r22)==10)
allhi=sorted({nm for d in r22 for nm in hix(d)}, key=lambda s:int(s[1:]))
DEEP=["x%d"%i for i in range(74,84)]
lin=all(all(dict(k).get(nm,0)<=1 and (nm not in dict(k) or len([1 for n2,_ in k if n2.startswith("x") and int(n2[1:])>=74])<=1)
            for k in d for nm in DEEP) for d in r22)
chk("deep vars present: %s; x74..x83 appear affine-linearly"%(",".join(allhi)), lin and set(DEEP)<=set(allhi))
# fold radgens at the fiber (W symbolic), split A|b on DEEP
A={}; Bv={}
for ri,d in enumerate(r22):
    for k,c in d.items():
        kd=dict(k)
        v=c
        v=v*pow(pt["A1"],kd.pop("A1",0),p)%p
        v=v*pow(pt["A2"],kd.pop("A2",0),p)%p
        hh=kd.pop("HW1",0)+kd.pop("HW2",0)
        # careful: HW1,HW2 fold separately
        kd2=dict(k); w1=kd2.get("W1",0)+kd2.get("HW1",0); w2=kd2.get("W2",0)+kd2.get("HW2",0)
        v=c
        v=v*pow(pt["A1"],kd2.get("A1",0),p)%p
        v=v*pow(pt["A2"],kd2.get("A2",0),p)%p
        v=v*pow(h32,kd2.get("HW1",0)+kd2.get("HW2",0),p)%p
        ds=[nm for nm,_ in k if nm in DEEP]
        rest=tuple(sorted((nm,e) for nm,e in k
                          if nm not in DEEP and nm not in RADG))
        key=(rest,w1,w2)
        if ds:
            tgt=A.setdefault((ri,DEEP.index(ds[0])),{})
        else:
            tgt=Bv.setdefault(ri,{})
        tgt[key]=(tgt.get(key,0)+v)%p
A={k:{kk:c for kk,c in dd.items() if c} for k,dd in A.items()}
A={k:dd for k,dd in A.items() if dd}
okF=True; C=[[0]*10 for _ in range(10)]; Umono=[None]*10
for j in range(10):
    col={ri:dd for (ri,jj),dd in A.items() if jj==j}
    ws=set(); ent={}
    for ri,dd in col.items():
        okF &= all(kk==() for (kk,w1,w2) in dd) and len(dd)==1
        if not okF: break
        (kk,w1,w2),v=next(iter(dd.items()))
        ws.add((w1,w2)); ent[ri]=v
    okF &= len(ws)==1
    if not okF: break
    Umono[j]=next(iter(ws))
    for ri,v in ent.items(): C[ri][j]=v
chk("A = C diag(u_j): each deep column = constant column x single "
    "W-monomial; u-monomials %s"%Umono, okF)
M=[r_[:] for r_ in C]
Um=[[int(i==j) for j in range(10)] for i in range(10)]
r=0
for cidx in range(10):
    prw=next((i for i in range(r,10) if M[i][cidx]),None)
    if prw is None: continue
    M[r],M[prw]=M[prw],M[r]; Um[r],Um[prw]=Um[prw],Um[r]
    iv=pow(M[r][cidx],p-2,p)
    M[r]=[x*iv%p for x in M[r]]; Um[r]=[x*iv%p for x in Um[r]]
    for i in range(10):
        if i!=r and M[i][cidx]:
            f=M[i][cidx]
            M[i]=[(a-f*b)%p for a,b in zip(M[i],M[r])]
            Um[i]=[(a-f*b)%p for a,b in zip(Um[i],Um[r])]
    r+=1
chk("rank(C) == 4, certified by exact row reduction with recorded "
    "invertible U", r==4)
L=[Um[i] for i in range(4,10)]
okL=all(sum(L[i][k]*C[k][j] for k in range(10))%p==0
        for i in range(6) for j in range(10))
chk("L C == 0 => L A == 0 for ALL W (unit diag cancels): the SIX "
    "compatibility rows are complete", okL)
cRows=[]
for i in range(6):
    acc={}
    for k in range(10):
        if not L[i][k] or k not in Bv: continue
        for key,v in Bv[k].items():
            acc[key]=(acc.get(key,0)+L[i][k]*v)%p
    cRows.append({k:v for k,v in acc.items() if v})
print("c = L b: 6 rows, %d terms (PRE-pivot, matching Sol stage "
     "'before pivot elimination')"%sum(len(d) for d in cRows), flush=True)
pickle.dump({"cRows":cRows,"L":L,"C":C,"u":Umono,"pivrows":rows[38:60],
             "core21":rows[:38],"eqs":eqs,"hdr":hdr,"p":p,
             "pt":dict(pt)}, open("/tmp/r22_s1.pkl","wb"))
bad=[n for n,c in OK if not c]
print("S1: %d checks, %d FAIL %s (%.0fs)"%(len(OK),len(bad),bad or "",time.time()-t0))
