# Hostile different-model review — AS D7 divided-carry erratum

| Field | Value |
|---|---|
| Claim under review | Frozen erratum: the quadratic first-carry bracket has universally zero basic Cartier coefficient, but it is not the full first residual. The source-honest residual contributes `u5_3+v5_2=0`. On the deep `D=7` branch the correct ideal has 40 variables and 30 rows and admits the displayed exact three-piece nonreduced cover |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks below; accepted second digits, the following integer carry, other associated-top branches, full `D=7`, all-depth lifting, characteristic zero, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian expansion over `Z` (not a mod-three bracket reconstruction); independent sparse coefficient emitter using integer derivatives then reduction modulo 3; 80 random `F3` row-vs-`det J` spot-checks plus 40 random `(C,D)` checks of the `9C,9D` residual modulo 27; independent Singular Groebner bases, radical, saturations, and two-sided containments across `dp`/`lp`/`Dp`, reversed generators, and reversed variables; unmodified rerun of the five registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the erratum producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `7832fb73ac887041968f9cec2dc6cba7aa0d0bcf` (the charged basis) |
| Git HEAD at close | `1144839652c6a4750b9b0cd43e21d80cc9a755eb` (unrelated max-12 Faber commit; charged basis remains an ancestor; erratum bytes unchanged) |
| Review window (UTC) | 2026-08-24T18:14:43Z – 2026-08-24T18:40:59Z |
| Python | host CPython 3.14.6 (hashes, integer identities, sparse emitter, spot-checks, registered replays) |
| Singular | 4.4.1 |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md` (SHA-256 `cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194`)
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/FREEZE.txt` (SHA-256 `e1e8bd61077354d3523c9b655980fe6118164fdbb67e7ff1930db064df0643f6`)
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/MANIFEST.sha256` (SHA-256 `15eaebe76b10f27f63bf16e01efebbb623d0a7c03a7c45787aa58fd977f0736d`)
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/README.md` (SHA-256 `f1d1fb0a1db89d44697b72c61c72f81e1ed82e77252b695548f8cd78912ea6b6`)
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/replay_divided_linear_carry.py` (SHA-256 `dde2c39caaaadae1a5e881c511cecc73c8842083076a01af50b950f91be59bfa`)
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/audit_divided_linear_carry.sing` (SHA-256 `a271c47faa8fcb8f96ecc9e7b04e4305237f59ec867feb4c4d9a0e4972dc0518`)
- `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/generate_corrected_deep_branch_gate.py` (SHA-256 `41ee62190262d779e36a62183cbdf27f05273cff5ac91cbcd002e324a3facca3`)

Quarantined predecessor, consumed only for the retraction ledger and byte-preservation check, never as mathematical evidence:

- `xmodel/as-fonly-first-carry-cartier-zero-deep-d7-20260824.md` (SHA-256 `b0ee40acf7e1df81574d0a41f0338df86b124cae475ad56bbf4e464b481a27f7`)
- `cases/as_fonly_first_carry_cartier_zero_deep_d7_20260824/FREEZE.txt` (SHA-256 `ef500fa54af3cb8070ccfb991cb9ae9d09772177e3ae427199ac87be3b31a071`)
- `cases/as_fonly_first_carry_cartier_zero_deep_d7_20260824/MANIFEST.sha256` (SHA-256 `59684bd4f16ed71432eb461b1de2c3b7ebd41ac35d9fb8ff6c53bf87fa38104d`)

