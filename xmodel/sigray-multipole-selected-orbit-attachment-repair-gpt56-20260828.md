# Sigray multipole: selected-orbit attachment repair

**Date:** 2026-08-28  
**Lane:** source-level repair for the ambient attachment blocker in the frozen
`sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md`  
**Result:** **PROVED, at the selected-exit/shared-inequality scope only.**

This supplies the one missing ambient-tree justification from the hostile
review. It does not reprove local prices or the actual-weight Euler theorem.

## 0. Exact scope and custody

Frozen multipole producer:

```text
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
```

Read inputs:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
37b83208ddebb6e1242d341294d98f96116bad431c05a33ab43eaa147044d47e  xmodel/sigray-cyclic-semi-invariance-repair-sol-ultra-20260828.md
521080ae8ae2c667908f6cb220a62a732f422777a1bad662099598f33df34962  xmodel/sigray-section7-resolution-free-quotient-route-gpt55-20260828.md
758c022696da6dbafaf7c907af25d733162ece203cc6599a30a903de03c93840  xmodel/sigray-section7-resolution-free-coordinator-final-delta-gate-terra-20260828.md
c3d6ff9239fb136cc35b815de6e229755f7d27b640481e7751d03d63291d1ebd  xmodel/sigray-prop67-prop68-source-audit-sol-ultra-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
062c92baea9ad7ad386f65fd7ef7dd820dd4b974c5e389580f8bdbf42a89aa0e  ladder/SHEET6-AF2.md
```

There is no standalone Eggers--Wall source PDF in `refs/`; the direct,
controlling construction is Sigray Definition 3.3. The primary source was
read through Definitions/Notations/Statements 3.1--3.18 (printed pp. 10--18),
the Section 6 orientation material (pp. 28--34), and Statements 7.1--7.3
(p. 35).

This report does **not** revive printed `(22)`, literal `delta_a`, `(22-cl)`,
cross-fibre constancy of `kappa`, equality/slack conclusions, or MP8's
no-refinement claim. The final delta gate's cross-fibre `kappa` failure
remains in force.

## 1. Correct quotient model

The literal premise that flag equality has no identifications beyond a cyclic
orbit is false. Definition 3.3 intentionally identifies different ends that
have a common Puiseux prefix:

```text
(P,t) ~ (Q,t)  <=>  t <= O(P,Q).                          (1.1)
```

`O` is Definition 3.2 contact; Statement 3.2 gives a coherent formal-series
presentation of that contact. Thus `T_a^*` is already the common-prefix
quotient, not a later quotient solely by a cyclic stabilizer. In particular,
for distinct ends,

```text
I_P(t)=I_Q(t)  <=>  t <= O(P,Q).                          (1.2)
```

Two rays agree through their contact and are unequal at every greater height.
A split therefore cannot remerge. This is direct from Definition 3.3.

The cyclic group has a distinct local job. At a flag `F`, roots in one
effective cyclic orbit describe one geometric outgoing direction. Corrected
Statement 3.18 selects the unique root-of-unity adjustment which gives the
actual child `F*(epsilon c)` (and fixes the zero orbit). The final delta gate
passes, at arbitrary rational height, the bridge that distinct effective
orbits have distinct next truncated directions. That is the only cyclic
quotient assertion used here.

## 2. Ambient prefix and pole-subtree facts

For `H=I_P(v)`, define its rootward segment by

```text
rho_H(t)=I_P(t),   0<=t<=v.                               (2.1)
```

If `H=I_Q(v)`, (1.2) implies `I_P(t)=I_Q(t)` for every `t<=v`; hence this
segment is representative-independent. This is the ambient, interval-level
form of the rootward-parent fact in Notation 3.3, not just a statement about
the induced vertex graph.

Represent each y-side pole flag by `I_(P_j)(v_j)` and set

```text
U^full = union_j I_(P_j)([0,v_j]).                        (2.2)
```

The definition is representative-independent by (2.1), and its vertex-edge
realization is the producer's `U`. For any end `P`, let

```text
A_P={t : I_P(t) belongs to U^full}.
```

This set is rootward closed. Indeed, if `I_P(t)=I_Q(t)` for a pole
representative `Q`, then (1.2) also gives equality at every smaller height.
Thus a ray cannot leave `U^full` and later re-enter it. This proves the
needed ambient assertion in the actual contact quotient.

Notation 3.8 and Statements 3.5--3.6 give the compatible grid-step
presentation, while Notation 3.3 gives the next rootward vertex. They are
not being asked to prove the stronger interval statement above.

## 3. Minimal selected-exit lemma

An actual outgoing direction `d` at `F=I_P(u) in U^full` is a **selected
exit** if it is one of the distinct cyclic direction-orbits chosen by the
local pricing rule and is neither a pole-chain arrival nor the rootward
continuation in `U`. Equivalently, its realized Statement-3.18 one-step
child is not on a pole path. This is exactly the frozen producer's class-3
selection; it removes merge arrivals before pricing.

### Lemma 3.1 (attachment and no remerging for selected exits)

Let `d` be a selected exit at `F=I_P(u)`. Assume its local transition proof
certifies it as positive/nearrow, and let Statement 7.3 give

```text
H(P,d)=I_P(v) in T_(a,cv).                                (3.1)
```

Then:

1. `H(P,d)` is outside `U^full`, with unique attachment `F`.
2. Distinct selected cyclic direction-orbits at the same `F` have distinct
   cv witnesses.
3. Selected exits based at different flags of `U^full` have distinct cv
   witnesses.

**Proof.** A locally priced flag is in `T_a^searrow`, so `u<1` by the
Section 6 definition. Statement 7.1 gives `v>1`; hence `v>u`. Statement 7.3
has supplied the witness on the very same ray `P`, not merely somewhere in
the fibre.

Fix a pole representative `Q` whose ray contains `F`. Since `d` is not a
pole-arrival direction, `O(P,Q)>u` is impossible: with a sufficiently
divisible common denominator, agreement above `u` gives the same coefficient
at height `u`, hence the same corrected-3.18 child and actual direction.
That would make `d` the pole-path direction. Since `I_P(u)=I_Q(u)`, (1.2)
therefore yields

```text
O(P,Q)=u.                                                 (3.2)
```

By (1.2), `I_P(t)` is not on that pole ray for any `t>u`. This holds for
every pole representative, so `A_P=[0,u]`; in particular `H(P,d)` lies
outside `U^full` and its rootward segment meets `U^full` exactly through
`F`. This proves (1).

For two different effective coefficient orbits at the same `F`, corrected
Statement 3.18 supplies different actual next coefficients. The two rays
agree below `u` because they realize `F` and differ at height `u`; by
Definition 3.2 and Statement 3.2 their contact is exactly `u`. This is also
the AF2 Section 2 R4 conclusion. Equation (1.2) now prevents equality at a
height greater than `u`, whereas both witnesses have height greater than
`u`. This proves (2).

If one flag `H` were a witness for exits based at `F` and `F'`, its
representative-independent segment (2.1) would have a rootward-closed
intersection with `U^full`. The first construction makes the outer endpoint
of that intersection `F`; the second makes it `F'`. Hence `F=F'`, and (2)
then forces the two direction-orbits to be equal. This proves (3). QED.

