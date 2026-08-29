# Hostile review — delayed affine-Faber `A`, `H=15,a=3` kernel fan

| Field | Value |
|---|---|
| Target | internal kernel-fan composition of the charged `a=3` predecessor note, the low-kernel lemma, V5 grade-42 graph predecessor, and graph-relative `q>6` support |
| Charged predecessor composition | `xmodel/max12-812-order2-affine-faber-a-a3-q6-graph-predecessor-composition-20260826.md` = `264033da9f60f7954a17d32f468e563838da310b7628ef21d06c1a0c6775c560` |
| Charged low-kernel lemma | `xmodel/max12-812-order2-affine-faber-a-low-kernel-center-independence-lemma-20260826.md` = `5e8e82b3a29f2bdbb1d0c90130bbc7496808582ac0bc7148924b23df1a59bf25` |
| Charged V5 `RESULT.md` | `a5a876aee85a2249a9932bcab76875d94e7f450ea3ecaf32b68d98b8e29493c1` |
| Charged V5 `EVIDENCE.sha256` | `16f2e56d6cac53cc20ca660a0c928f3d24e4cc1181fe6f40967909646a2a2bb9` |
| Charged V5 `FREEZE.sha256` | `0ca8d71a58caddcd48f3c72824049a600abd473cf8f016d02e71046d6c39b1e3` |
| Charged cone-V2 `RESULT.md` | `b0b25cf2134afc6e695b4a8a4b98ae49b6f0fd35b2bd57a760c049eb0a4e0bbc` |
| Charged cone-V2 `EVIDENCE.sha256` | `0cd8adeddd5b23dd628d1bface222a3c4c39a6b98e3652ceed99b37d66be79a3` |
| Charged cone-V2 `FREEZE.sha256` | `2942eb95dc6aff9f2b13b218fb416ba66ade8cb23ae28fc37d9eafc421f1233c` |
| Charged multisupport `RESULT.md` | `cb01e3c30042561558658557398d8390f895f4f15bc8e48c322d4e991c9d4581` |
| Charged multisupport `EVIDENCE.sha256` | `5d57f5f53b9d6b9baa270e0e07197667b6cf0056fde7e7c172022bbf1bad5ff5` |
| Charged multisupport `FREEZE.sha256` | `779f9a6af9eae993bf9f6744b01cb24174e41ebd38763e639616517dd7b0bdac` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered cell of the fan below; `q=0`, `K10=0`, `a<3`, another normal/load slope, and factor degeneracies are outside the stated neighbourhood, not holes inside it |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producers. No producer status line, no `PASS`/`CONFIRMED`/`ENDPOINT` token, no validator string, and no review prompt is evidence |
| Method | SHA-256 of every charged pin and of every freeze/evidence path before opening result prose; exact polynomial identities for the first polar block and the seven grade-42 rows; independent truncated substitution of the frozen ordinary-Faber tails at the first-face specialization `a=0`; complete 365-term Newton analysis of the frozen exact-`Q` graph-relative support with linear weights in `(v(a),q)`, not a sampled cone; chart emptiness by direct rewriting on `D(x)` and `D(y)`. Characteristic 65521 was opened only as a software control |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the eleven charged files match the
pins. Independently recomputed SHA-256 of every path named in the three
charged `EVIDENCE.sha256` and three charged `FREEZE.sha256` files match
those manifests (77/77). Producer verdict language, `A_A3Q6_*` and
`A_KGRAPH_*` endpoint strings, both validator `PASS_*` lines, and the
prompt were not used as characteristic-zero evidence. Exact `Q` is the
mathematical lane. V2/V3/V4 in the predecessor package are negative or
preformal custody only; only V5 is the controlling grade-42 replay. No
file other than this review was written. `jc2-lean` and shared ledgers
were not touched.

---

## Verdict

**CONFIRMED.**

On the delayed affine-Faber `A` chart with normal order 15, center order
3, and leading loads on the corrected affine graph, the first kernel face
is a finite fan in the rational order `q=min(v(U),v(V))>0`:

```text
(0,6) : center-independent quadratic two-chart block, empty on D(E*M);
{6}   : the same block after graph cancellation at grade 42, empty on
        both projective charts D(E*M*x) and D(E*M*y);
(6,∞] : graph-relative intrinsic cubic -E*λ^3*M^3/16, the unique least
        nondeviation term once d6,d2,dm have strictly positive excess
        above weight 42.
```

Positive center order does not enter the first quadratic polar face. The
two residue charts remain empty for every rational `0<q<6`, including
unequal orders after finite ramification. At `q=6` the seven exact
grade-42 rows are the displayed `G1,...,G7`; three of them are redundant
on `D(E)`, and replacing `G2` by `G6` uses `E` (called `p` in the source
replay) as a unit. The raw weight-45 tie at `(a,q)=(3,6)` is a valid
support sentinel and is unreachable because the full grade-42 row ideal
is already the unit ideal on both kernel charts. Center monotonicity of
the complete 365-term support, not a sampled cone, extends the `q>6`
cubic uniqueness to every `v(a)>3` and `q>=6`.

This is an internal normalized/coefficient-chart kernel-fan composition
on `D(E*M)` in the delayed chart. It is not a literal source-cover or
total-Rees theorem. `K10` is a unit coefficient of the delayed load
`k10=t^{42}K10` used to write the graph ratios; the grade-42 predecessor
does not invert it, and the identities hold without that inversion.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| predecessor composition | `264033da9f60f7954a17d32f468e563838da310b7628ef21d06c1a0c6775c560` | charged hand note (matches required pin) |
| low-kernel lemma | `5e8e82b3a29f2bdbb1d0c90130bbc7496808582ac0bc7148924b23df1a59bf25` | charged lemma (matches required pin) |
| V5 `RESULT.md` | `a5a876aee85a2249a9932bcab76875d94e7f450ea3ecaf32b68d98b8e29493c1` | charged; opened after hashing; `PASS` language is not evidence |
| V5 `EVIDENCE.sha256` | `16f2e56d6cac53cc20ca660a0c928f3d24e4cc1181fe6f40967909646a2a2bb9` | charged evidence list; every listed file rehashes |
| V5 `FREEZE.sha256` | `0ca8d71a58caddcd48f3c72824049a600abd473cf8f016d02e71046d6c39b1e3` | charged freeze list; every listed file rehashes |
| cone-V2 `RESULT.md` | `b0b25cf2134afc6e695b4a8a4b98ae49b6f0fd35b2bd57a760c049eb0a4e0bbc` | charged; support-split prose opened after hashing |
| cone-V2 `EVIDENCE.sha256` | `0cd8adeddd5b23dd628d1bface222a3c4c39a6b98e3652ceed99b37d66be79a3` | charged evidence list; every listed file rehashes |
| cone-V2 `FREEZE.sha256` | `2942eb95dc6aff9f2b13b218fb416ba66ade8cb23ae28fc37d9eafc421f1233c` | charged freeze list; every listed file rehashes |
| multisupport `RESULT.md` | `cb01e3c30042561558658557398d8390f895f4f15bc8e48c322d4e991c9d4581` | charged; inventory prose opened after hashing |
| multisupport `EVIDENCE.sha256` | `5d57f5f53b9d6b9baa270e0e07197667b6cf0056fde7e7c172022bbf1bad5ff5` | charged evidence list; every listed file rehashes |
| multisupport `FREEZE.sha256` | `779f9a6af9eae993bf9f6744b01cb24174e41ebd38763e639616517dd7b0bdac` | charged freeze list; every listed file rehashes |
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete ordinary-Faber tails used to rebuild `G1,...,G7` |
| load-graph cancellation note | `c467fc5454eda943721c60f599f9e005f158a2fa3f934b64c694df116b1d6bbd` | graph ratios and transverse coordinates; consumed by the composition |
| affine-`mu2` connection review | `4ddc0e4837e1581129fddad70fc7b5c029d642e644f4fd8ab478a4dec59bded3` | parent of the graph; not a kernel-fan theorem |
| exact-Q V5 stdout | `fe5df60b98c9b766ccc436e1f570d41dde4eb92435c23ca7d897e3272bbc184e` | printed `C1,...,C7` compared with reconstructed `G_i` |
| exact-Q graph-relative stdout | `40953daef89c5d57ecd14619e6ead4870f81f9c75c1b3e2c33ed029848716a30` | complete 365-term support parsed below |

