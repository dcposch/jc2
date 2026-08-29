# Hostile review — generic-square correction-aware half-weight normalized ray

| Field | Value |
|---|---|
| Targets | `xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md`; `cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews and producer status lines are not evidence |
| Method | source reading, SHA-256 of every named pin and evidence file, and hand identities only; no Singular, Sage, msolve, Lean, package compiler, CAS, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the design is
`37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd`,
matching the required pin. Independently recomputed SHA-256 of
`FREEZE.sha256` and `RESULTS.sha256` match their required pins. Independently
recomputed SHA-256 of `RESULTS.md` is
`eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af`.
The review prompt required
`eb2cd8036a0fbf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af`
(one hex nibble: `0a` versus `0f`). That is a prompt-pin transcription error,
not an evidence mutation: every file named in both manifests verifies, the
printed exact-Q rows reproduce the frozen Q stdout, and the three other
primary pins match. Producer verdict language, the two status lines, and the
good-prime lane were not used as characteristic-zero algebra. No file other
than this review was written.

---

## Verdict

**CONFIRMED.**

On the generic square open, the substitutions `Lambda=sigma^2`,
`M=sigma^3 A`, `S=sigma C` give the exact identity
`f=(L^2+sigma^2 R)^2+sigma^5(LA+C)`. Expanding `f^{3/2}` and the charged
load `sigma^4 k10 f^{5/4}` through total sigma grade ten, every contribution
below grade ten is polynomial in `z`, the grade-nine `D K^{1/2}` cross term
is polynomial, and the complete grade-ten negative receiver is exactly

```text
[(3/8) D^2/L^2 + (5/16) k10 R^3/L]_- ,     D=LA+C.
```

Polynomiality is `L^2 | 6 D^2 + 5 k10 R^3 L`. On `D(p*k10)`, squarefreeness
of `L` and `deg C, deg R < deg L` force `C=0` then `R=0`, with `A` free.
The seven frozen complete-source rows are divisible by `sigma^{10}`,
independent of `k6,k2,mu2,mu4,mu6,J`, and realize that receiver before
specialization: the first ordinary coordinate equals the coefficient of
`z^{-1}` (hence of `w^{-1}`) by unitriangularity, and matches the hand
Laurent coefficient exactly, including the mixed `A C` terms omitted by
the earlier zero-higher-correction slice. The raw nonreduced ideal retains
quadratic `C`, mixed `A C`, and cubic `k10 R` thickness; its localized
radical is `(c0,c1,cs,rs)`. This is one normalized ray
`wt(Lambda,M,S,R)=(2,3,1,0)` with its coordinate faces, not a Newton-fan
exhaustion, not a square-branch exclusion, and not an order-two,
`(8,12)`, maximum-twelve, or JC2 theorem.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Custody of four primary pins | hashes | design, `FREEZE.sha256`, `RESULTS.sha256` match; `RESULTS.md` mismatches the prompt pin by one nibble (`0a`/`0f`); disk file is internally consistent |
| 1. Both manifests | every named file | all eleven `FREEZE` rows and all twelve `RESULTS` rows rehash to the printed digest |
| 1. Exact-Q versus `F_65521` | separate frozen runs | distinct hosts, tags, characteristics, compiled-script hashes, stdout hashes, stderr hashes, and meta; identical validation bytes are the same two-line validator payload, not a cloned run |
| 2. Scaling identity `(1.2)` | hand substitution | exact, including every compiler coefficient `c,r,n3,n2,n1,n0` |
| 3. Grade-ten receiver `(2.1)` | independent expansion | complete; lower grades polynomial in `z`; later loads dropped by explicit valuation, then rechecked as forbidden variables |
| 4. Frozen-source bridge | seven emitted rows | `sigma^{10}`-divisible; row 1 equals `[z^{-1}]` of `(2.1)`; `C^2` and `k10 R^3` blocks reproduce the load-ladder faces; no inhomogeneous unitriangular mixing |
| 4. Seven rows suffice | degree, not slogan | after clearing `L^2` and deleting the polynomial `A^2`, the remainder has denominator degree four, so four negative Laurent coefficients already imply `(2.2)` |
| 5. UFD support `(2.3)` | `L^2 \| 6D^2+5k10 R^3 L` | squarefreeness of `L` on `D(p)` plus `deg C, deg R < deg L` in characteristic zero force `C=0` then `R=0`; `A` free |
| 5. Coefficient conventions | `R=cs z+rs/4`, `C=(c1 z+c0)/2` | match the compiler and the load-ladder chart |
| 5. Raw versus radical | stdout | nonreduced basis retained; localized radical `(c1,c0,rs,cs)`; nilpotents involving `A` when `C\neq 0` are scheme thickness, not an extra reduced component |
| 6. Good prime `65521` | control lane only | no binomial denominator or localization factor `2,3,5,p,k10` vanishes in `F_65521`; not a characteristic-zero proof |
| 7. Correction awareness | `A C/L` | repaired on this ray; present in the analytic receiver and in five of the seven ordinary coordinates |
| 7. Stronger inferences | fan, `p=0`, terminal, Taylor, order two | all open, and so stated |

---

## 1. Custody

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md` | `37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd` | design (matches required pin) |
| `cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md` | `eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af` | producer endpoint; prompt pin differs by one nibble |
| `cases/.../FREEZE.sha256` | `ee4718fc24ae451f8f86c05e9c4eeae83215835e7cff5fdc8eccc54b9f881677` | source freeze (matches required pin) |
| `cases/.../RESULTS.sha256` | `a41a704b44cd4a3e456edd1e214d4d872f9d151bb43336f46a22a19b1a8c7d37` | evidence freeze (matches required pin) |

