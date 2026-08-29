# Hostile review — order-two generic-square `r=1` and symbolic unique-`AC`, `d=1` (V12)

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/` |
| Overall verdict | **REPAIR** |
| Smallest failing identity | none found in the claimed receivers |
| Smallest obstruction | both `r=1` stdout files still contain the Singular diagnostic `// ** R1_rad is no standard basis` (twice); `RESULT.md` asserts that no stdout contains a Singular diagnostic; the validator does not reject `// **` comments, so the `r=1` radical membership test is not Groebner-certified |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Stored PASS markers are evidence, never authority |
| Method | source reading, SHA-256 of every named pin and evidence file, byte-level V11/V12 and Q/`F_65521` comparison, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of `RESULT.md` is
`fe7a5c8a528b059c22118cc0256c180a9b455d8ba04637b5dc3ae2d3dbf95ae3`.
Independently recomputed SHA-256 of `RESULTS.sha256` is
`f06671486459aeb34a797e64ea4f8572cd01728218bb526d419ed6d326eda72a`.
Independently recomputed SHA-256 of `FREEZE.sha256` is
`decc00a91c952354902da2eeeeac6eb9c7fdc06748bf5f96957f45617e07743a`.
Independently recomputed SHA-256 of the two design authorities match the
required pins. Every path named in `RESULTS.sha256` (41 files) rehashes to
its printed digest. The V12--V1 freeze chain, including the shared-Faber
`tails.json` pin, rehashes. No file other than this review was written.

The two producer statements do not disagree about the geometry: both
`RESULT.md` theorems are claimed as dual-AWS producer pass, and
`REGISTRATION.md` only withholds promotion pending review. They do disagree
about software cleanliness. `RESULT.md` asserts that no stdout contains a
Singular diagnostic. Both actual `r=1` stdout files do. The exact
conjunction claimed is therefore not confirmed.

---

## Verdict

**REPAIR.**

On the reviewed generic-square first-normal chart `D(p*k0)`, after the
half-weight support gate, the normalized `r=1` substitutions produce a
complete seven-row source vector at absolute grade 13 which is the
lower-unitriangular Faber image of the proper part `(5/16) k0 R0^3/L0` with
`L0=z^2+p/2`. Vanishing of that proper part forces both coefficients of the
linear `R0` to vanish, by an elementary remainder calculation that does not
need a Groebner basis. That is contact-raising of the normalized receiver,
not a silent change of contact, and it is set-theoretic.

The symbolic unique-`AC` substitution with free `theta,eta` covers exactly
`a=2+n`, `c=a+1`, `r=a+s` for integers `n,s>=0` without inverting either
scale. The three successor modules are the complete next-grade split of the
pinned lower-hull `d=1` cell. Complete source-to-Laurent identities at
grades 15 and 16 are a genuine tails-versus-analytic bridge. After the
etale splitting of `L0` and opposite-root allocation, the grade-16 proper
numerator evaluates to `(3/2) lambda^2 cv^2 theta^2` at both deck
orientations; every competing `RC`, `R3`, moving-`L`, higher-correction, and
load term is at most a simple pole there and vanishes in the allocated
numerator. That quantity is nonzero on the unique-`AC` chart with nonzero
leading `C` and `p!=0`.

V12 changes only the claimed five recurrence spellings in the D1 block,
byte-for-byte, and leaves `r=1` identical to V11/V8. Exact Q carries
characteristic zero; `F_65521` differs by the two ring-characteristic tokens
only.

The load-bearing failure is the `r=1` radical certificate. Both engines
print

```text
// ** R1_rad is no standard basis
```

twice, then `R1_LOCALIZED_REDUCED_SUPPORT_ZERO=1`. Singular is warning that
`reduce(b0,R1_rad)` and `reduce(b1,R1_rad)` are not Groebner remainders.
The validator accepts this because it only rejects `=FAIL` and a leading
`? ` prompt. `RESULT.md` nonetheless claims that no stdout contains a
Singular diagnostic. Q9 required that verification. The software radical
step is therefore not a proof, even though the same support conclusion is
available by hand. That is a missing certified step, not a false geometric
claim.

