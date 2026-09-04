# H1 NONRES census and ladder-row audit

Status: **COMPLETE for the bounded census and exact row probes; the proposed
uniform arithmetic kill is refuted.**

## 0. Decision

The three questions have different answers and must not be collapsed.

| question | decision |
|---|---|
| Is `NONRES(S)` true throughout the requested 166-group cohort? | **No: option (b).** It is true on 124 groups and false on 42. |
| Does the displayed numerical ladder law transfer from `(99,66)`? | **No.** It agrees there because of the accidental identity `N=u_s d_2`, and already fails at `D=108` and `D=126`. |
| Does a nonzero ladder coefficient generate the unit ideal? | **No.** It is at most a pivot-availability condition. A homogeneous row `cL=0`, `c != 0`, eliminates `L`; it is not the constant `c` in the ideal. |

On the task's conditional 274 `(skeleton,delta)` screen, `NONRES` is true on
192 and false on 82, so its arithmetic pass fraction is

```text
192/274 = 96/137 = 70.0729927007...%.
```

The theorem-grade number killed **by this predicate alone** is nevertheless
`0/274`: the missing inhomogeneous/augmented row is what makes an ideal a unit
ideal. The already banked `(99,66)` units `6264` and `64` remain valid, but both
use branch-specific pole data in addition to the Jacobian ladder. Thus the
literal proposed mechanism is **`(99,66)`-specific**, while the corrected
congruence is only a necessary condition for using this particular pivot, not
a sufficient condition for chart death and not a necessary condition for
death by another row family.

## 1. Custody and the exact meaning of “the 166 groups”

### 1.1 Frozen charged inputs

Before enumeration, I mechanically generated a check manifest from the lane
receipt rather than transcribing any digest. The command pattern was

```bash
awk -F= -v dir=/tmp/jc2-lane.7wKvYN/inputs '
  /charged_input_[0-9]+_sha256=/  { split($1,a,"_"); h[a[3]]=$2 }
  /charged_input_[0-9]+_basename=/ { split($1,a,"_"); b[a[3]]=$2 }
  END { for (i=1;i<=8;i++) print h[i] "  " dir "/" b[i] }
' xmodel/h1-nonres-census-sol56-20260903.run.v2 > MANIFEST
sha256sum -c MANIFEST
```

All eight entries returned `OK`. The receipt basis is
`e4e0d0eb88d22c50fa3d90bd90936fd7726e1bb1`. The same mechanical check was
rerun before sealing this report.

### 1.2 Raw Moh census versus the requested sharpened cohort

There is an important provenance correction to the wording of the task.
Running the frozen `moh_skeleton_full.py` directly does **not** yield 166
groups. Its `census(D,Kmin=16,full=True)` implements conditions (1)--(13); the
definition and recursion are at `moh_skeleton_full.py:69-135,147-215`. I ran it
for `48 <= D <= 200`. There can be no row below 48 because `Kmin=16` and the
enumerator requires `D/K >= 3`, so this is the entire `D <= 200` range under
that convention. It produces:

| layer | row assignments | groups | NONRES true/false |
|---|---:|---:|---:|
| raw frozen `(1)-(13)` census | 23,720 | — | — |
| raw with `u_s >= 2` | 6,117 | 4,012 | rows `4,389/1,728`; groups `2,896/1,116` |
| upstream POLY/ODE `u_s >= 2` screen | 310 | 177 | groups `129/48` |
| requested sharpened candidate cohort | **296** | **166** | rows `204/92`; groups **`124/42`** |

The requested 166 are obtained by importing the auxiliary workspace snapshot
`box/xufloor-20260903/results.json` and selecting

```text
record.phase == "us_gt_1" and record.xu_ok_candidate.
```

That snapshot has SHA-256
`68fca166c02217e35cfc9299f95b71a56e623ed1e7076594d807e6f047ed61f5`
and 1,304,597 bytes. It is **not one of this lane's eight charged inputs**, and
its own policy labels the `u_s>1` floor `candidate_under_proof_audit`. Hence the
166-group result is a reproducible audit of the requested sharpened cohort,
not a newly sourced promotion of that cohort. Every one of its 296 row records
was matched to exactly one row regenerated from the frozen Moh enumerator, and
`windows_ok()` and `full_ok()` were rechecked.

