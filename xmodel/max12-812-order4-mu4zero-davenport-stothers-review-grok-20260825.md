# Hostile review — Shioda/Hall divisor-19 elimination of the `(8,12)` order-four `mu_4=0` stratum

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order4-mu4zero-davenport-stothers-elimination-20260825.md` |
| Target SHA-256 | `a5d40fd81838118735c4c2ad379bbac0a1e7d70a66a4a419eff078e8099d7b03` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer (OpenAI Codex, GPT-5 family). Charged reviews were opened only because they are named in target §1; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target, every charged local source, and the official Rikkyo Shioda PDF; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `24184c989634b40b00da1bbc3328bcc6ab92fa9b` (named producer artifact uncommitted) |
| Date | 2026-08-25 |

Independently recomputed SHA-256 of the target is `a5d40fd81838118735c4c2ad379bbac0a1e7d70a66a4a419eff078e8099d7b03`, matching the immutable pin. Producer verdict language, the target's own status line, and every charged review's overall token were not used as evidence. No file other than this review was written.

---

## Verdict

The charged theorem is correct as a necessary-terminal-profile elimination. Independently, from Shioda §1 and §5: essential equivalence is the displayed affine/scaling action, the Hall `m=4` polynomials and the sign of `H=F^3-G^2` match the official PDF byte-for-byte in the printed coefficients, `St(4)=1`, and Theorem 5.1 supplies a unique essential-equivalence class over `C`. Transfer of that unique orbit to `Mbar` is a first-order statement about a finite-type `Q`-scheme and is licensed by completeness of `ACF_0`. From the charged tail convention, `g=F_{12}(f)` and `r_1=\cdots=r_6=0` give `W(z(w))=-2r_7 w^5+O(w^4)` with `[z^5]W=-2r_7\neq 0`, so `deg_z W=5`; Davenport over the characteristic-zero field `M` identifies `(f,g,f^3-g^2)` as an order-four DS triple. Monicity forces `c=\alpha^{-4}`; depression forces `beta=-3/4`; the translated Hall coefficients are `21/4` and `11/4`; both lie in `M` and are nonzero, so `\alpha\in M^*`; the leading coefficient of `W` is `27\alpha^{-19}`; and `r_7=-(27/2)\alpha^{-19}` has every zero and pole order on `C` divisible by nineteen. The divisor audit on the smooth normalization of `u^4=h` then yields orders `3,1,1` at multiplicities `m=1,2,3`, a simple pole of nonzero residue at `m=4`, pole degree `m-4` at each `m>4`, unramified finite zeros of order one, and zeros of order `U-1` at all four infinite places. Degree zero forces a single finite root, hence a fourth-power core, contradicting exact Kummer order four. The same DS identity kills the named order-two `U=2,[6,2]` all-zero-load sub-stratum because `div(T)` has orders `\pm 1`. Sheetwise integration constants and residue cancellation do not furnish a loophole. The `mu_4\neq 0` degree-eight lane, the remainder of the order-two client, the order-one leaf, `(8,12)`, maximum twelve, and JC2 are untouched.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order4-mu4zero-davenport-stothers-elimination-20260825.md` | `a5d40fd81838118735c4c2ad379bbac0a1e7d70a66a4a419eff078e8099d7b03` | target (matches required pin) |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` | tail convention `(2.3)`, complete `e=4` loads `(2.5)`–`(2.6)`, terminal row `(2.4)`, unramified unit `t=q^U u` |
| `xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md` | `2f0a03a99ba6563034cdaf84ffc06f6d78ddd377144201d40aa4352ac71c6b55` | named in target §1; opened only to obey the inspection clause; unused as a verdict |
| `xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` | `8r_7'=j/u`, inverse-character line, local orders of `dx/u`, `U=1` residue, `[6,2]` primitive |
| `xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` | named in target §1; unused as a verdict |
| `xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md` | `e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7` | concrete source `h=x^6(x-1)^2`, `T^2=(x-1)/x`, `r_7=(j/4)T`, full load list |
| Official Rikkyo PDF `AA00610867_54-01_04.pdf` | `467701925109586976ca8f89ec614ee95c5ad740084b969a93ba3795b0cdb740` | Shioda 2005; matches the target pin and the DOI record |

All five local hashes match the values printed in target §1 and §6. The PDF was fetched from `https://rikkyo.repo.nii.ac.jp/record/8708/files/AA00610867_54-01_04.pdf` and hashed independently. No D1 compiler, no Stothers 1981 PDF, no Hall 1971 book, and no producer replay was consumed as evidence.

The coefficient-infinity review's `REPAIR` is confined to that target's §7 identity `(7.2)`, which is not an input here. The present theorem uses only the tail convention, the complete `e=4` load list after the three target gauges, the terminal row, and the unramified unit at infinity, all of which are written as identities in the charged source audit itself. Those identities are re-used as formulae and re-derived where they enter a bridge; the review token is not.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero constant field, enlarged harmlessly to contain `\mu_4`. Let `C` be the smooth projective normalization of `u^4=h(x)` with `h\in L[x]` monic of degree `4U` and with the class of `h` in `L(x)^*/L(x)^{*4}` of exact order four. Put `M=L(C)`. Let `f\in M[z]` be monic depressed of degree eight, let `g=F_{12}(f)`, and suppose the ordinary Faber tails of `H_F(w)-g(z(w))` satisfy `r_1=\cdots=r_6=0` and `8 r_7'=j/u` with `j\in L^*`. Then no such pair exists, for every `U\ge 1`.

Equivalently: the entire nontrivial order-four `mu_4=0` terminal stratum is empty. On the separate closed sub-stratum `k_{10}=k_6=k_2=0`, `mu_2=mu_4=mu_6=0` of the source-typed order-two client `U=2`, `h=x^6(x-1)^2`, the same identity is empty.

