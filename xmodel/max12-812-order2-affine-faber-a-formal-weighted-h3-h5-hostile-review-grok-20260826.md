# Hostile review — affine-Faber `A` center-complete formal weighted `H3/H5` direct unit

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_affine_faber_a_formal_weighted_h3_h5_identity_20260826/` |
| Charged freeze | `FREEZE.sha256` = `0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5` |
| Charged evidence | `EVIDENCE.sha256` = `86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48` |
| Charged result | `RESULT.md` = `5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d` |
| Charged results | `RESULTS.sha256` = `1946cec19e71fcce5b7a38a68125362a158bb589c61347b196d36bb6cdc62fbf` |
| Charged q6 review | `xmodel/max12-812-order2-affine-faber-a-loaded-kernel-q6-hostile-review-grok-20260826.md` = `06e2709344b47ec09549638a53f193b79ca4f791d40c2c0b9c8c04e0284330be` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing valuation face | none inside the claimed chart; the two-sided source-to-chart lemma is a remaining composition gate, not a false monomial |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. No producer status line, no `PASS`/`UNIT`/`ENDPOINT` token, and no validator string is evidence |
| Method | SHA-256 of every charged pin and every freeze/evidence/results row; independent reconstruction of all seven frozen ordinary-Faber tails; hand depression of `Q` and `N`; independent Laurent-to-Faber matrix from `Q^{1/4}` and its inverse; exact-`Q` Singular replay that prints the reduced polynomials, not control bits; explicit series/ramification/jet substitutions. Characteristic 65521 was not used as characteristic-zero algebra |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the five files named in the review
prompt match those pins. Independently recomputed SHA-256 of every freeze,
evidence, and results row match the corresponding manifest. Producer
verdict language, `A_FWH35_UNIT`, `A_FWH35_ENDPOINT`,
`PASS_FORMAL_WEIGHTED_CENTER_COMPLETE_DIRECT_UNIT`, and both validator
`PASS_*` strings were not used as characteristic-zero evidence. Exact `Q`
is the mathematical lane: the reduced polynomials `H3`, `H5`, and
`K=E*H3+H5` modulo `t^46`. No file other than this review was written.
`jc2-lean` and shared ledgers were not touched.

---

## Verdict

**CONFIRMED.**

On the weighted moving-discriminant chart with independent polynomial
symbols

```text
a, E, M, X, Y, R1, R0, S1, S0, lam, K10t, K6t, K2t, mu2t
```

and weights `a:5`, `X:Y:6`, `R:S:12`, `lam:15`, loads/target `42`,
`E:M:0`, the seven frozen complete ordinary-Faber tails, after the exact
depressed substitutions for

```text
Q = A^2(A^2+4aA+E) + (X+R1)A + R0,
N = lambda*(M A(A^2+4aA+E) + Y A + M X/2 + S1 A + S0),
```

satisfy the inverse-Faber identities

```text
H3 = -(3/8) t^42 lam^2 M X Y - (1/16) t^45 lam^3 M^3    mod t^46,
H5 =  (3/8) t^42 E lam^2 M X Y                           mod t^46.
```

Consequently `K=E*H3+H5` has no term of `t`-degree less than 45, and

```text
[t^45] K = -E lam^3 M^3 / 16.
```

This is a polynomial identity in every displayed symbol. Substituting
arbitrary formal or ramified power series for those symbols preserves it.
That includes the omitted integral jet `a6` of the earlier `q=6` REPAIR,
every later center/tangent/complement/kernel jet that can meet weight 45
after the stated leading valuations, every rational first kernel order
`q>=6` after common ramification, and every higher-kernel monomial present
in the complete tails. Loads, the `mu2` target, both complementary series,
and the moving center cancel in `H3` and `H5` through grade 45. No
predecessor source equation is used.

The identity does not prove that every raw delayed-load source arc enters
this chart. The remaining theorem gate is the two-sided
moving-discriminant / K2 / Rees-coordinate lemma stated in §5. The
separate `q<6` homogeneous face, `m=0`, other load slopes, terminal/Taylor
receivers, total fan, order two, maximum twelve, and JC2 are outside the
claim.

**CONFIRMED**

---

## Hashes and charged artifacts

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../FREEZE.sha256` | `0ef7cfc84691c5fa466e98cf76f942d6bcd217547d0eb91b0f3860240da8eae5` | freeze manifest (matches required pin) |
| `.../EVIDENCE.sha256` | `86883cc16a48e0ee4b4a1ea01844cedbdd212eb41414fe918f641d6654582f48` | evidence manifest (matches required pin) |
| `.../RESULT.md` | `5736a3b00ec6e1b74b43c5112b8fadccf340b98558854b63ddd6ca9042d8370d` | producer result (matches required pin) |
| `.../RESULTS.sha256` | `1946cec19e71fcce5b7a38a68125362a158bb589c61347b196d36bb6cdc62fbf` | results manifest (matches required pin) |
| q6 hostile review | `06e2709344b47ec09549638a53f193b79ca4f791d40c2c0b9c8c04e0284330be` | truncation defect being repaired (matches required pin) |
| `.../REGISTRATION.md` | `e47cd54dcf2a88c37fbb6239f11f56f04666188527edeb532a4809c9dac64fd6` | registered identity and scope |
| `.../compile_formal_weighted_h3_h5.py` | `cbd6aa79849242bdb39ddad42dce3587e8aa83d71fafde331cc4a015de85b338` | formal-weighted compiler |
| `.../run_aws.sh` | `adada638ebb870206fce0c7d26fb20f856e6acc17e6f865868e5d5b209f2e555` | freeze pin |
| `.../launch_host.sh` | `5ca346251d83c502e659f3be519fbef28004d20e467289d53db796366e29756e` | freeze pin |
| loaded-kernel compiler | `a32372ce3fd088be74a3456f63c17bcb880c2eaf32c1856e86eb52d7b15f385a` | tail renderer import |
| mixed sigma-45 compiler | `c19badfcfad44842f42118d031a5bfe92729d714e2a329b2af7097be629ea3d9` | frozen `tail_text` |
| `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | complete frozen ordinary-Faber tails |
| canonical `tails.json` | `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8` | matches parent `EXPECTED_CANONICAL` |
| V2 direct-unit addendum | `78766c9df5dbf95fad5bdff531657f58cb7445e30575a58a59cec656b00d9a63` | claimed raw congruences |
| exact-`Q` `.sing` | `6924447099ddd5af7b06473262ee9404ffb16fce7968b74ca0c62ab0483a04f3` | compiled source |
| exact-`Q` stdout | `4fa84c7587556d43f9441ac68bfbb6c6f7577a39ea9e58e6e1fef91d61233af8` | printed only after independent replay |
| exact-`Q` validation | `5c237b6776d7bf90e3853ed1c816172c60f6258bb272467f368970683c65e9ce` | custody, not algebra |
| exact-`Q` compiler stderr | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | empty file |

Every hash above matches the corresponding freeze, evidence, or results
row, or is an auxiliary reconstruction check. Characteristic-65521 stdout
hash `61e108b59227dfa40de6da32455aef3e3e08d548c011c5e23c42559640b7d867`
appears in `RESULTS.sha256` and was opened only to confirm it is a
software control: it prints `K45=4095*lam^3*M^3*E` with
`4095 ≡ -1/16 (mod 65521)`. That lane is not characteristic-zero evidence.

Independent re-emission of the compiler body, using the pinned
`tail_text` and the pinned tails, byte-matches the frozen exact-`Q` `.sing`.
The F65521 `.sing` differs only by the ring characteristic.

---

## 1. Seven frozen tails and the exact `Q`/`N` substitutions

The formal-weighted compiler pins the loaded-kernel compiler, which pins
`compile_sigma45.py` at
`c19badfcfad44842f42118d031a5bfe92729d714e2a329b2af7097be629ea3d9`.
That renderer expands each tail on the ordinary-Faber monomials

```text
(qr^2+n0, 2*qc*qr+n1, qc^2+2*qp*qr+n2, 2*qp*qc+n3,
 qp^2+2*qr, 2*qc, 2*qp, k10, k6, k2).
