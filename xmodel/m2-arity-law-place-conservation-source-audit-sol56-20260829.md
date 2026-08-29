# M2 ARITY-LAW source audit: places, series, flags, and the safe defect floor

Date: 2026-08-29  
Producer: Sol 5.6 (Ultra), post-blind-round exact source audit  
Status: sealed producer report; no canonical promotion in this file

## 0. Verdict

The literal Opus Card-2 hypothesis is **REFUTED**:

> At an extra-direction vertex of multiplicity `m`, the selected exit-set
> physical flags exhaust exactly all `m` places.

There are two independent typing failures.

1. `m = mult(p_F,c*) = deg(p_(F*c*))` counts Puiseux **series** after passage
   to a suitable cover, not physical places of `Rbar_a \ R_a`.  A physical
   place may contribute several conjugate series.  Thus there need not be
   `m` physical places, even before asking how many flags there are.
2. The promoted MFE selected-witness set chooses one cv witness for each
   priced outgoing direction-orbit.  It expressly does **not** claim that
   every actual cv flag is selected.  If one outgoing direction branches
   farther out, places on an unchosen later branch can have a different cv
   flag from the chosen witness.

A nearby statement is, however, **CERTIFIED** and is the statement the td8
and td12 arguments actually need:

> For the **full actual exit set** below an up extra direction, every physical
> place through that direction has a unique same-ray cv flag.  Taking the set
> of all distinct such flags leaves no physical place without a carrier, but
> the map from places to flags can be many-to-one and `m` remains a series
> count.  Corollary 7.1 charges each distinct flag once, not each place and not
> each conjugate series.

With this correction:

- the reviewed td8 trunk lower bound `lambda >= 3` remains valid;
- the reviewed td12 B-charge `lambda = 8` remains valid;
- the state-packet phrase “a lone flag would carry all `2i` places” must read
  “the full exit set is a singleton; with `q=1`, neither physical-place
  divergence nor conjugate-series shedding occurs, so all `2i` series remain
  in the common prefix”; and
- the proposed general equality

  ```text
  Lambda(delta) = min(num(delta), 2 ceil(delta))
  ```

  does **not** follow from H1--H4 or from the reviewed exact-separation law.
  Integrality applies to `q*(tau_0-kbar)`, not to `q*delta`, where
  `delta=D/m-kbar`.  The safe general lower floor for the full actual exit set
  is instead

  ```text
  L_safe(delta) = delta          if delta is a positive integer,
                  ceil(2 delta)  if delta is nonintegral,
  ```

  and even this is only a lower bound; attainment is a separate theorem.

The overall binary verdict requested for `PLACE-CONSERVATION` / ARITY-LAW H1
is therefore **REFUTED AS STATED**.  The corrected full-exit coverage theorem
is certified, while MFE representative-witness exhaustiveness remains outside
the theorem and must not be inferred.

## 1. Custody and exact read set

Primary printed source:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

Closed blind-round packet and all four sealed lane reports:

```text
65afb334763023765f701ee9a2140087a47c6ae470877cee0a04b4f4651c0d8f
  xmodel/ideation-20260829T0820Z-state-packet.md
cc58a521b92955b8c1e423aacdf60a5b619ba5384c9e05781bafec1ed7647b8c
  xmodel/ideation-20260829T0820Z-fable5.md
ec454b2e958690f396bbd14e901afcb1b5faf9204907911d27b8ab1c972cd98a
  xmodel/ideation-20260829T0820Z-grok46.md
142d1e3dcd1305dda7397b5cd8f812080c2bf6d6eeb7106203fce9912777e451
  xmodel/ideation-20260829T0820Z-opus5.md
ad50d1ada197a3ad424f321707ea62105fafc74a650d8b55e34cc1130c2efa84
  xmodel/ideation-20260829T0820Z-sol56.md
```

Their body seals are respectively Fable `7c97c36...`, Grok `349dfed1...`,
Opus `17dacd75...`, and Sol `06933494...`.  Opus Card 2 is the target of this
audit; no blind report was opened before the round closed.

Reviewed exact-separation and route packets:

```text
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508
  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370
  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
3c2c9a7ed79cc6d05ec3ba7098c1dc89cabb3547791d777c4bf8971d1ae28e39
  xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md
d9db244079c521a2e3643c824b715adb4c934d843f9da18e9140c80d6758f012
  xmodel/m2-td8-trunk-exact-charge-r1-hostile-review-opus5-20260829.md
a5c342e49aaa0ede12b857ed7742c6474737becabab0dcf7a10fbdedb26a8978
  xmodel/m2-td8-trunk-exact-charge-r1-hostile-rereview-grok46-20260829.md
2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829
  xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md
3f214db8c12d022c2852dfadbbc268d105484343a8f6d4664765a08d3efcea03
  xmodel/m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md
```

The relevant producer/review body seals are exact-separation
`f1ae6c2b...` / `463a8f48...`, td8 trunk `688dbf41...` /
`51f3ed7c...` / `fdb2a6e...`, and td12 `b25217e9...` / `8ef16e10...`.

Exit-set and budget repairs:

```text
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad
  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
86b491adc6ba6b21fcec5a8722126d80f3666d8e3d9f2cdcf4568d408bbc83a8
  xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md
ac49c025e3e010d3ecaf3839adf51c40cb88b0088198ae1c5ab1198e07cc8004
  xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14
  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5259d77766cc8179f3d1248ee0c1320daf411f04758487d2e94e216bb
  xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
```

Only desk algebra and local source extraction were used.  No web, AWS, or
heavy computation was used; no canonical file was edited.

## 2. The three carrier types cannot be identified

Fix a fibre `f=a`, a vertex `F`, and a nonzero extra root `c*`.  Write

```text
G = F*c*,       m = mult(p_F,c*) = deg(p_G).
```

There are three different finite objects.

### 2.1 Physical places / ends

Statement 3.1 (printed p. 10) starts with a point
`P in Rbar_a \ R_a` and gives its local Puiseux expansion.  Definition 3.2
and Statement 3.2 (pp. 10--11) define contact between physical points and
choose one coherent series `Omega(P)` per point.  Definition 3.3 (p. 11)
then constructs

```text
T_a^* = ((Rbar_a \ R_a) x [0,infinity]) / ~,
(P,u) ~ (Q,u)  iff  u <= O(P,Q).
```

Thus a ray `I_P` is carried by a physical point/place.  Conjugate expansions
of one place do not create several physical rays.

### 2.2 Puiseux series on a suitable cover

Proposition 3.1(*) and (**) (printed p. 14) say that `deg(p_d)` and
`mult(p_d,c)` count Puiseux **series** with a prescribed truncation.  Its proof
passes to the smooth closure of `h(t^kappa,y)=0` and counts points there.  Those
cover-points are the conjugate series, not necessarily distinct physical
points of the original `Rbar_a`.  Statement 3.9(i) (p. 15) gives

```text
mult(p_F,c*) = deg(p_(F*c*)).
```

Therefore `m` is the number of series in the child prefix group.  In general

```text
m = sum_(physical P through G) (number of conjugate series of P in the group),
```

not the number of physical places through `G`.

The reviewed A-step conjugate regime is already an explicit campaign example:
two series belong to one physical place, the series degree drops `2 -> 1` at a
characteristic exponent, `kappa` jumps, and the physical ray/flag remains
single.  This alone refutes “`m` places.”

### 2.3 Physical flags

A flag is an equivalence class `I_P(u)`.  Several physical places can share a
flag if their contact is at least `u`; one physical place can carry several
conjugate series while contributing only its one ray.  Flags therefore count
neither physical places nor series.  Corollary 7.1 charges a set of distinct
cv flags once each.

The only generally valid cardinality relations are surjections/partitions,
not `#flags = #places = m`.

## 3. Exact source-backed coverage theorem

Assume the child `G` is in `T_a^up`.  Let

```text
P(G) = {physical P in Rbar_a \ R_a : G lies on I_P},
u_0(P) = the unique u with d_(I_P(u)) = 0,
E_all(F,c*) = {I_P(u_0(P)) : P in P(G)} as a set of distinct flags.
```

Then the following chain is literal or reviewed-source backed.

