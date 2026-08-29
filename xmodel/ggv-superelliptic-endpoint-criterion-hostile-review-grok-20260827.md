# Hostile review: GGV superelliptic endpoint criterion (Opus5 Card A / §3)

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Target:** `xmodel/ideation-20260827T1349Z-opus5.md` §§0.2, 3, 4, 5 and Card A, read against the frozen R1/R2/R3 producer and hostile-review artifacts named there. The cokernel audit

```text
xmodel/ggv-8_28-M-cokernel-seven-vector-hostile-audit-sol2-20260827.md
```

was used only to keep the polynomial operator `M:Q[X]→Q[X]` distinct from the rational ODE under review.

**Claim under review (narrow):** for nonzero `H` over a characteristic-zero field, rational solutions of `2 H g' + H' g = 2 H` are equivalent to a polynomial `v` with `A = B v' + (3/2) B' v` after `H=A^2 B` and `B` squarefree; the displayed degree/denominator bound, the integrating-factor and de Rham reformulation on `w^2=H` including `[w dX]=-(4/5)[dX/w]` for `H=X^8-1`, the displayed examples, the general `(α,β,N)` endpoint formula, and the Card A firewall from that endpoint to a degree-uniform GGV exclusion. **Not** under review as a theorem, and not granted if implied: a general-`H` rational-mode classification, raw `2S/3S` provenance, polynomial source cleanup, a GGV family exclusion, `G2-PSC`, `G2-BD`, a cofinal `td` bound, or JC2.

**Method.** Rehashed the charged ideation, the R1/R2/R3 producer reports and their completed Grok reviews, and the cokernel audit. Independently derived the first-order ODE, finite-place and infinity valuations, the substitution `u=A g`, `u=B v`, and the operator `N_B`; independently expanded `E(F,t^n F^γ)` and the weight-`N` residual; independently reduced `X^k ω` on `w^2=X^8-1`; independently rebuilt a desk-scale exact-`Q` solver (squarefree decomposition, linear image of `N_B`, enclosing ansatz `g=P/A0` of degree 1, direct substitution of `2 H g'+H' g-2 H`). Producer `PASS` strings, the claimed `33/33` and `10/10`, and the `D=80` timing were not used as evidence. No AWS, no CAS, no canonical-ledger or case-directory edits, no ideation edits, no `jc2-lean` access.

**Firewall.** A correct rational endpoint solver is not a GGV family exclusion without a mode-completeness and denominator-provenance bridge. The artificial R3 edge `F_0=(X^8-1)^2`, `G_0=(X^8-1)^3` remains the only jet object for which that bridge is a reviewed theorem. The polynomial seven-vector of `coker_Q(M)` is a different object.

---

## Verdict table

| Item | Verdict |
|---|---|
| Rational criterion `A∈im(N_B)` | **CONFIRMED** |
| Denominator statement | **REFUTED** as written; enclosing ansatz survives |
| de Rham computation | **CONFIRMED** |
| Displayed examples | **CONFIRMED** |
| General `(α,β,N)` formula | **GAP/REPAIR** |
| Mode-completeness bridge | **GAP/REPAIR** (open; not a hidden lemma) |
| Claimed degree-uniform GGV use | **REFUTED** as a present license |
| History / novelty | **CONFIRMED** with the disclosed contamination |
| Final scope | **GAP/REPAIR** |

The rational ODE, the identity `N_B(v)=B v'+(3/2) B' v`, the infinity law `deg g=1`, and the five displayed examples survive an independent exact replay. The literal wording “denominator exactly `A0`” and “poles of order exactly half” fail on `H=X^2`. The geometric superelliptic slogan needs a primitive-cover and field/root repair. `deg A < deg B-1` is a sufficient exclusion of the *endpoint ODE*, and is presently licensed as a *jet* exclusion only for the reviewed R3 edge.

---

## Independent hashes

Recomputed SHA-256 of the charged inputs:

