# QQIDEAL-ORACLE-CODEGEN — parallel-oracle window for the new stack

Lane: `QQIDEAL-ORACLE-CODEGEN`. Date: 2026-09-01. Agent: grok-4.6.

Status: SEALED — oracle jobs emitted; three Fraction self-checks PASS in
sandbox; Groebner/verdict execution is the coordinator's on-box run
(qqideal 0.1.0 + msolveio 0.1.0 + msolve 0.10.1). No exit-price claim.

This lane writes the parallel-oracle window for cutover from Macaulay2 as
generation target to `qqideal` 0.1.0. msolve stays the Gröbner engine;
Sage/SIROCCO stays for braids. Campaign policy: cut over only after the
same five corrected N=4 systems are asked of the new stack; any
disagreement with a binding old-stack verdict is P0.

No `charge_basis` line: this report does not assert a new exit price.

## 0. Custody, hash gate, method

Frozen charged copies were hashed with `shasum -a 256` before they were
read. All three match the charge exactly:

```text
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.sPQx3a/inputs/encoding-faithfulness-audit-r2-sol56-20260901.md
d80c691861d362f1569b38c80a222c2df4992e62f13297adc2e5a996d99a0f18
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.sPQx3a/inputs/corrected-suite-codegen-grok46-20260901.md
e9ddeaead333a544d2e896b4b5d827dd3bea867b5a04ea6bc15c7dd1a6c244bc
  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.sPQx3a/inputs/corrected-863-kill-review-gpt55-20260901.md
```

Workspace copies of the same bytes (identically hashed) are used below for
readable paths. As-run corrected job files used as encoding oracles were
rehashed and match the kill-review / codegen tables:

```text
cd13e1c25bcfcc43d30c238420ab8383580b8c078b16c0b0ff967ff43761d75b  box/corrected_863.ms
411b2e865602aefc8c3bc9993318e3980a62cf21ae5ad3ac30c3b4ec446fd74f  box/corrected_863.m2
d0d5e5d40ce74adda6f84df2e01959fe7f628625cd76537df24febd74471adb8  box/corrected_869.ms
f2c46839b56a766230eebd7e279a88f449fe0df0ecf8f1dc09cbaf0f39cc6434  box/corrected_964.ms
9feb22915f92f92eb80aedff29829c0e2846dcc8d3147aed895c503f343b5766  box/corrected_8611.ms
2f6cb64e1a44cd9176c8b424a3bc4323090fa9fe2570a9593d365308d9d61ea5  box/corrected_867.ms
```

Line references:

```text
charged_input:
  encoding-faithfulness-audit-r2-sol56-20260901.md     (audit)
  corrected-suite-codegen-grok46-20260901.md           (codegen)
  corrected-863-kill-review-gpt55-20260901.md          (kill-review)
jobs (old stack, reviewed):
  box/corrected_863.ms  box/corrected_863.m2
  box/corrected_869.ms  box/corrected_869.m2
  box/corrected_964.ms  box/corrected_964.m2
  box/corrected_8611.ms box/corrected_8611.m2
  box/corrected_867.ms  box/corrected_867.m2
deliverables:
  box/qq_oracle_jobs.py
  box/qq_oracle_run.py
```

Method. Coefficient polynomials of `G86`/`G96` are expanded over `QQ` by
plain `fractions.Fraction` arithmetic (univariate-in-`t` with sparse
multivariate coefficients). This is the sandbox-runnable derivation. The
new-stack layer consumes those generators as `qqideal.Ideal` on
`qqideal.Ring`, replaces the old Rabinowitsch `u*g_c-1` by
`Ideal.saturate` / `ideal_verdict(..., opens=)`, and replaces the old
M2 `idpPostcheck` *construction* of `I_DP` by `qqideal.double_point_ideal`.
Groebner calls go through qqideal's `Verdict` (Kind + Certainty); msolveio
`emit_system` supplies the custody SHA-256 of the emitted system text.
This sandbox cannot import qqideal or msolveio; the three membership
self-checks were run here with Fraction arithmetic only. Canonical ledgers
and `jc2-lean` were not inspected.

API surface used, pinned to the published v0.1.0 source
(`github.com/dcposch/qqideal`, `github.com/dcposch/msolveio`) rather than
guessed from the coordinator's lowercase enumeration. Coordinator names
`qqideal.ring` / `qqideal.ideal` / `qqideal.dimdeg` are the v0.1.0
callables `Ring`, `Ideal`, and the submodule `qqideal.dimdeg`
(`dim_and_degree`, `dimension`, `degree`). There is no lowercase
`qqideal.ring` function in 0.1.0.