Repair is: `std` the radical before `reduce`, or replace the radical block
by the elementary case analysis of `e0,e1` below; make the validator reject
`// **` diagnostics; and retract the cleanliness sentence in `RESULT.md`.
Do not promote on the present bundle.

**REPAIR**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Ancestry regenerates seven source tails | first-normal substitutions, loads, gauges, signs, row order, grades, denominators | **holds**; neither input is an analytic-only surrogate |
| 2. Grade-13 proper part `(5/16) k0 R0^3/L0` | independent expansion plus unitriangular Faber | **holds**; seven rows are an invertible lower-unitriangular image |
| 3. Exact-Q radical on `D(p*k0)` | localization, support of linear `R0`, scheme vs set, contact | localization is represented; hand algebra forces `b0=b1=0`; software `reduce` against a non-GB radical is **not certified**; set-theoretic only; `R0=0` is contact-raising |
| 4. Symbolic D1 substitution | `theta=sigma^n`, `eta=sigma^s`, no inversion | **holds** for all integers `n,s>=0` |
| 5. Three successor modules | lower-hull ties, moving `L`/`p` | **exhaustive** on the pinned `d=1` cell; moving-`p` connection is in the grade-16 Faber bridge |
| 6. Source-to-Laurent at grades 15 and 16 | seven rows, recurrence, degree bounds, independence | **holds**; tails versus `universal_hshift`, not two copies of one formula |
| 7. Etale split, AC/L allocation, four maps | 27-variable order, both decks, faithful chart, nonvanishing factors | **holds** |
| 8. Grade-16 allocated residue `(3/2) lambda^2 cv^2 theta^2` | all three modules, competing terms, nonvanishing | **holds** by hand; nonzero on the unique-`AC` chart with `p*cv*theta!=0` |
| 9. V1--V12 history and cleanliness | five recurrence spellings, polynomials/guards, no diagnostic, Q vs `F_65521` | spellings **hold**; the `r=1` radical diagnostic **remains**; exact Q is the characteristic-zero lane |
| 10. Firewall | licensed vs unlicensed claims | producer firewall **matches** the required scope; a positive verdict would still license only that |

---

## 1. Custody

Recomputed SHA-256 of the named pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `RESULT.md` | `fe7a5c8a528b059c22118cc0256c180a9b455d8ba04637b5dc3ae2d3dbf95ae3` | producer report |
| `RESULTS.sha256` | `f06671486459aeb34a797e64ea4f8572cd01728218bb526d419ed6d326eda72a` | evidence manifest |
| `FREEZE.sha256` | `decc00a91c952354902da2eeeeac6eb9c7fdc06748bf5f96957f45617e07743a` | source freeze |
| `REGISTRATION.md` | `a90bbc2ab84cc9c05c68b373f4b250152298cbf1f2f0a65afcf7bd96911a40c7` | registration |
| `compile_v12_recurrence_products.py` | `cb1b07bb679c1149bc2671c2ed88417352c0708787f8362756ed3ffb12d3a88a` | V12 compiler |
| exact-Q `square_r1_v12_q.sing` | `e253681e155c0cbbc2c2984ecd6eeb7b5edfcb3e75b7b0c5649ec1051be7e5b3` | compiled `r=1` |
| exact-Q `square_d1_ac_v12_q.sing` | `9ea31841e78ffdf927509b4e15aa4505c7c31c0acfe39a32cb3f3040007f9845` | compiled D1 |
| `F_65521` `square_r1_v12_p65521.sing` | `e388c06b366dbcf083529861ad94de0184105125c90d8e4a595eb75c9d184bc3` | compiled `r=1` |
| `F_65521` `square_d1_ac_v12_p65521.sing` | `73fd282452e7f4a1b8bcb708b8678ed7d1729246a88ea0641f34473c124dced5` | compiled D1 |
| marker-only `r=1` stdout (both fields) | `8adb20f408c987d72d346224d92bfcbb2af441a2ee82107434d1caf3f0b1ef25` | engine stdout |
| marker-only D1 stdout (both fields) | `c56b388cfc8f3b4cee41c9976d55012662529b885693d9c1b83f7593db154044` | engine stdout |
| both `validation` files | `d58eedfdb10620e85b1a4c19f44366a6a2fcc03afaf79d36141f20fc89e77247` | validator payload |
| lower-hull design | `c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d` | weight authority |
| closure criterion | `3c0a33ceddfad8ca69afb145ae5249f0d2b4866c5a8af498d257e9d4a78cfd95` | arcwise lemma |