A row assignment retains all `V_2,...,V_s`. A group has key

```text
(D, m, (M_2,...,M_s), V_s),
```

so lower `V_i` assignments are merged. Here
`u_s=d_s-V_s` and `v_s=V_s`; the driver's `Skel.u` is a different integration
quantity and was not used. The 166 group distribution is

```text
u_s=2: 136,   u_s=3: 23,   u_s=4: 5,   u_s=5: 2.
```

### 1.3 What the 274 pairs count

For each group I enumerated each reduced rational

```text
delta=a/b,       1 < delta < v_s/u_s,       1 <= b <= u_s,
```

once. The resulting group/order count is exactly 274; lower `V_i` row
assignments do not multiply it. Of the 166 groups, 91 have at least one such
order and 75 have none. All 75 empty-order cells happen to satisfy `NONRES`, so
among groups that actually contribute pairs the group split is `49 true / 42
false`.

This count is conditional. The bound `den(delta) <= u_s` is explicitly a
charged gap: Xu uses it but neither proves nor cites it
(`ideation-20260904T1200Z-opus5.md:368-394`). Therefore 274 is a finite
candidate screen, not a sourced exhaustive census of all physical split
orders.

Nor does `u_s>=2` alone assert a genuine split. A genuine split requires a
multiplicity partition with at least two distinct-root packets, not the
one-part partition `[u_s]` (`minor-empty-disc-sol56-20260903.md:103-121`). The
enumeration here is skeleton/order arithmetic and does not silently identify a
skeleton, physical place, cover series, or multiplicity stratum.

## 2. Arithmetic predicate

Put `d=d_s=u_s+v_s` and `g=gcd(u_s,v_s)=gcd(u_s,d)`. Then

```text
d | u_s j
iff (d/g) | (u_s/g)j
iff (d/g) | j,
```

because `gcd(u_s/g,d/g)=1`. Thus some `j` in `1 <= j <= v_s` is resonant if
and only if `d/g <= v_s`. Negating and using `d=u_s+v_s` gives the promised
equivalence:

```text
NONRES(S)
iff d_s does not divide u_s j for every 1 <= j <= v_s
iff d_s/g > v_s
iff u_s > (g-1)v_s.
```

Both definitions were evaluated independently and asserted equal for every
row and group.

### 2.1 Complete cell table for the 166-group cohort

`pairs` is the number of group/order pairs, not row-assignment/order pairs.

| `u_s` | `v_s` | `d_s` | `g` | NONRES | groups | rows | pairs | reduced strict orders |
|---:|---:|---:|---:|:---:|---:|---:|---:|---|
| 2 | 3 | 5 | 1 | T | 73 | 136 | 0 | — |
| 2 | 4 | 6 | 2 | F | 30 | 72 | 30 | `3/2` |
| 2 | 5 | 7 | 1 | T | 15 | 19 | 30 | `3/2,2` |
| 2 | 6 | 8 | 2 | F | 7 | 12 | 21 | `3/2,2,5/2` |
| 2 | 7 | 9 | 1 | T | 6 | 7 | 24 | `3/2,2,5/2,3` |
| 2 | 8 | 10 | 2 | F | 3 | 6 | 15 | `3/2,2,5/2,3,7/2` |
| 2 | 9 | 11 | 1 | T | 2 | 4 | 12 | `3/2,2,5/2,3,7/2,4` |
| 3 | 4 | 7 | 1 | T | 2 | 5 | 0 | — |
| 3 | 5 | 8 | 1 | T | 11 | 15 | 22 | `4/3,3/2` |
| 3 | 7 | 10 | 1 | T | 5 | 6 | 20 | `4/3,3/2,5/3,2` |
| 3 | 8 | 11 | 1 | T | 3 | 3 | 18 | `4/3,3/2,5/3,2,7/3,5/2` |
| 3 | 9 | 12 | 3 | F | 1 | 1 | 7 | `4/3,3/2,5/3,2,7/3,5/2,8/3` |
| 3 | 11 | 14 | 1 | T | 1 | 1 | 10 | `4/3,3/2,5/3,2,7/3,5/2,8/3,3,10/3,7/2` |
| 4 | 7 | 11 | 1 | T | 2 | 3 | 8 | `5/4,4/3,3/2,5/3` |
| 4 | 11 | 15 | 1 | T | 3 | 4 | 30 | `5/4,4/3,3/2,5/3,7/4,2,9/4,7/3,5/2,8/3` |
| 5 | 10 | 15 | 5 | F | 1 | 1 | 9 | `6/5,5/4,4/3,7/5,3/2,8/5,5/3,7/4,9/5` |
| 5 | 14 | 19 | 1 | T | 1 | 1 | 18 | `6/5,5/4,4/3,7/5,3/2,8/5,5/3,7/4,9/5,2,11/5,9/4,7/3,12/5,5/2,13/5,8/3,11/4` |

