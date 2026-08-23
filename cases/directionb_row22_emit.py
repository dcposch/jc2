import sys, os, time, pickle, re
sys.path.insert(0,'/Users/dc/code/math/jc2/cases')
import directionb_residual32_emit as E32
import r1_fullcore as FC
HERE='/Users/dc/code/math/jc2/cases'
OK=[]
def chk(n,c):
    OK.append((n,bool(c))); print(("PASS " if c else "FAIL ")+n, flush=True)
RADG=("A1","A2","W1","HW1","W2","HW2")
t00=time.time()
def parse(e,p):
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
DEEP=["x%d"%i for i in range(74,84)]
allsizes={}
for p in (105337,105673,200257):
    pt=FC.radical_point(p)
    h32=pt["HW1"]*pow(pt["W1"],p-2,p)%p
    hdr,char,eqs=E32.FCparse("directionb_core23_p%d.ms"%p)
    rows=[parse(e,p) for e in eqs[:70]]
    r22=[d for d in rows[38:] if any(nm in DEEP for k in d for nm,_ in k)]
    pivrows=[d for d in rows[38:] if d not in r22]
    assert len(r22)==10 and len(pivrows)==22
    # fold radgens (A,HW) at the fiber; W symbolic; A|b split
    A={}; Bv={}
    for ri,d in enumerate(r22):
        for k,c in d.items():
            v=c; rest=[]; w1=w2=0; deep=None
            for nm,e in k:
                if nm=="A1": v=v*pow(pt["A1"],e,p)%p
                elif nm=="A2": v=v*pow(pt["A2"],e,p)%p
                elif nm=="HW1": v=v*pow(h32,e,p)%p; w1+=e
                elif nm=="HW2": v=v*pow(h32,e,p)%p; w2+=e
                elif nm=="W1": w1+=e
                elif nm=="W2": w2+=e
                elif nm in DEEP: deep=nm
                else: rest.append((nm,e))
            key=(tuple(sorted(rest)),w1,w2)
            tgt=A.setdefault((ri,DEEP.index(deep)),{}) if deep \
                else Bv.setdefault(ri,{})
            tgt[key]=(tgt.get(key,0)+v)%p
    A={k:{kk:c for kk,c in dd.items() if c} for k,dd in A.items()}
    A={k:dd for k,dd in A.items() if dd}
    C=[[0]*10 for _ in range(10)]; okF=True
    for j in range(10):
        col={ri:dd for (ri,jj),dd in A.items() if jj==j}
        ws=set()
        for ri,dd in col.items():
            okF &= all(kk==() for (kk,w1,w2) in dd) and len(dd)==1
            (kk,w1,w2),v=next(iter(dd.items()))
            ws.add((w1,w2)); C[ri][j]=v
        okF &= len(ws)==1
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
    L=[Um[i] for i in range(4,10)]
    okL=all(sum(L[i][k]*C[k][j] for k in range(10))%p==0
            for i in range(6) for j in range(10))
    chk("[p=%d] Schur: A=C diag(u), rank(C)=4, L C = 0 (certified)"%p,
        okF and r==4 and okL)
    c6=[]
    for i in range(6):
        acc={}
        for k in range(10):
            if not L[i][k] or k not in Bv: continue
            for key,v in Bv[k].items():
                acc[key]=(acc.get(key,0)+L[i][k]*v)%p
        c6.append({k:v for k,v in acc.items() if v})
    # emit: [fiber core rows (24, W-symbolic)] + [22 pivot rows folded
    # W-symbolic] + [6 compat rows] + uW rows
    fh,fc,feqs=E32.FCparse("directionb_core2_fiber_p%d.ms"%p)
    corerows=feqs[:-2]
    def foldW(d):
        out={}
        for k,c in d.items():
            v=c; rest=[]; w1=w2=0
            for nm,e in k:
                if nm=="A1": v=v*pow(pt["A1"],e,p)%p
                elif nm=="A2": v=v*pow(pt["A2"],e,p)%p
                elif nm=="HW1": v=v*pow(h32,e,p)%p; w1+=e
                elif nm=="HW2": v=v*pow(h32,e,p)%p; w2+=e
                elif nm=="W1": w1+=e
                elif nm=="W2": w2+=e
                else: rest.append((nm,e))
            if w1: rest.append(("W1",w1))
            if w2: rest.append(("W2",w2))
            kk=tuple(sorted(rest))
            out[kk]=(out.get(kk,0)+v)%p
        return {k:c for k,c in out.items() if c}
    def tostr(d):
        parts=[]
        for k in sorted(d):
            mono=[nm+("^%d"%e if e>1 else "") for nm,e in k]
            parts.append("%d%s"%(d[k],"*"+"*".join(mono) if mono else ""))
        return "+".join(parts)
    pivstr=[tostr(foldW(d)) for d in pivrows]
    c6f=[]
    for d in c6:
        out={}
        for (rest,w1,w2),v in d.items():
            kk=list(rest)
            if w1: kk.append(("W1",w1))
            if w2: kk.append(("W2",w2))
            kk=tuple(sorted(kk))
            out[kk]=(out.get(kk,0)+v)%p
        c6f.append({k:c for k,c in out.items() if c})
    cstr=[tostr(d) for d in c6f]
    allv=sorted({nm for e in corerows+pivstr+cstr
                 for nm in re.findall(r'[A-Za-z][A-Za-z0-9_]*',e)
                 if not nm.startswith('W') or nm in ("W1","W2")} |
                {"uW1","uW2"})
    allv=[v for v in allv if v not in ("uW1","uW2")]+["uW1","uW2"]
    body=corerows+pivstr+cstr+["uW1*W1+%d"%(p-1),"uW2*W2+%d"%(p-1)]
    path="%s/directionb_row22compat_p%d.ms"%(HERE,p)
    with open(path,"w") as f:
        f.write(", ".join(allv)+"\n%d\n"%p)
        f.write(",\n".join(body)+"\n")
    txt=open(path).read(); assert "(" not in txt and ")" not in txt
    nt=sum(e.count("+")+1 for e in body)
    allsizes[p]=(len(allv),len(body),nt,os.path.getsize(path))
    chk("[p=%d] emitted: %d vars, %d eqs, %d terms, %dB -- DEEP "
        "TAILS ELIMINATED (no x74..x83 in the system)"%(
        p,len(allv),len(body),nt,os.path.getsize(path)),
        not any(nm in DEEP for e in body for nm in re.findall(r'x\d+',e)))
    if p==105337:
        pickle.dump({"c6f":c6f,"L":L,"C":C},open("/tmp/r22_c6_p105337.pkl","wb"))
print("shapes:", allsizes)
bad=[n for n,c in OK if not c]
print("EMIT TOTAL: %d checks, %d FAIL %s (%.0fs)"%(len(OK),len(bad),bad or "",time.time()-t00))
