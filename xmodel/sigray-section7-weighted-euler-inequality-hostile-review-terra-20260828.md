# Hostile review: Section 7 weighted-Euler inequality repair

**Date:** 2026-08-28  
**Reviewer:** GPT-5.6 Terra / Codex  
**Original reviewed hash:**
`5036f9a233e15e7efbf0fa99ba1fb6157eb95d10b5aef03580a025cbf635e6b5`  
**Amended reviewed hash:**
`c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6`

## 0. Verdict

**Original hash: FAIL.  Amended hash: PASS.**

The original Lemma 3.2 claimed

```text
w_i(z_0) >= mult_(z_0)(P_i-P_i(z_0))*b_i^+.
```

The reviewed proper tube does not prove this.  Ramification indices at
several nearby direction points cannot be added when their `Q_i`-values are
different.  The already reviewed local Keller chart gives an exact local
countermodel to that multiplication.

The amendment makes the precise minimal repair:

```text
w_i(z_0) >= b_i^+.
```

It chooses only one nearby simple nonzero direction.  Its local `g`-degree
is `b_i^+` and cannot exceed the constant total degree `w_i(z_0)` of the
proper finite tube.  This is fully supported by the repaired Proposition
7.3 tube, handles a moving `Q_i`-value, and is exactly the strength needed
for the compact-Euler sign argument.  No new common-resolution or
cross-fibre `kappa`-invariance assertion is introduced.

Consequently the amended report proves

```text
td(f,g) >= 1 + sum_(F in T_(a,cv)) kappa_F(pi(F)-1)
```

for every prescribed fibre and every subset of distinct critical-value
flags.  This promotes the numerical content of repaired Corollary 7.1.  It
does not promote printed equation (22), the printed per-puncture `delta`, or
the failed fixed-weight `(22-cl)` identity.

## 1. Custody and reviewed perimeter

The following inputs were checked directly:

```text
5036f9a233e15e7efbf0fa99ba1fb6157eb95d10b5aef03580a025cbf635e6b5
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
  (original version supplied for review)

c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
  (amended version gated here)

758c022696da6dbafaf7c907af25d733162ece203cc6599a30a903de03c93840
  xmodel/sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md

f31f948747656102a529eeac54e66a6a66ba67bdbbc922c1fa3fbac1f75598de
  xmodel/sigray-section7-kappa-variation-salvage-gpt55-20260828.md

0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31
  xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md

af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe
  xmodel/sigray-section7-full-independent-audit-hostile-review-gpt5-20260828.md

dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90
  xmodel/sol-h5a.md

3b8bd5c9e2a1f4132cff4353e0e7e0fd9b4426cbeea0b0c13d092161018f5d2f
  xmodel/grok-h5a-review.md
```

The printed proof of Proposition 7.3 on pp. 36--38 of
`refs/sigray_full.pdf` was also checked.  The review uses only the repaired
proper-tube version in the full independent audit, not the malformed literal
print.  The final Terra delta gate passed the quotient coordinate,
formal-deck/EW2 bridge, centred value formulas, every-point realization,
and no-duplication clauses; it failed only the old fixed `kappa` transport.
The present argument does not reuse that failed clause.

## 2. The original multiplicity factor is false

Use the exact local chart already checked in the full Section 7 audit:

```text
s=y^(-1),  t=xy^3,
x=t*s^3,   y=s^(-1),
g=t,       f=t^2+s^2/2.
```

It is an exact local Jacobian-one chart because

```text
dx wedge dy = s ds wedge dt = df wedge dg.
```

At the height-three flag, the quotient is unramified (`m=1`), its direction
coordinate is `z=t`, and

```text
P(z)=z^2,  Q(z)=z,  kappa^-=kappa^+=1,  b^+=2.
```

On the special fibre `f=0`, the direction `z=0` contains the two normalized
branches `t=alpha_+ s` and `t=alpha_- s`.  On each branch `g=t` is a local
uniformizer.  Hence

```text
w(0)=Lambda(P_+)+Lambda(P_-)=1+1=2.
```

But `mult_0(P-P(0))=2`, so the original Lemma 3.2 would require

```text
2=w(0) >= 2*b^+=4,
```

which is false.

For a nearby fibre `f=a'`, the two simple directions are
`z=+sqrt(a')` and `z=-sqrt(a')`.  At either one,

