# Hostile review — complete-source D1 finite band `a=2..5`

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers and prior V12 wording are not authority |
| Method | source reading, SHA-256 of every named pin and evidence file, compiled-script inspection, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the three required primary pins match. Every path named in `FREEZE.sha256` (4 rows) and `EVIDENCE.sha256` (28 rows) rehashes to the printed digest. Nested `compiled.sha256` rows on both lanes rehash. The imported V1 freeze, `tails.json`, and canonical all-tails digest rehash. The `/tmp` source archive recorded in `RESULT.md` was not retrieved; the repository freeze and the 28 evidence files are the custody. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

On the reviewed generic-square first-normal chart `D(p*k10)`, after the half-weight support gate, each of the four fixed contacts

```text
ord(A)=a,  ord(C)=a+1,  ord(R)>=a,  a in {2,3,4,5}
```

has complete seven-row source at the first two relevant grades `g=11+2a` and `g+1`. Those rows are the moving lower-unitriangular Faber image of an exact Laurent receiver whose only in-window polar forms are `AC/L` at grade `g`, `C^2/L^2` at grade `g+1`, `k10 RC/L` at `g+1` when `ord(R)=a`, and `k10 R^3/L` at `g+1` only for `a=ord(R)=2`. The extracted source is independent of `k6,k2,mu2,mu4,mu6,J` through `g+1`. After the two opposite-root allocations of nonzero linear `A0,C0` on squarefree `L=z^2+p/2`, the first numerator vanishes identically and the next `L^2` numerator evaluates at the `A0` root to `(3/2) lambda^2 cv^2`, nonzero on `D(p)` with nonzero `C0`. No finite-order normalized arc exists in any of the four listed contacts. The statement is arcwise/set-theoretic, not scheme-theoretic, and it does not close the square branch, order two, `(8,12)`, maximum twelve, or JC2.

The coefficient `eta` is only the grade-`a` section of `R`. That is a finite truncation, not an unbounded substitution.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Three primary pins | hashes | all three match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 4/4, `EVIDENCE` 28/28, both nested `compiled.sha256` 2/2 |
| 0. Ancestry | V1 compiler, V1 freeze, erratum, first-normal, closure, tails | all five compiler pins and the V1 freeze rows rehash; `tails.json` `d72f774c…`, canonical `6eed03d4…` |
| 1. Seven-tail reconstruction | frozen Faber, loads `k10,k6,k2`, targets `mu2,mu4,mu6,J/4` | **holds**; compiled `Phi1..Phi7` are `tail_text` expansions, not the eight-term analytic |
| 2. Source substitution | `f=K^2+sigma^5 D`, `K=L(sigma)^2+sigma^2 R`, `D=LA+C`, orders | **holds** after the documented factors 2 and 4 and all outer `sigma` |
| 3. First two grades | `g=11+2a`, `g+1`; unlisted terms later except `RC` and `a=r=2` `R^3` | **holds** by support inequalities |
| 4. Coefficient independence | `k6,k2,mu2,mu4,mu6,J` through `g+1`; `diff` sentinels | **holds** on the complete source; `diff` is sufficient |
| 5. Moving row relation | `g+1` includes `L(sigma)` and `T1=2 ell1 dT0/dp` | **holds**; inspected `row_checks` and the compiled `Check*` lines |
| 6. Laurent emitter | `AC/L`, `C^2/L^2`, `k10 RC/L`, `k10 R^3/L`; sigma/t powers | **holds**; complete through `g+1` for these four contacts |
| 7. Recurrences | first `L`, next `L^2`; every `p` and `p^2/4` | **holds** independently of V12 |
| 8. Ring maps | 26 images, both allocations, exhaustiveness | **holds** for nonzero linear `A0,C0` when `L` is squarefree |
| 9. Next numerator | `(3/2) lambda^2 cv^2`; competing terms vanish | **holds**; licensed reason is simple-pole versus double-pole |
| 10. `eta` scope | grade-`a` section only; `eta=0` for `ord(R)>a` | **holds**; not an unbounded substitution |
| 11. Inversions | `D(p*k10)`, nonzero A/C; set versus scheme | **holds**; arcwise only |
| 12. Dual AWS | rc0, PASS, no rejected diagnostics, `time -v` in stderr | **holds**; exact Q is characteristic zero; `F_65521` is a software control |
| 13. Firewall | no `a>=6`, no positive-order `k10`, no `p=0`/`k10=0`, no fan/order-two | **holds**; Pell/Chebyshev all-load survivor is compatible |

