from itertools import combinations_with_replacement as cwr

def dicriticals(W):
    """multisets {(s_l,mu_l)} with sum s*mu = W, mu>=2, s>=1"""
    out=[]
    def rec(rem, start, acc):
        if rem==0: out.append(tuple(acc)); return
        cand=[(s,mu) for mu in range(2,rem+1) for s in range(1,rem//mu+1) if s*mu<=rem]
        for c in cand:
            if c<start: continue
            rec(rem-c[0]*c[1], c, acc+[c])
    rec(W,(0,0),[])
    return out

def b3_profiles(N, kmax=3, rmax=6):
    res=[]
    for a in range((N+1)//2, N-1):
        W=N-a; Dgap=2*a-N
        if W<2: continue
        for dic in dicriticals(W):
            R=sum(s-1 for s,mu in dic)
            smin=min(s for s,mu in dic)
            Ktot=a-1
            # charged points: K_p>=1 ; by Lem 4.2 (R=0 case) they carry a singular branch
            # cusp = (r=1, singular);  charged multibranch = (r>=2, has singular branch)
            charged=[]
            def rec(rem, start, acc):
                if rem==0:
                    charged.append(tuple(acc)); return
                for r in range(1,rmax+1):
                    for K in range(1,rem+1):
                        if r>=2 and K>Dgap: continue
                        ap=N-r*W-K
                        if ap<0: continue
                        c=(r,K,ap)
                        if c<start: continue
                        rec(rem-K,c,acc+[c])
            rec(Ktot,(0,0,0),[])
            for cp in charged:
                if not any(r==1 for r,K,ap in cp): continue      # need >=1 cusp
                # uncharged multibranch pts: r>=2, K=0, all branches smooth
                unch=[(r,0,N-r*W) for r in range(2,rmax+1) if N-r*W>=0 and (0<=Dgap)]
                if not unch: continue
                # (C3) #{K_p>0} <= R + beta ; beta = #singular-branch points = #charged
                if len(cp) > R + len(cp): pass
                res.append((a,W,Dgap,dic,cp,tuple(sorted(set(unch)))))
    return res

for N in (5,6,7):
    print("="*74); print("N =",N)
    for a,W,Dg,dic,cp,unch in b3_profiles(N):
        mer = "1^%d"%a + "".join(" . %d^%d"%(mu,s) for s,mu in dic)
        print("  a=%d W=%d Dgap=%d  dicriticals=%s  meridian=%s"%(a,W,Dg,list(dic),mer))
        print("      charged (r,K,a_p): %s"%(list(cp),))
        print("      uncharged multibranch (r,K,a_p) allowed: %s"%(list(unch),))
