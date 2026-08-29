# Hostile review: V47 fail-closed direct three-row linker

| Field | Value |
|---|---|
| Charged target | V47 fail-closed direct three-row linker |
| Reviewer / model | Grok 4.6 (xAI). Independent different-model adversarial desk review |
| Method | SHA-256 of every charged file and every V47-consumed pin before any producer `PASS` line was treated as evidence; unmodified in-process replay of `verify_three_row_linker.py` with no output write; independent `Fraction` sparse expansion of `AC/L` and even `C^2/L^2`; four syzygies; radical/unit-ideal/ramified-fibre countermodels; `Inv1` series recurrence with moving `P`; independent four-atom aggregated enumerator (not the producer `own_inventory`, miner not sole authority), cancelled-family trap, pad `+1`; wall-derived 12+4 list; monotonicity; eight negatives; local-versus-global pole attack; generated-map/factor audit; mutation live-fire. Producer `PASS-GATE-T-STRICT-UAC-THREE-ROW-LINKER-V47`, schema status tokens, and prior review `CONFIRMED`/`PASS` labels were assertions to attack, not evidence |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` (charged files are untracked relative to that commit; custody is the assignment SHA-256) |
| Date | 2026-08-27 |

Independently recomputed SHA-256 of the six charged files match the review assignment. Every V47 `source_pins` and `endpoint_authorities` pin rehashes. The producer verifier was rerun in this session **without** writing into `run_v0_v9/`; the Python object it compared to frozen `result.json` is identical (exit 0, internal `json.loads(frozen) != result` did not fire). No file other than this review was written. No frozen producer artifact, canonical ledger, AWS job, heavy CAS, web sweep, or `jc2-lean` tree was entered or modified. `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`; no `__pycache__` or `.pyc` remains.

This review does **not** replace any promoted D1 endpoint, does **not** promote `(a,d,r)=(8,3,8)`, and does **not** conclude Gate T, order two, maximum twelve, either global `G2-PSC`/`G2-BD`, JC2, or a counterexample.

---

## Verdicts

| # | Mandated attack | Verdict |
|---|---|---|
| 1 | Custody and freeze | **CONFIRMED** |
| 2 | Independent algebra | **CONFIRMED** |
| 3 | Independent polar census | **CONFIRMED** |
| 4 | Contact derivation and closed tails | **CONFIRMED** |
| 5 | Manifest completeness / literal-row bridge | **GAP/REPAIR** |
| 6 | Mutations | **CONFIRMED** (three string-only pins flagged) |
| 7 | Transport direction and scope | **CONFIRMED** |
| 8 | Promotion / allocation-step replacement | **GAP/REPAIR** |

**Smallest failing identity:** none of the four syzygies, none of the sixteen inventory hashes, none of the eight negatives.

**Smallest failing hypothesis:** that a SHA-256 of a promoted D1/D23 endpoint report, plus the schema strings `Phi1=h1`, `Phi2=h2`, `Phi4=h4+(P/2)*h2`, is a coefficient comparison of `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]` to `(g1,g2,g4)`. It is not. The D1 finite-band and low-`a` `d=2,3` endpoints prove emptiness by allocating opposite roots of `L` and evaluating `N(lambda)=(3/2) lambda^2 cv^2`. That is a different obstruction. Hashing those markdown files does not extract the three g-coefficients from the emitter or from any chamber compiler.

**Smallest repair:** per-manifest executable extraction of `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]` from the frozen V46 seven-emitter (569 tails on `F0..F6`) at generic shifted leading jets, polynomial equality to `(g1,g2,g4)`, and vanishing of every extra in-window jet in those three slots. Retain endpoint hashes only for localization and theorem-type inheritance. Do not treat prose provenance as that comparison.

**Exact V47 scope after this review: not eligible to replace the moving-root allocation step.** Algebra, global-pole census, derived 12+4 list, monotonicity, negatives, generated `2,4` leading-jet maps, and V0/V1/V3/V4-only transport direction all hold. Replacement stays withheld until the coefficient bridge is executable.

---

## 0. Custody of the six charged artifacts

Recomputed SHA-256, all matching the assignment:

```text
b1770cc0254098343c27600136f0ec1d95084623a4f48eed5216409106703ab2
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/SCHEMA.json
070d5a96627ac300f87791b9386e809de21b52317581b01731cde5dc55c7ecaa
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/GENERATED_MANIFESTS.json
903c6932a53ec5c0a1d2f7e7a7266135131fdc23512e8562f2b5b36ff20c0111
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/verify_three_row_linker.py
a8be0c67b113f0c92e077fc2ff3ef591edee6b859f2e83ed1abca38ec44c367b
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/run_v0_v9/result.json
e53dd54948f5f67c855ddde8bc705f67b24c9e384aec269269d446c40a449871
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/RESULT.md
6ad0ac3f496a7ec67247494dd536fcc1508642b44d22e8147c4406df02f04774
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/FREEZE.sha256
```

`FREEZE.sha256` contains exactly those five producer files (schema, generated manifests, verifier, `result.json`, `RESULT.md`) and matches each recomputed digest. `RESULT.md` lists the first four of those five and does not hash itself or the freeze; that is the correct freeze split.

Relevant charged interfaces, also matching:

```text
2354703a559a5da2b4f2032560a5740b2cda1f3160f5c6598dcdbe1c4c1432be
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-sol-20260827.md
591049f064bbedbfd8ddf9482e94fa76257543c56115cf8322d2831c52b4f004
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-hostile-review-grok-20260827.md
13450b727aad5a27f40ba22333b91b03765009a41de8aa36c330a5cd02347e71
  xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46-hostile-review-grok-20260827.md
