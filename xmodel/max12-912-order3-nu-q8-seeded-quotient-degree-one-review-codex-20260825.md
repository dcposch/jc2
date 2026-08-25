# Hostile audit: selected-Q8 seeded-quotient degree-one shortcut

Date: 2026-08-25  
Reviewer: Codex, independent audit of the coordinator lemma  
Status: **CORE CONDITIONAL IMPLICATION CONFIRMED; one multiplicity wording
repair and explicit regularity acceptance gates required**

## 1. Verdict

The quotient direction and the degree-one shortcut are correct.  Let `S` be
the generic localized polynomial ring, `A=S/I`, and let `P` be the prime of
the reviewed `H`-dominant integral source component.  Since `H in P`, there
is a surjection

```text
B=S/(I,H)=A/(H)  ->  S/P=A/P.
```

Geometric integrality and `deg_v(H)=190` give

```text
dim_K(A/P)=190*d,       d=[Frac(A/P):K(v)/(H)]>=1.
```

Thus an exact `dim_K(B)=190` endpoint forces `d=1`.  The surjection then has
equal-dimensional source and target and is an isomorphism:

```text
B ~= A/P ~= K[v]/(H),       (I,H)=P.
```

This proves that the seeded cut is a reduced field, that the known component
has source-to-image degree one, and that it is the unique generic support of
`A` on which `H` vanishes.  It does not require the whole algebra `A` to be
finite or to have length 190, and it leaves components on which `H` is
nonzero completely untouched.

## 2. Required wording repair: ambient multiplicity

The sentence

> the only generic source component supported over `H`, including
> scheme-theoretic multiplicity

is safe only if “multiplicity” refers to the seeded cut `B`.  It is not a
consequence about the ambient source algebra `A`.  Counterexample:

```text
A=E[epsilon]/(epsilon^2),       H=epsilon,
A/(H)=E,                       P=(epsilon).
```

Here the seeded cut is a reduced field of length one over `E`, while the
ambient component has generic length two.  Accordingly the exact promotion
from Section 2 must read:

```text
the H-cut has one reduced support and C has field degree one;
ambient cycle multiplicity is not yet inferred.
```

This does not damage the intended all-contact route.  Once the degree-one
graph is proved to contain one full corrected-Q8 contact, the full relative
Jacobian unit makes the source local ring regular there; localization at the
component generic point then proves the ambient component is generically
reduced.  The multiplicity conclusion belongs after, not before, the contact
regularity certificate.

## 3. Exact coordinate-regularity acceptance gate

The seeded basis must provide more than `seeded_vdim=190`.  Acceptance needs:

1. a pure-Singular standard basis for the exact same localized ideal
   `I+(H)`, with every original source generator and `H` reducing to zero;
2. a certified 190-element standard-monomial basis, not a partial or
   parser-dependent dimension report;
3. for each of the seven internal/source coordinates, an exact identity in
   `B ~= K[v]/(H)` of the form `y=a(w,v)/b(w,v)`;
4. exact substitution of all coordinate identities into the same eight
   source equations modulo `H`;
5. after clearing coefficient poles in `K=k(w)`, a representative satisfying
   `gcd(b(0,v),Q8bar)=1` for every coordinate;
6. reduction of each value modulo `Q8bar` to the frozen full-contact value,
   including the `v` relation and inverse-localizer equation.

Condition 5 is sufficient only together with the frozen facts

```text
H(0,v)=Q8bar(v)*C(v),
gcd(Q8bar,C)=gcd(Q8bar,H_v(0,v))=1.
```

Those facts make each corrected-Q8 plane contact a smooth local point of
`H`, so a denominator prime to `Q8bar` gives a regular graph section there.
The value checks then put that graph at the **full source** contact, not just
at its `(w,v)` projection.

At each matched full contact, the source `8 x 8` Jacobian unit gives completed
local ring `k[[w]]`.  Hence there is one local component in every dimension;
the closure of the degree-one graph is that component.  Repeating the same
unit/value check over `Fbar_127[v]/(Q8bar)` attaches all eight contacts to the
one `H`-supported component.  This step also supplies ambient generic
reducedness as explained in Section 2.

## 4. Remaining firewalls

Even after a seeded PASS plus the coordinate certificate, the conclusion is
only the mod-127 degree-one/all-eight-contact component statement.  It does
not exclude unrelated source components, and none need be excluded for this
contact grouping.  Characteristic-zero specialization still requires the
common `Z_(127)` source and integral-contact/Jacobian bridge.  Taylor
polynomiality, the terminal trajectory equation, the repaired no-merger
application, the infinity exclusion, maximum twelve, and JC2 remain
separate.

Subject to the ambient-multiplicity wording repair and the six explicit
coordinate gates above, the conditional shortcut is **CONFIRMED**.
