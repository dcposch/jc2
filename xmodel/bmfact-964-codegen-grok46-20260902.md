# BMFACT-964-CODEGEN — braid decision pipeline for the realized (9,6,4) curve

**Lane.** `BMFACT-964-CODEGEN`. Date 2026-09-02. Agent grok-4.6.
**Charge.** Clone the proven (9,6,2) SIROCCO / Hurwitz pipeline onto the
HF-twin parametrization, now six-nodal by a four-for-four CONFIRMED
review, and decide its `S_4` representation existence on *this curve*.
**Method.** Exact `sympy` over `QQ` in-lane; Sage SIROCCO is env-gated
and AWS-only (not executed here). No `sat()`, no msolve, no ledger
edit, no `jc2-lean`. FALLACY-v2 in force. No exit price is asserted;
`charge_basis` is inapplicable.

**Headline.** The pipeline is emitted. The implicit equation, bidegree,
identity substitution, and discriminant census all replay in `sympy`
and match 964-NODALITY-REVIEW item (4) exactly: degree-8 squarefree
tangency octic, one four-node fibre at `x=0`, two one-node fibres at
the new-node abscissae, exponent ledger `8+2(4+1+1)=20`. Enumerator
self-controls all pass (72 / 0 / pruner cert). The native decision
token is not claimed: SIROCCO JSON does not exist in this lane.

This curve is a `REPRESENTATIVE`, not `FULL_ACTUAL_EXIT` of the census
row. A later `NATIVE_ZERO_CURVE_ONLY` would decide this witness only.
A `SURVIVOR` would be a representation of `pi_1(C^2-D)`, not a Keller
map. Neither is a row-level kill.

---

## 0. Custody

Frozen charged inputs, hashed on this host with `shasum -a 256`
**before any reading**. All three match the charge exactly:

```text
402ec9e18dcec798b46210cc4acb6b3282acbfcde14d48252c6cb89c078f24e5  [frozen]/964-nodality-review-grok46-20260902.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  [frozen]/rep-96-inner-opus5-20260901.md
7cef355be1af63e71bc24361955ad19755598c3925fa1cb2612e62e186f4a35b  [frozen]/hf-twin-964-grok46-20260831.md
```

Clone sources, hashed in the repo (read, not modified), both match:

```text
2d18c1183d8ba5d7db8db767b38929064303422deadab41857e4c1a49d82d916  box/bmfact_962.sage
b51813adcf7a407f97c486995f7f99ba73f616d0f04594506a069757bdbf832b  box/bmfact_enum.py
```

Line citations `REV:L`, `REP:L`, `HF:L` refer to the frozen copies.
Campaign FALLACY-v2 is in force. The 962 sibling died at the output cap
before writing its report; this lane writes the report per-section and
seals at completion.

**Ring map (FALLACY variable/ring).** Coefficient field `QQ`. Parameter
ring `QQ[t]`. Affine ring `QQ[coord_x, coord_y]` with generator order
`(coord_x, coord_y)` so Sage `braid_monodromy` projects over the first
variable. Elimination ring `(QQ[coord_x,coord_y])[param_t]`. Image
check: `F(p(t), q(t)) = 0` as a polynomial, and the primitive
`Res_t(p-x, q-y)` is a unit times the identity-substitution resultant
in `z=t^2` (below). Matching names are not a map proof. No `sat()`.
Remainders are taken in the declared univariate quotients (leaders
`u^2+35/8`, `v+11/8` from the review, and `z`-reduction of the
identity pair), including the zero remainder.

---

## 1. Clone policy and the two footguns kept

`box/bmfact_964.sage` is a clone of `box/bmfact_962.sage`, not a rewrite.
Conventions (B1)–(B7) of the 962 header are kept: first-variable
projection, geometric-basis orientation, Sage Tietze, left Hurwitz
with rightmost letter first, affine `pi_1(C^2-D)` (no projective
relation `xi_9...xi_1=1`). Dialect: no variables named `pi`, `gamma`,
`I`, or `O`.

Two coordinator footguns diagnosed on the 962 run are kept:

