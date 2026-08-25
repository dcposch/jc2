# Selected-Q8 good-reduction no-merger lemma

Date: 2026-08-25  
Status: **producer proof lemma; hostile different-model review required;
computational hypotheses not yet discharged**

## 1. Purpose

The active Q8 computation is over `F_127`, whereas the primitive contact
grouping and infinity exclusion are in characteristic zero.  A finite-field
component containing all eight reduced contacts cannot simply be called a
characteristic-zero component: distinct horizontal components can merge at
a bad prime.  This note isolates a sufficient multiplicity-one criterion
that rules out exactly that failure.

## 2. No-merger lemma over a DVR

Let `R` be a DVR with uniformizer `pi`, fraction field `K`, and algebraically
closed residue field `k`.  Let `X` be a finite-type `R`-scheme.  Let `C` be a
geometrically integral one-dimensional irreducible component of the special
fibre `X_k`, and let `q_1,...,q_m` be closed points of `C`.  Assume:

1. `X -> Spec R` is flat at the generic point `eta_C` of `C`;
2. `X_k` is reduced at `eta_C`;
3. at each `q_i`, the special fibre is reduced and has `C` as its unique
   one-dimensional local irreducible component;
4. for each `i`, a geometric irreducible curve component `Y_i` of `X_K` has
   an integral model whose closure in `X` contains `q_i`.

Then all `Y_i` are the same geometric irreducible component of `X_K`.

The statement is unchanged after replacing the original DVR by a common
finite extension over which the finitely many geometric components and
marked points are defined.  Thus it applies to geometric components.

## 3. Proof

Localize `X` at `eta_C` and write its noetherian local ring as `A`.  Flatness
over the DVR says that `pi` is a non-zero-divisor in `A`.  Because `C` is the
only special-fibre component at its generic point and the special fibre is
reduced there, `A/pi A` is a field, hence a domain.

These two facts force `A` itself to be a domain.  Indeed, if `ab=0`, then
domainhood modulo `pi` makes one factor divisible by `pi`; cancel the
non-zero-divisor `pi` and repeat.  If the other factor is not eventually
divisible by `pi`, the first lies in every `pi^n A`; if both are repeatedly
divisible, remove their maximal finite powers first.  Krull intersection in
the noetherian local ring gives `intersection_n pi^n A=0`.  Hence one of
`a,b` is zero.

Now fix `Y_i` and let `bar Y_i` be its integral closure inside `X` after the
chosen finite DVR extension.  It is horizontal and integral, so its
coordinate rings are torsion-free, hence flat, over the DVR.  Since
`q_i in bar Y_i`, the flat dimension formula (equivalently, the principal
ideal theorem applied to `pi`) gives a one-dimensional special-fibre germ of
`bar Y_i` through `q_i`.  By assumption 3 that germ lies on `C`; because both
are one-dimensional and `C` is irreducible, `bar Y_i` contains `eta_C`.

Thus every `bar Y_i` determines a minimal prime of `A`.  But `A` is a
domain, so it has only one minimal prime.  All `bar Y_i`, and therefore all
generic components `Y_i`, coincide.  This proves the lemma.

The proof also identifies the exact bad-reduction failure: if two horizontal
components really merge, then at least one of flatness, generic reducedness,
or local uniqueness at the marked reductions must fail.  A bare irreducible
set-theoretic reduction is insufficient.

## 4. Concrete selected-Q8 discharge checklist

Apply the lemma after base change from `Z_(127)` to a DVR containing the
eight corrected-Q8 contact roots.  The following evidence is required:

1. **Integral model.**  The divided selected-Q8 equations, localizer, contact
   coordinates, and the corrected octic must be integral at 127.  The octic
   reduction must remain squarefree and every contact-coordinate denominator
   must be a unit at its roots.
2. **A genuine special component.**  The candidate `H(w,v)` and seven
   reconstructed coordinate functions must satisfy all eight original rows
   identically over `F_127(w)[v]/(H)`, with `v` retained.  Arithmetic
   irreducibility from the two exact specializations plus the smooth
   `F_127` point must give geometric integrality of its image component
   `C_127`.
3. **Multiplicity one.**  At one point of `C_127`, the full relative
   eight-by-eight Jacobian in the internal variables must be a unit.  This
   makes the selected quotient étale over the `w`-line there, so it is flat
   and reduced at `eta_C`.
4. **All full contacts, not only projections.**  The coordinate functions
   must have finite limits at `w=0` along the simple `Q8bar` factor of
   `H(0,v)` and those limits must equal the eight corrected contact
   coordinates.  The already frozen projection certificate supplies only
   `H(0,v)=Q8bar*C`, `gcd(Q8bar,C)=1`, and `H_v` a unit.
5. **Local uniqueness at the reductions.**  A full source-derived local
   Jacobian/unit calculation modulo 127 must show that the divided quotient
   special fibre is reduced and has `C_127` as its unique one-dimensional
   component at each contact.  Characteristic-zero formal uniqueness alone
   does not substitute for this good-prime check.
6. **Specialization of the marked branches.**  The reviewed characteristic-
   zero non-parity contact branches must extend over the chosen DVR and
   specialize to those eight full contact points.  Unit denominators and the
   same implicit-function minors at 127 are the intended certificate.

Once items 1--6 are exact, the lemma forces all eight characteristic-zero
selected contact branches onto one geometric component.  The confirmed
primitive grouping then selects the all-eight alternative, and the confirmed
infinity theorem excludes a registered actual trajectory on it.

## 5. Scope firewall

This is a conditional specialization lemma, not a completed Q8 bridge.  In
particular, the current `(w,v)` boundary certificate does not discharge the
seven coordinate functions, full contact limits, mod-127 local uniqueness,
or integral specialization.  Even after the selected-Q8 trajectory lane is
closed, components disjoint from the eight contacts, other maximum-twelve
strata, lower maximum degree, landing/coverage, and JC2 remain separate.