---

## 0. Custody

Recomputed SHA-256 of the three required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `17c3baa20232dad9dd1356c8e903a863a44480344d81d8aa587216414aad0a61` | producer report |
| `.../FREEZE.sha256` | `9c53eecf7aa3a1fbc75012d9566a2d564e7a39da7e9011c6d5fd63cd53431920` | source freeze |
| `.../EVIDENCE.sha256` | `49264a8d6ae24724ee1005dfac9b4602946f2f3b7a77c0512df237369470f254` | evidence freeze |

`FREEZE.sha256` names four files, all matching:

| Path | SHA-256 |
|---|---|
| `REGISTRATION.md` | `1329021d75ce044d7ec2d7695708a0b4ab37f9045acbe9cd190594fc03aef46b` |
| `compile_finite_band.py` | `beff666bedffd912e052e8bd03b74ed4b8f658d94f697f99be1ec97748309848` |
| `run_aws.sh` | `744528265063b6f189917fa844c216962d95e2c55c1335327f116812b4582dc3` |
| `launch_host.sh` | `3ec2bbf1ef2562786274e6f6096a5b3057cd53afa5c1d53ed55e03ca0ea1c171` |

`EVIDENCE.sha256` names 28 files; all 28 rehash. Both nested `compiled.sha256` files rehash to the retrieved `.sing` and `result.json`. The two stdout files are byte-identical (`be11fa82…`); the two `validation` files are byte-identical (`9e57aef1…`); the two `compiler.validation` files are byte-identical (`7680278d…`, the line `compiler_rc=0`). Characteristic-normalized compiled scripts are byte-identical: the only difference is the eight ring-characteristic tokens `0` versus `65521` (32 bytes, matching the 32-byte size gap 559523 versus 559555).

A passing sentinel is not mathematics. The algebra below is independent of those sentinels.

Imported pins, all recomputed:

```text
e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py
34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/FREEZE.sha256
997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114
  xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md
40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94
  xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md
3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95
  xmodel/max12-812-order2-square-contact-raising-closure-criterion-20260826.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  .../compiled_v2/tails.json
6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8
  canonical all-tails digest
```

Every V1 freeze row rehashes, including `compile_cge3_universal.py` and `compile_square_load_ladder.py`. Frozen Faber `tails.json` has seven rows with 36, 54, 58, 81, 89, 120, 131 monomials.

`AWS_LAUNCH_METADATA.md` is not in `FREEZE` or `EVIDENCE`. It is not used.

---

## 1. Seven exact frozen Faber tails

The finite-band compiler does not emit an eight-term Laurent polynomial as source. It loads frozen `compile_r1_d1_ac.py`, which loads frozen `compile_cge3_universal.py`, which pins `tails.json` and `compile_square_load_ladder.py`. Before any `.sing` is written it rechecks every imported pin and the canonical all-tails digest. Each ordinary coordinate is

```text
base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
```

with target subtractions `-sigma^{2(12+row)}*(mu2|mu4|mu6|J/4)` on rows 2, 4, 6, 7. `tail_text` refuses a monomial whose length is not the frozen name list, whose load exponents are not in `{0,1}` with at most one load, or whose weighted degree is not `12+row`. Load weights in Lambda units are `k10:2`, `k6:6`, `k2:10`, i.e. `sigma^{4} k10`, `sigma^{12} k6`, `sigma^{20} k2` after `Lambda=sigma^2`.

The compiled scripts contain all seven `Phi` rows for each of `a=2,3,4,5`. Each `Phi` is a long tail expansion containing `k0*(sigma^2)^2`, `k6*(sigma^2)^6`, and `k2load*(sigma^2)^10`. Each contact subtracts exactly `-sigma^28*(mu2)`, `-sigma^32*(mu4)`, `-sigma^36*(mu6)`, `-sigma^38*(J/4)` once. The independent analytic block is `universal_hshift`, compared afterwards by `row_checks`. That is a tails-versus-analytic bridge, not a replay of the analytic formula as source.