```

Independent reconstruction of all seven strings matches both compiled
sources. Counts: `T1` 36 monomials, `T2` 54, `T3` 58, `T4` 81, `T5` 89,
`T6` 120, `T7` 131. After substitution, none of `P1,...,P7` retains a
Faber generator. Rows six and seven are rebuilt and fully substituted;
the inverse-Faber identities through `H5` consume only `P1,...,P5`, which
is the correct truncation of the connection, not a tail truncation.

Put `A=z-a` and expand the claimed chart polynomials in `z`.

```text
Q = A^4 + 4a A^3 + E A^2 + (X+R1) A + R0.
```

The `z^3` coefficient cancels, so the form is depressed. The remaining
coefficients are

```text
QP = E - 6 a^2,
QC = 2a(4a^2 - E) + X + R1,
QR = a^2(E - 3 a^2) + R0 - a(X+R1).
```

These are exactly the compiled substitutions with `aa=t^5 a`,
`XX=t^6 X`, `RR1=t^{12} R1`, `RR0=t^{12} R0`.

For the cubic,

```text
N/lambda = M A^3 + 4a M A^2 + (E M + Y + S1) A + M X/2 + S0
```

the `z`-coefficients are

```text
N3 = lambda M,
N2 = lambda a M,
N1 = lambda*((E-5a^2) M + Y + S1),
N0 = lambda*(-a(E-3a^2) M - a Y + M X/2 + S0 - a S1).
```

These match the compiled `N3,N2,N1,N0` with `NL=t^{15} lam` and
`YY=t^6 Y`, `SS*=t^{12} S*`. Equivalence with the loaded-kernel writer
`DD-2 aa^2 = E-5 a^2` is exact. No predecessor equation is substituted.
Loads and the target are independent leading symbols of weight 42,
not locked to the affine-Faber point `(15/32)p^2`, `(15/256)p^4`.

---

## 2. Inverse-Faber connection, and the identities modulo `t^46`

Let `B=4a` and let `Q_0=z^4+B z^3+E z^2` be the unperturbed double-root
principal part. Write `w=Q_0^{1/4}`, invert to a series `z(w)`, and
expand `z^{-j}` in powers of `w^{-1}`. The resulting lower-unitriangular
Laurent-to-Faber matrix, independently derived, is

```text
P1 = H1,
P2 = (B/4) H1 + H2,
P3 = (-B^2/32 + E/4) H1 + (B/2) H2 + H3,
P4 = (E/2) H2 + (3B/4) H3 + H4,
P5 = (7 B^4/2048 - 3 B^2 E/128 + E^2/32) H1
     + (-B^3/64 + B E/8) H2
     + (3 B^2/32 + 3 E/4) H3
     + B H4 + H5.