The lemma is intentionally minimal. It proves neither an arbitrary quotient
claim nor a cross-fibre transport theorem.

## 4. Consequence for MFE only

Repaired Propositions 6.7--6.8 supply the producer's remaining premise: a
remaining searrow microstep follows the same branch to a pole, so it is a
pole-chain arrival. Thus every locally priced remaining direction is a
positive selected exit. The local Section 9/AF2 package supplies

```text
kappa_H*(pi(H)-1) >= price(F,d).                          (4.1)
```

Lemma 3.1 makes the witnesses over all vertices of `U` pairwise distinct and
shows that a merge arrival has no selected witness. Consequently a merge
price is consolidated once per actual exit orbit, never once per incoming
pole path.

The actual-weight repair proves `(C7.1*)` for every pairwise-distinct set of
cv flags in one prescribed fibre. Add the separately certified x-side witness
once. Statement 3.3 puts it in the other component, hence it is distinct
from all y-side witnesses; its stipulated weight is at least `psi`. Applying
`(C7.1*)` once gives

```text
sum_(F in U) lambda_F^exit <= td(f,g)-1-psi.
```

Thus the frozen producer's MFE inequality is validated after its Section 2
ambient paragraph is replaced by Lemma 3.1 and definition (2.2).

## 5. Boundaries for the hostile gate

Closed here:

- every flag has a representative-independent rootward segment;
- a selected off-`U` direction cannot reattach or remerge with `U`;
- different selected cyclic direction-orbits cannot share a cv witness;
- merge arrivals are excluded before local pricing; and
- all selected y witnesses plus the one x witness fit in the prescribed-fibre
  actual-weight inequality.

Still inputs, not conclusions of this lemma:

- repaired Propositions 6.7--6.8 for same-branch pole arrival of a searrow
  direction;
- corrected Statement 3.18 and the passed unweighted quotient bridge for
  cyclic-orbit-to-actual-direction conversion;
- local Section 9/AF2 price (4.1); and
- actual-weight `(C7.1*)`.

The artificial double-count/remerging diagram from the prior hostile review
cannot occur in `T_a^*`: it requires `I_P(t)=I_Q(t)` at some
`t>O(P,Q)`, contrary to Definition 3.3. This has no bearing on failed
`(22)`/`(22-cl)` equalities or on the final delta gate's `kappa` counterexample.

**Disposition for a different-model gate:** the precise ambient attachment
blocker is repaired. The consumer must use `U^full` (or its vertex-edge
realization) and price exactly the selected exit-orbits, once each. Any
per-incoming-edge price, equality upgrade, or fixed-`kappa` transport remains
outside this result and must fail closed.
