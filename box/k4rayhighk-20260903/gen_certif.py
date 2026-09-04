#!/usr/bin/env python3
"""Homogeneous-chart certificate: hilb numerator + cst^N in I + lift verification."""
import sys
sys.path.insert(0, "/home/ubuntu/jc2/box/k4rayhighk-20260903")
import gen_hk

K = int(sys.argv[1]); Bdeg = int(sys.argv[2]); ch = sys.argv[3]; Nmax = int(sys.argv[4])
pre, names, wts = gen_hk.direct(K, Bdeg, ch, 4)
L = [pre]
A = L.append
A('print("CERT__STD_BEGIN 1"); timer=1; int t0=timer;')
A("ideal GI = std(ROWS);")
A('print("CERT__STD_SECONDS "+string(timer-t0));')
A('print("CERT__BASIS_SIZE "+string(size(GI)));')
A('print("CERT__DIM "+string(dim(GI)));')
A('intvec HN = hilb(GI,1);')
A('print("CERT__HILB_NUM "+string(HN));')
A('poly cp = CSTP; int nn; int nz; int jj; poly rr; poly ck; matrix LFT;')
A('for (nn=1; nn<=' + str(Nmax) + '; nn++) {')
A('  rr = reduce(cp,GI);')
A('  print("CERT__CST_POW_IN_I "+string(nn)+" "+string(rr==0));')
A('  if (rr==0) { LFT = lift(ROWS,cp); ck = cp - (matrix(ROWS)*LFT)[1,1];')
A('    nz=0; for(jj=1;jj<=nrows(LFT);jj++){ if(LFT[jj,1]!=0){nz++;} }')
A('    print("CERT__LIFT_VERIFY "+string(nn)+" "+string(ck==0)+" support "+string(nz)); break; }')
A('  cp = cp*CSTP; }')
A('print("CERT__DONE 1"); quit;')
print("\n".join(L))
