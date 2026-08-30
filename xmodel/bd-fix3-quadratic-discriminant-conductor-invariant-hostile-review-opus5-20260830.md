# Hostile review: cubic-block trace discriminant and order/normalization index

Date: 2026-08-30 UTC
Reviewer: Opus 5, independent hostile algebraic review
Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1` (verified at HEAD)
Subject seal verified: body `6323` bytes,
`3362a7913801a180cf0d4ee06e9bf08ee13324ea598d72e0e8f797d59ff28ac5`;
both companion integration seals verified byte-exact.

Execution scope: shell available; all algebra below is hand/`python3`-free exact
symbolic work reproduced independently from the displayed AL3 multiplication
table. No CAS, no Singular, no `jc2-lean` contact, no input edited.
No exit-price assertion is made, so no `charge_basis` line is emitted.

## 0. Itemized verdict

| # | Item | Verdict |
|---|---|---|
| 1 | Trace Gram determinant under `GL2(A)` trace-zero change; `A=C[u,v]` unit scalar; which object is invariant | **CONFIRMED** (hypotheses reducible, see C1) |
| 2 | `Tr(z^2),Tr(zw),Tr(w^2)`, full determinant, identification with the binary-cubic discriminant, coefficient-degree four, `deg<=8` | **CONFIRMED** (scalar sharpened, C2) |
| 3 | Support = non-etale/branch divisor; multiplicity separation; hypotheses | **CONFIRM_WITH_CORRECTIONS** (C3, C4) |
| 4 | Height-one order/normalization identity; object represented by `ord(det M)`; torsion-free case | **CONFIRM_WITH_CORRECTIONS** — provable strictly stronger over `C[u,v]` (C5, C6) |
| 5 | Conductor/curve interface cautions | **CONFIRMED as stated**; one wording is still too strong (C7) plus a required Gorenstein caveat (C8) |
| 6 | Campaign consequence, controls, rejection of the two shortcuts | **CONFIRM_WITH_CORRECTIONS**; §5 nonclaim is understated and wrong as written (C9) |

Nothing in the packet is **REFUTED**. One nonclaim (§5, first sentence) is
false in the safe direction, i.e. the packet proves more than it admits.

## 1. Independent reconstruction

### 1.1 Traces and determinant (item 2)

From the AL3 table `z^2=2(a^2-bd)+az+bw`, `zw=-(ad-bc)-dz-aw`,
`w^2=2(d^2-ac)+cz+dw`, multiplication by `z` and by `w` have zero trace, so
`(1,z,w)` is a genuine trace-zero basis, and with `Tr(1)=3`

```text
Tr(z^2)=6(a^2-bd),   Tr(zw)=-3(ad-bc),   Tr(w^2)=6(d^2-ac).
```

All three reproduce. The Gram matrix is block diagonal `diag(3,G_E)` since
`Tr(z)=Tr(w)=0`, hence

```text
Delta = 3*[36(a^2-bd)(d^2-ac) - 9(ad-bc)^2]
      = 27*[4(a^2-bd)(d^2-ac) - (ad-bc)^2]
      = 81a^2d^2 - 108a^3c - 108bd^3 - 27b^2c^2 + 162abcd.
