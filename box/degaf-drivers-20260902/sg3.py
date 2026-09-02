P=(1<<61)-1
def pmul(u,v,M):
    r=[0]*min(len(u)+len(v)-1,M+1)
    for i,ui in enumerate(u):
        if ui:
            lim=min(len(v),M+1-i)
            for j in range(lim):
                if v[j]: r[i+j]=(r[i+j]+ui*v[j])%P
    return r
def deg(u):
    d=len(u)-1
    while d>=0 and u[d]%P==0: d-=1
    return d
def gamma(a,b,M):
    da,db=deg(a),deg(b); piv={}
    apow=[1]; i=0
    while i*da<=M:
        row=apow[:]; j=0
        while i*da+j*db<=M:
            v=row+[0]*(M+1-len(row))
            while True:
                d=deg(v)
                if d<0: break
                if d in piv:
                    c=v[d]*pow(piv[d][d],P-2,P)%P
                    pv=piv[d]; v=[(v[k]-c*pv[k])%P for k in range(d+1)]+[0]*(M-d)
                else:
                    piv[d]=v; break
            row=pmul(row,b,M); j+=1
        apow=pmul(apow,a,M); i+=1
    return set(piv.keys())
def analyse(name,a,b,M,window):
    G=gamma(a,b,M); da,db=deg(a),deg(b)
    gp=[m for m in range(window+1) if m not in G]
    c=(max(gp)+1) if gp else 0
    sym=all(((z in G)!=((c-1-z) in G)) for z in range(c))
    mg=[]
    for g in sorted(G):
        if 0<g<=window and not any((g-h) in G and g-h>0 for h in mg): mg.append(g)
    n=max(da,db); pa=(n-1)*(n-2)//2
    print(f"{name:34s} (p,q)=({da:2d},{db:2d}) n={n:2d} delta_aff={len(gp):3d} c={c:3d} sym={str(sym):5s} "
          f"mingens={mg}  p_a={pa} delta_inf={pa-len(gp)}")
    return len(gp),c,mg
if __name__=="__main__":
    analyse("(9,6) Chau realised",[0,24,0,0,0,12,0,0,0,1],[0,0,8,0,0,0,1],200,40)
    analyse("(9,6) variant (t^9,t^6+t)",[0]*9+[1],[0,1,0,0,0,0,1],200,40)
    analyse("generic (3,5)",[0,1,0,1],[0,1,1,0,0,1],120,30)
    analyse("generic (3,7)",[0,2,0,1],[0,1,3,0,1,0,0,1],160,30)
    analyse("generic (4,5)",[0,1,1,0,1],[0,2,0,1,0,1],140,30)
    analyse("generic (5,7)",[0,1,2,0,1,1],[0,1,0,3,1,0,0,1],220,40)
    analyse("(t^4,t^6+t^5)",[0,0,0,0,1],[0,0,0,0,0,1,1],120,30)
    analyse("(t^2,t^9)",[0,0,1],[0]*9+[1],80,20)