Every `RESULTS.sha256` row matches. The freeze walker V12 → V11 → V10 → V9 → V8 → V7 → V6, and the V1 freeze through `compile_cge3_universal.py`, `tails.json`
(`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`),
canonical all-tails digest
`6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`,
and `compile_square_load_ladder.py`, all rehash.

Exact Q (Box03) and `F_65521` (r6d) are separate frozen runs: distinct hosts,
tags, PIDs, compiled-script hashes, stderr hashes, and `.meta` files. The
identical validation bytes are the same three-line validator payload, not a
cloned run. All four engine records have `rc=0`. Peak RSS is about 14–15 MiB
with zero swap; wall-clock is 0.02–0.03 s, consistent with sparse
low-degree polynomial identities rather than a hard Groebner search.

Both validators (`aws_q_box03/validation` and `aws_p65521_r6d/validation`)
print

```text
r1_engine_rc=0
d1_engine_rc=0
validator=PASS_R1_D1_AC_SYMBOLIC_V12_RECURRENCE_PRODUCTS
```

The validator source in `run_aws.sh` requires each listed PASS token to occur
exactly once, then rejects `=FAIL` and a leading `? ` prompt. It does not
inspect `// **` comments. That gap is the custody-level reason the leftover
radical diagnostic survived a dual-AWS PASS.

`AWS_LAUNCH_METADATA.md` names the preregistration `2026-08-26T11:20Z`; the
four `.meta` records start at `11:09:14Z` / `11:09:16Z`. The lane tags still
carry `T112000Z`. This is a naming offset, not an evidence mutation.

---

## 2. Question 1 — source typing through the V12--V1 chain

**Verdict: holds.** Neither compiled input is an analytic-only surrogate.

V1 `compile_r1_d1_ac.py` loads the frozen cge3 module, checks that module's
`EXPECTED` pins including `tails.json` and the load-ladder compiler, and
rechecks the canonical all-tails digest. Each of the seven ordinary
coordinates is

```text
base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
```

with target subtractions `mu2`, `mu4`, `mu6`, `J/4` on rows 2, 4, 6, 7.
`tail_text` enforces monomial length, load linearity, and weight `12+row`
against the frozen Faber names. The compiled `r=1` `Phi1..Phi7` are those
expanded tails with the first-normal coefficient substitution, not a
hardcoded Laurent polynomial.

First-normal substitutions in the V1 emitter, visible in the compiled
scripts:

| Object | `r=1` | D1 |
|---|---|---|
| `p` | frozen `p` | `p+2*sigma*ell1` |
| `A` | `sigma*(a1 z + a0)` | `sigma^2*theta*((a1 z + a0)+sigma*(aa1 z + aa0))` |
| `C` | `sigma^3*(c1 z + c0)` | `sigma^3*theta*((c1 z + c0)+sigma*(cc1 z + cc0))` |
| `R` | `sigma*(b1 z + b0)` | `sigma^2*theta*eta*(b1 z + b0)` |
| `k10` | `k0` | `k0` |
| lower loads | `k6`, `k2load` present, then forbidden at the extracted grade | same |
| `L0` | `z^2+p/2` | moving `sp=p/2+sigma*ell1` |

The coefficient encoding matches the load-ladder / cge3 convention after the
documented insertion of the factors 2 and 4: `kc=sigma^2*(rz)`,
`kr=(pp)^2/4+sigma^2*(rc)`, and `n1=sigma^3*((pp*az)/2+cz)`. Direct
polynomial `C,R` therefore land on the same Faber slots as the older
`C=(e31 z+e30)/2`, `R=bs z + br/4` chart.