The charged basis is `7832fb73ac887041968f9cec2dc6cba7aa0d0bcf`. Review started there. During the window an unrelated commit `1144839652c6a4750b9b0cd43e21d80cc9a755eb` (`Promote universal maximum-12 Faber landing`) advanced `HEAD`; it does not touch this erratum. The charged basis remains an ancestor. Named producer artifacts remain uncommitted. Recomputed erratum hashes at close match the launch table. No producer, case, canonical, ladder, notes, prompt, log, run, freeze, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_d7_divided_carry_review/` and did not import `generate_corrected_deep_branch_gate.py`, `replay_divided_linear_carry.py`, or `audit_divided_linear_carry.sing`.

Tried hard, and failed, to reconstruct the next residual from a mod-three bracket of `(U,V)` alone; to make `L/3` an integer polynomial off the 14-row first-divergence scheme; to cancel `[x^2 y^2]` by any bounded `C_x+D_y`; to keep the negative control `U=x^3 y^2`, `V=x^2 y` inside the corrected ideal; to leak a divided-linear term into carry degrees 12 or 11; to keep a degree-six Frobenius coefficient in a cap-boundary or Cartier row; to recover dimension 19 after adjoining `u5_3+v5_2`; to make the original 30-row ideal radical; to restore the old two-piece saturation equality; to drop `E` or to replace `q4^2` / `u5_0^2` by first powers; to change the ideal by reversing generators or switching to `lp`/`Dp`; and to promote the erratum to an accepted second digit, a completed next carry, other branches, full `D=7`, all-depth lifting, characteristic zero, a counterexample, or JC2.

---

## Promotion

**Accept `THE QUADRATIC FIRST-CARRY BRACKET HAS UNIVERSALLY ZERO BASIC CARTIER COEFFICIENT, BUT IT IS NOT THE FULL FIRST RESIDUAL. THE SOURCE-HONEST RESIDUAL CONTRIBUTES THE ADDITIONAL ROW u5_3+v5_2=0. ON THE DEEP D=7 BRANCH THE CORRECT IDEAL HAS 40 VARIABLES AND 30 ROWS AND ADMITS THE EXACT THREE-PIECE NONREDUCED COVER RECORDED BELOW.`**

On the map-only first digit `P=x-x^3+3U`, `Q=y+3V`, then `P_new=P+9C`, `Q_new=Q+9D`:

- Over `Z`, `det J(P,Q)-1=3L+9K` with `L=U_x+V_y-x^2` and `K=(U_x-x^2)V_y-U_y V_x`. After adjoining `9C,9D` the exact expansion is `3L+9(K+C_x+D_y)+27M+81N`. The quotient `L/3` is an integer polynomial if and only if `L≡0 mod 3`, which is exactly first-digit admissibility modulo nine. On that scheme the next residual is `L/3+K+C_x+D_y` modulo three.
- The basic Cartier coefficient of `K` vanishes for every prime. The same coefficient of `L/p` is `u_(p,p-1)+v_(p-1,p)`, hence `u5_3+v5_2` at `p=3`. The integer pair `U=x^3 y^2`, `V=x^2 y` satisfies the old 29-row test and has full-residual Cartier coefficient one.
- On the charged deep branch `U_7=V_7=0` with degree-six Frobenius layers, the first-digit acceptance ideal in the 40 lower variables is the independently enumerated 30-row scheme: 14 first-divergence rows, nine degree-eight carry rows, six degree-seven carry rows, and the divided-linear Cartier row. The six Frobenius coefficients remain a free `A^6` factor. No divided-linear term reaches the already reviewed degree-12/11 associated-top gate.
- Over `F_3`, with `dp` and `redSB`: 40 variables, 30 rows, reduced Groebner size 269, dimension 18, radical Groebner size 44, original ideal not radical. The ideal, not the Groebner-basis size, is independent of monomial order and generator order. No minimal-prime or primary decomposition is inferred from the radical.
- From the original 30-row `I`, with the named quartic separator `q4`, one has `I=Q0∩B=Q0∩Q1∩E` by two-sided reduction, with piece statistics `(18,150)`, `(18,169)`, `(17,3277)`. The old two-piece cover fails. `E` is load-bearing. The pieces are localization aids, not asserted primary or minimal.

**Do not promote this to:** a classification of accepted second digits; a completed following integer carry; a statement about other associated-top branches; emptiness or nonemptiness of `FONLY_(3,7)(D=7)` or of the full depth-seven locus; all-depth lifting; a characteristic-zero lift or no-lift theorem; a counterexample to JC; or any JC2 inference. Do not replace `I` by `Q0`, `Q1`, `E`, or the radical.

**Smallest honest successor.** The degree-ten mixed-carry system coming from the coefficient of `27` in `det J(P+9C,Q+9D)-1`, generated componentwise from the original nonreduced `I` (retaining `E`), together with the accepted-second-digit equations that make the first residual integrally divisible by three. That mixed carry has total degree at most ten and no degree-eleven term. The three pieces in `(8)` may guide localization; none may replace `I`. A reduced-only calculation still covers field-valued points of *this* gate, but it is not an honest successor for accepted-digit / Fitting recursion.

---

## Quarantine

The following predecessor statements are retracted and must not be reused as live mathematics:

- `K` is the full first residual;
- the 29-row ideal completely characterizes first-digit acceptance on this branch;
- old dimension 19 and the old minimal/saturation component statistics;
- the old two-piece equality `I=(I:q4^∞)∩(I:u5_0^∞)`.

The quarantined bytes themselves are unchanged. Generic uncarried first-residual tests that omit `L/3`, and any cover that drops `E` or uses only the two old saturations of `I`, are quarantined. No result here proves or disproves JC2, constructs or excludes a polynomial lift of `(x-x^3,y)`, empties or populates `FONLY_(3,7)(D=7)`, runs a second accepted digit, or produces a compatible tower. Producer strings `PASS-DIVIDED-LINEAR-CARRY-ERRATUM`, `PASS-SINGULAR-DIVIDED-LINEAR-CARRY-ERRATUM`, and `PASS-DEEP-BRANCH` were not used as evidence; the Jacobian identities, every row coefficient, the Cartier coefficient, both containment directions of `(8)`, and nonradicality were re-derived. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; one total-degree cap seven; the first map digit only; the aligned deep branch `U_7=V_7=0` with degree-six Frobenius layers; first-divergence rows and quadratic-carry rows of degrees 8 and 7; the divided-linear Cartier row; an exact nonreduced cover of that ideal. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `P0=x-x^3`, `Q0=y`, `P=P0+3U`, `Q=Q0+3V`, the identity `det J-1=3L+9K` holds over `Z` with `L=U_x+V_y-x^2` and the displayed sign of `K`. `L/3` is integral on the charged first-digit scheme if and only if `L≡0 mod 3`. After `9C,9D` the next residual is `L/3+K+C_x+D_y` modulo three | **CONFIRMED** | a leftover `27`-term already in the `(U,V)`-only expansion; opposite sign on `K` or on `-x^2`; `L/3` integral off the 14-row divergence scheme; next residual equal to `K+C_x+D_y` with `L/3` omitted |
| 2 | `[x^{p-1}y^{p-1}]K=0` for every prime, while `[x^{p-1}y^{p-1}](L/p)=u_(p,p-1)+v_(p-1,p)`, hence `u5_3+v5_2` at `p=3,D=7`. The integer pair `U=x^3 y^2`, `V=x^2 y` passes the old 29-row test and has full-residual coefficient one at `x^2 y^2` | **CONFIRMED** | a contributing pair with `ad-bc` not divisible by `p`; a second source for the Cartier slot of `L/3`; the negative control failing a divergence or degree-8/7 row; `[x^2 y^2]` of the integer residual not `1 mod 3`; some bounded `C_x+D_y` hitting that slot |
| 3 | Independent coefficient arithmetic produces 40 variables and 30 nonzero rows: 14 first-divergence, nine degree-eight carry, six degree-seven carry, and `u5_3+v5_2`. The six degree-six Frobenius coefficients are a free factor. No omitted divided term reaches carry degrees 12 or 11 | **CONFIRMED** | a vanished or extra row; a coefficient/sign mismatch against integer `L` or `K`; a Frobenius name in a displayed row; `L/3` of degree `>=11`; adjoining the six Frobenius variables failing to raise dimension by six |
| 4 | Over `F_3`: reduced Groebner size 269, dimension 18, radical Groebner size 44, original `I` not radical. The ideal is independent of `dp`/`lp`/`Dp` and of generator order. No minAss/primary inference from the radical | **CONFIRMED** | Groebner size other than 269 in the producer `dp`+`redSB` ring; dimension other than 18; radical size other than 44; `reduce(radical(I),I)=0`; `lp`/`Dp`/reversed generators producing a different ideal; a minAss count sold as a corollary of the radical |
| 5 | From original `I`: `Q0=I:q4^∞`, `B=I+(q4^2)`, `Q1=B:u5_0^∞`, `E=B+(u5_0^2)` satisfy both directions of `I=Q0∩B=Q0∩Q1∩E`, with piece statistics `(18,150)`, `(18,169)`, `(17,3277)`. The pieces are not asserted primary or minimal. `E` is load-bearing | **CONFIRMED** | a nonzero two-sided remainder in `(8)`; the old two-piece cover still equal to `I`; `Q0∩Q1` without `E` equal to `I`; `q4^1` or `u5_0^1` restoring equality; a primary or minimal-component claim |
| 6 | The universal Cartier-zero lemma for `K` and the degree-12/11 associated-top gate survive. Full-residual, 29-row completeness, old dimension/component statistics, and the old two-piece cover are retracted. Old frozen bytes are unchanged. No second-digit / next-carry / other-branch / full-D7 / all-depth / characteristic-zero / counterexample / JC2 inference. The degree-ten mixed-carry system from original nonreduced `I` is the smallest honest successor | **CONFIRMED** | old report/freeze/manifest hashes mutated; the erratum still asserting 29-row completeness or dimension 19; `FONLY_(3,7)(D=7)=∅` or `≠∅` asserted; the successor sold as already computed, as a reduced-only calculation, or as a replacement of `I` by a cover piece |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Registered commands, rerun unmodified from the replacement case directory:

```sh
python3 replay_divided_linear_carry.py
Singular -q audit_divided_linear_carry.sing
python3 generate_corrected_deep_branch_gate.py | Singular -q
COVER=1 python3 generate_corrected_deep_branch_gate.py | Singular -q
RADICAL=1 python3 generate_corrected_deep_branch_gate.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

