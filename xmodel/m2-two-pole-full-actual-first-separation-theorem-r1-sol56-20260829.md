# Two-pole full-actual first-separation theorem

**Date:** 2026-08-29  
**Producer:** Sol 5.6 Ultra  
**Stable basis:** `76c746f698103d20019bfeb72654a361ccc5371d`  
**Disposition:** **`PROVED_FULL_TWO_POLE_ATTACHMENT`**, provisional producer
result pending an independent hostile review.

## 0. Result and exact boundary

On one fixed fibre, Sigray's physical y-side Eggers--Wall object from
Definition 3.3 is a rooted prefix tree.  It is not a collection of raw
Puiseux representatives later subjected to an unidentified quotient.
Consequently, if `U` is the union of two pole paths, then:

1. `U` is rootward closed;
2. every flag outside `U` has a unique outermost attachment to `U`;
3. corrected Statement 3.18 identifies each effective nonzero root orbit of
   `p_F` with one actual microchild at `F` (and the zero orbit with the zero
   microchild);
4. for every actual up microchild outside `U`, **all** distinct actual cv
   flags below it attach at its base `F`; and
5. the full sets belonging to different directions or different attachment
   vertices are pairwise disjoint and may be inserted simultaneously, once
   each, into a single repaired Corollary-7.1 budget.

The prior selected-orbit repair proved this for one chosen Statement-7.3
witness in each priced direction.  The extension to the full actual set does
not need a new global quotient axiom: rootward closure immediately propagates
the attachment of the realized microchild to every one of its descendants.

This result is fixed-fibre and inequality-only.  It does **not** prove printed
`(22)`, `(22-cl)`, cross-fibre constancy of `kappa`, an equality or attainment
claim, realization of an LL-1 row, landing, or the plane Jacobian conjecture.

## 1. Frozen custody and source audit

