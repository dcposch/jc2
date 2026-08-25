# Scope audit: universal order-three terminal Belyi classification

Date: 2026-08-25  
Method: read-only identity/provenance audit; no computation

## Verdict

**CONFIRMED, as a necessary classification on actual trajectories.**  The
divisor/Belyi argument in the selected-Q8 terminal report does not use Q8 or
`nu` after the terminal scalar equation has been formed.  It therefore
globalizes to the entire nontrivial-Kummer `(9,12)` branch, provided the
reviewed monic/depressed Faber normalization, order-three covariance, and
history condition `3|deg(h)` are imported explicitly.

For any actual trajectory in that branch,

```text
u^3=h,       r8=u^2 R,       9 r8'=j/u,       j!=0,
```

with `R in C(x)`.  Hence `S=r8^9=h^6 R^9` lies in `C(x)`, is nonconstant,
and direct differentiation gives

```text
h^3 (S')^9 = j^9 S^8.                              (1)
```

The nonconstancy is automatic from the original row: `r8'=j/(9u)!=0`.
Applying the already CONFIRMED divisor argument to `(1)` (equivalently its
selected formula with `nu=1` and `Z=S`) gives

```text
S=T^3,       h=C*T^2/(T')^3
```

for nonconstant `T in C(x)`.  Writing reduced `T=A/B`, the same
polynomiality, Wronskian, and infinity proof applies verbatim.  The reviewed
preflight supplies `h in C[x]`, `h` noncube, and `3|deg(h)` on this
nontrivial residual branch; these hypotheses kill both unequal-degree
strata.  Thus `deg A=deg B`, and `T` has the three-value passport already
displayed in the terminal classification.

## Duplicate and genuinely new scope

The root-free identity `(1)` is not new: it is already independently
CONFIRMED as Claim 5 of the selected-Q8 leaf-4 review.  The repo does not,
however, appear to state the resulting *branch-wide* reuse of Sections 2--4
of the terminal Belyi classifier.  The scope extension is therefore a
provenance/composition lemma, not new divisor algebra.

In the selected proof, `nu` only supplied the constant rescaling
`S=nu^10 Z`; Q8 supplied local quotient/contact coordinates used by later
infinity-primitivity claims.  Neither is used by the bare Belyi
classification.  Consequently the branch-wide theorem may consume the
passport shape, but not the Q8-specific contact parity, eight-contact
partition, evenness of the contact index, or any selected-component kill.

## Missing hypotheses and firewall

The composition must state all of the following:

1. characteristic zero and an actual Keller trajectory, not a coefficient-
   fibre point;
2. the reviewed order-three Faber covariance `r8=u^2R` and terminal row;
3. the monic polynomial core `h`, nontrivial Kummer class (`h` noncube), and
   the history residue `3|deg h`;
4. `S!=0`, here discharged more strongly by `S` nonconstant; and
5. the original terminal row remains charged in any converse direction.

Taking ninth powers is only a necessary descent.  A rational Belyi datum
`(T,h)` need not reconstruct `r8`, the seven lower Laurent rows, either
Taylor-boundary family, or an original polynomial pair.  The cyclic terminal
positive controls still prevent an exclusion.  No all-`(9,12)` emptiness,
maximum-partial-degree theorem, counterexample, or JC2 conclusion follows.