All six exited 0. Manifest contents (`README.md`, `audit_divided_linear_carry.sing`, `generate_corrected_deep_branch_gate.py`, `replay_divided_linear_carry.py`) matched. Default generate printed `40/30/269/18` and the 30 labels recorded below. `COVER=1` printed separator `q4`, saturation exponents hardcoded as `2,2`, piece statistics `18,150 / 18,169 / 17,3277`, two-sided remainders `0,0` and `0,0`, and both intersection equalities `1`. `RADICAL=1` printed radical size `44` and original-is-radical `0`. These runs were regressions only.

Recomputed SHA-256 (all match the launch prompt and `FREEZE.txt`):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md` | `cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194` |
| `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/MANIFEST.sha256` | `15eaebe76b10f27f63bf16e01efebbb623d0a7c03a7c45787aa58fd977f0736d` |
| `cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/FREEZE.txt` | `e1e8bd61077354d3523c9b655980fe6118164fdbb67e7ff1930db064df0643f6` |
| `replay_divided_linear_carry.py` | `dde2c39caaaadae1a5e881c511cecc73c8842083076a01af50b950f91be59bfa` |
| `audit_divided_linear_carry.sing` | `a271c47faa8fcb8f96ecc9e7b04e4305237f59ec867feb4c4d9a0e4972dc0518` |
| `generate_corrected_deep_branch_gate.py` | `41ee62190262d779e36a62183cbdf27f05273cff5ac91cbcd002e324a3facca3` |
| `README.md` | `f1d1fb0a1db89d44697b72c61c72f81e1ed82e77252b695548f8cd78912ea6b6` |

Quarantined predecessor hashes, unchanged:

| Artifact | SHA-256 |
|---|---|
| old report | `b0ee40acf7e1df81574d0a41f0338df86b124cae475ad56bbf4e464b481a27f7` |
| old freeze | `ef500fa54af3cb8070ccfb991cb9ae9d09772177e3ae427199ac87be3b31a071` |
| old manifest | `59684bd4f16ed71432eb461b1de2c3b7ebd41ac35d9fb8ff6c53bf87fa38104d` |

The old manifest contents (`README.md`, `audit_cartier_control.sing`, `generate_deep_branch_gate.py`, `replay_universal_cartier.py`) still verify. Old freeze payload hashes `5f4d952cac06d1c2020d942b65321a89ed659d5ba616e579786e33440ae2e9dd`, `1d1cc0793f28dda47e6f09b1734fa8e8bc92ffb42067f7f01d0e4097b5a247db`, `d4a2807a59338660a0b83513d4fa1568d2f67f2fdc477ceec2b6995a6aabba13` are therefore intact.

---

## Independent recomputation

### 1. Integral quotient provenance — CONFIRMED

Let `P_0=x-x^3`, `Q_0=y`, `P=P_0+3U`, `Q=Q_0+3V` in `Z[x,y]`. Direct expansion of the Jacobian, with integer derivatives and no reduction, gives

```text
P_x = 1-3x^2+3 U_x,     P_y = 3 U_y,
Q_x = 3 V_x,             Q_y = 1+3 V_y,
```

and

```text
det J(P,Q)-1
  = 3(U_x+V_y-x^2) + 9((U_x-x^2)V_y-U_y V_x).
