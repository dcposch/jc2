import sys; sys.path.insert(0,'/tmp/mfs')
from lib import n_from_delta, partitions_into
# W=2 column of (B3): S=1, d=1, a=N-2, K-total = N-3 spread over exactly beta charged cusps
def phi_w2(N,beta):
    a=N-2; Kt=a-1; d=1; MF=N-1
    best=None
    if Kt<beta: return None
    for K in partitions_into(Kt,beta,Kt):
        mults=[max(2,1+k) for k in K]+[2]          # cusps + the mandatory multibranch point
        deltas=[m*(m-1)//2 for m in mults[:-1]]+[1]
        ms=sorted(mults,reverse=True)
        v=max(MF,1+ms[0],ms[0]+ms[1],n_from_delta(sum(deltas)))
        if best is None or v<best: best=v
    return best
print("(B3), W=2 column : sharpened floor Phi as a function of beta = #singular-branch points")
print(" N | banked  beta=1  2   3   4   5   6   >=7 (min over beta)")
for N in range(4,21):
    row=[phi_w2(N,b) for b in range(1,8)]
    mn=min([v for v in row if v is not None]+[phi_w2(N,b) for b in range(1,N-2) if phi_w2(N,b)])
    print("%2d | %5d  %s | min=%d"%(N,N-1," ".join('  - ' if v is None else '%3d '%v for v in row),mn))