Every path named in `FREEZE.sha256` rehashes to the printed digest, including
`tails.json`, the load-ladder compiler, the third-tail theorem, the
one-parameter reduction, both first-normal theorems, the named Padé review,
and the half-weight compiler, `run_aws.sh`, and `launch_host.sh`. Every path
named in `RESULTS.sha256` rehashes to the printed digest.

Exact-Q and `F_65521` are genuinely separate frozen runs.

| Charge | Exact `Q` (Box03) | `F_65521` (r6d) |
|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-45` |
| Tag | `max12_812_order2_square_halfweight_q_20260826T071955Z_box03` | `max12_812_order2_square_halfweight_p65521_20260826T071955Z_r6d` |
| Characteristic | `0` in both rings | `65521` in both rings |
| Compiled script SHA | `43e3dadbef58060ea3390bf98ec7a90310dcb5845016b6a7269ec185e4fe2a93` | `60e88ec7a73e01fac249e231b46b4a38574c3de0a1861cba8f914b0ee52b343b` |
| `result.json` SHA | `50f5a4239089e211f870fe05988a0162ea7497fe84e24caa9ecf4913e39bd2f7` | `573eec72bce6483ee0e699a532622b6b148b22deaa3d6c1b9ea2171a163e30e7` |
| Compiler SHA (Python) | `0852b9460f862bd686f3e277b27a959a8c4b0b85c83c90645ba5c44fe2579858` | same source, independently invoked |
| Source / tails / design pins in `result.json` | match `FREEZE` | match `FREEZE` |
| Engine `rc` | `0` | `0` |
| Validator | `PASS_SQUARE_HALFWEIGHT` | `PASS_SQUARE_HALFWEIGHT` |
| Stdout SHA | `54bf5d295b4533298708963465ada6def98b4277b308f5ef22e3ce07c47ec5e2` | `53517a5900e702e63682bd1409d0dd80f39cc40d7cef761d55fdf2136077b981` |
| Stderr SHA | `2c88b1180181d3b1a644f8919064ff938b07fc66207750acaf63a2a858a05233` | `6c281f312434b9a15eaf51d1daae51ad166afb55738d07b1c07478d3ce3db9c6` |
| Peak RSS / swap | 14,636 KiB / 0 | 14,992 KiB / 0 |

The two compiled scripts differ by exactly the two ring-characteristic
tokens (`Rfull` and `Rsmall`). Substitutions, target exponents
`sigma^{2(12+ell)}`, and sentinels are otherwise identical. The two
validation files are byte-identical (`engine_rc=0` plus the same validator
line), which is why they share the hash
`5f8b55632ef0e7c6ddffe593c5df98b934052c85ed2b5a02e68905ba7b7155fa`;
that common payload is not evidence that the runs were copied. Both
`freeze_check.stdout` records report every `FREEZE` row OK. Both metas
record `argv` as `Singular -q` on the lane-local compiled script, return
code 0, and stdout hashes matching `RESULTS.md` and `RESULTS.sha256`.

A passing manifest is not a mathematical verdict. The algebra below is
independent of those sentinels.

---

## 2. Scaling identity

Start only from

```text
L = z^2 + p/2,
K = L^2 + Lambda R,
N = L M + Lambda S,
f = K^2 + Lambda N,
```

and substitute `Lambda=sigma^2`, `M=sigma^3 A`, `S=sigma C`. Then

```text
N = L sigma^3 A + sigma^2 * sigma C = sigma^3 (L A + C),
Lambda N = sigma^5 (L A + C),
```

so

```text
f = (L^2 + sigma^2 R)^2 + sigma^5 (L A + C).
```

This is exactly design `(1.2)`, and it is the primitive correction tie:
the load-ladder slice had already set the reduced `M` to zero and then
frozen `S` to zero, so it never formed the product `A C`. Here `D=LA+C`
retains both first permitted corrections.

Coefficient conventions `A=a1 z+a0`, `C=(c1 z+c0)/2`, `R=cs z+rs/4` give

```text
N = sigma^3 [
      a1 z^3
    + a0 z^2
    + (p a1 + c1)/2  z
    + (p a0 + c0)/2
    ],
