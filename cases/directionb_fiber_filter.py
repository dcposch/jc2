import sys, re, random, time, pickle
sys.path.insert(0,'/Users/dc/code/math/jc2/cases')
import fastelim as FE
p=105337
t0=time.time()
# ---- parse GB
txt=open('/tmp/fiber_gb.out').read()
gvars=[v.strip() for v in re.search(r'#variable order:\s*(.+)',txt).group(1).split(',')]
nv=len(gvars); vi={v:i for i,v in enumerate(gvars)}
polys=[]
for s in txt.split('---')[-1].strip()[1:-2].split(',\n'):
    d={}
    for t in s.split('+'):
        fs=t.split('*'); c=int(fs[0]); e=[0]*nv
        for f in fs[1:]:
            m=re.match(r'([A-Za-z0-9_]+)\^(\d+)',f)
            if m: e[vi[m.group(1)]]=int(m.group(2))
            else: e[vi[f]]+=1
        d[tuple(e)]=(d.get(tuple(e),0)+c)%p
    polys.append({k:c for k,c in d.items() if c})
FREE=['x53','x55','x58','x60','x62','x63','x65','x66','x68','x70','x71','x72','x73']
BOUNDX=['x47','x52','x54','x57','x59']
W4={"W1":57673,"W2":53212}
def r4(a):
    for x in range(2,p):
        if pow(x,4,p)==a: return x
    return None
w1r, w2r = r4(W4["W1"]), r4(W4["W2"])
print("4th roots exist:", w1r is not None, w2r is not None, flush=True)
def ev(d,val):
    tot=0
    for k,c in d.items():
        m=c
        for i,e in enumerate(k):
            if e:
                if val[i] is None: return None
                m=m*pow(val[i],e,p)%p
        tot=(tot+m)%p
    return tot
def subs(d,val):
    out={}
    for k,c in d.items():
        m=c; ke=[0]*nv
        for i,e in enumerate(k):
            if e:
                if val[i] is None: ke[i]=e
                else: m=m*pow(val[i],e,p)%p
        ke=tuple(ke)
        out[ke]=(out.get(ke,0)+m)%p
    return {k:c for k,c in out.items() if c}
def uniroots(d,i):
    cs={}
    for k,c in d.items(): cs[k[i]]=(cs.get(k[i],0)+c)%p
    dg=max(cs)
    if dg==0: return None
    if dg==1:
        a,b=cs.get(1,0),cs.get(0,0)
        return [(-b)*pow(a,p-2,p)%p]
    return [x for x in range(p) if sum(c*pow(x,e,p) for e,c in cs.items())%p==0]