Characteristic-65521 stdout hashes `2c424238536832186ded4db6ee0b69da07724a7a8c70afbfdab3d7aa287801fa`
and `37961e6a9b120c85d95fc6bc16912cff946050106529cffcb0ce3dacfebba6f5`
appear in the charged evidence lists. They were opened only to confirm
exponent-sequence agreement and coefficient reduction of the exact-`Q`
polynomials. They are not characteristic-zero evidence.

---

## 1. First quadratic polar block

In the moving repeated-`A` coordinates

```text
A=z-a,     D=A^2+4 a A+E,
Q=A^2 D+U A+R0,
N=λ (M A D+V A+M U/2+W0),
```

write `Qp=A^2 D`, `Np=M A D`, `dQ=U A+R0`, `dN=V A+M U/2+W0`. The linear
polar part of `N^2/Q` is the rational function
`2 Np dN/Qp-Np^2 dQ/Qp^2`. Clearing the denominator `A^2 Qp^2` yields the
polynomial identity

```text
2 A dN - M dQ
  = 2 A (V A + M U/2 + W0) - M (U A + R0)
  = 2 V A^2 + M U A + 2 W0 A - M U A - M R0
  = 2 V A^2 + 2 W0 A - M R0.
```

The two `M U A` terms cancel for every `a,E,M`. Restoring the denominator
gives lemma (2.2):

```text
2 M V + (2 M W0)/A - (M^2 R0)/A^2.
```

The only Laurent coefficients are those of `A^{-1}` and `A^{-2}`. The
regular term `2 M V` does not enter ordinary Faber tails. Either those
polar coefficients supply a unit pivot, or genuine complements satisfy
`v(R0),v(W0)>=2q`.

On the kernel `R0=W0=0` the quadratic polar is
`dN^2/Qp-2 Np dN dQ/Qp^2+Np^2 dQ^2/Qp^3`. Multiplying by `Qp^3` produces
the square `(dN Qp-Np dQ)^2`, and

```text
dN Qp - Np dQ
  = (V A + M U/2) A^2 D - (M A D)(U A)
  = A^2 D (V A - M U/2).
```

Hence the quadratic polar is exactly

```text
(V A - M U/2)^2 / (A^2 D).
```

The geometric expansion `1/D=1/E-(4 a/E^2) A+O(A^2)` holds because
`D=E(1+(4 a/E) A+A^2/E)`. Every center-dependent correction therefore
carries a positive factor of `a` and, equivalently, one extra power of
`A`. The leading `A^{-2}` coefficient of the first face is the `a=0`
residue `M^2 U^2/(4 E)` and does not involve `v(a)`. Tangent jets of
`E,M` likewise multiply already later grades. Positive center order does
not enter the first face.

Multiplication by the unit normal square and by `3/8`, after the linear
complement split, produces the ordinary rows of section 2. The
Laurent-to-ordinary connection is lower unitriangular, so at a complete
first face it cannot mix a later center correction into grade `30+2q`.

### Complete first face, and emptiness for `0<q<6`

On the delayed schedule (normal 15, loads/`mu2` 42, complements 12,
intrinsic cubic `3*15=45`) the quadratic kernel face has grade `30+2q`.
For every rational `0<q<6`:

- loads and `mu2` start at 42, strictly after `30+2q`;
- genuine complements of order 12 start at `30+12=42`, strictly after
  `30+2q` because `2q<12`;
- the intrinsic cubic is at 45, after both;
- center times kernel is at `v(a)+30+2q`, hence at least three grades
  after the first face;
- `mu4` is at 48;
- `mu6` and `J` are absent from the graph-relative functional `K`
  (section 3).

No load, target, cubic, or complement ties the first face. The lemma's
complete-first-face hypothesis is satisfied by this schedule, and is not
a hidden extra assumption inside `(0,6)`.

