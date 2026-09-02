"""Re-derivation of the H2 profile thresholds and of the delta_aff strength each
consumer needs.  Constraints used (MPRIME, re-derived here):
  N = a + W,  W = sum_l s_l mu_l >= 2,  mu_l >= 2 (7.B'),  S := sum_l s_l <= W//2
  sheet gate  1 <= a <= N-2 ;  D_gap := 2a-N ;  K_p <= D_gap at multibranch p
  sum_p K_p = a-1 ;  a_p = a - (r_p-1)W - K_p >= 0
  (C3)  #{p : K_p>0} <= R + beta,  R = sum_l (s_l-1) <= floor(W/2) - 1
  (5.3) a-1 <= (R+beta) D_gap
"""
from math import ceil, floor

def Rmax(W): return W//2 - 1

def beta_min(N):
    """least beta for which some admissible a satisfies (5.3)."""
    for beta in range(0, 60):
        for a in range(1, N-1):
            W=N-a; Dg=2*a-N
            if W<2 or Dg<0: continue
            if a-1 <= (Rmax(W)+beta)*Dg: return beta, a, W, Dg
    return None

print("N   beta_min   witness (a,W,D_gap)   delta_aff needed to KILL (B2)   [<= 2*beta_min-1]")
for N in range(4,21):
    r=beta_min(N)
    if r is None: print(N,"none"); continue
    b,a,W,Dg=r
    need = 2*b-1
    print(f"{N:2d}    {b:2d}        (a={a},W={W},Dgap={Dg})            "
          f"{'delta_aff <= %d'%need if b>=1 else 'B2 already empty'}")
print()
print("MERIDIAN-FLOOR   n_min >= ceil((N-1)/(W-S)),  guaranteed form S=1: ceil((N-1)/(W-1))")
print("N   W-range        max guaranteed floor (at W=2)   floor at W=floor(N/2)")
for N in range(4,21):
    ws=[N-a for a in range(1,N-1) if N-a>=2]
    f2 = ceil((N-1)/1) if 2 in ws else None
    wmax=max(ws)
    fm = ceil((N-1)/(wmax-1))
    print(f"{N:2d}  W in [2,{wmax}]      n_min >= {f2}                    n_min >= {fm}")