- **#10.** Sage `squarefree_part()` divides by the maximal square
  factor. On this discriminant that would drop `X^8` and the squared
  new-node quadratic and report support degree 8 instead of 11.
  Distinct support is `radical()`. The 964 precheck uses
  `disc_univariate.radical()` and, separately, exact `quo_rem` by
  `X^8` and by `(134217728 X^2+3087315)^2`.
- **#11.** `sage script.sage` on conda-forge Sage 10.9 does not set
  `__name__=="__main__"` (zero output, `rc=0`). The coordinator runs
  via `sage.repl.preparse.preparse_file`, prepends `sage.all_cmdline`,
  then `python bmfact_964_pp.py <mode>`. The `__main__` guard is kept
  as the python entry. Monodromy remains env-gated:
  `BRAID_JOB_RUN_MONODROMY=1` is required; SIROCCO is AWS-only.

---

## 2. Parametrization (charged, not re-derived as a search)

From `REV:59-63` / `HF:120-122`, the HF-twin polynomial member:

```text
x = p(t) = t^9 + 3 t^7 + (21/4) t^5 + (35/8) t^3 + (63/32) t
y = q(t) = t^6 + 2 t^4 + (5/2) t^2 + 3/4
```

Write `q0 = t^6 + 2 t^4 + (5/2) t^2`, so `y = q0 + 3/4`. This is the
shared constant-zero chart of the encoding-faithfulness audit. Sequence
`(r_0,r_1,r_2)=(9,6,4)`. The review confirmed six ordinary nodes:
four banked `{t,-t}` on `x=0`, plus two at `v=-11/8`, `u^2=-35/8`,
images `y=21/512`, `x=-297 u/4096`. Immersive (`gcd(p',q')=1`).
`Delta_aff=6`. Representative, not row-attainment.

`k_* = -8` from REP-96 §1 (exact Puiseux of this curve, and
`k_* = 2d - a - beta_1 = 15-23`). GATE-3 residue `k_* ≡ 0 (mod 4)`
admits `const-4c` and `noncst-T`, not `noncst-4c`.

---

## 3. Derivation of the implicit equation `F(x,y)`

### 3.1 The audit-trail identity, replayed

Charged identity (`AUD` as quoted in the prompt; equivalently
`y^3-p^2 = 27/1024 (8t^4+13t^2+16)` from `REV:67-68` / `HF:127-129`).
Because `y = q0+3/4` expands as

```text
y^3 = q0^3 + (9/4) q0^2 + (27/16) q0 + 27/64,
```

the two forms are the same polynomial:

```text
p^2 - q0^3 - (9/4) q0^2 - (27/16) q0 - 27/64
  = -(y^3 - p^2)
  = -27/1024 (8 t^4 + 13 t^2 + 16).
```

In-lane `sympy` over `QQ`, verbatim:

```text
ident = -27*t**4/128 - 351*t**2/1024 - 27/64
rhs   = -27*t**4/128 - 351*t**2/1024 - 27/64
ident == rhs: True
y^3 - p^2 = 27*(8*t**4 + 13*t**2 + 16)/1024
gcd(p', q') = 1
```

This is an identity in `QQ[t]`, not a floor and not a remainder-degree
substitute. The zero remainder is recorded as zero.

### 3.2 Resultant, bidegree, closed form

**Declared elimination.** In `QQ[coord_x, coord_y][param_t]`,

```text
F_raw = Res_t( p(t) - coord_x,  q(t) - coord_y ).
```

`sympy` returns `content(F_raw) = 1/2^{32}`, `deg_x=6`, `deg_y=9`,
`total_degree=9`, irreducible over `QQ`, 14 terms, `lc_y(F_raw)=-1`.
No vertical asymptotes: Sage `braid_monodromy` therefore projects over
the first variable with no linear change of coordinates (convention
B1, kept from 962).

The primitive integer polynomial (positive `x^6`, content 1 in `ZZ`)
is `F_prim = 2^{32} F_raw`:

```text
F_prim =
    4294967296 x^6
  - 12884901888 x^4 y^3 + 1585446912 x^4
  + 12884901888 x^2 y^6 - 3170893824 x^2 y^3
  - 167215104 x^2 y + 73156608 x^2
  - 4294967296 y^9 + 1585446912 y^6 + 167215104 y^4
  - 73156608 y^3 + 40310784 y^2 - 7164612 y
  + 964467.
```

