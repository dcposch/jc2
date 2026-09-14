**HOSTILE GATE — R050 physical-place residue pilot — Fable 5.1 — 2026-09-06**

Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. Producer: Astra,
`xmodel/r050-parent-residue-pilot-astra-20260906.md` with `box/r050-parent-residue-20260906/check.py`.
Method: desk proof plus bounded SymPy replay (about one minute in total); no AWS, no `jc2-lean`,
no live report, ledger, launcher or adapter touched. Independent notes, scripts and JSON are in
`box/r050-parent-residue-gate-20260906/`.

**Verdict.** All five charged claims are CONFIRMED at the producer's stated scope, with the scope
of item 3 pinned, item 4 split into a proved half and an OPEN half, and one exact addition
(residue theorem at the e=28 place). The pilot proves a local constraint (four coefficient
equations, `H1` constant) that is the `u^-1` row of the pulled-back constant-Jacobian identity
at the e=4 place. It kills no R050 row, realizes no source, and measures no speedup.
Campaign disposition: **NO_NEW_MECHANISM**; the surviving object is the exact theorem in §7.

| Item | Verdict | What survives the gate |
|---|---|---|
| 1. Split 4+28; centre; `u`; no `t^(19/28)` term; `alpha != 0` | **CONFIRMED** | The zero root is forced by Galois semi-invariance (`q = 1 mod 7`), not chosen. The e=4 place is `K(T)`-rational; the 28 nonzero-root series are one place. The "no intermediate split" arrow is consumed from the exact-contact gate (Moh Prop 5.3), not re-read here. |
| 2. `H=Av+B+uH1+O(u^2)`, `deg H1<=4`, `A!=0`, `Res=4H1'((T-B)/A)/A^2` | **CONFIRMED** | Sign and all three coordinate changes verified by hand and by a generic SymPy series. Addition: `Res_P' = -Res_P`, so the e=28 place adds no equation. |
| 3. 19-term family | **CONFIRMED, scope pinned** | Proves non-implication from {top form, D2 face, D1 face} only. It is not shown to be an R050 tree, has no g-face, no Jacobian row, no mate, and says nothing about Jacobian-row independence. |
| 4. Mate floor; `b H1' = -4[u^1]J_xy` | **CONFIRMED / OPEN** | Redundancy on the full Keller ideal localized at `A j` is exact; `b != 0` already follows from `A b = -4 j`. Early-row compression is OPEN: the row mixes Jacobian rows of every total degree 1..250. |
| 5. Controls; Sol off-by-one; pencil caveat | **CONFIRMED** | Sol's printed pair has `J = gamma^(l+1)`; repaired `P = gamma^l/l`. `h = x + x^2 y` is the `b=1` member of the pencil report's own family `f_b`; it shows fibrewise exactness is not sufficiency. |

**Custody.** I joined the seven `charged_input_i_basename` / `charged_input_i_sha256` fields of my
own `run.v2` receipt to the files in `/tmp/jc2-lane.xD53BS/inputs` in a loop: **7/7 OK**. The
producer's `check.py` bytes are preserved as `producer-check.py.frozen` (same SHA) and replayed:
`PASS_EXACT_SYMBOLIC`, SymPy 1.12, exit 0. My `independent_checks.py` derives every quantity from
the licensed pattern and Xu's text, not from the producer's formulas; all its asserts pass
(`independent_checks.json`). Moh's paper is not a charged input of this lane; every arrow that
needs it is labelled CONSUMED in §6. Xu references are to the frozen `xu.txt` by section and
printed page.

**1. The physical place.** Licensed R050 data (exact-contact gate §4, replayed in `R050_arith`):
`n=196, m=56, d2=28, n-M2=12, delta2=1/4`, level-2 face `[pi(pi^4-c1)^4(pi^4-c2)]^2` with
`c1 c2 (c1-c2) != 0`. The selected multiplicity 4 gives `rho=8` f-roots per final-major disc,
`-lambda_f(D2)=7/2`, `delta1=19/28`, `lambda_f=-1/14`, `lambda_g=-1/4`, and
`1+lambda_f+lambda_g=delta1` (Xu Lemma 4.4 through Lemma 4.1, pp.4-5). Four discs, centres
`t^-1 + (order-0 term) + alpha t^(1/4) + ...`, `alpha^4 = c1 != 0` because the zero root of the
D2 face is the separate factor `pi`, not a root of `pi^4-c1`.