1. Statement 7.3 (printed p. 35) is universal in `P`: if some flag on
   `I_P` is up, there exists a `v` on that **same ray** with
   `I_P(v) in T_(a,cv)`.
2. Statement 3.13 (p. 16) gives exactly one zero of `d` on each physical ray.
   Hence the Statement-7.3 witness is `I_P(u_0(P))`, and each physical place
   in `P(G)` has exactly one cv carrier.
3. Definition 3.3 gives no remerging: if two places split at contact `s`,
   their flags are different at every height greater than `s`.
4. Corollary 7.1 (p. 38), in its reviewed actual-weight subset form, accepts
   any set of pairwise-distinct cv flags on the fibre:

   ```text
   td(f,g) >= 1 + sum_(H in S) kappa_H (pi(H)-1).
   ```

Consequently `E_all(F,c*)` covers every physical place through the up child.
It does not count a place more than once when several places share the same cv
flag, and it does not count conjugate series as flags.  “No physical place has
a cv carrier” is impossible here; “every physical place pays a separate
summand” is equally false.

### 3.1 Which repaired exit set is exhaustive?

The Section-9 repair, `2763d970...` Section 4.6, defines

```text
E_i = Y_lit(F_i) \ Y_lit(F_(i-1)),
lambda_i^exit = sum_(H in E_i) kappa_H(pi(H)-1).
```

Here `E_i` contains **all cv vertices** whose first separation from the pole
path occurs at `F_i`.  The `c*`-direction slice of this `E_i` contains
`E_all(F_i,c*)`, so it is exhaustive at flag level for that direction.

The MFE theorem is a different object.  It defines `D_F` as the set of priced
outgoing direction-orbits and chooses one witness `H(F,d)` for each `d`.  Its
charge is the lower-price sum

```text
lambda_F^exit = sum_(d in D_F) price(F,d),
```

not the sum of all descendant actual weights.  The producer says that one
witness is chosen per component, allows a stronger local theorem to include
several flags in one direction-component, and explicitly quarantines “a claim
that every actual cv flag is one of the selected witnesses” (MFE Sections 4
and 6).  The selected-orbit attachment repair proves attachment and
injectivity of the chosen witnesses, not exhaustiveness inside their later
subtrees.

Thus:

- `E_all` / the full Section-9 first-separation slice: **coverage certified**;
- the MFE representative-witness subset: **not exhaustive and never claimed
  to be**;
- exactly `m` physical places: **refuted by type**.

An allowed formal picture makes the second distinction concrete.  One local
direction `d` can contain physical rays `P,Q` which agree immediately after
`F`, split later while `d_f>0`, and acquire distinct flags `H_P,H_Q`.
Statement 7.3 permits choosing `H_P` as MFE's witness for `d`; it does not put
`H_Q` into that selected subset.  The full set `E_all` contains both.  MFE is
still valid because it claims only the price of one selected witness; a local
arity theorem may add `H_Q` separately.

## 4. Correct reconstruction of the td8 trunk use

For the reviewed equal-join trunk,

```text
m = 2i,       D = 17i,       kbar = 7,
delta = D/m-kbar = 17/2-7 = 3/2.
```

Take the full actual set `E_all`.  For every `H in E_all`, the reviewed exact
separation law gives

```text
tau_H >= D/m = 17/2,
q_H = kappa_H/kappa_F in N*,
w_H = q_H(tau_H-7) in N*.
```

Therefore every flag has `w_H >= ceil(3/2)=2`.  Now use the correct
ramification dichotomy.

1. If some `q_H >= 2`, then that flag alone has

   ```text
   w_H >= 2(17/2-7) = 3.
   ```

2. Otherwise all `q_H=1`.  If `E_all` were a singleton, full coverage says no
   two physical places diverge before its cv level.  The equality `q=1` says
   the ray has no new characteristic denominator and hence no conjugate-series
   shedding before that level.  Together these facts give
   `N(tau)=m=2i` throughout, so the area identity gives
   `tau_H=D/m=17/2`.  Then `w_H=3/2`, contradicting `w_H in N*`.  Hence there
   are at least two distinct flags, each of weight at least two, and their
   total is at least four.

Thus the full trunk exit weight is at least three.  The route budget remains

