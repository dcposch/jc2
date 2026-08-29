# Sigray Section 7 kappa-variation salvage

Date: 2026-08-28  
Reviewer: GPT-5.5/Codex  
Status: **salvage, not promotion of the printed Corollary 7.1 inference**

## 0. Executive verdict

The newly exposed obstruction is real.

The quotient transport `tau` and the root-orbit bookkeeping can be kept, but
the Section 7 fixed-weight Euler proof cannot: the Q/jump/max value of
`kappa` may vary along the quotient line when the realised residual root
moves between the zero coefficient orbit and nonzero coefficient orbits.
The Terra witness

```text
K=e=2, n=3, effective action eta -> -eta, z=eta^2, P(z)=z
```

is enough to break the cross-fibre weight transport.  On `a0=0` the only
root is the zero coefficient root; on `a=1` the roots are nonzero.  The
strict prefix and quotient parameter may be identical while the post-height
gcd changes.

The strongest result presently supported by the reviewed files is:

```text
d - N = sum_i (phi_i)_! W_i                         (actual-weight pushforward)
td(f,g) = 1 + sum_i int_{U_i} W_i dchi_c             (actual-weight Euler)
td(f,g) = 1 + sum_i b_i^- + Delta^- , Delta^- >= 0   (coarse zero-baseline)
```

Here `W_i(z)` is the actual cluster weight
`sum_{P in C(i,z)} Lambda(P)`, and `b_i^-` is the direction-specific
zero-coefficient baseline on the quotient line.  This coarse identity is
invariant, but it is weaker than printed Corollary 7.1: it does **not**
bound an arbitrary fixed fibre by its vertex-global Q/max weights.

Consequences for the downstream `td<=5` campaign:

- the Section 9 table enumeration and all purely local arithmetic rows
  remain as audited;
- rows `1,5,7,10` still die by the independent nonroot `M=1` pole pin;
- row `4 = (2,3), a=1, b=2, nu=3, Lambda=4, M=2` is no longer certified,
  because its repaired closure uses the Section 7 fixed-fibre exit budget;
- therefore the audited `td>=6` conclusion is not currently certified from
  the reviewed dependency perimeter.

There is a plausible conditional upgrade: if one proves an **upward
specialisation theorem**

```text
W_i(z0) >= mult_{z0}(P_i - P_i(z0)) * b_i^+
```

where `b_i^+` is the nonzero/generic jump baseline, then the weighted-Euler
candidate would recover the Corollary 7.1 inequality without fixed
`(22-cl)`.  That theorem is not in the reviewed Section 7/H5a/Prop5.8/Section
9 package, and it is exactly the new load-bearing assertion that must be
proved before row 4 can be reinstated.

## 1. Source custody

SHA-256 values of files used for this audit:

```text
0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31  xmodel/sigray-section7-full-independent-audit-sol-ultra-20260828.md
af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe  xmodel/sigray-section7-full-independent-audit-hostile-review-gpt5-20260828.md
758c022696da6dbafaf7c907af25d733162ece203cc6599a30a903de03c93840  xmodel/sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md
521080ae8ae2c667908f6cb220a62a732f422777a1bad662099598f33df34962  xmodel/sigray-section7-resolution-free-quotient-route-gpt55-20260828.md
aa5dc37bd505cc5be78d77817a115afa5d05062023800ada7c8e40572abe07cb  xmodel/sigray-section7-resolved-direction-lemma-hostile-review-terra-20260828.md
dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90  xmodel/sol-h5a.md
3b8bd5c9e2a1f4132cff4353e0e7e0fd9b4426cbeea0b0c13d092161018f5d2f  xmodel/grok-h5a-review.md
47eef0925470fc769eec08e6d3bf972446feaaff6f6ef709c154edaa31054caf  xmodel/sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md
7deca833e78e26271b873d862c6081c6bffa369b6dea4a178e18b1d042ff7490  ladder/SOL-PROP58.md
569661d0771b8353ae76e4d8f48a809f996e83b36a93239f1e8540bb274fbac8  ladder/SOL-PROP58-REVIEW.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
f1da7026320b3dedd47534428aa53e6df66c698888c398e4f7eb5288d89b0748  ladder/SIGRAY-AUDIT.md
5036f9a233e15e7efbf0fa99ba1fb6157eb95d10b5aef03580a025cbf635e6b5  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
```