```

The right-hand side is exactly `3L+9K` with the producer signs. A generic symbolic expansion through total degree seven left a zero remainder: no `27`-term exists before a second digit is adjoined.

Adjoin `P_new=P+9C`, `Q_new=Q+9D`. The same integer engine produces the complete identity

```text
det J(P_new,Q_new)-1
  = 3L + 9(K+C_x+D_y) + 27 M + 81 N,
```

with

```text
M = -x^2 D_y + U_x D_y + C_x V_y - U_y D_x - C_y V_x,
N = C_x D_y - C_y D_x.
```

Remainder against the expanded Jacobian was empty.

**When `L/3` is integral.** Write `L` as an integer polynomial in the coefficient variables of `U,V`. A coefficient of `L` is identically divisible by three if and only if it comes from an exponent divisible by three (or from the Cartier slot treated below). The remaining coefficients are units times displayed linear forms. Reducing `L` modulo three is exactly the `F_3` first-divergence polynomial computed with `F_3` derivatives. Therefore `L/3` is an integer polynomial if and only if every coefficient of `L` vanishes modulo three, if and only if the 14 first-divergence rows vanish. That is precisely first-digit admissibility modulo nine, because `det J-1=3L+9K` is then `0 mod 9`.

The Cartier coefficient of `L` is exceptional: it is identically `3(u5_3+v5_2)` before those 14 rows are imposed. So that one coefficient of `L/3` is an integer polynomial even off the scheme; the rest of `L/3` is integral only on the scheme.

**Next residual.** On the scheme write `L=3 L_3`. Then

```text
det J(P_new,Q_new)-1
  = 9(L_3+K+C_x+D_y) + 27 M + 81 N,