The two residue charts are the projective leading kernel `(x:y)=(U:V)`.
The combination

```text
G3 - (E/4) G1 = -(3/8) M x y
```

is an identity of the four first-face rows (verified coefficientwise in
section 2). On `D(M)` one has `x y=0`. Then `G6=(3 E^2/64)(y^2-M^2 r0)`.

- On `D(x)`: `y=0`, so `G6=0` forces `r0=0` on `D(E M)`, and
  `G4=3 M^2 x^2/32`, a unit on `D(M x)`.
- On `D(y)`: `x=0`, so `G6=0` forces `r0=y^2/M^2` on `D(M)`, and
  `G4=-3 E y^2/8`, a unit on `D(E y)`.

If complements of order 12 are strictly later than `2q`, the `r0` terms
drop out of the first face and `G6=3 E^2 y^2/64` already kills `D(y)` on
`D(E)`. Unequal orders specialize to one axis: `v(U)<v(V)` is `D(x)`,
`v(V)<v(U)` is `D(y)`. After a ramification `σ=τ^e` that makes `q`
integral, the face is homogeneous of `τ`-degree `e(30+2q)` while loads
start at `42 e`; the inequality `30+2q<42` is preserved. Both charts are
empty for every rational `0<q<6` on `D(E*M)`.

At `q=6` the loads and the order-12 complements tie grade 42, so the
lemma stops and the V5 predecessor must retain them. That is the content
of section 2, not a hole in `(0,6)`.

---

## 2. Seven V5 grade-42 rows

The delayed source map at `q=6` is

```text
a = s^3 (a3 + s a4 + s^2 a5 + s^3 a6),
E = p + s e1 + s^2 e2,     M = m + s m1 + s^2 m2,
U = s^6 (x6 + s x7) + s^{12} (r112 + ...),
V = s^6 (y6 + s y7) + ...,
R0 = s^{12} (r012 + ...),   S0 = s^{12} (s012 + ...),
N = s^{15} M_shape,
k10 = s^{42} (kk + s k101),
k6  = s^{42} ((15/32) kk p^2 + s d61),
k2  = s^{42} ((15/256) kk p^4 + s d21),
mu2 = s^{42} (-(5/4096) kk p^6 + s dm1).
```

The leading graph is the `p`-specialization of composition (1.2). Higher
`E`-jets are absorbed into the registered deviation successors.

Independent truncated substitution of the seven frozen ordinary-Faber
tails into this map, at the first-face specialization `a=0` (center off
the face, as licensed by section 1) and truncated at `s^{42}`, produces
coefficientwise

```text
G1 = -3 r112 m^2/8 + 3 s012 m/4,
G2 = -3 r012 m^2/8 + 3 y6^2/8,
G3 = -3 p r112 m^2/32 - 3 m x6 y6/8 + 3 p s012 m/16,
G4 =  3 m^2 x6^2/32 - 3 p m^2 r012/16 - 3 p y6^2/16,
G5 = -3 p^2 r112 m^2/256 + 3 p m x6 y6/32 + 3 p^2 s012 m/128,
G6 = -3 p^2 m^2 r012/64 + 3 p^2 y6^2/64,
G7 =  3 p^3 r112 m^2/1024 - 3 p^2 m x6 y6/256 - 3 p^3 s012 m/512.
```

Each row is supported only in degree `s^{42}`: every coefficient of
`s^0,...,s^{41}` vanishes. No `kk` monomial occurs. These are exactly
composition (2.2) with `E` renamed `p` and with the unit normal square
absorbed into the scale `s^{15}`. The hash-pinned exact-`Q` stdout
polynomials `C1,...,C7` are the same seven polynomials (monomial order
aside). Characteristic 65521 reduces each displayed rational coefficient
to the printed prime-lane polynomial; that is a software control, not a
proof.

The polar calculation of section 1 identifies the same monomials: `G1`
is `(3/8)` times the `A^{-1}` complement polar `2 M S0-M^2 R1`; `G2`
carries the `A^{-2}` complement `-3 M^2 R0/8` together with the ordinary
image of the quadratic `V^2` term; `G4` and `G6` carry the remaining
quadratic `(U,V,R0)` face. Center corrections miss grade 42 because they
are at least `v(a)=3` later, i.e. grade 45.