All listed inputs were hashed before the proof write.  The after-write audit in
Section 8 reproduced the same hashes.

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
ded3051d1a2009498f49bed20e5168d34b823518ab1b94ed340b380b37da6d15  ladder/SIGRAY-AUDIT.md
758c022696da6dbafaf7c907af25d733162ece203cc6599a30a903de03c93840  xmodel/sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md
521080ae8ae2c667908f6cb220a62a732f422777a1bad662099598f33df34962  xmodel/sigray-section7-resolution-free-quotient-route-gpt55-20260828.md
37b83208ddebb6e1242d341294d98f96116bad431c05a33ab43eaa147044d47e  xmodel/sigray-cyclic-semi-invariance-repair-sol-ultra-20260828.md
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5259d77766cc8179f3d1248ee0c1320daf411f04758487d2e94e216bb  xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
05f68f4b7278a8ac1216ba82b40e7081bfff66f351380ccd671d12a955784d84  xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md
56e95db58e53aa030ef1100cc1640d115105a77607d40e3f160e77b46174a34d  xmodel/m2-arity-law-place-conservation-source-audit-hostile-review-fable5-20260829.md
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7  xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md
3e3cea4aa6e0bda907dd291a0f1e62e1ffa744e84463e5596c2e0e0e408a166b  xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b.md
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json
1ae50f7925de2d63a718b48ab892c78a3313e4a505b8faf7385853d591c58840  ladder/BOOK-OFFAXIS.md
93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md
d7d0038c5fd1a3522b2908a598d99c23c64e85ec81d1280f1c7ec686c6c8ab2f  ladder/SHEET6-2POLE.md
```

I independently re-extracted and read the primary source at printed pp.
10--18 (Definitions 3.1--3.4, Statements 3.2--3.18 and Notation 3.8), pp.
28--35 (Notation 6.1, Propositions 6.6--6.8, Statements 7.1--7.3), and p. 38
(Corollary 7.1).  The literal p. 18 conclusion of Statement 3.18 contains the
known unused-`epsilon` typo.  `ladder/SIGRAY-AUDIT.md:52` records and
re-derives the unique correction `F*(epsilon*c)`.  The fixed-fibre
`d_F`/Statement-3.13 uses below adopt the separately filed `d_(f-a),F`
correction at `ladder/SIGRAY-AUDIT.md:43-46`.

The overall-FAILED final delta gate is used for exactly one independently
checked PASSED clause: distinct effective root orbits give distinct actual
`F*c` directions, including the zero orbit.  Its failed cross-fibre
`kappa`-transport clause remains rejected and is not used here.

## 2. Physical flag tree

Fix one fibre `R_a` and work in its y-component.  Statement 3.2 supplies a
coherent choice `Omega(P)` of one formal series for every physical place
`P`, preserving the physical contact `O(P,Q)`.

### Lemma 2.1 (ultrametric contact)

For physical places `P,Q,R` in the y-component,

```text
O(P,R) >= min(O(P,Q), O(Q,R)).                              (2.1)
```

**Proof.**  For raw formal series, contact is the first exponent at which
coefficients differ.  If the first two series agree below height `s` and the
last two agree below height `t`, the first and last agree below
`min(s,t)`.  Apply this to `Omega(P),Omega(Q),Omega(R)` and use Statement
3.2(ii).  QED.

Definition 3.3 is therefore the well-posed common-prefix quotient

```text
T_a^* = ((Rbar_a \ R_a) x [0,infinity]) / ~,
(P,u) ~ (Q,u)  iff  u <= O(P,Q).                            (2.2)
```

Write `I_P(u)=[P,u]`.  For `H=I_P(v)`, define its rootward restriction

```text
rho_H(t)=I_P(t),                 0 <= t <= v.                (2.3)
```

If also `H=I_Q(v)`, then `v<=O(P,Q)`, hence
`I_P(t)=I_Q(t)` for every `t<=v`; (2.3) is representative-independent.
Moreover,

```text
I_P(t)=I_Q(t)  iff  t<=O(P,Q).                              (2.4)
```

Thus two rays that differ at one height differ at every greater height.  A
split never remerges.  The last common flag of `I_P(u)` and `I_Q(v)` is at
height `min(u,v,O(P,Q))`, and the two rootward segments from that flag are
unique.  This gives the usual rooted-tree structure directly, without any
extra quotient axiom.

The rational subtree `T_a=T_a^* intersect pi^(-1)(Q)` and the vertex-edge
subtree generated by `V_a` inherit these rootward restrictions.  Notations
3.3 and 3.8 only discretize parent edges and microchildren.  No later source
definition identifies two already-physical flags.

### Lemma 2.2 (pole union and unique attachment)

Let the two y-side pole flags be `Z_j=I_(P_j)(v_j)`, `j=1,2`, and set

```text
U^full = union_(j=1,2) I_(P_j)([0,v_j]).                    (2.5)
```

For any physical place `P`, its ray meets `U^full` at exactly

```text
A_P=[0,a(P)],
a(P)=max_(j=1,2) min(v_j,O(P,P_j)).                         (2.6)
```

Indeed, membership at height `t` means that for some `j`, both `t<=v_j`
and `t<=O(P,P_j)`.  Therefore `U^full` is connected and rootward closed.
If `H=I_P(w)` lies outside it, then `w>a(P)` and

```text
att_U(H)=I_P(a(P))                                          (2.7)
```

is the unique outer endpoint of its root-path intersection with `U^full`.
The endpoint is representative-independent by Lemma 2.1 and (2.3).  It is
a transition-tree vertex: the maximum in (2.6) is a pole endpoint or a
physical contact, hence lies in the vertex set from Definition 3.4.

This formula incorporates the endpoint repair from the hostile review of the
selected-orbit lemma.  At a pole endpoint one may have
`O(P,P_j)>v_j`; the relevant quantity is `min(v_j,O(P,P_j))=v_j`, not the
false universal assertion `O(P,P_j)=v_j`.

## 3. Root orbits are actual child components

Let `F=I_P(u)` be a vertex.  Choose a common suitable cover denominator
`K`, divisible enough that `Ku`, every pole height, every physical contact,
and every characteristic exponent is integral on the `1/K` grid.  Refining
a suitable denominator by a multiple preserves suitability.

Notation 3.8 defines an actual microchild

```text
G_c=F*c=I_P(u+1/K)                                         (3.1)
```

when a physical continuation has coefficient `c` at the current height.
The first clause of Statement 3.18 says that every realized `c` is a root of
`p_F`.  Statement 3.16 writes

```text
p_F(eta)=eta^ell * p_tilde(eta^(nu_F)),                    (3.2)
```

so its nonzero roots are unions of `mu_(nu_F)` orbits and zero is a fixed
singleton.  Corrected Statement 3.18 says that every nonzero root orbit has
one and only one realized coefficient `epsilon*c`, while a zero root realizes
`F*0`.  Conversely every actual microchild comes from such a root.  Hence:

```text
{effective root orbits of p_F}  <-->  {actual microchildren at F}. (3.3)
```

This is also the exact fixed-fibre quotient clause passed in the final delta
gate.  It can be checked directly: representatives chosen from two different
root orbits remain unequal after multiplication by their respective roots of
unity.  If their actual children at height `u+1/K` were equal, Definition
3.3 would make their coherent series agree at the coefficient of height `u`,
contradicting those unequal realized coefficients.

If two actual children `G_c,G_d` are distinct, their representative rays
share `F`, so their contact is at least `u`, but it is less than `u+1/K`.
All contacts lie on the chosen grid, hence their contact is exactly `u`.
By (2.4), their entire descendant components are disjoint.

Finally, suppose `F in U^full` and `G_c` is an outward microchild not in
`U^full`.  Formula (2.6) gives `a(P)>=u` because `F` lies in the union and
`a(P)<u+1/K` because `G_c` does not.  Grid integrality forces

```text
a(P)=u,       att_U(G_c)=F.                                (3.4)
```

This single calculation covers both interior vertices and pole endpoints;
it never asserts contact exactly `u` with a pole path that ends at `F`.

The abstract countermodel from the earlier MFE hostile review is therefore
not a model of the available source.  It starts with two distinct realized
microchildren and identifies cv descendants later.  Distinct microchildren
have contact exactly `u`, while later equality at height `w>u` would require
`w<=O(P,Q)=u` by Definition 3.3.  That is the precise violated axiom.

## 4. Full actual cv exits

At each `F in U^full`, exclude every rootward direction and every outward
microchild contained in `U^full`; the latter are pole-chain arrivals, including
all arrivals at a merge.  Let `d` be a remaining **actual up** direction,
represented by a realized microchild

```text
G_(F,d) notin U^full,       G_(F,d) in T_a^nearrow.          (4.1)
```

Here `T_a^nearrow` denotes the source's `T_a^%`: it is a subset of `T_a^+`.
The corrected local transition package and Propositions 6.7--6.8 establish
this typing for the priced non-chain directions used by MFE and the LL-1 P0
cells; a remaining searrow child follows its same physical branch to a pole
and is therefore an arrival in `U`, not a priced exit.

Let `P(G)` be the finite set of physical places whose rays contain `G`.  For
each `P in P(G)`, Statement 7.3 gives a cv flag on the same ray.  Corrected
Statement 3.13 (`d_(f-a)` reading) makes that flag unique; denote it

```text
H_P=I_P(u_0(P)) in T_(a,cv).
```

Define the **full actual exit set**, as a set of distinct physical flags,

```text
E_all(F,d)={H_P : P in P(G_(F,d))}.                         (4.2)
```

This is not a set of cover series, not a set of physical places, and not the
one-witness MFE representative subset.  The map `P -> H_P` may be many-to-one.

### Theorem 4.1 (full-actual attachment and disjointness)

For every pair `(F,d)` satisfying (4.1):

1. (4.2) is exactly the set of all distinct actual cv flags below that
   microchild;
2. every `H in E_all(F,d)` lies outside `U^full` and
   `att_U(H)=F`; and
3. the sets `E_all(F,d)` are pairwise disjoint as `(F,d)` varies over all
   such directions on the two-pole union.

**Proof.**  Since `G_(F,d)` is up, it has positive `d_(f-a)`.  Along a fixed
ray that decoration is monotone decreasing (Statement 3.10), while a cv flag
has `d_(f-a)=0`; hence the unique Statement-7.3 carrier `H_P` is strictly
farther out than `G_(F,d)`.  It is therefore a descendant of the actual
microchild.  Conversely, every cv flag below the child has a physical-place
representative `P` through the child and equals the unique `H_P`.  This proves
(1).

Equation (3.4) says the child's root path leaves `U^full` at `F`.  The child
and every descendant have the same root-path prefix through that child.
Because `U^full` is rootward closed, a descendant cannot re-enter it; its
outermost intersection with `U^full` is still `F`.  This proves (2).

For two different directions at the same `F`, Section 3 gives different
actual microchildren and disjoint descendant components.  For directions at
different `F,F'`, a common cv flag would have both `F` and `F'` as the unique
endpoint (2.7) of its root-path intersection with `U^full`, forcing `F=F'`;
the same-base argument then forces the directions equal.  This proves (3).
QED.