Gauges, signs, and row order: rows 1–7 in increasing ordinary index;
Faber diagonal 1; odd-delta entries zero; even-delta binomial coefficients
`(1/4)p`, `(1/2)p`, `(3/32)p^2`, `(3/4)p`, `(1/4)p^2`, `p`, `(5/128)p^3`,
`(15/32)p^2`, `(5/4)p` as in the compiled `Check` identities. Absolute
grades: 13 for `r=1`; 15 and 16 for D1. Denominator convention: `r=1` uses
`L0` (simple pole, proper numerator degree `<2`); D1 grade 15 uses `L0`,
grade 16 uses `L0^2` (proper numerator degree `<4`).

V2–V5 are identifier-only. V6 replaced the D1 root evaluator by four chart
ideals, later discarded. V7 expanded `rtx^2`, `cv^2`, `theta^2` in that
chart block. V8 split `r=1` and D1 at `ring Rd1=` and kept `primdec.lib`
only in `r=1`. V9–V12 copy `r=1` byte-for-byte (exact-Q SHA frozen at V8:
`e253681e...`) and only rewrite the D1 terminal evaluator, then the
recurrence serialization, then five power spellings. A syntactically
successful patch chain is not itself a typing proof; the typing proof is
that V1 still emits `tail_text` of the pinned tails under the substitutions
above, and no later patch replaces those `Phi` polynomials.

The printed `R1_SOURCE_HASHES=PASS` / `D1AC_SOURCE_HASHES=PASS` tokens are
unconditional prints. The actual digest check is compile-time in V1. That
is acceptable because the compiled scripts are frozen outputs of that
compiler.

---

## 3. Question 2 — grade-13 proper part and unitriangularity

**Verdict: holds.**

After the half-weight gate the negative receiver of the generic square, at
the common absolute grade ten, is

```text
[(3/8) D^2/L^2 + (5/16) k10 R^3/L ]_-,    D=LA+C.
```

On the normalized `r=1` chart put

```text
A=sigma A0,   C=sigma^3 C0,   R=sigma R0,   k10=k0,
```

with `A0,C0,R0` linear (first-normal: degrees `< deg L0=2`) and `L0` frozen.
Valuations of every displayed term:

| Term | sigma order | absolute grade |
|---|---|---|
| `(3/8) A^2` | `sigma^2` times `sigma^10` | 12, polynomial in `z`, dropped by `[_-]` |
| `(3/4) AC/L` | `sigma^{4}` times `sigma^10` | 14 |
| `(3/8) C^2/L^2` | `sigma^{6}` times `sigma^10` | 16 |
| `(5/16) k0 R^3/L` | `sigma^{3}` times `sigma^10` | **13** |
| `(5/8) k0 R C /L` | `sigma^{1+3}` times `sigma^11` | 15 |
| `(5/32) k0 R^2 A /L^2` | `sigma^{2+1}` times `sigma^13` | 16 |
| `(5/32) k0 A^2 /L` | `sigma^{2}` times `sigma^14` | 16 |
| `A^3 / L^3` | `sigma^{3}` times `sigma^15` | 18 |

No other first-normal term enters at grade 13. The truncated inverses
`Inv2=Inv3=1` in the `r=1` analytic generating function are therefore
harmless at this grade: those denominators multiply terms already above
grade 13. The surviving proper part is exactly

```text
(5/16) k0 R0^3 / L0,    L0=z^2+p/2.
```

The compiled analytic `R1_Hshift` is this generating function, including
the inert higher terms. The compiled numerator identity is

```text
reduce(R1_N - (5/16)*k0*R1_R^3, ideal(L0)) == 0
```

with `R1_N=R1_h13_1*z+R1_h13_2` and `R1_R=b1*z+b0`, i.e. the proper
numerator of degree `<2`.

Faber transform at frozen `p`, offset 0 (no `ell1` in the `r=1` ring):

```text
g1 = h1
g2 = h2
g3 = (1/4) p h1 + h3
g4 = (1/2) p h2 + h4
g5 = (3/32) p^2 h1 + (3/4) p h3 + h5
g6 = (1/4) p^2 h2 + p h4 + h6
g7 = (5/128) p^3 h1 + (15/32) p^2 h3 + (5/4) p h5 + h7
```