```text
1c17b61f00079802b20fc459550eea7bc7b09bcdcc98f27c233bde91cf348968
  xmodel/ideation-20260827T1349Z-opus5.md
66121bddbe0b004ad1b8960f896d3691c4dd3963068fbfddb6ad3ba15dda7027
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-sol-20260827.md
d40cd78f4f0afc12d09f8d1e99724de9fd5125fddc064089d6ca0870c7d777e0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-hostile-review-grok-20260827.md
0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md
b271a2958138d8e85c0a8cab068efd7bfa59227a56e5252eb27310a50fb11e24
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-hostile-review-grok-20260827.md
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md
2803b705d41b332cabd12249b0a0be17cdd18e8f2f251fe7b242bf55fc9bb289
  xmodel/ggv-8_28-M-cokernel-seven-vector-hostile-audit-sol2-20260827.md
941aea0c2a664feb10abca88c9daeb4b07e0c8a2f7265f6f0b7e67f3e5bd2b61
  xmodel/ideation-20260827T1349Z-grok.md
```

The last digest is custody for the one contaminating line in §0.2, not an imported mathematical premise. Repository `HEAD` at review time: `418e413593120d19e15e6546eb50c985f4b1f038`.

---

## 1. Rational criterion — CONFIRMED

Let `K` be a field of characteristic zero, `H∈K[X]` nonzero, and `g∈K(X)`. Write

```text
L(g) := 2 H g' + H' g.
```

The charged equation is `L(g)=2 H`. This is the first-order linear ODE

```text
g' + (H'/(2 H)) g = 1.
```

An integrating factor is `sqrt(H)` in a quadratic extension of `K(X)`: equivalently

```text
(sqrt(H) g)' = sqrt(H).
```

The homogeneous equation is `g'/g = -H'/(2 H)`, so `g_hom = C / sqrt(H)` in that extension.

Write `H=A^2 B` with `A,B∈K[X]`, `B` squarefree (including the case `B∈K`), which exists uniquely up to units of `K` by the characteristic-zero squarefree factorization. Put `u:=A g`. Then `sqrt(H)=A sqrt(B)` and the ODE becomes

```text
(u sqrt(B))' = A sqrt(B),
```

hence, after multiplying through by `sqrt(B)`,

```text
2 B u' + u B' = 2 A B.                                 (*)
```

**Finite places.** Let `P` be a monic irreducible of `K[X]`, `e=v_P(H)`, `s=v_P(g)`. In characteristic zero, `v_P(H')=e-1` whenever `e≥1`. The leading coefficient of `L(g)` at `P` is proportional to `(2 s + e)` whenever `s≠0`. Consequently:

- if `s<0` and `2 s+e ≠ 0`, then `v_P(L(g))=e+s-1 < e = v_P(2 H)`, contradiction;
- if `s<0` and `2 s+e=0`, then `s=-e/2`, so `e` is even (valuations of rational functions are integers) and the leading terms cancel;
- if `s < -e/2` then `2 s+e<0`, no cancellation, and again `v_P(L(g))<e`;
- if `e=0` and `s<0`, then `v_P(L(g))=s-1<0=v_P(2 H)`, so `g` has no pole off the support of `H`.

Thus every finite pole of a rational solution lies over an even-multiplicity factor of `H`, of order *at most* `e/2`. (Order exactly `e/2` is a separate, false, claim; §2.)

Define `A0 := ∏_{e_i even} p_i^{e_i/2}` in `K[X]`, product over monic irreducibles. Then `A0` divides `A`, the denominator of `g` divides `A0` after reducing, and `u=A g` is regular at every finite place, hence a polynomial. From `(*)`, `B` divides `u B'`. Squarefreeness of `B` in characteristic zero is `gcd(B,B')=1`, so `B` divides `u` in `K[X]`. Writing `u=B v` with `v∈K[X]` and dividing `(*)` by `2 B` yields

```text
A = N_B(v) := B v' + (3/2) B' v.
```

(The factor `3/2` uses `char≠2`, which is included in characteristic zero.) Conversely, any polynomial solution of `N_B(v)=A` produces `u=B v∈K[X]` and `g=u/A∈K(X)` satisfying `L(g)=2 H` by reversing the substitutions. This is an equivalence of existence, not of reduced representatives.

