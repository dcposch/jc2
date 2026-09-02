import sys; sys.path.insert(0,'/tmp/degaf')
from sg import gamma, deg
def analyse(name,a,b,Mbig,window):
    G=set(gamma(a,b,Mbig)); da,db=deg(a),deg(b)
    # trust Gamma only on [0,window]
    gp=[m for m in range(window+1) if m not in G]
    c=(max(gp)+1) if gp else 0
    sym=all(((z in G)!=((c-1-z) in G)) for z in range(c))
    mg=[]
    for g in sorted(G):
        if 0<g<=window and not any((g-h) in G and g-h>0 for h in mg): mg.append(g)
    print(f"{name}: (deg a,deg b)=({da},{db}) n=max={max(da,db)}  delta_aff={len(gp)} c={c} sym={sym} mingens={mg}")
    return len(gp),c,mg
analyse("(9,6) Chau realised",[0,24,0,0,0,12,0,0,0,1],[0,0,8,0,0,0,1],600,60)
analyse("(9,6) variant (t^9, t^6+t)",[0]*9+[1],[0,1,0,0,0,0,1],600,60)
analyse("(t^6+t^5, t^4)",[0,0,0,0,0,1,1],[0,0,0,0,1],400,60)
analyse("generic (3,5): (t^3+t, t^5+t^2+t)",[0,1,0,1],[0,1,1,0,0,1],400,40)
analyse("generic (3,7)",[0,2,0,1],[0,1,3,0,1,0,0,1],500,60)
analyse("generic (4,5)",[0,1,1,0,1],[0,2,0,1,0,1],500,60)
analyse("generic (5,7)",[0,1,2,0,1,1],[0,1,0,3,1,0,0,1],800,80)