The five false arithmetic cells are `(u_s,v_s)=(2,4),(2,6),(2,8),(3,9),
(5,10)`. Their resonant stages are respectively `j=3`, `j=4`, `j=5`,
`j=4,8`, and `j=3,6,9`. By degree the 42 false groups are concentrated as

| `D` | false groups | false row assignments | false pairs |
|---:|---:|---:|---:|
| 144 | 8 | 17 | 8 |
| 180 | 11 | 19 | 33 |
| 192 | 22 | 54 | 36 |
| 200 | 1 | 2 | 5 |
| **total** | **42** | **92** | **82** |

## 3. Exact false-group list

The complete key list follows. `r` counts lower-`V_i` row assignments and
`#delta` counts candidate strict orders. Resonant stages and the orders are
recoverable without ambiguity from the cell table; the full columns are also
serialized in `box/h1nonres-20260903/false-groups.tsv` and all 92 underlying
rows in `false-rows.tsv`.

| # | D | m | `(M_2,...,M_s)` | `(u_s,v_s)` | r | #delta |
|---:|---:|---:|---|:---:|---:|---:|
| 1 | 144 | 96 | `-72,84,102,142` | (2,4) | 3 | 1 |
| 2 | 144 | 96 | `-72,84,126,142` | (2,4) | 3 | 1 |
| 3 | 144 | 96 | `-72,84,138,142` | (2,4) | 2 | 1 |
| 4 | 144 | 96 | `72,84,102,142` | (2,4) | 3 | 1 |
| 5 | 144 | 96 | `72,84,138,142` | (2,4) | 3 | 1 |
| 6 | 144 | 96 | `120,138,142` | (2,4) | 1 | 1 |
| 7 | 144 | 108 | `132,138,142` | (2,4) | 1 | 1 |
| 8 | 144 | 120 | `132,138,142` | (2,4) | 1 | 1 |
| 9 | 180 | 72 | `126,174,178` | (2,4) | 1 | 1 |
| 10 | 180 | 108 | `126,168,178` | (2,4) | 1 | 1 |
| 11 | 180 | 120 | `-84,126,178` | (2,4) | 3 | 1 |
| 12 | 180 | 120 | `-80,150,178` | (2,8) | 2 | 5 |
| 13 | 180 | 120 | `-24,138,178` | (2,4) | 2 | 1 |
| 14 | 180 | 120 | `36,150,178` | (2,4) | 2 | 1 |
| 15 | 180 | 120 | `96,162,178` | (2,4) | 3 | 1 |
| 16 | 180 | 120 | `100,170,178` | (2,8) | 2 | 5 |
| 17 | 180 | 120 | `150,165,178` | (5,10) | 1 | 9 |
| 18 | 180 | 120 | `168,174,178` | (2,4) | 1 | 1 |
| 19 | 180 | 120 | `168,178` | (3,9) | 1 | 7 |
| 20 | 192 | 128 | `-32,144,184,190` | (2,6) | 3 | 3 |
| 21 | 192 | 128 | `32,144,168,190` | (2,6) | 2 | 3 |
| 22 | 192 | 128 | `32,144,184,190` | (2,6) | 2 | 3 |
| 23 | 192 | 128 | `32,168,190` | (2,6) | 1 | 3 |
| 24 | 192 | 128 | `96,144,184,190` | (2,6) | 2 | 3 |
| 25 | 192 | 128 | `144,184,190` | (2,6) | 1 | 3 |
| 26 | 192 | 128 | `160,176,184,190` | (2,6) | 1 | 3 |
| 27 | 192 | 144 | `-120,-12,18,190` | (2,4) | 5 | 1 |
| 28 | 192 | 144 | `-72,-12,42,190` | (2,4) | 1 | 1 |
| 29 | 192 | 144 | `-72,-12,150,190` | (2,4) | 1 | 1 |
| 30 | 192 | 144 | `-72,12,78,190` | (2,4) | 6 | 1 |
| 31 | 192 | 144 | `-72,12,114,190` | (2,4) | 2 | 1 |
| 32 | 192 | 144 | `-72,108,174,190` | (2,4) | 3 | 1 |
| 33 | 192 | 144 | `-24,-12,42,190` | (2,4) | 1 | 1 |
| 34 | 192 | 144 | `-24,-12,150,190` | (2,4) | 1 | 1 |
| 35 | 192 | 144 | `-24,132,150,190` | (2,4) | 4 | 1 |
| 36 | 192 | 144 | `-24,132,174,190` | (2,4) | 5 | 1 |
| 37 | 192 | 144 | `-24,132,186,190` | (2,4) | 3 | 1 |
| 38 | 192 | 144 | `24,60,186,190` | (2,4) | 1 | 1 |
| 39 | 192 | 144 | `72,108,138,190` | (2,4) | 3 | 1 |
| 40 | 192 | 144 | `72,108,174,190` | (2,4) | 3 | 1 |
| 41 | 192 | 144 | `120,132,150,190` | (2,4) | 3 | 1 |
| 42 | 200 | 120 | `20,150,198` | (2,8) | 2 | 5 |