a2a6a5e204b78485509a314b71bd8ab877ea4cdd9dbad8f2af637b0d753614ac
  xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46r1-hostile-review-grok-20260827.md
b862e00f6ac80c3392cd365aad5d7001608e2a75fabfa4a76bb2f4c751e1f0fc
  xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46r1-promotion-sol-20260827.md
```

V46R1 is a charged comparator for the unused mixed `V2` root display. V47 does not pin it and does not contain `shifted_root` or `check_shifted_root`. That is the correct consumption split.

---

## 1. Custody and freeze — CONFIRMED

### 1.1 Every consumed pin

| Pin | Recomputed | Match |
|---|---|---|
| lemma sol | `2354703a…c1432be` | yes |
| original replay | `56edb06f…b2c5c3f4` | yes |
| syzygy Grok review | `591049f0…52b4f004` | yes |
| support miner | `0e94e540…9952fe9a` | yes |
| tails.json byte | `d72f774c…3813848` | yes |
| tails.json canonical | `6eed03d4…ce387e8` | yes |
| tail emitter | `77f25216…f90dcdc` | yes |
| V46 SCHEMA.json | `796eb084…8b02673` | yes |
| V46 FREEZE.sha256 | `b39f66e2…187ae22` | yes |
| V46 Grok review | `13450b72…02347e71` | yes |
| D1_A2_A5 authority | `973f7953…922d6d1` | yes |
| D1_A2_A5 review | `e03de4e1…75cad335` | yes |
| D1_A6_A7 authority | `829ac12f…605ea0f` | yes |
| D1_A6_A7 review | `3e601cf3…47f949e3` | yes |
| D23_LOW_A6 authority | `8b92c22b…3362864da` | yes |
| D23_LOW_A6 review | `841f0d6c…0592a3` | yes |
| V45 corroboration (optional pin) | `99d32a77…031ba29` | yes |

Tails row census independently `[36, 54, 58, 81, 89, 120, 131]`, sum **569**. V46 freeze inner lines rehash against `SCHEMA.json`, `verify_uniform_naturality.py`, `RESULT.md`, and `run_v0_v4/result.json`. Uniform schema `tails.byte_sha256` equals V47's tails byte pin. Uniform `semantic_witnesses` role `tail/load/target emitter` equals the emitter pin. Consumed-scope string is exactly `V0,V1,V3,V4 only; V2 shifted-root maps are not consumed`.

**Weak pin, not a gap.** V47 hashes the V46 freeze file and the V46 schema file, and does not re-walk the freeze inner lines. Those inner lines nonetheless match the files on disk.

### 1.2 Unmodified replay

Command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/verify_three_row_linker.py
```

Exit 0. Printed object has `status=PASS-GATE-T-STRICT-UAC-THREE-ROW-LINKER-V47`, `manifest_results_sha256=c2c300e610be134c59d42a02111d679bb1d8db0f3e6b0416949888e112332716`, twelve mutations, eight negatives, `independent_inventory_coefficient_count=71`, `uniform_scope_consumed=V0,V1,V3,V4; no V2 shifted-root map`, `endpoint_replacement_status=WITHHELD_PENDING_DIFFERENT_MODEL_REVIEW`. The verifier compares the live dict to `json.loads(run_v0_v9/result.json)` and would have raised `frozen result mismatch`. It did not. No file in `run_v0_v9/` was written.

Miner `main()` is AWS-gated and was not run. `enumerate_primitives` is ordinary Python and was imported only by the producer replay, not as this review's census authority.

**Custody/freeze: CONFIRMED.**

---

## 2. Independent algebra — CONFIRMED

Work in `Z[1/6][X0,X1,Y0,Y1,rr]` with names deliberately different from the verifier (`A0c,A1,C0c,C1,rho`). Chart:

```text
L : zz^2 = rr^2,
A0 = X1*zz + X0,
C0 = (Y1*zz + Y0)/2.
```

### 2.1 `AC/L` remainder

Unloaded two-atom family `A+C`: `binom(3/2,2)*2 = 3/4`. Numerator `(3/4) A0 C0`, reduce `zz^2 -> rr^2`:

```text
A0 C0 = (X1 Y1 rr^2 + X0 Y0 + (X1 Y0 + X0 Y1) zz)/2.
```

Times `3/4`:

```text
[zz]     = (3/8)(X0 Y1 + X1 Y0) = g1,
[const]  = (3/8)(X0 Y0 + rr^2 X1 Y1) = g2.
```