```

hence

```text
n3 = sigma^3 a1,
n2 = sigma^3 a0,
n1 = sigma^3 (p a1 + c1)/2,
n0 = sigma^3 (p a0 + c0)/2.
```

The compiler writes precisely those four strings. It also writes
`c = sigma^2 cs` and `r = (p^2 + sigma^2 rs)/4`, which is
`K = L^2 + sigma^2 R` in the ordinary monic-quartic chart. The degree-eight
coefficients of `f=K^2+Lambda N` are the same seven polynomials as in the
load-ladder compiler, with `Lambda` replaced by `sigma^2` on the `K^2` side
and with `sigma^2 n_i` on the `N` side. Every listed substitution in design
§3, including

```text
k10 -> sigma^4 k10,     k6 -> sigma^{12} k6,     k2 -> sigma^{20} k2,
target row ell -> sigma^{2(12+ell)} delta_ell,
```

is realized: load weights `[2,6,10]` in the frozen tails become
`(sigma^2)^{2,6,10}` after the `Lambda` replacement, and the compiled
targets are `-sigma^{28} mu2`, `-sigma^{32} mu4`, `-sigma^{36} mu6`,
`-sigma^{38}(J/4)`.

---

## 3. Independent derivation of the grade-ten receiver

Write `K=L^2+sigma^2 R` and `D=LA+C`, so `f=K^2+sigma^5 D`. The complete
source combination at this valuation is `f^{3/2}+k10 f^{5/4}` plus later
loads (equivalently `H(w)=w^{12}+k10 w^{10}+\cdots` pulled back along
`w=f^{1/8}`). Charge `k10` by `sigma^4` as in the frozen tails.

### 3.1 Unloaded term

```text
f^{3/2}
  = K^3 (1 + sigma^5 D/K^2)^{3/2}
  = K^3 + (3/2) sigma^5 K D + (3/8) sigma^{10} D^2/K + O(sigma^{15}).
```

`K` is polynomial in `z`, so `K^3` is polynomial at every displayed grade
`0,2,4,6`. The product `K D` is polynomial, so both the grade-five term
`(3/2) L^2 D` and the grade-seven term `(3/2) R D` are polynomial in `z`.
The first nonpolynomial unloaded contribution is therefore the grade-ten
summand `(3/8) D^2/K`. Expanding `1/K=1/L^2+O(sigma^2)` pushes the
correction to grade twelve, so at total grade ten

```text
[(3/8) D^2/K]_- = [(3/8) D^2/L^2]_- .
```

Moreover `D^2/L^2=A^2+2AC/L+C^2/L^2`, and `A^2` is polynomial, so the
negative part is exactly that of `(3/4)AC/L+(3/8)C^2/L^2`.

### 3.2 Charged `k10` term

```text
f^{5/4}
  = K^{5/2} (1 + sigma^5 D/K^2)^{5/4}
  = K^{5/2} + (5/4) sigma^5 D K^{1/2} + (5/32) sigma^{10} D^2 K^{-3/2} + O(sigma^{15}).