This is a necessary-terminal-profile statement. It does not assume a Taylor family or a Keller pair, and it does not address `mu_4\neq 0`.

---

## Attack 1 — Shioda §5, Hall `m=4`, `St(4)=1`, unique orbit, ACF0/Lefschetz

**CONFIRMED.** Essential equivalence, the printed Hall polynomials and sign, `St(4)=1`, and Theorem 5.1 match the official PDF. Applying the unique orbit over `Mbar` is licensed. The stated Lefschetz transfer is a correct first-order transfer, not a slogan.

**Essential equivalence.** Shioda, beginning of §5 (PDF p.57): two triples are essentially the same if one is obtained from the other by `(i)` `t\mapsto at+b` with `a\neq 0`, `(ii)` `{f,g,h}\mapsto\{c^2 f,\,c^3 g,\,c^6 h\}` with `c\neq 0`, or a combination. This is target `(1.1)`. Section 6 of Shioda repeats that this is the equivalence used for `(C1)` in Theorem 2.2.

**Definition of a DS triple.** Shioda (3): `{f,g,h}` is a DS triple of order `m` if `f^3-g^2=h`, `deg f=2m`, `deg g=3m`, `deg h=m+1`. Target uses this with `m=4` and writes the triple as `(f,g,f^3-g^2)`.

**Hall `m=4` polynomials and sign.** Shioda §5, bullet `m=4 (Hall [5])`, PDF p.58, prints

```text
f = t^8 + 6t^7 + 21t^6 + 50t^5 + 86t^4 + 114t^3 + 109t^2 + 74t + 28,
g = t^{12}+9t^{11}+45t^{10}+156t^9+408 t^8+846 t^7+1416 t^6
    +1932 t^5+2136 t^4+1873 t^3+(2517/2)t^2+(1167/2)t+299/2,
h = -(27/4)(4t^5+15t^4+38t^3+61t^2+62t+59).
```

Target `(1.2)` is this display, including every half-integer in `G` and the overall minus sign on `H`. The identity `H=F^3-G^2` is Shioda's definition (3) applied to the printed triple. The leading term of the printed quintic is `4t^5`, times `-27/4`, hence `[t^5]H=-27`. That is the only Hall coefficient used later as a number; the remaining printed coefficients of `H` are not consumed.

Hand check that the printed `F,G` can have `deg(F^3-G^2)=5` at all: write `F=t^8(1+x)`, `G=t^{12}(1+y)` with `x=6t^{-1}+21t^{-2}+50t^{-3}+86t^{-4}+114t^{-5}+\cdots` and `y=9t^{-1}+45t^{-2}+156t^{-3}+408t^{-4}+846t^{-5}+\cdots`. The coefficients of `t^{24}` through `t^{19}` in `F^3` and `G^2` agree:

| relative degree | `F^3` | `G^2` |
|---:|---:|---:|
| `t^{0}` | `1` | `1` |
| `t^{-1}` | `18` | `18` |
| `t^{-2}` | `171` | `171` |
| `t^{-3}` | `1122` | `1122` |
| `t^{-4}` | `5649` | `5649` |
| `t^{-5}` | `23076` | `23076` |

(The `t^{-3}` row is `3\cdot50+3\cdot2\cdot6\cdot21+6^3=150+756+216=1122` on the `F` side and `2\cdot156+2\cdot9\cdot45=312+810=1122` on the `G` side; the first arithmetic pass with `3\cdot2\cdot6\cdot21` written as `378` instead of `756` is a trap and was discarded.) This is not a full expansion to `t^5`. It is independent evidence that the printed polynomials are the same cancellation type as a DS triple of order four, and that the printed leading `-27` is the first number one is entitled to read off Shioda's `h`. Characteristic zero is used (`2\neq 0` in the halves of `G`).

**`St(4)=1` and Theorem 5.1.** Shioda (4), PDF p.49: `St(m)=1` for `m=1,2,3,4`. One `m=4` example is printed. Theorem 5.1: for `m\le 5` those examples are a complete set of representatives of essentially distinct DS triples; the proof is one sentence, “this follows from Stothers' enumeration (4)”. For `m=4` that is uniqueness of the essential-equivalence class over `C`. Shioda §8.4 explicitly does *not* supply a completed Mordell–Weil uniqueness proof for `m=4` (“we have not verified every detail”). Uniqueness is Stothers via Shioda, over `C`. The target states this and does not pretend §8 is the uniqueness engine.

**Algebraic setup versus the complex enumeration.** Shioda §2.1: `k` is an algebraically closed field of characteristic zero, later specialised to `C` for Riemann surfaces. Theorem 2.1 is stated with `k=C`. Theorem 5.1 inherits Stothers' complex count. The Hall representative itself is defined over `Q`.

**Lefschetz / `ACF_0` transfer.** Fix degrees `8,12,5`. The functor of triples is a finite-type affine `Q`-scheme: finitely many coefficients, the coefficient equations of `F^3-G^2-H=0`, and the open conditions that the three leading coefficients are nonzero. Essential equivalence is the action of the finite-type `Q`-group `G=\mathrm{Aff}^1\times\mathbb{G}_m`. Hall is a `Q`-point. The statement “every geometric point is in the `G`-orbit of Hall” is the surjectivity of the morphism of finite-type `Q`-schemes `G\times\{\mathrm{Hall}\}\to(\mathrm{DS}\ \mathrm{scheme})` on points. Surjectivity on `C`-points is Theorem 5.1 plus `(4)`. A morphism of finite-type `Q`-schemes which is surjective on `C`-points is surjective on points of every algebraically closed field of characteristic zero: the image is constructible, and `ACF_0` is complete, so a first-order sentence true in `C` is true in `Mbar`. Explicitly, the sentence is