## 4. What the ladder formula actually is

To remove the source's overloaded `n`, write:

```text
N = global degree,       K=d_2,       e=N/K,       f=m/K,
p = Jacobian band/stage, i=k-k_0,
in(K_2)=w^A(w-1)^B,
A=u_s K/d_s,             B=v_s K/d_s, A+B=K.
```

Take `KF=A0^e` and the `t^p` contribution
`KG=A0^f+t^p Q A0^(f-1)`, where `A0=w^A(w-1)^B` and
`Q=(w-1)^q`. Direct differentiation of the transported Jacobian gives the
factored `B_1` contribution

```text
e w^k0 (w-1)^[B(e+f-1)+q-1]
  * [K(q-K+p)w + A(K-p)],
k0=A(e+f-1)-1.
```

The driver checks this factorization directly from
`N*A0*Q' - e(K-p)Q*A0'`, for every ambient `B_1` coordinate in each tested
band. Consequently the lowest-row coefficient is exactly

```text
|c(p,k0)| = eA(K-p)
           = (N/d_s) u_s(d_2-p).                 (1)
```

This is the transferable raw calculation. The charged general discussion
derives the same lowest-row law and warns that the higher reduced ladder uses
the special `(99,66)` support cuts
(`minor-empty-disc-sol56-20260903.md:530-578`; see also
`minor-residue-formula-opus5-20260903.md:93-124`). If that same triangular
reduction pattern is available, its corrected candidate extension is

```text
|c(p,i)| = (N/d_s)[u_s(d_2-p)-d_s i].             (2)
```

The formula in the question is instead

```text
(N/d_s)[N-u_s p-d_s i].                           (3)
```

Equations (2) and (3) agree exactly when `N=u_s d_2`, equivalently `e=u_s`.
That identity holds at `(99,66)` but is not a skeleton identity.

There is a useful narrow survival: since `d_s | d_2`, a zero of the corrected
candidate (2) still forces

```text
d_s | u_s(d_2-p)  iff  d_s | u_s p.
```