**Infinity.** Let `d=deg g ∈ Z` (degree of a rational function). If `2 d + deg H ≠ 0`, the leading term of `L(g)` has degree `d+deg H-1` and coefficient `(2 d + deg H) lc(g)`. Matching `deg(2 H)=deg H` forces `d=1`. The remaining case `2 d + deg H=0` is `d=-deg H/2`, the degree of a homogeneous solution `C/sqrt(H)`. After that leading cancellation one has `deg L(g) ≤ deg H/2 - 2 < deg H` for `deg H≥0`, so `L(g)` cannot equal `2 H`. Therefore every rational solution of the inhomogeneous equation has `deg g=1` exactly.

**`N_B` as a polynomial operator.** If `deg B≥1` and `v≠0`, the two summands of `N_B(v)` have equal degree `deg v+deg B-1` and combined leading coefficient

```text
lc(B) lc(v) (deg v + (3/2) deg B) ≠ 0
```

in characteristic zero. So `N_B` is injective on `K[X]`, `deg N_B(v)=deg v+deg B-1`, and the image contains no nonzero polynomial of degree strictly less than `deg B-1`. Hence

```text
deg A < deg B - 1  ⇒  A ∉ im(N_B)  ⇒  no rational g.
```

This is sufficient, not necessary: `H=X^4(X^2-1)` has `A=X^2`, `B=X^2-1`, `deg A=2 ≰ 1=deg B-1`, yet `N_B(v)=X^2` has no polynomial solution (already at the only candidate degree `deg v=1` the constant term `-b` and the `X^2` coefficient `4b` cannot hold together). The first guess “solvable iff `deg B≤1`” is therefore false, as the submission records.

If `deg B=0`, then `N_B(v)=B v'` with kernel the constants, and in characteristic zero every `A∈K[X]` is a derivative, so `A∈im(N_B)` always. This is exactly the perfect-square escape `H=c A^2`.

**Uniqueness.** The difference of two rational solutions of `L(g)=2 H` is a rational homogeneous solution. `C/(A sqrt(B))` lies in `K(X)` if and only if `sqrt(B)∈K(X)` after absorbing constants, and a squarefree polynomial `B` is a square in `K(X)` if and only if `B` is constant. When `B∈K`, including the case that the constant is not a square in `K` (example `H=2 X^2` over `Q`), the homogeneous solutions `k/A` still lie in `K(X)`. Thus:

- `B` nonconstant: at most one rational `g`;
- `B` constant: an affine line `g = (∫A + k)/A`.

**Relation to `M` and to R3.** For `g=H Y` one has the identity, verified by direct expansion on five independent `Y` including `H=X^8-1`,

```text
H g' + g H'/2 = (H/4) M(Y),    M(Y)=4 H Y' + 6 H' Y.
```

So `M(Y)=1` is `L(g)=H/2`. Existence for nonzero constant multiples of `H` on the right-hand side is equivalent, because `L` is linear. This is *not* existence for `L(g)=1`, which is exactness of `dX/w` rather than `w dX`. The charged ODE is the latter. For squarefree `H` one has `A0=1`, so a rational `g` is a polynomial of degree 1; `B|u` then asks a degree-`1` polynomial to be divisible by `H` of degree `≥2`, which is the same obstruction as `M(Y)=1` having no polynomial solution. That last polynomial fact is R1/R3 and, for this specific `H`, the seven-dimensional cokernel of `M` on `Q[X]`. The cokernel seven-vector classifies remainders of a *global polynomial* `E_22`; it does not decide the rational ODE for general `H`, and it does not replace raw provenance.

**Smallest repair to the writeup, not to the equivalence:** state characteristic zero and `H≠0` in `K[X]`; take `B` squarefree in `K[X]` (no splitting of `K` is required); record that `N_B` fails to be injective precisely when `B` is constant; record that `deg A < deg B-1` is sufficient, not an if-and-only-if.

---

## 2. Denominator statement — REFUTED as written

The submission asserts that `g` has poles “of order exactly half” at even-multiplicity roots, and that “the denominator is exactly `A0`”. Both sentences are false.

**Smallest failing example.** `H=X^2`. Then `A=X`, `B=1`, `A0=X`. The ODE is `2 X^2 g' + 2 X g = 2 X^2`, i.e. `(X g)'=X`. Solutions