```text
∀ coefficients of (F,G,H):
  (DS equations of degrees 8,12,5)
  ⇒ ∃ a,b,c (ac≠0 and F(t)=c^2 F_Hall(at+b), G(t)=c^3 G_Hall(at+b)).
```

This is first-order in the language of rings (the Hall coefficients lie in `Q`; inequalities are leading coefficients nonzero). The topological content of Stothers is in the *proof over `C`*, not in the sentence. Completeness transfers the sentence, not the dessin. The witnesses `a,b,c` therefore exist in `Mbar`. Descent of `a=\alpha` back to `M` is a separate algebraic computation, carried out in Attack 3, and is not assumed from Lefschetz.

Attacks that failed: treating Shioda's algebraic setup as already uniqueness over every `ACF_0` without Lefschetz (it is not; uniqueness is Stothers over `C`); treating Lefschetz as transferring Riemann existence rather than a first-order orbit statement (degrees are bounded, the scheme is of finite type); expecting an extra orbit over a function field (elementary equivalence of `ACF_0` forbids it); using Shioda §8.4 as uniqueness (it is incomplete, and the target does not use it); a sign mismatch on `H` (the PDF and the target agree, including `-27/4`).

Non-blocking naming: Shioda does not label the Hall display “Example 5.1”. The target's phrase “Example 5.1 / Theorem 5.1” is a section-and-theorem reference, not a numbered environment in the PDF. The polynomials are the ones in §5.

---

## Attack 2 — tail convention, `W=-2r_7 z^5+O(z^4)`, Davenport, `mu_4\neq 0` split

**CONFIRMED.** Signs, the `w`-to-`z` conversion, nonvanishing, and the exact use of Davenport's bound survive. The degree-eight `mu_4\neq 0` lane is correctly separated.

**Convention.** Charged source audit `(2.3)`:

```text
w=f^{1/8},     H_F(w)-g(z(w))=sum_{ℓ≥1} r_ℓ w^{-ℓ}.
```

Under `(0.1)` one has `e=4` and `mu_4=0`, so the three target gauges have already forced `H_F(w)=w^{12}` and the character filter has already forced `r_1=r_2=r_3=r_5=r_6=0`. Thus `g=F_{12}(f)` and

```text
g(z(w))=w^{12}-r_7 w^{-7}+O(w^{-8}).
```

Depression of `f` gives the monic eighth root `w=z+O(z^{-1})`; more precisely, with `[z^7]f=0`,

```text
w=z+(a_6/8)z^{-1}+O(z^{-2}).
```

Characteristic zero is used for `8\neq 0` and for the binomial root.

**Expansion of `W=g^2-f^3`.** By definition `f=w^8`, so `f^3=w^{24}` and

```text
W(z(w))=g(z(w))^2-w^{24}.
```

Square: `g^2=w^{24}-2 r_7 w^{5}+O(w^{4})`, the cross term being `-2 w^{12}\cdot r_7 w^{-7}=-2 r_7 w^5` and the square of the tail being `O(w^{-14})`. Hence

```text
W(z(w))=-2 r_7 w^5+O(w^4).
```

The sign is forced by the convention `H_F-g=sum r_ℓ w^{-ℓ}`. The opposite tail sign would produce `+2 r_7 w^5` and would be incompatible with `(2.3)` of the charged audit.

**Conversion `w\to z`.** From `w=z+O(z^{-1})` one has `w^5=z^5+O(z^3)` (no `z^4` term: the first correction in `w-z` is `O(z^{-1})`). The remainder `O(w^4)` is `O(z^4)`. As an equality of polynomials in `z`, this is

```text
W(z)=-2 r_7 z^5+O(z^4),
```

i.e. `deg_z W\le 5` and `[z^5]W=-2 r_7`. Equivalently, reversion `z(w)=w+O(w^{-1})` preserves the degree and the leading coefficient of a polynomial of degree five. This is target `(2.2)`–`(2.3)`.

**Nonvanishing.** The terminal row is `8 r_7'=j/u` with `j\neq 0`. The form `dx/u` is not the zero form on `C`, so `r_7` is nonconstant, hence nonzero in `M`. Then `[z^5]W=-2 r_7\neq 0` already gives `deg_z W=5`. In particular `W\neq 0`.

**Davenport.** Shioda (1), for nonconstant polynomials over `C` with `f^3\neq g^2`: `deg(f^3-g^2)\ge (1/2)deg(f)+1`. Lemma 3.1(i) is the equivalent form used here, and is stated for an arbitrary field `k` of characteristic zero: if `deg f=2m`, `deg g=3m`, and `deg(f^3-g^2)\le m`, then `f^3=g^2`. The proof is van der Monde on power sums and does not use topology. Applying it to `k=M`, `m=4`, `deg_z f=8`, `deg_z g=12` (the latter because `F_{12}(f)` is monic of degree twelve) yields: if `W\neq 0` then `deg_z W\ge 5`. Combined with the tail bound, equality holds, `deg_z(f^3-g^2)=5`, and `(f,g,f^3-g^2)` is a DS triple of order four over `M`. This is the only use of Davenport's bound in the lane.

**`mu_4\neq 0` is a different polynomial.** If `r_4=mu_4\neq 0`, the expansion is `g=w^{12}-mu_4 w^{-4}-r_7 w^{-7}+\cdots`, so `W=-2 mu_4 w^8+O(w^7)` and `deg_z W=8` exactly. Davenport still gives `deg\ge 5`, which is strictly weaker than equality. Target `(2.2)` is not available. The two strata must not be merged.

Attacks that failed: opposite tail sign; a `z^4` correction in `w^5` spoiling the leading coefficient (the first correction is `O(z^3)`); `r_7=0` forced by the ODE (the right-hand side is a nonzero multiple of `dx/u`); applying Davenport over `C` rather than over `M` (Lemma 3.1 is for any characteristic-zero field); using Davenport to kill `mu_4\neq 0`; treating `W` as a rational function of `z` rather than an element of `M[z]`.