Thus `NONRES` remains a congruence screen for possible zero pivots **if** the
same row exists and the same support reduction reaches it. It does not repair
the false numerical transfer, source the row in every chart, or produce an
inhomogeneous right-hand side.

## 5. Exact controls

### 5.1 Banked `(99,66)` ledgers

Here

```text
(d_1,d_2,d_s,d_{s+1})=(99,33,11,1),
(u_s,v_s,g)=(3,8,1), e=3, A=9, B=24, k0=35.
```

Thus `N=u_s d_2=99`, and all three forms coincide. Reading the two banked pivot
ledgers and checking every entry gives:

| branch | ledger pivots | Jacobian pivots matching `9(99-3p-11i)` | other pivots | minimum absolute J pivot |
|---|---:|---:|---|---:|
| `delta=5/2` | 66 | **66/66** | none | 9 |
| `delta=2` | 35 | **31/31** | four `G`-pole pivots `8,-8,8,8` | 18 |

This reproduces the charged closed-form audit
(`g9966-chart-necessity-opus5-20260903.md:632-676`). It also locates the two
actual constants:

* At `delta=2`, the stage-4, `i=0` Jacobian row is `-783` times one alternating
  `B_1` functional. The branch-specific pole row sets that same functional to
  `-1` with factor `-8`, leaving `(-8)(-783)=6264`; the exact derivation is at
  `minor-residue-formula-opus5-20260903.md:126-142`.
* At `delta=5/2`, `64` is the normal form of the terminal pole row after the
  66 pivots, not a raw ladder coefficient
  (`minor-residue-formula-opus5-20260903.md:145-156`). Equivalently, the
  43-by-43 `B_1` block and its pole functional have Schur residue 64
  (`two-place-obstruction-core-sol56-20260903.md:367-408`).

The ladder nonvanishing is real pivot arithmetic in these two compiled charts;
the **kill** comes from the extra affine pole/Schur row.

### 5.2 `D=108`

The census skeleton is

```text
(N,m,M_2,M_3;V_2,V_3)=(108,72,81,106;7,7),
(d_1,d_2,d_s,d_{s+1})=(108,36,9,1),
(u_s,v_s,g)=(2,7,1), e=3, A=8, B=28, k0=31.
```

Equation (1) gives, for `p=1,...,7`,

```text
12(72-2p) = 840,816,792,768,744,720,696.
```

The prompt's formula gives instead

```text
12(108-2p) = 1272,1248,1224,1200,1176,1152,1128,
```

a fixed discrepancy of 432. More decisively, the actual `D=108` chart dies on
the common-`h_3` incidence page. Its seven rational pivots have coefficients

```text
-1, 1, 1, -1, 1, -1, 1,
```

and its five residual rows are

```text
-jet2^2,
 2 jet1^2 jet2,
-2 jet2,
-c-jet1^4+9 jet1 jet2^2,
 2 jet1^2.
```

Those are not Jacobian-ladder residues. The exact localized identity uses
incidence rows `r80,r81` and `Zc*c-1`, and no pole or Jacobian row
(`two-place-obstruction-core-sol56-20260903.md:430-534`). Therefore the same
closed form neither reproduces the raw `B_1` numbers nor the incidence kill.

### 5.3 Independent `D=126` control

The third exact census match is

```text
(N,m,M_2,M_3,M_4;V_2,V_3,V_4)
  =(126,84,-14,63,124;1,10,5),
(d_1,...,d_{s+1})=(126,42,14,7,1),
(d_s,u_s,v_s,g)=(7,2,5,1), e=3, A=12, B=30, k0=47.
```

For `p=1,...,5`, the exact raw lowest coefficients are

```text
18(84-2p) = 1476,1440,1404,1368,1332,
```

whereas the prompt gives

```text
18(126-2p) = 2232,2196,2160,2124,2088,
```

a fixed discrepancy of 756. This is a second direct refutation of the numeric
transfer. The top-form `B_1` contribution is exact, but the charged inputs do
not contain a case-specific `D=126` joint-chart compiler proving that all
other blocks vanish at this slot or that the post-support row has exactly the
same functional. Its promotion is therefore
`OPEN[ROW-TRANSFER-D126]`, not an analogy from `(99,66)`.