Only this new `xmodel/` report was added.  No canonical or producer file was
edited.  No heavy local CAS was run.

## 2. What still passes

The Terra final delta gate separates the quotient geometry from the weight
claim.  The following clauses still pass and can be used:

1. With a fixed reference presentation, the quotient coordinate is
   well-defined up to the formal deck action.
2. The formal deck quotient is the same quotient as the EW2 root-orbit
   quotient.
3. The centred first value and common `g` value are encoded by descended
   polynomials `P_i,Q_i` and the map

   ```text
   phi_i(z) = (P_i(z), Q_i(z)).
   ```

4. Every quotient point `z` is realised by a direction cluster, and the
   passed no-duplication statement partitions all finite-value clusters.
5. Proposition 5.8 gives the every-fibre meromorphic degree identity

   ```text
   d - N(a,b) =
     sum_{P at infinity on f=a, g(P)=b} Lambda(P).
   ```

These are enough for an exact actual-weight pushforward.  They are not enough
for a fixed baseline.

## 3. Why route A fails: no reviewed Keller/EW constraint gives invariance

H5a proves that the Q/jump/max convention is the only coherent global
vertex decoration for Section 9 Q-data and integer `D_{h,F}` bookkeeping.
It does not identify the residual root sets of `P_i(z)=a0` and `P_i(z)=a`.

The failed transport step needs exactly that missing identification.  It
compares a zero coefficient root on one fibre with nonzero coefficient roots
on another fibre.  A prefix stabilizer preserves zero/nonzero status of a
given coefficient; it does not preserve the set of roots of a moving
polynomial equation.

There is also a vertex/nonvertex distinction.  A drop of the max value across
fibres can occur only at a special value where `P_i(z)-P_i(0)` has no
nonzero quotient root.  In that situation the special flag may be nonvertex,
but `T_(a,cv)` in the Section 7 ledger permits such flags.  H5a's vertex
Q/max convention therefore cannot be used to delete the zero-orbit case from
Section 7.

Conclusion for A:

```text
No reviewed Keller/EW statement proves kappa invariance across fibres.
The fixed weights b_i in the old (22-cl) are unavailable.
```

## 4. Direction-specific versus vertex-global kappa

The obstruction is not just cross-fibre.  It also affects EW4/Proposition
7.3 if those are read with vertex-global Q/max weights.

There are two distinct quantities:

```text
kappa^max_F   = the global vertex Q/max decoration used by H5a and Section 9
kappa^dir_C   = the denominator/baseline along the specific direction cluster C
```

For a fixed prefix with height `u=n/K` and lower coefficient gcd `e`, the two
local values are

```text
kappa^- = K/e
kappa^+ = K/gcd(e,n).
```

The zero coefficient direction uses the nonjump value `kappa^-`; a nonzero
coefficient direction uses the post-jump value `kappa^+`.  If
`gcd(e,n)<e`, then `kappa^+>kappa^-`.

Now take a doubly realised fibre model such as

```text
P(z)=z(z-1).
```

At `a=0`, the same fibre has a zero quotient root `z=0` and a nonzero root
`z=1`.  The vertex-global max for the flag is high, `kappa^+`.  But the
simple zero direction has no post-height coefficient jump.  The repaired
simple-direction proof in Section 7 uses the fact that no characteristic
vertex intervenes along that branch; this identifies the terminal denominator
with the direction-specific value, not with the global max created by the
other realised direction.

