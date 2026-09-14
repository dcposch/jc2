#!/usr/bin/env python3
"""Expected (Froberg-type) weighted Hilbert function for I_{t,+}: 2t-1 forms of weights 4t+1-k (k=1..2t-1)
in variables of weights 1..t-1, t+1.  H_exp(w) = [s^w] prod(1-s^{d_i}) / prod(1-s^{w_j}), truncated at the
first non-positive coefficient.  Compare with measured HF and record predicted socle s_t vs 8t+2 and 4t+1."""
import sys
measured = {
 2: [1,1,1,2,2,2,2,1],                       # exact, y=2/5 (t2p_main.out)
 3: [1,1,2,2,4,4,6,6,8,7,8,6,6,3,2],         # exact (t3_main.out)
 4: [1,1,2,3,4,6,8,10,13,16,19,22,25,27,29,30,29,28,25,20,14,6],  # exact (t4_main.out)
 5: [1,1,2,3,5,6,10,12,17,21,28,33,43,49,60,68,80,87,100,105,115,118,124,120,121,109,100,80,61,29,1],  # mod 32009
 6: [1,1,2,3,5,7,10,14,19,25,33,42,54,67,83,101,122,145,171,199,230,262,296,330,365,399,431,460,485,504,516,519,512,493,460,413,349,269,170,54],  # mod 32003
}
def series(t, W):
    wts = list(range(1,t)) + [t+1]
    degs = [4*t+1-k for k in range(1,2*t)]
    c = [0]*(W+1); c[0]=1
    for w in wts:                       # multiply by 1/(1-s^w)
        for i in range(w, W+1): c[i] += c[i-w]
    for d in degs:                      # multiply by (1-s^d)
        for i in range(W, d-1, -1): c[i] -= c[i-d]
    return c
for t in range(2, 19):
    W = 12*t+40
    c = series(t, W)
    # truncate at first non-positive coefficient
    H = []
    for x in c:
        if x <= 0: break
        H.append(x)
    s_pred = len(H)-1
    m = measured.get(t)
    agree = (m == H) if m else None
    print(f"t={t:2d} socle_pred={s_pred:3d} len={sum(H):7d}  8t+2={8*t+2:3d} 4t+1={4*t+1:3d}  forced_square={8*t+2>s_pred}  tau_not_forced={4*t+1<=s_pred}  measured_agree={agree}")
    if m and m != H:
        print("   measured:", m); print("   predicted:", H); print("   raw series:", c[:len(m)+3])