*Centre.* Between orders `-1` and `1/4` only the integer order 0 occurs (unsplit, denominator 1).
Between `1/4` and `19/28` the pattern allows no split (CONSUMED: gate §3-4 via Moh Prop 5.3).
An unsplit term at an order `d'` there must be fixed by the stabiliser of the prefix inside
`Z/28`, which is `{k = 0 mod 4}`, a `Z/7`; that forces `4 d'` integral, so only `d' = 1/2`.
Hence `eta = t^-1 + c0 + alpha t^(1/4) + beta t^(1/2)`, exactly the producer's form. It is
`T`-independent because every face at or below `delta1` has negative f-order
(`-14, -7/2, -3/2, -1/14` at orders `0, 1/4, 1/2, 19/28`) while `T` has order 0.

*The zero root is forced.* For `k = 4j`, `tau_k` fixes `eta`, sends `pi t^(19/28)` to
`zeta_7^(5j) pi t^(19/28)` and `t^(-1/14)` to `zeta_7^(-2j) t^(-1/14)`. Since `-2 = 5 mod 7`,
the final face satisfies `f_sigma(w pi) = w f_sigma(pi)` for a primitive seventh root `w`, so
every monomial has `q = 1 mod 7`. Degree 8 and squarefree (final) leave only
`f_sigma = pi (C pi^7 + A)` with `A C != 0`. The direct floor agrees: `7i + 19q = -2` has exactly
the solutions `(i,q) = (-3,1), (-22,8)` (`floor_equality_monomials`). The producer's
"shape `C pi (pi^7 - d)`" is a theorem of the pattern, and the simple zero root is not an extra
hypothesis.

*Parameter and cover.* Put `t = u^4`, `z = y - eta = u^3 v`. The floor `7i + 19q >= -2`
(u-units: `4 lambda_f = -2/7`) with `N = i + 3q` gives `N >= ceil((2q-2)/7)`: no negative
u-power; `N=0` admits `q <= 1`; `N=1` admits `q <= 4`; `N=2` admits `q <= 8`
(`f_allowed_v_degrees_by_u_power`). Therefore `H(u,v) := f(u^-4, eta + u^3 v)` is a polynomial,
`H = A v + B + u H1(v) + O(u^2)`, with `A` the coefficient of `pi` in the face, `A != 0`, and
`deg H1 <= 4`. Since `H_v(0,v) = A` is a unit, `H(u,v) = T` has a unique solution
`v(u)` in `K(T)[[u]]` with `v(0) = (T-B)/A`. The resulting root lies in `K(T)((t^(1/4)))`, has no
`t^(19/28)` term (its distance from `eta` has order `3/4 > 19/28`, so its face value is `pi = 0`),
and has exact denominator 4 because `alpha != 0`. Its four conjugates under
`t^(1/4) -> i t^(1/4)` are the zero roots of the four discs: **one** `K(T)`-rational place `P` with
`e_P = 4` and residue field `K(T)`. The other seven roots per disc have a nonzero `t^(19/28)`
coefficient (exact denominator 28) and, as simple face roots, continue inside
`K(T)((t^(1/28)))`; the 28 series are one orbit under `Z/28`: one place `P'` with `e = 28`.
Thirty-two series, two places. This is exactly FALLACY-v2's series/flag/place separation, and the
producer keeps it.

**2. The residue.** On `f = T`, `df = 0` gives `omega_f := dx/f_y = -dy/f_x`, and
`dg = (g_x f_y - g_y f_x)/f_y dx = -j omega_f`. At `P` with uniformizer `u`: `dx = -4 u^-5 du`;
`d/dv H = u^3 f_y`, so `f_y = u^-3 H_v`; hence `omega_f = -4 u^-2 du / H_v(u, v(u))` with
`H_v(u, v(u)) = A + u H1'(v0) + O(u^2)`, `v0 = (T-B)/A`. Expanding,

