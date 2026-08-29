# Coordinator integration — corrected Sigray Proposition 5.1

Date: 2026-08-28 UTC.

Lifecycle verdict: **PROMOTABLE WITH THE REVIEW REPAIRS BELOW.**  This note
integrates the Sol Ultra producer
`xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md`
(`a0470416...`) with the independent Opus5 hostile review
`xmodel/sigray-prop51-forced-puncture-shift-hostile-review-opus5-20260828-r1.md`
(`dc549047...`).  It does not modify either immutable report.

## 1. Corrected theorem

Let `P` be a puncture of the normalized fibre `R_a`, put

```text
b_P = g(P)  if g(P) is finite,
b_P = 0     if g(P) is infinite,
A   = f-a,
B_P = g-b_P,
F_v = I_P(v),
rho_P(v) = d_(A,F_v) + d_(B_P,F_v) + v - 1.
```

Then:

1. `(B_P)^+_(F_v)` is never a nonzero scalar constant, for every rational
   `v>=0`; hence condition (7) holds along the whole path.
2. `rho_P` is nonnegative, continuous, nonincreasing and finitely
   piecewise-linear with rational breakpoints and integral slopes.  Wherever
   `rho_P>0`, its slope is at most `-1`.
3. There is a unique rational threshold `u_P>0` such that
   `rho_P(v)>0` for `v<u_P` and `rho_P(v)=0` for `v>=u_P`.
4. Equivalently, `u_P` is the first flag at which
   `J(A^+_(F_v),B_P^+_(F_v))` is nonzero.  Put `F_P^*=F_(u_P)`.
5. The threshold is sided:

   ```text
   g(P)=infinity  <=> F_P^* in T_a^+ <=> d_(B_P,F_P^*)>0,
   g(P) in C      <=> F_P^* in T_a^- <=> d_(B_P,F_P^*)<0.
   ```

   In particular `F_P^*` never lies in `T_a^0`.
6. Accordingly `m_(F_P^*)=0` in Proposition 4.2's positive-side notation at
   a pole, and `m_(F_P^*,b_P)=0` in Proposition 4.3's negative-side notation
   at a finite puncture.  At the unique intermediate flag with `d_A=0`, no
   `m` is defined; only the leading-Jacobian predicate is well-typed there.

## 2. Proof ledger

The producer and reviewer independently establish items 1--4.  The essential
points are:

- `deg p_(A,F_v)>=1` at every flag, because the branch `P` itself is counted;
- Statement 3.15(ii), whose printed label is unaffected by the audited
  (i)/(iii) swap, excludes a scalar leading part of `B_P`;
- the exact leading bracket is
  `d p q' - e p' q`; when `rho_P>0` it vanishes, and condition (7) then forces
  both residual degrees positive;
- Statement 3.10 supplies continuity and finitely many rational linearity
  intervals, while
  `rho_P'=1-deg p_(A,F_v)-deg p_(B_P,F_v)<=-1` wherever `rho_P>0`;
- Proposition 4.1's monomial-order argument supplies `rho_P>=0`; condition
  (7) is needed for the bracket classification and the Proposition 4.3
  tower, not for that nonnegativity inequality itself.

The Opus review proves item 5 using Proposition 4.4.  That version inherits
the newly exposed auxiliary-`h` `kappa` rider.  The following shorter argument
removes that dependency and is the authoritative integration proof.

At `F_P^*`, the nonzero bracket implies that `p_A` and `p_B` have no common
root.  Statement 3.15 applies to `B_P`; its corrected value dictionary gives
`e_*:=d_(B_P,F_P^*)>0` at a pole and `e_*<0` at a finite puncture, so
`e_*!=0`.

For rational `v<u_P` sufficiently close to `u_P`, continuity makes
`e(v)!=0`.  Since `rho_P(v)>0`, both residual polynomials are nonconstant and

```text
d(v) p q' - e(v) p' q = 0.
```

Thus `d(v)!=0`; comparison of the top eta coefficients gives

```text
e(v)/d(v) = deg(q)/deg(p) > 0.
```

Moreover `deg(p)>=1` and `deg(q)` is bounded by the fixed polynomial degree
of `B_P`, so this positive ratio is uniformly bounded above.  Hence `d(v)`
has the same sign as `e(v)`, and if `d(v)` tended to zero then `e(v)` would
also tend to zero.  Continuity and `e_*!=0` exclude that possibility.
Therefore `d_(A,F_P^*)` has the same nonzero sign as `e_*`, proving item 5
without Proposition 4.4 or any derived-`h` use of Statement 3.9.

Item 6 follows from the positive/negative tower definitions and the exact
equivalence `m=0 <=> rho=0` on each side.  The unique `T_a^0` flag remains a
source typing exception but is never `F_P^*`.

## 3. Downstream repair and firewall

The sidedness theorem proves, rather than assumes, non-leakage:

```text
T_(a,pole)
 = {F_P^*: P a puncture} intersect T_a^+
 = {F_P^*: g(P)=infinity}.
```

Thus Notation 5.2, Propositions 5.3--5.8, `Lambda(P)`, `Lambda(F)`, the pole
entry book and the topological-degree mass formula are unchanged.  At a pole
`b_P=0`, `B_P=g`, and in fact all target constants have the same leading
tail; the printed `h_0=g`, `m_F=0`, `M_F`, `Q(F)` and `Lambda(F)` are literal.

At a finite puncture the unique centre is `b_P=g(P)`; any other shift is
eventually a nonzero constant and violates condition (7).  This repair also
proves the source's unproved Statement 7.2 and supplies the missing shift and
condition-(7) premise in Proposition 7.3.  Proposition 7.2 and the remaining
Section 7 trust perimeter are not repaired by this theorem.

## 4. Required wording and source riders

- Replace the all-`v` phrases `m_(F_v)>0` / `m_(F_v)=0` in Proposition 5.1 by
  the leading-Jacobian or `rho_P` predicate, and use sided `m` only where
  `d_A` is nonzero.
- Retain `b_P` and the side as part of Notation 5.1's datum.
- Attribute the condition-(7) proof to the swap-invariant Statement 3.15(ii);
  use the corrected (i)/(iii) labels only for the value/sign dictionary.
- Any later use of Statement 3.9 with a derived auxiliary `h_j` still owes a
  common-`kappa` enlargement or compatibility lemma.  The sidedness proof
  above deliberately does not consume that rider.
- Notation 8.1 and Statement 8.1 have the same pre-existing over-broad `m_F`
  domain and remain audit targets.

## 5. Computational evidence and scope

Coordinator replay of the frozen producer checker passes all 54,854 grouped
checks.  The Opus review independently checks the bracket in a Laurent ring,
136,080 rational-order classifications, 24,000 zero-bracket cases, 8,000
negative-order cases and 3,000 threshold profiles.  It correctly notes that
the producer checker never uses a nonconstant `q` and therefore cannot detect
a sign mutation in the bracket; the independent reconstruction, not that
group, verifies the sign.

This theorem repairs Proposition 5.1, the pole-set non-leakage and the named
Section 7 uses.  It is not a landing theorem, not `RPMC(C)`, not a degree
bound, not a counterexample, and not JC2.