The proof works verbatim for any finite union of pole paths on one fixed
y-component.  The present disposition is deliberately named only at the
two-pole scope required by LL-1.

## 5. Single-budget consumer theorem

Put `wt(H)=kappa_H(pi(H)-1)`.  For any finite collection of actual up
non-chain directions satisfying (4.1), Theorem 4.1 makes

```text
S = disjoint_union_(F,d) E_all(F,d)
```

a set of pairwise-distinct flags in one `T_(a,cv)`.  The reviewed
actual-weight Corollary 7.1 may therefore be applied **once**:

```text
sum_(F,d) sum_(H in E_all(F,d)) wt(H) <= td(f,g)-1.          (5.1)
```

If the separately certified x-side flag has weight at least `psi`, Statement
3.3 puts it in the other component, so it is distinct from all flags in `S`.
The shared multipole form is

```text
sum_(F,d) sum_(H in E_all(F,d)) wt(H)
  <= td(f,g)-1-psi.                                         (5.2)
```

Common suffixes are subsets of one `U`, not duplicated path copies.  Merge
arrivals are removed before `(F,d)` is admitted.  Thus neither a shared
vertex nor a pole arrival is charged once per incoming pole path.

Machine-readable carrier declarations:

```text
consumer_tag={"carrier":"REPRESENTATIVE","coverage":"one-selected-Statement-7.3-witness","attachment":"selected-only","promotion":"LEGACY_FLOOR_ONLY"}
consumer_tag={"carrier":"FULL_ACTUAL_FIRST_SEPARATION","coverage":"all-distinct-cv-flags-below-actual-up-microchild","ambient":"Definition-3.3-physical-flag-tree","attachment":"unique-U-outer-endpoint","budget":"single-C7.1","promotion":"FULL_EXIT_FLOOR_LICENSED"}
```