`lc_y(F_prim) = -2^{32}`. Image check: `F_prim(p(t), q(t)) = 0`.

**Independent closed form, identity substitution.** Set `z=t^2` and
`w=y^3-x^2`. The identity says `1024 w = 27(8z^2+13z+16)`, and
`4y-3 = 4z^3+8z^2+10z`. Ring `QQ[x,y][z]`, resultant

```text
G = Res_z( 1024(y^3-x^2) - 27(8z^2+13z+16),
           4y-3 - (4z^3+8z^2+10z) ).
```

`G` has content 4, bidegree `(6,9)`, 14 terms, and
`primitive(G) = - primitive(F_raw) = -F_prim`. Equivalently
`G = -4 F_prim`. Matching names were not used: the two resultants
were expanded and compared as elements of `QQ[x,y]`.

Sage `build_F` computes `Res_t`, divides by content, and asserts
equality with the hardcoded `F_prim` (preferring the positive-`x^6`
sign). It then evaluates `F(p(t),q(t))` via the declared hom
`QQ[coord_x,coord_y] -> QQ[t]`, `(coord_x,coord_y) |-> (p,q)`.

### 3.3 Fibre at `x=0`, and the two new nodes on `F=0`

```text
F_prim(0,y) = -(4y-3) (32768 y^4 + 12288 y^3 + 6912 y^2 - 1728 y + 567)^2
```