Lower unitriangular with unit diagonal, hence invertible over `Z[1/2]`.
Characteristic zero, and `F_65521`, both invert 2. Seven vanished source
rows therefore vanish all seven Laurent coefficients. The `L0`-recurrence
`h_{j+2}+(p/2) h_j=0` for `j=1..5` then says the seven coefficients are
the expansion of a unique degree-`<2` numerator, so they vanish if and only
if `N=0`.

---

## 4. Question 3 — radical, localization, contact

**Verdict: localization and the support conclusion hold by hand; the
software radical step is not certified.**

Localization on `D(p*k0)` is represented by the standard chart equation
`inv*p*k0-1` inside

```text
R1_I = std(ideal(R1_e0, R1_e1, inv*p*k0-1)).
```

Write `R0=b1 z+b0` and reduce `R0^3` modulo `L0=z^2+p/2`, using `z^2=-p/2`
and `z^3=-(p/2)z`:

```text
rem = [ 3 b1 b0^2 - (p/2) b1^3 ] z + [ b0^3 - (3p/2) b1^2 b0 ].
```

So

```text
e1 = b1 ( 3 b0^2 - (p/2) b1^2 ),
e0 = b0 ( b0^2 - (3p/2) b1^2 ).
```

On `D(p)` the system `e0=e1=0` forces `b0=b1=0`:

- `b1=0` ⇒ `e0=b0^3=0` ⇒ `b0=0`;
- `b0=0` ⇒ `e1=-(p/2) b1^3=0` ⇒ `b1=0`;
- both nonzero ⇒ `p b1^2 = 6 b0^2` and `2 b0^2 = 3 p b1^2`, hence
  `2 b0^2 = 18 b0^2`, so `16=0`, contradiction in characteristic not 2.

This is set-theoretic support of the linear `R0`. The raw ideal may retain
multiplicity; scheme structure is not claimed and is firewalled.

The compiled test is `reduce(b0, R1_rad)==0 && reduce(b1, R1_rad)==0` after
`R1_rad=radical(R1_I)`. Both `r=1` stdout files, on exact Q and on
`F_65521`, insert

```text
// ** R1_rad is no standard basis
// ** R1_rad is no standard basis
```

between `R1_NUMERATOR_IDENTITY=1` and `R1_LOCALIZED_REDUCED_SUPPORT_ZERO=1`.
That is Singular reporting that `R1_rad` is not a standard basis, so those
`reduce` calls are not Groebner remainders. Membership is therefore not
software-certified. The hand calculation above is the proof; the engine
marker is not.

`R0=0` does not silently change contact. The substitution was
`R=sigma R0` with `R0` the declared leading linear section of the
normalized `r=1` receiver. Forcing `R0=0` says that this receiver has no
arc with a nonzero order-one leading section. Higher contact, or `R=0`
identically, is a different face and must be routed by the pinned closure
criterion. The producer statement matches that: no finite-order arc in this
normalized receiver has a nonzero leading `R0`. The closure criterion's
demand to invert declared leading units applies to units that are supposed
to stay nonzero; here the leading of `R` is the unknown being killed, so it
must not be inverted.

---

## 5. Question 4 — symbolic unique-`AC` substitution

**Verdict: holds.**

The compiled D1 coefficients are

```text
A = sigma^2 theta (A0 + sigma A1),
C = sigma^3 theta (C0 + sigma C1),
R = sigma^2 theta eta R0,
pp = p + 2 sigma ell1,
```

with `A0,A1,C0,C1,R0` linear and `theta,eta` indeterminates in the ring.
Interpreting `theta=sigma^n` and `eta=sigma^s` as series gives

```text
ord(A)=2+n,   ord(C)=3+n,   ord(R)=2+n+s,
```

i.e. `a=2+n`, `c=a+1`, `r=a+s`. Integers `n,s>=0` are exactly the closed
unique-`AC` `d=1` cell `a>=2`, `c=a+1`, `r>=a` of the pinned lower-hull
lemma. Neither `theta` nor `eta` is inverted, specialized to a nonzero
constant in the source extraction, or placed in a denominator. The
identities

```text
H15 = theta^2 H15unit,
H16 = theta^2 H16base + theta^2 eta H16rc + theta^3 eta^3 H16r3
```