---

## 2. Source coefficient substitution

Imported `source_coefficients` encodes `K=L(sigma)^2+sigma^2 R` and `D=L A+C` in the load-ladder/cge3 slots, after inserting the factors 2 and 4 that convert direct polynomial `C,R` into the older generating-function chart `C=(e31 z+e30)/2`, `R=bs z+br/4`:

```text
pp = p+2*sigma*ell1
L(sigma) = z^2 + pp/2 = z^2 + p/2 + sigma*ell1
kc = sigma^2 * rz,     kr = (pp)^2/4 + sigma^2 * rc
n3 = sigma^3 * az,     n2 = sigma^3 * ac
n1 = sigma^3 * ((pp*az)/2 + cz)
n0 = sigma^3 * ((pp*ac)/2 + cc)
```

The degree-6 dictionary is the expansion of `K^2+sigma^5 D` in those slots: `n_i` already carry `sigma^3`, and the dictionary multiplies them by another `sigma^2`, giving `sigma^5 D`. The `K=L^2+sigma^2 R` piece is `kc,kr`.

The finite-band client passes the fixed powers

```text
az, ac = sigma^a * (a1+sigma aa1, a0+sigma aa0)
cz, cc = sigma^{a+1} * (c1+sigma cc1, c0+sigma cc0)
rz, rc = sigma^a * eta * (b1, b0)
```

After every outer `sigma` in `source_coefficients`, this is `ord(A)=a`, `ord(C)=a+1`, `ord(R)=a` when `eta` is a unit and `ord(R)>a` when `eta=0`. The analytic generating functions use the same powers. The compiled `a=2` block has `sigma^2` on `A,R` and `sigma^3` on `C`; the `a=5` block has `sigma^5` on `A,R` and `sigma^6` on `C`.

---

## 3. First two relevant grades

For each `a=2,3,4,5` one has `g=11+2a` and `g+1=12+2a`, i.e. the pairs `(15,16)`, `(17,18)`, `(19,20)`, `(21,22)` printed as `GRADE_PAIR` and compiled as `ideal Sigma=std(ideal(sigma^g))`.

Absolute orders of the eight analytic monomials, with `ord(A)=a`, `ord(C)=a+1`, `ord(R)>=a`, unit `k10`:

| term | order | versus `g=11+2a` | in-window through `g+1` |
|---|---:|---|---|
| `AC/L` | `11+2a` | `g` | yes, first grade |
| `C^2/L^2` | `12+2a` | `g+1` | yes, next grade |
| `RA^2/L^2` | `>=12+3a` | `g+(1+a)` | no (`a>=2`) |
| `A^3/L^3` | `15+3a` | `g+(4+a)` | no |
| `k10 R^3/L` | `>=10+3a` | `g+(a-1)` | only `a=ord(R)=2` at `g+1` |
| `k10 RC/L` | `>=12+2a` | `g+1` | yes iff `ord(R)=a` |
| `k10 R^2 A/L^2` | `>=13+3a` | `g+(2+a)` | no |
| `k10 A^2/L` | `14+2a` | `g+3` | no |

Omitted lower-load/target orders from the complete source, matching the V12 erratum support table and the compiled `Lambda` weights:

| contribution | order | at/before `g+1=12+2a` when |
|---|---:|---|
| `k6 C/L` | `18+a` | `a>=6` |
| `k6 R^2/L` | `>=16+2a` | never in this band (gap 4) |
| `k2 R/L` | `>=22+a` | `a>=10` |
| `mu2` | `28` | `a>=8` |
| `mu4` | `32` | `a>=10` |
| `mu6` | `36` | `a>=12` |
| `J/4` | `38` | `a>=13` |

For `a=5`, `k6 C/L` is at 23 against window 21–22. That is the recorded first load transition, not a hole in this band. Every unlisted unloaded/`k10` term lies later except `RC` for `ord(R)=a` and `R^3` only for `a=ord(R)=2`.

