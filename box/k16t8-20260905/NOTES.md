# Working notes for k16-t8-onepoint-grok46 (not the sealed report)

## Hash custody
15/15 charged inputs sha256sum -c OK from receipt awk manifest.

## Controls
- t=6 verifypoint replay: byte-identical to charged .out (sha256 6b87efdd...), wall=0s.
- perturbed W: W_r+1 FITTcheck=0 all r; nearby q2+1 MINORS_ZERO=0 and local vdim=0.
- msolve_point.py on charged t=6 param: ROOT 12955 COORDS [4339,9016,16021,25108] matches charged POINT and BETA.

## Boundary of Γ_8 mod 32003 (this lane, listboundary, wall=1s)
Charged boundary job (w18, 179s): slice dim=1; j=2 empty; j=3 vdim=6 dim=0; j=3+(W) vdim=0; j=4..7 empty.
This lane listed the j=3 scheme:
- finduni: q4=q5=q7=0 (minpoly the variable itself); q6 degree-6 squarefree, FACTOR_PATTERN 1^1 2^1 3^1.
- q6 minpoly = x^6+865x^5-11155x^4+14501x^3+5432x^2-3663x+9115
  = (x-7416)(x^2+2445x+7483)(x^3+5836x^2+15822x-2966) over F_32003.
- Unique F_p-point: P̄_bd = (b4,q2,q3,q4,q5,q6,q7)=(0,0,1,0,0,7416,0)
  local_vdim=1 (simple in the j=3 chart), MINORS_ZERO=1, JACRANK_FREE=4=expected,
  KERNEL_CONSISTENT=1, β=-9925 from r=3, T_top=4235≠0,
  W3=-6850, W6=12365, other W_r=0, W_NONZERO=1, all FITTcheck=1.
- vdim(stratum+(W))=0 ⇒ W≠0 at the quadratic and cubic geometric points as well.

## Does a boundary point certify (ii)_8?
NO, not by itself.
- Lemma 3.7 as written: P̄ ∈ Y_t(k) = {b4=1}. This point has b4=0.
- Lemma 3.1: all-or-nothing on one Gal-orbit. The 6 points have F_p-Frobenius type (1)(2)(3), so not a single F_p-orbit; over A_8 the orbit count is not proved (k_t=1 is OPEN for t≥7, and this is the boundary).
- Prop 7.1 needs V(I2+(W))={0} on the WHOLE cone. Boundary W-nonvanishing is only V(I2+(W))∩{b4=0}={0}. Affine chart of the W-locus is a separate computation (conew/affinew, running).
- The Nullstellensatz vdim(stratum+(W))=0 + flatness + properness would certify (ii) on the *boundary* of Γ_8, once CONE dim=1 is printed. It does not touch affine orbits.

## Affine hunt (negative, useful)
Coordinate lines, 2-planes, 3-spaces, and eight 4-spaces in {b4=1} are all empty (gcd=1 or dim=-1). Affine F_p-points of Γ_8, if any, have at least five nonzero q-coordinates.

## (i)_8
Rank lane: PARTI (B) dim=0 vdim=11440=C(16,7) at (p,yy)=(32003,11288); (B,C) dim=0 vdim=5224. Promoted (i) and B-hsop at t=8 with DETECTOR-ONLY p-integrality caveat (no PINT PASS; absence of `div. by 0`). 17(rrrrr).

## Good reduction of A_8 at p=32003
H_8=3468 yy^2-1836 yy+234 splits: roots 11288, 18833. disc H = 124848 ≠ 0 mod p. A_8=Q(√27)=Q(√3), p∤3, (3/p)=1. a0=7970≠0. 2 invertible. Branch 0 = 11288.

## Pending
- msolve CI 16-thread -l 44 on .7
- msolve CI 4-thread on .28 (legacy)
- conew I2+(W) on .28
- affinew I2+(W)+(b4-1) on .7
- pattern dimonly MAIN vdim on .18 (SLICE dim=1 already)

## Lemma 3.3 at t=8
Need CONE dim=1. Currently: SLICE dim=1 (boundary nonempty). MAIN vdim pending. Explicit points of I2 exist (the 6 boundary points), so I2≠(1) and dim≥1.