Thus the statement

```text
Lambda(P) = kappa^max_F * (u-1)
```

for the simple zero direction is not licensed.  The valid local statement is
only

```text
Lambda(P) = kappa^dir_C * (u-1)
```

for a simple direction, and

```text
L_C >= kappa^dir_C * (u-1)
```

for a general direction cluster.

This is the clean separation needed downstream: H5a is a global vertex-data
repair; Section 7 cluster estimates must be direction-specific unless an
additional upward-specialisation theorem is proved.

## 5. Route B: the true constructible actual-weight identity

For each quotient line `U_i ~= A1_z`, define the actual cluster weight

```text
W_i(z) = sum_{P in C(i,z)} Lambda(P).
```

Using the passed quotient partition and Prop5.8, we get the pointwise
constructible identity on `A2`:

```text
d - N = sum_i (phi_i)_! W_i.                         (B1)
```

Here the pushforward sums over the finite geometric fibre of
`phi_i(z)=(P_i(z),Q_i(z))`.  This statement is stronger and safer than any
fixed-baseline claim: it uses only actual Lambda mass.

Euler-Fubini gives

```text
td(f,g) = 1 + sum_i int_{U_i} W_i dchi_c.             (B2)
```

Now define the direction-specific baseline

```text
b_i(z) =
  kappa_i^-(u_i-1),  z=0,
  kappa_i^+(u_i-1),  z!=0.
```

For nonzero simple points, repaired Proposition 7.3 gives equality
`W_i(z)=b_i(z)`.  At finitely many bad points, it gives
`W_i(z)>=b_i(z)`.  Hence

```text
W_i = b_i + E_i,       E_i>=0,       supp(E_i) finite,
```

and

```text
int_{U_i} b_i dchi_c
 = b_i(0) * chi_c({0}) + b_i(nonzero) * chi_c(A1 - {0})
 = kappa_i^-(u_i-1),
```

because `chi_c(A1-{0})=0`.

Therefore the exact variable-weight identity collapses to the invariant
coarse baseline:

```text
td(f,g)
 = 1 + sum_i kappa_i^-(u_i-1) + sum_i sum_{z in S_i} E_i(z),   (B3)
```

where `S_i` is finite.  In particular

```text
td(f,g) >= 1 + sum_i kappa_i^-(u_i-1).                       (B4)
```

What B does **not** give:

```text
td(f,g) >= 1 + sum_{F in T_(a0,cv)} kappa^max_F(pi(F)-1)
```

for an arbitrary fixed fibre `a0`.  A generic fibre may realise only nonzero
roots and therefore carry the high `kappa^+` weight, while the compact Euler
integral of the quotient line remembers only the zero-orbit baseline unless
extra special mass is proved.

So B proves an exact constructible Euler identity, but it does not by itself
recover Corollary 7.1 or the Section 9 first-separation exit budget.

## 6. Route C: the invariant coarse-baseline theorem

The unconditional replacement for `(22-cl)` is:

```text
Theorem C.
For every reviewed Section 7 quotient line U_i attached to a reference
critical-value flag with height u_i, lower gcd e_i, and K_i as above,

td(f,g)
 = 1 + sum_i b_i^- + Delta^-,
Delta^- >= 0,
b_i^- = (K_i/e_i)(u_i-1).
```

This is invariant under the quotient transport because `K_i,e_i,u_i` are
strict-prefix data.  It deliberately does not use the post-height max created
by a nonzero coefficient root.

Equivalently, with `b_i^+ = (K_i/gcd(e_i,n_i))(u_i-1)`:

```text
b_i^- <= b_i(z) <= b_i^+,
int_{A1_z} b_i(z) dchi_c = b_i^-.
```

The proof is just (B1)--(B3).  The finite exceptional contribution is

```text
Delta^- = sum_i sum_{z in S_i} (W_i(z)-b_i(z)),
```