---

## Attack 3 — monicity, depression, Hall constants `21/4` and `11/4`, leading `27\alpha^{-19}`, descent of `\alpha`, divisor `19`

**CONFIRMED.** Every displayed constant recomputes. Both coefficients lie in `M` and are nonzero, so `\alpha` descends. The identity `r_7=-(27/2)\alpha^{-19}` is exact, and `(3.7)` follows.

**Unique orbit, written in coordinates.** Over `Mbar` there exist `\alpha,c\neq 0` and `\beta` with

```text
f(z)=c^2 F(\alpha z+\beta),     g(z)=c^3 G(\alpha z+\beta).
```

This is Attack 1 plus the definition of essential equivalence. No other affine parameter is introduced.

**Monicity.** `F` and `G` are monic of degrees `8` and `12`, as is visible from the PDF, and `f,g` are monic by the high-row normalisation. Leading coefficients:

```text
c^2 \alpha^8=1,     c^3 \alpha^{12}=1.
```

Put `\gamma=c\alpha^4`. Then `\gamma^2=\gamma^3=1`. In characteristic zero, `\gamma^2(\gamma-1)=0` and `\gamma\neq 0` give `\gamma=1`, hence `c=\alpha^{-4}`. The extra sign `c=-\alpha^{-4}` satisfies the first equation and fails the second: `c^3\alpha^{12}=-1`. Both monic conditions together kill it. This is `(3.2)`.

**Depression.** The coefficient of `z^7` in `F(\alpha z+\beta)` comes only from `t^8` and `6t^7`:

```text
[z^7]F(\alpha z+\beta)=\alpha^7(8\beta+6).
```

Then `[z^7]f=c^2\alpha^7(8\beta+6)=\alpha^{-1}(8\beta+6)`. Depression forces `8\beta+6=0`, hence the unique translation `\beta=-3/4`. This is `(3.3)`. Consistency on `g`: `[z^{11}]G(\alpha z+\beta)=\alpha^{11}(12\beta+9)` and `[z^{11}]g=\alpha^{-1}(12\beta+9)=0` at the same `\beta`. The Hall `t^{11}` coefficient `9` is exactly `12\cdot(3/4)`.

**Translated coefficients.** With `c=\alpha^{-4}` and `\beta=-3/4`,

```text
[z^6]F(\alpha z+\beta)=\alpha^6\bigl(28\beta^2+42\beta+21\bigr),
[z^5]F(\alpha z+\beta)=\alpha^5\bigl(56\beta^3+126\beta^2+126\beta+50\bigr),
```

coming from `t^8,6t^7,21t^6` for the first line and from those plus `50t^5` for the second. Scaling by `c^2=\alpha^{-8}`:

```text
[z^6]f=\alpha^{-2}(28\beta^2+42\beta+21),
[z^5]f=\alpha^{-3}(56\beta^3+126\beta^2+126\beta+50).
```

Substitute `\beta=-3/4`:

```text
28(9/16)+42(-3/4)+21 = 63/4 - 63/2 + 21 = (63-126+84)/4 = 21/4,
56(-27/64)+126(9/16)+126(-3/4)+50
  = -189/8 + 567/8 - 756/8 + 400/8 = 22/8 = 11/4.
```

Thus `[z^6]f=(21/4)\alpha^{-2}` and `[z^5]f=(11/4)\alpha^{-3}`. Both rational constants are nonzero in characteristic zero. Both left-hand sides lie in `M` because `f\in M[z]`. Hence `\alpha^{-2},\alpha^{-3}\in M`, and their quotient is `\alpha^{-1}\in M`, hence `\alpha\in M`. No affine parameter remains only over `Mbar`. (If `21/4` or `11/4` vanished, descent of one of `\alpha^{-2},\alpha^{-3}` would fail; neither does.)

**Leading coefficient of `W`.** From Attack 1, `[t^5]H=-27`. Translation does not change a leading coefficient, so `H(\alpha z-3/4)=-27\alpha^5 z^5+O(z^4)`. Scaling by `c^6=\alpha^{-24}`:

```text
f^3-g^2 = \alpha^{-24} H(\alpha z-3/4) = -27 \alpha^{-19} z^5 + O(z^4),
W=g^2-f^3 = 27 \alpha^{-19} z^5 + O(z^4).
```

The exponent is `-24+5=-19`, independently of every lower Hall coefficient. Comparison with `[z^5]W=-2 r_7` gives the exact identity

```text
r_7=-(27/2)\alpha^{-19}.
```

The constant `-27/2` is nonzero in characteristic zero. Since `\alpha\in M^*`,

```text
div_C(r_7)=-19\,div_C(\alpha).
```

Every zero and pole *order* of `r_7` on `C` is an integer multiple of nineteen. (The constant `-27/2` has divisor zero; the sign of `r_7` is irrelevant to `(3.7)`, but the exact constant is nevertheless the one displayed.)

Attacks that failed: a residual cube root of unity in `c\alpha^4` (the equation `x^2=x^3=1` has only the solution `1` in characteristic zero); a second translation making `g` depressed at a different `\beta` (the Hall `t^{11}` coefficient forces the same value); descent from a single coefficient `\alpha^{-2}` (that would leave a possible quadratic ambiguity; the second coefficient `\alpha^{-3}` kills it); `\alpha` remaining in a proper extension of `M` (the quotient `\alpha^{-3}/\alpha^{-2}` lies in `M`); a vanishing of `21/4` or `11/4`; using `[t^5]H=-27/4` instead of `-27`.

---

## Attack 4 — divisor audit on the smooth normalization of `u^4=h`