```text
g = X/2 + k/X,    k∈K.
```

Direct substitution: for `k=0`, `g=X/2`,

```text
2 X^2 · (1/2) + 2 X · (X/2) = X^2 + X^2 = 2 X^2.
```

The reduced denominator is `1`, which properly divides `A0=X`. The pole order at `0` is `0`, not `1=e/2`. For `k≠0` the denominator is exactly `A0`. So even the weaker claim “every solution has denominator `A0`” fails, and the claim “there exists a solution with denominator `A0`” is true only after adding a homogeneous term that is unavailable when `B` is nonconstant.

The same cancellation occurs for `H=X^4`, particular solution `g=X/3`, and for every perfect square by taking the integration constant so that `∫A+k` vanishes to first order at a chosen root of `A` when that is possible. For `(X+1)^2` the solver’s particular `g=(X+X^2/2)/(X+1)` still has denominator `A0`, but the homogeneous shift `k=1/2` cancels it to `g=(X+1)/2`.

**What survives.** The denominator of any rational solution *divides* `A0`. The linear system with denominator `A0` and `deg g=1` (equivalently `deg P=deg A0+1`, hence `deg A0+2` unknown coefficients) is a correct enclosing ansatz: cancelled numerators are included, and the homogeneous line for squares is the one free variable in that system. The a-priori bound is therefore still a bound, not a search cap, once “exactly `A0`” is replaced by “divides `A0`”.

**Firewall coefficient in §5.** The displayed pole leading coefficient `((12-N) e + 4 s)`, claimed to force `s=e/2`, is the wrong formula for this ODE. For `L(g)` the leading coefficient is `2 s+e`. For the R3 operator on `d` with `F_0=H^2` it is `2 e(α-N)-β s_d` (`=-20 e-8 s_d` at `(α,N,β)=(12,22,8)`), which vanishes at `s_d=-5e/2`, not at `s=e/2`. This does not refute the valuation conclusion of §1; it refutes the certificate identity as printed. Repair: quote `(2 s+e)` for `g`, or R3’s `(8 m-20)` for the squarefree `H`-adic pole of `d`.

---

## 3. Integrating factor and de Rham — CONFIRMED

**Operator identity.** Direct expansion, independent of any producer file:

```text
d/dX (H^{3/2} Y) = (3/2) H^{1/2} H' Y + H^{3/2} Y',
4 H^{-1/2} d/dX (H^{3/2} Y) = 4 H Y' + 6 H' Y = M(Y).
```

The identity `H g' + g H'/2 = (H/4) M(Y)` for `g=H Y` holds on `H=X^8-1` for `Y∈{1,X,1+X^2, 1/2+(3/4)X-(1/5)X^2, X^3}`. Thus `M(Y)=1` says that `(1/4) sqrt(H) dX` is exact with primitive `H^{3/2} Y`. That is exactness of `w dX` on `w^2=H` with primitive in `w^3 K(X)`, equivalently in `w K(X)`.

**Function-field form.** A meromorphic primitive of `w dX` on the affine curve is `F=p+q w` with `p,q∈K(X)`. Then

```text
dF = (p' + (q' + q H'/(2 H)) w) dX.
```

Matching `w dX` forces `p` constant and `L(q)=2 H`. The rational criterion of §1 is therefore exactly meromorphic exactness of `w dX` in the function field of `w^2=H`.

**Reduction on `H=X^8-1`.** Let `ω=dX/w`. From `dw=(H'/(2 w)) dX=4 X^7 ω` one has `[X^7 ω]=0`. For any integer `k≥0`,

```text
d(X^k w)/dX
  = k X^{k-1} w + X^k · 4 X^7 / w
  = (k X^{k-1} (X^8-1) + 4 X^{k+7}) ω
  = ((k+4) X^{k+7} - k X^{k-1}) ω
```

(with the `k=0` term `k X^{k-1}` absent). This coefficient identity was checked for `k=0,...,7`. At `k=1`,

```text
5 X^8 ω - ω  is exact,    hence  [X^8 ω]=(1/5)[ω].
```