```

The last displayed summand, after the charge `sigma^4 k10`, sits at grade
fourteen and is omitted by valuation, not by an unproved weight slogan.

The cross term at grade nine is `(5/4) sigma^9 k10 D K^{1/2}`. Here
`K^{1/2}=L+O(sigma^2)`, so `D K^{1/2}=D L+O(sigma^2)=A L^2+C L+O(sigma^2)`,
which is polynomial in `z`. (The opposite power `D/K^{1/2}` would not be
polynomial; that is not the binomial that appears.) Design's sentence
that the `D K^{1/2}` cross term at grade nine is polynomial is therefore
correct, and it is proved by expanding the binomial, not by dropping the
term.

The remaining piece is `sigma^4 k10 K^{5/2}`. With
`Y=sigma^2 R/L^2`,

```text
K^{5/2}
  = L^5 (1+Y)^{5/2}
  = L^5 + (5/2) sigma^2 L^3 R + (15/8) sigma^4 L R^2
    + (5/16) sigma^6 R^3/L + O(sigma^8).
```

The first three summands are polynomial in `z`. The first nonpolynomial
term of `K^{5/2}` is `(5/16) sigma^6 R^3/L`. Multiplying by `sigma^4 k10`
places it at grade ten, with next term `O(sigma^{12})`. Thus

```text
sigma^4 k10 K^{5/2}
  = polynomial + (5/16) sigma^{10} k10 R^3/L + O(sigma^{12}).
```

### 3.3 Completeness

`k6` enters the frozen tails with `Lambda^6=sigma^{12}`; `k2` with
`Lambda^{10}=sigma^{20}`; target row `ell` with `sigma^{2(12+ell)}` in
`{28,32,36,38}`. Those valuations are strictly larger than ten, so they
cannot contribute to the grade-ten negative part. The compiler
additionally checks that the coefficient of `sigma^{10}` is independent
of `k6,k2,mu2,mu4,mu6,J`; the emitted rows contain none of those
variables. Distinguish:

- *Proved polynomial in `z`:* `K^3`; `(3/2)KD`; `sigma^4 k10` times
  `L^5`, `L^3 R`, and `L R^2`; the grade-nine `D K^{1/2}` term.
- *Dropped by an explicit larger valuation:* `k6`, `k2`, both Taylor
  families and the terminal row, the `X^3` term of `f^{3/2}`, the `X^2`
  term of `k10 f^{5/4}`, and the `Y^4` correction to `K^{5/2}`.

No residual cross term from lower grades, from `K`'s `sigma^2` correction
inside `D^2/K`, or from targets survives at grade ten. The complete
grade-ten negative receiver is exactly design `(2.1)`.

---

## 4. Frozen-source bridge and sufficiency of seven rows

The compiler reconstructs all seven frozen loaded rows from `tails.json`
and the charged substitutions; it does not insert `(2.1)` in place of the
source. Both lanes report `SIGMA10_DIVISIBLE=1` and
`DIVISION_IDENTITY=1`, so each `Phi_ell` is exactly `sigma^{10} Xi_ell`.
The seven exact-Q divided rows printed in `RESULTS.md` §2 coincide with
the frozen Q stdout.

Independently, the coefficient of `z^{-1}` in `(2.1)` is computed as
follows. The substitution `z=w+O(w^{-1})` is unitriangular on the first
seven negative coefficients and is the identity on the first coefficient,
so ordinary row 1 equals `[z^{-1}]`.

For the `R^3/L` summand,

```text
R^3/L = (polynomial of degree 1)
      + [ (-p/2 cs^3 + 3/16 cs rs^2) z + (-3p/8 cs^2 rs + rs^3/64) ] / L,
```

and `z/L=z^{-1}+O(z^{-3})`, so

```text
[z^{-1}]((5/16) k10 R^3/L)
  = (5/16) k10 (-p/2 cs^3 + 3/16 cs rs^2)
  = -(5/32) p cs^3 k10 + (15/256) cs rs^2 k10.
