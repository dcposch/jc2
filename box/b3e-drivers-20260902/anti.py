from fractions import Fraction
# G-ANTI: counting-admissible (THEOREM PROFILE / (C1),(K),(C2)) vs covering-admissible
# (Riemann-Hurwitz on Ebar~ -> P^1 of degree a, ramified only over the 1+R punctures).
#
# counting side (case B3, H2):  N>=4 ; N/2 < a <= N-2 ; W=N-a>=2 ;
#   profile = multiset of singular points p with r_p>=1, K_p>=0, sum K_p = a-1,
#   a_p = N - r_p*W - K_p >= 0, K_p <= D_gap = 2a-N at multibranch points (C2),
#   at least one cusp (r=1, singular) and at least one multibranch point (r>=2).
# covering side: over each of the r_p punctures at p, a_p points are unramified
#   (F etale), the remaining degree a-a_p = (r_p-1)W+K_p sits on places of E at
#   infinity, so   a - n_P <= max(0, a-a_p-1);  over the infinity puncture a-n <= a-1.
#   RH:  2g-2 = -2a + sum_P (a-n_P)   =>   2g <= -a-1 + sum_p r_p*max(0,(r_p-1)W+K_p-1)
def gmax(N,a,pts):           # pts = list of (r_p,K_p)
    W=N-a
    return (1-a+sum(r*max(0,(r-1)*W+K-1) for r,K in pts))/2
rows=[]
for N in range(4,21):
    for a in range((N+1)//2, N-1):
        W=N-a; Dgap=2*a-N
        # minimal B3 profile: one cusp (r=1,K=Kc) + one multibranch (r=2,K=Km), Kc+Km=a-1
        best=None
        for Km in range(0, min(a-1,Dgap)+1):
            Kc=a-1-Km
            if N-1*W-Kc<0 or N-2*W-Km<0: continue
            g=gmax(N,a,[(1,Kc),(2,Km)])
            if best is None or g>best[0]: best=(g,Kc,Km)
        rows.append((N,a,W,Dgap,best))
print(" N   a   W  Dgap   max g admissible (minimal B3 profile: 1 cusp + 1 double point)")
bad=[]
for N,a,W,Dgap,b in rows:
    if b is None: print(f"{N:3d} {a:3d} {W:3d} {Dgap:5d}   -- no admissible minimal profile --"); continue
    g,Kc,Km=b
    flag="" if g>=0 else "   <-- EMPTY (covering window closed)"
    if g<0: bad.append((N,a))
    print(f"{N:3d} {a:3d} {W:3d} {Dgap:5d}   g <= {g}   (K_cusp={Kc}, K_mult={Km}){flag}")
print("\ncells with an empty covering window:", bad if bad else "NONE  -> no crossing at any N in 4..20")