```text
2 + 2 + 3 + 1 = 8 > td-1 = 7.
```

No step asserts that there are `2i` physical places.  What remains together
in the forbidden singleton-`q=1` branch is the complete group of `2i`
**series**, because the two possible loss mechanisms have separately been
excluded: physical-place divergence by singleton full coverage, and conjugate
shedding by `q=1`.  This is exactly the repair in the Opus hostile review and
is independent of MFE representative-witness exhaustiveness.  The td8 route
kill therefore survives this audit unchanged.

## 5. Correct reconstruction of the td12 use

For the reviewed U1 B-direction,

```text
m = i,       D = 25i,       kbar = 17,
delta = D/m-kbar = 25-17 = 8.
```

For every `H in E_all`,

```text
tau_H >= 25,       q_H in N*,       w_H=q_H(tau_H-17) in N*,
```

so `w_H >= 8`.

- If a conjugate-series shedding occurs before the cv level, the relevant
  flag has `q_H>=2`, hence `w_H>=16`, and Corollary 7.1 gives
  `12>=1+16`, impossible.
- If physical places diverge before their cv levels into distinct actual
  flags, the full exit set contains at least two flags, each of weight at
  least eight, and Corollary 7.1 gives `12>=1+8+8`, impossible.

Thus the full actual exit set is a singleton with `q=1`, and neither loss
mechanism occurs before the cv level.  Hence `N(tau)=i`, the area identity
gives `tau_0=25`, and the unique actual weight is

```text
w = 1(25-17) = 8.
```

This proves exact charge eight and excludes nine.  Again there is no need for
`i` physical places: there may be fewer physical places, and several places
may share the unique flag, but all `i` series remain in the common prefix
through the cv level.  The td12 result survives with the Fable R1 case split
and does not consume the refuted literal H1.

## 6. Audit of the proposed closed form

Let

```text
delta = D/m-kbar > 0.
```

For each actual flag `H`, the exact law gives

```text
tau_H-kbar >= delta,
w_H = q_H(tau_H-kbar) in N*,       q_H in N*.
```

Opus's proposed single-flag term argues that if `delta=a/b` in lowest terms,
then integrality forces `b|q`, and so `w>=a=num(delta)`.  This inference is
invalid unless `tau_H=D/m`, or unless one separately proves
`q_H*delta in Z`.  In general a conjugate shedding makes
`tau_H>D/m`, and integrality of `q_H(tau_H-kbar)` says nothing about the
denominator of the smaller number `q_H*delta`.

### 6.1 Exact-law counterprofile

The failure is visible without a numerical cap.  Consider the following
formal prefix/area profile:

```text
m = 6,      D = 14,      kbar = 1,      delta = 14/6-1 = 4/3,
tau_0 = 5/2,       q = 2,

N(tau) = 6   for 0 < tau <= 13/6,
         3   for 13/6 < tau <= 5/2.
```

Then

```text
integral N d tau = 6(13/6) + 3(5/2-13/6) = 13+1 = 14 = D,
w = q(tau_0-kbar) = 2(5/2-1) = 3 in N*.
```

It has `tau_0>D/m`, `q=E_+/E_0=2/1`, and `E_+<=m`.  Declare the one flag to
carry every abstract physical carrier in the group.  Then all scalar
requirements actually stated in H1--H4, together with monotonicity and the
reviewed area identities, are satisfied, but

```text
min(num(4/3), 2 ceil(4/3)) = min(4,4) = 4 > w=3.
```

This is an **axiomatic** countermodel to the claimed deduction from H1--H4
plus the displayed exact-separation identities.  It is not claimed to come
from a compatible Puiseux characteristic sequence, still less from a
polynomial Keller pair.  A source congruence or characteristic-grid invariant
could exclude it, but that would be a new load-bearing hypothesis, precisely
what the proposed formula presently lacks.  Thus this profile refutes the
advertised derivation and leaves the stronger law itself unproved; it does not
claim an actual Sigray-tree counterexample.

### 6.2 Safe lower floor

For the full actual exit set, the strongest immediate universal floor from
the reviewed inputs is:

> **Safe-floor lemma.** If `delta>0`, then
>
> ```text
> total actual exit weight >= delta          when delta is integral,
>                            ceil(2 delta)  when delta is nonintegral.
> ```