```text
qqideal.Ring(*names, characteristic=0)
qqideal.Ideal(gens, ring=R)
qqideal.ideal_verdict(gens, ring=R, opens=(), timeout=)
qqideal.double_point_ideal(p, q, ring=Rt, names=("s","t"))
qqideal.dimdeg.dim_and_degree(leading, nvars)
Ideal.saturate(f)  # Rabinowitsch I + (u*f-1) in ring[u]
Ideal.colon(f)     # v0.1 alias of saturate; colon IS the saturation
Verdict.kind in {Kind.EMPTY, NONEMPTY, TIMEOUT, ERROR}
Verdict.certainty in {Certainty.MODULAR, Certainty.PROVEN}
Verdict.__bool__ raises TypeError

msolveio.emit_system(polynomials, variables=..., characteristic=0) -> str
msolveio.run_groebner(source, gb=2, timeout, threads, binary,
                      allow_unknown_version=False) -> RunResult
  (msolve_version, input_sha256, output_sha256, wall_seconds, ...)
```

Certainty (qqideal README, `ideal.py` verdict docstring): a unit ideal
over Q from msolve `-g` is `Certainty.MODULAR`, not `PROVEN` — msolve
0.10.1 returns after its first modular prime and still prints
characteristic 0. A nonempty result over Q uses a lifted `-g 2` basis
and is `Certainty.PROVEN`. The runner prints the certainty label and
never treats a Verdict as a boolean.

## 1. Derivation (kill-review §2 is the tightest statement)

The audit's shared `(8,6)` chart (audit lines 51-57; kill-review lines
54-60) is

```text
p = t^8 + B t^5 + C t^4 + D t^3 + E t^2 + F t + G
q = t^6 + b t^4 + gam t^3 + d t^2 + e t + f
H = p^3 - q^4
```

The `(9,6)` chart (audit lines 59-64; codegen lines 71-73) is

```text
p = t^9 + A t^7 + P6 t^6 + B t^5 + P4 t^4 + C t^3 + P2 t^2 + D t
q = t^6 + a t^4 + Q3 t^3 + b t^2 + Q1 t
K = p^2 - q^3
```

Raw coefficients of `H`/`K` are not the characteristic coefficients
(audit §3). The reduced second approximate root is the polynomial
(audit 7.1 lines 469-476; kill-review lines 70-74; codegen lines 69, 73):

```text
G86 = p^3-q^4
    + a22 p^2 q + a20 p q^2 + a18 q^3
    + a16 p^2   + a14 p q   + a12 q^2
    + a8 p + a6 q

G96 = p^2-q^3 + a15 p q + a12 q^2 + a9 p + a6 q
```

Retain only auxiliary terms of weight strictly greater than the target
`c`. Let `g_j = [t^j] G`. Closed equations are **every** `g_j = 0` in
the stated range, not the raw odd list. The open is `g_c != 0`.
Kill-review §2 (lines 77-79) for D: `c=3`, all eight auxiliaries
retained, closed `g_22,...,g_4`, open `u*g_3-1`. Independent expansion
in that review gives support `0..22` and `g_23=0`, with leading

```text
g_22 = a22 - 4*b
g_21 = 3*B - 4*gam
g_20 = a22*b + a20 + 3*C - 6*b^2 - 4*d
g_19 = 2*a22*B + a22*gam + 3*D - 12*b*gam - 4*e
```

(kill-review lines 87-92; codegen lines 84-92). Semigroup slots are
triangular of leading coefficient 1 in `a22,a20,a18,a16,a14,a12,a8,a6`
at degrees `22,20,18,16,14,12,8,6`. Degrees 10 and 4 are genuine gap
residuals of `⟨8,6⟩` (audit lines 151-156; kill-review lines 102-106).
On `(9,6)`, degree 16 is a gap of `⟨9,6⟩` (codegen lines 141).

Audit 7.1 table (lines 481-486) and codegen layout (lines 29-34, 108-113),
re-stated as the five oracle jobs:

| job | `Delta` | aux retained | closed | open | `delta_aff` |
|---|---|---|---|---|---:|
| P1 | `(8,6,3)` | `a22..a6` | `g_22..g_4` | `g_3 != 0` | 7 |
| P2 | `(8,6,9)` | `a22..a12` | `g_22..g_10` | `g_9 != 0` | 10 |
| P3 | `(9,6,4)` | `a15,a12,a9,a6` | `g_16..g_5` | `g_4 != 0` | 6 |
| P4a | `(8,6,11)` | `a22..a12` | `g_22..g_12` | `g_11 != 0` | 11 |
| P4b | `(8,6,7)` | `a22..a8` | `g_22..g_8` | `g_7 != 0` | 9 |

Census for P3 (codegen §2, recomputed from audit §3 formulae, not from a
prior validator): `beta_1 = 27-4 = 23`, `delta_inf = 22`,
`p_a(9) = 28`, `delta_aff = 6`. Constants of `G96` are omitted because
every target degree is positive (audit 7.1 lines 494-497).

Variable/ring map, declared: coefficient field `QQ`; grevlex; generator
order auxiliaries then the eleven chart coefficients (msolve first-listed
largest). Slack `u` is *not* a chart variable: qqideal `saturate` appends
it. Matching names are not a map proof; sandbox comparison of the
Fraction expansion against the hashed `.ms` generators is.

## 2. Correspondence: old `.ms`/`.m2` encoding <-> qqideal calls

Exact replacements, with the v0.1.0 semantics taken from the library
source rather than analogy.

### 2.1 Rabinowitsch open (exact)

Old M2 (`box/corrected_863.m2:35-43`, and the same pattern in every
sibling `.m2`):

```text
I0    = ideal(g_22, ..., g_4)          in R0 = QQ[aux, chart]
R     = R0[u]
Iopen = sub(I0, R) + ideal(sub(gopen,R)*u - 1)
```

Old `.ms`: the same generators flattened in `QQ[aux, chart, u]`, last
line `u*g_c-1` (kill-review lines 232-241; codegen lines 108-113).

qqideal v0.1.0 (`ideal.py` saturate docstring; README "Saturation"):

```text
I0    = Ideal(closed_g_j, ring=Ring(*aux, *chart))
Iopen = I0.saturate(g_c)
      = I0 + (u * g_c - 1)   in ring.extend("u")
```

`Ideal.colon` is an alias: "in v0.1 the colon is the saturation."
`ideal_verdict(I0, opens=[g_c])` saturates at the product of `opens`
before the test, so for a single open it is the same variety as
`I0.saturate(g_c).verdict()`.

This is the same Rabinowitsch trick, same slack, same variety
`V(I0) \ V(g_c)`. Emptiness, dimension, and 0-dimensional degree agree.
The returned *generators* of `saturate` are not `I0 : g_c^∞` written
back in `R0` (that would need elimination, which msolve grevlex does
not offer); they are the extended-ring generators, which is exactly
what the old `.ms` already stored.

### 2.2 Cover colon (not a v0.1 hypersurface saturate)

Old M2 (`box/corrected_863.m2:45-66`; codegen §6; kill-review lines
351-381):

```text
Cover0 = ideal(B, D, F, gam, e)          # in-chart gcd-2 even locus
Icolon = colonInf(Iopen, Cover)          # iterate K := K : Cover until stable
                                       # = Iopen : Cover^∞
```

`(9,6)` cover is `ideal(P6, P4, P2, Q3, Q1)` (`corrected_964.m2:46-48`).

qqideal v0.1 `saturate`/`colon` inverts **one polynomial** (a
hypersurface). `I : Cover^∞` for an ideal `Cover = (f1,...,fk)` is the
intersection `∩_i (I : fi^∞)`, which v0.1 does not compute (no ideal
intersection, no primary decomposition). Saturating at the product
`B*D*F*gam*e` would be `I : (product)^∞`, i.e. the complement of the
*union* of the five hyperplanes, which is a strictly larger open than
the complement of the cover locus `V(B,D,F,gam,e)`. Sequential
`saturate(B).saturate(D)...` is the same over-open. **FALLACY-v2
`sat()` wrapping and "if no safe replacement exists, return typed
OPEN":** this lane does not fake `I : Cover^∞` by a product saturate.

The cover colon is also downstream of the binding P1 decision.
Kill-review §6: the reported unit ideal is for `Iopen` *before* cover
colon; on `Cover0` every odd `g_j` vanishes, so `u*g_3-1` already
makes the degree-2 cover disjoint from `Iopen`. Audit lines 169-177
and 504-505: `gcd(d,n,c)=1` in every corrected row, so the `c`-open
already excludes nontrivial common right components. The old `.ms`
jobs never carried the cover (codegen line 38: extra slacks would
raise dimension). The oracle therefore compares `Iopen`, and records
the cover colon as a documented non-correspondence rather than a
silent substitution.

