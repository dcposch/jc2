# Hostile review — unit-load D1 strict unique-`AC`, `d=2,3` composition

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-audit-20260826.md` |
| Overall verdict | **CONFIRMED_CONDITIONAL** |
| Smallest failing identity | none in the seventeen promoted finite tails, the closed `a>=10` source ceiling, or the independent unique-`AC` fan |
| Smallest omitted or extra integral point | none among strict unique-`AC` `d=2,3` points with `1<=a<=9`; the two omitted `s=0` points are the equality faces `(a,d)=(2,2)` and `(3,3)` |
| Condition | frozen `(a,d,r_floor)=(8,3,8)` producer `PRODUCER_FREEZE` `4c9b9e44…` / `RESULT` `0f63f33c…` must be independently hostile-reviewed **CONFIRMED** for exact `ord(A)=8`, `ord(C)=11`, closed `ord(R)>=8` on `D(p*k0*J)`, then narrowly promoted; this review does not so confirm or promote it |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Audit summaries, producer PASS markers, the navigation-only support miner, and the live unfinalized `(8,3,8)` review are not authority |
| Method | SHA-256 of every charged pin, nested freeze/evidence row, and cited review; independent five-weight unique-`AC` inequalities and integral census; band-by-band re-reading of each promotion, CONFIRMED review, and the unpromoted producer statement. No Singular, Sage, msolve, Lean, or package compiler |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the frozen audit and of all seven charged authorities match the required bytes. Nested freeze/evidence trees and every cited CONFIRMED review rehash as recorded below. The distinct cell review

```text
xmodel/max12-812-order2-square-d1-a8d3-targetshadow-chamber-hostile-review-grok-20260826.md
```

is absent. Its `.run` custody is live (`initial_status=RUNNING`, wrapper pid 30198, `start_utc=2026-08-26T21:28:03Z`, no `end_utc`, no verdict token). This review does not complete that cell. No file other than this review was written.

---

## Verdict

**CONFIRMED_CONDITIONAL.**

The frozen file is a literal coverage audit of the normalized integral unit-load strict unique-`AC`, `d=2,3` cell, not a composition promotion and not a whole-D1 theorem. Independently recomputing the unit-load lower hull from

```text
AC=a+c,  C2=2c,  R3=3r,  RC=1+r+c,  A2=4+2a
```

on `q=0`, `a>=1`, `c>=3`, `r>=2` shows that unique minimality of `AC` is exactly

```text
1<=d:=c-a<=3,   s:=r-a>=0,   a+3s>d.
```

Equality faces are excluded. Restricting to `d in {2,3}` and taking the least integral `s` with `r=a+s>=2` yields the claimed `s_min` table. The finite residue `1<=a<=9` is exactly eighteen disjoint closed `R`-tails, one per `(a,d)`, with no omitted strict integral point and no extra equality point.

Seventeen of those baselines are already promoted empty, with exact `A,C` and closed `R`, on `D(p*k0)` or `D(p*k0*J)`, after the registered square/D1 gates. The remaining finite baseline `(8,3,8)` is assigned only to the frozen target-shadow producer; that producer states the matching closed tail on `D(p*k0*J)` and records a triple exact-`Q`/`F_65519`/`F_65521` PASS, but it has no final hostile review and no promotion. The promoted closed source ceiling

```text
a>=10,  c>=a+1,  r>=a
```

on `D(J)` contains every strict `d=2,3` tail at high `a`, including arbitrary larger `C` and `R` order inside that cone. Its `CONFIRMED_CONDITIONAL` parent-promotion condition is discharged by the promoted grade-38 parent.

The common composition, if later promoted after the `(8,3,8)` gate closes, may be stated only as *arcwise* emptiness on `D(p*k0*J)` after the registered gates, and may be conventionally named `D(p*k0)` for Keller sources because `J` is then a unit. It is not a uniform scheme-structure theorem, not whole D1, and not a theorem on any equality face, other primary/tied face, positive-order leading load, or excluded localization.

This review does not import the unreviewed `(8,3,8)` PASS, does not write a composition promotion, and does not decide the live cell review.

**CONFIRMED_CONDITIONAL**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Frozen audit | `cdd23058…` | **MATCH** |
| 0. Seven charged authorities | listed SHA-256 | all seven match |
| 0. Nested reviews | six cited CONFIRMED / one CONFIRMED_CONDITIONAL | hashes and verdicts match; parent promotion discharges the ceiling condition |
| 0. Manifests | freeze/evidence/compiled | low-`a` 5+22+54; E freeze/evidence match promotion; `a=7` 5+25+39; `a=8,d=2` 4+4+36; `(8,3,8)` 6+11+48 and three nested compiled 2/2 by basename; `a=9` 4+21+108; ceiling corollary 7/7 and parent 4+13+30 |
| 0. Live `(8,3,8)` review | inspect, do not decide | **absent / not final**; `.run` `RUNNING`; not imported |
| 1. Unique-`AC` fan | five weights; strict vs closed; `1<=d<=3` | **holds**; equality faces kept out |
| 2. `s_min` table and 18 tails | independent census | **holds**; first omitted strict point: none; extra equality point in the 18: none |
| 3. Literal matching | 18 baselines to promotions or the frozen producer | **holds**; eleven-block excludes E and `a=7..9`; miner not imported |
| 4. Closed `R`; no extrapolation | leading `R` uninverted; E, `a=7` tie, `a=8` split, `a=9` | **holds** on every promoted band; `(8,3,8)` language matches the producer but is not promoted |
| 5. Source ceiling | closed `a>=10,c>=a+1,r>=a`; parent condition | **holds**; condition discharged by parent promotion `d4aceedb…` |
| 6. Localizations | `D(p*k0)`, `D(p*k0*J)`, `D(J)` | **holds** as an audited common open, not a new theorem |
| 7. Theorem type | mixed unit ideals vs jet/rootwise | **holds**; strongest common type is arcwise/set-theoretic emptiness |
| 8. Qring / residuals | no silent whole-D1 | **holds**; residual list below is necessary |

---

## 0. Custody

Recomputed SHA-256 of the frozen audit and of the seven charged authorities:

| Artifact | SHA-256 | Role |
|---|---|---|
| composition audit | `cdd2305804073e771b26d00a22030486a3d8347c6d70c41f4d6a7a7b6482e1c7` | frozen coverage audit |
| eleven-block promotion | `8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da` | **PROMOTED** |
| E promotion | `2ff74f6914a3316104d7a406ca6d6d4ede2cf8332221dfcccd7461f9d925176e` | **PROMOTED** |
| `a=7` promotion | `b5c38f1b2e2e5ec6f2ac32fb350f11686dac5cb45eabe8cf1ea67d20726bd362` | **PROMOTED** |
| `a=8,d=2` promotion | `9cc6870289ec0697e438c3999616194d3955e3bc875cd69cad855fd16d28c3b9` | **PROMOTED** |
| `(8,3,8)` `PRODUCER_FREEZE.sha256` | `4c9b9e441d666b91d8255af8aca3978eeccd8263775b33184a1e3334f0fd51b2` | producer freeze; **not a promotion** |
| `a=9` promotion | `551ca2f6f8aaf75fd67019d055e43ae862150de62d51cb0bd8755d4d0085a19a` | **PROMOTED** |
| `a>=10` ceiling promotion | `470ea478c9463d62d39a428962fd9dd5845f4bf882388f84594c82a211634fb8` | **PROMOTED** |

Cited reviews and nested producer pins, independently rehashed:

| Artifact | SHA-256 | Verdict / role |
|---|---|---|
| eleven-block review | `841f0d6ccbb596fa4ace3f08760f039eb288030efa91075112e915d1320592a3` | **CONFIRMED** |
| eleven-block `PRODUCER_FREEZE` | `4d69b97d8c6e24baadc76aba69d3d37158a3aa466cf7e44bc3111008c5a07fd3` | 5/5 |
| eleven-block `RESULT.md` | `04324859fac936e4bca2e114e259d7bcf444491c21d905219a9490deb3dab012` | producer report |
| E review | `984783eab8342d2523a6e1d7365785f5d37746d0393fc30cfad206bb5658b774` | **CONFIRMED** |
| E `PRODUCER_FREEZE` | `65a40079b7b52964a775d01ef651f24ee04dcce05650147ed11327ace5913237` | matches promotion |
| E `RESULT.md` | `f2b947ddb2b251069666bb8287800127253ca3f118f5fb22587b3b0032bba1f5` | matches promotion |
| E `EVIDENCE.sha256` | `31050d988c6246a48610847a7e7498bc55922a8ea0c9a4e87a1db7a30808e382` | matches promotion |
| `a=7` review | `1ae7f6d95b7d707b3fe54b07a59fbd103435d13b4a0a764b6495215785d26530` | **CONFIRMED** |
| `a=7` `PRODUCER_FREEZE` | `bb662b3d25cd12dec712dc2763e1efd6dd09b1dd084babce65bcb9effb0daac0` | 5/5 |
| `a=7` `RESULT.md` | `69048f6fd2f3ddf78e8328840d0400fe29d523c5258fbd5c154b211559c433aa` | producer report |
| `a=8,d=2` review | `0558ea1e668245b983e217ef329a6ccf0baf5a8f5769f669f43a245d24990e21` | **CONFIRMED** |
| `a=8,d=2` `PRODUCER_FREEZE` | `9a85f15ea741255ecda04fc787467393d1661a08cd8ed501549d4cacf32d91fd` | 4/4 |
| `a=8,d=2` `RESULT.md` | `919f6e1a296e084ffdf4d569fcf8c184bcf5b2cf263f47b2882bd03f50539021` | producer report |
| `(8,3,8)` `RESULT.md` | `0f63f33ced93c1109e3146172e46b33e3fee28e174b081d1a1e426150168ba23` | **unpromoted** producer report |
| `(8,3,8)` `FREEZE.sha256` | `76ebe3a4d8c8dfad196cf72c96f2221cef540c600a6ab9b80225744163c39f8a` | 11/11 |
| `(8,3,8)` `EVIDENCE.sha256` | `24d74a8441b11fd6105a4db1cbb3dd390fdc253f5de0fc9ea4ec624c000d95c0` | 48/48 |
| `a=9` review | `f922fab0828ff0470ada62fa22bd84a9383233b27948bca12726f1c3aa7785f5` | **CONFIRMED** |
| `a=9` `RESULT_A9.md` | `65ecc9cb8c4a51fb699e8ff86fdd4d5cb4b7dce744f77a77d2f0c4bc346c01db` | producer report |
| `a=9` `PRODUCER_FREEZE_A9` | `3430b677791372e50b3fc0bc3ad2f504f234832c1f0f1f38f6a891dec64affd1` | 4/4 |
| `a=9` `EVIDENCE_A9` | `0e953f19aef02184f0dc68e80b0d61deca5c53b5292d7b057744dfd848c20d53` | 108/108 hash rows |
| `a=9` `FREEZE.sha256` | `4a36e6ff0b97800559bbef9b1366ab1e995f2e1deef341b1d009b2d4f7595dc6` | 21/21 |
| ceiling review (Grok V2) | `f75d885da6b39af85127540fa8ede8a17d1f83a3a2d5279bb5c641f2bd98e15b` | **CONFIRMED_CONDITIONAL** |
| ceiling corollary | `d0ef64c39189df96654df50726fd7b65a958e0eaea67ec2204456b7bc9bf3087` | frozen corollary |
| ceiling `.sha256` | `7cdf4a707204bcd7fbbbea6e6b21aab687afef11b2a8aad7e33a864b01fac560` | 7/7 |
| parent `a>=10` promotion | `d4aceedbead2d0c27546e143ae8bb2b820faa32dd08454c58650f280593d0fb2` | **PROMOTED**; discharges the ceiling condition |
| parent `a>=10` review | `a4eff964e517e9050191bba938cb3573e90c904c7bcf0d492cfe36fce0dd60a2` | **CONFIRMED** |
| parent `RESULT.md` | `2ccfdfe9c3deb4d32594d2f5e1237684023d5b75438a02229776436c38456883` | parent producer |

Manifest counts independently recomputed: eleven-block `FREEZE` 22/22 and `EVIDENCE` 54/54; `a=7` `FREEZE` 25/25 and `EVIDENCE` 39/39; `a=8,d=2` `FREEZE` 4/4 and `EVIDENCE` 36/36; `(8,3,8)` `PRODUCER_FREEZE` 6/6, `FREEZE` 11/11, `EVIDENCE` 48/48, and each of the three nested `compiled.sha256` files 2/2 after resolving AWS absolute paths by basename; `a=9` as above; parent `PRODUCER_FREEZE` 4/4. The nested eleven-block review prints `FREEZE` 23/23; the freeze file on disk has 22 nonempty rows, all matching. That is a non-blocking nested count discrepancy, not a missing pin.

The `(8,3,8)` cell review file is not present. Custody of

```text
xmodel/max12-812-order2-square-d1-a8d3-targetshadow-chamber-hostile-review-grok-20260826.run
```

records `adapter=grok`, `initial_status=RUNNING`, `child_pid=60118`, wrapper pid 30198 still live, and no `CONFIRMED`/`REFUTED`/`INCONCLUSIVE` token. A passing producer freeze is not a mathematical verdict. The algebra below does not import that PASS.

The low-`a` support miner appears in freeze ancestry of the eleven-block and `a=7` producers. Its allocated-root census is not an authority for any band of this composition, and was not used below.

A passing manifest is not a theorem.

---

## 1. Strict unique-`AC` from the five unit-load weights

On the normalized integral unit-load horizontal chart put `q=ord(k10)=0`, `a=ord(A)>=1`, `c=ord(C)>=3`, `r=ord(R)>=2`. After subtracting the common absolute grade ten, the ordinary lower envelope of the unit-load chart is generated by the five weights named in the charge. Independently:

```text
AC-C2 = a-c = -d,
AC-A2 = (a+c)-(4+2a) = d-4,
AC-RC = (a+c)-(1+r+c) = a-1-r = -(s+1),
AC-R3 = (a+c)-3r = 2a+d-3(a+s) = d-a-3s.
```

Strict unique minimality of `AC` is therefore the conjunction of four strict inequalities

```text
d>0,     d<4,     s>-1,     a+3s>d.
```

At integral points this is exactly `1<=d<=3`, `s>=0`, and `a+3s>d`. The closed `AC` cell includes the equality faces `d=0` (`AC=C2`), `d=4` (`AC=A2`), `s=-1` (`AC=RC`), and `a+3s=d` (`AC=R3`). Those faces are **not** unique-`AC` and are kept out of this cell.

The restriction `d in {2,3}` is a subset of `1<=d<=3`, so the `C2` and `A2` comparisons are automatic on the charged cell. The remaining content of unique-`AC` on that cell is exactly `s>=0` and `a+3s>d`.

The next-weight gaps relative to `AC` are

```text
C2: d,     A2: 4-d,     RC: 1+s,     R3: a+3s-d.
```

On `d in {2,3}` and `s>=0` with `a+3s>d`, each of these is a positive integer, so unique minimality is not lost by raising `R`. The `RA2` weight `2+r+2a` satisfies

```text
RA2-AC = a+s+2-d.
```

On the charged cell this is at least `a-1` at `(d,s)=(3,0)` and at least `a` at `(d,s)=(2,0)`. For `a>=1` it is strictly positive except possibly `a=1,d=3,s=0`, which is excluded both by `a+3s>d` and by `r>=2`. The entire unit-load `RA2` hull is the tied locus `(a,r)=(1,2)`, `c>=5`, which has `d>=4` and is disjoint from unique-`AC` `d=2,3`. `A3` lies strictly above `A2` by `a+1`. Completeness sentinels `RAC`, `RC2`, `kAC`, and `kR2A` are never lower-face generators on this domain; they are not needed for the unique-`AC` interior.

---

## 2. Least integral `s` and the eighteen finite baselines

The domain constraint `r=a+s>=2` is imposed on top of `s>=0` and `a+3s>d`. The least such integral `s` is as follows.

For `d=2`, the inequality `a+3s>2` at `s=0` is `a>2`, hence `a>=3`. At `a=1` one has both `r=1<2` and `a+3s=1<2`; at `a=2` one has `r=2` but equality `a+3s=d`. In both cases `s=1` works (`a+3=4>2`, and `r=a+1>=2`). Thus

```text
d=2:  s_min=1 for a=1,2;   s_min=0 for a>=3.
```

For `d=3`, `s=0` requires `a>3`, hence `a>=4`. At `a=1,2` one has `a<3`; at `a=3` one has equality `a+3s=d`. In all three cases `s=1` works. Thus

```text
d=3:  s_min=1 for a=1,2,3;   s_min=0 for a>=4.
```

Each pair `(a,d)` with `1<=a<=9` and `d in {2,3}` therefore determines exactly one closed `R`-tail with floor `r_floor=a+s_min`. That is eighteen baselines. They are disjoint as contact cells because each has its own exact `(a,d)` and a closed `r>=r_floor` tail.

An exhaustive integral census of unique-`AC` points with `1<=a<=15`, `2<=r<=19`, `3<=c<=23` produces, on `d in {2,3}` and `1<=a<=9`, precisely the eighteen closed tails with the `s_min` table above. Every integer `s>=s_min` in the scanned `r`-window occurs; there is no interior gap. The symmetric difference against the claimed list is empty.

The two omitted in-domain `s=0` points are equality faces, not gaps:

```text
(a,d,s,r,c)=(2,2,0,2,4):  AC=R3=6,  ties {R3};
(a,d,s,r,c)=(3,3,0,3,6):  AC=R3=9,  ties {R3}.
```

No other `s=0` unique-`AC` `d=2,3` point with `a<=9` exists. The `s=-1` points with `d in {2,3}` that appear in the same window (for example `(5,2,-1)` tying `{R3,RC}`, and the `AC=RC` family at `a>=6`) are equality faces of unique-`AC` against `RC` and/or `R3`; they are correctly excluded. First omitted strict integral unique-`AC` `d=2,3` point in `1<=a<=9`: **none**. First extra equality point among the eighteen baselines: **none**.

The eighteen baselines, written as `(a,d,r_floor)`, are

```text
(1,2,2), (1,3,2),
(2,2,3), (2,3,3),
(3,2,3), (3,3,4),
(4,2,4), (4,3,4),
(5,2,5), (5,3,5),
(6,2,6), (6,3,6),
(7,2,7), (7,3,7),
(8,2,8), (8,3,8),
(9,2,9), (9,3,9).
```

---

## 3. Literal matching; eleven-block exclusions; miner not imported

Each of the eighteen baselines is assigned as follows. In every promoted finite theorem, `ord(A)` and `ord(C)=a+d` are exact, and `ord(R)>=r_floor` is a closed tail.

| baselines | count | authority | exact `A,C` / closed `R` | open |
|---|---:|---|---|---|
| `(1,2,2)`; `(2,2,3),(2,3,3)`; `(3,2,3),(3,3,4)`; `(4,2,4),(4,3,4)`; `(5,2,5),(5,3,5)`; `(6,2,6),(6,3,6)` | 11 | eleven-block promotion `8b92c22b…`, review `841f0d6c…` **CONFIRMED** | exact `ord(C)=a+d`, `ord(R)>=r_floor` | `D(p*k0)` |
| `(1,3,2)` | 1 | E promotion `2ff74f69…`, review `984783ea…` **CONFIRMED** | `ord(A)=1`, `ord(C)=4`, `ord(R)>=2` | `D(p*k0)` |
| `(7,2,7),(7,3,7)` | 2 | `a=7` promotion `b5c38f1b…`, review `1ae7f6d9…` **CONFIRMED** | exact `(A,C)=(7,9)` and `(7,10)`, `ord(R)>=7` | `D(p*k0)` |
| `(8,2,8)` | 1 | `a=8,d=2` promotion `9cc68702…`, review `0558ea1e…` **CONFIRMED** | `ord(A)=8`, `ord(C)=10`, `ord(R)>=8` | `D(p*k0)` |
| `(8,3,8)` | 1 | frozen producer `4c9b9e44…` / `RESULT` `0f63f33c…` only | producer states `ord(A)=8`, `ord(C)=11`, `ord(R)>=8` | producer open `D(p*k0*J)` |
| `(9,2,9),(9,3,9)` | 2 | `a=9` promotion `551ca2f6…`, review `f922fab0…` **CONFIRMED** | exact `(A,C)=(9,11)` and `(9,12)`, `ord(R)>=9` | `D(p*k0*J)` |

Count: `11+1+2+1+1+2=18`. No baseline is double-assigned. No strict `1<=a<=9` unique-`AC` `d=2,3` tail is unassigned.

The eleven-block promotion lists exactly those eleven triples and states that `(1,3,2)` is not promoted. Its CONFIRMED review excludes `E=(1,3)` as a pole-three control with no emptiness verdict, and independently records the six cells `a=7,8,9` with `d=2,3` as outside the producer (`a=7` is a load tie, `a=8,9` are load-first, and row-4 targets at grades 32/34 are outside the eleven-block windows). That is the exclusion claimed by the audit.

The `(8,3,8)` row is a producer assignment, not a promotion. The producer theorem, as written, is the missing closed tail. This review matches that language and does not import the PASS.

The support miner is cited in the audit only as navigation. It is not used here as a theorem, including for the `a=7` tie and the `a=8,9` chambers.

---

## 4. Closed `R` tails; exceptional clients; no extrapolation

Every promoted finite theorem writes `R=sigma^{r_floor}*(b1+t*b0+jets)` and does not invert `b0` or `b1`. Extra nonnegative powers of the uniformizer only delay `R`-bearing families. The named obstruction in each band is independent of leading `R`. That is the closed tail `ord(R)>=r_floor`, not an exact-order slice, and it is not obtained by inverting a leading coefficient of `R`.

The exceptional clients are distinct source/timing chambers. Nothing may be extrapolated across them.

- **E.** The eleven-block routes `(1,3,2)` because the second correction `-(3/8)R A^2/L^2` is nonzero and the global pole ceiling is three. The E promotion closes the cell by the unique pole-three family `-(1/16)A^3/L^3` after opposite-root allocation, with deck-conjugate terminal units `±(1/2)au^3 lambda^3`. Rows 1, 3, 5, 6 are target-free through grade 18. Leading `R` is uninverted, so the tail is `ord(R)>=2`. This is not the eleven-block `C^2` argument.
- **`a=7` load tie.** At the first wall the complete tied column is `(3/4)C(A+k60)/L`. The multiplication determinant `Delta_C=c0^2+(p/2)c1^2` closes the rank-two chamber; the rank-one face is retained and is killed by the dual pole-two functionals, which generate the unit ideal on both exact-`C` charts before radicals. Terminal grades 28 (`d=2`) and 30 (`d=3`) lie before the row-4 target at grade 32. The promotion firewall forbids `a=8,9`.
- **`a=8,d=2` load-first.** Exhaustive scheme split `D(k60) union V(k60)`. On `D(k60)` the unique grade-27 primitive `(3/4)k60 C/L` generates the unit ideal on both exact-`C` charts one grade before the row-2 target. On `V(k60)` the dual pole-two squares close both the rank-two and rank-one chambers. The CONFIRMED review firewall names `a=8,d=3` as a different chamber: first load grade 28 already coincides with the row-2 target (target-shadowed, not load-first). No emptiness claim may be copied from `d=2` to `d=3`.
- **`a=8,d=3`.** Assigned only to the frozen target-shadow producer. The producer states the closed tail on `D(p*k0*J)` by a four-odd-row combination and an exact-`C` cover `D(c1) union (V(c1) intersect D(c0))`. Neighboring promotions explicitly exclude this cell: `a=8,d=2` by target-shadow timing; `a=9` because the grade-38 bridge route used there is a different source (seventeen polar families, first pole-four at grade 41) and was falsified as a bridge for `(8,3)`. This review does not rederive the residual identity or the two compiled unit ideals, and does not promote the cell.
- **`a=9`.** Each cell has thirteen polar families and pole ceiling three through grade 38. The moving odd-row identity leaves `-sigma^38 J/4`; adjoining `iJ*J-1` is the unit ideal before radicals. The identity is polynomial in the homogeneous `R` factor `eta`, so `eta=sigma^s` covers `ord(R)>=9` without inverting `eta` or leading `R`. Exact `A,C`, not closed `C`. The neighboring `(8,3)` cell is excluded in both the promotion and the CONFIRMED review.

Raising `R` inside a promoted band is part of that band's closed theorem. It is not a licence to cross a load-tie, load-first, target-shadow, or pole-three wall.

---

## 5. Closed source ceiling; parent condition discharged

The ceiling promotion, after the CONFIRMED_CONDITIONAL Grok V2 review `f75d885d…` and the parent promotion `d4aceedb…`, states empty scheme on `D(J)` throughout

```text
a>=10,  C in sigma^c k[[sigma]][z]_{<=1} with c>=a+1,
        R in sigma^r k[[sigma]][z]_{<=1} with r>=a,