### Three redundancies, charts, localizations, controls

The identities

```text
G6 - (E^2/8) G2 = 0,
G5 - (3 E^2/32) G1 + (E/4) G3 = 0,
G7 - (E^2/32) G3 + (E^3/64) G1 = 0,
G3 - (E/4) G1 + (3/8) M x y = 0
```

hold by comparing coefficients of `E^k r1 M^2`, `E^k s0 M`, `E^k M x y`,
`E^k r0 M^2`, and `E^k y^2`. In particular `G6=(E^2/8) G2`, so replacing
`G2` by `G6` uses `E` as a unit: on `D(E)` one has `G6=0` if and only if
`G2=0`. On `V(E)`, `G6` vanishes identically while `G2=-3 r0 M^2/8+3 y^2/8`
need not. The charged charts invert `p`, so they work on `D(E)`. The four
rows `G1,G3,G4,G6` therefore generate the same ideal as all seven on
`D(E)`.

Chart emptiness does not use a Gröbner basis. On
`D(x)={y=0}` with `p m x` inverted, `G6=0` forces `r0=0` and
`G4=3 m^2 x^2/32` is a unit. On `D(y)={x=0}` with `p m y` inverted,
`G6=0` forces `r0=y^2/m^2` and `G4=-3 p y^2/8` is a unit. The origin
`x=y=0` of this `P^1` is the higher-order kernel, i.e. the cell `q>6`,
not a residue of the `q=6` face. Localizations by `p,m` are exactly these
two charts. Neither chart inverts `kk`.

Successor, center, load, and `K10` intrusion at grade 42 are absent from
the reconstructed `G_i`: those polynomials involve only
`r112,r012,s012,x6,y6,m,p`. A mutation of the leading `mu2` graph
coefficient changes `G2` by a nonzero multiple of `kk`, so it is
detected. V5 retains the jets `a3..a6`, `e1,e2`, `m1,m2`, `x7,y7`,
complement order 13, `k101`, `d61,d21,dm1` far enough to meet grade 42;
none of them appears in `G_i`.

V2 of the predecessor package is a Singular coefficient-syntax failure
(`m^2/8` parsed as a nonintegral exponent). V3 found the three extra
nonzero rows `G2,G5,G7` and failed a four-row control while both chart
bases were already units. V4 verified the seven-row block and the three
dependencies but omitted the dependency marker from its validator. None
of those clients is the controlling result. Only V5 is.

---

## 3. Graph-relative support for `q>6`

The frozen exact-`Q` support of `K=E H3+H5` in the two-sided graph
coordinates

```text
d6 = K6 - (15 E^2/32) K10,
d2 = K2 - (15 E^4/256) K10,
dm = mu2 + (5 E^6/4096) K10,
d4 = mu4
```

has 365 terms. The characteristic-65521 lane has the identical exponent
sequence. Raw `(q,n,k)` coordinates, `mu6`, and `J` are absent from every
exponent vector. The delayed Newton weight of a monomial is the linear
form

```text
W = 48 v(d4) + 42 (v(dm)+v(d2)+v(d6)+v(K10))
    + v(a)·(a-power) + 15 (λ-power)
    + q (2(S0+S1+R0+R1) + Y + X),
```

with the delayed identifications `v(a)=3` on the charged ray and
`v(k10)=42` for a unit coefficient of `k10=t^{42} K10`. Strict
transverse deviation means a positive exponent of `d6`, `d2`, or `dm`,
not of `d4` or `K10`. This is a convention of the cone, not a sampling
choice: those three coordinates are the graph-transverse loads of the
cancellation note, and they are hypothesized to have strictly positive
excess above weight 42.

The unique slope-zero, nondeviation monomial of weight 45 is

```text
-E λ^3 M^3 / 16
```

with exponent vector `λ^3 M^3 E` and coefficient `-1/16`. At
`(v(a),q)=(3,6)` the global minimum of `W` on the 365-term support is 45,
attained at exactly six monomials:

```text
-E λ^3 M^3 / 16,                          (intrinsic; no a; slope 0)
-(3/8) X^2 a λ^2 M^2,                     (nonstrict; a-power 1; slope 2)
 (3/2) Y^2 a λ^2 E,                       (nonstrict; a-power 1; slope 2)
-(9/128) d6 a E^5,                         (strict; a-power 1; slope 0)
 (1/8) d2 a E^3,                           (strict; a-power 1; slope 0)
-dm a E.                                   (strict; a-power 1; slope 0)
```

No term has `W<45`. No nondeviation `K10` term has `W<=45`. The next
nonstrict weights are 48. The largest `q` at which a non-intrinsic
nonstrict competitor still has `W<=45` is `q=6`, realized only by the
two displayed kernel monomials (intercept 33, slope 2).

For `a=3` and `q>6` those two nonstrict competitors have
`W=33+2q>45`. The three strict terms remain at 45 for every `q` if
`v(d*)=42` exactly, because they have slope 0. The unique-least claim
for `a=3,q>6` therefore requires the stated strict excess of `d6,d2,dm`,
after which those three have weight `>45` and the intrinsic cubic is the
unique least nondeviation term. It is a unit on `D(E*M)` (and of the
unit leading coefficient of the normal scale).

### Center monotonicity for `a>3`, `q>=6`

This is read from the complete support and the linear form `W`, not from
a sampled list of cones. Every nonstrict competitor at `(3,6)` other
than the intrinsic has `a`-power at least 1, so raising `v(a)` strictly
increases its weight. The only `a`-free nonstrict monomial with
`W(v(a)=3,q=6)<=45` is the intrinsic cubic itself. Consequently, for
every `v(a)>3` and every `q>=6` — including non-integral `q` and
arbitrarily large `q` — the unique nonstrict minimum remains
`-E λ^3 M^3/16` at weight 45. The three strict slope-zero ties all
contain `a`, so they also rise when `v(a)>3` even at exact
`v(d*)=42`. No `a`-free strict-deviation monomial has `W<=45` at
`q>=6`.

The composition's sentence that monotonicity "must be charged in the
graph-relative review rather than assumed" is discharged by this
complete-support identity, not by the cone analyzer's status string.

---

## 4. Rational partition, `q=0`, `q=∞`, predecessor order

The cells

```text
(0,6) ∪ {6} ∪ (6, ∞]
```

exhaust every positive rational `q` and the identically vanishing
kernel. They match the delayed schedule as follows.

- `(0,6)` is the complete first quadratic face of section 1.
- `{6}` is the V5 graph predecessor of section 2. Loads and order-12
  complements tie grade 42 and are retained; the projective kernel face
  is still empty.
- `(6,∞)` is the graph-relative cubic of section 3, after strict
  deviation excess.
- `q=∞` is the slope-zero slice of the same support: the only
  nondeviation monomial of weight 45 is again the intrinsic cubic. The
  complementary-pivot dichotomy forces `v(R0),v(W0)>=2q=∞` as well, so
  no finite-order complement remains. The hand note writes `q>6`; the
  slope-zero analysis is the actual infinity argument and covers
  `(6,∞]`.

`q=0` is not in the fan. It is the complementary first-normal open of
the repeated-`A` closed point (a unit leading `U`, equivalently a unit
`qc` after `a=0`), received by the squarefree/generic affine-Faber
stratum or by the square family. It is an earlier face, not a missing
cell of this neighbourhood.

Predecessor order at `(a,q)=(3,6)`. The graph-relative support emits the
three-term nondeviation weight-45 polynomial

```text
λ^2 (-E λ M^3/16 - 3 a M^2 X^2/8 + 3 a E Y^2/2).
```

That is composition (3.1), a valid raw-support sentinel. It is not a
survivor equation. The seven-row ideal at grade 42 is already the unit
ideal on both projective kernel charts, by section 2, so no arc of
leading order `q=6` reaches grade 45. The cubic in `K=E H3+H5` is in any
case later than those rows: the quadratic `X Y` terms cancel between
`H3` and `H5`, which is why `K` itself first sees the cubic. Emptiness
of the rows is the reason the tie is unreachable, not uniqueness of the
raw cubic.