---

## 4. Coefficient independence through `g+1`

Independence is not inferred from the order table. Each compiled block extracts `g_row` and `g+1_row` from the complete seven `Phi` polynomials, then runs

```text
if (diff(gname, k6)!=0) forbidden=0;
```

and the same for `k2load, mu2, mu4, mu6, J`, on both grades and all seven rows (84 `diff` tests per contact, 336 in the package). `SOURCE_FORBIDDEN=1` on both fields is the engine report of those tests.

The tests are sufficient for the claim. `tail_text` forces each load to appear to power 0 or 1, and at most one load per monomial, so there is no `k6^{65521}` Freshman's-dream kernel on the control field. In a free polynomial ring, `diff(-,k6)=0` if and only if `k6` does not occur. Exact Q is characteristic zero, so no coefficient of a present monomial can vanish by characteristic. `k0` is deliberately not forbidden: `k10 R^3` and `k10 RC` are licensed in-window terms.

The analytic block does not contain `k6,k2,mu*,J`. Combined with `ROW_IDENTITIES=1`, the source rows through `g+1` cannot hide a lower-load combination that the analytic omitted: such a combination would be a nonzero remainder.

---

## 5. Moving lower-unitriangular row relation

The implementation is `row_checks` in frozen `compile_r1_d1_ac.py`, not a marker name. For each grade in `{g,g+1}` and each ordinary index `i=1..7` it forms

```text
predicted = sum_{j<=i} T0_ij(p) h_{grade,j}
          + 1_{offset>=1} T1_ij h_{grade-1,j}
          + 1_{offset>=2} T2_ij h_{grade-2,j}
```

with `T0,T1,T2` from `transform_series` of frozen `compile_cge3_universal.py`, the first three coefficients of `T_ij(p+2 sigma ell1 + 2 sigma^2 ell2)`. Offset is `grade-g`, so the first grade uses only `T(p)` and the next grade uses `T(p)` and the coefficient of `sigma`.

`transform_series` for even delta `i-j=2n` gives `T0 = c p^n` and `T1 = 2 n c ell1 p^{n-1}`. That identity is `T1 = 2 ell1 dT0/dp`. It is visible in the compiled next-grade checks, for example

```text
A2_Check16_3 = g16_3 - ((1/4)p h16_1 + (1/2)ell1 h15_1 + h16_3)
A5_Check22_7 = g22_7 - ((5/128)p^3 h22_1 + (15/64)ell1 p^2 h21_1 + ...)
```

The `(1/2)ell1` and `(15/64)ell1 p^2` coefficients are exactly `2 ell1 dT0/dp` for `n=1` and `n=3` with `j=1`. The first-grade checks have no `ell1` summands, correctly: polar `Hshift` starts at `sigma^g`, so `h_{g-1}=0` and the `T1` connection is absent.

The denominator connection from `L(sigma)` is not a `T` coefficient. It sits in the analytic `h_{g+1}` itself, because `Inv1,Inv2,Inv3` are built from `sp=p/2+sigma ell1`. The next-grade identity is therefore `g_{g+1} = T(p) h_{g+1} + T1 h_g`, which includes both the moved receiver and the first row-basis connection. Offset never reaches 2, so `ell2` in the `T2` formula is never emitted and the ring has no `ell2`.

---

## 6. Analytic Laurent emitter

`universal_hshift` is the eight-term generating function

```text
(3/4) sigma^10 t A C Inv1          AC/L
(3/8) sigma^10 t^3 C^2 Inv2        C^2/L^2
-(3/8) sigma^12 t^2 B A^2 Inv2     RA^2/L^2
-(1/16) sigma^15 t^4 A^3 Inv3      A^3/L^3
(5/16) sigma^10 k B^3 Inv1         k10 R^3/L
(5/8) sigma^11 t k B C Inv1        k10 RC/L
-(5/32) sigma^13 t^2 k B^2 A Inv2  k10 R^2 A/L^2
(5/32) sigma^14 t k A^2 Inv1       k10 A^2/L
```

