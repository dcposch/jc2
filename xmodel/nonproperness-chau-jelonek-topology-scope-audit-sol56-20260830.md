# Primary-source scope audit: Chau topology versus Jelonek Euler positivity

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`nonproperness_topology_audit` lane)  
Frozen basis: `f047ed97dc4ef7181069c4d6d42c47ba6557640a`  
Lifecycle: **FINAL + VERIFIED / PRODUCER-CHECKED / DIFFERENT-MODEL REVIEW REQUIRED**  
Evidence: **PRIMARY-SOURCE SCOPE AUDIT + EXACT TOPOLOGICAL DERIVATION**

## 0. Verdict

Let

```text
F:C2 -> C2
```

be a polynomial map with nowhere-vanishing Jacobian, and let `A=A_F=S_F`
be its nonproper-value set.  Over `C`, the Jacobian polynomial is then a
nonzero constant.  If `A` is nonempty, the maximum safe conclusions from
the primary sources are:

1. every irreducible component of `A` has affine-line normalization, and
   the projective closure of the whole curve has one point at infinity
   (Chau 2004);
2. the whole exceptional curve is not simply connected (Chau 2003,
   Corollary 3; here the exceptional set equals `A` because `F` has no
   critical values);
3. consequently, **if `A` is connected, then**

   ```text
   b1(A) >= 1,                 chi(A)=1-b1(A) <= 0.       (0.1)
   ```

4. Jelonek's published Euler-positivity statement does **not** say that an
   arbitrary connected `A` has positive Euler characteristic.  Theorem 1.2
   of the correct arXiv version 3 first assumes that `S_F` is **smooth**;
   only under that standing hypothesis does its connected clause give
   `chi(S_F)>0`.  Its proof uses smoothness to make the restriction over
   `S_F` a finite covering before writing the Euler formula.

Thus Chau and Jelonek contradict one another only under the simultaneous
hypotheses

```text
A nonempty, smooth, and connected.
```

That case was already excluded more directly by Jelonek's plane Theorem
1.1 (`A` cannot be a curve without self-intersections).  There is **no
general connectedness exclusion**, no contradiction for a connected
singular `A`, and no new unconditional rank-four gate.

For the canonical finite normalization used by the campaign, the reduced
branch `B` is only a componentwise subcurve of `A`; equality `B=A` is not
known.  Cycles and connectedness of `A` do not pass to an arbitrary union of
its components.  If one separately proved `B=A` and connectedness, (0.1)
would give `b1(B)>=1`, but the current reviewed rank-four theorem already
proves that stronger conclusion directly, without `B=A`.

## 1. Objects and terminology

For a generically finite polynomial map, write

```text
A_F={a in C2 : there are z_n -> infinity with F(z_n) -> a}.
```

Jelonek writes this set as `S_F`.  Chau's 2003 paper uses the exceptional
value set `E_F`, the smallest target set outside which `F` is a locally
trivial smooth fibration.  For a nonsingular polynomial map, the critical
value set is empty and Chau explicitly identifies

```text
E_F=A_F.                                                   (1.1)
```

All occurrences of `A`, `A_F`, and `S_F` below refer to the entire reduced
nonproper-value curve, not to the branch support of a finite normalization.
The word “simply connected” has its usual topological meaning and therefore
includes connectedness.

For a reduced affine curve `C`, `chi(C)` denotes its topological Euler
characteristic.  For complex algebraic curves this agrees with the
compactly supported Euler characteristic used in constructible
additivity.

## 2. Primary-source statements and version firewall

### 2.1 Chau: component normalization and one common point at infinity

Nguyen Van Chau, *Note on the Jacobian condition and the non-proper value
set*, Annales Polonici Mathematici **84** (2004), 203--210,
DOI `10.4064/ap84-3-2`, Theorem 1 and Corollary 2:

- for a Keller map with nonempty `A_F`, every irreducible component admits
  a nonconstant polynomial parametrization from `A1`; and
- the projective closure of the whole `A_F` has exactly one point at
  infinity.

Primary copies checked:

```text
https://www.impan.pl/en/publishing-house/journals-and-series/
  annales-polonici-mathematici/all/84/3/85283/
  note-on-the-jacobian-condition-and-the-non-proper-value-set
https://arxiv.org/abs/math/0305088

PDF bytes: 112845
SHA-256: 8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
```

The polynomial parametrization gives more than rationality.  If `C_i` is
an irreducible component, its parametrization lifts to the normalization
and extends to a nonconstant map from `P1` to the smooth projective
normalization.  Hence that projective normalization has genus zero.  All
finite source points map to the affine curve, so the affine normalization
has at most one puncture; affineness gives exactly one.  Therefore

```text
Normalization(C_i) = A1.                                  (2.1)
```

### 2.2 Chau: exclusion of the whole simply connected exceptional curve

Nguyen Van Chau, *Two remarks on non-zero constant Jacobian polynomial
maps of C2*, Annales Polonici Mathematici **82** (2003), 39--44,
DOI `10.4064/ap82-1-4`, Theorem 2 and Corollary 3, states that the exceptional
value set of a Keller map cannot be a simply connected curve.

Primary copies checked:

```text
https://www.impan.pl/en/publishing-house/journals-and-series/
  annales-polonici-mathematici/all/82/1/84523/
  two-remarks-on-non-zero-constant-jacobian-polynomial-maps-of-bbb-c-2
https://arxiv.org/abs/math/0408048

PDF bytes: 102043
SHA-256: be0b5b6ead20313d475ea1b9862f1781143f017322afbf863f328acc7d7c7118
```

By (1.1), this applies to the whole `A_F`.  Its scope must not be enlarged:
it does not state that every irreducible component of a reducible `A_F` is
nonsimply-connected, and it does not state that every component union is
nonsimply-connected.

### 2.3 Jelonek: the smoothness hypothesis survives into Euler positivity

Zbigniew Jelonek, *A note on the Jacobian Conjecture*, Colloquium
Mathematicum **170** (2022), 85--90,
DOI `10.4064/cm8671-12-2021`, arXiv `2011.03472v3`:

- Theorem 1.1: for `n=2`, `S_F` cannot be a curve without
  self-intersections.
- Theorem 1.2 begins: assume `S_F` is smooth.  It then proves that `F` is
  surjective and, if `S_F` is connected, that `chi(S_F)>0`.

The standing smoothness assumption is load-bearing, not punctuation.  In
the proof, Jelonek first uses smoothness of `S=S_F` in the finite Zariski
Main factorization to show that the source preimage `T` of `S` is closed in
the finite completion.  This makes `T->S` a finite topological covering of
some degree `s`.  Only then, after adding connectedness, does the proof set
`a=chi(S)` and use

```text
1 = (1-a)q + s*a = q-a(q-s),                              (2.2)
```

where `q` is the generic degree.  Without smoothness the proof has not
established the proper finite covering `T->S`, so neither `s` nor (2.2) is
available.  The theorem therefore does not license

```text
S_F connected  ==>  chi(S_F)>0                            (FALSE SCOPE).
```

The exact correct source checked was:

```text
https://export.arxiv.org/pdf/2011.03472v3
PDF bytes: 124923
SHA-256: fd067d34cdb76246aeb86356cb859523703ab46310d694d738724f4b4c4dbc8c
```

There is an unusually dangerous version-history trap.  The current arXiv
metadata abstract advertises a stronger connectedness claim, but the
author's own current metadata comment says that versions 4 and 5 are
incorrect and versions 1--3 are correct.  The checked version ledger is:

```text
v1  9d0cc2d264b30267b17fef3ae8394f5cd9c45aceb450cfa7436fa2161f292db3
v2  e344e3f26345013f7b18ef4acd567b0f4c40641e5f41880739e44bd993f4ec98
v3  fd067d34cdb76246aeb86356cb859523703ab46310d694d738724f4b4c4dbc8c  CHARGE
v4  41b3100f454024789220df50807daf6e402da7205e0dedb8bedc6f45bfa2946c  REJECT
v5  5cb1ce790a433611cc22b390ed7c09ef2e01ec80530a333774f487eb88dd027f  REJECT
```