### 2.3 Immersive resultant (exact as a hypersurface open, not in the `.ms` job)

Old M2 (`corrected_863.m2:68-78`): `Iimm = I0 + (u*g_c-1, v*Res_t(p',q')-1)`.
That is two Rabinowitsch slacks, equivalently saturating at the product
`g_c * Res(p',q')`. qqideal `Ring.resultant(f,g,var)` exists over Q
(`ring.py`). A helper `immersive_open(I0, g_c, res)` can
`I0.saturate(g_c).saturate(res)`. The parallel-oracle row is still
`Iopen`, matching the old `.ms` / the kill-review `Gb = gens gb Iopen`.

### 2.4 Double-point scheme (construction corresponds; the four tests do not)

Our `I_DP` (msolve-prep §12; `corrected_964.m2:88-149`; audit 7.1 lines
501-504): for a *closed* parametrization `(p0,q0)` in `QQ[t]`, the
unordered pair scheme in `(sig, Pi)` via divided differences, then

```text
reduced, length == delta_aff, immersive (gcd(p',q')=1),
distinct tangents (Wsym does not vanish on V(I_DP)),
no reused parameter (F square-free).
```

`qqideal.double_point_ideal(p, q)` (`doublepoint.py` docstring, tests
in `tests/test_doublepoint.py`) builds

```text
(p(s)-p(t), q(s)-q(t)) : (s-t)^∞
```

as a Rabinowitsch ideal in `QQ[s,t,u]` with `u*(s-t)-1`. It is the
**ordered**-pair locus `s != t` with the same image.

What it does:

- constructs that ordered ideal (symbolic; no msolve until `.verdict()`);
- emptiness / dimension / 0-dimensional *ordered* degree of the pair locus;
- the cusp `t -> (t^2, t^3)` has empty double-point ideal (injective on
  parameters) and is *not* an embedding — the library says so explicitly.

What it does not check (relative to our `I_DP` definition):

- **unordered vs ordered.** Our length `N = delta_aff` is the degree of
  the `(sig, Pi)` scheme. Ordinary nodes contribute 2 ordered pairs each,
  so an ordinary six-node curve has ordered degree 12, not 6. The node
  test in qqideal (`t^2-1`, `t^3-t`) returns `(dim, degree) = (0, 2)`
  for one node. Comparing `degree == 6` against `double_point_ideal`
  would be the wrong number.
- **reduced.** v0.1 has `radical_member` only; `Ideal.radical` raises
  `NotImplementedError`. Multiplicity is kept in `dimdeg.degree`.
- **immersive.** `gcd(p',q')=1` is a different test (resultant of the
  derivatives). The cusp is the standard example of "no double point,
  not immersive."
- **distinct tangents / no reused parameter.** No Wronskian, no
  parameter polynomial `F(X)`.

P3 therefore uses `double_point_ideal` as the *scheme constructor* for
a later closed point, not as extra generators of the coefficient ideal
(codegen §6: adjoining one off-diagonal pair encodes "at least one
node", which the HF-twin already has four of, and does not encode
length 6). The P3 oracle *row* is the characteristic `Iopen`, matching
`corrected_964.ms`. The six-node question remains a post-check:
extract a closed point, build `double_point_ideal(p0,q0)`, read
`dimdeg`, and separately test immersive / reduced / tangents. Helper
`p3_idp_verdict_for_closed_point` in `qq_oracle_jobs.py` is that
constructor plus `verdict`/`dimdeg`; it does not claim REALIZED.

### 2.5 Line-cited call table