```text
t-t_0 = -s^2/(4t_0)+O(s^4),
```

so its local `g`-degree is two, equal to `b^+`.  Their values under `Q` are
`+sqrt(a')` and `-sqrt(a')`, however.  A degree-two finite map can have a
ramification point of index two over each of two different target values;
those indices do not add to a lower bound of four on the map degree.

This chart is not a global polynomial Keller pair (`f` contains
`1/(2y^2)` in the affine variables).  It is nevertheless a
dependency-faithful countermodel to the claimed implication from the
reviewed *local* proper-tube calculus: that calculus, local Jacobian-one
geometry, normalization, and conservation of degree do not license summing
ramification at different moving `Q`-values.

## 3. The amended one-point specialization is proved

Fix `z_0`.  Use the proper local tube from repaired Proposition 7.3 around
the geometric direction cluster `C(i,z_0)`.  It may have several normalized
punctures, but the constant degree of the finite map

```text
g : U intersect Rbar_(a') -> B
```

on the special fibre is exactly

```text
D=sum_(P in C(i,z_0)) Lambda(P)=w_i(z_0).
```

Choose a small quotient disc about `z_0`.  Local properness of the
nonconstant polynomial `P_i` gives a root `z'` in that disc for every
sufficiently close first-coordinate value `a'`.  Choose `a'` outside the
finite discriminant and, if `z_0=0`, outside `P_i(0)`.  Then `z'` is both
nonzero and a simple quotient root.

The passed quotient/EW2 bridge sends `z'` to one geometric direction point
inside the same tube.  It does not create one point per covered lift.  At a
nonzero lift, the derivative of `eta -> eta^{m_i}` is nonzero; hence the
covered residual root is simple.  Repaired Proposition 7.3 therefore gives
the local degree at this one point as

```text
e(z')=kappa_i^+(u_i-1)=b_i^+.
```

Continuity puts its moving value `Q_i(z')` inside the target disc `B`.
For a finite map of total degree `D`, the ramification index of any one
source point over its own target value is at most `D`.  Therefore

```text
b_i^+=e(z') <= D=w_i(z_0).
```

This proves amended Lemma 3.2.  The checks requested in the hostile prompt
are all explicit here:

- **moving `Q`-values:** only one local index is used, so its target may
  move;
- **cyclic orbits:** one quotient point is one EW2 direction; covered lifts
  are coordinate presentations, not additive geometric points;
- **the zero orbit:** choose the nearby root away from zero;
- **multiple punctures:** their special local degrees sum to the tube degree
  `w_i(z_0)`;
- **cross-flag isolation:** the repaired tube is chosen after fixing the
  common strict prefix and coefficient orbit and excludes every other
  boundary cluster; the passed EW1/injective-transport clause excludes
  cross-reference duplication.

No factor `mult_(z_0)(P_i-P_i(z_0))` follows, and none is needed.

## 4. The zero-root objection does not refute the amendment

The D2 objection in the GPT-5.5 salvage report treated `z=0` as a simple
zero direction while simultaneously assigning it the low value
`kappa_i^-<kappa_i^+`.  Those conditions are incompatible in the covered
coordinate.

Indeed,

```text
m_i=e_i/gcd(e_i,n_i),
kappa_i^+=m_i*kappa_i^-.
```

Thus strict inequality `kappa_i^+>kappa_i^-` implies `m_i>1`.  At the
special value,

```text
p(eta)=P_i(eta^m_i)-P_i(0)
```

has `eta=0` as a root of multiplicity at least `m_i`.  The simple-direction
clause of Proposition 7.3 cannot assign this cluster the low weight.  If
`m_i=1`, then `kappa_i^+=kappa_i^-`, so there is no high/low discrepancy.

The Terra formal witness `K=e=2,n=3,P(z)=z` therefore shows variation of
the vertex decoration, but it does not bound the actual zero-cluster mass
by the low value.  The amended proper-tube argument gives precisely the
missing upward bound on that mass.

## 5. Lattice and generic-weight audit

With

```text
e_i=gcd(K_i,{r<n_i:c_r!=0}),  n_i=K_i*u_i,
```

the prefix lattice and effective coefficient-orbit order are

```text
kappa_i^-=K_i/e_i,
m_i=e_i/gcd(e_i,n_i).
```

A nonzero coefficient at height `u_i` adjoins `n_i` to the support gcd and
therefore gives

