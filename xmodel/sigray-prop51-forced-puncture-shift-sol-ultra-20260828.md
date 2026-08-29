# Sigray Proposition 5.1: the forced puncture shift repairs the threshold, with a typing correction

Date: 2026-08-28  
Status: **PROVISIONAL THEOREM — exact source-level repair, awaiting hostile review**  
Scope: Sigray Proposition 5.1 and Notation 5.1 only.  This note does not
alter the pole book, Proposition 4.2's separately repaired positive tower,
Proposition 4.3, Statement 3.14, Proposition 5.8, or any JC2 landing claim.

## 1. Verdict

The apparent finite-puncture repair is mathematically sound, but the clean
erratum is slightly larger than the phrase “put `b=g(P)`.”  For
`P in Rbar_a \ R_a`, put

```
A := f-a,
b_P := g(P)  if g(P) is finite, and b_P := 0 if g(P)=infinity,
B_P := g-b_P.
```

Then replace the printed function by

```
rho_P(v) := d_{A,I_P(v)} + d_{B_P,I_P(v)} + v - 1.       (1.1)
```

It has a unique first rational zero `u_P`, is positive below `u_P`, and is
identically zero from `u_P` onward.  Equivalently, `u_P` is the first flag at
which the leading Jacobian of `A` and `B_P` is nonzero.  On `T_a^+` this is
equivalent to the translated, repaired Proposition 4.2 tower having length
zero; on `T_a^-` it is equivalent to the Proposition 4.3 `b_P`-tower having
length zero.

Two qualifications are necessary.

1. Merely changing the letter `b` while leaving `d_{g,F}` in `rho` does not
   repair the proof.  At a finite nonzero puncture the unshifted leading part
   eventually is the constant `g(P)`, so condition (7) fails and the
   unshifted `rho` remains strictly positive.
2. The printed phrase `m_{I_P(v)}` for every rational `v` is not typed at the
   unique flag with `d_{f-a}=0`: Proposition 4.2 defines `m_F` on `T_a^+`
   and Proposition 4.3 defines `m_{F,b}` on `T_a^-`, but neither defines it
   on `T_a^0`.  The exact global statement is therefore the `rho`/leading-
   Jacobian threshold.  Its `m=0` translations are sided corollaries.  One
   may instead introduce a new global terminal predicate, but should not
   pretend that it is an approximate-root tower at `d_{f-a}=0`.

Thus the **threshold and Notation 5.1 are repaired**, while the literal
all-`v` tower wording needs this independent typing correction.  All campaign
uses at poles remain exactly as before: there `b_P=0`, `B_P=g`, the selected
threshold lies in `T_a^+`, and the ordinary positive tower has `m_F=0`.

## 2. Primary-source custody

Pinned source:

```
refs/sigray_full.pdf
SHA256 9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
```

Printed-page custody (PDF page equals printed page):

- p. 18: Proposition 4.1, condition (7), and the `rho>=0`/leading-Jacobian
  dichotomy (8);
- pp. 19--20: Proposition 4.2 (positive tower), subject to the separately
  promoted constant-leading-part repair;
- pp. 20--21: Proposition 4.3 and Notation 4.2, explicitly starting with
  `h_0=g-b` on `T_a^-`;
- pp. 23--24: Proposition 5.1 and Notation 5.1; the print uses
  `rho(v)=d_F+d_{g,F}+v-1` and an un-subscripted `m_F`;
- pp. 35--37: Proposition 7.2 and Proposition 7.3; the latter explicitly sets
  `b:=q(c)=g(P)` and applies the `g-b` negative tower between the finite
  critical-value flag and `F_P^*`.

Audit custody: `ladder/SIGRAY-AUDIT.md`, rows for Propositions 4.1--4.3 and
5.1/Notation 5.1.  The audit already identifies the finite-nonzero failure and
the forced value `b=g(P)`; the theorem below supplies the exact replacement
statement and isolates the all-`v` typing issue.

## 3. Corrected threshold theorem

### Theorem 3.1 (puncture-centred threshold)

Let `(f,g)` be a normalized complex Keller pair, let `a in C`, let `P` be a
puncture of the normalization of a component of `f=a`, and define `A`,
`b_P`, and `B_P` as in Section 1.  For rational `v>=0`, set
`F_v=I_P(v)` and define `rho_P(v)` by (1.1), using throughout the
audit-corrected `f-a` reading of Notation 3.13.  Then:

1. `(B_P)^+_{F_v}` is never a nonzero constant; hence condition (7) holds
   for every `v`.
2. `rho_P(v)>=0` for every rational `v`.
3. `rho_P` is continuous, nonincreasing and rational piecewise linear.  At
   every non-break point,

   ```
   rho_P'(v) = 1-deg p_{A,F_v}-deg p_{B_P,F_v}.           (3.1)
   ```

