# Control: general covering formulas (this lane) vs THEOREM B3-N4 (charged, CONFIRMED)
# N=4 (B3): a=2, W=2, one cusp p0 (r=1, K=1, a_p=1), k double points (r=2, K=0, a_p=0)
ok=True
for k in range(1,9):
  for kodd in range(0,k+1):
    a,W=2,2
    R = 1 + 2*k                       # branch punctures of A_F~
    # E~ -> A_F~-bar : degree a=2, branched exactly over the 2*kodd odd-contact punctures
    ram = 2*kodd
    g = (2*(-2) + ram + 2)//2         # 2g-2 = a(-2)+ram
    # places of E at infinity
    n_inf = 2                          # over the puncture at infinity of A_F (unbranched)
    n_inf += 1                         # cusp puncture: a-a_p = 1 -> one place, index 1
    n_inf += 2*kodd*1 + 2*(k-kodd)*2   # node punctures: ramified ->1 place, unramified ->2
    chi = 2-2*g-n_inf - 1*(1-1)        # cusp is unibranch: no correction
    # charged B3-N4
    g_ref  = kodd-1 if kodd>=1 else 0
    j_ref  = 1 if kodd>=1 else 2
    n_ref  = 3+4*k-2*kodd if kodd>=1 else 3+4*k
    chi_ref= 1-4*k
    # this lane's degree-free identity chi_c(E) = a(1-R) + sum a_p
    chi_id = a*(1-R) + 1
    good = (n_inf==n_ref and chi==chi_ref and chi_id==chi_ref and (kodd==0 or g==g_ref))
    ok &= good
    if k<=3: print(f"k={k} kodd={kodd}: g={g}(ref {g_ref})  n_inf={n_inf}(ref {n_ref})  chi={chi}={chi_id}(ref {chi_ref})  {'OK' if good else 'MISMATCH'}")
print("\nall cells k<=8 agree with B3-N4:", ok)
