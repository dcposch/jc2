import sys, os, time, pickle, random
os.environ["DIRECTIONB_STATE"]="/tmp/directionb_tails_D23.pkl"
sys.path.insert(0,'/Users/dc/code/math/jc72108/cases')
import fastelim as FE
import directionb_residual32_emit as E32
HERE='/Users/dc/code/math/jc72108/cases'
RADG=FE.RADG
OK=[]
def chk(n,c):
    OK.append((n,bool(c))); print(("PASS " if c else "FAIL ")+n, flush=True)
PIV22=[("tf1_44",(12,2)),("tf2_44",(12,5)),("tf1_46",(14,0)),("tf2_46",(14,3)),
       ("tf1_43",(16,1)),("tf1_48",(16,4)),("tf2_43",(16,7)),("tf2_48",(16,10)),
       ("tf1_45",(18,2)),("tf1_50",(18,5)),("tf2_45",(18,8)),("tf2_50",(18,11)),
       ("tf1_47",(20,0)),("tf1_52",(20,3)),("tf2_47",(20,6)),("tf2_52",(20,9)),
       ("tf1_38",(6,2)),("tf1_40",(8,0)),("tf2_40",(8,3)),("tf1_39",(12,8)),
       ("tf1_41",(14,6)),("tf2_41",(14,9))]
t00=time.time()
for p in (105337, 105673, 200257):
    t0=time.time()
    r3v, pt = FE.r3_of(p)
    eng = FE.Engine(p, r3v)
    hdr21, char21, eqs21 = E32.FCparse("directionb_core2_p%d.ms"%p)
    assert char21==p
    core21rows=eqs21[:38]; radsat=eqs21[38:]
    pivlabs=[lab for _,lab in PIV22]
    extra=[lab for lab in eng.labs if lab in pivlabs or lab[0]==22]
    body2=[]; names_extra=set(); nterm2=0; mdg=0
    _,names,_,_,_=E32.load_rows()
    # xN names for D21-registry vars; D23-only vars get their own names
    imap={}
    nxt=[74]
    v21list=pickle.load(open('/tmp/directionb_tails_D21.pkl','rb'))["vars"]
    name2x={}
    for vid,xn in names.items(): name2x[v21list[vid]]=xn
    def xname(nm):
        if nm in name2x: return name2x[nm]
        if nm not in imap:
            imap[nm]="x%d"%nxt[0]; nxt[0]+=1
        return imap[nm]
    for lab in extra:
        v=eng.P0[eng.labs.index(lab)]
        d=FE.mp_to_dict(v)
        parts=[]
        for k in sorted(d):
            mono=[]
            for j in range(eng.nt):
                if k[j]:
                    nm=xname(eng.vars_[eng.occ[j]]); names_extra.add(nm)
                    mono.append(nm+("^%d"%k[j] if k[j]>1 else ""))
            for j in range(6):
                if k[eng.nt+j]: mono.append(RADG[j]+("^%d"%k[eng.nt+j] if k[eng.nt+j]>1 else ""))
            parts.append("%d%s"%(d[k],"*"+"*".join(mono) if mono else ""))
            mdg=max(mdg,sum(k))
        nterm2+=len(d)
        body2.append("+".join(parts))
    hdr=[h for h in hdr21 if h not in ("uW1","uW2","uA") and h not in RADG]
    hdr=hdr+sorted(names_extra-set(hdr))+list(RADG)+["uW1","uW2","uA"]
    path="%s/directionb_core23_p%d.ms"%(HERE,p)
    with open(path,"w") as f:
        f.write(", ".join(hdr)+"\n%d\n"%p)
        f.write(",\n".join(core21rows+body2+radsat)+"\n")
    txt=open(path).read(); assert "(" not in txt and ")" not in txt
    sz=os.path.getsize(path)
    print("p=%d: D23-core-v2 = 38 compressed + %d pristine (22 pivot + 10 Row_22) rows; +%d terms (deg<=%d); %d vars, %d eqs, %dB (%.0fs)"%(
        p,len(extra),nterm2,mdg,len(hdr),38+len(extra)+len(radsat),sz,time.time()-t0), flush=True)
    h3,c3,e3=E32.FCparse("directionb_core23_p%d.ms"%p)
    chk("[p=%d] REGRESSION: first 38 emitted rows byte-identical to "
        "directionb_core2_p%d.ms rows"%(p,p), e3[:38]==core21rows and c3==p)
print("ALL PRIMES %.0fs"%(time.time()-t00), flush=True)
bad=[n for n,c in OK if not c]
print("V2 TOTAL: %d checks, %d FAIL %s"%(len(OK),len(bad),bad or ""))