```
omega_f = [ -(4/A) u^-2 + (4 H1'(v0)/A^2) u^-1 + O(1) ] du,
Res_P(omega_f) = 4 H1'((T-B)/A) / A^2 .
```

I re-derived this with a fully generic `H` through `u^2` and generic `v(u)` through `u^1`
(`residue_formula`), including the leading `-4/A`. Cross-check with Xu Prop 3.3(i), p.2:
`ord_t f_y = lambda_f - delta1 = -3/4`, three u-orders, matching `f_y = u^-3 (A + ...)`.
`H1'` is the genuine `v`-derivative of a polynomial of degree at most 4 and `T` is transcendental,
so `Res_P = 0` identically iff `h1 = h2 = h3 = h4 = 0`, i.e. `H1` constant. Substituting a numeric
`T` first would lose this equivalence; the producer says so, correctly. The four discs are Galois
conjugate (`alpha -> i^k alpha`, `beta -> (-1)^k beta`), so one disc's four equations are the
whole content of `Res_P = 0`.

*Addition: residue theorem.* On the smooth generic fibre `omega_f` is regular at every affine
point (`f_y = 0` forces `f_x != 0`). At every final-minor place, `lambda_f = 0` and
`e ord_t f_y = -e delta` is an integer, so `ord_u omega_f = e(delta-1) - 1 >= 0` (Xu Lemma 4.4(ii)
gives `delta > 1`; checked for all `e <= 59`). The places over `x = infinity` on the pattern are
`P`, `P'`, and minor places only (`14 + 10 + 32 = 56` roots). Hence **`Res_P' = -Res_P`**: the
seven-order expansion at the e=28 place is determined by the four equations at `P`. This is new
relative to the producer and costs nothing.

**3. The family.** `f_eps = r^2 (y^4 w^2 q^8 - kappa y w^2 q + eps y w^3 q)`, `w = y-x`,
`q = y w^4 - 1`, `r = y w^4 - a`. Replayed independently: total degree 56, top form `y^14 w^42`,
19 monomials in `(y,w)` (329 in `(x,y)`); D2 face at `u^-14` equals `[pi(pi^4-1)^4(pi^4-a)]^2`;
D1 face at `s^-2` equals `(1-a)^2 ((4 pi)^8 - 4 kappa pi) = 4(1-a)^2 pi (4^7 pi^7 - kappa)`,
squarefree with a simple zero root; both faces and the top are `eps`-free. The complete support of
`f_eps(u^-4, u^-4 + u + z)` obeys `7i + 19q >= -2` with equality exactly at `(-3,1), (-22,8)`
(`family_floor_violations = []`), so the family sits on the licensed floor. `H0 = -4 kappa (1-a)^2 v`,
`H1 = 4 eps (1-a)^2 v`, `Res_P = eps / (kappa^2 (1-a)^2)`. `A != 0` iff `kappa (1-a) != 0`, and
`alpha = 1`, so `P` is a genuine e=4 place of the generic fibre of `f_eps`, not a decorative flag.

Scope: this proves only that {top form, D2 face, D1 face} do not imply `H1` constant. It proves
nothing about independence from the rest of the R050 source. `f_eps` is not shown to realize the
R050 tree: its minor-side data (five level-2 minor discs at `delta = 2`, fourteen principal minors
at `delta* = 3`), its `g`-face, every Jacobian row, and a mate are all absent. The producer's scope
sentence is correct and is not extended here. In particular the family must not be used to fill
the GAP row of §6.