are polynomial in `theta,eta` and are checked as such. Substituting
`theta=1` or `eta=0` occurs only when extracting homogeneous components for
that decomposition, not when forming the source rows.

---

## 6. Question 5 — successor modules and moving connection

**Verdict: the three modules are exhaustive on the pinned cell.**

From the lower-hull note, unique-`AC` has `1<= d:=c-a <=3` and `s:=r-a>=0`
with `a+3s>d`. The whole `d=1` family is `a>=2`, `c=a+1`, `r>=a`. Relative
to the first `AC` weight, the gaps are

```text
C2:  d=1,
A2:  4-d=3,
RC:  1+s,
R3:  a+3s-d=a+3s-1,
RA2: a+s+2-d=a+s+1,
A3:  a+5-d=a+4.
```

Next grade is gap 1.

- `(n,s)=(0,0)`: `(a,c,r)=(2,3,2)`. Then `C2`, `RC`, and `R3` all have gap
  1. Unique equality `a+3s-1=1` at this point. Module `C2,RC,R3`.
- `n>=1`, `s=0`: `a>=3`, `r=a`. `C2` and `RC` have gap 1; `R3` has gap
  `a-1>=2`. Module `C2,RC`.
- `s>0`: `RC` has gap `>=2`; `R3` has gap `>=a+2>=4`. Only `C2`. Module
  `C2`.

Closed-cell comparisons with the five unit-load generators, at `c=a+1`,
`r=a+s`, `a>=2`:

```text
a <= c                 always,
a+c = 2a+1 <= 3r=3a+3s always (and equality would need a=1,s=0, off-cell),
a <= r+1               always,
c <= a+4               always.
```

`A2`, `RA2`, `A3` never meet the next grade on this cell. The RA2 exception
locus of the hull lemma is `(a,r)=(1,2)`, `c>=5`, disjoint from `a>=2`,
`c=a+1`.

Moving `L`: D1 uses `pp=p+2 sigma ell1` and `Inv1,Inv2,Inv3` in `sp`. The
grade-16 Faber identities contain the first moving-`p` summands, e.g.

```text
g16_3 = (1/4) p h16_1 + (1/2) ell1 h15_1 + h16_3,
```

which is exactly `t1` from `transform_series` at `n=1`. Offset 1 at grade
16; `t2` (which would need `ell2`) is never referenced, matching the
absence of `ell2` from the D1 ring. The first connection of already
polynomial `AC/L` therefore arrives as a simple pole at the next grade and
is retained. The residue lemma's warning that a double pole two grades
later can mix with second-order motion applies to `(1,3)`, not to this
cell: here the double pole is one grade after `AC`.

---

## 7. Question 6 — source-to-Laurent at grades 15 and 16

**Verdict: holds, and is independent.**

Source rows are `tail_text` of the frozen tails under the D1 substitutions.
The analytic generating function is `universal_hshift`, which unlike the
cge3 grade-13--15 formula includes the `(3/8) sigma^10 t^3 C^2 Inv2` term.
That term is the `C2` double pole, valuation `sigma^{16+2n}`, and is
required at grade 16. Matching `g` against `T(h)` for all seven rows at
both grades is therefore a comparison of two independently constructed
expressions, not two copies of one formula, and not a hardcoded expected
polynomial in the source slots.

The hardcoded `(3/2) rtx*rtx*cvg*cvg*theta*theta` is the residue claim, not
the source bridge. Recurrence:

- grade 15, simple pole: `h_{j+2}+(p/2) h_j=0`, proper numerator
  `N15=h1 z+h2`, degree `<2`;
- grade 16, double pole: `h_{j+4}+p h_{j+2}+(p^2/4) h_j=0` for `j=1,2,3`,
  proper numerator the unique degree-`<4` polynomial
  `N16=h1 z^3+h2 z^2+(h3+p h1)z+(h4+p h2)`.

Seven rows suffice by these degree bounds. V11's serialization guard still
requires `D1AC_rec15==1` and `D1AC_rec16==1` before printing the
denominator tokens as the literal `1`.

---

## 8. Question 7 — etale split, allocation, four maps

**Verdict: holds.**

