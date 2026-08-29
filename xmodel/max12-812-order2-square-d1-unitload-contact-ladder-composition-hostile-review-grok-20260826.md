# Hostile review — unit-load D1 unique-`AC`, `d=1` contact-ladder composition

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-square-d1-unitload-d1-contact-ladder-composition-audit-20260826.md` |
| Fan authority | `xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md` |
| Overall verdict | **CONFIRMED_CONDITIONAL** |
| Smallest failing identity | none in the frozen `a=2..9` ladder or in the affine unique-`AC` `d=1` cell |
| Smallest omitted integral point | none in `a>=2`, `c=a+1`, `r>=a` on the registered unit-load domain |
| Condition | frozen `a>=10` producer RESULT `2ccfdfe9…` / PRODUCER_FREEZE `60b2e1d5…` must be independently hostile-reviewed CONFIRMED for `a>=10,c=a+1,r>=a` on `D(J)` after the same gates, then promoted; this review does not so confirm or promote it |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Audit summaries, producer PASS markers, and unnamed concurrent reviews are not authority |
| Method | SHA-256 of every named pin and every source/evidence manifest row; independent pairwise hull comparison and integral census; band-by-band re-reading of RESULT, freeze, promotion, and CONFIRMED reviews; mechanical binomial grading of the `a>=10` primitives and jet ceilings. No Singular, Sage, msolve, Lean, or package compiler |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of both required primary pins and of every named constituent match the charged bytes. Every path named in the `a=2..5` freeze (4/4) and evidence (28/28), the `a=6,7` freeze (4/4) and evidence (32/32), the `a>=10` producer freeze (4/4) together with nested `FREEZE` (13/13) and `EVIDENCE` (30/30), and the `a=8` / `a=9` freeze/evidence trees cited by their promotions, rehashes to the printed digest. Nested `compiled.sha256` rows rehash after resolving AWS absolute paths by basename. No file other than this review was written.

---

## Verdict

**CONFIRMED_CONDITIONAL.**

The frozen audit is a literal coverage audit of the normalized integral unique-`AC`, `d=1` cell, not a promotion and not a whole-D1 theorem. Independently recomputing the unit-load lower hull from the five candidate weights shows that the unique-minimum integral cell on the registered domain `q=0`, `a>=1`, `r>=2`, `c>=3` is exactly

```text
a>=2,  c=a+1,  r>=a.                                 (D1-AC1)
```

There is no omitted integral point, no silent closed-versus-strict enlargement, and no collision with the `RA2` exception. The five contact intervals `{2,3,4,5}`, `{6,7}`, `{8}`, `{9}`, `{a>=10}` partition that cell with no gap. On the unit-load chart, `k10` and its leading jet `k0` define the same open. The `D(J)` tail may be restricted to `D(p*k0*J)`; that is the largest common open on which the bands compose.

The named `a=2..5` and `a=6,7` CONFIRMED reviews, the promoted `a=8` and `a=9` theorems, and the independently inspected `a>=10` producer statement, together exhaust (D1-AC1) as an *arcwise* emptiness on `D(p*k0*J)` after the reviewed first-normal, half-weight, and `M=0` gates — **if** the frozen `a>=10` producer theorem is independently hostile-reviewed CONFIRMED for the cone it actually states. This composition review does not import that producer PASS, and does not promote it.

The composition is not reduced scheme structure of the cell, and it is not whole D1.

**CONFIRMED_CONDITIONAL**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Two primary pins | hashes | both match the required bytes |
| 0. Named constituents | every named file | all fifteen charged paths match |
| 0. Manifests | every freeze/evidence row | `a=2..5` 4+28; `a=6,7` 4+32; `a>=10` producer 4 and nested 13+30; `a=8` 10+32; `a=9` endpoint 9+46, grade-27 7+43, collision freeze 9/9; nested compiled by basename |
| 1. Unique-`AC` `d=1` cell | five weights; strict vs closed; `RA2`; integral `ord_sigma` | **holds**; first omitted integral unique-`AC` `d=1` point: none. First omitted if `r>a` were used: `(2,3,2)` |
| 2. Partition and `k10`/`k0`/`D(J)` | `{2..5}∪{6,7}∪{8}∪{9}∪{a>=10}`; same unit-load open; `D(J)` to `D(p*k0*J)` | **holds**; `a>=13` is overlap on `D(J)` for `a>=13` only and does not fill `a=10,11,12` |
| 3. `r>a` | `eta=0` finite bands; next-R-jet timing; exact contact; homogeneous tail | **holds** in every named band |
| 4. Lower-load transitions | no early `k6`; `a=6,7` timing; `a=8` `D(k60)/V(k60)`; `a=9` scheme split and DVR; `a>=10` jet list | **holds** as stated, with theorem-type differences recorded in §5 |
| 5. Upstream gates and theorem type | first-normal / half-weight / `M=0`; arcwise vs scheme | **holds**; composition is arcwise emptiness, not reduced scheme structure |
| 6. Missing early promotions | reviews `e03de4e1…` and `3e601cf3…`; no `xmodel/*promotion*` | **lifecycle, not a mathematical gap**; two narrow promotions must be written before composition promotion |
| 7. Frozen `a>=10` producer | inspect, do not promote | producer states the missing cone on `D(J)` and is source-complete at the inventory/jet-ceiling level; **not imported**; composition is conditional on its separate review and promotion |
| 8. Residuals | not whole D1 | **holds**; residual list is necessary and not silently absorbed |

---

## 0. Custody

Recomputed SHA-256 of the two required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-square-d1-unitload-d1-contact-ladder-composition-audit-20260826.md` | `52ab6ce6a9628dfc019d1e99aa2deba8af9a6f467f23f2821ff1f30109a56d85` | frozen coverage audit |
| `xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md` | `c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d` | affine lower-hull lemma |

Named constituents, independently rehashed:

| Artifact | SHA-256 | Role |
|---|---|---|
| `a=2..5` `RESULT.md` | `17c3baa20232dad9dd1356c8e903a863a44480344d81d8aa587216414aad0a61` | producer report |
| `a=2..5` `FREEZE.sha256` | `9c53eecf7aa3a1fbc75012d9566a2d564e7a39da7e9011c6d5fd63cd53431920` | source freeze |
| `a=2..5` `EVIDENCE.sha256` | `49264a8d6ae24724ee1005dfac9b4602946f2f3b7a77c0512df237369470f254` | evidence freeze |
| `a=2..5` hostile review | `e03de4e1fc1816a7141c6bb8060b4a75c2a6b5a08ea4d56ca63582b875cad335` | **CONFIRMED** |
| `a=6,7` `RESULT.md` | `f3c987b630a2895defabcc1043768497f2e8caad538f58122bb4e17b317c0a9c` | producer report |
| `a=6,7` `FREEZE.sha256` | `b2a38e4f5c38166789c5d73ecae989c30ed8168c5fc6a58fc3058eb5535e1ad5` | source freeze |
| `a=6,7` `EVIDENCE.sha256` | `eb0058746a406c9d36c11d00c97884e7e937f93cf693763401aa957c432990ee` | evidence freeze |
| `a=6,7` hostile review | `3e601cf34eb23270daa067794087155b7179607d27af01f84a60624447f949e3` | **CONFIRMED** |
| `a=8` promotion | `3d847561946751c68a081db55f2f514b3808c22f7ac6e236fcbff10911ab1ce6` | **PROMOTED** |
| `a=8` hostile review | `b5944e1582a2df9ff37224bd7c5875520321f0ee0998c63c8ceeeedfbb66bba2` | **CONFIRMED** |
| `a=9` composition promotion | `dfabe08283e8fe9cb1ea6cef28a9eac6a4728d0f7c482e8c642b2835798d0459` | **PROMOTED** |
| `a=9` composition review | `8524bd1e20ecfc3931df5c9df9e88f6673de5a7f348b015954884acdddd558eb` | **CONFIRMED** |
| `a>=10` `PRODUCER_FREEZE.sha256` | `60b2e1d52156f0648f7f39739f06c139d7d274c28fe4147eaba8d7213dfc2f0b` | producer freeze; **not a promotion** |

`a=2..5` `FREEZE` names four files, all matching (`REGISTRATION.md` `1329021d…`, compiler `beff666b…`, `run_aws.sh` `74452826…`, `launch_host.sh` `3ec2bbf1…`). `EVIDENCE` names 28 files; all 28 rehash. Both nested `compiled.sha256` rehash by basename to the retrieved `.sing` / `result.json` (exact Q `0e6a3098…` / `07c702f2…`; `F_65521` `8e4845e5…` / `7e844a5c…`).

`a=6,7` `FREEZE` names four files, all matching (`REGISTRATION.md` `d9053b80…`, compiler `03a76642…`, `run_aws.sh` `e7dd9fde…`, `launch_host.sh` `61259870…`). `EVIDENCE` names 32 files; all 32 rehash. Both nested `compiled.sha256` rehash by basename (exact Q `ef494de7…` / `fb98814f…`; `F_65521` `16ed9782…` / `f5d963ee…`).

`a>=10` `PRODUCER_FREEZE` names four files, all matching, including RESULT `2ccfdfe9c3deb4d32594d2f5e1237684023d5b75438a02229776436c38456883`, `EVIDENCE.sha256` `25793913…`, `FREEZE.sha256` `d5bf43b8…`, and `AWS_LAUNCH_METADATA.md` `9720c604…`. Nested `FREEZE` 13/13 and `EVIDENCE` 30/30 rehash. Nested compiled manifests rehash 3/3 on each lane, including byte-identical inventories `884922fede59bc3540a61aa089a9ed92f65235b269330d63b9195afa69019297`.

Promotion-cited `a=8` pins rehash: RESULT `67e0c081…`, `EVIDENCE.sha256` `a3a64018…` (32/32), `FREEZE.sha256` `dcd6c3eb…` (10/10). Promotion-cited `a=9` pins rehash: grade-27 RESULT `3679d0db…`, its `EVIDENCE` `f878c18a…` (43/43) and `FREEZE` `be2a611f…` (7/7); collision RESULT `eb1b77e1…` and `FREEZE` `e4625f8e…` (9/9); grade-30 RESULT `bbb1d718…`, `EVIDENCE` `dc223883…` (46/46), `FREEZE` `6881229b…` (9/9).

The audit's overlapping `a>=13` pins also rehash and are overlap only: promotion `29e2ac114099a9d934ffd593ccf7157aca84ffc201b59fb312ddd80185a60386`, review `7a0676034b1c1b588a57d447b300568c49e026dfe22d68bb81d3c90f07b83250`.

No standalone `xmodel/*promotion*` artifact exists for `a=2..5` or for `a=6,7`.

An on-disk file

```text
xmodel/max12-812-order2-square-d1-age10-j38-order3-hostile-review-grok-20260826.md
```

rehashes to `a4eff964e517e9050191bba938cb3573e90c904c7bcf0d492cfe36fce0dd60a2` and prints CONFIRMED. It is **not** a named pin of this composition review, has **no** promotion artifact, and is **not** re-derived here. Charge 7 forbids importing a producer PASS as already promoted; the same firewall applies to that unnamed concurrent review.

A passing freeze is not a mathematical verdict. The algebra below is independent of those sentinels.

---

## 1. Unit-load lower hull and the unique-`AC`, `d=1` cell

The fan lemma is an affine weight arrangement after subtracting common absolute grade ten. The eleven displayed weights are taken as given candidate generators; this review does not re-prove that they exhaust the complete source expansion (the lemma's own firewall). Global dominance of `RAC`, `RC2`, and `kAC` is the three strict summands `+(2+r)`, `+(2+r)`, `+(4+q)`. Independently, `kR2A` cannot lie on a lower face: `kR2A-kR3=3+a-r` and `kR2A-kA2=2r-a-1` cannot be simultaneously nonpositive, because `r>=a+3` forces `kR2A-kA2>=a+5>0` and `a>=2r-1` forces `kR2A-kR3>=r+2>0`. A finite integral scan of `a,r>=0` and `q>=0` finds no counterexample.

On the unit-load horizontal domain `q=0`, `a>=1`, `r>=2`, `c>=3`,

```text
A3-kA2 = a+1 > 0,
RA2-kA2 = r-2 >= 0.
```

The ordinary lower envelope is therefore generated by

```text
AC=a+c,  C2=2c,  R3=3r,  RC=1+r+c,  A2=4+2a,
```

except that `RA2` is retained where it ties `A2`. Equality `r=2` together with `A2` being at most every function in the five-list forces `a=1` and `c>=5`. Conversely, every point `(a,r)=(1,2)`, `c>=5` has `RA2=A2=R3=6` and every other listed function at least six. That is the entire `RA2` lower-hull locus. It is disjoint from unique-`AC` `d=1`, which will require `a>=2` or else `c=2` (outside `c>=3`).

The five closed cells of the lemma are the pairwise comparisons of those five functions. An exhaustive integral scan of `1<=a<12`, `2<=r<16`, `3<=c<20` finds no uncovered domain point. Equalities are shared faces; unique-minimum interiors are the corresponding strict inequalities.

At an integral point where `AC` is *uniquely* minimal, strict comparison with `C2` and `A2` is `1<=d:=c-a<=3`. Strict comparison with `RC` is `s:=r-a>=0`. Strict comparison with `R3` is `a+3s>d`. These are strict: the closed `AC` cell includes the equality faces `d=0` (`AC=C2`), `d=4` (`AC=A2`), `s=-1` (`AC=RC`), and `a+3s=d` (`AC=R3`), which are **not** unique-`AC`.

For `d=1` the inequality `a+3s>1` is automatic on `a>=2`. The domain constraint `c>=3` excludes `a=1`, `c=2`. The constraint `r>=2` is then implied by `r>=a>=2`. Hence the entire normalized integral unique-`AC`, `d=1` cell on the registered domain is

```text
a>=2,  c=a+1,  r>=a.
```

Relative successor gaps at `d=1` are `C2: 1`, `A2: 3`, `RC: 1+s`, `R3: a+3s-1`, `RA2: a+s+1`, `A3: a+4`. All are strictly positive for `a>=2`, `s>=0`. `RC` meets the next grade only for `s=0`. `R3` meets the next grade only at `(a,c,r)=(2,3,2)`. Unique minimality of `AC` itself is never lost on this cell.

An exhaustive integral census of unique-`AC` points with `a<=15`, `r<=19`, `c<=24` produces a `d=1` set identical to the claimed cell, with empty symmetric difference. In particular:

- there is no unique-`AC` `d=1` point with `a=1`;
- there is no unique-`AC` `d=1` point with `r<a`;
- the exact-contact face `r=a` is included, starting at `(2,3,2)`, `(3,4,3)`, ….

First omitted integral unique-`AC` `d=1` point: **none**.

If the cell had been written with `r>a`, the first omitted point would be `(2,3,2)`. If it had been written with closed `AC` inequalities, the first extra `d=1` equality face would be the `AC=RC` family `s=-1`; the first such with `R3` also tying is `(4,5,3)`, while `(3,4,2)` is already unique-`R3` (`R3=6<AC=7`) and belongs to a residual face. Those points are correctly excluded from unique-`AC`.

Integral `ord_sigma` means ordinary DVR-arc orders, hence integers. The finite-band theorems are four and two fixed integer contacts; they are not a separately normalized rational-weight convention. Ramifying a hypothetical rational-weight `d=1` arc multiplies `d` by the ramification index and lands in another unique-`AC` family, not in this cell. The audit's refusal to enlarge `a=2..9` to rational weights is therefore mandatory, not optional. The `a>=10` producer claims ramified rationals by a homogeneous polynomial identity in `theta,eta`; that claim is part of the conditional tail, not of the finite bands.

---

## 2. Contact partition, `k10` versus `k0`, and `D(J)`

The integer interval `a>=2` is the disjoint union

```text
{2,3,4,5} ∪ {6,7} ∪ {8} ∪ {9} ∪ {a>=10}.
```

There is no integer hole. Each named band states `c=a+1` and `r>=a` on its chart, so the partition of `a` is a partition of (D1-AC1).

On the unit-load chart, `q=ord(k10)=0`, so `k10=k0+sigma k10_1+…` with leading jet `k0`. Invertibility of that series is invertibility of `k0`. Every finite-band compiler realises the `k10` load as the ring variable `k0`. The `a=9` theorem inverts `p*k0` explicitly. The two notations name the same open `D(k0)=D(k10)`.

The `a>=10` producer inverts `J` (Keller) after the registered square/D1 gates, which already live on `D(p*k10)`. The resulting chart is `D(p*k0*J)`, not the larger open `D(p*k0)`. Restricting a `D(J)` theorem to `D(p*k0*J)` is legitimate and is a restriction, not an extension. The audit's phrase that the tail “restricts to the same `D(p*k0)` chart” is campaign language after Keller `J!=0`; the largest common open on which the bands compose is `D(p*k0*J)`. Section 5 of the audit already writes that open before the naming gloss. The narrow composition theorem below uses `D(p*k0*J)` and does not pretend that `a>=10` is known on `V(J)`.

The promoted `a>=13` order-two theorem is emptiness of the same contact cone on `D(J)` for `a>=13` by a pole-order-at-most-two identity. Its own firewall and the `a=12` negative control (`k2*C/L^3` at grade 38) show that it does **not** fill `a=10,11,12`. It is overlap, not a routing assumption, and it does not discharge the `a>=10` condition.

---

## 3. `r>a` in every finite band, and the homogeneous tail

`a=2..5`. `R=sigma^a eta (b1 z+b0)` with `eta` a ring variable. Arbitrary `eta` is exact contact `r=a`; `eta=0` kills the grade-`a` section. The next `R` jet first produces `k10 R_1 C` at grade `13+2a=(g+1)+1` and `k10 R^3` at `>=13+3a>=g+3`. The CONFIRMED review re-derives that timing; `eta=0` is a finite truncation through `g+1`, not an unbounded `eta=sigma^s` substitution. Exact orders of `A` and `C` are the compiled powers `sigma^a`, `sigma^{a+1}` with nonzero linear leading forms after allocation.

`a=6,7`. The same truncation. Next `R` jet at `13+2a` after `g+1=12+2a`. Exact contact is the same power of `sigma`. The CONFIRMED review records this explicitly.

`a=8`. Same `R=sigma^8 eta (b1 z+b0)`. Next `k10 R_1 C` at grade 29, after the `V(k60)` window 27/28. `D(k60)` is already empty at grade 26 independently of `R`. `eta=0` is complete through the consumed grades.

`a=9`. The source substitution is `rz,rc=sigma^9(b1+…, b0+…)`. Leading `R` coefficients remain in the ring and may vanish, which is `r>9`. The in-window `k10 RC` term is grade 30 at `r=9` and later if `r>9`; it is retained rather than inverted. The promoted theorem is stated for all `r>=9`. No `eta` inversion occurs.

`a>=10`. The producer writes `R=sigma^{10} theta eta Rbar` with `eta` a free polynomial variable, not inverted. Substitution `eta=sigma^s` is a homogeneous shift. Raising `r` delays every inventoried family. This is the one band that uses an unbounded substitution, and it does so because the obstruction identity is polynomial in `eta`. Closed leading-coefficient faces of `A` and `C` are likewise included by not inverting `theta` (tied to both `A` and `C` at baseline). That is a strengthening of the exact-contact cell, not an omission of `r>a`.

Exact-contact hypotheses in the finite bands are opposite-root allocations of nonzero linear `A0,C0` on squarefree `L` (shifted by the in-window `k6` jet at `a=7,8`), together with the `a=9` Bezout equation of exact order ten. Those are exact-order statements. The tail is stronger.

---

## 4. Lower-load transitions

Orders used below are the binomial polar orders on the unit-`k10` chart with `ord(A)=a`, `ord(C)=a+1`, `ord(R)>=a`.

**No early `k6` at `a<=5`.** `k6 C/L` has order `18+a`. The two-grade window ends at `12+2a`. For `a=5` this is 23 against 22; for `a<=4` the gap is larger. `k6 R^2/L` is at `>=16+2a`, gap 4. `k2`, `mu2`, `mu4`, `mu6`, `J` all lie after `g+1` in this band. The CONFIRMED review charges 336 `diff` tests on the complete seven-row source, not an order table alone. There is no silent `k6` section.

**Complete `k60/k61` timing at `a=6,7`.** Windows `(23,24)` and `(25,26)`.

```text
a=6: U0 ; U1+KRC+S0          (k60 at grade 24; k61 out)
a=7: U0+S0 ; U1+KRC+S1       (k60 at 25; k61 at 26)
```

No inversion of `k60`. The `k60=0` specialisation is inside the ring. The CONFIRMED V2 review isolates the V1 fail-closed remainder as a `t` versus `t^2` alignment of the new analytic comparator, reconstructs V2 as exactly two token replacements, and retains the residue `(3/2)lambda^2 cv^2` including the `a=7` face `A0+k60≡0`.

**Exhaustive `D(k60)/V(k60)` at `a=8`.** Grade 26 is `S0=(3/4)k60 C0/L` on `D(k60)` and forces `C0=0`. On `V(k60)` the load is `sigma k61+sigma^2 k62`; `k61,k62` are free and may vanish. `k63 C/L` is at order 29, after grade 28. The promoted theorem and CONFIRMED review are arcwise: the two sections cover every finite-order `k6` jet, and identically zero `k6` is the specialisation `k61=k62=0` inside `V(k60)`. Intermediate valuation `0<v(k60)<∞` has generic point in the empty open `D(k60)` and is empty as an arc. This is not a scheme-theoretic initial ideal.

**Exhaustive `k60,k60_1` scheme split at `a=9`.** The promoted split is

```text
D(k60) ∪ (V(k60) ∩ D(k60_1)) ∪ V(k60,k60_1).
```

`D(k60)` is empty at grade 27 by `(3/4)c1 k60=(3/4)c0 k60=0`. On `D(k60_1)` after `V(k60)`, `e28z` forces `c1=0` and unrestricted `g30_4` forces `c0^2=0`; the exact-order-ten Bezout equation yields the unit ideal. On `V(k60,k60_1)` the compact ideal contains `c1 c0` and `2 c0^2-p c1^2` before radicals; on `D(p)` it contains `c0^3,c1^3`, and cubing Bezout yields `1=0`. A DVR point with `0<v(k60_1)<∞` (resp. `0<v(k60)<∞`) has generic point in the already empty open. Higher `k6`, delayed `k2/k10_1`, moving connection, and terminal targets are present in the complete source and first enter at grades `>=31`. This band is scheme-theoretic.

**All `k10_6,k6_10,k2_6` at `a>=10`.** The frozen compiler enumerates four binomial summands of `f^alpha` at baseline `A=10,C=11,R=10` through grade 38 and fail-closes unless the mechanical jet maxima equal

```text
A_7, C_10, R_6, k10_6, k6_10, k2_6, p_10, mu2_10, mu4_6, mu6_2.
```

Both compiled `result.json` files print those maxima and `primitive_family_count=11`. Independent grading of the four atoms at that baseline recovers the eleven polar families displayed in the producer RESULT, with the same coefficients, first grades, and pole orders: `k6 C/L` at 28, `AC/L` at 31, `k10 RC/L`, `k2 R/L`, `C^2/L^2` at 32, `k10 A^2/L` at 34, `k10 AC/L^2` and `k2 A/L^2` at 35, `k10 C^2/L^3`, `k2 C/L^3`, `k6 R^2/L` at 36. The first omitted polar family is `k6 RA/L^2` at 39 (pole 2). The first pole-order-four family is `k6 AC/L^4` at 43. Jet ceilings follow: earliest `k10` family remaining `38-32=6`, earliest `k6` remaining `38-28=10`, earliest `k2` remaining `38-32=6`, earliest `A` remaining `38-31=7`. No load coefficient is inverted. Whether the odd-row identity `(R3)` and the unit-ideal argument on `D(J)` hold is exactly the live `a>=10` review, not this review.

There is therefore no remaining `k6`-valuation or delayed-load section *inside* (D1-AC1) once the `a>=10` producer theorem is granted. Positive-order leading load `ord(k10)>0` is a different fan (`A3` can enter; `RA2-kA2=r-2-q` changes sign) and remains outside.

---

## 5. Common upstream hypotheses and theorem types

Every named band assumes the already reviewed generic-square first-normal, half-weight, and `M=0` gates. Those gates are imported, not re-proved: first-normal Padé support promotion `40790378…`, third-tail sharp `M=0` promotion `dfc44850…`. They place the argument on `D(p*k10)` after the square reduction and after the sharp third tail has forced `M=0`. Characteristic zero is the exact-Q endpoint in every band; `F_65521` is a software control.

Theorem types, read from the named reviews and promotions rather than from the audit's one-line table:

| band | type | chart |
|---|---|---|
| `a=2..5` | arcwise / set-theoretic | `D(p*k10)` |
| `a=6,7` | arcwise / set-theoretic | `D(p*k10)` |
| `a=8` | arcwise / set-theoretic | `D(p*k10)` |
| `a=9` | scheme-theoretic unit ideal, no radicals | `D(p*k0)` |
| `a>=10` (producer claim) | scheme-theoretic unit ideal after `iJ*J-1` | `D(J)` |

Arcwise emptiness of some bands and scheme-theoretic emptiness of later bands compose to arcwise emptiness of the union. They do **not** automatically give reduced scheme structure of the source ideal on the whole cell: embedded components, multiplicities, and nilpotents in the `a=2..8` opens are not controlled. The `a=8` split `D(k60)∪V(k60)` is exhaustive for arcs, not a statement that the ideal is radical. A future composition promotion that writes “the cell is a reduced empty scheme on `D(p*k0*J)`” would be a strengthening and would be false as an inference from these constituents.

The Pell/Chebyshev all-load survivor is compatible throughout: it lives off the unit-`k10` square when `k6` and `k2` are comparable to `k10`. Finite early-grade emptiness on `D(p*k0)` does not contradict that locus.

---

## 6. Missing standalone promotions for `a=2..5` and `a=6,7`

The two hostile reviews rehash to the charged SHAs and both finish `CONFIRMED`:

```text
e03de4e1fc1816a7141c6bb8060b4a75c2a6b5a08ea4d56ca63582b875cad335
  xmodel/max12-812-order2-square-d1-finite-band-a2-a5-hostile-review-grok-20260826.md
3e601cf34eb23270daa067794087155b7179607d27af01f84a60624447f949e3
  xmodel/max12-812-order2-square-d1-load-transition-a6-a7-v2-hostile-review-grok-20260826.md
```

No `xmodel/*promotion*` artifact exists for either band. The audit already records this. It is not an interval gap and not a mathematical omission of `(a,c,r)`.

Campaign practice for `a=8`, `a=9`, and `a>=13` is: CONFIRMED review, then a promotion artifact that freezes the theorem statement and the review SHA, then any later composition. A single final composition promotion that imported these two reviews directly would be the *first* promotion of two bands, mixed with already-promoted `a=8` and `a=9`. That hides promotion-layer status.

**Decision.** Two narrow promotion artifacts must be written before a composition promotion. Each must quote the corresponding CONFIRMED theorem verbatim (arcwise emptiness of the listed contacts on `D(p*k10)`, no scheme upgrade, no enlargement of `a`, no rational-weight extension) and must cite the exact review SHA above. Direct import of the reviews into a composition promotion without those artifacts is rejected as lifecycle irregular, even though it would not by itself create a new mathematical identity.

This finding does not change the coverage of (D1-AC1) and is not a `REPAIR` of the frozen audit.

---

## 7. Frozen `a>=10` producer: inspect, do not promote

The producer RESULT status is `DUAL-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW`. Its firewall says promotion requires fresh hostile review. This composition review does not convert that PASS into a theorem.

Independent inspection, limited to what is required to condition the composition:

1. The stated cone is exactly `a>=10`, `c=a+1`, `r>=a` on `D(J)` after the registered square/D1 gates. Scope string: `UNIFORM_A_GE_10_C_EQ_A_PLUS_1_R_GE_A_D_J_LITERAL_SOURCE_ONLY`. That is the missing piece of the partition, not a different cell.
2. The compiler is pinned at `9f0184b1007103478381c474ce6e4c1802ed8a53ab23dee79e7dd77518e0168e`. It fail-closes off Amazon Linux, rechecks the frozen `a>=13` parent, enumerates primitives from four binomial summands rather than a handwritten wall, and fail-closes unless jet maxima match the mechanical inventory. Both lanes print inventory SHA `884922fe…` and require live grade-38 `A_7` and `k10_6`.
3. The eleven primitive families and the jet list `k10_6,k6_10,k2_6` recompute from the binomial grading as in §4. No load is inverted. Homogeneous coverage is by not inverting `theta,eta`.
4. The obstruction is the odd-row identity of pole order at most three plus the unique odd target `-sigma^{38} J/4`, giving the unit ideal on `D(J)` before radicals. Whether that identity is correctly derived from the frozen Faber matrix, whether even targets are truly invisible to it, and whether the Laurent emitter is independent of a shared omission, are charges of the separate `a>=10` review. They are not discharged here.
5. The `a>=13` order-two theorem is a different annihilator and a different pole ceiling. The producer correctly treats it as overlap and records the incomplete `A_3,k10_1` draft as no-verdict.

Therefore the composition is **at least** conditional on independent hostile confirmation of this producer for the cone it states. It is not confirmed by the producer PASS, and it is not confirmed by an unnamed concurrent review file.

---

## 8. Residual list: this is not whole D1

The composition, even after the `a>=10` condition, closes one fan cell only. The following remain outside unless separately promoted:

1. The other unique-`AC` families: `d=2` with `s=0,1,>=2` and `d=3` with `s=0,>=1`, plus the small-`a` equality boundaries visible in the successor gaps (including `d=4` `AC=A2` faces such as `(1,5,r)`).
2. Primary `C2`, `R3`, `RC`, and `A2` lower faces and all equality intersections, including the exceptional `RA2=A2=R3` locus `(a,r)=(1,2)`, `c>=5`, and the `d=1` equality face `(4,5,3)` (`AC=R3=RC`) together with the `AC=RC` family `c=a+1`, `r=a-1` for `a>=5`.
3. The `a=1` charts, including `(1,3)` and `(1,4)` `AC` and the separate `r=1` receiver. Normalized `r=1` having a distinct CONFIRMED result does not remove these faces.
4. Positive-order leading load `ord(k10)>0`, where `A3` can become minimal and the five-weight unit-load fan is invalid.
5. `p=0`, `k0=0`, the exact-square zero section, zero/infinity receivers, terminal/Taylor landing, and other lifecycle charts.
6. Global source landing/coverage needed to transport every hypothetical counterexample into this local fan.

Beyond D1: the whole square component, nonsquare/Pell receiver, exact order two, `(8,12)`, maximum twelve, and JC2 remain separate campaign obligations. Calling this composition “D1 is closed” is forbidden.

---

## Narrowest legitimate composition theorem

After the reviewed generic-square first-normal, half-weight, and `M=0` gates, and **subject to independent hostile confirmation and promotion of the frozen `a>=10` producer** `2ccfdfe9…` / `60b2e1d5…` for the cone it states, there is no finite-order normalized DVR arc on `D(p*k0*J)` with integral

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,  ord_sigma(R)>=a,  a>=2.
```

Equivalently: the normalized integral unique-`AC`, `d=1` unit-load cell (D1-AC1) is empty on that open, as an arcwise/set-theoretic statement.

This is not reduced scheme structure of the cell. This is not whole D1. This is not a statement on `V(J)`, `V(p)`, or `V(k0)`.

---

## Lifecycle steps required before promotion

The frozen audit is not a promotion. A composition promotion may be written only after all of the following, in order:

1. Write two narrow promotions
   - `a=2..5` citing review SHA `e03de4e1fc1816a7141c6bb8060b4a75c2a6b5a08ea4d56ca63582b875cad335`, restating arcwise emptiness of `ord(A)=a`, `ord(C)=a+1`, `ord(R)>=a`, `a in {2,3,4,5}` on `D(p*k10)`;
   - `a=6,7` citing review SHA `3e601cf34eb23270daa067794087155b7179607d27af01f84a60624447f949e3`, restating arcwise emptiness of the two listed contacts on `D(p*k10)`.
   Neither promotion may upgrade those theorems to scheme structure or enlarge their contacts.
2. Independently hostile-review the frozen `a>=10` producer (RESULT `2ccfdfe9…`, PRODUCER_FREEZE `60b2e1d5…`) and, if CONFIRMED, write its promotion for `a>=10,c=a+1,r>=a` on `D(J)` after the same gates. Do not treat the producer PASS, or the unnamed on-disk review SHA `a4eff964…`, as that promotion.
3. Then write the composition promotion that imports only promoted theorems, states the narrow theorem of the previous section, records theorem types by band, and repeats the residual list of §8.

No other file is required to repair the frozen audit. The audit's routing of (D1-AC1) is correct; the composition *theorem* is conditional on step 2; the composition *promotion* is blocked on steps 1–3.

---

CONFIRMED_CONDITIONAL
ORDER2_SQUARE_D1_UNITLOAD_CONTACT_LADDER_COMPOSITION_CONFIRMED_CONDITIONAL