4. There is a rational `u_P>=0` such that

   ```
   rho_P(v)>0  for v<u_P,
   rho_P(v)=0  for v>=u_P.                               (3.2)
   ```

   In particular `u_P` is unique.
5. For every `v`,

   ```
   rho_P(v)=0
      iff J(A^+_{F_v},B^+_{P,F_v}) is nonzero
      iff J(A^+_{F_v},B^+_{P,F_v})=xi^{-v}.              (3.3)
   ```

   (The last equality uses the thesis's normalization `J(f,g)=1`; with a
   nonzero Keller constant it is multiplied by that constant.)
6. If `d_{A,F_v}>0`, let `m^+_{F_v,b_P}` denote the repaired Proposition
   4.2 tower applied to the translated Keller pair `(A,B_P)`.  Then

   ```
   m^+_{F_v,b_P}=0  iff  rho_P(v)=0.                     (3.4+)
   ```

   If `d_{A,F_v}<0`, Proposition 4.3 applies and

   ```
   m^-_{F_v,b_P}=m_{F_v,b_P}=0  iff  rho_P(v)=0.         (3.4-)
   ```

At `d_{A,F_v}=0`, (3.2)--(3.3) remain valid but (3.4+) and (3.4-) are not
statements: neither source tower is defined there.

### Proof

Write the leading forms at `F_v` as

```
A^+_{F_v}=xi^d p(eta),       B^+_{P,F_v}=xi^e q(eta),    (3.5)
```

where `p,q` are nonzero polynomials.  Since the truncation `F_v` lies on the
actual branch `P` of `A=0`, its next coefficient supplies a root of `p`
(Statements 3.9 and 3.18); hence

```
deg p >= 1.                                                (3.6)
```

If `B^+_{P,F_v}` were a nonzero constant, then `e=0` and `q` would be that
constant.  It has no root in common with `p`, so the corrected value
dictionary of Statement 3.15 would give `B_P(P) in C*`.  This contradicts
`B_P(P)=0` in the finite case and `B_P(P)=infinity` in the pole case.  Thus
condition (7) holds, proving (1).  Proposition 4.1 applied to `(A,B_P)` now
gives (2) and the dichotomy (3.3).

Statement 3.10 applied separately to `A` and `B_P` gives continuity and
piecewise linearity and gives (3.1).  Equation (3.6) makes its right-hand side
nonpositive, proving monotonicity.

It remains to prove that a zero occurs.  Suppose `rho_P(v)>0`.  Proposition
4.1 then says the leading bracket is zero.  From (3.5), its coefficient is

```
d p q' - e p' q = 0.                                      (3.7)
```

If `deg q=0`, then `q` is a nonzero constant; (3.6)--(3.7) force `e=0`.
But then `B^+_{P,F_v}=q` is a nonzero constant, contradicting (1).  Therefore

```
rho_P(v)>0  implies  deg q>=1.                             (3.8)
```

On every linearity interval on which `rho_P` is positive, (3.1), (3.6), and
(3.8) give `rho_P'<=-1`.  If no rational zero existed, integration across the
finitely many rational breakpoints would give

```
rho_P(w) <= rho_P(v)-(w-v),
```

which is negative for sufficiently large rational `w`, contradicting (2).
So a rational zero exists.  Nonnegativity plus monotonicity makes every later
value zero.  The finite rational piecewise-linear structure makes the first
zero rational (it is either a rational breakpoint or the rational zero of an
integer-slope affine piece).  This proves (3.2).

Finally, both Proposition 4.2 and Proposition 4.3 stop at stage zero exactly
when the stage-zero leading bracket is nonzero.  Apply (3.3).  The positive
case uses the independently promoted constant-leading-part repair for later
stages; the negative case uses the already audited Proposition 4.3 with
condition (7), which was proved in (1).  This proves (3.4+/-).  QED.

## 4. Why `b_P` is forced at a finite puncture

Let `P` have finite value `g(P)=b_P`.  If `b'!=b_P`, then
`(g-b')(P)=b_P-b' in C*`.  After a sufficiently deep truncation its leading
part is exactly that nonzero constant.  Thus condition (7) fails for `b'`.
The failure is not cosmetic: in the stable tail, write `r>0` for the negative
order of `g-b_P`.  The shifted terminal profile has the form

```
d_A(v)=r+1-v,       d_{g-b_P}(v)=-r,
deg p_A=1,          deg p_{g-b_P}=0,
rho_P(v)=0.                                                (4.1)
```

For the unshifted function (or any wrong shift), the nonzero constant
dominates the negative-order term, so

```
d_{g-b'}(v)=0,       deg p_{g-b'}=0,
rho_{b'}(v)=r>0.                                           (4.2)
```