```

so

```text
(det J-1)/9 ≡ L_3+K+C_x+D_y  (mod 3).
```

A reconstruction that keeps only the quadratic bracket `K` and the second-digit divergence misses `L_3`. Forty random integer lifts of `(U,V,C,D)` with coefficients in `{0,1,2}` confirmed `det J-1 ≡ 3L+9(K+C_x+D_y) modulo 27`. That congruence is the truncation of the exact identity, not a substitute for it.

### 2. Cartier row and falsifier — CONFIRMED

A monomial pair `u_(a,b) x^a y^b`, `v_(c,d) x^c y^d` contributes to `x^{p-1} y^{p-1}` in `U_x V_y-U_y V_x` only when `a+c=p` and `b+d=p`. The multiplier is

```text
ad-bc = a(p-b)-b(p-a) = p(a-b) ≡ 0  (mod p).
```

This is an integer identity, not a `p=3` enumeration. The seed `-x^{p-1} V_y` contributes to the same slot only by differentiating `y^p`, with multiplier `p≡0`. Direct expansion of generic `K` through degree seven has thirteen integer terms at `x^2 y^2` and zero terms modulo three. Thus `[x^{p-1} y^{p-1}]K=0` for the quadratic bracket, including the AS seed.

The same slot of `L=U_x+V_y-x^{p-1}` is produced only by `U=u_(p,p-1) x^p y^{p-1}` and `V=v_(p-1,p) x^{p-1} y^p`. Integer derivatives supply the factor `p` in both cases, so

```text
[x^{p-1} y^{p-1}](L/p) = u_(p,p-1)+v_(p-1,p).
```

At `p=3` the unique such monomials in degrees `≤7` are `x^3 y^2` and `x^2 y^3`, i.e. `u5_3+v5_2`. There is no other source: the derivative factors are exactly three, so the row exists before clearing, radicalization, or a component split.

**Negative control.** Take integer representatives `U=x^3 y^2`, `V=x^2 y`. Then

```text
L = 3 x^2 y^2,     L ≡ 0 (mod 3),
K ≡ 2x^4 + 2x^4 y^2 (mod 3),
```

so every first-divergence row and every degree-eight/degree-seven carry row vanishes, and `[x^2 y^2]K=0`. Direct integer expansion nevertheless gives

```text
det J(x-x^3+3U, y+3V)-1 = -9x^4 + 9x^2 y^2 - 9x^4 y^2,
```

so the full residual over nine is `-x^4+x^2 y^2-x^4 y^2` and

```text
[x^2 y^2]((det J-1)/9) ≡ 1 (mod 3).
```

This is `L/3+K` reduced modulo three. The same point, evaluated on the independently emitted 30 rows, kills every divergence and cap-boundary row and leaves the Cartier row equal to `1`. It therefore passes the old 29-row test and fails the corrected gate.

No bounded second digit cancels that class: for `C_x+D_y` to produce `x^2 y^2` one needs a factor `3` from differentiating `x^3` or `y^3`. Forty random `(C,D)` of degree at most seven had `[x^2 y^2](C_x+D_y)=0` in `F_3`. The cokernel of divergence in degrees `≤6` is spanned by the single monomial whose two exponents are both `2 mod 3`, namely `x^2 y^2`.

The quarantined control `U=x^3`, `V=x^2 y` still passes both the 29-row and the 30-row tests (`L=3x^2`, Cartier zero). It is a witness that `[x^2 y^2]K=0`, not a witness that `K` is the full residual.

### 3. Corrected source ideal — CONFIRMED

Variables are every coefficient of `U,V` in homogeneous degrees `1..5`, named `u{d}_{i}` / `v{d}_{i}` for the monomial `x^i y^{d-i}`:

```text
deg 1: 4,  deg 2: 6,  deg 3: 8,  deg 4: 10,  deg 5: 12;  total 40.
```

Independent integer derivatives of this generic pair, then reduction modulo three, produced exactly 30 nonzero rows. Labels and `F_3` polynomials:

```text
div_0_0     u1_1+v1_0
div_0_1     u2_1+2*v2_0
div_1_0     2*u2_2+v2_1
div_0_2     u3_1
div_1_1     2*u3_2+2*v3_1
div_2_0     2+v3_2
div_0_3     u4_1+v4_0
div_1_2     2*u4_2
div_2_1     2*v4_2
div_3_0     u4_4+v4_3
div_0_4     u5_1+2*v5_0
div_1_3     2*u5_2+v5_1
div_3_1     u5_4+2*v5_3
div_4_0     2*u5_5+v5_4
carry_0_8   u5_0*v5_1+2*u5_1*v5_0
carry_1_7   2*u5_0*v5_2+u5_2*v5_0
carry_2_6   u5_1*v5_2+2*u5_2*v5_1
carry_3_5   u5_0*v5_4+2*u5_1*v5_3+u5_3*v5_1+2*u5_4*v5_0
carry_4_4   2*u5_0*v5_5+u5_2*v5_3+2*u5_3*v5_2+u5_5*v5_0
carry_5_3   u5_1*v5_5+2*u5_2*v5_4+u5_4*v5_2+2*u5_5*v5_1
carry_6_2   u5_3*v5_4+2*u5_4*v5_3
carry_7_1   2*u5_3*v5_5+u5_5*v5_3
carry_8_0   u5_4*v5_5+2*u5_5*v5_4
carry_0_7   2*u4_0*v5_1+2*u4_1*v5_0+u5_0*v4_1+u5_1*v4_0
carry_1_6   u4_0*v5_2+u4_1*v5_1+u4_2*v5_0+2*u5_0*v4_2+2*u5_1*v4_1+2*u5_2*v4_0
carry_3_4   2*u4_0*v5_4+2*u4_1*v5_3+2*u4_2*v5_2+2*u4_3*v5_1+2*u4_4*v5_0
            +u5_0*v4_4+u5_1*v4_3+u5_2*v4_2+u5_3*v4_1+u5_4*v4_0