after taking `S_i` large enough to contain `0` and the non-simple residual
roots.  Repaired Proposition 7.3 gives termwise nonnegativity.

This theorem is useful as an invariant ledger, but it is too weak for any
argument whose budget requires the high vertex-global max at a prescribed
fibre.

## 7. Section 9 blast radius

The Section 9 source audit used Section 7 in the first-separation exit
budget:

```text
sum_i lambda_i^exit <= td(f,g)-1-psi,
sum_i lambda_i^exit <= td(f,g)-2
```

after replacing nested `Y(F)` sums by disjoint exit sets.  Those inequalities
charge the actual Section 9 vertex weights

```text
kappa^max_H(pi(H)-1).
```

The coarse replacement charges only the direction-specific zero baseline.
It does not control the same exit weights.  Therefore the H2/H3 exit-budget
repair is no longer certified.

The exact `td<=5` impact is:

```text
Table (23) enumeration                         survives
Prop5.8 mass/entry layer                       survives
Statement 9.3 sign/local arithmetic repairs    survive
Statements 9.6--9.11 arithmetic corrections    survive
E2--E4 zero-charge self-family bookkeeping      survives locally
Rows 1,5,7,10                                  still killed by nonroot M=1
Row 4                                          open / not certified
td>=6 conclusion                               not certified
td=6 exclusion                                 still not claimed
```

Rows `2,3,6,8,9,11` were already outside the `td<=5` one-pole selection
because their `Lambda` values are `6` or otherwise too large for that
assembly.  The relevant surviving obstruction is precisely row 4:

```text
row 4: (alpha,beta)=(2,3), a=1, b=2, nu=3, Lambda=4, M=2.
```

The old repaired Statement 9.12 closure for row 4 used the local exit budget
and terminal `psi` charge.  Without the fixed-fibre Corollary 7.1 inequality,
that closure is conditional at best.

## 8. Route D: dependency-faithful countermodels

These are not asserted to be global Keller counterexamples.  Their purpose is
to show that the printed Section 7 inference is not a formal consequence of
the reviewed dependencies.

### D1. Cross-fibre kappa variation

Use the Terra witness:

```text
K=e=2, n=3, z=eta^2, P(z)=z.
```

The quotient transport is well-defined.  The reference fibre `a0=0` has only
the zero quotient root; the target fibre `a=1` has nonzero quotient roots.
The zero root has no post-height jump, while the nonzero roots do.  Therefore
there is no rootwise transport of `kappa^max`.

This invalidates fixed weights in `(22-cl)`.

### D2. Same-fibre global-max EW4 failure

Use the local quotient polynomial

```text
P(z)=z(z-1).
```

On the fibre `a=0`, both a zero root and a nonzero root are realised.  A
global max convention assigns the high value `kappa^+` to the flag.  The
zero direction remains direction-specific low, `kappa^-`.

If the zero root is simple, the repaired simple-direction computation gives
the low direction-specific weight.  A global-max EW4 would demand the high
weight on that same simple direction.  Thus global-max EW4 is not a safe
reading of Proposition 7.3.

### D3. Euler ledger showing Corollary 7.1 is not formal

Take two abstract Terra quotient lines with

```text
b^- = 1/2,     b^+ = 1,
W(0)=1/2,      W(z)=1 for z!=0.
```

Then for each line

```text
int_{A1} W dchi_c = 1/2*chi({0}) + 1*chi(A1-{0}) = 1/2.
```

For two lines, the total Euler contribution is `1`, so the ledger allows

```text
td = 1 + 1 = 2.
```

But a generic fixed fibre seeing the nonzero roots on both lines would have
high-weight demand

```text
1 + 1 + 1 = 3.
```

Thus the printed fixed-fibre Corollary 7.1 does not follow from quotient
constructibility plus compact Euler integration.  Some extra theorem must
force special zero mass upward, or the generic fixed-fibre inequality is
simply unavailable.