```

This is (2.1) **on the nose**, and it equals `Disc(Phi)` for
`Phi=bX^3-3aX^2Y+3dXY^2-cY^3` in the *classical* convention
`Disc(pX^3+qX^2Y+rXY^2+sY^3)=q^2r^2-4pr^3-4q^3s-27p^2s^2+18pqrs`
with `(p,q,r,s)=(b,-3a,3d,-c)`: the residual "convention scalar" is exactly
`1`, not merely nonzero.

Two independent instance checks of table-plus-formula consistency:

* `(a,b,c,d)=(0,1,-1,0)`: table gives `z^2=w`, `zw=-1`, `w^2=-z`, hence
  `z^3=-1`, so `B=A[z]/(z^3+1)`, `Disc=-27`; (2.1) gives `-27b^2c^2=-27`.
* `(a,b,c,d)=(0,1,0,1)`: `Phi=X^3+3XY^2`, classical `Disc=-4*27=-108`;
  (2.1) gives `-108bd^3=-108`. Associativity check
  `z(zw)=(zz)w=2-w` holds.

Signs and scalars are therefore fully confirmed, including the `-3` in
`Tr(zw)` (a sign slip there would change the `-27b^2c^2` term).

**Coefficient degree four**: every monomial `a^2d^2, a^3c, bd^3, b^2c^2, abcd`
has degree exactly four, so `Delta` is homogeneous of degree four in
`(a,b,c,d)`. Hence `deg_{u,v} Delta <= 4*max deg(a,b,c,d)`, and (2.2) follows.
Confirmed.

**Identically zero / cancellation.** `Delta=0` in `A` iff the generic fibre is
non-etale, which the standing generic-separability hypothesis excludes; the
packet states this correctly. Cancellation to `deg Delta < 8` is possible and
is *not* an obstruction to anything, which the packet also states correctly.

### 1.2 Invariance (item 1)

In characteristic zero `E=ker(Tr_{B/A})` is canonical (`(1/3)Tr` splits
`A*1`), so any basis of the displayed shape differs by `M=diag(1,g)`,
`g in GL2(A)`; `G |-> M^T G M` gives `Delta |-> det(g)^2 Delta`, and
`det(g) in A^* = C^*` for `A=C[u,v]`. So: the **polynomial is not invariant**
(only up to `C^*`); the **ideal `(Delta)`, the principal divisor `div(Delta)`,
and the zero scheme `V(Delta)` are invariant**. The packet's §1 statement is
exactly this and is confirmed.

Cross-check against the packet's own remark on the binary-cubic tensor: plain
substitution gives discriminant weight `6`; the Delone--Faddeev/Miranda twist
`f |-> (det g)^{-1} f(.g)` contributes `det(g)^{-4}` because `Disc` has
coefficient-degree four; net `6-4=2`, matching `(1.2)`. The packet leaves the
"net exponent" unnamed; it is `2`, and the two computations agree. Equivalently
`Disc` is a section of `(det E)^{\otimes 2}`.

## 2. Corrections

**C1 (item 1, hypotheses are reducible).** §0 lists "free global trace-zero
module" as a hypothesis. Over `A=C[u,v]` it is automatic: `E` is a projective
rank-two summand of a finite locally free module, hence free by
Quillen--Suslin. Moreover divisor invariance needs neither the trace splitting
nor `A^*=C^*`: for *any* `A`-basis change of `B` by `h in GL3(A)`,
`Delta |-> det(h)^2 Delta` and `div(det h)=0` because units have zero divisor.
The splitting is needed only to define `(a,b,c,d)`. Net: §1's headline is true
under strictly weaker hypotheses than advertised.

**C2 (item 2, scalar).** Replace "up to a fixed nonzero convention scalar" by
the exact statement `det G = Disc(Phi)` in the classical convention. The packet
already asserts equality with (2.1); pinning the convention removes the last
place a reader could reinsert an unknown scalar.

**C3 (item 3, "branch divisor" is a set-level statement).** For `B` finite
locally free and generically separable, `V(Delta)` equals the non-etale locus
and its image is the branch locus — *set-theoretically*. Writing "support is
the non-etale/branch divisor" invites reading `div(Delta)` as the reduced
branch divisor. Four objects must stay separate:

```text
reduced source ramification R_red   (on Spec B)
different  d_{B/A}                  (on Spec B, ord = e-1 when tame)
discriminant div(Delta)             (on Spec A, = Nm(different) when B is A-free)
reduced branch b_red = (image R)_red(on Spec A)
```

For a tame `e=3` point, `ord(different)=2` and `ord(Delta)=2` while
`b_red` has multiplicity `1`; for simple branching `ord(Delta)=1`. So
`div(Delta)` is neither reduced nor equal to the different. The packet's §2
last sentence says this; §2's preceding clause and §3's phrase "trace
discriminant/different contribution" conflate source and target objects and
should be split as above.

**C4 (item 3, hypotheses actually used).** `V(Delta)=` non-etale locus needs
finite *locally free* (flat + finite presentation) and char `0` (or `2,3`
invertible); it does **not** need `B` normal, `A` normal, or purity of the
branch locus — `V(Delta)` is automatically pure codimension one in
`Spec C[u,v]` whenever `Delta` is a nonzero nonunit. Normality of `A` enters
only in §3; normality of `B` only in §3's "first term is the normalized cover".
The packet does not misuse these, but it also does not say which section needs
which; the campaign should not import §3's normality into §1--§2.

**C5 (item 4, the exact global object).** For a general normal noetherian `A`
and finite torsion-free full-rank orders, the correct global object is the
**effective Weil divisor**

```text
D_idx = sum_p length_{A_p}((Otilde/O)_p) * [p]
      = divisorial part of Fitt_0(Otilde/O),