Then `w dX=(X^8-1) ω=X^8 ω - ω`, so

```text
[w dX] = (1/5)[ω] - [ω] = -(4/5)[ω].
```

The complete nonsingular model of `w^2=X^8-1` is hyperelliptic of genus `3` (`deg=2g+2`). The form `ω` is holomorphic and nonzero (a basis of holomorphic differentials is `X^i ω` for `i=0,1,2`). A nonzero holomorphic differential on a compact curve of positive genus is not the differential of a meromorphic function: a nonconstant meromorphic `Z` has `deg(Z)_∞≥1`, hence `dZ` has a pole of order at least `2`. Therefore `[ω]≠0` in meromorphic de Rham cohomology of the compactification, hence `[w dX]≠0`, hence there is no primitive in the function field, hence no rational `g`. This agrees with §1: `A=1`, `deg B-1=7>0`.

The affine-versus-compact distinction is harmless here. A rational primitive on the affine curve extends to a meromorphic primitive on the compactification (poles at infinity allowed). The class computation already permits meromorphic primitives.

Nonexactness is a statement about a curve, not about a Keller map. It obstructs the charged face jet only after the R3 mode/denominator bridge, which is reviewed for this one `H` and not for a family.

---

## 4. Degree bound and displayed examples — CONFIRMED

Independent exact-`Q` checker, not the producer tables:

| `H` | `A` | `B` | `deg A < deg B-1` | criterion | substitution `L(g)=2H` | enclosing `g=P/A0` |
|---|---|---|---|---|---|---|
| `X^8-1` | `1` | `X^8-1` | yes (`0<7`) | EXCLUDED | — | no solution |
| `X^16-1` | `1` | `X^16-1` | yes (`0<15`) | EXCLUDED | — | no solution |
| `X^2` | `X` | `1` | no | SOLVABLE, `g=X/2` | holds | holds (`1` free) |
| `h^2=(X+1)^2` | `X+1` | `1` | no | SOLVABLE, `g=(X+X^2/2)/(X+1)` | holds | holds (`1` free) |
| `X^D`, `D=1,3,5` | `X^{⌊D/2⌋}` | `X` | no | SOLVABLE, `g=(2/(D+2)) X` | holds | holds |
| `X^2(X^2-1)` | `X` | `X^2-1` | no (`1≮1`) | SOLVABLE, `v=1/3`, `g=(X^2-1)/(3 X)` | holds | holds |

Further guards, all agreeing with `A∈im(N_B)` versus the enclosing linear system: `X^4-1` excluded; `X^2-1` excluded; `X(X^2-1)` excluded; `X^3(X^2-1)` excluded; `X^2(X^4-1)` excluded; `X^4(X^2-1)` excluded *without* the degree test; `X^2(X^2+1)` solvable with `v=1/3`; constant `H=1` solvable by `g=X`; forty random dense `H` of degree `1..8` with coefficients in `{-3,...,3}` plus six structured extra polynomials: `46/46` agreement, `0` substitution failures.

The single-root family is closed-form, not a sample: `H=c(X-r)^D` with `D` odd gives `B` linear, `N_B(v)=(X-r) v'+(3/2) v`, and `v=c' (X-r)^{(D-1)/2}` hits `A`. For `D` even, `B` is constant and §1 applies. The `X^D-1` family is excluded for every `D≥2` by `A=1` and `deg B-1=D-1>0`; squarefreeness of `X^D-1` in characteristic zero is `gcd(X^D-1, D X^{D-1})=1`. No degree-`80` solve is required for that conclusion. The producer timing is not a witness.

The square escape `g=(∫h)/h` is one particular solution; the full rational solution set is `(∫h+k)/h`.

These examples are endpoint-ODE verdicts. `H=X^{16}-1` being ODE-excluded does not exclude a jet with leading edge `F_0=X^{16}-1`; R3 already disclaims that edge, and this criterion does not repair the disclaimer.

---

## 5. General `(α,β,N)` formula — GAP/REPAIR

Let

```text
E = α F_X G - β F G_X - t (F_X G_t - F_t G_X)
```