with `Inv1,Inv2,Inv3` the truncations of `(1+sp t^2)^{-1,-2,-3}` through `t^8`. The extra overall `t` on even-degree numerators (`AC`, `C^2`, `RC`, `A^2`) and its absence on the odd cubic `R^3` is the same packing that makes `Nfirst=h1 z+h2` and `Nnext=h1 z^3+h2 z^2+(h3+p h1)z+(h4+p h2)` hold in Section 7.

Coefficients and `sigma` powers were re-derived from

```text
f = K^2 + sigma^5 D,   K = L^2 + sigma^2 R,   D = L A + C
```

and the source summand `sigma^4 k10 f^{5/4}`:

- `(3/8) x^2 K^3` with `x=sigma^5 D/K^2` produces `(3/4) sigma^{10} AC/L` and `(3/8) sigma^{10} C^2/L^2`;
- `K^{5/2}=L^5(1+sigma^2 R/L^2)^{5/2}` produces `(5/16) sigma^{10} k R^3/L`;
- `(5/4) sigma^9 k D K^{1/2}` produces `(5/8) sigma^{11} k RC/L`;
- the `x^2` piece of `(1+x)^{5/4}` produces `(5/32) sigma^{14} k A^2/L`.

`t` powers match `1/L=t^2 Inv1`, `1/L^2=t^4 Inv2`, `1/L^3=t^6 Inv3` after writing `A_gen=A_poly/z` and inserting the extra `t` on even numerators. The `t^8` truncation of `Inv` is exactly the `t^8` coefficient needed for ordinary row 7.

No further binomial term of `f^{3/2}` or `k10 f^{5/4}` enters through `g+1` on these four contacts: `ACR/L^3`, `C^2 R/L^4`, `C^3`, `k C^2`, `k R^2 C` are at least grade `g+3`. Raising `a` only pushes those terms later. Completeness at `a=5` is therefore inherited from completeness of the same emitter at `a=2`, plus the support table of Section 3. The compiled `a=2` and `a=5` `Hshift` lines contain all eight summands with the displayed coefficients.

---

## 7. First `L` recurrence and next `L^2` recurrence

The generating function uses an extra overall `t` relative to `t=1/z`. With that convention,

```text
N/L     = (n1 z + n0)          corresponds to  H = (n1 t^2 + n0 t^3) Inv1
N/L^2   = (n3 z^3+n2 z^2+n1 z+n0) corresponds to  H = (n3 t^2+n2 t^3+n1 t^4+n0 t^5) Inv2
```

and `h_row=[t^{row+1}] H`. Hence `n1=h1`, `n0=h2` for a simple pole, i.e. `Nfirst=h1 z+h2`. For a double pole, `[t^2]Inv2=-2 sp=-p` at frozen `p` gives

```text
n3=h1,  n2=h2,  n1=h3+p h1,  n0=h4+p h2
```

which is exactly

```text
Nnext = h1 z^3 + h2 z^2 + (h3 + p h1) z + (h4 + p h2).
```

The coefficient of `h1` in the linear slot is `p`, not `p/2`. That is the `[t^2]` coefficient of `Inv2=(1+sp t^2)^{-2}`, namely `-2*(p/2)=-p`. Copying the simple-pole formula here would have been a false identity.

The recurrences are the coefficient identities

```text
(1 + (p/2) t^2) Inv1 = 1
(1 + p t^2 + (p^2/4) t^4) Inv2 = 1
```

applied to `H`. They give, without remainder from the displayed prefactors,

```text
h_{k+2} + (p/2) h_k = 0           for the first grade, k=1..5
h_{k+4} + p h_{k+2} + (p^2/4) h_k = 0   for the next grade
```

i.e. the five compiled first checks `h3+(p/2)h1`, …, `h7+(p/2)h5` and the three compiled next checks

```text
h5 + p h3 + (p^2/4) h1
h6 + p h4 + (p^2/4) h2
h7 + p h5 + (p^2/4) h3.
```

Every `p` and every `p^2/4` is the expansion of `(z^2+p/2)^2=z^4+p z^2+p^2/4`, not a V12 relic. The compiled `a=5` block uses `p*p/4` for the same rational.

---

## 8. Ring maps and exhaustive allocation