```text
kappa_i^+=K_i/gcd(e_i,n_i)=m_i*kappa_i^-.
```

A zero coefficient gives no jump.  Under the reviewed Q/jump/max
convention, a transported flag has the high value exactly when
`P_i(z)=a` has a nonzero geometric quotient root; if zero is its only root,
it has the low value.  In particular

```text
kappa_i(a) <= kappa_i^+
```

on every fibre, with equality away from `P_i(0)`.  Synchronized denominator
refinement scales `K_i,e_i,n_i` together and leaves all these ratios
unchanged.

For `z!=0` and `P_i'(z)!=0`, every covered lift is nonzero and simple.  The
simple-direction clause gives a singleton cluster of weight
`b_i^+=kappa_i^+(u_i-1)`.  The orbit is counted once, not `m_i` times.
This verifies amended Lemma 3.1 and the common generic value.

## 6. Constructibility and compact-Euler sign

Set

```text
S_i={0} union {z:P_i'(z)=0}.
```

The polynomial `P_i` is nonconstant by the passed quotient construction,
so `S_i` is finite.  Lemma 3.1 gives `w_i=b_i^+` off `S_i`, and amended
Lemma 3.2 gives `w_i(s)>=b_i^+` on `S_i`.  The weights are finite sums of
local degrees, hence integer-valued; equality with a constant away from a
finite set makes `w_i` constructible.

The compact-Euler calculation is then sign-safe:

```text
integral_(A1) w_i dchi_c
 = b_i^+*(1-#S_i) + sum_(s in S_i) w_i(s)
 >= b_i^+.
```

This is not an illicit appeal to monotonicity of compact Euler
characteristic.  It uses a constant generic value and individually
nonnegative corrections at the finite exceptional set.

## 7. Actual-weight pushforward and arbitrary-fibre Corollary 7.1

The passed quotient bijection partitions every finite-value direction
cluster exactly once.  The every-fibre Proposition 5.8 replacement and
Keller simplicity at affine preimages give

```text
d-N(a,b)
 = sum_(P at infinity on f=a, g(P)=b) Lambda(P)
 = sum_i (phi_i)_! w_i(a,b).
```

The pushforward uses actual cluster weights, not a transported baseline.
The maps have finite fibres because each `P_i` is nonconstant.  Thus all
functions are constructible and compact-Euler Fubini gives

```text
d-1
 = sum_i integral_(U_i) w_i dchi_c
 >= sum_i b_i^+.
```

Now choose the reference fibre to be any prescribed `f=a_0`.  At each of
its critical-value flags, the actual Q/jump/max value is at most the generic
high value:

```text
kappa_(F_i)(pi(F_i)-1) <= b_i^+.
```

Therefore

```text
td(f,g)
 >= 1 + sum_(F in T_(a_0,cv)) kappa_F(pi(F)-1).
```

All terms are positive because `pi(F)>1`, so the same inequality holds for
every subset of pairwise distinct flags.  Since `a_0` was arbitrary, this
is the required every-fibre repaired Corollary 7.1.

## 8. Final clause ledger

| clause | verdict |
|---|---|
| original multiplicity-strengthened Lemma 3.2 | **FAIL; explicit reviewed local countermodel** |
| amended one-point Lemma 3.2 | **PASS** |
| `kappa^-`, `m`, `kappa^+` formulas | **PASS** |
| generic equality at nonzero simple quotient points | **PASS** |
| cyclic/root-orbit counting | **PASS; one orbit is one direction** |
| zero-root compatibility with the simple clause | **PASS; high/low variation forces a multiple covered root** |
| multiple-puncture special cluster | **PASS; its sum is the tube degree** |
| moving `Q`-values | **PASS after deleting the invalid sum** |
| cross-flag isolation/no duplication | **PASS at the exact final-delta perimeter** |
| constructibility of actual weights | **PASS** |
| compact-Euler sign | **PASS** |
| actual-weight pushforward | **PASS** |
| arbitrary-fibre Corollary 7.1 inequality | **PASS** |
| printed per-puncture `delta`, printed (22), fixed-weight `(22-cl)` | **NOT RESTORED** |

No further lemma is missing at the amended dependency perimeter.  The
smallest repair required by the original failure was exactly the one now
made: delete the ramification multiplicity factor, select one nearby simple
nonzero quotient direction, and compare its one local degree with the
proper tube's total degree.