On `D(p)`, `L0=z^2+p/2` is squarefree. The etale chart is `p=-2 rtx^2`, so
`L0=(z-rtx)(z+rtx)`. Opposite-root allocation:

- positive: `a1=aua`, `a0=-aua rtx`, `c1=cvg`, `c0=cvg rtx`
  (`A0=aua(z-rtx)`, `C0=cvg(z+rtx)`);
- negative: `a0=+aua rtx`, `c0=-cvg rtx` (deck swap).

The four maps from `Rd1` to `Rd1eval` have 27 images in the ring-variable
order

```text
z, t, sigma, p, ell1, theta, eta, a0, a1, aa0, aa1, c0, c1, cc0, cc1,
b0, b1, k0, k6, k2load, mu2, mu4, mu6, J, rtx, aua, cvg
```

with `p |-> -2 rtx rtx` and the two allocations above; `posroot`/`negroot`
further send `z |-> ±rtx`. The unused extra variables `rtx,aua,cvg` in
`Rd1` map to themselves. The map is the etale chart, not an injective ring
map; it is faithful for the evaluation identity on `D(p)` after adjoining
`sqrt(-p/2)`. Both orientations are checked. Nonvanishing chart factors
are `rtx` (equivalently `p`), `cvg` (leading of allocated `C0`), and
`theta` (the `A,C` scale, geometrically `sigma^n`). Grade 15 numerators
map to 0; that is the first `AC/L` allocation.

---

## 9. Question 8 — grade-16 residue

**Verdict: holds. The unmatched value is exactly `(3/2) lambda^2 cv^2 theta^2`.**

At the positive root, `C0=cv(z+lambda)` and `L0=(z-lambda)(z+lambda)`, so

```text
C0^2 / L0^2 = cv^2 / (z-lambda)^2.
```

The `(3/8) C^2/L^2` contribution has `L0^2`-numerator
`(3/8) cv^2 (z+lambda)^2` (already degree `<4`). Evaluating at `z=lambda`:

```text
(3/8) cv^2 (2 lambda)^2 = (3/2) lambda^2 cv^2.
```

Times `theta^2` this is the claimed value. The negative orientation is the
same with `lambda |-> -lambda`.

Competing same-grade terms, after allocation `A0(lambda)=0`, `L0(lambda)=0`,
as `L0^2`-numerators evaluated at the root:

| Term | Pole at allocated root | `N(lambda)` |
|---|---|---|
| `C^2/L^2` | double, `cv^2/(z-lambda)^2` | `(3/2) lambda^2 cv^2 theta^2` |
| first moving-`L` of `AC/L` | `A0 C0 / L0 ~ 1/L0`, simple | numerator contains `L0`, vanishes |
| `RC ~ k R0 C0 / L0` | simple | numerator contains `L0`, vanishes |
| `R3 ~ k R0^3 / L0` | simple | numerator contains `L0`, vanishes |
| `A1 C0 / L0`, `A0 C1 / L0` | simple | vanish |
| `k A^2/L`, `k R^2 A/L^2`, `A^3/L^3`, `R A^2/L^2` | above grade 16 at `n=0` | absent |

The scale identity writes every grade-16 analytic term as one of
`theta^2` (the `C2` plus moving-`L` module), `theta^2 eta` (`RC`), or
`theta^3 eta^3` (`R3`). The residue identity is polynomial in `eta` and
`ell1` as well as in the jets `aa,cc,b,k0`, so it covers all three modules
at once. Nonvanishing: on `D(p)` one has `lambda^2=-p/2!=0`; unique-`AC`
with finite `c=a+1` has `C0!=0`, hence `cv!=0` because `z±lambda` is
monic; `theta=sigma^n` is a nonzero series. The registered localization
`D(p*k0)` is stronger than needed for this residue (`k0` does not appear),
and is not a hole.

The closure criterion requires inverting declared leading units to obtain a
unit-ideal certificate. The software checks a polynomial identity, not an
inverted unit. The geometric step “this polynomial is a unit on the
unique-`AC` chart” is the missing explicit localization at `cv*theta`. It
is implied by the cone, and is not an unstated extra hypothesis about
orders, but a promotion package should invert those factors rather than
leave them in the residue.