```

It coincides with the frozen connection used by the half-weight and
formal-weighted compilers. The inverse through rows three and five is
unique for a unitriangular matrix, and the claimed combinations

```text
H3 = P3 - (B/2) P2 + (5 B^2/32 - E/4) P1,
H5 = P5 - B P4 + (21 B^2/32 - 3E/4) P3
     + (-5 B^3/16 + 3 B E/4) P2
     + (195 B^4/2048 - 45 B^2 E/128 + 5 E^2/32) P1
```

satisfy `H3`-row times the forward matrix `= e_3` and `H5`-row times the
forward matrix `= e_5` as polynomials in `B,E`. Those are the compiled
rows, with `BB=4 t^5 a` and `EE=E`.

An independent exact-`Q` Singular replay, built from the reconstructed
tails rather than from the producer control bits, prints the reduced
polynomials

```text
H3 ≡ - (1/16) lam^3 M^3 t^45 - (3/8) Y X lam^2 M t^42    mod t^46,
H5 ≡   (3/8) Y X lam^2 M E t^42                           mod t^46,
K  ≡ - (1/16) lam^3 M^3 E t^45                            mod t^46.
```

Signs, `t`-powers, and the convolution `M X Y` versus the cubic `M^3`
all match the claim. The `MXY` series cancels in `K` before coefficient
extraction. No term of `K` below grade 45 survives, and

```text
[t^45] K = - E lam^3 M^3 / 16.
```

On the slice `a=X=Y=R=S=loads=mu2=0` one has `QC=QR=N2=N0=0`,
`N3=t^{15} lam M`, and the unique cubic monomial of `T3` is
`-1/16 n3^3`. That slice gives

```text
P3 ≡ H3 ≡ (-1/16) N3^3 ≡ - (1/16) lam^3 M^3 t^45,
H5 ≡ 0.
```

The coefficient `-1/16` is therefore the frozen cubic face of tail three,
not an output of the solver. The `t^{42}` coefficient `-3/8 M X Y`
specializes, at `a=0` and `lam=1`, to the previously rederived integral
`q=6` identity `G3-(p/4)G1=-(3/8) m x_6 y_6`.

Loads and the target do not appear in the reduced `H3` or `H5`:

- `mu2` meets `H3` and `H5` only through `P2`, whose inverse-Faber
  multipliers have `t`-weight at least `wt(B)=5`, hence total weight at
  least 47;
- `k10,k6,k2` have weight 42 and could have entered through `P1` and
  `P3`, but the inverse-Faber combinations cancel them through grade 45,
  even with the three loads independent rather than locked.

Complements `R1,R0,S1,S0` and the center `a` likewise have vanishing
derivatives on the reduced polynomials. Second derivatives in `X` and in
`Y` vanish: no `X^2`, `Y^2`, or higher kernel power survives the window.
The printed identity uses no predecessor reduction.

---

## 3. Polynomial variables and legitimate series substitution

The congruence is membership of `H3-EXPECT3` and `H5-EXPECT5` in the
principal ideal `(t^{46})` inside a polynomial ring over `Q`. A
`Q`-algebra homomorphism that sends `t` to `t` (or to `u^e`) and sends
the other symbols to power series therefore preserves the congruence.
Negative powers of `t` in those symbols are not licensed, so the leading
valuations of the chart cannot be lowered by substitution.

Explicit exact-`Q` tests, all reducing to zero:

| Substitution | Meaning | Window |
|---|---|---|
| `a → a + t Jt` | omitted `q=6` center jet `a6`, and later center jets | `t^{46}` |
| `E → E + t Jt`, `M → M + t Jt` | discriminant and normal tangents of every order | `t^{46}` |
| `R1 → R1 + t Jt` | complementary jets of order `>12` | `t^{46}` |
| `X → t X` | first kernel order strictly larger than 6 | `t^{46}` |
| `t → t^2` | common ramification | `t^{92}` |
| compose ramification, `a6`, and `X → t X` | fractional `q>6` after ramification, with moving center | `t^{92}` |

The prefactor `XX=t^6 X` forbids `q<6`: a first kernel order five would
require a pole in `X`. Raising the valuation of `X` or `Y` after
`t=u^e` produces every rational `q>=6`. Higher-kernel monomials are not
an omitted face: they are present in the complete tails and cancel in
the inverse-Faber rows through weight 45.

This discharges the algebraic truncation named by the `q=6` hostile
review, *inside the chart*. It does not absorb an arc whose first
complementary order is strictly less than 12, whose first normal order is
strictly less than 15, or whose first center order is strictly less than
5; those are earlier Newton faces, not series substitutions in these
weights.

---

## 4. Direct unit versus chart coverage

Along a source solution every `P_ell` vanishes, hence `H3=H5=0`, hence
`K=0`. The identity then forces

```text
[t^{45}] K = - E_0 lam_0^3 M_0^3 / 16 = 0
```

on the leading coefficients of the series. That coefficient is a unit on
`D(E_0 * lam_0 * M_0)`. The localization at `K10t` does not appear in
`K45`; it is the ambient delayed-load open `D(k10)`, not a hidden factor
of the obstruction. No case split on `[t^{15}](M X Y)` is required.

This is a unit on the stated moving-discriminant chart. It is not a
proof that every raw source arc of the delayed-load repeated-root `A`
ray admits these coordinates.

The producer states that firewall in `REGISTRATION.md` and `RESULT.md`.
The identity does not silently close it.

---

## 5. Remaining two-sided coordinate / Rees gate

The remaining gate is exactly the two-sided chart lemma, not a missing
monomial of `H3` or `H5`.

Work on the delayed-load repeated-root `A` open `D(E * lam * M * k10)`.
The identity is a theorem after a coordinate change to symbols with

```text
v(a) >= 5,     v(X), v(Y) >= 6,     v(R*), v(S*) >= 12,
v(lambda) >= 15,    v(k10), v(k6), v(k2), v(mu2) >= 42,
```

`E` and `M` of valuation zero at the leading term, and with `Q,N`
equal to the displayed chart polynomials. Two-sidedness means a formal
(or ramified) isomorphism of DVRs onto that chart, from the raw
delayed-load source through the ordinary-Faber / first-normal square
coordinates `(qp,qc,qr,n_i,k_{10},k_6,k_2)`, that neither drops arcs nor
adds extra solutions.

No such lemma is supplied here, and none is claimed. Arcs that never
enter the chart — including every genuine `q<6` initial face, every
locus with leading `M=0`, every other load slope, and every arc whose
complementary or center valuation undershoots the weights above — are
outside the identity. Kernel-degree-three and higher terms through
weight 45 are *not* a remaining gate: they are in the complete tails and
cancel.

---

## 6. Scope firewall

`q<6` remains a separate homogeneous certificate. The identity does not
reopen the quarantined `q>15/2` sigma-45 slice as a standalone claim; on
arcs that do enter this chart, that slice is included as the special
case of high kernel valuation, in which the `MXY` series starts after
grade 42 and the cubic unit remains. This review claims none of `m=0`,
other load slopes, terminal or Taylor receivers, total fan coverage,
order two, maximum twelve, or JC2.

---

## Strongest exact theorem that survives

Work over a field of characteristic zero. In the polynomial ring on the
symbols `a,E,M,X,Y,R1,R0,S1,S0,lam,K10t,K6t,K2t,mu2t,t`, after
substituting the seven frozen complete ordinary-Faber tails along the
exact depressed chart map of §1 and forming the inverse-Faber rows of
§2, one has

```text
H3 ≡ -(3/8) t^{42} lam^2 M X Y - (1/16) t^{45} lam^3 M^3,
H5 ≡  (3/8) t^{42} E lam^2 M X Y
```

modulo `t^{46}`, as an identity of polynomials. Hence
`K=E H3+H5 ≡ -(1/16) t^{45} E lam^3 M^3` modulo `t^{46}`. The same
congruences remain true after substituting arbitrary formal power
series for the non-`t` symbols, and after any common ramification
`t=u^e`. On `D(E * lam * M * k10)` of this chart, a source solution is
therefore impossible through grade 45.

This repairs the algebraic center-truncation defect of the literal
integral `q=6` compiler, for every ramified arc that already lies on the
moving-discriminant chart with first kernel order at least six. It is
not a two-sided source-coverage theorem, not a `q<6` theorem, and not a
substitute for `m=0`, other load slopes, terminal/Taylor receivers,
total fan, order two, maximum twelve, or JC2.

CONFIRMED