Proof.  If there are at least two distinct flags, each integral weight is at
least `ceil(delta)`, so the total is at least `2ceil(delta)`.  If there is one
flag with `q>=2`, its integral weight is at least `ceil(2delta)`.  If there is
one flag with `q=1`, full coverage excludes physical-place divergence and
`q=1` excludes conjugate shedding, so `tau_0=D/m` and `w=delta`; this is
possible only when `delta` is integral.  For nonintegral `delta`, the first two
branches remain and
`ceil(2delta) <= 2ceil(delta)`.  For integral `delta`, the singleton `q=1`
branch gives the lower floor `delta`.  QED.

This lemma is a floor, not an equality.  To recover Opus's numerator branch as
a lower bound one needs, for every singleton `q>=2` branch, an added condition
such as

```text
tau_0 = D/m,             or directly             q*delta in Z.
```

The former permits a denominator jump exactly at the cv level but no earlier
area shedding; the latter is the exact divisibility premise Opus's arithmetic
silently assumes.  Even with it, equality of `Lambda` requires an attainment
theorem for one of the minimizing branches.

Calibration explains why the flaw was invisible:

```text
td8 trunk: delta=3/2, safe floor ceil(3)=3, proposed value 3;
td12 B:    delta=8,   safe floor 8,       proposed value 8;
td8 A:     delta=2,   safe floor 2,       proposed value 2.
```

All three reviewed values lie in cases where the safe floor and the proposed
formula coincide.  They do not validate the numerator term at general
rational defect.

## 7. Downstream scope and required wording repairs

1. **State packet.** At lines 45--52, replace “all `2i` places” by the
   two-mechanism series statement in Section 4 above.  The numerical route
   kill does not change.
2. **Opus Card 1.** Do not promote `ARITY-LAW` as an equality.  Carry the
   safe-floor lemma only for a full actual exit set, and keep attainment and
   any stronger numerator/divisibility law open.
3. **Opus Card 2 / H1.** Mark literal H1 `REFUTED`; replace it with
   `FULL-EXIT-COVERAGE`, which is certified by Statements 7.3 and 3.13 plus
   Definition 3.3.  Never write `m places` without a separate unramifiedness
   theorem.
4. **MFE.** No repair is needed.  Its selected witnesses are intentionally a
   lower-bound subset, and its own quarantine already forbids exhaustiveness.
   A consumer needing arity must explicitly upgrade from one representative
   witness to the full local actual flag set and prove that set's disjointness.
5. **td8 and td12.** Retain both reviewed conclusions.  Their repaired proofs
   use all actual flags directly through Corollary 7.1 and the ramification
   dichotomy; neither depends on `#places=m` or on MFE witness exhaustiveness.

## 8. Review risks and exclusions

A hostile reviewer should attack exactly these points:

1. Check that `mult(p_F,c*)` is a series count at Proposition-3.1 scope, not
   silently a count of physical ends in the original compactification.
2. Check the distinction between the full Section-9 set `E_i` and the MFE
   representative set `{H(F,d)}`; matching notation is not set equality.
3. Check that Statement 7.3 is applied to every physical ray through the same
   up child, and that Statement 3.13 supplies uniqueness only raywise, not
   injectivity across places.
4. Check the safe-floor singleton-`q=1` step: it needs **full** physical-place
   coverage.  It is not licensed for a one-witness MFE subset.
5. Try to find a reviewed source constraint coupling `q`, the complete step
   function `N`, and `delta` strongly enough to exclude the Section-6.1
   profile.  Without such a constraint, the numerator term is unavailable.
6. Do not upgrade a lower floor to an attained minimum.

Nothing here proves a degree ceiling, excludes td8 or td12 globally, lands a
formal cell, constructs a Keller pair or counterexample, or settles JC2.

*End of sealed report body.*

## Seal (outside the sealed body)

- Body length: `20836` bytes (the complete file before this seal heading,
  through the newline following `*End of sealed report body.*`).
- Body SHA-256:
  `1608a44660e094e0fa8cf05b4f1db3b97173243a9e8319a7f55d4c44f0f1cb85`.