Each eval ring has the same 26 variables as the source ring, in order

```text
z,t,sigma,p,ell1,eta,a0,a1,aa0,aa1,c0,c1,cc0,cc1,
b0,b1,k0,k6,k2load,mu2,mu4,mu6,J,rtx,aua,cvg.
```

Each of the four maps has 26 images. `p` maps to `-2 rtx^2`, so `L` maps to `z^2-rtx^2`. The two allocations are

```text
pos: a1=aua, a0=-aua rtx, c1=cvg, c0= cvg rtx
     A0 = aua(z-rtx), C0 = cvg(z+rtx)
neg: a1=aua, a0= aua rtx, c1=cvg, c0=-cvg rtx
     A0 = aua(z+rtx), C0 = cvg(z-rtx)
```

and the two root maps evaluate at the `A0` root (`z=rtx` on pos, `z=-rtx` on neg). Both orientations are present. `evalposfirst` and `evalnegfirst` test `Nfirst` identically zero after allocation, which is `L | A0 C0`, not merely vanishing at one root.

Exhaustiveness on `D(p)` with nonzero linear `A0,C0`. Squarefree `L` has two distinct roots. The first-grade polar part of `AC/L` vanishes if and only if `L` divides `A0 C0`. A nonzero polynomial of degree at most 2 divisible by a squarefree quadratic must be a unit times `L`, so both `A0` and `C0` have degree exactly 1 and vanish at complementary roots. They cannot share a root: that would make `A0 C0` a square, hence `L` a square, hence `p=0`. Constant nonzero `A0` or `C0` cannot be complementary factors of `L`. The only remaining possibilities are the two opposite-root allocations.

---

## 9. Next cleared numerator at the allocated root

On the pos allocation, `C0_gen=cvg(1+rtx t)` and the `C^2` summand is

```text
H = (3/8) t^3 C0^2 Inv2 = (3/8) cvg^2 (t^3 + 2 rtx t^4 + rtx^2 t^5) Inv2
```

at grade `g+1`. Section 7 converts this to

```text
N = (3/8) cvg^2 (z + rtx)^2.
```

At the `A0` root `z=rtx`,

```text
N(rtx) = (3/8) cvg^2 (2 rtx)^2 = (3/2) rtx^2 cvg^2 = (3/2) lambda^2 cv^2.
```

The same value appears on the neg deck at `z=-rtx`. The compiled identity is that polynomial equality, in both orientations, identically in the remaining variables.

Every competing in-window term is a simple pole (denominator `L`, not `L^2`):

- first `A/C` jets of `AC/L`;
- the `sigma ell1` derivative of `Inv1` acting on leading `AC`. After allocation `A0 C0` is a multiple of `L`, so `ell1 AC/L^2` reduces to a simple pole `const/L`;
- `k10 RC/L` when `ord(R)=a`;
- `k10 R^3/L` when `a=ord(R)=2`.

A simple-pole numerator `N_s`, rewritten with denominator `L^2`, becomes `N_s L`. That vanishes at both roots of `L`. Therefore every moving-`p`, `A/C` correction, `RC`, and `R^3` contribution to `Nnext` vanishes at the allocated root for that licensed reason. The only genuine double pole in the window is `C^2/L^2`. The engine identity `Nnext(root)-(3/2) rtx^2 cvg^2=0` as a polynomial in `ell1, eta, aa*, cc*, b0, b1, k0, …` is the same statement.

Nonvanishing is then `p!=0` (so `lambda!=0`) and `cv!=0` (nonzero leading `C0`). Characteristic zero supplies `2,3`.

---

## 10. `eta` scope

`R` is compiled as `sigma^a eta (b1 z+b0)` with no grade-`a+1` jet. Arbitrary `eta` is exactly the leading section of exact contact `ord(R)=a`. Setting `eta=0` kills that section.

If `ord(R)>=a+1`, the in-window `R` terms move later:

- `k10 R^3/L` at `>=10+3(a+1)=13+3a`, which is at least `g+3`;
- `k10 RC/L` at `>=11+(a+1)+(a+1)=13+2a=(g+1)+1`.