```

For the mixed term, `AC/L` has remainder
`(a1 c0+a0 c1)z+(a0 c0-(p/2)a1 c1)` over `2L`, and

```text
[z^{-1}]((3/8)·2 AC/L) = (3/8)(a1 c0 + a0 c1).
```

The `C^2/L^2` contribution is `O(z^{-2})` and does not affect row 1.
Adding these pieces recovers exact-Q row 1, including the `A C` monomials
absent from both load-ladder grades. The `C^2` block of rows 2--7
reproduces the load-ladder grade-four rows under `v_i \leftrightarrow c_i`.
The `k10 R^3` block reproduces the load-ladder grade-five rows identically.
The `A^2` summand of `D^2/L^2` appears in none of the seven rows, as
required of `[_-]`.

Lower-grade negative parts vanish by §3, so the unitriangular change from
`z`-Laurent to `w`-Laurent at grade ten is homogeneous: no lower charged
row can mix an inhomogeneous term into this grade. The third-tail note's
warning about mixing applies only when a previous negative tail is
nonzero; that does not occur here.

Sufficiency of seven rows is a degree statement, not a row-count slogan.
Clearing the denominator of `(2.1)` gives the polynomiality criterion
`(2.2)`. The unreduced numerator `6 D^2+5 k10 R^3 L` has degree six
because `deg D=3`. Design §2's phrase “degree at most five” is therefore
slightly loose if read of the unreduced numerator; after deleting the
polynomial `L^2 A^2`, the leftover `2 L A C + C^2 + 5 k10 R^3 L` reduces
modulo `L^2` to a remainder of degree at most three. A proper rational
function with monic denominator of degree four vanishes if and only if its
first four negative Laurent coefficients vanish. Vanishing of the first
seven ordinary coordinates, equivalent by unitriangularity to vanishing of
the first seven Laurent coefficients, is more than enough. The extra three
rows are consistent zeros or redundant linear combinations, not an
independent obstruction.

---

## 5. UFD interpretation

Polynomiality of `(2.1)` is equivalent to `L^2 | 6 D^2 + 5 k10 R^3 L` in
characteristic zero. Reducing modulo `L` and using `D\equiv C` gives
`L | 6 C^2`. On `D(p)`, `L=z^2+p/2` is squarefree (two distinct roots in
a quadratic extension; equivalently, prime in the UFD `k(p)[z]` when
`-p/2` is a nonsquare). The constant `6` is a unit. Thus `L | C^2`, hence
`L | C`. The chart forces `deg C<deg L`, so `C=0`.

With `C=0` the criterion becomes `L | 5 k10 R^3`. On `D(k10)` the factors
`5` and `k10` are units, so `L | R^3`, hence `L | R` by squarefreeness,
hence `R=0` because `deg R<deg L`. Squarefreeness is still required at
this second step: degree alone would permit `R^3` to be `L` times a
linear. The hypothesis remains in force from the first step and is not
missing. Characteristic zero is used honestly: it supplies invertibility
of `2,3,5` in the binomial coefficients and in `6` and `5`.

Conventions `R=cs z+rs/4` and `C=(c1 z+c0)/2` are the same as in the
load-ladder chart (where `S=(v1 z+v0)/2`) and match the compiler.

The raw localized standard basis printed in both stdout artifacts is not
radical: it contains `c1^3`, `c0^3`, `c0 c1`, `p c1^2-2 c0^2`, mixed
`A C` generators, and high powers of `cs,rs`. That is the scheme
thickness the design required to retain. After `sat(-,p)` then
`sat(-,k10)`, both lanes report radical `(c1,c0,rs,cs)` with both
generator-wise containments equal to one, i.e. equality with
`(c0,c1,cs,rs)`. Sequential saturation by `p` and `k10` is saturation at
`D(p*k10)` and does not discard an embedded component on that open.
Nilpotent generators involving `A` when `C\neq 0` live over `V(C)` as
thickness, not as an extra reduced component; on the reduced support `A`
is free, as claimed.

---

## 6. Good-prime role

`F_65521` is an independent compiler and engine control, not a
characteristic-zero proof. The two `.sing` files differ only in
characteristic; the displayed `F_65521` rows are the image of the exact-Q
rows (checked for the unitriangular first coordinate: `3/8\equiv-24570`
in `F_65521`). Every binomial denominator in the compiled source is a
power of two; `65521` is odd, so those units survive. The coefficients
`3` and `5` are nonzero. Localization factors are the variables `p` and
`k10`, not the prime `65521`. On `D(p)`, `L` remains squarefree in
characteristic `65521` because `2\neq 0`. No charged denominator of the
receiver or of the UFD argument vanishes in this field.

---

## 7. Correction awareness and scope

The load-ladder endpoint itself recorded that it was not correction-aware:
replacing the already-zero `M` and `S` by higher-order corrections can
create cross terms at the same grade as `k10 R^3/L`. The third-tail
theorem forces only the reduced `M=0` on `D(p)` and explicitly forbids
substituting `K=L^2`, `N=LM` globally. The cross-pollination note asked
for a source-typed generic-square next-grade receiver retaining `R,S,k10`
and the first permitted rescalings. This calculation is that receiver
along the single ray `wt(Lambda,M,S,R)=(2,3,1,0)`.

The mixed term `2AC/L` is present in the analytic receiver `(2.1)` and in
ordinary rows 1, 2, 3, 5, and 7. It is absent from rows 4 and 6, which is
compatible with the Laurent parities of `AC/L` and does not remove it
from the obstruction. RESULTS §4's phrase “present in every row” is
therefore an overstatement of the seven coordinates, not of the
rational function. The overstatement is not load-bearing: the first
coordinate already contains `(3/8)(a1 c0+a0 c1)`, and the radical still
kills `C` then `R`. No numbered identity is repaired.

The ray includes its coordinate faces `A=0`, `C=0`, and `R=0`. The face
`A=0` recovers the old sequential `S` then `R` ladder as a simultaneous
grade-ten slice. The new face is `C=0` with `A` free.

It does not prove that every valuation centred at the generic square
component lies on this ray. Smaller or larger valuations need a
lowest-weight or Newton-fan argument. The direction `A` survives at this
grade; the parenthetical observation that the next `k10` term in the
zero-new-correction subchart is proportional to `A^2/L` is not a
correction-aware verdict, and RESULTS §4 says so. Still open: `p=0`, the
square/discriminant intersection, the terminal row, both Taylor
receivers, higher-contact corrections, and existence or exclusion of a
strict arc.

---

## Strongest surviving theorem

On the generic square open `p\neq 0`, after the reviewed first-normal
support and the exact third-tail reduced gate `M=0`, impose the primitive
normalized corrections `Lambda=sigma^2`, `M=sigma^3 A`, `S=sigma C` with
`A` linear, `C=(c1 z+c0)/2`, `R=cs z+rs/4`, and first-contact saturation
`k10\neq 0`. Then the complete frozen seven-row source is divisible by
`sigma^{10}`, the divided grade is independent of `k6,k2` and of both
Taylor families and the terminal row, and it is the charged unitriangular
image of

```text
[(3/8)(LA+C)^2/L^2 + (5/16) k10 R^3/L]_- .
```

Polynomiality of that receiver forces `C=R=0` on `D(p*k10)` in
characteristic zero, with `A` free. The raw source ideal at this grade is
not reduced. This is a theorem about one normalized ray and its
coordinate faces.

---

## Exact scope

Generic square chart `L=z^2+p/2` with `p\neq 0`, after reduced `M=0` and
on `D(k10)`, at the single weighted ray `wt(Lambda,M,S,R)=(2,3,1,0)`,
through total sigma grade ten of the complete frozen seven tails. Exact
`Q` is the characteristic-zero promotion; `F_65521` is software control.

---

## Sharpest non-claim

This is not a proof that the ray exhausts the generic-square Newton fan,
not an exclusion of the square component, not a statement at `p=0` or at
the square/discriminant intersection, not a terminal or Taylor receiver,
not a correction-aware verdict on the surviving `A` direction, and not a
strict-arc, order-two, `(8,12)`, maximum-twelve, or JC2 conclusion.

ORDER2_SQUARE_HALFWEIGHT_RAY_CONFIRMED