Independent sparse engine, monomials as sorted exponent tuples, coefficients `Fraction`: both dictionaries equal the displayed polynomials. Dropping the chart factor `/2` on `C0` replaces `3/8` by `3/4`.

### 2.2 Symmetric `C^2/L^2` even combination

Unloaded two-atom family `C+C`: `binom(3/2,2)=3/8`. `C0(±rr)=(± Y1 rr + Y0)/2`, so

```text
N(±rr) = (3/32)(Y1^2 rr^2 ± 2 Y1 Y0 rr + Y0^2),
[N(rr)+N(-rr)]/2 = (3/32)(Y0^2 + rr^2 Y1^2) = g4.
```

Match. The extra `4` in the denominator is the square of the chart factor. Displayed coefficients `3/8, 3/8, 3/32` are therefore forced, not optional normalizations.

### 2.3 Four syzygies

Set `D = rr^2 Y1^2 - Y0^2`. Direct expansion, four empty dictionaries:

```text
Y1*g2 - Y0*g1                 =  (3/8) X1 D,
Y0*g2 - rr^2 Y1*g1            = -(3/8) X0 D,
(32/3)*g4 + D                 =  2 rr^2 Y1^2,
(32/3)*g4 - D                 =  2 Y0^2.
```

Mutations: `g1` scale `3/8 -> 3/4` makes identity 1 the nonzero polynomial `(-3/8)(X0 Y0 Y1 + X1 Y0^2)`; `g4` scale `3/32 -> 3/16` makes identity 3 the nonzero polynomial `Y0^2 + rr^2 Y1^2`.

### 2.4 Localization / radical / what is not true

Let `I=(g1,g2,g4)`. Identities 1–2 put `X1 D` and `X0 D` in `I`. After inverting `X1` (resp. `X0`), `D` lies in the localized ideal. Identities 3–4 then put `Y0^2` and `rr^2 Y1^2` in that localization. After inverting `rr`, `Y1^2` does too. Hence

```text
Y0, Y1  in  radical(I[rr^{-1}, X0^{-1}])
and
Y0, Y1  in  radical(I[rr^{-1}, X1^{-1}]).
```

Set-theoretically, on `D(rr) ∩ (D(X0) ∪ D(X1))`, `g1=g2=g4=0` forces `Y0=Y1=0`. Combined with exact nonzero leading `A` this contradicts exact nonzero leading `C`. Over a domain, in particular a DVR arc, `C^2=0` implies `C=0`.

**Unit-ideal overreading, refuted.** `I` is not the unit ideal: the locus `Y0=Y1=0` with `X,rr` free is a zero of all three generators. After localization the ideal contains the squares `Y0^2`, `Y1^2`, not `1`. Schema `scheme_unit_ideal=false` is the correct strength.

**Inverted factors, all of them:** `2` and `3` (from `3/8` and `32/3`), `rr`, and exactly one of `X0`,`X1`. No leading `C`, no `k10`, no `J`, no Hensel root, no deck sign. `Z[1/6]` suffices.

**Load-bearing countermodels, independently evaluated.**

- `X0=X1=0`, `Y0=1`, `Y1=0`, `rr=1`: `g1=g2=0`, `g4=3/32 ≠ 0`. Exact `A` is necessary; with `A=0` the pair `g1,g2` vanishes identically and `g4` only forces the even combination of `C0(±rr)`.
- `rr=0`, `X0=0`, `X1=1`, `Y0=0`, `Y1=1`: all three `g` vanish and `Y1 ≠ 0`. The ramified fibre is not covered.
- Shared-root `Y0=rr Y1` with `g4` dropped: identities 1–2 only recover `D=0`. At `rr=Y0=Y1=X1=1`, `X0=0` one has `g1=g2=3/8 ≠ 0` once `g4` is present; without `g4` the old allocation lemma is not `C=0`. All four identities are used.

No root allocation is used. Schema `root_allocation_used=false` and `allocation_local_pole_bit=forbidden` match the lemma that was actually proved.

### 2.5 Full moving-`P` simple-pole cancellation

`Inv1 = (1+(P/2) t^2)^{-1}` as an even series in `t`, coefficients series in `sigma`. Write `P = p0 + p1 sigma + p2 sigma^2 + ···`. Recurrence `v_0=1`, `v_{m+1}=-(P/2) v_m` in the `sigma`-series ring. Truncation to `sigma`-degree `<6` with generic `p0,p1,p2`: `v2 + (P/2) v1` is the zero series, and `v1` contains moving `p1,p2` terms. Therefore for a simple pole `H = N_s * Inv1` with `deg_z N_s < 2`,

```text
Phi4 := h4 + (P/2) h2 = 0
```

identically, as a polynomial identity of jets, with the full moving `P`, not frozen `p0`. Equivalently, rewritten over `L^2` a simple pole has numerator `N_s L`, which vanishes at both roots of `L`.

This licenses pole-one loads and moving connection jets cancelling from `Phi4` rather than being set to zero. It does **not** license them in `Phi1[G]` or `Phi2[G]`.

