import sys; sys.path.insert(0,'/tmp/mfs')
from price import cell
from delta import min_delta
print("N   W   a  Dgap | MF_banked  Phi(B1) Phi(B2) Phi(B3) | Phi  gain  C=Phi-1 | dlo(B2) dlo(B3)")
for N in range(4,21):
    for W in range(2,N//2+1):
        a=N-W; Dg=N-2*W; banked=-(-(N-1)//(W-1))
        vals={}; dlo={}
        for c in ('B1','B2','B3'):
            if c=='B1' and N<=16: vals[c]=None; dlo[c]=None; continue
            r=cell(N,W,c); vals[c]= None if r is None else r[0]
            q=min_delta(N,W,c); dlo[c]= None if q is None else q[0]
        live=[v for v in vals.values() if v is not None]
        Phi=min(live) if live else None
        f=lambda v:('  -  ' if v is None else '%4d '%v)
        g=lambda v:('  - ' if v is None else '%3d '%v)
        print("%2d %3d %3d %4d  | %8d   %s%s%s | %s %s  %s | %s%s"%(
            N,W,a,Dg,banked,f(vals['B1']),f(vals['B2']),f(vals['B3']),
            g(Phi),g(None if Phi is None else Phi-banked),g(None if Phi is None else Phi-1),
            g(dlo['B2']),g(dlo['B3'])))
    print()