carry_4_3   u4_0*v5_5+u4_1*v5_4+u4_2*v5_3+u4_3*v5_2+u4_4*v5_1
            +2*u5_1*v4_4+2*u5_2*v4_3+2*u5_3*v4_2+2*u5_4*v4_1+2*u5_5*v4_0
carry_6_1   2*u4_2*v5_5+2*u4_3*v5_4+2*u4_4*v5_3+u5_3*v4_4+u5_4*v4_3+u5_5*v4_2
carry_7_0   u4_3*v5_5+u4_4*v5_4+2*u5_4*v4_4+2*u5_5*v4_3
divided_linear_cartier_2_2   u5_3+v5_2
```

Counts: 14 first-divergence, 9 degree-eight, 6 degree-seven, 1 Cartier. The genuinely zero slots are `div_2_2` (the Cartier slot of `L` over `F_3`, identically `0` because the integer coefficient is `3(u5_3+v5_2)`), `carry_2_5`, and `carry_5_2`. Degree four therefore contributes four of five monomials; degree seven contributes six of eight; degree eight contributes all nine.

Eighty random `F_3` assignments produced zero mismatches between these rows and the corresponding coefficients of integer `L` and `K`. The Cartier row matched both `u5_3+v5_2` and `[x^2 y^2](L/3)` whenever that coefficient of `L` was divisible by three.

**Frobenius free factor.** The six coefficients of `U_6=a x^6+b x^3 y^3+c y^6` and `V_6` analogously do not appear in `L mod 3`, in `K mod 3` at degrees 8 or 7, or in the Cartier slot of `K`. Their integer contribution to `L/3` has degree five and does not meet `x^2 y^2`. Adjoining the six names as unused variables raises dimension from 18 to 24 and leaves Groebner size 269. They remain a free `A^6` factor of first-digit acceptance on this branch.

**Degree-12/11 gate.** The always-divisible-by-three part of `L`, including a full degree-seven layer, has total degree at most six. After imposing the `F_3` divergence rows, the leftover quotient still has degree at most six. Carry degrees 12 and 11 of the associated-top gate are coefficients of `K` on `(U_7+U_6,V_7+V_6)`; those degrees occur in `K` (10, 11, and 12), not in `L/3`. The divided-linear correction cannot reach that gate. The already reviewed associated-top checkpoint is therefore not disturbed by this erratum.

Non-Cartier coefficients of `L/3` on the displayed lower layers occupy degrees `≤4` at slots other than `(2,2)`. They are absorbed by `C_x+D_y` and are not extra constraints on `(U,V)`.

### 4. Exact algebra — CONFIRMED

Independently emitted generators, `ring r=3,(u1_0,...,v5_5),dp` with `option(redSB)`:

```text
variables                         40
rows                              30
reduced Groebner basis size      269
dimension                         18
radical Groebner basis size       44
reduce(radical(I), I) size        21
reduce(I, radical(I)) size         0
I radical?                        no
```

So `I ⊂ rad(I)` properly. No `minAss`, `primdecGTZ`, or `primdecSY` was run, and the radical basis of size 44 is not a component count.

Order and generator attacks, two-sided reduction against the `dp` basis of the independently generated ideal:

| Attack | GB size | dim | two-sided remainders vs `dp` `I` |
|---|---|---|---|
| `dp`, listed generators | 269 | 18 | (reference) |
| `dp`, reversed generators | 269 | 18 | `0,0` |
| `dp`, reversed variable order | 142 | 18 | `0,0` |
| `lp` | 78 | 18 | `0,0` |
| `Dp` | 78 | 18 | `0,0` |

The ideal is invariant. The reduced Groebner-basis *size* 269 is specific to the producer monomial order `dp` with `redSB`. Sizes 142 and 78 are not a contradiction. In particular `lp`/`Dp` size 78 coinciding with the old 29-row `dp` size is an artifact of order, not a restoration of the retracted scheme.

Dropping only the Cartier row from the independently generated ideal recovers the retracted 29-row scheme: Groebner size 78, dimension 19, and `I_30 ⊂ I_29` properly (`reduce(I_30,I_29)=0`, converse remainder 232). That is the dimension drop the erratum asserts, obtained without reading the quarantined generator.

### 5. Nonreduced cover — CONFIRMED

The named separator, copied only as a polynomial and then consumed against independently generated `I`, is

```text
q4 = u4_3^2 v4_1^2 + u4_3 v4_0 v4_1 v4_3
   - u4_0 v4_1 v4_3^2 - u4_3 v4_0^2 v4_4
   + u4_0 u4_3 v4_1 v4_4 + u4_0 v4_0 v4_3 v4_4
   + u4_0^2 v4_4^2.