```

with no displayed leading coefficient of `A`, `C`, or `R` inverted. The substitutions `theta=sigma^n`, `eta=sigma^s`, `Cbar=sigma^m Chat` with `n,m,s>=0` are polynomial specializations of the promoted grade-38 identity. For `0<=m<=10` the frozen `C_10` jet is tight; at `m=11` the first `C`-dependent family `k6 C/L` moves to grade 39 and vanishes modulo `sigma^39`. Raising `C` delays every family containing `C`, does not increase pole order, and moves the first pole-four family from grade 43 to `43+m`. The odd-row combination remains `-sigma^38 J/4`; adjoining `iJ*J-1` is the unit ideal before radicals.

Every strict unique-`AC` `d=2,3` point with `a>=10` satisfies `c=a+d>=a+2>=a+1` and `r=a+s>=a`, and `a+3s>d` is automatic because `a>=10>3>=d`. The closed cone therefore contains both `d=2,3` tails for every `s>=0`, including arbitrary larger `C` order inside `c>=a+1` and arbitrary larger `R` order inside `r>=a`. An independent census of unique-`AC` `d=2,3` points with `a>=10` in a finite window finds no point outside the cone. First high-`a` omitted unique-`AC` `d=2,3` point: **none**.

The Grok V2 ceiling review returned `CONFIRMED_CONDITIONAL`, with sole condition independent confirmation and promotion of the frozen parent producer. That condition is discharged by the parent promotion `d4aceedb…`, which itself rests on the CONFIRMED parent review `a4eff964…` of exact-contact `a>=10`, `c=a+1`, `r>=a` on `D(J)`. The earlier Claude delivery has no report and no verdict; it is not used. This composition review does not re-prove the parent identity.

The ceiling promotion firewall correctly refuses `a<=9`. Finite `a<=9` coverage remains the eighteen baselines of §3.

---

## 6. Localizations

Named opens of the inputs:

- eleven-block, E, `a=7`, `a=8,d=2`: `D(p*k0)` after the registered square/D1 gates;
- `a=9`: exact producer open `D(p*k0*J)`; the promotion records that a Keller source has `J` a unit, so the campaign normally names `D(p*k0)`;
- ceiling: `D(J)` after the same registered gates;
- unpromoted `(8,3,8)` producer: `D(p*k0*J)`, with the same Keller naming remark and with an explicit refusal to assert the global composition.

The largest open on which every promoted input may be restricted is `D(p*k0*J)`. Restricting a theorem on `D(p*k0)` to `D(J)`, or a theorem on `D(J)` to `D(p*k0)`, is valid and does not invert a new leading coefficient. On a Keller source `J` is a unit, so `D(p*k0*J)=D(p*k0)` as opens of that source; the campaign name `D(p*k0)` is then conventional. It does **not** erase the hypothesis `J` invertible, and it is not a theorem on `V(J)`, `V(p)`, or `V(k0)`.

Until `(8,3,8)` is independently reviewed and promoted, this localization reconciliation is only an audited route for a later composition statement. It is not itself a new composition theorem, matching the audit.

On the unit-load chart `q=0`, the leading jet of `k10` is `k0`, so `D(k10)` and `D(k0)` coincide. The finite theorems that invert `k0` are already on the registered D1 chart.

---

## 7. Strongest common theorem type

The inputs are not of one theorem type.

The eleven-block CONFIRMED review proves emptiness of a localized `T`-jet / formal chart on the finite etale root cover, then descends. It expressly is “not a claim about associated primes of an unlocalized ideal.” E is the same kind of statement at grade 18: localized unit ideals on both sheets, finite etale descent, no formal arc, jet-truncated.

The `a=7` and `a=8,d=2` theorems generate the unit ideal before radicals from explicit dual squares (and, for `a=8,d=2`, from a scheme-theoretic split `D(k60) union V(k60)`), then descend from the etale cover. The `a=9` and ceiling theorems adjoin `iJ*J-1` to `-J/4` and obtain the unit ideal before radicals on `D(J)`; those two are scheme-theoretic emptiness of the named open.

The union of “no point / no formal arc” statements is arcwise, equivalently set-theoretic, emptiness on the common open `D(p*k0*J)`. It does **not** support a uniform scheme-structure assertion for the unlocalized seven-equation ideal on that open. A later composition promotion must not silently upgrade mixed jet/rootwise exclusions and unit-ideal certificates to a single scheme-theoretic claim.

The unpromoted `(8,3,8)` producer writes an exact ideal-membership certificate for two compiled odd-row ideals. Even after that cell is reviewed, the *union* with the eleven-block and E remains mixed, so the strongest honest common type of the composition stays arcwise emptiness.

---

## 8. Qring safety, firewalls, residuals

Qring. The `a=9` CONFIRMED review records no `qring` in any of the six retrieved compiled programs: ordinary `ring R=char,(…),dp;` with `reduce` against `std(ideal(sigma^N))`. The ceiling parent is the same shape; the Grok V2 review records an ordinary polynomial ring whose only extra inverse variable is `iJ`. The `(8,3,8)` compiler extends a frozen parent ring by `ip,ik0,ic1,ic0` and uses `std`/`reduce` on ordinary polynomial ideals; the three retrieved compiled scripts begin `ring R=0` / `65519` / `65521` and contain no `qring`. Division by `sigma^{28}` or `sigma^{38}` is issued only after a `reduce(..., std(ideal(sigma^N)))==0` guard. Those observations are qring-safety inspections of frozen bytes, not a mathematical confirmation of the unreviewed chamber split.

Firewalls of the inputs are respected. In particular: the eleven-block does not cover E or `a=7..9`; E does not cover any neighboring strict cell; `a=7` does not cover `a=8,9`; `a=8,d=2` does not cover `a=8,d=3`; `a=9` does not cover `(8,3)`; the ceiling does not cover `a<=9`. Positive-order leading load, equality faces, `p=0`, `k0=0`, `J=0`, terminal/global charts, the square component, order two, `(8,12)`, maximum twelve, and JC2 remain outside every cited theorem.

Exact first residual D1 cells after this composition, even after the `(8,3,8)` gate later closes, are:

1. Unique-`AC` equality faces: `d=0` (`AC=C2`), `d=4` (`AC=A2`), `s=-1` (`AC=RC`), and `a+3s=d` (`AC=R3`), including the two omitted `s=0` points `(a,d)=(2,2)` and `(3,3)` and the `AC=RC` family at `s=-1`.
2. Other primary unique-minimum interiors `C2`, `R3`, `RC`, `A2`, and all of their tied intersections, including the exceptional unit-load `RA2=A2=R3` locus `(a,r)=(1,2)`, `c>=5`.
3. The other unique-`AC` family `d=1` (the separate contact-ladder cell `a>=2`, `c=a+1`, `r>=a`), which is not this composition.
4. Positive-order leading load `q=ord(k10)>0`.
5. Excluded localizations `p=0`, `k0=0`, `J=0`, and the excluded zero/infinity and terminal/Taylor charts.

This is not whole D1, not the square component, not order two, not maximum twelve, and not JC2. Until the `(8,3,8)` review and promotion exist, that single finite baseline is an additional lifecycle residue of the present audit, not a mathematical hole in the unique-`AC` partition.

The audit’s phrase “two finite lifecycle gaps” is wording for the still-unpromoted `(8,3,8)` cell together with this composition review itself. There is one missing finite *cell*, namely `(8,3,8)`. That is a lifecycle condition, not an omitted integral point.

---

## Firewall

This review may at most license a later composition promotion for the normalized integral unit-load strict unique-`AC`, `d=2,3` cell as arcwise emptiness on `D(p*k0*J)` after the registered square/D1 gates, and only after the frozen `(8,3,8)` producer is independently CONFIRMED and narrowly promoted. It says nothing about equality faces, primary `C2/R3/RC/A2` or their ties, positive leading load order, `p=0`, `k0=0`, `J=0`, zero/infinity or terminal landing, the full square component, order two, maximum twelve, or JC2. It does not promote the composition, and it does not confirm the live `(8,3,8)` cell.

If the `(8,3,8)` review returns other than CONFIRMED, the surviving union is the seventeen promoted finite baselines together with the closed `a>=10` ceiling; the smallest then-missing strict cell is `(a,d,s)=(8,3,0)`, i.e. `(a,d,r_floor)=(8,3,8)`.

---

## Verdict

**CONFIRMED_CONDITIONAL**

Condition, stated exactly: the frozen `(a,d,r_floor)=(8,3,8)` producer with

```text
PRODUCER_FREEZE  4c9b9e441d666b91d8255af8aca3978eeccd8263775b33184a1e3334f0fd51b2
RESULT.md        0f63f33ced93c1109e3146172e46b33e3fee28e174b081d1a1e426150168ba23
```

must be independently hostile-reviewed CONFIRMED for the closed tail `ord(A)=8`, `ord(C)=11`, `ord(R)>=8` on `D(p*k0*J)` after the registered square/D1 gates, and then narrowly promoted. The distinct cell review named in the charge is absent and its `.run` is not final. This composition review does not perform that review, does not import the producer PASS, and does not write a composition promotion.

**CONFIRMED_CONDITIONAL**
