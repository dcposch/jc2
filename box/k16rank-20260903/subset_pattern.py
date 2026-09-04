"""Compare measured sop (t-1)-subsets of {B_r,C_r} with the coordinate-axis necessary condition:
a subset S is an sop of P_t only if for every variable weight j in {1..t-1} some member has weight
divisible by j (else all members vanish on the q_j-axis).  wt B_r=t+1+r, wt C_r=2t+2+r."""
import re, sys, itertools, pathlib
for t, path in [(3,'rank_t3_mod_p32003_b0.out'),(4,'rank_t4_mod_p32029_b1.out'),(5,'rank_t5_mod_p32009_b0.out'),(6,'rank_t6_mod_p32003_b1.out')]:
    p=pathlib.Path(path)
    if not p.exists(): print(t,'missing'); continue
    txt=p.read_text()
    meas={}
    for m in re.finditer(r"SUBSET (SOP|notsop) (.+)", txt):
        meas[tuple(m.group(2).split())]= (m.group(1)=='SOP')
    if not meas: print(t,'no subset lines yet'); continue
    wt=lambda nm: (t+1+int(nm[1:])) if nm[0]=='B' else (2*t+2+int(nm[1:]))
    agree=0; dis=[]
    for S,ok in meas.items():
        axis_ok = all(any(wt(n)%j==0 for n in S) for j in range(1,t))
        if axis_ok==ok: agree+=1
        else: dis.append((S,ok,axis_ok))
    nsop=sum(meas.values())
    print(f"t={t}: subsets={len(meas)} sop={nsop} notsop={len(meas)-nsop}; axis-condition agrees on {agree}; disagreements={len(dis)}")
    for d in dis[:12]: print("   ", d)