**Method note, not a gap in the algebra.** The verifier implements

```text
h4 = pscale(-1/2, pmul(P_full_series, h2));
assert padd(h4, pscale(1/2, pmul(P, h2))) == 0
```

That defines `h4` to be the cancelling term and checks `X+(-X)=0`. It is not a derivation from `Inv1`. The identity is nevertheless true, and was re-proved here from `Inv1` with moving `P`. The schema string `Phi4=h4+(P/2)*h2` is the correct row, not `h4`.

**Independent algebra: CONFIRMED.**

---

## 3. Independent polar census — CONFIRMED

Generating function, first principles, not copied from `own_inventory`:

```text
x = 2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 A/L^3 + sigma^5 C/L^4,
```

four atoms of `sigma`-costs `(2,4,5,5)`, `L`-denominators `(2,4,3,4)`, R-atom scalar `2`; four binomial summands `alpha in {3/2, 5/4, 3/4, 1/4}` with extra delays `0,4,12,20`. Aggregation key `(summand, load, fixed, R, A, C, pole)`. Pad `+1` on every atom bound.

### 3.1 Cancelled-family trap

Unloaded `R^2 C`, same key `(fixed,R,A,C,pole)=(9,2,0,1,2)`:

| Atomization | `binom * multi * scalar` |
|---|---|
| `R2+C` (deg 2) | `(3/8)*2*1 = +3/4` |
| `2R+C` (deg 3) | `(-1/16)*3*4 = -3/4` |

Sum `0`, family omitted. Independently also cancelled at `(2,3,2)`: unloaded `R^2 A` (pole 1) and unloaded `R^4` (pole 2, three atomizations `+3/8, -3/4, +3/8`). The `R^4` cancellation is load-bearing for `A2D1`: without it a second double pole would sit at `T_C2=16` and the first baseline would fail. Pad `+1` stable on every tested cell.

### 3.2 Sixteen hashes, coefficients, global pole, both walls

Canonical digest `sha256(json.dumps(inv, sort_keys=True, separators=(',', ':')))`. All sixteen match the schema pins. Sum of lengths **71**, matching frozen `independent_inventory_coefficient_count`. Every cell: unique primitive through `G` is unloaded `AC/L` coefficient `3/4` at grade `G`; unique pole-`>=2` primitive through `T_C2` is unloaded `C^2/L^2` coefficient `3/8` at grade `T_C2`; `G<28`, `T_C2<32`; pad `+1` equal.

Selected inventories (independent enumerator):

```text
A2D1  (G,T)=(15,16):
  AC  3/4 @15 pole 1;  C2 3/8 @16 pole 2;
  k10 R^3 5/16 @16 pole 1;  k10 RC 5/8 @16 pole 1
A6D1  (23,24):
  AC  3/4 @23;  C2 3/8 @24;
  k10 RC 5/8 @24 pole 1;  k6 C 3/4 @24 pole 1
A6D3  (25,28):
  AC  3/4 @25;  C2 3/8 @28;
  pole-one k10 R^3, k10 RC, k10 A^2, k6 C, k6 R^2, k2 R @28
A1D2_R3 (14,16): AC 3/4 @14; C2 3/8 @16; k10 A^2 5/32 @16 pole 1
A2D3_R5 (17,20): AC 3/4 @17; C2 3/8 @20; k10 A^2 5/32 @18 pole 1
```

Purity predicate is **global** pole, not `local_pole_upper_at_A_root`.

### 3.3 Allocation-predicate overreading, live and rejected

The miner's `SAFE_C2_ONLY` bit subtracts allocated `A`-zeros from the pole. Independently:

| Cell | Global | Local non-`C^2` pole `>=2` |
|---|---|---|
| `(a,d,r)=(2,3,3)` i.e. `(a,c,r)=(2,5,3)` | `RA2` at 19, coeff `-3/8` | **empty** |
| `(2,3,4)` i.e. `(2,5,4)` | `RA2` at 20 | **empty** |
| `(1,2,2)`, `(3,3,4)`, `(4,3,4)` | `RA2` | **empty** |
| `E` at `r=20` | `A3` at 18, coeff `-1/16` | **empty** |

Local pole would accept every named `RA^2` wall and the persistent `E` subtail. Those are exactly the cells the three-row lemma must refuse. V47 rejects all of them on global pole. Schema `allocation_local_pole_bit=forbidden` is implemented, not decorative.

**Independent polar census: CONFIRMED.**

---

## 4. Contact derivation and closed tails — CONFIRMED

Closed forms, then checked against the enumerator, not against a hardcoded twelve-set:

```text
G      = 10+a+c = 10+2a+d
T_C2   = 10+2c
s_min  = 1 if a<=d else 0
r_fl   = a+s_min
strict unique-AC floor: r>=2 and a+3 s_min > d
RA^2/L^2 : grade 12+r+2a, coeff -3/8, enters T_C2 iff r <= 2d-2
A^3/L^3  : grade 15+3a,   coeff -1/16, enters T_C2 iff a <= 2d-5
k6 C/L   : grade 17+c, pole 1; ties G iff a=7
k2 R/L   : grade 22+r, pole 1
k2 A/L^2 : grade 25+a, pole 2
mu2 in Phi2 at 28; mu4 in Phi4 at 32
```