Even for exact `r=a`, the first jet of `R` at order `a+1` produces `RC` only at `(g+1)+1` and `R^2 R1` only at `g+2` or later. No `R` jet beyond grade `a` is required through `g+1`. This is four fixed-`a` blocks with literal `sigma^a`, not a `eta=sigma^s` substitution after extracting a single window.

---

## 11. Inversions, set versus scheme

The root argument inverts `p` (squarefree `L`, etale roots `±rtx`) and uses nonzero linear `A0,C0` (degree 1, opposite roots). Nonvanishing of `(3/2) lambda^2 cv^2` inverts `p` again and the leading coefficient of `C0`. The ambient chart is `D(p*k10)` from the reviewed first-normal/half-weight hypotheses; `k10` is a chart unit, not a factor in the residue. No hidden inversion of `ell1`, `eta`, `b0`, or `L` occurs: `Nnext` is a polynomial, evaluated at a root, not divided by `L`.

The conclusion is that no formal arc with one of the four exact contact vectors exists on that chart. It is not a statement about the scheme structure of the source ideal (embedded components, multiplicity, nilpotents). `RESULT.md` and the firewall say so.

---

## 12. Dual AWS records

| | exact Q (characteristic-zero producer) | `F_65521` (software control) |
|---|---|---|
| host | `ip-172-30-0-249` (Box03) | `ip-172-30-0-45` (r6d) |
| tag | `..._q_20260826T120500Z_box03` | `..._p65521_20260826T120500Z_r6d` |
| launcher PID | `214524` | `275139` |
| characteristic | `0` | `65521` |
| VM cap | `25165824` KiB (24 GiB) | same |
| compile / engine caps | 600 s / 1800 s | same |
| `compiler_rc` | `0` | `0` |
| `compiler.stderr` | empty (`e3b0c442…`) | empty |
| `engine_rc` | `0` | `0` |
| validator | `PASS_D1_FINITE_BAND_A2_A5_FULLSUPPORT` | same bytes |
| stdout SHA-256 | `be11fa82…` | `be11fa82…` |
| wall / peak RSS | 0.10 s / 19504 KiB | 0.07 s / 15408 KiB |
| swaps | 0 | 0 |
| `.sing` SHA-256 | `0e6a3098…` | `8e4845e5…` |

`/usr/bin/time -v` is only in stderr, via frozen `ops/aws_exact_lane.sh`. Stdout is sixty-one marker lines plus the package endpoint; no coefficient dump, no `// **`, no leading `?`, no `error occurred`, no `=FAIL`. The validator requires each of the fifteen per-contact tokens exactly once, plus the package endpoint, and rejects `=FAIL`, `// **`, a leading `?` prompt, and `error occurred` on both stdout and stderr. That is the V12 radical-diagnostic repair. Exact Q is the characteristic-zero producer; `F_65521` differs by the eight ring-characteristic tokens only and is not a substitute for Q.

`RESULT.md` resource claims match the Q stderr: 0.10 seconds wall, 19504 KiB peak RSS, zero swap.

---

## 13. Firewall

Licensed: the four listed D1 contacts on `D(p*k10)`, subject to the reviewed generic-square first-normal and half-weight hypotheses, as an arcwise finite-band emptiness. Unlicensed, and not claimed: `a>=6`; positive-order or ramified `k10`; `p=0`; `k10=0`; zero/infinity receivers; fan exhaustiveness; scheme structure; the full square branch; order two; `(8,12)`; maximum twelve; JC2.

The next complete-source client is recorded as fixed `a=6,7`, where `k6 C/L` enters. That is outside this theorem.

The all-load Chebyshev/Pell survivor is the reduced support of `sqrt(Q)(k10 Q^2+k6 Q+k2)` in which `k6` and `k2` are comparable to `k10` and may cancel on a nonsquare Chebyshev component. Those lower loads do not occur through grade `g+1` on this unit-`k10` chart. A finite early-grade emptiness on `D(p*k10)` does not contradict a later combined-load cancellation locus. Later complete-support clients must keep that locus as a positive control, as `RESULT.md` states.

---

CONFIRMED
ORDER2_SQUARE_D1_FINITE_BAND_A2_A5_CONFIRMED