```

and `ord_p(det M_p) = length_{A_p}((Otilde/O)_p)` (Smith normal form:
`det M_p = unit * prod d_i`, `Fitt_0 = (prod d_i)`, `length = sum ord(d_i)`).
The packet's identification is correct; the length reading is missing and is
the one the curve interface will want. Effectivity holds since `M_p` has
entries in `A_p`; orientation `Disc(O) = Disc(Otilde) + 2*D_idx` is correct —
the *smaller* order has the *larger* discriminant.

If `O` or `Otilde` is only finite torsion-free rather than locally free, then
(i) nothing changes at height one (finitely generated torsion-free over a DVR
is free), so (3.1) and (0.1) survive verbatim; but (ii) there is no global
`det M` and no global discriminant polynomial, so `Disc(-/A)` must be *defined*
as the height-one divisor rather than as `div` of an element — the packet
should say this explicitly, since §1--§2 do produce a polynomial and the two
sections are silently glued in §0; and (iii) `Fitt_0(Otilde/O)` may have
support in codimension `>= 2` that `D_idx` discards, so the passage from the
ideal to the divisor is lossy.

**C6 (item 4, strictly stronger statement is available and should be promoted
instead).** Over `A=C[u,v]` the torsion-free caveat is vacuous. If `B` is
reduced, its integral closure `Otilde` is finite over `A` (excellent ring), is
a product of normal domains of dimension two, hence CM, hence
`depth_{A_n}(Otilde_n)=2=depth(A_n)`, so `pd_A(Otilde)=0` by
Auslander--Buchsbaum, so `Otilde` is projective and — Quillen--Suslin — **free
of rank three**. Therefore a *global* inclusion matrix `M in M_3(A)` exists,
`Fitt_0(Otilde/B)=(det M)` is **principal**, and (0.1) upgrades from a
height-one statement to an exact identity of polynomials:

```text
Delta_B = (det M)^2 * Delta_Otilde     (equality, not up to C^*, in fixed bases)
div Delta_B = div Delta_Otilde + 2 div(det M),   div(det M) effective.
```

This is the correct maximum form; see §3 below.

**C7 (item 5, one wording still too strong).** §0's "The index is the
determinant/Fitting divisor of the lattice quotient" and the title's "conductor
index" invite the conflation `D_idx = conductor`. They are different objects.
Minimal counterexample over a DVR `R` with uniformizer `pi`: take
`Otilde=R x R x R`, `O = R + pi*Otilde = {(x,y,z): x=y=z mod pi}`. Then
`Otilde/O =~ (R/pi)^2`, so `ord(Fitt_0)=2` but `ord(Ann(Otilde/O))=1`. In
general `Fitt_0 subset Ann subset sqrt(Fitt_0)`, so the index divisor
*dominates* any annihilator/conductor divisor, with equality only when the
quotient is cyclic at that prime. Recommended wording: "index (Fitting/length)
divisor", and never "conductor divisor" without a cyclicity hypothesis.

**C8 (item 5, missing Gorenstein caveat).** Even after a legitimate slice, the
classical curve dictionary `length(Otilde/c) = 2*delta` requires the sliced
order to be **Gorenstein**; rank-three orders arising here need not be. Same
example: `R + pi*(R x R x R)` is the spatial triple point (three coordinate
axes in `A^3`), `delta=2`, not Gorenstein, whereas the plane ordinary triple
point has `delta=3`, is Gorenstein, and has the *same* normalization and the
same branch count. So `delta` is not a function of branch data, and any
conductor dictionary must carry the Gorenstein hypothesis. The packet's §3
caution list (slice, `Tor`, correct order, vertical components, nonreduced
infinity) is correct but omits this.

Also, and independently: `Otilde ⊗_A A/L` is generally **not** the
normalization of `B ⊗_A A/L` (normalization does not commute with base change),
so a sliced index computes `length((Otilde⊗A/L)/(B⊗A/L))`, which is only a
**floor** for `delta` of the sliced curve. This is exactly the
FALLACY-v2 floor/attainment pattern; equality needs a separate theorem. The
`Tor` condition is checkable in our free setting: since `B, Otilde` are both
`A`-free, `Tor_1^A(Otilde/B, A/L) = ker(M mod L)`, which vanishes iff `L` is
not a component of `div(det M)`. So "transversality" has an exact algebraic
form: **the slice must avoid the components of the index divisor**.

**C9 (item 6, §5 nonclaim is understated and, as written, false).** §5 says
"This packet proves no bound on the minimum degree of Miranda coefficients over
all bases." A lower bound follows immediately from the packet's own two
ingredients (basis-invariance of `div Delta`, coefficient-degree four):

```text
d_min := min over global trace-zero bases of max total deg(a,b,c,d)
d_min >= ceil( deg Delta / 4 ).
```

This is the only genuinely new *basis-free* campaign lever in the packet, and
it should be promoted, not disclaimed. The intended (correct) nonclaim is that
no **upper** bound on `d_min` follows. Replace "no bound" with "no upper
bound".

## 3. Maximum exact theorem safe to promote

> **THM D-INV.** Let `A=C[u,v]`, `B` a finite locally free `A`-algebra of rank
> three, generically separable. Put `E=ker(Tr_{B/A})` (free of rank two),
> `e=(1,z,w)` with `(z,w)` an `A`-basis of `E`, `Delta_e=det(Tr(e_ie_j))`.
>
> (i) For `h in GL3(A)` acting on any `A`-basis of `B`,
> `Delta |-> det(h)^2 Delta` with `det(h) in C^*`. Hence `(Delta)`,
> `div(Delta)`, `V(Delta)` are basis-independent; the polynomial is defined
> only up to `C^*`. Trace-zero changes are the case `h=diag(1,g)`.
>
> (ii) With the AL3 table, `Tr(z^2)=6(a^2-bd)`, `Tr(zw)=-3(ad-bc)`,
> `Tr(w^2)=6(d^2-ac)`, and
> `Delta = 27[4(a^2-bd)(d^2-ac)-(ad-bc)^2]
> = 81a^2d^2-108a^3c-108bd^3-27b^2c^2+162abcd = Disc(Phi)`
> in the classical binary-cubic convention (scalar exactly `1`).
>
> (iii) `Delta` is homogeneous of degree four in `(a,b,c,d)`. Hence
> `deg_{u,v} Delta <= 4 * max deg(a,b,c,d)`; in particular quadratic
> coefficients give `deg Delta <= 8`, and conversely
> `d_min >= ceil(deg Delta / 4)` in every global trace-zero basis. **No upper
> bound on `d_min` follows.**
>
> (iv) `Delta != 0`, and `V(Delta)` is exactly the non-etale locus, i.e. the
> branch locus as a set. Its multiplicities are `Nm(different)` exponents
> (`e-1` per tame point, summed over the fibre), not the reduced branch divisor
> and not the reduced source ramification.
>
> (v) If in addition `B` is reduced with integral closure `Otilde`, then
> `Otilde` is `A`-free of rank three, the inclusion has a global matrix
> `M in M_3(A)` with `det M != 0`, `Fitt_0(Otilde/B) = (det M)` is principal,
> and exactly
> `Delta_B = (det M)^2 Delta_Otilde`, i.e.
> `div Delta_B = div Delta_Otilde + 2 div(det M)` with `div(det M)` effective
> and `ord_p(det M) = length_{A_p}((Otilde/B)_p)`.
> Consequently `deg Delta_B <= 8` forces `deg(det M) <= 4` and
> `deg Delta_Otilde <= 8 - 2 deg(det M)`.

(v) is strictly stronger than the packet's §0/§3 (global polynomial identity
and principal Fitting ideal, not merely a height-one divisor split), and (iii)'s
second half is strictly stronger than the packet's §5. Everything else is the
packet's content with C2/C3/C5 wording.

## 4. Rejection of the two false shortcuts

**"Square leading discriminant implies Galois" — REJECTED.** `B ⊗ C(u,v)` has
Galois group of its Galois closure inside `A_3` iff `Delta` is a square in
`C(u,v)^*`; over the UFD `C[u,v]` that is equivalent to `Delta` being a square
in `C[u,v]` (and the `C^*` ambiguity is harmless because `C` is algebraically
closed, so every unit is a square). The leading homogeneous form of a square is
a square, so the implication runs *only* in that direction; its converse fails.
Minimal counterexample: `Delta = u^8+v` has leading form `u^8=(u^4)^2`, yet
`u^8+v` is irreducible (degree one in `v`), hence not a square. Two further
independent gaps in the shortcut: (a) `A_3` includes the totally split case
`C(u,v)^3`, which is not a cubic field at all, so "square" never by itself
produces a Galois *field* extension; (b) squareness must be tested on the full
affine `Delta`, and the packet correctly says the bound and the invariant are
statements about the full affine discriminant, not about the infinity form.

**"Degree-eight discriminant implies low-degree Miranda basis" — REJECTED as a
non-sequitur.** The only proved inequality is `deg Delta <= 4 d`; its
contrapositive bounds `d` from *below*, never from above. There is no reverse
inequality in the packet and none is formal: an upper bound would require a
reduction theory for binary cubic forms under `{g in GL2(C[u,v]) : det g in
C^*}` over a two-dimensional base, which is not supplied. A cheap decisive
count at the polynomial level: quadratic tuples `(a,b,c,d)` form a `4*6=24`
dimensional space, degree-`<=8` polynomials a `45`-dimensional space, so the
discriminant map has constructible image of dimension `<= 24 < 45` and a
general degree-eight `Delta` is not the discriminant of *any* quadratic tuple.
That refutes the naive version outright. Whether some rank-three algebra can
have `deg Delta <= 8` with `d_min >= 3` is **OPEN** and is exactly the
realizability question in the next-test spec; I do not certify a counterexample
at that level and do not fill the gap by analogy.

## 5. Cheapest two strict-henselian controls (pre-AWS)

Both are hand-checkable over the strict henselization `R` of `C[u,v]` at the
origin; neither needs CAS. They form the positive/negative control pair the
campaign requires before any elimination sieve.

**SH-1 (separation control: discriminant vs different vs reduced branch vs
index).** `B = R[t]/(t^3-u)`. Expected exactly: `B` regular, hence normal, so
`D_idx = 0`; `Delta = -27u^2`, `ord_{(u)} Delta = 2`; different exponent `2`
(tame, `e=3`); reduced branch multiplicity `1`. Any pipeline that reports `1`,
`3`, or a nonzero index here has conflated two of the four objects of C3.
Slice `v=c` (transverse, disjoint from `div(det M)=0`): sliced `delta = 0`,
matching sliced index `0`.

**SH-2 (index/conductor and base-change control).** `Otilde = R x R x R`,
`B = R + u*Otilde`. Expected exactly: `Delta_Otilde` a unit; `M` similar to
`diag(1,u,u)` so `det M = u^2` and `Delta_B = unit * u^4`;
`D_idx = 2*[u=0]`; `Ann(Otilde/B) = (u)` of order `1` — so index `!=`
annihilator (C7). Positive slice `v=c`: transverse (not a component of
`div(det M)={u=0}`), `Tor_1 = 0`, sliced curve is the spatial triple point with
`delta = 2 =` sliced index, and it is **not** Gorenstein, so
`length(Otilde/c) != 2 delta` (C8). Negative slice `u=0`: contained in
`div(det M)`, `Tor_1 = ker(M mod u) != 0`, and the length count must be
reported as failing rather than as a number.

A sieve that cannot reproduce SH-1's `(2,2,1,0)` tuple and SH-2's
`(index 2, annihilator 1, positive slice 2, negative slice FAIL)` should not be
run at scale.

## 6. Bounded next-test specification

Exactly one bounded, decidable test, no block closure attached:

* **T-1 (realizability, settles the second shortcut).** Fix `deg Delta = 8`.
  Decide whether there exists a finite locally free generically separable
  rank-three `C[u,v]`-algebra with `deg Delta = 8` and `d_min >= 3`.
  Bounded form: over the `24`-dimensional space of quadratic tuples, compute
  the image of the discriminant map and test membership of a fixed explicit
  degree-eight `Delta_0` (e.g. one with irreducible support) — a single
  elimination on `24` unknowns with one degree-four target. Verdict values:
  `IN_IMAGE`, `NOT_IN_IMAGE`, `INCONCLUSIVE`. `NOT_IN_IMAGE` for a `Delta_0`
  realized by an actual algebra converts the second shortcut from
  non-sequitur to refuted-by-witness. This is heavy/uncertain and is therefore
  AWS-only, and it must be gated behind SH-1 and SH-2.

Deferred, not authorized here: the five-item stratification of §4 (support,
infinity multiplicities, index divisor, reduced ramification classes, resolved
dual graph). Item 3 of that list should be re-typed as "index (Fitting/length)
divisor" per C7 before use.

## 7. Nonclaims of this review

No quadratic or cubic block closure, no primitivity statement, no map claim, no
counterexample to any promoted result, no JC2 consequence. The `d_min` lower
bound of THM D-INV(iii) is a statement about presentations only and closes
nothing. No exit-price assertion is made. `jc2-lean` was not inspected,
listed, searched, built, modified, or controlled; no input, canonical file,
script, or dependency was edited; no heavy CAS or Singular was run.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19766`.
- Body SHA-256:
  `013af71756795a10bdb6435af5a6e790c0ee1ed9a6b99f6047af40f2a872b881`.
- Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.