Eligibility is monotonic in `r` at fixed `(a,d)`: raising `r` only delays `R`-bearing families; `G` and `T_C2` are independent of `r`; `A^3` and `k6 C` do not depend on `r`. Independently, on every accepted manifest, every `r` in `[r_min, r_min+11]` stays pure and every `R`-free signature is invariant. A threshold `r` is therefore a complete closed subtail.

### 4.1 Twelve baselines, derived

Registered tails in the box `a=1..6`, `d=1,2,3`, `c>=3` that pass global purity:

```text
d=1, r=a :  (2,1,2), (3,1,3), (4,1,4), (5,1,5), (6,1,6)
d=2      :  (2,2,3), (3,2,3), (4,2,4), (5,2,5), (6,2,6)
d=3      :  (5,3,5), (6,3,6)
```

Twelve, equal to the schema set (including `G,T`). Not accepted because typed twice.

### 4.2 Four first recovered raised thresholds, derived

Among rejected `a<=4`, `d=2,3` registered tails, first `r` that passes:

```text
(1,2): r=2 fails (RA^2 at 16=T); r>=3 admits
(2,3): r=3,4 fail; r>=5 admits          <-- (a,c,r)=(2,5,r)
(3,3): r=4 fails (RA^2 at 22=T); r>=5 admits
(4,3): r=4 fails (RA^2 at 24=T); r>=5 admits
(1,3): no r admits (A^3 at 18=T for every r)
```

Schema raised set `{(1,2,3,3),(2,3,5,5),(3,3,6,5),(4,3,7,5)}` matches. `E` never recovers: at `r=20` the only remaining pole-`>=2` non-`C^2` family is `A^3`.

**The `(2,5,r)` decision, exactly.** `G=17`, `T_C2=20`, `RA^2` grade `16+r`:

| r | RA^2 | in window? | eligible |
|---|---|---|---|
| 3 | 19 | yes, `-3/8` | **NO** |
| 4 | 20 | yes, at `T_C2` | **NO** |
| >=5 | >=21 | no | **YES** |

Current `(2,5,>=3)` is not wholly a three-row contact. `r=3,4` still need a certificate that retains `RA^2`.

At `r_min-1`, every one of the sixteen accepted cells fails (raised cells by `RA2`; d=1 baselines by `NONUNIQUE_G` from an earlier `R`-family). The registered floor is sharp.

### 4.3 Eight negatives

| Control | Independent reasons | Expected |
|---|---|---|
| `A1D2_R2` | `RA2` at 16, coeff `-3/8` | `RA2` |
| `A2D3_R3` | `RA2` at 19 | `RA2` |
| `A2D3_R4` | `RA2` at 20 | `RA2` |
| `A3D3_R4` | `RA2` at 22 | `RA2` |
| `A4D3_R4` | `RA2` at 24 | `RA2` |
| `E` at `r=20` | `A3` at 18, coeff `-1/16`, `r`-free | `A3` |
| `A7D1` `r=7` | `NONUNIQUE_G`: `k6 C` ties `AC` at `G=25` | `NONUNIQUE_G` |
| `A9D3` `r=9` | `k2 R` `1/2` at 31=`G` (pole 1); `k2 A` `1/4` at 34=`T` (pole 2); `G=31>=28`; `T=34>=32` | `K2_OR_TARGET` |

The last cell is a genuine `k2`/target cell, not a synthetic wall. Dropping uniqueness at `a=7` would pass: `k6 C` is pole one, so `Phi4` still cancels it, while `Phi1[G],Phi2[G]` become coefficients of `C(A+k60)`. Uniqueness is load-bearing.

`(8,3,8)` is not in the manifest. Independent purity: `NONUNIQUE_G`, `G_TARGET_WALL` (`G=29`), `T_TARGET_WALL` (`T=32`). It is not a three-row contact.

D23's eleven registered tails are `(1,2,2),(2,2,3),(2,3,3),(3,2,3),(3,3,4),(4,2,4),(4,3,4),(5,2,5),(5,3,5),(6,2,6),(6,3,6)`. V47 takes seven of them as baselines and the other four as raised subtails `r>=3` or `r>=5`. The impure prefixes stay with the allocation endpoints.

**Contact derivation: CONFIRMED.**

---

## 5. Manifest completeness — GAP/REPAIR

### 5.1 What is present and correct