pts=[]; tries=0
rng=random.Random(2026)
while len(pts)<12 and tries<40:
    tries+=1
    val=[None]*nv
    for v in FREE: val[vi[v]]=rng.randrange(0,p)
    s1=rng.choice([1,-1]); s2=rng.choice([1,-1])
    i1=rng.choice([0,1]); i2=rng.choice([0,1])
    # 4 roots each: w, -w, iw, -iw (i = sqrt(-1) mod p, p%4==1)
    ii=pow(pow(3,(p-1)//4,p),1,p)
    ii=next(x for x in range(2,p) if x*x%p==p-1)
    w1=w1r*(ii if i1 else 1)*(s1%p)%p; w1=w1 if s1>0 else (p-w1)%p
    w2=w2r*(ii if i2 else 1)%p; w2=w2 if s2>0 else (p-w2)%p
    val[vi["W1"]]=w1; val[vi["W2"]]=w2
    val[vi["uW1"]]=pow(w1,p-2,p); val[vi["uW2"]]=pow(w2,p-2,p)
    unk=set(BOUNDX)
    progress=True
    ok=True
    while unk and progress and ok:
        progress=False
        for d in polys:
            sd=subs(d,val)
            if not sd: continue
            sup={i for k in sd for i,e in enumerate(k) if e}
            if not sup:
                ok=False; break
            if len(sup)==1:
                i=next(iter(sup))
                rs=uniroots(sd,i)
                if rs is None: continue
                if not rs: ok=False; break
                val[i]=rs[0]; unk.discard(gvars[i]); progress=True
        if not ok: break
    if not ok or unk: continue
    if all(ev(d,val)==0 for d in polys):
        pts.append(list(val))
print("F_p points found: %d (in %d tries, %.0fs)"%(len(pts),tries,time.time()-t0), flush=True)
if not pts:
    print("NO F_p-rational points sampled (variety nonempty over closure; rational sampling failed)")
    sys.exit(0)
# ---- reconstruct D21 chart + D23 Row_22 filter
eng,resid,plog,strips,pt,census=FE.run_core2(p, verbose=False)
print("engine ready %.0fs"%(time.time()-t0), flush=True)
import directionb_residual32_emit as E32
_,names,_,_,_=E32.load_rows()
name_of={names[i]:i for i in names}          # xN -> vid (D21 registry)
st23=pickle.load(open('/tmp/directionb_tails_D23.pkl','rb'))
byk23, vars23 = st23["byk"], st23["vars"]
r22=byk23[22]
h32=pt["HW1"]*pow(pt["W1"],p-2,p)%p
A1v,A2v=pt["A1"],pt["A2"]
UNK54=[v for v in vars23 if v[:2] in ("tf","tg") and v.rsplit("_",1)[-1] in ("49","54")]
survivors=0; details=[]
for DRAW in (0,1,2):
    FRNG=random.Random(777+DRAW)
    print("--- auxiliary-free draw %s ---"%("zeros" if not DRAW else "random#%d"%DRAW), flush=True)
    for pi,val in enumerate(pts):
        # D21 var values by NAME
        dval={}
        for j,gv in enumerate(gvars):
            if gv in ("W1","W2","uW1","uW2"): continue
            dval[eng.vars_[eng.occ[[names[i] for i in eng.occ].index(gv)]] if False else None]=None
        # simpler: map gvars xN -> registry name via names
        dval={}
        for j,gv in enumerate(gvars):
            if gv.startswith("x"):
                vid=name_of[gv]
                dval[eng.vars_[vid]]=val[j]
        W1v,W2v=val[vi["W1"]],val[vi["W2"]]
        for nm in vars23:
            if nm not in dval and nm[:2] in ("tf","tg","uf","vf"):
                lv=nm.rsplit("_",1)[-1]
                if nm.startswith(("bf","bg")) or lv in ("42",):
                    dval[nm]=0                  # B-side + pins stay 0
                elif lv in ("49","53","54"):
                    dval[nm]=0                  # deep unknowns (49/54 solved)
                else:
                    dval[nm]=FRNG.randrange(0,p) if DRAW else 0
        # back-solve the 22 pivots on the D21 engine at this point
        gval=[0]*(eng.nt+6)
        for j,vid in enumerate(eng.occ):
            gval[j]=dval.get(eng.vars_[vid],0)
        gval[eng.nt+0]=A1v; gval[eng.nt+1]=A2v
        gval[eng.nt+2]=W1v; gval[eng.nt+3]=h32*W1v%p
        gval[eng.nt+4]=W2v; gval[eng.nt+5]=h32*W2v%p
        pividx=[(gx,lab) for gx,lab,_ in plog]
        rowsP={lab:eng.P[eng.labs.index(lab)] for _,lab in pividx}
        for gx,lab in reversed(pividx):
            P=rowsP[lab]; cp=P.derivative(gx)
            v0=list(gval); v0[gx]=0
            b=int(P(*v0))%p; c=int(cp(*v0))%p
            gval[gx]=(-b)*pow(c,p-2,p)%p
        for j,vid in enumerate(eng.occ):
            dval[eng.vars_[vid]]=gval[j]
        # sanity: all 22 pivot rows vanish
        assert all(int(rowsP[lab](*gval))%p==0 for _,lab in pividx)
        # Row_22 affine system on the 49/54-level unknowns
        ui={nm:i for i,nm in enumerate(UNK54)}
        rows=[]; rhs=[]
        okpt=True
        for n,v in sorted(r22.items()):
            row=[0]*len(UNK54); b=0
            for vk,r in v.items():
                nms=[vars23[i] for i in vk]
                us=[nm for nm in nms if nm in ui]
                if len(us)>1: okpt=False; break
                m=1
                for nm in nms:
                    if nm in ui: continue
                    m=m*dval.get(nm,0)%p
                    if m==0: break
                if m==0: continue
                import r1_fullcore as FC
                rv=0
                for (z,e1,e2,pw,h1,qw,h2,B),c in r.items():
                    x=(FC.frmod(c[0],p)+FC.frmod(c[1],p)*pt["r3"])%p
                    x=x*pow(A1v,e1,p)*pow(A2v,e2,p)*pow(h32,h1+h2,p)%p
                    x=x*pow(W1v,pw+h1,p)*pow(W2v,qw+h2,p)%p
                    rv=(rv+x)%p
                if rv==0: continue
                if us: row[ui[us[0]]]=(row[ui[us[0]]]+m*rv)%p
                else: b=(b+m*rv)%p
            if not okpt: break
            rows.append(row); rhs.append((-b)%p)
        if not okpt:
            details.append((pi,"NONAFFINE")); continue
        # rank test
        M=[r[:] for r in rows]; R=rhs[:]; rk=0; incons=False
        for c in range(len(UNK54)):
            pr=next((i for i in range(rk,len(M)) if M[i][c]),None)
            if pr is None: continue
            M[rk],M[pr]=M[pr],M[rk]; R[rk],R[pr]=R[pr],R[rk]
            iv=pow(M[rk][c],p-2,p)
            M[rk]=[x*iv%p for x in M[rk]]; R[rk]=R[rk]*iv%p
            for i in range(len(M)):
                if i!=rk and M[i][c]:
                    f=M[i][c]
                    M[i]=[(a-f*bb)%p for a,bb in zip(M[i],M[rk])]
                    R[i]=(R[i]-f*R[rk])%p
            rk+=1
        for i in range(len(M)):
            if not any(M[i]) and R[i]: incons=True
        if incons: details.append((pi,"DIES at depth 23"))
        else:
            survivors+=1
            details.append((pi,"SURVIVES depth 23 (rank %d/%d, %d free deep tails)"%(rk,len(UNK54),len(UNK54)-rk)))
for pi,msg in details: print("  point %d: %s"%(pi,msg))
print("FILTER VERDICT: %d/%d sampled fiber points SURVIVE the D23 Row_22 conditions"%(survivors,len(pts)), flush=True)
if survivors: print("*** LOUD: genuine mod-p residue-A germ candidates through depth 23 ***")