This is exactly the printed finite-nonzero stuck case: the old `rho` never
vanishes and its use of Proposition 4.1 has lost condition (7).  Equations
(4.1)--(4.2) also show why one must replace `d_g` by `d_{g-b_P}` inside
`rho`, not merely attach `b_P` to the tower notation.

At a pole, subtracting a finite constant does not change the leading tail.
The canonical choice `b_P=0` therefore recovers the source and every pole
consumer literally.

## 5. Clean erratum text for Proposition 5.1 and Notation 5.1

Replace Proposition 5.1 by:

> **Proposition 5.1 (corrected).**  Let `P in Rbar_a\R_a`.  Put
> `b_P=g(P)` if `g(P)` is finite and `b_P=0` otherwise, and define
> `rho_P(v)=d_{f-a,I_P(v)}+d_{g-b_P,I_P(v)}+v-1`.  There is a unique
> `u_P in Q_+` such that `rho_P(v)>0` for `v<u_P` and `rho_P(v)=0` for
> `v>=u_P`.  Equivalently, `u_P` is the first `v` at which
> `J((f-a)^+_{I_P(v)},(g-b_P)^+_{I_P(v)})` is nonzero.  At vertices in
> `T_a^+` (respectively `T_a^-`) this is equivalent to the translated
> Proposition 4.2 (respectively Proposition 4.3) tower having length zero.

Replace Notation 5.1 by:

> Define `F_P^*:=I_P(u_P)` and retain `b_P` with this datum.  When
> `g(P)=infinity`, `b_P=0`; the audited pole-only argument shows
> `F_P^* in T_a^+`, and `m_{F_P^*}=0` in the original Proposition 4.2
> notation.

This avoids inventing an `m` on `T_a^0`.  If preservation of the three-clause
layout is desired, replace “`m_F=0`” by the globally typed terminal predicate
“the leading Jacobian of `(f-a,g-b_P)` at `F` is nonzero”; add the sided tower
equivalences as a final sentence.

The printed citation “By Proposition 8” on p. 24 should simultaneously be
replaced by “By Proposition 4.1 and Proposition 4.2/4.3 on their respective
domains.”  This is the already catalogued cosmetic E8 citation slip plus the
domain correction.

## 6. Section 7 corroboration and separation

The source itself uses the same forced centre in Proposition 7.3 (pp. 36--37):
for a finite puncture continuing through the root `c` of a critical-value
flag it sets

```
b := q(c) = g(P)
```

and then works with `(g-b)^+_H` and Proposition 4.3 on the intervening
`T_a^-` segment.  This is direct internal corroboration of `b_P`, not a proof
that unshifted Proposition 5.1 was correct.

The repaired threshold does not by itself repair any other Section 7 input.
In particular, it does not fill the proof omitted for Proposition 7.2, repair
Statement 3.14's conjugation twist, or prove Proposition 5.8's every-fibre
mass identity.

## 7. Strict pole-use firewall

For every campaign use that concerns `T_{a,pole}`:

1. require `g(P)=infinity` explicitly;
2. set `b_P=0`, so `B_P=g`;
3. use the already audited pole conclusion `F_P^* in T_a^+`;
4. use the original positive tower label `m_{F_P^*}=0` and `h_0=g`;
5. consequently retain

   ```
   M_{F_P^*}=gcd(deg p_{F_P^*},deg p_{g,F_P^*})
   ```

   and all existing pole `Q(F)`, `Lambda`, and mass formulas unchanged.

Finite thresholds are different objects: they carry the forced value `b_P`,
use `g-b_P`, and usually enter the negative tower used in Section 7.  They
must not be inserted into `T_{a,pole}`, Notation 8.1's pole `M_F`, the pole
entry book, or any `Lambda`-mass sum.

## 8. Exact checker and controls

The standard-library checker

```
cases/sigray_prop51_forced_puncture_shift_20260828/verify_threshold.py
```

checks the polynomial coefficient identity behind (3.7), the constant-`q`
classification, thousands of integer-slope threshold profiles, the stable
tail (4.1), and two negative controls: omitting the shift and shifting by the
wrong finite value.  It is an arithmetic replay of the proof's fragile steps,
not a substitute for Statements 3.9--3.10 or Proposition 4.1.

## 9. Bottom line

`b_P=g(P)` is the correct and unique finite-puncture centre.  With the
corresponding replacements `g -> g-b_P`, `d_g -> d_{g-b_P}`, and
`m_F ->` the appropriate `b_P`-tower, the monotone-threshold proof closes.
The cleanest global formulation uses `rho_P=0`/nonzero leading Jacobian,
because the source never defines a tower at `d_{f-a}=0`.  Pole-only campaign
work is unchanged and must remain firewalled at `b_P=0`.