---

## 10. Question 9 — V1--V12 history

**Verdict: the five recurrence spellings hold; the no-diagnostic claim fails.**

Byte-level comparison of exact-Q D1 V11 versus V12: prefix before
`poly D1AC_N15=` and suffix from `ring Rd1eval=` are identical. The
recurrence block differs by exactly

```text
z^3 -> z*z*z     (once)
z^2 -> z*z       (once)
p^2 -> p*p       (three times, all in `p^2/4`)
```

Replaying those five replacements on the V11 block reproduces the V12 file.
Mathematical polynomials and fail-closed guards are unchanged. `r=1` V12 is
byte-identical to V11 and to V8 (SHA `e253681e...`). Exact-Q versus
`F_65521` differs by the ring-characteristic token on `Rr1` for `r=1`, and
by the two tokens `Rd1` and `Rd1eval` for D1.

V1–V7 failed closed at the terminal root block after source/row/scaling
sentinels. V8 isolated processes. V9 substitutions, V10 four maps, V11
literal recurrence prints. Those are software controls, not theorems.
Exact Q is `ring Rr1=0` and `ring Rd1=0`; it carries the characteristic-zero
assertion. `F_65521` is a software control; 2, 3, 5, and the binomial
denominators in the Faber matrix are invertible there.

Both `r=1` stdout files still contain a Singular diagnostic, as quoted in
the verdict. No `=FAIL` marker is present. The cleanliness half of Q9
therefore fails.

---

## 11. Question 10 — firewall

**Verdict: the producer firewall matches the required license.**

A positive verdict would license only arcwise, set-theoretic elimination of
the normalized `r=1` receiver and of the unique-`AC` subcone
`a>=2`, `c=a+1`, `r>=a` on `D(p*k0)`, subject to the frozen first-normal
hypotheses (linear `A,C,R`, `K=L^2`, unit load, generic-square substitutions
after the half-weight gate). It would not cover `(1,3)`, `(1,4)`, other
AC/RC/RA2 faces, positive-order or ramified loads, `p=0`, `k0=0`,
zero/infinity sections, fan exhaustiveness, scheme structure, the whole
square branch, exact order two, maximum twelve, or JC2.

`RESULT.md` states that firewall. This review does not promote even that
restricted license, because the `r=1` radical certificate is not clean.

---

## Strongest surviving theorem

Hand identities, independent of the non-GB `reduce`, give:

On the reviewed generic-square first-normal chart `D(p*k0)`, the normalized
receiver `ord(A)>=1`, `ord(C)>=3`, `R=sigma R0` with `R0` linear has
complete source at grade 13 equal to the Faber image of
`(5/16) k0 R0^3/L0`. Vanishing forces `R0=0` as a linear polynomial. No
arc in this normalized receiver has a nonzero order-one leading section.

On the same open, the symbolic unique-`AC` family `a=2+n`, `c=a+1`,
`r=a+s` (`n,s>=0`) has complete source at grades 15 and 16 agreeing with
the analytic Laurent rows. After opposite-root allocation of the first
`AC/L` equation, the grade-16 proper numerator equals
`(3/2) lambda^2 cv^2 theta^2` at both deck orientations. That is nonzero
whenever the unique-`AC` leading of `C` and the etale root are nonzero.
The three next-grade modules are exhaustive for this cell.

These geometric claims are not promoted on this bundle, because the frozen
`r=1` engine certificate still emits a Singular diagnostic and uses an
uncertified radical reduction.

## Exact scope

Normalized `r=1` and unique-`AC` `d=1` only, first-normal, unit load,
`D(p*k0)`, arcwise and set-theoretic, pending a repaired `r=1` radical
block and a validator that rejects `// **` diagnostics.

## Sharpest non-claim

Not `(1,3)`, not `(1,4)`, not other AC/RC/RA2 faces, not ramified or
positive-order loads, not `p=0` or `k0=0`, not zero/infinity sections, not
fan exhaustiveness, not scheme structure, not the whole square branch, not
exact order two, not maximum twelve, not JC2.

---

ORDER2_SQUARE_R1_D1_V12_REPAIR