## 6. Row necessity is not a unit ideal

Every positive-degree coefficient of `J(F,G)` must vanish for a Keller pair,
so in a coefficient chart for `F,G` the **full coefficient row** is a necessary
polynomial equation. The charged `(99,66)` chart makes this explicit and checks
the coefficient-ring map (`g9966-chart-necessity-opus5-20260903.md:573-599`).
That fact does not turn one coefficient of the row into a constant generator.

To test precisely the inference forbidden by FALLACY-v2, the probe built only
the ladder rows for `(99,66)`, `D=108`, and `D=126`. In each case it used the
declared ring

```text
Q[L_1,...,L_v_s]
```

and the homogeneous rows `c_p L_p`. All `c_p` are nonzero under `NONRES`, but
the all-zero point is a common zero and the Groebner normal form of `1` is
still `1`. Hence every ladder-only ideal is proper:

| case | ladder-only coefficients | common zero | `NF(1)` | unit ideal? |
|---|---|:---:|:---:|:---:|
| `(99,66)` | `864,837,810,783,756,729,702,675` | yes | 1 | no |
| `D=108` | `840,816,792,768,744,720,696` | yes | 1 | no |
| `D=126` | `1476,1440,1404,1368,1332` | yes | 1 | no |

The membership conclusions are therefore:

1. **`(99,66)`: yes for the actual Jacobian rows, but not from NONRES alone.**
   The compiled support reductions identify the ladder rows as necessary
   joint-ideal rows. The constants 6264 and 64 appear only after the necessary
   branch-specific pole rows are adjoined.
2. **`D=108`: the full positive-degree Jacobian equations are necessary in an
   ambient Keller coefficient chart, but this case's sourced certificate does
   not use them.** The chart is already empty by incidence plus localization;
   a nonzero raw `B_1` contribution is not that certificate.
3. **`D=126`: the raw top-form calculation is exact, but actual reduced-row
   isolation/reachability in a sourced joint chart is open.** Building a
   ladder fragment cannot fill that chart-map gap.

This is exactly the distinction recorded in the charged synthesis: a
Jacobian functional set to zero is consistent; `(99,66),delta=2` dies only
because a pole row sets the same functional to a nonzero affine value, and no
source supplies such a partner uniformly
(`minor-empty-disc-sol56-20260903.md:563-578`). The general missing theorem is
a nonzero augmented Schur row after the pivot block
(`minor-empty-disc-sol56-20260903.md:663-680`). The final Schur scalar depends
on the branch partition, series, normalization, jets, and low-tower
coefficients, not merely `(d_s,u_s,v_s,delta,weights)`
(`two-place-obstruction-core-sol56-20260903.md:646-663`).

## 7. Smallest false skeleton and what must replace the ladder

The lexicographically smallest false group is

```text
(D,m,(M_2,...,M_s),V_s)
  = (144,96,(-72,84,102,142),4),
s=5,
(d_1,...,d_6)=(144,48,24,12,6,2),
(d_s,u_s,v_s,g)=(6,2,4,2).
```

It has three lower-`V_i` row assignments and the single screened order
`delta=3/2`. Resonance occurs at `p=3`, since `6 | 2*3`. The generalized
first-point operator makes the failure concrete. With

```text
H=w^2(w-1)^4,   d_2=48,   d_s=6,
B=H^((48-3)/6)=w^15(w-1)^30,
```

the resonant operator has the nonzero polynomial kernel generated by `B`.
This uses the non-coprime extension of the exact kernel calculation, not its
coprime special case (`minor-empty-disc-sol56-20260903.md:580-625`). Thus the
same ladder block is genuinely rank-deficient at the first predicted
resonance.

If this chart is to die, a row **outside that resonant homogeneous ladder** must
hit its kernel and supply an affine obstruction. Depending on the actual
split datum that can be a common-incidence row (as at `D=108`), a pole row (as
at `(99,66)`), an interior row, or another Jacobian band, followed by a
nonzero augmented Schur/Fitting residue. The frozen inputs do not compile a
joint chart for this `D=144` group and do not select one of those families.
Accordingly the honest answer is