`FULL_ACTUAL_FIRST_SEPARATION` is the precise stronger carrier required by
the stable LL-1 repricing review.  It is not an assertion that the generic
MFE representative set is exhaustive; MFE remains correctly typed as
`REPRESENTATIVE` unless a consumer explicitly substitutes the sets (4.2).

## 6. LL-1 application

The reviewed full-exit arity theorem applies to a nonzero actual up direction
of reduced series multiplicity `m`, with

```text
delta=X/m-kbar>0.
```

For its full carrier (4.2), the total actual weight has the safe lower floor

```text
L_safe(delta) = delta          if delta is a positive integer,
                ceil(2*delta)  if delta is nonintegral.     (6.1)
```

For nonintegral `delta`, the exhaustive proof split is: if the full set has
at least two distinct flags, two positive integral weights give the
`multi-flag` bound; if it is a singleton, `q=1` would force the exact
nonintegral weight `delta` and is impossible, so `q>=2` gives the other
bound.  This is a lower floor only.

The four LL-1 P0 cells isolated by the stable rereview have identical local
data:

| cell | `m` | `X` | `kbar` | `delta` | full nonzero floor | zero kept |
|---|---:|---:|---:|---:|---:|---:|
| `(17,5)@2` | 3 | 17 | 5 | `2/3` | 2 | 1 |
| `(51,15)@7` | 3 | 17 | 5 | `2/3` | 2 | 1 |
| `(85,25)@12` | 3 | 17 | 5 | `2/3` | 2 | 1 |
| `(119,35)@17` | 3 | 17 | 5 | `2/3` | 2 | 0 |

In each cell the multiplicity-3 nonzero root orbit is already locally typed
as an actual up, non-chain P0 direction.  Theorem 4.1 now supplies the missing
`FULL_ACTUAL_FIRST_SEPARATION` carrier and global disjointness license.  Thus
its nonzero floor is `ceil(4/3)=2`, rather than the one-representative floor
1.  The epsilon/zero summands remain separate and are not repriced.  No
attainment, exactness, realization, or landing conclusion is added.