- Tuple fields `a,d,c,r_min` with `c=a+d`; unlabelled triples rejected (`validate_manifest_shape((2,3,2), schema)` fires). Hard-reject `(a,c,r) in {(2,5,3),(2,5,4)}`.
- `G=10+a+c`, `T_C2=10+2c` on every manifest.
- Sixteen inventory hashes match the independent enumerator.
- Generated total names `az_a, ac_a, ez_c, ec_c, cs_r, rs_r` and D1 images `AzD1_0, AcD1_0, 2*CzD1_0, 2*CcD1_0, BzD1_0, 4*BcD1_0`. Factors `2` on both C jets and `4` on `rs` are the V46 jet-reindexing cancellations against `/2` in `N1,N0` and `/4` in `Rtot`. `cs -> Bz` is unscaled.
- Shifted names `A0c,A1,C0c,C1`; forbidden stage-zero `{a0,a1,c0,c1,rs,cs}` do not occur as D1 images. Equation names split `g-triple-v1` vs `emitter-7-v1`.
- `row_origin=general_rho_literal_Phi`; `rho0_face_as_general_rho` is forbidden.
- Per-manifest `authority_sha256` / `review_sha256` equal the resolved endpoint record.
- Localization retained: `D(p*k10)` on every `d=1` manifest, `D(p*k0)` on every `d=2,3` manifest. Direct lemma open `D(rho) ∩ (D(A0c) ∪ D(A1))` never removes those chart factors.
- Theorem type always starts `arcwise/set-theoretic`. `scheme_unit_ideal=false`. Reverse transport forbidden.

### 5.2 The gap: endpoint hash is not a coefficient comparison

Lemma condition 4 requires a reviewed literal-row bridge identifying `Phi1,Phi2,Phi4` with the total seven-tail emitter after the contact shift, and the extracted coefficients equal to `(g1,g2,g4)`.

What V47 actually does:

1. Pins the strings `Phi1=h1`, `Phi2=h2`, `Phi4=h4+(P/2)*h2`.
2. Expands `A0 C0 mod L` and the even `C^2` combination as standalone polynomials (real, §2).
3. Hashes three endpoint promotion/review markdown files per family.
4. Stores leading-jet alias names.

What V47 does **not** do (string search of the verifier): no `Phi1[G]`, no `assemble_f`, no `row_series`, no `source_block`, no `compile_r1`, no contraction of `tails.json`. It never evaluates the frozen 569-tail emitter, and it never reads a chamber compiler.

The hashed D1 finite-band promotion states the obstruction as: the first simple-pole equation forces two opposite-root allocations of linear `A0,C0` along `L=z^2+p/2`; the next double-pole numerator is `(3/2)*lambda^2*cv^2` at the allocated `A` root. The hashed D23 promotion states the obstruction as the moving-root functional `Phi4+lambda*(Phi3+(p/4)*Phi1)=N(lambda)` after `AC/L` allocates exact `A,C` to opposite roots. Those are allocation certificates. They are not the triple `(g1,g2,g4)`. A SHA-256 of those reports does not supply the promised row/compiler semantic bridge.

V46 remaining obligation “chamber-compiler semantic checks” is still open. V0 tokens remain selected fragments. Pinning the V46 schema/freeze/review does not extract three coefficients at `(G, T_C2)` for these sixteen contacts.

The primitive-calculus identification of §2–§3 (purity plus local remainder plus `Inv1` cancellation) is the *mathematical* content of the bridge. It is not compiled into the linker as an executable comparison against the frozen emitter, which is what a fail-closed schema owes the next consumer.

### 5.3 Minimal executable linker delta

All fail-closed, desk-scale (`T_C2 <= 28`, 569 monomials):

1. For each of the sixteen manifests, instantiate the pinned V46 seven-emitter (`F0..F6` plus frozen tails, loads delayed `4/12/20`, targets subtracted at `28/32/36/38`) at generic shifted leading jets `(A0c,A1,C0c,C1)`, zero lower jets, and generic extra in-window pole-one jets. Read `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]` as polynomials. Require equality to `(g1,g2,g4)` in `Z[1/6][A0c,A1,C0c,C1,rho]`. Every extra-jet coefficient in those three slots must be `0`.
2. Pin that comparison's canonical digest per manifest. Mutation: perturb the AC primitive coefficient, or replace `Phi4` by `h4`, or inject a pole-one jet into `Phi1[G]`; the comparison must fire.
3. Keep endpoint SHA-256 solely for localization (`D(p*k10)` / `D(p*k0)`) and theorem-type inheritance. If a chamber compiler still emits allocated `N(lambda)` at `T_C2`, that is a different proof; it is not this linker, and must not be silently identified with `g4`.
4. Do not accept `RESULT.md` prose, promotion-document narrative, or a hash of either, as item 1.

Until that delta is frozen, V47 is a fail-closed *purity-and-syzygy* schema with generated leading-jet aliases, not a completed row-level linker.

**Manifest completeness: GAP/REPAIR.**

---

## 6. Mutations — CONFIRMED

All twelve required mutations fire. Independent live-fire of the non-string ones:

| Mutation | Independent failure | Path |
|---|---|---|
| `g1` `3/8 -> 3/4` | syzygy 1 nonzero | coefficient extraction / (1.2) |
| `g4` `3/32 -> 3/16` | syzygy 3 nonzero | coefficient extraction / (1.2) |
| drop `/2` on `C0` | displayed `g` no longer equals `(3/4)*(1/2)` remainder | chart factor |
| accept `RA2` as `C2` | `(1,2,2)` global purity becomes true | global pole, not a string |
| drop uniqueness at `a=7` | `k6 C` tie at `G=25` becomes accepted | uniqueness through `G` |
| open `G<28` | synthetic `G=28` accepted only after `G_upper=100` | target wall |
| open `T_C2<32` | synthetic `T=32` accepted only after `T_upper=100` | target wall |
| stage-zero names | `validate_static_schema` | **string-only** |
| `rho=0` face as general-`rho` | `validate_static_schema` | **string-only** |
| `Phi4` replaced by `h4` | `validate_static_schema` | **string-only** |
| AC coefficient `3/4 -> 1` | `matches_pin` misses AC, `NONUNIQUE_G` | coefficient pin |
| unlabelled tuple `(2,3,2)` | `validate_manifest_shape` | typing |

`g1`-normalization and `C0`-factor-two trip the same extraction site with different inputs; they remain distinct mathematical errors. Synthetic target walls are allowed by the required list and are live; a genuine wall cell exists as negative `A9D3`. `RA2-as-C2` is not tautological: `accept_ra2_as_c2=True` makes `(1,2,2)` pass.

**String-only flags.** Mutations 8–10 are schema-label firewalls for live naming hazards (D1AC reuse of `a0,a1,c0,c1`; ramified-fibre relabelling; `h4` versus `Phi4`). They must remain. They do not prove the `Inv1` recurrence, do not prove `Phi[G]=g`, and are not a substitute for §5. The verifier's `P_full_series` block is the same tautology as mutation 10 at the polynomial level.

**Required for promotion?** All twelve are required as fail-closed pins. None of the string-only three, and no additional string, can close §5. A thirteenth mutation — extracted `Phi` unequal to the g-triple — is the missing live path.

**Mutations: CONFIRMED**, with those flags. Not a promotion license.

---

## 7. Transport direction and scope — CONFIRMED

V47 consumes V46 `V0,V1,V3,V4` as a hashed freeze and does not read `shifted_root`. Generated maps are the relative-grade-zero restriction of V46 `jet_reindexing_map`:

```text
az_a, ac_a -> AzD1_0, AcD1_0,
ez_c, ec_c -> 2*CzD1_0, 2*CcD1_0,
cs_r, rs_r -> BzD1_0, 4*BcD1_0,
```

lower ideal `az_i=ac_i=0` (`i<a`), and likewise for `(ez,ec)` below `c` and `(cs,rs)` below `r`. Direction: total coefficient ring, after the lower-contact quotient, onto shifted D1 relative leading jets. That is a quotient-then-reindex. Emptiness of a D1 source coefficient therefore forces emptiness of the total arcs that map to it. Reverse emptiness is forbidden and is not implemented.

The three-row lemma uses only leading jets, so the grade-zero restriction is the correct slice. Factors `2,4` are retained; the direct lemma's smaller algebraic dependence on `rho` does not cancel them.

No mixed V2 root display is used. That is required: the three-row proof allocates no root. V46R1 is the unique typed shifted-root interface on `D(rho)` and is complementary infrastructure, not an input to this linker.

No whole-fan union, no scheme-theoretic endpoint, no rejected contact, no `(8,3,8)`. D23 authority on a raised subtail is inheritance of a stronger closed-tail emptiness, not an upgrade of `r=3,4`.

**Caveat, not a transport gap.** V47 does not re-execute V46 V1. Formula-level carrying of *whatever* three D1 coefficients one has is the jet map. Whether those coefficients are `(g1,g2,g4)` is §5.

**Transport: CONFIRMED** at that scope.

---

## 8. Promotion decision — GAP/REPAIR

V47 does **not** now license replacing the moving-root allocation step on the sixteen named closed tails.

What would be replaceable after §5 is closed: the allocation step only, on exactly

```text
d=1: (a,r)=(2,2),(3,3),(4,4),(5,5),(6,6);
d=2: (2,3),(3,3),(4,4),(5,5),(6,6) and raised (1,2, r>=3);
d=3: (5,5),(6,6) and raised (2,3, r>=5),(3,3, r>=5),(4,3, r>=5),
```

at radical / set-theoretic / normalized-DVR-arc strength, on `D(rho) ∩ (D(A0c) ∪ D(A1))`, retaining the frozen endpoint localizations `D(p*k10)` or `D(p*k0)`, after V46 source naturality carries the same three equations to total in the permitted direction.

What is not licensed, and is not claimed by a correct reading of the schema:

- replacing a stronger endpoint theorem, or a scheme-theoretic unit ideal;
- removing upstream chart factors `/2`, `/4`, `D(p*k10)`, `D(p*k0)`;
- `(a,c,r)=(2,5,3)` or `(2,5,4)`, registered `(1,2,2),(3,3,4),(4,3,4)`, exceptional `E`, `a=7` or later load cells;
- `(8,3,8)`, generic-square coverage, a strict-fan union;
- Gate T, order two, maximum twelve, either global `G2-PSC`/`G2-BD`, JC2, or a counterexample;
- `rho=0`, equality faces, positive-order leading loads, `k=0`, staged Rees charts, the terminal receiver.