**CONFIRMED.** Number of places, local orders, inertia at `m<4`, orders `3,1,1`, nonzero residue at `m=4`, pole order and total pole degree for `m>4`, unramified finite zeros of order one, all four infinite places, transitivity, existence of a zero, order `U-1`, and degree balance survive. Nonzero integration constants on different sheets, and residue cancellation between branches, are not loopholes.

Work on the smooth projective model of `u^4=h`. The terminal equation is the equality of meromorphic differentials `dr_7=(j/8)\,dx/u` on that model. The charged local form at infinity, derived independently below, excludes `U=1` by a nonzero residue on every sheet. Assume `U\ge 2`.

**Local data at a finite root.** Let `a` be a root of multiplicity `m`, put `d=\gcd(4,m)`, and write `h=(x-a)^m c(x)` with `c(a)\neq 0`. The Kummer extension of `L((x-a))` has ramification index `E=4/d` and `d` geometric places (degree formula `d\cdot E=4`, residue degree one after the licensed roots of unity). A uniformizer `\tau` may be chosen so that `x-a=\tau^{4/d}` and, after Hensel on the unit `c(a+\tau^{4/d})`, `u=\tau^{m/d}\varepsilon(\tau)` with `\varepsilon(0)\neq 0`. Then `dx=(4/d)\tau^{4/d-1}d\tau` and

```text
ord_P(dx/u)=(4-m)/d-1
```

at every place `P` over `a`. This is `(4.2)`. Independently, for each small `m`:

| `m` | `d` | places | `E` | `ord(dx/u)` | shape |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 4 | `2` | zero of order two |
| 2 | 2 | 2 | 2 | `0` | regular, ramified |
| 3 | 1 | 1 | 4 | `0` | regular, totally ramified |
| 4 | 4 | 4 | 1 | `-1` | unramified simple pole |
| 5 | 1 | 1 | 4 | `-2` | pole |
| 6 | 2 | 2 | 2 | `-2` | pole |
| `\ge 5` | `d\mid(4-m)` | `d` | `4/d` | `\le -2` | pole of order `\ge 2` |

**4.1. Small roots, inertia, orders `3,1,1`.** For `m<4` the ramification index is `4`, `2`, or `4`, so inertia is nontrivial. The charged character computation (recalled, not imported as a verdict): a Kummer generator sending `u\mapsto\zeta u` sends `z\mapsto\zeta z` and `w\mapsto\zeta w`, and the tail series is invariant, so `\sigma(r_ℓ)=\zeta^ℓ r_ℓ`. For `ℓ=7` and `\zeta^e=1` with `e\mid 8` one has `\zeta^7=\zeta^{-1}`. Thus inertia acts on `r_7` by a nontrivial character: the full group for `m=1,3`, and the subgroup `{1,-1}` for `m=2` (restriction of `\zeta\mapsto\zeta^{-1}` to `\zeta^2=-1` is still `-1`). In each case the residue-field extension degree is `1`, so inertia acts trivially on the residue field.

Regularity first. For `m\le 3`, `ord(dx/u)\ge 0`, so `dr_7` is holomorphic at `P`. A pole of `r_7` of order `k\ge 1` would produce a pole of `dr_7` of order `k+1\ge 2` (characteristic zero: `d(\tau^{-k})=-k\tau^{-k-1}d\tau` with `k\neq 0`). Hence `r_7` is regular at `P`.

Value zero next. If the regular value `r_7(P)` were nonzero, `r_7` would be a unit at `P`. Reduction of `\sigma(r_7)=\zeta^{-1} r_7` would then give `r_7(P)=\zeta^{-1} r_7(P)` with `\zeta^{-1}\neq 1` (or `=-1` at `m=2`), so `r_7(P)=0` in characteristic not `2`, a contradiction. Therefore `r_7(P)=0` and `ord_P(r_7)\ge 1`.

Integration last. If `ord_P(r_7)=k\neq 0` then `ord(dr_7)=k-1`. Combined with `(4.2)`:

```text
ord_P(r_7)=(4-m)/d = 3,1,1    for m=1,2,3.
```

None is divisible by nineteen, contradicting `(3.7)`. Thus `h` has no root of multiplicity below four.