## 9. Hostile comparison with the weighted-Euler candidate

Candidate reviewed:

```text
5036f9a233e15e7efbf0fa99ba1fb6157eb95d10b5aef03580a025cbf635e6b5
xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
```

Verdict: **not accepted as an unconditional repair.**

What is correct in the candidate:

1. Replacing fixed baselines by the actual cluster weight `W_i(z)` is the
   right first move.
2. The pointwise pushforward

   ```text
   d-N = sum_i (phi_i)_! W_i
   ```

   follows from Prop5.8 plus the passed quotient partition.
3. The formula

   ```text
   kappa(a) in {kappa^-, kappa^+}
   ```

   is a valid description of the zero/nonzero local alternatives in the
   two-stratum first-height model.
4. The Euler sign argument would be valid **if** all exceptional
   specialisations jumped upward from the generic high value.

The load-bearing gap is candidate Lemma 3.2:

```text
W_i(z0) >= mult_{z0}(P_i-P_i(z0)) * b_i^+.
```

This is stronger than the reviewed Proposition 7.3.  Proposition 7.3 gives a
proper-tube lower bound using the baseline of the fixed special direction.
It does not prove that a zero-coefficient special direction inherits the
nonzero/generic jump baseline.  For `P(z)=z`, Lemma 3.2 asserts exactly the
missing conclusion:

```text
W(0) >= b^+,
```

even though the direction-specific simple computation gives only `b^-`.

The candidate's local-degree paragraph implicitly assumes that nearby
nonzero simple directions over `P_i(z)=a'` can be charged into the special
zero cluster with their high weights.  That is a new theorem, not a
consequence of the passed quotient map.  The reviewed local-tube argument
isolates a direction cluster and proves `L_C >= b_C` for the chosen
directional baseline; it does not identify `b_C` with the generic high
baseline when zero/nonzero support changes.

This also explains the global-max issue.  If a single fibre has both zero
and nonzero residual roots, `kappa^max` is high, while the zero branch's
terminal denominator remains direction-specific low.  The old assertion
that no characteristic vertex intervenes implies `kappa_E=kappa_F` is valid
only after `kappa_F` is read direction-specifically.  With vertex-global
max, the equality is precisely what fails.

Conditional upgrade:

```text
If Lemma 3.2 is proved from a genuine Keller/resolution constraint, then the
candidate recovers the Corollary 7.1 inequality and restores the Section 9
row-4 exit budget.  Until then it should be recorded as KINV-budget, not as
an established Section 7 repair.
```

## 10. Final replacement statement

Promote this, not the printed Corollary 7.1 inference:

```text
Section 7 actual-weight Euler replacement.

Let U_i be the passed quotient lines attached to a finite list of reference
critical-value directions, phi_i=(P_i,Q_i), and
W_i(z)=sum_{P in C(i,z)} Lambda(P).  Then

  d-N = sum_i (phi_i)_! W_i,
  td(f,g) = 1 + sum_i int_{U_i} W_i dchi_c.

Moreover, with b_i^- the zero-coefficient direction baseline,

  td(f,g) = 1 + sum_i b_i^- + Delta^-,
  Delta^- >= 0.

No inequality with the arbitrary fixed-fibre vertex-global weights
kappa^max_F(pi(F)-1) follows unless one adds and proves the upward
specialisation theorem W_i(z0)>=mult*z-generic-weight.
```

Operational status:

```text
Printed fixed-weight (22-cl)             FAIL
Printed Corollary 7.1 inference          FAIL / unavailable
Actual-weight pushforward identity       PASS
Variable direction-weight Euler identity PASS
Invariant coarse-baseline identity       PASS
Weighted-Euler high-baseline candidate   CONDITIONAL on new Lemma 3.2
Section 9 rows 1,5,7,10                  survive
Section 9 row 4 / td>=6 closure          open
```