with `α,β∈K` and `β≠0`. For `Z=t^n F^γ` in a binomial extension of `K(X)[[t]]`,

```text
E(F, t^n F^γ) = t^n F^γ F_X (α - β γ - n).
```

The kernel condition is `γ=(α-n)/β`. This is the R3 identity with `(12,8)` replaced by `(α,β)`, and the same cancellation of the `F_t` Jacobian block.

If a residual first appears at weight `N` as `t^N d` with `d∈K(X)`, the `t^N` slice uses only `F_0`: `t F_t G_X` starts at order `N+1`, and

```text
(α-N) F_0' d - β F_0 d' = 1.                           (**)
```

The integrating factor `F_0^{-(α-N)/β}` gives `d=F_0^{(α-N)/β} v` with

```text
v' = -1 / (β F_0^{(α+β-N)/β)} = - (1/β) F_0^{(N-α-β)/β}.
```

For `(α,β,N)=(12,8,22)` and `F_0=H^2`,

```text
v' = -1/(8 F_0^{-1/4}) = -(1/8) H^{1/2},
```

which is the charged square-root ODE. That algebra is confirmed.

**What needs repair.**

1. *Field and branch.* Characteristic zero (or at least `β` invertible and the integers `2 d+deg H`, `deg v+(3/2) deg B` nonzero). The identity `(**)` is an ODE over `K(X)`. The functions `F_0^{(α-N)/β}` and `F_0^{(N-α-β)/β}` live in a radical extension. A branch of `F_0^{1/β}` in an algebraic closure of `K(X)` must be fixed; R3’s normalisation `S_0=H` together with `G_0=H^3` is such a choice for the square-cube edge, and the opposite square root is excluded by `(-H)^3≠H^3` in characteristic not `2`.

2. *Primitive cover, not the naive degree-`β` equation.* The slogan “exactness on `u^β=F_0^{N-α-β}`” is not primitive in general. For the charged weights, `N-α-β=2` and `β=8`, so `u^8=F_0^2=H^4`. Then `gcd(2,8)=2` and `u^8-H^4` is reducible; the relevant component under `S_0=H` is `w^2=H`, degree `2`, not a degree-`8` superelliptic curve. In general one must replace the cover by a primitive equation `û^{β/d}=F_0^{k/d}` with `k=N-α-β` and `d=gcd(k,β)`, then select the branch compatible with the leading edge. Card A’s specialisation “[`sqrt(H) dX`] on `w^2=H`” is the correct reduced statement; the two-parameter slogan is not.

3. *Exactness on the cover is necessary, not sufficient, for `d∈K(X)`.* The residual coefficient is required to be rational in `X`. That is exactness of `F_0^{(N-α-β)/β} dX` with primitive in the specific `K(X)`-line `F_0^{(α-N)/β} K(X)`, not an arbitrary meromorphic primitive on the cover.

4. *Resonance.* If `(α-N)/β∈Z` and `F_0` to that power is rational, weight `N` is itself a homogeneous mode, `(**)` acquires a kernel, and the pole lemma of R3-type has no bite. The submission names this. For `(12,8,22)` one has `(12-22)/8=-5/4∉Z`, so this particular endpoint is not a mode for squarefree `H`. It *is* a mode when `H` is a square: `H^{(12-22)/4}=H^{-5/2}` is rational as soon as `H` is a square, and for `H=X^2` every even `n` (including `22`) is a mode. That is consistent with the square escape of the ODE, and it is exactly why R3’s induction does not copy to general `H`.

5. *The operator `N_B` is not the general-face criterion.* `N_B` uses the square-root substitution for `F_0=H^2`. Other `(α,β,N)` produce other radical profiles. Instantiating “one criterion per GGV face” requires a fresh squarefree decomposition in that radical, not a reuse of `N_B`.

Repair: keep `(**)` and the `v'` formula as the endpoint ODE in a named radical extension; state the primitive cover and the `d∈K(X)` restriction; do not advertise a uniform superelliptic theorem across the GGV face table without those hypotheses.

---

## 6. Firewall, mode completeness, and GGV use

### 6.1 What is a theorem today

