#!/usr/bin/env python3
import sys, numpy as np
path,p=sys.argv[1],int(sys.argv[2])
lines=open(path).read().split("\n"); nb=int(lines[0].split("=")[1])
M=np.array([[int(x)%p for x in ln.rstrip(",").split(",")] for ln in lines[1:1+nb]],dtype=np.int64)
assert M.shape==(nb,nb)
det=1; A=M.copy()
for c in range(nb):
    piv=None
    for i in range(c,nb):
        if A[i,c]: piv=i; break
    if piv is None: det=0; break
    if piv!=c: A[[c,piv]]=A[[piv,c]]; det=(-det)%p
    det=det*int(A[c,c])%p; inv=pow(int(A[c,c]),-1,p)
    A[c]=(A[c]*inv)%p
    nz=np.nonzero(A[c+1:,c])[0]+c+1
    for i in nz: A[i]=(A[i]-A[i,c]*A[c])%p
d=det if det<=p//2 else det-p
print(f"{path}: nb={nb} det mod {p} = {d}")
