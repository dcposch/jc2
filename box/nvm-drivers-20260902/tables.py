import math
print("TABLE T1  (N,W): P0 = ceil((N-1)/(W-1)) = guaranteed floor on p;")
print("           n_min >= P0+1;  D_min >= P0+2 (S=1,kappa=1);  at W=2 D_min >= N+1.")
print("  N |" + "".join("   W=%-2d " % W for W in range(2,7)))
for N in range(4,21):
    row = "%3d |" % N
    for W in range(2,7):
        a = N - W
        if not (math.ceil(N/2) <= a <= N-2):
            row += "   --  "; continue
        P0 = math.ceil((N-1)/(W-1))
        row += " %2d/%2d/%2d" % (P0, P0+1, P0+2) if False else " %2d/%-3d" % (P0, P0+2)
    print(row)
print("\n   entries are  P0 / D-floor  where D-floor = P0+2 (guaranteed) ")
print("   [at W=2, S=1 is forced and the sharper floor is D_min >= N+1]")
print()
print("TABLE T2  crossing price, three ledgers, guaranteed (S=1,kappa=1) form")
print("  N  W |  DEG-AF crossing (n)    this lane (p)      this lane (D)")
for N in [4,5,6,8,10,11,12,14,16,20]:
    for W in [2,3,4]:
        a = N-W
        if not (math.ceil(N/2) <= a <= N-2): continue
        P0 = math.ceil((N-1)/(W-1))
        print("  %2d  %d |  n_min <= %-3d          p <= %-3d (n<=%-3d)   D_min <= %-3d"
              % (N, W, P0-1, P0-1, P0, P0+1))
print()
print("TABLE T3  conditional ceiling  n <= (2N+kappa)/(W-S) <= 3N  [OPEN[ANTICANON-DEFECT]]")
print("          window for n at (N,W) with S=1, kappa<=N:")
print("  N |" + "".join("     W=%-2d   " % W for W in range(2,7)))
for N in range(4,17):
    row = "%3d |" % N
    for W in range(2,7):
        a = N-W
        if not (math.ceil(N/2) <= a <= N-2):
            row += "     --    "; continue
        lo = math.ceil((N-1)/(W-1))+1
        hi = (2*N+N)//(W-1)
        row += "  [%2d,%3d] " % (lo, hi) if lo <= hi else "   EMPTY   "
    print(row)