Producer `endpoint_replacement_status=WITHHELD_PENDING_DIFFERENT_MODEL_REVIEW` remains the correct status after this review, because the row/compiler coefficient bridge is still missing.

**Promotion: GAP/REPAIR.**

---

## 9. Strongest exact surviving theorem

**Theorem (three-row unique-`AC` syzygy plus global-pole census, this review).**
Let `R` be a `Z[1/6]`-algebra. On `R[A0c,A1,C0c,C1,rho]`, with `C0=(C1 z+C0c)/2` and `L=z^2-rho^2`, the remainder of `(3/4) A0 C0` along `L` is

```text
g1 = (3/8)(A0c C1 + A1 C0c),
g2 = (3/8)(A0c C0c + rho^2 A1 C1),
```

and the even combination of `(3/8) C0^2` at `±rho` is

```text
g4 = (3/32)(C0c^2 + rho^2 C1^2).
```

The four identities of §2.3 hold as equalities of polynomials. Consequently, in the radical sense,

```text
V(g1,g2,g4)  subset  V(C0c, C1)
```

on `D(rho) ∩ (D(A0c) ∪ D(A1))`. This is not a scheme-theoretic unit ideal and does not use root allocation.

If in addition a contact `(a,c,r)` has a complete polar inventory through `T_C2=10+2c`, obtained by aggregating the four binomial summands of the square generating function (cancelled families omitted, pad `+1` stable), in which unloaded `AC/L` of coefficient `3/4` is the unique primitive at or before `G=10+a+c`, every other primitive through `T_C2` except unloaded `C^2/L^2` of coefficient `3/8` has global pole one, `G<28`, and `T_C2<32`, then the only polar contributors to the literal rows

```text
Phi1 = h1,   Phi2 = h2,   Phi4 = h4+(P/2) h2
```

at those grades are `g1`, `g2`, and `g4` respectively: pole-one families cancel from `Phi4` by the moving-`P` `Inv1` recurrence, and do not appear in `Phi1[G]`, `Phi2[G]`. The three equations then contradict exact nonzero leading `C` given exact nonzero leading `A`, on `D(rho)`, at the level of points / DVR arcs.

The contacts for which that inventory hypothesis was independently verified in this session are exactly the twelve registered tails of §4.1 and the raised subtails

```text
(a,d,r) = (1,2, r>=3),
          (2,3, r>=5),     i.e. (a,c,r)=(2,5, r>=5),
          (3,3, r>=5),
          (4,3, r>=5).
```

Monotonicity in `r` makes each threshold a closed tail. `(2,5,3)` and `(2,5,4)` fail by a nonzero `RA^2/L^2` term in `Phi4`. `E` fails by `A^3`. `a=7` fails by a `k6 C` tie at `G`. Local-pole allocation would hide every one of those `RA^2` walls and the high-`r` `E` cell; it is the wrong predicate.

V46 jet reindexing, with leading factors `2,4`, carries any such D1 source coefficient to the total emitter in one direction. Reverse transport, a whole-fan union, a scheme-theoretic endpoint, and every excluded contact are outside the theorem.

Replacement of any promoted allocation step is **not** part of this theorem, because V47 does not yet extract `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]` from the frozen emitter or from a chamber compiler.

---

## 10. Firewalls

Checked against the schema exclusions and against the theorem just stated.

- No strict-fan cover. Finite inventory list, sixteen named tails.
- No ramified-fibre statement. `D(rho)` only; the `rho=0` countermodel of §2.4 is explicit.
- No equality-face statement.
- No Rees chart, no terminal receiver.
- No Gate T, order two, maximum twelve, `G2-PSC`, `G2-BD`, JC2, or counterexample.
- No promotion of `(8,3,8)`. Independent purity fails.
- No drop of `D(p*k10)` or `D(p*k0)`.
- No claim that `r>=5` repairs `E` or `a=7`.
- Producer replacement-withheld bit is preserved, not lifted.

---

## 11. Execution record

Desk only. Commands:

```text
# charged and consumed pins
PYTHONDONTWRITEBYTECODE=1 python3 -B -c '...'   # hashlib of every pin

# unmodified producer replay, no output write
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/verify_three_row_linker.py

# independent algebra, census, contacts, maps, mutations
PYTHONDONTWRITEBYTECODE=1 python3 -B   # throwaway Fraction engine; discarded
```

Python 3.14 stdlib only (`fractions.Fraction`, `itertools.product`, `hashlib`, `json`). No AWS, no heavy CAS, no web sweep, no canonical-ledger edit, no entry into `jc2-lean`. No campaign artifact other than this file was written. Throwaway harness lived in the process and was discarded. After replay, no `__pycache__` under the V47 case directory or the miner directory.

Git HEAD at review time: `418e413593120d19e15e6546eb50c985f4b1f038`.

**GAP/REPAIR** — algebra, global-pole census, derived contacts, mutations, and transport direction hold; the executable `Phi`-to-`g` coefficient bridge is missing, so V47 does not yet replace a moving-root allocation step.
