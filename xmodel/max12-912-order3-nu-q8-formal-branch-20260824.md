# Max12 `(9,12)` order-three loaded fibre: genuine `Q8` non-parity formal branch

Date: 2026-08-24  
Status: **producer-exact; hostile different-model review required**

## 1. Fresh lineage and scope

This report starts from the corrected, frozen `Q8` erratum and recomputes all
formal-branch hypotheses.  It does not import the quarantined `Q12` formal
branch.  The chart uses the genuine numerator `1+3v` in `x1`, and the replay
asserts that fact explicitly.

Fix the seven-row constant-invariant fibre

```text
k=mu=0, nu != 0,
r1=r2=r3=r4=r5=r7=0, r6=nu.                           (1.1)
```

The eighth reconstructed tail `r8` is not imposed here.

## 2. Exact block ranks at `Q8`

For the involution `f(z)->-f(-z)`, set

```text
n=(a0,a2,a4,a6),
b=(p,x1,x3,x5).
```

The replay reconstructs and fingerprints all eight original tails and checks
that `r_l` has character `(-1)^l`.  The Jacobian of (1.1) at parity splits as

```text
J_N=d(r1,r3,r5,r7)/d(a0,a2,a4,a6),
J_I=d(r2,r4,r6)/d(p,x1,x3,x5).                         (2.1)
```

On the corrected generic chart, the frozen erratum gives

```text
det(J_N)=p^20*226492416*v^16*(3v^2+3v+1)^8*Q8(v)
         /(3v^2-2)^10.                                 (2.2)
```

Fresh exact gcd certificates at every root of `Q8` give

```text
rank J_N=3:
  det d(r3,r5,r7)/d(a2,a4,a6) is a unit;

rank J_I=3:
  det d(r2,r4,r6)/d(x1,x3,x5) is a unit.              (2.3)
```

Thus the fixed fibre is a smooth curve, the full Jacobian has rank six, and
the full tangent space has dimension two.  The replay also verifies

```text
gcd(Q8,Q8')=1,   gcd(Q8,num(R6'))=1.                   (2.4)
```

## 3. Equivariant formal normal form

Fix a loaded parity coefficient point above a root of `Q8`.  It exists because
`Q8` is coprime to `v`, `A2`, `D`, and `A5`, while

```text
p^9 R6(v)=nu != 0.
```

Use the two unit minors in (2.3) to eliminate three invariant and three
anti-invariant variables.  Retain an invariant coordinate `s` along the fixed
curve and an anti-invariant coordinate `t`.  Equivariance and uniqueness of
the formal implicit-function theorem make the sole residual odd equation

```text
t*Phi(s,t^2)=0.                                        (3.1)
```

On `t=0`, the Schur complement identifies

```text
Phi(s,0)=unit*det(J_N).                                 (3.2)
```

The loaded parity equation solves `p` as a formal function of `v`, and `Q8`
is squarefree with all factors in (2.2) units.  Hence

```text
dPhi/ds(0,0) != 0.                                     (3.3)
```

Therefore `Phi=0` solves uniquely as `s=psi(t^2)`.  The completed local fibre
has two reduced smooth curve branches with distinct tangents:

```text
parity:      t=0,
non-parity:  Phi(s,t^2)=0.                              (3.4)
```

## 4. Scope firewall

Every loaded `Q8` parity contact lies on a second smooth non-parity formal
component of the seven-row coefficient fibre.  This is positive formal fibre
geometry, not an algebraic or rational Keller trajectory.

Still required are normalization beyond existence, pullback of `r8` and
`9*r8'=j/u`, Kummer descent, Taylor and coprimality reconstruction, and any
analysis of components disjoint from parity.  There is no all-`(9,12)`,
maximum-twelve, counterexample, or Jacobian-conjecture conclusion.

## 5. Replay

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q8_formal_branch_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.json -
```

The stdlib replay reconstructs all eight tails, uses only the corrected chart,
recomputes (2.2), and verifies both unit minors and every gcd used above.
