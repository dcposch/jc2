#!/usr/bin/env python3
import sys
import numpy as np
P=32009
raw=np.fromfile(sys.argv[1],dtype='<u4')
n=int(raw[0]);assert n==1792 and len(raw)==1+n*n
A=raw[1:].reshape(n,n).astype(np.int64)
determinant=1
for k in range(n):
    nonzero=np.flatnonzero(A[k:,k])
    assert len(nonzero), 'zero determinant'
    pivot=k+int(nonzero[0])
    if pivot!=k:
        A[[k,pivot]]=A[[pivot,k]]
        determinant=-determinant % P
    value=int(A[k,k]);determinant=determinant*value % P
    inverse=pow(value,-1,P)
    factors=A[k+1:,k]*inverse % P
    A[k+1:,k+1:]=(A[k+1:,k+1:]-factors[:,None]*A[k,k+1:]) % P
    A[k+1:,k]=0
print('DET_MOD_P='+str(determinant),flush=True)
print('INDEPENDENT_NUMPY_FULL_RANK_PASS',flush=True)