---

## 5. Strongest theorem, `K10` audit, coverage distinction

Work over a field of characteristic zero, in the repeated-`A` affine
coefficient chart on `D(E*M)`, with the delayed weights

```text
v(normal)=15,   v(a)=3,   q=min(v(U),v(V))>0,
v(complements)>=2q,   v(k10)=v(k6)=v(k2)=v(mu2)=42,
```

after a finite ramification that makes `q` integral if needed, and impose
the corrected affine graph

```text
K6/K10 = 15 E^2/32,   K2/K10 = 15 E^4/256,
mu2/K10 = -5 E^6/4096
```

with graph deviations `d6,d2,dm` of strictly positive excess above
weight 42. Then there is no formal or Puiseux solution in this weighted
neighbourhood: the first kernel face is empty on every cell of
`(0,6)∪{6}∪(6,∞]`, by the identities of sections 1--4. The same cubic
uniqueness holds for every `v(a)>3` and `q>=6`, by the linear weight on
the complete graph-relative support. The only point at which a raw
grade-45 nondeviation tie occurs is `(v(a),q)=(3,6)`, and it is killed
at grade 42 rather than at grade 45.

This is an internal normalized/coefficient-chart theorem. The V5 replay
substitutes the graph into ordinary-Faber tails in coefficient space; it
does not prove that a literal raw source arc reaches the graph, and it
does not produce a two-sided total-Rees atlas. The load-graph
cancellation identities

```text
15/1024 - 45/2048 + 15/2048 = 0,
100/4096 - 135/4096 + 30/4096 + 5/4096 = 0
```

are the local algebraic reason a raw load wall at weight 45 disappears
after graph reduction. They are coefficient identities on `[λ]K` and
`[a]K`, not a source-accessibility lemma.

### `K10`

The hand composition names `K10,E,M` as units. The actual algebra is
stricter in one place and weaker in another.

- Grade-42 predecessor: the reconstructed `G_i` contain no `K10`. The
  charged V5 charts invert `p m x6` or `p m y6`, not `kk`. Independence
  of `K10` is the theorem; inversion of `K10` is not used and is not
  needed.
- Graph ratios: writing `K6/K10` requires `D(K10)` in the ratio chart.
  Equivalently one works in the polynomial deviation coordinates
  `(d6,d2,dm,K10)` with delayed source scale `v(k10)=42`. That scale is
  essential. If `K10` is given Newton weight 0, one hundred eighty
  nonstrict monomials drop to weight `<=45` at `(3,6)`, including
  `K10 a^{15}` at weight 45, and uniqueness of the cubic is false. The
  charged cone weights `K10` at 42, i.e. as the leading coefficient of
  `k10=t^{42} K10`, which is the delayed ray actually used.
- `q>6` cubic: the monomial `-E λ^3 M^3/16` does not involve `K10`. It
  is a unit on `D(E*M)`, not on `D(K10)`. Absence of a central `K10`
  competitor is the statement that no nondeviation `K10` monomial has
  delayed weight `<=45`.

Do not pass to `K10=0`. That is a factor degeneracy of the graph, outside
the charged neighbourhood.

### Firewall

The theorem does not cover `q=0`, `v(a)<3`, `v(a)=0`, another
normal/load slope, `K10=0`, `E=0` or `M=0`, an earlier complement, a
literal source arc, total-Rees/saturation, terminal/Taylor closure,
order two, maximum twelve, or JC2. No such broadening is licensed by
the identities above.

---

## Negative custody

V2/V3/V4 of
`cases/max12_812_order2_affine_faber_a_a3_q6_graph_predecessor_20260826/`
are not controlling. V2 is a parser-negative. V3 is the
specification-negative that first printed the extra rows `G2,G5,G7`. V4
is preformal positive evidence whose validator did not yet mandate the
dependency marker. The V1 cone expectation of a direct unit at
`(a,q)=(3,6)` is likewise negative: that face is the three-term
nondeviation equality recorded in section 3, not a unit.

---

CONFIRMED