| old encoding | file:line | qqideal call | correspondence |
|---|---|---|---|
| `R0 = QQ[a22,...,f]` | `corrected_863.m2:16` | `Ring("a22",...,"f")` | same names, QQ, grevlex |
| `p, q` chart | `corrected_863.m2:24-25`; kill-review 54-57 | Fraction UPoly / `Ring` gens | declared map |
| `G86poly = p^3-q^4+...` | `corrected_863.m2:26`; kill-review 70-74 | Fraction expansion of the same polynomial | generators compared to hashed `.ms` |
| `gj = coefficient(t^j, G86poly)` | `corrected_863.m2:32`; kill-review 251-279 | `[t^j]` of the UPoly | same extraction |
| `closedIdx = {22,...,4}` | `corrected_863.m2:33` | closed range in the job spec | same list |
| `I0 = ideal closedGens` | `corrected_863.m2:35` | `Ideal(closed, ring=R0)` | same |
| `Iopen = I0 + (u*g_3-1)` | `corrected_863.m2:42`; `.ms` last line | `I0.saturate(g_3)` / `opens=[g_3]` | exact Rabinowitsch |
| `Cover0 = ideal(B,D,F,gam,e)` | `corrected_863.m2:45` | *none* (see §2.2) | OPEN as a v0.1 primitive |
| `colonInf(I, Cover)` | `corrected_863.m2:50-63` | *not* `colon(product)` | would change the open |
| `Gb = gens gb Iopen` | `corrected_863.m2:83-85` | `ideal_verdict(Iopen)` / `Iopen.verdict()` | Kind EMPTY iff unit ideal |
| `idpPostcheck(p0,q0,6)` | `corrected_964.m2:114-149` | `double_point_ideal(p0,q0)` + `dimdeg` | construction only; tests omitted as in §2.4 |
| msolve `.ms` bytes | codegen §8 hashes | `Ideal.to_msolve()` = `msolveio.emit_system` | custody SHA-256 of *new* emission |

P2/P4a/P4b are the same pattern with the aux/closed/open of the table in
§1 (`corrected_869.m2:10-12,32-42`, `corrected_8611.m2:10-12,40-50`,
`corrected_867.m2:10-12,40-51`). P3 incidence is `corrected_964.m2:10-12,33-43`
and `corrected_964.ms` (13 generators).

## 3. Old-stack verdicts hard-coded from the charged reports

These are the DIFF targets in `box/qq_oracle_run.py`. They are not
re-inferred.

| job | old-stack record | source | oracle rule |
|---|---|---|---|
| P1 `(8,6,3)` | **EMPTY**, two-engine, binding | kill-review lines 7-8, 321-323, 476-488: `.ms` `basis=[1]`, patched `.m2` `gb=\|1\|`, `dim=-1`, char 0, `Iopen==(1)` before colon | any qqideal Kind other than `EMPTY` prints `ORACLE-P0` and exits 2. `TIMEOUT`/`ERROR` are also P0: they are not answers and must not collapse into EMPTY. Certainty on a unit ideal over Q is expected `MODULAR`. |
| P2 `(8,6,9)` | pending (corrected job not a charged as-run) | audit 7.2; codegen "no Groebner run" | record fresh; no P0 |
| P3 `(9,6,4)` | incidence locus **NONEMPTY** by the HF-twin (desk), nodal **OPEN**; raw EMPTY vacated | audit 7.2 lines 521, 37-38, 396-432; codegen self-check (iii) | record fresh incidence verdict; do not promote to six-node. HF-twin is self-check (iii), not a Groebner certificate. |
| P4a `(8,6,11)` | raw A was NONEMPTY, **vacated** as unfaithful; corrected system undecided | audit 7.2 line 517; codegen P4 archival | record fresh; do not assume EMPTY or NONEMPTY |
| P4b `(8,6,7)` | raw C was pending, **vacated**; corrected system undecided | audit 7.2 line 519; the prompt's "raw-NONEMPTY->vacated" applies to P4a (and raw B); P4b was pending, not nonempty | record fresh; do not assume |

Notes.md (live state 2026-09-01): today's 863 EMPTY was produced by
msolve 0.6.5 `-g 2` plus the M2 mirror; the `[1]` unit-basis convention
is stable across versions. The oracle reruns on msolve 0.10.1 regardless.
qqideal `Ideal.verdict` does not take `binary=`; the runner prepends
`MSOLVE_BINARY`'s directory to `PATH` and also passes `binary=` into any
direct `msolveio.run_groebner` call. `allow_unknown_version=False`.

## 4. Self-checks (Fraction, no msolve) — transcripts

The three reviewed controls, re-implemented as substitutions into the
same `[t^j]G` that the jobs emit. Coefficient field `QQ` or
`QQ(zeta)/(zeta^2-zeta+18474)`. No sympy, no qqideal, no msolve.

A leading-coefficient identity check against kill-review §2 is run
first (method sanity, not one of the three charged controls). An
encoding comparison of the Fraction closed generators against the
hashed `.ms` files is run second (variable/ring map, not matching
names). Then (i)(ii)(iii).

