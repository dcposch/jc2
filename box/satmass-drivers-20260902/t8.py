from math import ceil, floor
print("TABLE C2.  The price of SAT-MASS per (N,W), 4 <= N <= 16.")
print("  profile: a=N-W, ceil(N/2)<=a<=N-2;  S<=floor(W/2) [7.B'];  ell<=S;  kappa<=N.")
print("  P0+1 = reviewed MERIDIAN-FLOOR+ floor on n (S=1 gauge).")
print("  DIRECT (needs ell=1, i.e. W<=3):  D<=2(T+kappa) => tau <= 50-N closes N outright.")
print("  |A|<=1 route (any W):             D<=4T+2kappa  => tau <= 25-N/2.")
print("  CARRY route (charge's):           n <= (100-kappa-tau)/S.")
print()
h=f"{'N':>3}{'W':>3}{'Wmax':>5}{'Smax':>5}{'ell=1?':>7}{'P0+1':>6}{'tau_direct':>11}{'tau_|A|<=1':>11}{'carry n<=(tau=1)':>17}"
print(h); print("-"*len(h))
for N in range(4,17):
    Wmax=N//2
    for W in range(2,Wmax+1):
        a=N-W
        if not (ceil(N/2)<=a<=N-2): continue
        Smax=max(1,W//2); S=1
        P0=ceil((N-1)/(W-S))+1
        forced = "YES" if W<=3 else "no"
        td = 50-N if W<=3 else None
        ta = 25-N/2
        carry=(100-N-1)//Smax
        print(f"{N:3d}{W:3d}{Wmax:5d}{Smax:5d}{forced:>7}{P0:6d}"
              f"{(str(td) if td is not None else '--'):>11}{ta:11.1f}{carry:17d}")
print()
print("Corollaries at the charged cells:")
for N,W in [(4,2),(5,2),(6,2),(6,3),(7,2),(8,2),(8,4),(12,3),(16,2),(16,8)]:
    if W<=3: print(f"   (N,W)=({N},{W}): ell=1 forced; T<=%d closes N OUTRIGHT (no n-ceiling needed)."%(50-N))
    else:    print(f"   (N,W)=({N},{W}): ell<= {W//2}; direct route unavailable; need |A|<=1 (tau<=%.1f) or the carry route."%(25-N/2))