```text
OPEN[FALSE-SKELETON-AUGMENTED-ROW].
```

No uniform replacement row family is inferred from the skeleton symbols.

## 8. Repricing of (H1)

The arithmetic census by itself answers option (b): `NONRES` is false on
`42/166` sharpened groups and `82/274` screened pairs. On the `192/274` pairs
where it is true, it supplies only a conditional nonzero-pivot screen. It does
not prove that the reduced ladder row exists in the relevant stratum, and even
an existing nonzero row does not generate 1.

Therefore:

```text
arithmetic NONRES pass:             192/274 = 96/137;
arithmetic NONRES failure:           82/274 = 41/137;
unit ideals certified by NONRES alone: 0/274;
new uniform (H1) kill:                    none.
```

The literal formula `(N/d_s)(N-u_s p-d_s i)` is `(99,66)`-specific. Its
corrected raw base row preserves the same resonance congruence, but that is
**necessary-not-sufficient only for this particular ladder pivot**. It is not
a necessary condition for a different incidence/pole mechanism to kill the
chart. The flagship is therefore not re-priced as a uniform arithmetic proof.

## 9. Reproduction and artifacts

The bounded drivers are:

```text
box/h1nonres-20260903/nonres_census.py
box/h1nonres-20260903/ladder_probe.py
```

They use one process/core. The exact replay was

```bash
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  timeout 600 python3 -u box/h1nonres-20260903/nonres_census.py

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  timeout 600 python3 -u box/h1nonres-20260903/ladder_probe.py \
  --output-dir box/h1nonres-20260903

python3 -m py_compile \
  box/h1nonres-20260903/nonres_census.py \
  box/h1nonres-20260903/ladder_probe.py

sha256sum -c box/h1nonres-20260903/artifacts.sha256
sha256sum -c box/h1nonres-20260903/ladder-artifacts.sha256
```

Both manifests return only `OK`. The ladder replay also matched the stored
JSON byte for byte. Principal artifacts are:

| artifact | role |
|---|---|
| `summary.json` | totals, provenance, cell and degree tables |
| `all-groups.tsv` | all 166 sharpened group keys |
| `false-groups.tsv` | exact 42 false keys |
| `false-rows.tsv` | all 92 false lower-`V_i` rows |
| `order-pairs.tsv` | all 274 conditional group/order pairs |
| `ladder_probe.stdout.json` | banked-ledger, three-row-family, ideal, and incidence checks |
| `artifacts.sha256`, `ladder-artifacts.sha256` | integrity manifests |

No ledger, `jc2-lean`, or `ideation-*` file was edited. Writes were bounded to
`box/h1nonres-20260903/` and this report.

## 10. FALLACY-v2 audit

* **Flag/place/series:** the census group, candidate order, multiplicity
  partition, physical branch, and chart are kept distinct.
* **Floor/attainment:** the unpromoted candidate floor and the open denominator
  bound are disclosed; neither is promoted to an exhaustive theorem.
* **Variable/ring map:** the raw `B_1` contribution, the full Jacobian row, and
  the post-elimination row are distinguished. `D=126` is left typed `OPEN`
  where the chart map is missing.
* **Raw remainder and unit ideal:** the ring is declared, `NF(1)` is checked,
  the all-zero negative control is exhibited, and a nonzero coefficient is not
  mistaken for a constant normal form.
* **Pole/interior:** pole rows are used only in the two banked `(99,66)` branch
  charts. No pole identity is assigned to another skeleton by analogy.
* **Exit accounting:** this report makes no exit-price assertion, so no
  `charge_basis` declaration is emitted.

Where the charged material has no safe augmented-row replacement, the result
is typed `OPEN` as required by `FALLACY-v2.md:29-30`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23029`.
- Body SHA-256:
  `ea093bd3e0169b2eeb16b18a25d38275613c61e540340e3514da6ae32c11560f`.
- Frozen basis: `e4e0d0eb88d22c50fa3d90bd90936fd7726e1bb1`.