The linear factor is the residual smooth point `t=0`, `y=3/4`,
`x'(0)=63/32 ≠ 0`. The squared quartic is the four banked nodes
(the review's `Res_z(q, p-w)`). The two new nodes
`y=21/512`, `x = -297 u/4096` with `u^2=-35/8` (so
`x^2 = 3087315/134217728`) reduce `F`, `F_x`, and `F_y` to 0 in
the quotient `QQ[u]/(u^2+35/8)`.

Jacobian Groebner basis of `(F, F_x, F_y)` in `QQ[x,y]`, grevlex
`(x,y)`:

```text
y^4 + (3/8) y^3 + (3801/5632) x^2 + (27/128) y^2 - (27/512) y + 567/32768,
x^3 + (3087315/134217728) x,
x y - (21/512) x.
```

Zero-dimensional. Leading monomials `y^4`, `x^3`, `xy`. Standard
monomials `{1,y,y^2,y^3,x,x^2}`, quotient length 6. The third
generator is `x(y-21/512)=0`; the second is `x(x^2+3087315/134217728)=0`.
Support: four points on `x=0` (the banked nodes) and two points with
`y=21/512` and `x^2 = x_new^2`. Scheme length 6 equals `Delta_aff`.
Sage precheck asserts `dimension=0` and `vector_space_dimension=6`.

---

## 4. Discriminant census (item (4), replayed)

Tangency resultant `R(c) = Res_t(p(t)-c, p'(t))` is the even octic

```text
R(c) = 19683 · Omega(c) / 2^{31},
```

with primitive

```text
Omega = 42268920643584 c^8 + 32085100199936 c^6 + 7694037614592 c^4
      + 614771555328 c^2 + 16209796869.
```

Degree 8, `gcd(Omega, Omega')=1`, `R(0)=319057431772527/2^{31} ≠ 0`,
`gcd(Omega, 134217728 c^2 + 3087315)=1`. Eight distinct simple
vertical tangencies, none at `x=0` and none at the new-node abscissae.
This is `REV:243-265`, recomputed.

Polar discriminant `Delta(X) = Res_Y(F, F_Y)` of the integer primitive,
factored over `QQ`:

```text
Delta(X) = (unit in QQ) · X^8 · (134217728 X^2 + 3087315)^2 · Omega(X).
```

`sqf_list` multiplicities `(Omega,1)`, `(134217728 X^2+3087315, 2)`,
`(X, 8)`. Degree `8+4+8=20`. Support degree 11. Ledger
`8 + 2(4+1+1) = 20 = 2 Delta_aff + deg_t x - 1 = 12+9-1`.

| factor | multiplicity | geometric type |
|---|---:|---|
| `X` | 8 | four-node fibre at `x=0` (`2·4=8`) |
| `134217728 X^2+3087315` | 2 | two one-node fibres, val 2 each |
| `Omega(X)` | 1 each | eight simple tangencies |

No other affine factor. `x=infinity` is not a root of the affine
polynomial (`lc_y(F)` is a nonzero constant). Footgun #10 is load-bearing
here: `squarefree_part` would report only `Omega`.

Sage precheck aborts (banner `CENSUS-DISAGREES-964-NODALITY-REVIEW`)
unless all of: `deg disc=20`, `radical`-support 11, `val_0=8`,
`val_Q=2`, remaining octic monic-equal to `Omega`, Jacobian length 6.

Monodromy census (when SIROCCO runs) classifies geometric-basis braids
as `tangency` (exponent 1, transposition), `four_node_fibre` (exponent
8, identity, four commuting squares), `one_node_fibre` (exponent 2,
identity, one square). Expected counts 8, 1, 2; ledger 20. CPF
unexpected or an `other` class is a loud abort, not a silent
reclassification. A sign error giving ledger `-20` is still a census
disagreement.

---

## 5. `box/bmfact_964.sage`

SHA-256
`1d0d150950c1c55e9017724dbcca913d15bd492430be987e34c20038568a8f3f`.
1019 lines. Clone of the hashed 962 script with the (9,6,4)
parametrization, the integer closed form of §3.2, Jacobian length 6,
the item-(4) discriminant assertions of §4, and the three-type
monodromy classifier.

Outputs, under `BRAID_JOB_OUT` (default `./bmfact-964-out`):
`precheck.json`; on monodromy, `bmfact_964.json` and `.jsonl` with
per-braid Tietze, exponent, permutation, Artin auto on `F_9`,
conjugate-positive form, product, and a `census.ok` record.

Unpack accepts the Sage 10.8 4-tuple and the develop 5-tuple. Missing
base point is flagged `OPEN[BMFACT-BASEPOINT]`; strand `y`-roots are
then not claimed. Affine-curve method is cross-checked against the
module function (same library twice: FLAG).

This lane did not run Sage: no `sage` binary on the host, and
monodromy is AWS-only. Precheck is exact commutative algebra and is
independently covered by the `sympy` curve-check.

Replay (coordinator):

```text
# footgun #11: preparse, then python; do not rely on `sage file.sage`
python3 box/bmfact964_enum.py --curve-check
# on Box03, after preparse:
python bmfact_964_pp.py precheck
BRAID_JOB_RUN_MONODROMY=1 BRAID_JOB_OUT=... python bmfact_964_pp.py monodromy
```

---

## 6. Class list as control only; `box/bmfact964_enum.py`

SHA-256
`e441ee8a41eb6ed15e6b8ff198b3b47a55ca230a3c78bc0bcbeca333376e2d22`.
1619 lines. Adapted from hashed `box/bmfact_enum.py`.

**Charged class list, `REP:501-504`, hostile-review confirmed exact
3/72, CONTROL ONLY, never a strand map for the decision:**

```text
Delta = (9,6,4), k_* = -8, 3 classes, 72 tuples
  noncst-T-a : X=(3 4) Y=(2 3) Pi=(2 4) T1=((1 3),(1 4),(1 3))
  noncst-T-b : X=(3 4) Y=(2 3) Pi=(2 4) T1=((1 4),(1 3),(1 4))
  const-4c   : X=Y=(1 2 3 4) Pi=(1 4 3 2) T1=((3 4),(1 4),(1 2))
```

Each a 24-element `S_4`-conjugacy orbit. `noncst-4c` is dead at
`k_* ≡ 0 (mod 4)`. `iota = (delta_3^{-8}, 1, 1)` reconstructs
`(T_2,T_3)` from `T_1` in the adjacent-block reading; that reading
is diagnostic and is labelled `diagnostic_BLOCK_not_decision`.

In-lane, at `k_*=-8`: GATE-3 holds on all three representatives
(`h = Y X^2 Y = e` on every live class here, because `X` is an
involution on `noncst-T` and `X^4=e` on `const-4c`); `prod(T_1)=X`;
expansion 72 with no collision; 48 tuples have `Pi` a transposition
and 24 have `Pi` a 4-cycle; never in `V_4`. The (9,6,2) Pi-tau pin
("two of six transpositions") is **not** applied to `const-4c` and
is not a filter.

**Positive control.** Drop every local ZvK relation except the
product. Generating count must equal 72. Reconstruction: 72 of 72
product-fixed and generating. Independent CABLE-3 scan of all
adjacent-block `6^9` (lookup tables, `216^3`): `n_product_fixed=174`,
`n_generating=72`. With Sage JSON, the *native* product-only count
in Sage strand order must be 72 in at least one orientation (the
count is conjugation-invariant; emptiness of the full-ZvK set is
too).

**Negative control.** Extra projective relation
`xi_1 ... xi_9 = 1`. Count 0, because every charged `Pi` is odd.
In-lane count 0. Native product-only additionally counts generating
tuples whose nine-fold product is the identity and requires 0.

**Decision path: native `6^9`, no strand map.** Transpositions are
integer-encoded `{0..5}`. Each Sage Tietze word is applied as left
Hurwitz (rightmost letter first). After each local relation the
universe is pruned to the current fixed set. A deterministic
subsample (`base-6` id `≡ 0 (mod 1021)`, 9871 tuples) is filtered
both by pruning and by the unpruned all-words check; disagreement
aborts. Both orientations. Synthetic selftest (`sigma_1` then
`sigma_3^2`): pruned 550 = unpruned 550.

Output tokens, never a row-level kill:

| token | meaning |
|---|---|
| `SURVIVOR` | at least one generating 9-tuple fixed by every local braid in some orientation; full meridian tuple verbatim |
| `NATIVE_ZERO_CURVE_ONLY` | native full-ZvK generating count 0 in both orientations, with product-only = 72 on at least one; **this curve only** |
| `OPEN(census mismatch)` | Sage census disagrees with 8+1+2, ledger 20 |
| `OPEN(API mismatch)` | missing braids / Tietze / `nstrands`, or product-only count equals 72 in neither orientation |

Adjacent-block intersection is printed as a diagnostic and must not
be read as a kill (that was the 962 trap: BLOCK-zero with native
still running).

---

## 7. Self-checks, in-lane, verbatim

Command: `python3 box/bmfact964_enum.py --selftest --curve-check`
(17s). Exit 0. `SELFTEST-OK`, `CURVE-CHECK-OK`.

```text
GATE-3 at k_*=-8: all three reps passed; prod(T1)=X on each
expanded conjugacy orbits: 72
Pi-type: n_transposition=48 n_fourcycle=24 passed=True
POSITIVE CONTROL generating=72 expected=72 passed=True
NEGATIVE CONTROL projective-product=1 count=0 expected=0 passed=True
BRUTE CABLE-3 6^9: n_product_fixed=174 n_generating=72 passed=True
SYNTHETIC_PRUNER: subsample_mod=1021 n_seen=9871
  prune word0 sigma_1:  9871 -> 1646
  prune word1 sigma_3^2: 1646 -> 550
  pruned=550 unpruned=550 symmetric_difference=0 passed=True
curve_check:
  identity_ok=True
  gcd(p',q')=1
  deg_x=6 deg_y=9 total_degree=9 irreducible=True
  closed_form_matches_resultant=True
  F_vanishes_on_parametrisation=True
  disc_degree=20
  sqf_list = (unit, [(Omega, 1), (134217728 x^2+3087315, 2), (x, 8)])
  tangency_degree=8 tangency_squarefree=True
  census_ok=True
  lc_y(F_prim)=-4294967296
```

Sage monodromy was not run (no `sage` binary; AWS gate). The native
decision token is therefore not produced. That is a missing SIROCCO
artefact, not a filled gap: the enumerator refuses to decide without
JSON, and this report does not invent `SURVIVOR` or
`NATIVE_ZERO_CURVE_ONLY` by analogy with the 962 BLOCK reading.

---

## 8. What this lane does not claim

- Not a braid factorisation. SIROCCO has not run on this `F`.
- Not existence or non-existence of `phi : pi_1(C^2-D) ->> S_4` on
  this curve, until the coordinator consumes `bmfact_964.json`.
- Not a Keller map, not `Y ~ C^2`, not a companion `D_2`.
- Not `FULL_ACTUAL_EXIT` of the AG-S row `(9,6,4)`. Other moduli are
  not claimed six-nodal and are not claimed to have the same local
  braids.
- Not a row-level kill under any token this pipeline can emit.
- GATE-3 survival (`REP:488`, review CONFIRMED) is a necessary
  condition on `rho_inf`-fixed tuples, already known; it is not the
  local-braid decision.

Successor: run `bmfact_964.sage` monodromy on Box03 (preparse +
python, `BRAID_JOB_RUN_MONODROMY=1`), then
`python3 box/bmfact964_enum.py path/to/bmfact_964.json`. Read
`decision` as one of the four tokens above.

---

## 9. FALLACY-v2

- Flag / place / series not identified: AG-S sequence `(9,6,4)`,
  affine nodes, and `K_infty = C_{(3,4)}(T(2,3))` remain distinct;
  infinity semigroup `⟨3,23⟩` is used only as the charged `delta_infty`
  input already consumed by the review. Discriminant roots (tangency
  flags in the `x`-plane), physical nodes, and the cover series of a
  hypothetical `phi` are not identified.
- Carrier: this curve is a `REPRESENTATIVE`, not `FULL_ACTUAL_EXIT`.
  Realization is a witness, not row-attainment. A native zero is
  `NATIVE_ZERO_CURVE_ONLY`.
- Floor / attainment: ledger 20 is the identity
  `2 Delta_aff + d - 1`, matched to the factored discriminant, not
  inferred from a lower bound. Quotient length 6 covers every affine
  node in the Jacobian scheme; equality is the Groebner leading-term
  count plus the six geometric points of the review, not a floor.
- `sat()` wrapping: not used. Jacobian ideal in `QQ[x,y]`, Groebner,
  length from leading monomials. Positive control: the six charged
  nodes lie on `V(F,F_x,F_y)`. Negative: the residual smooth point
  `(0,3/4)` has `x' ≠ 0` and is a simple zero of `F(0,y)`, not of
  the Jacobian.
- Raw remainder: leaders `u^2+35/8`, `z`-quadratic of the identity
  pair, and `X^8`, `Q(X)^2` in the discriminant; zero remainders
  recorded as zero; `quo_rem` exactness asserted.
- Variable / ring map: §0 and §3.2. Image checks
  `F(p(t),q(t))=0` and `primitive(Res_t)=±primitive(Res_z)`.
- Prime marks `p',q',F_x,F_y` are derivatives in the declared rings.
- No pole identity, no M-descent, no target/arrival index, no
  per-ray charge. No new exit-price assertion: no `charge_basis`
  line.

---

## 10. Deliverables and replay

| path | role |
|---|---|
| `box/bmfact_964.sage` | SIROCCO job: build `F`, precheck census, env-gated monodromy |
| `box/bmfact964_enum.py` | class-list controls, native 6^9 prune, decision tokens |
| this report | derivation, census, self-checks, decision rule |

```text
python3 box/bmfact964_enum.py --curve-check
python3 box/bmfact964_enum.py --selftest --curve-check
# after SIROCCO JSON exists:
python3 box/bmfact964_enum.py path/to/bmfact_964.json --out path/to/enum.json
```

Hashes of the two scripts as of this seal, computed on this host:

```text
1d0d150950c1c55e9017724dbcca913d15bd492430be987e34c20038568a8f3f  box/bmfact_964.sage
e441ee8a41eb6ed15e6b8ff198b3b47a55ca230a3c78bc0bcbeca333376e2d22  box/bmfact964_enum.py
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19667`.
- Body SHA-256:
  `48e8e7972cc0838075b44441542cd80466990f33ce253583526daf8666a3efad`.
- Frozen basis: `cbe4be8530aac3038ce8ce93be1b8262de128ddf`.