```

Over `F_3` it is irreducible, and it satisfies the independent identity

```text
q4 = (u4_3 v4_1 - u4_0 v4_4)^2
   + (u4_3 v4_0 - u4_0 v4_3)(v4_1 v4_3 - v4_0 v4_4).
```

It is used as a localization separator inherited from the earlier associated-top calculation, not as a primary generator.

From the original 30-row `I`:

```text
Q0 = I : q4^∞,
B  = I + (q4^2),
Q1 = B : u5_0^∞,
E  = B + (u5_0^2).
```

Independent `dp`+`redSB` statistics:

```text
dim(Q0), size(Q0) = 18, 150
dim(Q1), size(Q1) = 18, 169
dim(E),  size(E)  = 17, 3277
dim(B),  size(B)  = 18,  373
```

Two-sided remainders against `I`:

| Test | `reduce(LHS,I)` | `reduce(I,LHS)` | equal to `I`? |
|---|---|---|---|
| `Q0 ∩ B` | 0 | 0 | yes |
| `Q0 ∩ Q1 ∩ E` | 0 | 0 | yes |
| `Q0 ∩ (I+(q4))` | 110 | 0 | no |
| `Q0 ∩ (I:u5_0^∞)` (old two-piece) | 23 | 0 | no |
| `Q0 ∩ Q1` (drop `E`) | 23 | 0 | no |
| `Q0 ∩ E` | 3620 | 0 | no |
| `Q0 ∩ Q1 ∩ (B+(u5_0))` | 38 | 0 | no |
| `Q0` vs `I` | 113 | 0 | no |
| `B` vs `I` | 136 | 0 | no |
| `Q1` vs `I` | 136 | 0 | no |
| `E` vs `I` | 3071 | 0 | no |

Equality `(8)` holds in both directions. Attempts to break it succeeded in every weakening: first powers of the separators, the old two-piece cover of `I`, and dropping `E`. The old two-piece remainder and the drop-`E` remainder are the same 23 extra generators, so `E` is exactly the load-bearing correction of that retraction. `E` does not reduce into `Q0` or `Q1` (remainders 1689 and 3007). `I ⊂ E` holds because `E ⊃ B ⊃ I`.

No piece equals `I`. This review does **not** claim that `Q0`, `Q1`, or `E` is primary, prime, or a minimal component. `E` remains in any successor.

Process remark, non-blocking: this Singular's `sat` list did not expose a second exponent slot. The producer hardcodes `n0=n1=2`. The equality attacks above show that exponent 1 is too small and exponent 2 is sufficient for both separators, so the hardcoded powers are the correct nilpotency indices in the displayed sums.

### 6. Retraction and scope — CONFIRMED

Surviving:

- Universal vanishing of `[x^{p-1} y^{p-1}]K`, including the AS seed, as a statement about the quadratic bracket only.
- Degree-eight and degree-seven cap-boundary rows of `K` (the divided-linear term has degree at most four on the displayed layers and at most five from the free Frobenius layer).
- The separately reviewed associated-top degree-12/11 gate: `L/3` cannot reach those degrees.
- Six derivative-invisible degree-six Frobenius parameters as a free acceptance factor.

Retracted, and independently shown false on the corrected gate:

- `K` is the full first residual. Replacement: equation `(2)`.
- 29-row completeness. Replacement: the 30-row ideal. The 29-row scheme has dimension 19 and properly contains the 30-row scheme.
- Old dimension 19 and old minimal/saturation component statistics.
- Old two-piece saturation equality. After adjoining `(6)` it fails with a 23-generator remainder; equation `(8)` replaces it.

Old frozen bytes are unchanged, as hashed above.

Out of scope, and not inferred: accepted second digits; the following integer carry as a completed computation; other associated-top branches; emptiness or nonemptiness of full `D=7`; all-depth lifting; characteristic zero; a counterexample; JC2.

**Successor.** Let `(C,D)` be a second digit of degree at most seven. The coefficient of `27` in `det J(P+9C,Q+9D)-1` is the mixed polynomial `M` displayed in §1. With `U,V` of degree at most five and `C,D` of degree at most seven, `M` occupies degrees `0..10` and has no degree-11 term. That degree-ten mixed-carry system, generated componentwise from the original nonreduced `I` and retaining `E`, together with the accepted-second-digit equations that make `L/3+K+C_x+D_y` integrally divisible by three, is the smallest honest successor. The cover pieces may localize the computation; replacing `I` by `Q0`, by `Q1`, by `E`, or by `rad(I)` is not honest for accepted-digit / Fitting recursion.

---

## Attacks that failed to refute

- Reconstructing the next residual from `{U,V}` over `F_3` alone: misses `L/3`, and is exactly the quarantined error.
- Finding a second Cartier source in degrees `≤7`: only `u5_3` and `v5_2`.
- Cancelling `[x^2 y^2]` by a cap-seven divergence: identically zero over `F_3`.
- Putting the negative control on the 30-row scheme: Cartier row evaluates to `1`.
- Leaking `L/3` into degrees 12 or 11, even after restoring a full degree-seven layer: maximum degree six.
- Putting a Frobenius coefficient into a displayed row, or failing to raise dimension by six when the six names are adjoined.
- Restoring dimension 19 after the Cartier row, or making `I` radical.
- Changing the ideal by `lp`, `Dp`, reversed generators, or reversed variables.
- Restoring `I=Q0∩(I:u5_0^∞)`, dropping `E`, or using first powers of the separators.
- Reading a minimal-prime or primary decomposition out of `radical(I)`.

---

## Non-blocking remarks

1. Reduced Groebner size 269 is the `dp`+`redSB` size. The same ideal has reduced sizes 78 in `lp` and in `Dp`. Quote the size together with the order, or quote the two-sided ideal.
2. The producer generator asserts that the `F_3` Cartier coefficient of `K` is the zero polynomial and then adjoins `u5_3+v5_2` by a comment. The independent evidence for that row is the integer coefficient of `L`, not the comment.
3. Eighty random `F_3` points missed the 14-row divergence scheme, as expected for a positive-codimension linear condition. Structured controls, not an affine census, are the point-level evidence.
4. `q4` is an irreducible quartic used as a named separator. Irreducibility is not a primeness claim for `Q0`.
5. `Q1` and `I:u5_0^∞` happened to have the same Groebner size 169 in this ring. Equal size is not equality of ideals, and neither is a minimal component.

None of these remarks changes a coefficient, a dimension, a containment, or a numbered verdict.
