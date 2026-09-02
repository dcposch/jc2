import sys; sys.path.insert(0,'/tmp/mfs')
from price import cell
from delta import min_delta
hdr=" N  W   a Dg | MFb  B1  B2  B3 | Phi gain  C | dB2 dB3"
print(hdr)
for N in range(4,21):
    for W in range(2,N//2+1):
        a=N-W; Dg=N-2*W; banked=-(-(N-1)//(W-1))
        v={}; d={}
        for c in ('B1','B2','B3'):
            if c=='B1' and N<=16: v[c]=None; d[c]=None; continue
            r=cell(N,W,c); v[c]=None if r is None else r[0]
            q=min_delta(N,W,c); d[c]=None if q is None else q[0]
        live=[x for x in v.values() if x is not None]; Phi=min(live) if live else None
        f=lambda x,w=3:(' '*(w-1)+'-' if x is None else ('%'+str(w)+'d')%x)
        print("%2d %2d %3d %2d | %3d %s %s %s | %3d %3d %4d | %s %s"%(
            N,W,a,Dg,banked,f(v['B1']),f(v['B2']),f(v['B3']),Phi,Phi-banked,Phi-1,f(d['B2']),f(d['B3'])))
