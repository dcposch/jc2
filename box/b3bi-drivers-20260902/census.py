from functools import lru_cache
from itertools import product

# P(m,r) = number of partitions of m into exactly r parts
@lru_cache(None)
def P(m,r):
    if m==0 and r==0: return 1
    if m<=0 or r<=0: return 0
    return P(m-1,r-1)+P(m-r,r)

def rows(m):
    """DO local rows for a fork of longitudinal degree m at a valence-3 target
    vertex: triples of partitions of m, one per direction, with total #parts m+2."""
    tot=0
    for rL in range(1,m+1):
        for rR in range(1,m+1):
            rD = m+2-rL-rR
            if 1<=rD<=m:
                tot += P(m,rL)*P(m,rR)*P(m,rD)
    return tot

print("m  : ", " ".join("%6d"%m for m in range(2,13)))
print("Rows: ", " ".join("%6d"%rows(m) for m in range(2,13)))
print()
print(" N   #fork-types(m,n)  raw local rows   ratio")
prev=None
for N in range(4,15):
    ft=sum(N//m for m in range(2,N+1))
    c =sum((N//m)*rows(m) for m in range(2,N+1))
    r = "" if prev is None else "%8.2f"%(c/prev)
    print("%3d %10d %16d %s"%(N,ft,c,r))
    prev=c