**4. Mate floor and Keller redundancy.** For an actual mate, Xu Lemma 2.1(i), p.2, gives
`lambda_g = -1/4`, so the g-floor is `7i + 19q >= -7`, `N >= ceil((2q-7)/7)`: `N=-1` admits only
`q = 0` (the term `b/u`), `N=0` admits `q <= 3`, `N=1` admits `q <= 7`
(`g_allowed_v_degrees_by_u_power`). With `G := g(u^-4, eta + u^3 v) = b/u + G0(v) + u G1(v) + u^2 G2(v) + ...`,
an exact expansion with generic `H` through `u^2` and `G` through `u^2` gives
`[u^-3] J_uv(H,G) = 0`, `[u^-2] = A b`, `[u^-1] = b H1'(v)`; neither `G0`, `G1` nor `H2` enters
at `u^-1`. The source determinant is `J_uv(x,y) = -4 u^-2`, so the chain rule gives
`J_uv(H,G) = -4 u^-2 (J_xy(f,g) o phi)`. Under `J_xy = j`: `A b = -4 j` and `b H1' = 0`; `b != 0`
follows from `A b = -4 j` alone. The face-disjointness argument is a second proof, and Xu's
Lemma 4.4 display at `pi = 0` reads `J = lambda_g f_sigma'(0) g_sigma(0) = -A b/4`, the same sign.
Without assuming constancy, `b H1'(v) = -4 [u^1](J_xy(f,g) o phi)`; the constant monomial of `J`
contributes only at `u^0 v^0`, so `b (k+1) h_(k+1)` lies in the ideal of the nonconstant Jacobian
rows for `k = 0..3`, and `h_i` lies in that ideal localized at `A j` once `c0, alpha, beta` are
adjoined. **Redundant on the full Keller ideal: CONFIRMED.**

Early-row compression is a different question and is **OPEN**. Writing
`[u^1](J o phi) = sum_(a,b) J_ab [u^(4a+4b+1)] (1 + c0 u^4 + alpha u^5 + beta u^6 + u^7 v)^b`,
the pure-`y` row `y^D` contributes `D c0^(D-1) alpha + ...` for every `D >= 1`, so the residue row
is a `K[c0,alpha,beta,v]`-combination of Jacobian rows of every total degree `1..250`, weighted by
growing powers of centre data. It is not a syzygy-free consequence of any degree-bounded top band,
while it is the second row in the u-adic order at `P`. Whether it lies in the ideal of the first
bands of any R050 engine is not decided here: no R050 band engine is among the charged inputs and
an engine's t-power grading is not total degree. The producer's typing, "possibly useful as a
projection constraint, no speed gain measured", is the correct one.

**5. Controls and the two older texts.** Positive: `(y + x^2, -x)` has `J = 1`, inverse
`(-g, f - g^2)`, `omega_f = dx` on the parabola `f = T` with a residue-free double pole at
`x = infinity`, and `dg = -omega_f` as the sign convention demands. Negative: `h = x + x^2 y` has
`(1 - 2xy) h_x + 4 y^2 h_y = 1`, so no critical points; on `h = T != 0`, `y = (T-x)/x^2` and
`omega_h = dx/x^2 = d(-1/x)`, both residues 0; on `h = 0` the disjoint components `x = 0` and
`xy = -1` carry `d(-y)` and `d(-1/x)`. Every fibre has a regular primitive. Yet `J(p,h) = j != 0`
is impossible for polynomial `p`: `d/dx p(x,(T-x)/x^2) = j/x^2` forces `p = -j/x + C(h)` in
`k[x, x^-1, y]`, and `x p` at `x = 0` gives `j = 0`. I also solved the coefficient system for every
`p` of degree at most 6: all solutions have `j = 0`. This `h` is the `b = 1` member of the pencil
report's own negative family `f_b = x + x^2 y^b` (KPG §2.3, genus 0 at `b = 1`). It is why the
charged caution stands: residue vanishing, even fibrewise exactness on every fibre, does not
supply a Keller mate.

Sol Q2.A prints `Q = gamma pi`, `P = gamma^(l+1)/(l+1)` with "`J(P,Q) = gamma^l`"
(sol56 lines 283-288). Direct computation: `P_gamma Q_pi - P_pi Q_gamma = gamma^l gamma = gamma^(l+1)`.
Off by one, as the producer reports; `P = gamma^l/l` gives `J = gamma^l`, `omega_Q = d gamma/gamma`
with residues `+1, -1`, and `gamma^l omega_Q = dP` (checked `l = 1..6`). The conceptual point of
Q2.A, that a descended `J = j gamma^l` child carries no residue constraint, survives the repair.