Sandbox transcript follows, verbatim from
`python3 box/qq_oracle_run.py --self-check` (exit 0). Leading-identity
and `.ms`-encoding lines are extra method/map controls; (i)(ii)(iii)
are the three charged checks.

```text
qqideal-oracle-codegen  self-checks (Fraction, no msolve)
=== leading G86 identities (kill-review §2) ===
g_22 == a22-4*b: match
g_21 == 3*B-4*gam: match
g_20 == a22*b+a20+3*C-6*b^2-4*d: match
g_19 == 2*a22*B+a22*gam+3*D-12*b*gam-4*e: match
g_23 identically 0: match
LEADING-IDENTITIES: PASS

=== encoding comparison vs reviewed .ms (polynomial equality) ===
corrected_863: match (19 closed + open g_3; vars 19+u)
corrected_869: match (13 closed + open g_9; vars 17+u)
corrected_964: match (12 closed + open g_4; vars 15+u)
corrected_8611: match (11 closed + open g_11; vars 17+u)
corrected_867: match (15 closed + open g_7; vars 18+u)
MS-ENCODING: PASS

=== (i) charged A false-positive vs corrected (8,6,11) ===
check(i) g22 at point (in a22): a22-4
check(i) g21 at point: 0
check(i) h19 at point: 0
check(i) g19 residual (a22=4): 11
check(i) raw h11 at point: 59291/18432 - 27671*zeta/110592
SELF-CHECK (i) charged A false-positive vs corrected (8,6,11): PASS — old A holds (g21=0, h19=0, h11=59291/18432 - 27671*zeta/110592 != 0) but corrected residual g19|a22=4b equals 11 != 0, so the point is not on V(g_22,...,g_12)
CHECK(i): PASS

=== (ii) (9,6,2) exhibit vs corrected membership ===
check(ii) closed g_16..g_3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check(ii) g2: 64
check(ii) g0,g1: 0 0
SELF-CHECK (ii) (9,6,2) curve q=t^6+8t^2, p=t^9+12t^5+24t vs corrected (9,6,2): PASS — aux (a15,a12,a9,a6)=(0,0,0,-64) gives g_j=0 for 3<=j<=16 and g_2=64 != 0
CHECK(ii): PASS

=== (iii) HF-twin (9,6,4) vs corrected locus (pre-nodal) ===
check(iii) closed g_16..g_5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check(iii) g4: -27/128
check(iii) g3,g2,g1,g0: 0 -351/1024 0 0
SELF-CHECK (iii) HF-twin (9,6,4) vs corrected (9,6,4) locus: PASS — aux (a15,a12,a9,a6)=(0,-9/4,0,-27/16) gives g_j=0 for 5<=j<=16 and g_4=-27/128 != 0 (constant term 0 omitted as in audit 7.1)
CHECK(iii): PASS

SELF-CHECKS OVERALL: PASS
```

The encoding comparison is polynomial equality of the Fraction
`[t^j]G` against the hashed reviewed `.ms` generators (not string
identity: monomial order in a sum is not a mathematical invariant).
Variable lists match, including the slack `u` on the open generator
`u*g_c-1`. That is the variable/ring map check: the qqideal jobs emit
those same generator strings into `Ideal(..., ring=Ring(*names))`.

## 5. Jobs and runner

`box/qq_oracle_jobs.py` exports one builder per system:

```text
job_p1_863, job_p2_869, job_p3_964, job_p4a_8611, job_p4b_867
```

Each returns `(Verdict, custody)` where custody has `input_sha256` of
`Ideal.to_msolve()` (msolveio `emit_system` of the saturated open
ideal), `msolve_version`, `wall_seconds`, ring names, generator
counts. P3 additionally constructs `double_point_ideal` (symbolic
schema, ring `("s","t","u")`) and exposes
`p3_idp_verdict_for_closed_point`. Cover colon is commented, not
faked. `Verdict` is never used as a boolean.

`box/qq_oracle_run.py` always runs the Fraction self-checks first
(failure exits 1). Then, if not `--self-check-only`, it executes the
five jobs, prints a table of `kind` + `certainty` + `dim` + `degree` +
custody SHA prefix + wall time, diffs against §3, and on P1
disagreement prints `ORACLE-P0` loudly and exits 2. Environment:
`MSOLVE_BINARY` (directory prepended to `PATH` because
`Ideal.verdict` has no `binary=`), `QQ_ORACLE_TIMEOUT` (default 3600).
`allow_unknown_version=False` on any direct msolveio call; qqideal's
internal `run_groebner` uses the same default.