- The rational ODE `L(g)=2 H` over a characteristic-zero field, with the criterion `A∈im(N_B)` and the sufficient test `deg A < deg B-1`, after the denominator wording of §2 is repaired.
- Exactness of `w dX` on `w^2=H` as a restatement of that ODE.
- The specialisation `H=X^8-1`: no rational `g`, equivalently `[w dX]=-(4/5)[ω]≠0`.
- R1: `M(Y)=1` has no polynomial solution inside two named ansatzes (reviewed).
- R2: rootwise scalar-carrier completeness through weight `22`, no global `H`-multiple (reviewed).
- R3: no polynomial-`X` formal jet with `F_0=(X^8-1)^2`, `G_0=(X^8-1)^3`, and `E=t^{22}+O(t^{23})`, via a complete homogeneous classification on `K(X)[[t]]` through weight `21` plus an endpoint pole lemma (reviewed).

R3 *is* the case `A=1`, `deg B-1=7` of the ODE obstruction, plus a mode-and-denominator bridge that is not supplied by the ODE solver. The one-line recovery of R3’s last step does not subsume R3.

### 6.2 Mode-completeness bridge — GAP/REPAIR

R3’s completeness uses that `H^{(12-n)/4}∈K(X)` for squarefree `H` if and only if `(12-n)/4∈Z`, hence only `n=0,4,8,12,16,20` below weight `22`. For general `H=A^2 B` the same exponent is rational at additional `n` as soon as the multiplicities of `H` supply the missing denominators. In particular:

- `H` a square: every even `n`, including the endpoint `n=22`;
- `H` a fourth power: every `n`.

Extra modes change both the kernel subtracted before weight `22` and the possible denominators of the residual `d`. R3’s pole lemma `d=-Y/(2 H)` with `Y` polynomial is squarefree-specific. The submission names this dependency and does not prove it. That honesty is recorded; the gap is still a gap. Until a reviewed general-`H` induction exists, the ODE exclusion cannot be copied to a jet exclusion.

Denominator provenance for non-squarefree `H`, raw `2S/3S` polynomial cleanup, and GGV landing are likewise untouched. The cokernel audit already forbids treating a seven-vector, or any rootwise interpolation, as a substitute for that provenance.

### 6.3 `deg A < deg B-1` beyond the R3 endpoint — REFUTED as a jet license

The inequality is presently licensed for:

- the rational ODE, for arbitrary nonzero `H` in characteristic zero;

and is presently licensed as a *formal-jet* exclusion only for:

- the artificial R3 edge `H=X^8-1`, by combining the ODE with the reviewed R3 bridge.

It is **not** licensed for `H=X^{16}-1`, for a general square/cube leading edge, for multiple-root edges, for a GGV `8_28` family member at its own leading data, or for any object produced by `lib/families.py`. Card A step (ii) (“run the criterion over `case_rows(150)`”) was not a theorem in the submission and would still only decide endpoints, not jets, until step (i) is proved. The original non-Keller `8_28` witness with `F_0=X^{16}-1` remains outside scope, exactly as R3 stated.

### 6.4 Claimed degree-uniform GGV use — REFUTED as a present theorem

The ODE solver is degree-uniform: the same leading-coefficient argument decides `H=X^8-1` and `H=X^{80}-1`. That is a property of an ODE. Avenue 1, §4.1, and Card A PASS convert it, in the success tense, into “no polynomial jet reaches the charged weight, for every square/cube edge with `deg A < deg B-1`, for every degree”, and into “the first degree-uniform exclusion in the portfolio”. That conversion is exactly the missing bridge. A correct endpoint solver is not a GGV family exclusion. It is not `G2-PSC`, not `G2-BD`, and not a cofinal `td` theorem. `REDUCTION.md` item 5 is not attacked until a reviewed source/landing statement exists.

The smallest repair, which the submission already sketches in §5’s scope gate and then undercuts in the raise: every GGV-facing sentence carries `mode_completeness_dependency=OPEN`, and Card A PASS is not spoken in the present tense.

---

## 7. History / novelty — CONFIRMED with the disclosed contamination

**Contamination.** Section 0.2 of the charged ideation records one `rg` hit, the line

