import sys, os, time, pickle
os.environ["DIRECTIONB_STATE"]="/tmp/directionb_tails_D23.pkl"
sys.path.insert(0,'/Users/dc/code/math/jc72108/cases')
import fastelim as FE
p=int(sys.argv[1])
PIV22=[("tf1_44",(12,2)),("tf2_44",(12,5)),("tf1_46",(14,0)),("tf2_46",(14,3)),
       ("tf1_43",(16,1)),("tf1_48",(16,4)),("tf2_43",(16,7)),("tf2_48",(16,10)),
       ("tf1_45",(18,2)),("tf1_50",(18,5)),("tf2_45",(18,8)),("tf2_50",(18,11)),
       ("tf1_47",(20,0)),("tf1_52",(20,3)),("tf2_47",(20,6)),("tf2_52",(20,9)),
       ("tf1_38",(6,2)),("tf1_40",(8,0)),("tf2_40",(8,3)),("tf1_39",(12,8)),
       ("tf1_41",(14,6)),("tf2_41",(14,9))]
t0=time.time()
r3v, pt = FE.r3_of(p)
eng = FE.Engine(p, r3v)
print("build %.0fs (window rows: %d)"%(time.time()-t0,len(eng.labs)), flush=True)
eng.reset()
used=set()
t1=time.time()
n2v={eng.vars_[i]: i for i in eng.occ}
CKPT="/tmp/c23_ckpt_p%d.pkl"%p
start=0
try:
    ck=pickle.load(open(CKPT,"rb"))
    start=ck["k"]
    eng.P=[eng.ctx.from_dict(d) if d is not None else eng.P0[i]
           for i,d in enumerate(ck["rows"])]
    used=set(ck["used"])
    print("resumed at pivot %d"%start, flush=True)
except FileNotFoundError: pass
for pk,(nm, lab) in enumerate(PIV22):
    if pk<start: continue
    bi=eng.labs.index(lab); gx=eng.gi[n2v[nm]]
    P=eng.P[bi]
    assert P.degrees()[gx]==1
    cp=P.derivative(gx)
    assert eng.tdeg0(cp)
    for bj in range(len(eng.P)):
        if bj==bi or bj in used or eng.P[bj].is_zero(): continue
        R=eng.P[bj]
        if R.degrees()[gx]==0: continue
        while (dg:=R.degrees()[gx])>0:
            D=R
            for _ in range(dg): D=D.derivative(gx)
            Adm=D.subs({gx:0})
            fct=1
            for i2 in range(2,dg+1): fct*=i2
            if fct>1: Adm=Adm*eng.ctx.from_dict({tuple([0]*(eng.nt+6)):pow(fct,p-2,p)})
            xm=[0]*(eng.nt+6); xm[gx]=dg-1
            R=cp*R-Adm*eng.ctx.from_dict({tuple(xm):1})*P
        eng.P[bj]=R
    used.add(bi)
    if pk==18:            # one-time merge before the low-39/41 block
        tm=time.time()
        for bj in range(len(eng.P)):
            if bj in used or eng.P[bj].is_zero(): continue
            dd=eng.reduce_lattice(eng.P[bj])
            if not dd:
                eng.P[bj]=eng.ctx.from_dict({}); continue
            iw1,iw2=eng.nt+2,eng.nt+4
            a=min(k[iw1] for k in dd); b=min(k[iw2] for k in dd)
            if a or b:
                dd={tuple(x-(a if j==iw1 else b if j==iw2 else 0)
                          for j,x in enumerate(k)):c for k,c in dd.items()}
            eng.P[bj]=eng.ctx.from_dict(dd)
        print("  [mid-merge %.1fs]"%(time.time()-tm), flush=True)
    print("  pivot %s %.1fs"%(nm,time.time()-t1), flush=True)
    if time.time()-t0>250:
        pickle.dump({"k":pk+1,
                     "rows":[None if bi2 in used else FE.mp_to_dict(eng.P[bi2])
                             for bi2 in range(len(eng.P))],
                     "used":sorted(used)}, open(CKPT,"wb"))
        print("CHECKPOINT at pivot %d -- rerun to resume"%(pk+1), flush=True)
        sys.exit(3)
print("22 pivots RAW %.1fs"%(time.time()-t1), flush=True)
t2=time.time()
def redstrip(f):
    d=eng.reduce_lattice(f)
    if not d: return {}, (0,0)
    iw1,iw2=eng.nt+2,eng.nt+4
    a=min(k[iw1] for k in d); b=min(k[iw2] for k in d)
    if a or b:
        d={tuple(x-(a if j==iw1 else b if j==iw2 else 0)
                 for j,x in enumerate(k)):c for k,c in d.items()}
    return d,(a,b)
def byname(d):
    o={}
    for k,c in d.items():
        nm=tuple(sorted((eng.vars_[eng.occ[j]],k[j]) for j in range(eng.nt) if k[j]))
        o[(nm, tuple(k[eng.nt:]))]=c
    return o
red=[]; stripsrec=[]
for bi in range(len(eng.P)):
    if bi in used or eng.P[bi].is_zero(): continue
    d,ab=redstrip(eng.P[bi])
    if d: red.append((eng.labs[bi],byname(d))); stripsrec.append(ab)
pivrows={}
for nm,lab in PIV22:
    d,_=redstrip(eng.P[eng.labs.index(lab)])
    pivrows[lab]=byname(d)
print("final reduce+strip %.1fs (%d strips nonzero)"%(
    time.time()-t2,sum(1 for ab in stripsrec if ab!=(0,0))), flush=True)
try: out=pickle.load(open("/tmp/core23_red.pkl","rb"))
except Exception: out={}
out[p]={"red":red,"pivrows":pivrows,"pivseq":PIV22,"r3v":r3v,"pt":dict(pt)}
pickle.dump(out, open("/tmp/core23_red.pkl","wb"))
import os as _os
try: _os.remove(CKPT)
except Exception: pass
nt=sum(len(d) for _,d in red)
n22=sum(1 for lab,_ in red if lab[0]==22)
tset=sorted({v for _,d in red for (nm,_) in d for v,_ in nm})
mdg=max(sum(e for _,e in nm)+sum(rt) for _,d in red for (nm,rt) in d)
print("p=%d: %d rows (%d Row_22-desc), %d terms, %d template coords, maxdeg %d, total %.0fs BANKED"%(
    p,len(red),n22,nt,len(tset),mdg,time.time()-t0), flush=True)