The two exhaustive nonintegral branches are declared separately:

charge_basis={"delta":"2/3","branch":"q>=2","flag_count":1,"citation":"xmodel/m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829.md:Section 6"}

charge_basis={"delta":"2/3","branch":"multi-flag","flag_count":2,"citation":"xmodel/m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829.md:Section 6"}

## 7. Dependency graph and hypotheses

The proof uses the following directed dependency chain:

```text
Statement 3.2 + Definition 3.3
  -> physical prefix tree, no remerging, rootward-closed U
  -> unique attachment outside U

Statement 3.16 + corrected Statement 3.18 + Notation 3.8
  -> effective root orbit <-> actual microchild
  -> distinct off-U child components

actual up child + Statement 7.3 + corrected Statement 3.13
  -> unique same-ray cv carrier for every physical place through child
  -> full set E_all

rootward closure + child attachment
  -> every E_all member has same attachment
  -> pairwise disjoint full sets

reviewed actual-weight Corollary 7.1
  -> one simultaneous budget

reviewed full-exit arity floor
  -> LL-1 delta=2/3 full-set price 2.
```

Exact hypotheses are:

1. one fixed fibre and one physical y-component;
2. the corrected `d_(f-a)` reading of Notation/Statement 3.13;
3. the corrected `F*(epsilon*c)` reading of Statement 3.18;
4. a sufficiently divisible common suitable cover denominator;
5. only realized actual child directions, with each direction typed up;
6. pole-chain/rootward arrivals excluded before pricing;
7. `E_all` treated as a set of distinct flags, not places or cover series;
8. the reviewed actual-weight form of Corollary 7.1 and, for (5.2), the
   separate x-side witness of weight at least `psi`; and
9. the reviewed local full-exit arity inequalities for the numerical floor.

Not hypotheses and not conclusions: cross-fibre `kappa` transport, printed
`(22)` or `(22-cl)`, flag/place/series equality, an exact-level no-parting
claim, equality in (5.1), or existence of a curve attaining a floor.

The strong blocker was therefore a **perimeter omission**, not false
mathematics: the earlier hostile review did not have the subsequently
reviewed Definition-3.3 selected-attachment repair in its effective
perimeter and correctly failed closed.  Once that repair is combined with
the already reviewed full-exit coverage theorem, the full-set extension is
the one-line rootward-closure argument in Theorem 4.1.

## 8. Controls and after-custody

The complete 21-file read perimeter in Section 1 was rehashed after this
report body was written.  Every SHA-256 reproduced byte-for-byte, HEAD was
still `76c746f698103d20019bfeb72654a361ccc5371d`, and the basis checker
reported `charge_basis=VALID:2:2/3,2/3`.  Thus the proof consumed one stable
source basis.  The only repo artifacts created by this lane are this producer
report and the separately sealed blind Opus prompt/log/run/report packet.

Negative controls:

- Remove corrected Statement 3.18: root orbits need not be proved to realize
  distinct physical microchildren, so the result drops to
  `PROVED_PHYSICAL_TREE_PARTIAL_ORBIT_INTERFACE_OPEN`.
- Allow a child in `U`: formula (3.4) fails and the direction is a pole-chain
  arrival, not a full exit.
- Replace `E_all` by one MFE witness: Theorem 4.1 still separates the witness,
  but the nonintegral full-set floor is not licensed.
- Permit post-split remerging: this contradicts Definition 3.3 exactly as
  shown in Section 3.
- Move flags between fibres: the failed `kappa` transport gate becomes
  relevant; the present theorem says nothing.

No canonical, ladder, case, guardrail, or operations file was edited.  No
heavy CAS, AWS, web lookup, commit, or push was used.  This is a provisional
producer artifact and should be hostile-reviewed before canonical promotion.

<!-- END-SEALED-BODY::m2-two-pole-full-actual-first-separation-theorem-r1-sol56-20260829 -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first byte of this
file through and including the newline terminating the unique marker line
above.  This seal section is excluded.

- Sealed-body bytes: `21235`
- Sealed-body SHA-256:
  `0c808734cf2f0c98d085503e8d0aaf8e0ca645c34adfb925c757d0beb6223428`