Primary metadata endpoint checked on 2026-08-30:

```text
https://export.arxiv.org/api/query?id_list=2011.03472
```

Accordingly, a search-result abstract or unversioned metadata page is not a
chargeable source for a general connectedness theorem.

## 3. Exact topology of a curve with affine-line normalizations

This section proves the maximum safe consequence rather than inferring it
from slogans about rational curves.

Let `C` be a reduced affine curve with irreducible components
`C_1,...,C_r`, each having normalization `A1`.  Let

```text
nu: disjoint_union_i A1_i -> C
```

be the normalization.  Let `Sigma` be the finite set of points at which
`nu` has more than one preimage, and put

```text
r_p = #nu^(-1)(p),              p in Sigma.
```

Unibranch singularities may be retained with `r_p=1`; they contribute zero.
Normalization additivity gives

```text
chi(C) = r - sum_(p in Sigma)(r_p-1).                     (3.1)
```

Define the bipartite incidence multigraph `Gamma_C` with one vertex for
each irreducible component, one vertex for each `p in Sigma`, and one edge
for each analytic branch over `p`.  Then

```text
chi(Gamma_C)
 = r + #Sigma - sum_p r_p
 = r - sum_p(r_p-1)
 = chi(C).                                                (3.2)
```

Topologically, a finite normalization is the quotient obtained by making
exactly these finite identifications.  Contract each copy of `C` relative
to its finitely many marked preimages to a finite tree.  The quotient shows
that `C` is homotopy equivalent to `Gamma_C`.  Hence

```text
pi1(C) is free of rank b1(Gamma_C),
chi(C)=b0(C)-b1(C).                                      (3.3)
```

Apply this to `A=A_F` using (2.1).  If `A` is connected, (3.3) becomes

```text
chi(A)=1-b1(A).                                          (3.4)
```

Chau Corollary 3 says that the entire `A` is not simply connected.  The
free-group description in (3.3) therefore forces

```text
b1(A)>=1,                 chi(A)<=0.                      (3.5)
```

Equivalently, a connected positive-Euler `A_F` is impossible.  This is the
strongest unconditional connected-case conclusion supplied by the Chau
topology package.  It does **not** say that `A_F` is disconnected.

## 4. What the Chau--Jelonek combination actually proves

Under Jelonek Theorem 1.2's full hypothesis, suppose `A` is smooth and
connected.  Jelonek gives `chi(A)>0`; (3.5) gives `chi(A)<=0`.  Thus no such
`A` exists.

This is valid but not new.  A smooth reduced plane curve has no
self-intersections, so Jelonek Theorem 1.1 already excludes a nonempty
smooth `A` in dimension two.  Alternatively, smoothness and connectedness,
together with (2.1), make `A` itself isomorphic to `A1`, which Chau excludes.

For a connected **singular** `A`, Jelonek Theorem 1.2 supplies no positivity.
The exact live row is instead

```text
A connected and singular,
b1(A)>=1,
chi(A)<=0.
```

There is no contradiction in that row.  Any claim that the two papers prove
all nonempty `A_F` disconnected has silently removed Jelonek's smoothness
hypothesis or charged the author-rejected arXiv versions.

## 5. Counter-controls against stronger readings

### 5.1 One point at infinity does not force connectedness

The reduced plane curve

```text
(y-x^2)(y-x^2-1)=0
```

is the disjoint union of two affine lines in the affine plane, while both
projective closures meet the line at infinity at the single common point
`[0:1:0]`.  Thus “the whole curve has one point at infinity” does not imply
that the affine curve is connected.  This is a logic control, not a claimed
nonproper set of a Keller map.

### 5.2 The Chau structural data allow connected negative Euler curves

Put

```text
C0: y=x^3,
C1: y=x^3+x,
C2: y=x^3+x^2-1,
A0=C0 union C1 union C2.
```

Each component is an affine line, and all three projective closures have
the same unique point `[0:1:0]` at infinity.  Their affine intersections are
five distinct transverse nodes:

```text
C0 cap C1: x=0;                    one point
C0 cap C2: x^2-1=0;                two points
C1 cap C2: x^2-x-1=0;              two points.
```

The incidence graph has `3+5` vertices and `10` edges, hence

```text
b1(A0)=10-8+1=3,             chi(A0)=-2.
```

This curve satisfies the component-normalization and one-point-at-infinity
structural conclusions and is connected, singular, and of negative Euler
characteristic.  Again it is not asserted to arise from a Keller map; it
shows exactly why those structural statements plus Jelonek's
smooth-conditional theorem do not logically force disconnectedness.

### 5.3 Cycles of the whole curve do not pass to a selected subcurve

In the same example, the selected component `B0=C0` is an affine line with
`b1(B0)=0`, while `A0` has `b1(A0)=3`.  Deleting components destroys every
cycle relevant to `B0`.  Therefore a topology theorem about the entire
`A_F` cannot be applied to the canonical branch `B` merely from
`B subset A_F`.

## 6. Canonical branch and rank-four consequence

For the campaign's canonical normalization, write

```text
Y = normalization of Spec C[F,G] in C(x,y),
pi:Y -> A2,
j:A2_source -> Y,
R=NonEt_Y(pi)_red,
B=pi(R)_red.
```

The reviewed interface proves

```text
B subset A_F componentwise: every irreducible B_i is an entire
irreducible component of A_F.                              (6.1)
```

It does not prove `B=A_F`.  Components of the finite boundary
`Y-j(A2)` can be unramified for `pi`; their images contribute to `A_F` but
not to `B`.  Intersections of such extra components with `B`, or among
themselves, can carry the cycles detected by (3.5).

Consequently:

- disconnectedness of `A_F`, if it were known, would not imply
  disconnectedness of `B`;
- `b1(A_F)>=1` does not imply `b1(B)>=1`;
- Chau Corollary 3 cannot be applied componentwise to `B_i`; and
- no rank-four survivor is removed by the present source combination.

There is only the conditional statement

```text
B=A_F and B connected  ==>  b1(B)>=1.                     (6.2)
```

But the campaign already has, for every actual proper rank-four block,

```text
b1(B)>=1
```

from the independent branch-cycle/Euler argument in the following frozen
review integration:

```text
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
```

Thus (6.2) is both conditional on an unpaid equality and redundant in rank
four.  The correct campaign action is to bank (3.5) as an `A_F`-level
topological gate, quarantine the unqualified Jelonek-positivity reading,
and leave the current quartic horns unchanged.

## 7. Reproduction and producer checks

All checks were desk-scale; no CAS or heavy local computation was used.

Primary-source reproduction:

```text
curl -L https://export.arxiv.org/pdf/math/0305088 -o chau-0305088.pdf
curl -L https://export.arxiv.org/pdf/math/0408048 -o chau-0408048.pdf
curl -L https://export.arxiv.org/pdf/2011.03472v3 -o jelonek-v3.pdf
pdftotext -layout SOURCE.pdf SOURCE.txt
shasum -a 256 SOURCE.pdf
```

The following hostile scope checks were performed:

1. retained `smooth` while parsing both clauses of Jelonek Theorem 1.2;
2. traced the smoothness use into the finite-cover premise of (2.2);
3. checked arXiv versions 1--5 and the author's current primary metadata
   warning rather than trusting the unversioned abstract;
4. distinguished the entire exceptional curve from each irreducible
   component;
5. distinguished `A_F` from the canonical branch `B`;
6. verified (3.1)--(3.5) directly from normalization additivity and the
   incidence multigraph; and
7. supplied explicit one-infinity, connectedness, Euler, and subcurve
   counter-controls.

No claim here proves or disproves JC2, proves `A_F` disconnected, proves
`B=A_F`, or strengthens the existing rank-four branch-cycle theorem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15569`.
- Body SHA-256:
  `77f6a9fb40898525fca61c48a5e7e391e0fe8dd77a1cb21a472fc1dd659d7037`.
- Frozen basis: `f047ed97dc4ef7181069c4d6d42c47ba6557640a`.