(The same orders follow from the global shape `r_7=u^3 A` with `A\in L(x)`, which is the inverse-character line in the charged terminal theorem: `ord_P(r_7)=3m/d+(4/d)v_a(A)`, and matching `(4.2)` forces `v_a(A)=1-m`, hence the same `3,1,1`. Inertia on the value is the target's route; both close the unit case that a holomorphic `dr_7` would otherwise permit.)

**4.2. Multiplicity four, nonzero residue, no cancellation.** For `m=4` one has `d=4`, `E=1`, four unramified places, and `x-a=\tau`, `u=\tau\varepsilon`. Then `dx/u=\varepsilon^{-1}\tau^{-1}d\tau`, residue `\varepsilon(0)^{-1}` with `\varepsilon(0)^4=c(a)\neq 0`. Times `j/8\neq 0`, the form `(j/8)dx/u` has a simple pole of nonzero residue at each of the four places. Residues of exact differentials vanish place by place: if `r_7=\sum a_k\tau^k` locally, the coefficient of `\tau^{-1}d\tau` in `dr_7` is zero. Hence multiplicity four is impossible.

Cancellation between the four sheets is not a loophole. The four residues are the inverses of the four fourth roots of `c(a)`, which sum to zero, so the global residue theorem is satisfied. Exactness is a local condition at each place and already fails at any one of them. Pushforward to `\mathbb{P}^1_x` can cancel; that is not exactness on `C`.

**4.3. Large roots, pole degree `m-4`, no unramified finite zeros.** For `m>4`, `d` divides `4-m`, so `(4-m)/d` is a negative integer `\le -1` and `ord(dx/u)\le -2`. A pole of `r_7` of order `k\ge 1` has `ord(dr_7)=k-1`, hence

```text
-ord_P(r_7)=(m-4)/d.
```

In particular nineteen divides `(m-4)/d`. There are `d` places over `a`, so this root contributes total pole degree `d\cdot(m-4)/d=m-4`.

Off the roots of `h`, the cover is unramified (`v(h)=0` gives ramification index `4/\gcd(4,0)=1`) and `u` is a unit. At such a place `x-x(P)` is a uniformizer, so `dx` has order zero and `ord(dx/u)=0` exactly (the form does not vanish). A pole of `r_7` would make `ord(dr_7)\le -2`, contradicting order zero. A zero of `r_7` of order `k\ge 1` would make `ord(dr_7)=k-1=0`, hence `k=1`. Order one is not divisible by nineteen. Therefore `r_7` has no finite zeros, and its finite poles are exactly those of `(4.4)`.

**4.4. Infinity: four places, transitivity, a zero, order `U-1`.** Because `h` is monic of degree `4U`, `v_\infty(h)=-4U` and the ramification index is `4/\gcd(4,4U)=1`. Four unramified places, `q=1/x` a uniformizer at each. On a selected sheet `t=q^U u` satisfies `t^4=q^{4U}h(q^{-1})=1+O(q)`, a unit; the fibre `T^4-1=0` is separable in characteristic zero, so Hensel lifts four branches. The deck group permutes them transitively by `t\mapsto\zeta t`. Then `dx=-q^{-2}dq` and `u=q^{-U}t`, so

```text
dx/u=-q^{U-2}t^{-1}dq,     dr_7=-(j/8)q^{U-2}t^{-1}dq.
```

The coefficient `t^{-1}` is a unit on every sheet (`t(0)^4=1`). The order at each infinite place is exactly `U-2`. For `U=1` this is a simple pole of residue `-(j/8)t(0)^{-1}\neq 0` on every sheet; exactness fails sheetwise, and summing the four residues (the negatives of the four fourth roots of unity, times `j/8`) is the global residue theorem, not exactness. For `U\ge 2` the form is regular at infinity, so `r_7` is regular at infinity: a pole of order `k\ge 1` would produce a pole of `dr_7` of order `k+1\ge 2`.

`r_7` is nonconstant by `(4.1)`. A nonconstant rational function on a complete smooth curve has a zero (otherwise it would have no pole either, hence be a global regular function, hence constant). No zero is finite, so a zero occurs at some place above infinity.

Galois spreading: `\sigma(r_7)=\zeta^{-1} r_7` with `\zeta^{-1}` a unit, so `r_7` vanishes at `P` if and only if it vanishes at `\sigma^{-1}P`. Transitivity forces zeros at all four infinite places, of equal order.

Value zero plus `ord(dr_7)=U-2` forces `ord_P(r_7)=U-1` at every infinite place: if the order were `k\neq 0` then `k-1=U-2`. (The unit case `k=0` is already excluded by the existence of a zero together with Galois.) Then nineteen divides `U-1`, and the total zero degree is `4(U-1)`.

**Loophole: nonzero integration constants on different sheets.** Local integration of `(4.6)` produces a primitive of order `U-1` plus a constant of integration on each sheet. For `U=2` the form is holomorphic and nonvanishing, so a local primitive may have a nonzero value. That is not a loophole for a *global* function `r_7\in M`. The four local expansions are Galois conjugates of one element of the function field. An extra constant of the function field is an element of `L` after the licensed enlargement, and scalars have trivial character, not inverse character; the charged uniqueness of `A` in `r_7=u^3 A` already kills an uncharged constant. Independently, the global argument never uses local vanishing of a chosen primitive: it uses existence of some zero of a nonconstant function on a complete curve, absence of finite zeros, and Galois. The constant of integration is thereby forced to vanish at every infinite place, after which the order is `U-1`.

**Loophole: residue cancellation.** Treated in 4.2. Exactness is local. The same applies to a hypothetical simple pole at one infinite place: `U=1` is already impossible on each sheet separately.

**Degree balance.** Sections 4.1 and 4.2 force every remaining root multiplicity `m_i` to be strictly greater than four. Let `N` be the number of distinct finite roots. The total pole degree is `\sum_i(m_i-4)=4U-4N`. The total zero degree is `4(U-1)=4U-4`. Degree zero of a principal divisor gives `N=1`. Then `h=(x-a)^{4U}=((x-a)^U)^4`, whose class in `L(x)^*/L(x)^{*4}` is trivial, contradicting exact order four.

A configuration of several large roots, even 19-compatible ones (for instance a root of multiplicity `23`, where `(m-4)/d=19`), still has total pole degree `4U-4N`. Equality with `4U-4` forces `N=1` regardless of nineteen. The 19-divisibility is used to kill small-root zeros of orders `3,1,1` and unramified finite zeros of order one, so that every zero is at infinity and the count applies. It is not needed for the last sentence, which is the Kummer class.

Together with the `U=1` residue obstruction, this is the theorem for every `U\ge 1`.

Attacks that failed: a missed place above a root (the count is `d`, not `4`); inertia of order two at `m=2` acting trivially on `r_7` (it acts by `-1`); a holomorphic `dr_7` licensing a nonzero value at `m=1` without inertia (the character forbids it); residue `0` at `m=4` on some sheet (`\varepsilon(0)^4=c(a)\neq 0`); cancellation of the four residues licensing a simple pole; an unramified finite zero of order `19` (`ord(dx/u)=0` forces order exactly one); a hidden pole of `dx/u` at a non-root ( `u` is a unit and `dx` has order zero); a missed fifth infinite place; non-transitive Galois action at infinity (the four units `t(0)` are the four fourth roots of unity); local primitives with sheetwise constants producing a function with no zero (incompatible with being one element of `M`, and with inverse character); `N>1` after all small zeros are killed.

---

## Attack 5 — order-two `U=2,[6,2]` corollary, only on the all-zero-load sub-stratum

**CONFIRMED.** The identities `T^2=(x-1)/x`, `r_7=(j/4)T`, and `div(T)=[0]-[\infty]` hold on the stated closed sub-stratum. Nonzero loads lie outside the DS argument.

Charge the source-typed client `h=x^6(x-1)^2`, `u^2=x^3(x-1)`, `T=u/x^2`. Directly:

```text
T^2=u^2/x^4=x^3(x-1)/x^4=(x-1)/x.
```

The charged terminal primitive at `(a,b)=(0,1)` is `r_7=j T/(4(b-a))=(j/4)T`. Restrict to the closed sub-stratum

```text
k_{10}=k_6=k_2=0,     mu_2=mu_4=mu_6=0.
```

Then `g=F_{12}(f)` and `r_1=\cdots=r_6=0`, so Attacks 2 and 3 apply verbatim over this quadratic function field: the unique order-four Hall orbit over `Mbar`, monicity, depression, and the two Hall coefficients again force `r_7=-(27/2)\alpha^{-19}` with `\alpha\in M^*`. Every divisor order of `r_7` is divisible by nineteen.

The normalization is the rational `T`-line: `x=1/(1-T^2)`, `u=T/(1-T^2)^2`, deck involution `T\mapsto -T`. On `\mathbb{P}^1_T` the function `T` has a simple zero at `T=0` and a simple pole at `T=\infty`, so `div(T)=[T=0]-[T=\infty]`. Independently on the cover: at `x=1`, `T^2\sim(x-1)` and `T` is a uniformizer (simple zero); at `x=0`, `x=\sigma^2`, `ord(u)=3`, `ord(T)=3-4=-1` (simple pole); at both infinite places `T^2=(x-1)/x\to 1`, so `T\to\pm 1` is a unit. Since `j/4\in L^*`,

```text
div_C(r_7)=div_C(T)=[T=0]-[T=\infty].
```

Both orders are one, contradicting divisibility by nineteen. The sub-stratum `(6.2)` is empty.

This does not eliminate the source-typed order-two client. Any of `k_{10},k_6,k_2,mu_2,mu_4,mu_6` nonzero makes `g` fail to equal `F_{12}(f)` or makes some `r_ℓ` for `ℓ\le 6` fail to vanish, so `deg_z(g^2-f^3)` need not be five and the unique order-four DS classification does not apply. In particular `mu_4\neq 0` on this quadratic client is the degree-eight lane of Attack 2, not a DS equality.

Attacks that failed: `div(T)` picking up the two infinite places ( `T` is a unit there); order of `T` at `x=0` equal to `3` rather than `-1` (forgetting to divide by `x^2`); applying the corollary off `(6.2)`; treating `(j/4)T` as having a zero of order nineteen because `j` might vanish (`j\in L^*`).

---

## Attack 6 — firewall

**CONFIRMED.** The target does not smuggle a closure of anything outside the two named empty loci.

A confirmation of Attacks 1–5 eliminates exactly:

- the whole order-four `mu_4=0` terminal stratum, for every monic core degree `4U`;
- the named closed order-two zero-load sub-stratum `(6.2)` of the concrete `U=2,[6,2]` client.

It does not eliminate, and the target does not claim to eliminate:

- `mu_4\neq 0`, where `deg_z(g^2-f^3)=8` and DS equality is unavailable;
- the remainder of the genuine order-two leaf, on which at least one of `k_{10},k_6,k_2,mu_2,mu_4,mu_6` is nonzero;
- the order-one leaf;
- bounded sectors, the full `(8,12)` cell, maximum twelve, a counterexample, or JC2.

The argument is orthogonal to the common-quartic Rees lane: it uses the generic finite polynomial `z`-degree of `g^2-f^3`, uniqueness of the order-four equality case, descent of the affine parameter, and the terminal differential divisor. It requires no saturation and no Taylor realization. The target's §7 matches this boundary. No creep was found in the theorem statement, in the order-two corollary, or in the firewall paragraph.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Shioda essential equivalence is `(1.1)`; Hall `m=4` polynomials and the sign of `H` match the official PDF; `St(4)=1`; Theorem 5.1 is uniqueness of that orbit over `C`; the unique-orbit statement is first-order of finite type over `Q` and transfers to `Mbar` | **CONFIRMED** | a mismatch with the PDF; `St(4)\neq 1`; an extra essential class over `C`; Lefschetz applied to an unbounded-degree or topological sentence; an extra `Mbar`-orbit of finite type |
| 2 | Under the charged tail convention, `g=F_{12}(f)` and `r_1=\cdots=r_6=0` give `W=-2r_7 z^5+O(z^4)` with `[z^5]W=-2r_7\neq 0`; Davenport over `M` makes this an order-four DS triple; `mu_4\neq 0` is degree eight and is not this lane | **CONFIRMED** | opposite tail sign; a vanishing `z^5` coefficient; Davenport failing over a characteristic-zero function field; `mu_4\neq 0` still forcing `deg W=5` |
| 3 | Monicity gives `c=\alpha^{-4}`; depression gives `\beta=-3/4`; translated Hall coefficients are `21/4` and `11/4`; both descend `\alpha` to `M`; `[z^5]W=27\alpha^{-19}`; `r_7=-(27/2)\alpha^{-19}` and `div(r_7)=-19\,div(\alpha)` | **CONFIRMED** | a second solution of `\gamma^2=\gamma^3=1`; a different `\beta` depressing `g` but not `f`; `21/4=0` or `11/4=0`; leading of Hall `H` not `-27`; `\alpha` remaining only in `Mbar` |
| 4 | Local orders `(4-m)/d-1`; inertia forces `r_7(P)=0` for `m<4` with resulting orders `3,1,1`; nonzero residue at each of four places for `m=4`; pole order `(m-4)/d` and total pole degree `m-4` for `m>4`; unramified finite zeros of order one; four unramified infinite places, transitivity, a zero, order `U-1`; degree balance forces `N=1` and a fourth-power core | **CONFIRMED** | a wrong ramification index; a regular nonzero value at a ramified place; residue `0` at `m=4`; branch-cancellation licensing a simple pole; an unramified finite zero of order `19`; a sheetwise integration constant producing a function with no zero; `N>1` after small zeros are killed |
| 5 | On `(6.2)` only: `T^2=(x-1)/x`, `r_7=(j/4)T`, `div(T)=[0]-[\infty]`, orders `\pm 1`, contradiction with `(3.6)`; nonzero loads are outside the DS argument | **CONFIRMED** | a zero or pole of `T` of order divisible by nineteen; the corollary applied off `(6.2)`; `j=0` |
| 6 | Confirmation eliminates only the whole order-four `mu_4=0` terminal stratum and the named order-two zero-load sub-stratum; not `mu_4\neq 0`, not the remaining order-two client, not the order-one leaf, not `(8,12)`, not maximum twelve, not JC2 | **CONFIRMED** | a hidden promotion in §0, §6, or §7 |

---

## Remarks (non-blocking)

1. Shioda does not number the Hall display as “Example 5.1”. The polynomials, the sign, and Theorem 5.1 are the load-bearing objects and match. Not a numbered failure.
2. The `O(z^4)` in `(2.2)` is an equality of polynomials in `z`. As functions of `w` one has `w^5=z^5+O(z^3)`, which is absorbed into the lower-degree part of a degree-five polynomial. The leading identity `(2.3)` does not use a `z^4` term in `w^5`.
3. The exact constant `-27/2` is not needed for `(3.7)` beyond being a nonzero scalar of `L`. It is nevertheless the correct constant, and the order-two corollary uses only the exponent `19`.
4. Characteristic zero is essential and present: `8\neq 0`, `2\neq 0` in the Hall halves, `11\neq 0`, `19\neq 0`, `4T^3\neq 0` in Hensel at infinity, and `d(\tau^{-k})` does not drop order. The theorem's opening sentence supplies it.
5. Genus of `C` is not used. The holomorphic-exact argument of the charged terminal theorem, which already kills all-multiplicities-at-most-three for `U\ge 2`, is stronger than needed here: nineteen kills those zeros even without holomorphy of `dx/u`. The two obstructions are compatible.
6. The coefficient-infinity review's `REPAIR` of `(7.2)` is orthogonal. The present theorem never evaluates a Faber polynomial `F_j(K^2)` along a load direction.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms emptiness of the order-four `mu_4=0` terminal stratum for every monic core degree `4U`, and emptiness of the closed order-two `U=2,[6,2]` sub-stratum on which every lower Faber load and every lower tail load vanishes. It does **not**:

- eliminate `mu_4\neq 0`, where `deg_z(g^2-f^3)=8`;
- eliminate the remainder of the genuine order-two client, on which at least one of `k_{10},k_6,k_2,mu_2,mu_4,mu_6` is nonzero;
- close the order-one leaf, the bounded-pole sector, the strict Rees fibre, either original Taylor-boundary family, or the cell `(8,12)`;
- bound maximum twelve, produce or exclude a counterexample, or speak to JC2;
- replace the charged tail convention, the terminal row `8r_7'=j/u`, or the inverse-character line by a new derivation from a Keller pair (those are source-typing identities, re-used as formulae);
- consume Stothers 1981, Hall 1971, or Shioda §8 as uniqueness (uniqueness is Shioda Theorem 5.1 plus `(4)`, transferred by `ACF_0`).

The target's own firewall matches this boundary. No creep was found.

---

## Terminal boundary (accepted, not enlarged)

```text
shioda_essential_equivalence_and_hall_m4=PROVED
St(4)=1_unique_orbit_over_C=PROVED
ACF0_Lefschetz_transfer_to_Mbar=PROVED
W=-2_r7_z^5_order_four_DS_triple=PROVED
mu4_nonzero_degree_eight=SEPARATE
c=alpha^{-4}_beta=-3/4_Hall_21/4_11/4=PROVED
alpha_descends_to_M=PROVED
r7=-(27/2)alpha^{-19}_orders_divisible_by_19=PROVED
finite_orders_3_1_1_and_m=4_residue=PROVED
large_root_pole_degree_m-4=PROVED
unramified_finite_zero_order_one=PROVED
infinity_four_places_order_U-1=PROVED
degree_balance_N=1_fourth_power=PROVED
sheetwise_constants_and_residue_cancellation=NOT_LOOPHOLES
order_two_U=2_[6,2]_zero_load_substratum=EMPTY
mu4_nonzero=NOT_ELIMINATED
remaining_order_two_client=NOT_ELIMINATED
order_one_leaf=NOT_ELIMINATED
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```

---

## Model identity and evidence boundary

Reviewer: Grok 4.6, released by xAI. Independent hostile rederivation. Every charged review was opened only because target §1 names it; its verdict string was not used. No prior stdout, no CAS, no solver, and no Python reconstruction was used as evidence. The load-bearing chain is Shioda §5 essential equivalence and the printed Hall triple, Stothers' `St(4)=1` as recorded by Shioda Theorem 5.1, first-order transfer of a finite-type orbit to `Mbar`, the charged ordinary-tail expansion of `g^2-f^3`, Davenport's bound over a characteristic-zero field as Shioda Lemma 3.1, monic/depressed normalisation with binomial coefficients `21/4` and `11/4`, descent of `\alpha` from two nonzero elements of `M`, the exponent `-19` in `c^6\alpha^{5}`, inverse-character inertia at ramified places, sheetwise residues of exact differentials, and degree zero of a principal divisor on the smooth projective model of `u^4=h`.

CONFIRMED