Pencil report §2.3 (KPG lines 164-165) says a mate `v` with `{u,v} = 1` exists iff `omega_u` is
exact on every fibre, "(integrate `omega_u` from a section; algebraicity is the residual)". The
negative control shows that the parenthesis is load-bearing: fibrewise exactness holds for `h`
with no polynomial mate. Retain the sentence only as "iff, with a primitive that is the restriction
of one global polynomial". The producer's reading is right. KPG §2.2's "residues vanish, periods
vanish, neither is a condition" remains a statement about Keller pairs, not a sufficiency test,
and KPG §2's identification of its divisor count with Riemann-Hurwitz is untouched by this pilot.

**6. Source-interface arrows.**

| Arrow | Status |
|---|---|
| Pattern: levels, multiplicities, `delta2 = 1/4`, `delta1 = 19/28`, 8 roots per disc | CONSUMED from exact-contact gate §4 (charged) |
| No intermediate split between `1/4` and `19/28` | CONSUMED (gate §3-4 via Moh Prop 5.3; Moh not in this lane) |
| Orders at D1: `lambda_f, lambda_g`, `delta = 1 + lambda_f + lambda_g` | VERIFIED in Xu (Lemma 2.1, 4.1, 4.4) |
| Centre form, forced zero root, floors, shape of `H`, `e = 4` | PROVED here |
| Residue formula, Keller `u^-1` row, redundancy, `Res_P' = -Res_P` | PROVED here |
| Explicit `h1..h4` as polynomials in R050 source unknowns | **GAP**: no R050 source chart exists in the inputs; the producer gives the recipe (expand through `u^1` under the declared map), not the rows. Not filled by the family. |

**7. Usable exact theorem (surviving scope).** Let `(f,g)` be a Jacobian pair over an
algebraically closed field of characteristic zero realizing the licensed R050 pattern above, and
let `eta, u, H, G` be as in §1 and §4 on one final-major disc. Then:
(i) `H` is a polynomial, `H = A v + B + u H1(v) + O(u^2)`, `A != 0`, `deg H1 <= 4`; the zero root
is a `K(T)`-rational place `P` of `f = T` with `e_P = 4` and `Res_P(dx/f_y) = 4 H1'((T-B)/A)/A^2`;
(ii) `G = b/u + G0(v) + ...` with `deg G0 <= 3`, `A b = -4 j`, and `H1` is constant, i.e.
`h1 = h2 = h3 = h4 = 0`, these being the `u^-1` row of the pulled-back Jacobian identity;
(iii) `Res_P' = -Res_P` at the e=28 place and every minor place has zero residue, so (ii) is the
complete residue content over `x = infinity` on this pattern;
(iv) the four equations are not implied by the top form and the two displayed faces (the family),
and are implied by the full constant-Jacobian ideal localized at `A j`.
Nothing in (i)-(iv) is a kill, a realization, or a count improvement.

**Cheapest next discriminator.** None with a new mechanism. If an exact R050 source chart is ever
built, add the four rows `h1..h4` (through-`u^1` expansion under the declared map, `c0, alpha,
beta` adjoined, `1 - Z A j` as localizer) before any Groebner step and record whether they change
the chart; that is bookkeeping, not a kill. Repeating the contact census, computing an untwisted
child residue, or expanding the e=28 place are answered above and should not be run.

**FALLACY-v2 disposition.** Series (32), discs (4), places (2), the cover parameter `u` and the
physical uniformizer are kept distinct throughout. The valuation floor is used only as an upper
bound on `v`-degrees; attainment (`A != 0`) is a theorem of the final face, not a cap. The pole
identity is applied at a verified final-major vertex with `lambda_f < 0` and squarefree face. The
ring map `x -> u^-4, y -> u^-4 + c0 + alpha u + beta u^2 + u^3 v` is declared with its determinant
`-4 u^-2` and image checks. `H1'` is a genuine derivative in `v`. No `sat()` is used. No new
exit-price assertion is made, so no `charge_basis` line is licensed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16736`.
- Body SHA-256:
  `83fd2af0571413db573103a4ffba187ba9f0164747f0e38f357b68f3f5fce569`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