This sandbox cannot import qqideal/msolveio (charge: write against the
signatures; coordinator executes on the box with msolve 0.10.1).
On-box:

```text
python3 box/qq_oracle_run.py --self-check
MSOLVE_BINARY=$HOME/msolve-0.10.1/bin/msolve QQ_ORACLE_TIMEOUT=3600 \
  python3 box/qq_oracle_run.py
```

## 6. Guardrails

- **Flag/place/series:** not in play. The charged A point remains one
  place with conjugate series; this lane tests coefficient-ideal
  membership and stack agreement.
- **Variable/ring map:** charts, auxiliary names, grevlex, QQ, and the
  slack `u` are declared. Matching names are not a map proof; closed
  generators are compared to hashed `.ms` polynomials.
- **Raw remainder degree:** encoded generators are `[t^j]G86`/`[t^j]G96`
  after the 7.1 auxiliaries, not raw `h_j`/`k_j`. Gap degrees 10, 4, 16
  are explicit. Zero polynomial is rendered `0` and is not emitted as a
  generator.
- **`sat()` wrapping:** the ideal is `I0` in `R0`; `saturate(g_c)` is
  Rabinowitsch in `R0[u]`; ring of the result is asserted by using
  `Iopen.ring`. Positive control: `(9,6,2)` membership. Negative
  control: charged A vs corrected 8611. Cover colon is *not* wrapped
  as a product saturate.
- **Floor/attainment:** P3 incidence NONEMPTY (HF-twin) is not a
  six-node witness. `double_point_ideal` degree is not `delta_aff`.
  P1 EMPTY of `Iopen` is consumed only as the curve-level obstruction
  already charged, subject to the on-box rerun.
- **Carrier:** `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. Emitting an
  oracle job is not a realization. A modular unit-ideal certainty is
  not a Q-exact lift.
- **Prime label/derivative:** `gam` is the chart coefficient, not a
  derivative. `p'` is written `dp`. qqideal I_DP uses `s,t,u`, not `pi`.
- **Target/arrival index:** target is fixed `Delta=(d,n,c)`, equivalently
  exact reduced second-approximate-root degree `c`, not a Moh raw-index
  label.

## 7. Per-file SHA-256

Independent `shasum -a 256` of the deliverable bytes after the last
write. POSIX text, LF only.

```text
7be3d100ffbfc0a36f7a3876d87480ccd92f7a652d2a2424a051bd4497d1a0e3  box/qq_oracle_jobs.py
331ba6ead88b7998aa52a3f2498185fa876da3af63d648d3c21848f47f0edf9c  box/qq_oracle_run.py
```

Reviewed old-stack encodings this window compared against (unchanged):

```text
cd13e1c25bcfcc43d30c238420ab8383580b8c078b16c0b0ff967ff43761d75b  box/corrected_863.ms
411b2e865602aefc8c3bc9993318e3980a62cf21ae5ad3ac30c3b4ec446fd74f  box/corrected_863.m2
d0d5e5d40ce74adda6f84df2e01959fe7f628625cd76537df24febd74471adb8  box/corrected_869.ms
f2c46839b56a766230eebd7e279a88f449fe0df0ecf8f1dc09cbaf0f39cc6434  box/corrected_964.ms
9feb22915f92f92eb80aedff29829c0e2846dcc8d3147aed895c503f343b5766  box/corrected_8611.ms
2f6cb64e1a44cd9176c8b424a3bc4323090fa9fe2570a9593d365308d9d61ea5  box/corrected_867.ms
```

**Final status: oracle window written.** Self-checks (i)(ii)(iii) PASS
in this sandbox. P1 on-box disagreement is P0. P2/P3/P4a/P4b record
fresh. Types remain at their charged scopes (P1 curve-level EMPTY is
the charged two-engine fact, to be confirmed or P0'd by the new
stack; P3 nodal OPEN; P4a/P4b vacated-raw). No ledger edit, no
`jc2-lean` inspection, no exit-price claim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25335`.
- Body SHA-256:
  `d8b4a55e59a49003cb06329d207d6f8e7e75d2a8e68d24c2382329005712a185`.
- Frozen basis: `4252acc58f89a5cc6047b7f2215bab3278911407`.