```text
xmodel/ideation-20260827T1349Z-grok.md:209:`8_28`. The integrating factor of `M` is `H^{-1/2}`; making `H` a
```

Hash of that peer file is `941aea0c...` above. The integrating factor of `M` is therefore convergent in this round, not a sole-novelty claim. Grok’s use of it, in the unread-beyond-this-fragment remainder of that paragraph, is a type-change warning against making `H` a square, i.e. against reading R3 as a degeneration of the original edge. Opus5’s use is the closed-form ODE criterion. Those are different payloads behind the same one-line identity. Discount independence of the integrating-factor sentence; do not discard the rest on that sentence.

**Pre-round, independently searched.** Hits for hyperelliptic/de Rham in this repository attach to AS109 Cartier/de Rham–Witt, to polynomial exactness on `A^2`, or to the max-12 hyperelliptic deck action. They do not attach a curve `w^2=H`, a genus, or a class `[w dX]` to a GGV face or to `M`. Hits for integrating factors are the AS109 warning not to hunt an ambient factor of `ω`, plus the present round. The six-mode R3 normal form and the endpoint pole lemma are R3, not this criterion. The polynomial Pell receiver `A^2-Q P(Q)^2=` constant on `w^2=Q` is a live max-12 object (`xmodel/max12-812-order2-p0-cech-lowcontact-pell-total-rees-successor-design-20260826.md` and descendants); repository search finds no pre-round identification of that Pell equation with a GGV-face de Rham class.

**Nonduplicate relative to pre-round history, after subtracting the convergent integrating factor:**

- the closed-form rational criterion `A∈im(N_B)` and the sufficient test `deg A < deg B-1`;
- the a-priori law `deg g=1` with denominator dividing `A0`, as a general-`H` rational bound rather than R3’s squarefree polynomial `Y`;
- the distinction that Pell solvability on `w^2=Q` and de Rham exactness of `w dX` on `w^2=H` are different tests, with the same curve `z^4-1` a positive Pell control and a negative exactness example (`H=X^4-1` is ODE-excluded by `deg B-1=3>0`, independently of any Chebyshev formula).

Conflating those two tests would be the error the submission flags. That warning is correct and pre-round-new as a GGV/max-12 connection. Building a shared software instrument is a proposal, not a result.

The polynomial cokernel theorem audited in `ggv-8_28-M-cokernel-seven-vector-hostile-audit-sol2-20260827.md` is a third object: `Q[X]=im(M)⊕Q[X]_{≤6}` for this one `H`. It is not the rational criterion, and the present review does not retry it.

---

## 8. Final scope — GAP/REPAIR

**Promote, after the denominator wording is repaired, as an endpoint theorem only:**

> Over a characteristic-zero field, a nonzero polynomial `H=A^2 B` with `B` squarefree admits a rational solution of `2 H g'+H' g=2 H` if and only if `A` lies in the image of `N_B(v)=B v'+(3/2) B' v` on `K[X]`. In particular `deg A < deg B-1` excludes every rational solution. For `H=X^8-1` this is equivalent to `[w dX]=-(4/5)[dX/w]≠0` on `w^2=H`.

**Do not promote:**

- “denominator exactly `A0`” / “poles of order exactly half”;
- a degree-`β` superelliptic cover without primitive reduction and branch choice;
- general-`H` mode completeness, extra-mode lists, or R3’s pole lemma beyond squarefree `H=X^8-1`;
- raw `2S/3S` provenance or polynomial cleanup;
- any GGV family exclusion, any `case_rows(150)` conclusion, `G2-PSC`, `G2-BD`, a cofinal `td` bound, or JC2;
- present-tense Card A PASS / avenue 1 “degree-uniform exclusion of square/cube edges”.

The submission’s own §3.2 paragraph “What this does not do”, Card A’s named open dependency, and §5’s `mode_completeness_dependency=OPEN` gate are the correct scope. The raise text and the PASS sentence are not. The coordinator should keep the endpoint theorem and the R3 jet theorem on separate ledgers: the first is general in `H` and silent on jets; the second is a jet theorem for one artificial edge.

Nothing in this review is a Keller pair, a counterexample, or a JC2 statement.
