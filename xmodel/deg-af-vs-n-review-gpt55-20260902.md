# Hostile review: DEG-AF-VS-N -- every PROVED-HERE item, the family, the consequences

Reviewer: gpt-5.5  
Date: 2026-09-02  
Lane: `DEG-AF-VS-N-REVIEW`  
Basis commit: `9c8412a92e5c74cf915b903e788ad9eee3128409`

No exit-price assertion is made; no `charge_basis` line is emitted. No
canonical ledger was edited, and `jc2-lean` was not inspected. The only write is
this bounded review report.

## Custody

The frozen inputs were hashed with `shasum -a 256` before any review read. All
four match the charge exactly:

```text
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kCRADW/inputs/deg-af-vs-n-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kCRADW/inputs/chau-delta-budget-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kCRADW/inputs/mprime-alln-h2-opus5-20260902.md
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.kCRADW/inputs/b3-e-geometry-opus5-20260902.md
```

Abbreviations: **DG** = the DEG-AF-VS-N producer report; **CD** = Chau delta
budget; **MI** = MPRIME-ALLN-H2; **B3E** = B3-E-GEOMETRY. I also read local
reviewed context for typings only: `AM-CHECK.md`, `SHEET6-CLASSICAL.md`,
`horn-flagship-opus5-20260902.md`, `horn-flagship-review-grok46-20260902.md`,
and `ops/open_collision.py`. Web custody was used only for primary/public
literature metadata around Jelonek and the semigroup-at-infinity theorem.

## Verdict Table

| Item | Producer lines | Verdict | Promotion recommendation |
|---|---:|---|---|
| SG-INV: `Gamma={deg_t f(a,b)}` is Aut-invariant and `#gaps=delta_aff` | DG:118-147 | **CONFIRMED with repair** | Promote after adding reparametrisation invariance and naming the gap identity as the normalization-length formula, not AM-SG. |
| BUDGET=IDENT: `delta_aff+delta_infty=p_a(n)` computes `delta_infty` | DG:149-156 | **CONFIRMED** | Promote. This is the genus formula split into affine and infinity terms. |
| DEG-DELTA(a): `delta_aff <= (n-1)(n-2)/2` in every gauge | DG:194-199 | **CONFIRMED** | Promote. |
| DEG-DELTA(b): `b_1|b_0` or `n <= 2 delta_aff+b_1-1 <= 3 delta_aff` | DG:206-233 | **CONFIRMED with scope repair** | Promote only with the stated principal/Tschirnhausen escape retained. |
| (R1)-(R4) minimal-gauge necessary conditions | DG:253-274 | **CONFIRMED as necessary** | Promote as filters/lower-bound data, not as sufficiency or exact `n_min`. |
| MERIDIAN-FLOOR | DG:304-328 | **CONFIRMED** | Promote. It uses only generic meridian cycle type and transitivity. |
| Lower half of `OPEN[N-VS-MAPDEG]` | DG:361-368 | **CONFIRMED** | Promote as a lower bound on map degree, explicitly not the needed upper half. |
| Non-derivability certificate at fixed `N`, `k -> infinity` | DG:376-402 | **CONFIRMED** | Promote as formal ledger satisfiability only; no Keller realization. |
| Explicit cusp-plus-`k`-nodes family, verified through `k<=11` | DG:406-422 | **CONFIRMED with wording repair** | Promote as affine singularity witnesses. Do not promote "no other projective singularity": infinity is singular when `delta_infty>0`. |
| `(B2)` consequence `beta <= floor(delta_aff/2)` and death condition | DG:475-498 | **CONFIRMED** | Promote; it repairs CD's weaker `beta <= Delta_aff`. |
| `(B3)` consequence `k <= delta_aff-delta_c` | DG:500-549 | **CONFIRMED** | Promote with representative-only typing. |
| `2g(E)=1+N nu-n_infty(E)` | DG:572-581 | **CONFIRMED with convention** | Promote if `g` means arithmetic genus of the compactified normalization, or if `E` is known irreducible. |
| `n=4`, `(2,3)`, `k=1` empty; minimal profile at `n=5` | DG:524-549 | **CONFIRMED** | Promote; it sharpens CD's budget-only list. |
| Literature custody: Jelonek degree bound is in coordinate degrees, not `N`; no curve-degree-by-etale-degree theorem in custody | DG:588-624 | **CONFIRMED with citation repair** | Promote custody warning. Repair: the displayed Jelonek bound appears already in Jelonek 1993 Theorem 15, not only the 1999 testing-sets reference. |

## 1. SG-INV And The Delta Identity

**Verdict: CONFIRMED with two mandatory repairs.**

DG defines, under MI Lemma A, a birational polynomial parametrisation
`t |-> (a(t),b(t))` of `D=A_F` and

```text
Gamma = { deg_t f(a(t),b(t)) : f in C[u,v], f not in I(D) }.
```

Target automorphisms are correctly handled at DG:143-145: if `psi in
Aut(C^2)`, then a parametrisation of `psi(D)` is `psi(a,b)`, and
`f |-> f o psi` is an automorphism of `C[u,v]`. Thus the degree set is
unchanged.

The missing line is reparametrisation. Since `D~ = A^1`, every algebraic
automorphism of the normalization is affine, `t |-> alpha t + beta` with
`alpha != 0`; polynomial degree is invariant under this substitution. A
projective change such as `t |-> 1/t` does not preserve the affine normalization
`A^1` and is not a reparametrisation of the polynomial one-place model. This
must be stated before promotion.

The gap count is also correct, but its source is not AM-SG. It is the classical
normalization-length formula for affine curves:

```text
dim_C( normalization coordinate ring / curve coordinate ring )
  = sum_{p in Sing D} delta_p.
```

Here the affine normalization is `C[t]` and the curve coordinate ring is
`S=C[a,b]`. The conductor makes `C[t]/S` finite. Filtering by degree gives a
basis represented by the monomials `t^m` whose degrees are gaps of `Gamma`;
hence `#(N\Gamma)=dim_C C[t]/S=sum delta_p`.

Hypotheses: one place at infinity is needed to make the affine normalization
`C[t]` and to make the degree/pole-order semigroup numerical. No unibranch
hypothesis is needed at the affine singularities. Multibranch affine points are
exactly included in `sum delta_p`.

Classical custody: modern public accounts define the semigroup at infinity for
a curve with one place at infinity as the pole-order semigroup of regular
functions off the infinity point, and recall the Abhyankar-Moh delta-sequence
theorem for its generators; see Suzuki 1999, abstract/citation data, and the
definition/theorem summary in Galindo-Monserrat-Moreno-Avila-Moyano-Fernandez
2024. The gap identity above is the affine normalization quotient, not the
delta-sequence theorem.

**Repair text.** "The equality `#gaps(Gamma)=delta_aff` is the finite length
`dim_C(C[t]/C[a,b])`, hence the sum of affine local delta invariants. One place
at infinity is needed; affine singularities may be multibranch."

## 2. Degree-Delta Bounds

### 2.1 BUDGET=IDENT and DEG-DELTA(a)

**Verdict: CONFIRMED.**

For a rational projective plane curve of degree `n`,

```text
delta_aff + delta_infty = p_a(n) = (n-1)(n-2)/2.
```

This proves DG:149-156: the Chau-style budget computes the gauge-dependent
`delta_infty` once `n` and `delta_aff` are known. It is not an independent
invariant constraint.

DEG-DELTA(a), DG:194-199, is immediate from the same genus formula because the
affine singularities are a subset of all projective singularities:

```text
delta_aff <= p_a(n)
```

in every target gauge, hence also at `n_min`.

### 2.2 DEG-DELTA(b), AM-SG, And Tschirnhausen

**Verdict: CONFIRMED with the escape clause load-bearing.**

The exact banked AM-SG statement consumed is `AM-CHECK.md:50-63`: for an
irreducible degree-`n` plane curve with one place at infinity, the semigroup at
infinity is generated by a positive delta-sequence
`(delta_0,...,delta_h)`, `delta_0=n`, with

```text
d_1 = delta_0,              d_{i+1}=gcd(d_i,delta_i),
d_{i+1} < d_i,              d_{h+1}=1,
n_i = d_i/d_{i+1},
delta_{i+1} < n_i delta_i,
n_i delta_i in <delta_0,...,delta_{i-1}>.
```

This is consistent with the public semigroup-at-infinity summaries: a curve
with one place at infinity determines a numerical semigroup generated by a
delta-sequence, and the first element can be the degree of the curve.

DG's derivation at 223-233 is algebraically sound. In the notation
`b_0=n`, `d_1=gcd(b_0,b_1)`, if `b_1` does not divide `b_0`, then
`d_1 <= b_1/2`, so

```text
(n_1-1)b_1 = b_0(b_1/d_1)-b_1 >= 2b_0-b_1.
```

The conductor formula for a telescopic/free semigroup gives

```text
2 delta_aff >= (n_1-1)b_1 - b_0 + 1 >= b_0-b_1+1,
```

which is `n <= 2 delta_aff+b_1-1`. Since the semigroup multiplicity has
`1,...,b_1-1` as gaps, `b_1-1 <= delta_aff`, giving
`2 delta_aff+b_1-1 <= 3 delta_aff`.

The Tschirnhausen step is narrower than a theorem closing the principal case.
If the smaller coordinate degree is `p=b_1`, the larger coordinate has degree
`n`, and `p|n`, then the triangular target automorphism

```text
(u,v) |-> (u, v - lambda u^(n/p))
```

with `lambda` chosen from the leading coefficients strictly lowers the larger
degree. This proves non-minimality in that represented-coordinate situation.
It does not prove the global statement `n_min <= 2 delta_aff+1` for every
principal delta-sequence; DG correctly leaves `OPEN[MIN-EMBED-DEGREE]` at
244-250.

**Promotion scope.** Promote DEG-DELTA(b) exactly with "`b_1|b_0` or ..." and
with `OPEN[MIN-EMBED-DEGREE]` kept open.

### 2.3 (R1)-(R4)

**Verdict: CONFIRMED as necessary conditions only.**

DG:253-274 correctly records: `n in Gamma`; `(n,Gamma)` satisfies AM-SG;
`delta_aff <= p_a(n)`; and there is a smaller degree `p in Gamma` with
`p<n`, `p` not dividing `n`, and

```text
delta_aff <= p_a(n) - (n-p)(n-p-1)/2.
```

The multiplicity computation at infinity is correct after a target linear
change giving coordinate degrees `p<n`: in the infinity chart the one branch
has multiplicity `n-p`. A branch of multiplicity `mu` has
`delta >= mu(mu-1)/2`, yielding (R4). The divisibility exclusion is the
Tschirnhausen reduction above.

**Repair text.** "These are necessary filters for a minimal gauge; the table
gives a lower bound `n_min >= n_AM(Gamma)`, not a sufficiency theorem."

## 3. MERIDIAN-FLOOR

**Verdict: CONFIRMED.**

The proof at DG:312-328 is valid and can be made completely explicit.

`F : A^2\E -> A^2\D` is a connected degree-`N` finite etale cover: B3E states
this at 111-121, and the argument is standard from the definition of the
non-properness set plus Keller etaleness. Connectedness gives transitive
monodromy on the `N` sheets.

A generic affine line meets the degree-`n` curve `D` in `n` points. Zariski's
generic-line theorem gives a surjection from the line complement group to
`pi_1(A^2\D)`, so the global group is generated by those `n` meridians. Since
`D` is irreducible, the meridians are conjugate.

The generic meridian cycle type is

```text
1^a * prod_l mu_l^{s_l}
```

with `W=N-a=sum_l s_l mu_l` and `S=sum_l s_l`. This is the same type used in
MI's representation gate at 694-696 and in HORN's parity theorem: HR:73
computes the sign from exactly `N-#cycles = W-S`. At `N=4`, MI's N4-PIN gives
`(a,W,s,mu)=(2,2,1,2)`, hence generic cycle type `(2,1,1)`, matching
MI:585-592 and HR:135-149. The local cusp and node types `(3,1)` and `(2,2)`
are stronger local data; ORBIFOLD-CAGE uses those locally and does not change
the generic-meridian floor.

Block-count proof: begin with `N` singleton blocks. Adding one generator with
cycle lengths `mu_l` can merge at most `sum_l s_l(mu_l-1)=W-S` blocks, because
each cycle of length `r` can reduce the current block count by at most `r-1`.
After all `n` meridian generators have been added, transitivity requires a
single block. Thus

```text
n(W-S) >= N-1.
```

If `W-S=0`, no generator moves any sheet and transitivity fails for `N>1`; in
the campaign regime 7.B' gives `mu_l>=2`, hence positivity anyway
(MI:82-88). Since `S>=1`, `W-S <= W-1`, so

```text
n_min >= ceil((N-1)/(W-S)) >= ceil((N-1)/(W-1)).
```

**Cycle-typing check.** CUSP-PARITY uses this same generic meridian type and is
compatible. ORBIFOLD-CAGE is local at a quasi-homogeneous cusp and is not a
premise of the floor. No flag/place/series identification is present.

**Half of `OPEN[N-VS-MAPDEG]`.** CD's Chau transfer gives the cap
`n <= max(deg P,deg Q)` under its hypotheses (CD:119-126). Composing gives only

```text
max(deg P,deg Q) >= ceil((N-1)/(W-1)).
```

This is the lower half. It does not answer the needed upper bound of
`OPEN[N-VS-MAPDEG]`.

## 4. Non-Derivability And The Curve Family

### 4.1 Fixed-`N` Satisfying Assignment

**Verdict: CONFIRMED.**

DG:380-392 gives a genuine satisfying assignment for the banked profile
constraints at fixed `N`. I checked the arithmetic at fixed `N=5` for
`k=2,3,5`; the same algebra is independent of `k`.

Use

```text
N=5, a=3, W=2, one dicritical (s,mu)=(1,2), R=0, beta=1.
cusp: r=1, K=2, a_p=1.
each node: r=2, K=0, a_p=1.
```

Then sheet gate, `[P3]`/7.B', `(L)`, `(K)`, `(C2)`, `(C3)`, and `(M')` all
hold:

```text
sum K_p = 2 = a-1,
node K=0 <= D_gap=1,
# {K_p>0} = 1 <= R+beta,
a(nu+s-1) - sum a_p = 5 nu - 1.
```

For `k=2,3,5`, the last identity gives respectively `9=9`, `14=14`,
`24=24`. This proves only ledger non-derivability. It is not a Keller witness.

### 4.2 CAS Verification Of The Family

**Verdict: CONFIRMED with the affine-only repair.**

I ran independent SymPy 1.14.0 exact computations over `Q`. The three
mandatory samples use:

```text
k=2:  (x,y) = (t^3, t^4+t^2)
k=3:  (x,y) = (t^3, t^5+7t^4+3t^3+t^2)
k=5:  (x,y) = (t^3, t^7+t^2)
```

For each sample I computed the implicit resultant, the line-at-infinity
intersection, critical parameters, the two divided differences

```text
(x(t)-x(s))/(t-s),   (y(t)-y(s))/(t-s),
```

the squarefree nonzero self-intersection resultant, tangent determinant at
paired parameters, and the triple-fibre remainder. Results:

```text
k=2: degree 4, implicit factor degree 4, F_h(Z=0)=-X^4.
     critical gcd T; orders at 0 are (3,2), so germ is (2,3).
     squarefree nonzero resultant degree 4 -> 2 nodes.
     no tangent-degenerate pair, no critical node parameter, no triple fibre.
     p_a=3, delta_aff=3, delta_infty=0.

k=3: degree 5, implicit factor degree 5, F_h(Z=0)=-X^5.
     critical gcd T; orders at 0 are (3,2), so germ is (2,3).
     squarefree nonzero resultant degree 6 -> 3 nodes.
     no tangent-degenerate pair, no critical node parameter, no triple fibre.
     p_a=6, delta_aff=4, delta_infty=2.

k=5: degree 7, implicit factor degree 7, F_h(Z=0)=-X^7.
     critical gcd T; orders at 0 are (3,2), so germ is (2,3).
     squarefree nonzero resultant degree 10 -> 5 nodes.
     no tangent-degenerate pair, no critical node parameter, no triple fibre.
     p_a=15, delta_aff=6, delta_infty=9.
```

The unique preimage of the line at infinity is `t=infinity`, so there is one
place at infinity in each case. The parametrisation is birational because the
only multiple fibres are the listed double fibres, and no triple fibre occurs.
For a birational map from a smooth curve, the only affine singularities are
critical images and multiple-fibre images; therefore the listed cusp and nodes
are all affine singularities.

I also reran the remaining printed `k<=11` cases using the same criterion:

```text
k=2/q4       ok, degree 4,  nodes 2,  delta_aff 3
k=3/q5tail   ok, degree 5,  nodes 3,  delta_aff 4
k=5/q7       ok, degree 7,  nodes 5,  delta_aff 6
k=6/q8tail   ok, degree 8,  nodes 6,  delta_aff 7
k=8/q10      ok, degree 10, nodes 8,  delta_aff 9
k=9/q11tail  ok, degree 11, nodes 9,  delta_aff 10
k=11/q13     ok, degree 13, nodes 11, delta_aff 12
```

**Repair text.** DG should say "no other affine singularity." For `k=3` and
`k=5`, `delta_infty` is positive, so the projective point at infinity is a
singular unibranch point. Interpreted as "no other projective singularity," the
claim is false; interpreted as the affine family needed for the profile, it is
confirmed.

## 5. B2 And B3 Consequences

### 5.1 B2: `beta <= floor(delta_aff/2)`

**Verdict: CONFIRMED.**

CD:232-236 proves only `beta <= Delta_aff`. DG:477-482 strengthens this
correctly in case `(B2)`. A point counted by `beta` is multibranch and has at
least one singular branch. For a reduced plane curve singularity,

```text
delta_p = sum_i delta(B_i) + sum_{i<j} I(B_i,B_j) - r + 1.
```

If one branch is singular, then `delta(B_i)>=1` and its intersection with at
least one other branch contributes at least its multiplicity, hence at least
`2`. Already for two branches this gives `delta_p >= 1+2-2+1=2`, and extra
branches cannot lower it. Therefore

```text
beta <= floor(delta_aff/2).
```

MI's profile theorem requires `beta>=2` for `5<=N<=10` and `beta>=1` for
`11<=N<=16` (MI:413-436). Hence this instrument kills `(B2)` exactly under:

```text
5 <= N <= 10:   delta_aff <= 3,
11 <= N <= 16:  delta_aff <= 1.
```

"Exactly" here means exactly for the beta lower-bound instrument; it is not an
absolute classification theorem beyond the stated inequalities.

### 5.2 B3: `k <= delta_aff-delta_c`

**Verdict: CONFIRMED.**

For one cusp of Puiseux pair `(p,q)`, `delta_c=(p-1)(q-1)/2`. Every additional
double point has at least delta `1`, or contact contribution `t_i>=1`. Thus

```text
delta_c <= delta_aff,       k <= delta_aff-delta_c,
sum_i t_i = delta_aff-delta_c
```

when the double points are the only other affine singularities. This removes
`delta_infty` from the B3 list. HF Prop. 3.2's `N=4` cusp typing
`(2|p and 3|q) or (3|p and 2|q)` is correctly consumed from the reviewed horn
lane (HF:286-304, HR:139).

### 5.3 `n=4`, `(2,3)`, `k=1`

**Verdict: CONFIRMED.**

CD's list is explicitly budget-only (CD:347-384) and admits at `n=4` the row
`(2,3), k=1..2` (CD:392-394). DG's sharpening at 524-546 is correct:

`k=1` gives `delta_aff=2`. A degree-4 one-place rational curve would then have
`delta_infty=1`. Its branch at infinity has multiplicity `2`, so after a linear
change the coordinate degrees are `p=2<n=4`. Since `2|4`, the Tschirnhausen
triangular automorphism lowers the degree to at most `3`. But a rational plane
curve of degree at most `3` has `p_a<=1`, impossible with
`delta_aff=2`. Thus the `n=4`, `(2,3)`, `k=1` row is empty.

The row `n=4`, `(2,3)`, `k=2` is real: the CAS sample
`(t^3,t^4+t^2)` above has one place at infinity, one ordinary `(2,3)` cusp,
and exactly two ordinary nodes. The minimal B3 profile `(2,3)+one node` is
realized at degree `5` by DG's representative `(t^2,t^5+t^3+t^2)`, not at
degree `4`.

### 5.4 `2g(E)=1+N nu-n_infty(E)`

**Verdict: CONFIRMED with a convention.**

DG:572-581 combines Theorem (E), `chi_c(E)=1-N nu`, with

```text
chi_c(E) = 2 - 2g(E) - n_infty(E).
```

This is correct for irreducible `E` with `g` the geometric genus. For
disconnected `E`, the same display remains correct only if `g(E)` is read as
the arithmetic genus of the compactified normalization:

```text
g_arith = sum_i g_i - (#components) + 1.
```

B3E's review already made this binding repair. Promote the formula with this
convention; do not quote it as a nonnegative geometric genus statement in
disconnected cells.

## 6. Literature Custody

**Verdict: CONFIRMED with one citation repair.**

Local custody is as DG reports: `refs/` contains Chau and Moh PDFs, but no
Jelonek or Abhyankar-Moh PDFs. `SHEET6-CLASSICAL.md:267-276` carries Jelonek's
component and degree statements, with the degree-bound form marked from memory.

Primary-source web check: Jelonek's 1993 Annales Polonici Mathematici paper,
"The set of points at which a polynomial map is not proper," states Theorem 15
for a dominant map `f=(f_1,...,f_n): C^n -> C^n`: the non-properness set is
empty or a uniruled hypersurface with degree bounded by

```text
(prod_i deg f_i - mu(f)) / min_i deg f_i.
```

In dimension two this is exactly a bound in the coordinate degrees
`deg f, deg g` and geometric degree `mu(F)=N`; it is not a bound in `N` alone.
This confirms DG's mathematical custody claim. The repair is bibliographic:
the displayed bound is already in the 1993 paper, not only in "Testing sets for
properness" 1999-2002.

The 2018 Jelonek-Lason quantitative paper gives another coordinate-degree
style statement: for a generically finite polynomial map of algebraic degree
`d`, `S_f` is covered by parametric curves of degree at most `d-1`. Again this
uses algebraic/coordinate degree, not the etale covering degree `N`.

I found no primary theorem bounding the degree of a plane curve from above by
the degree of a finite etale cover of its complement. This is a custody
finding, not a proof of nonexistence. The mathematics in this lane points the
opposite way: MERIDIAN-FLOOR gives a lower bound on curve degree from a
transitive degree-`N` cover with prescribed meridian cycle type.

Sources checked:

```text
Jelonek 1993 PDF, Theorem 15: https://matwbn.icm.edu.pl/ksiazki/apm/apm58/apm5834.pdf
Jelonek-Lason 2018 metadata/abstract: https://arxiv.org/abs/1411.5011
Suzuki 1999 semigroup theorem metadata: https://www.numdam.org/item/AIF_1999__49_2_375_0/
Galindo et al. 2024 semigroup-at-infinity definitions: https://arxiv.org/html/2408.15931v2
```

## 7. FALLACY-v2 Audit

Flag/place/series: `Gamma` is the affine coordinate-ring degree semigroup;
`Gamma_infty` is the local semigroup at the projective infinity branch; AM
delta-sequences are ordered generating data; Chau's `m` is a gauge gcd. These
are not identified.

Carrier/attainment: the fixed-`N` assignment and the cusp-plus-nodes curves are
representative/numerical witnesses only. No Keller `A_F` realization is
claimed.

Floor/attainment: DEG-DELTA(a) and MERIDIAN-FLOOR are floors. The B3 crossing
still needs an upper bound. DEG-DELTA(b) has a named principal escape and does
not close `OPEN[MIN-EMBED-DEGREE]`.

Per-ray/exit-set charge: no new exit price is asserted.

Pole/interior: the multiplicity `n-p` is used only for the unique infinity
branch after one-place normalization is fixed.

Variable/ring map: CAS checks used declared rings over `Q`, resultants of the
implicit parametrisations and divided differences, squarefree degrees, and
tangent determinant controls. No `sat()` wrapping or quotient normal-form
claim is in play.

## Opens Raised Or Sharpened

`OPEN[MIN-EMBED-DEGREE]`: bounds the minimal embedding degree `n_min` of a
rational one-place polynomial curve above in terms of its affine delta,
specifically whether `n_min <= 2 delta_aff + 1` after the principal
`b_1|b_0`/Tschirnhausen cases are resolved. This bounds the delta-form
crossing in DG:557-561; it is not needed for the B2/B3 consequences in
DG:475-549.

`OPEN[DELTA-AFF-VS-N]`: bounds `delta_aff(A_F)=sum_p delta_p` above in terms of
the Keller geometric degree `N`. This is the invariant replacement for the raw
degree gate `OPEN[DEG-AF-VS-N]`, whose unminimized curve-degree form is already
false by target automorphisms.

`OPEN[N-VS-MAPDEG]`: bounds `max(deg P,deg Q)` above in terms of geometric
degree `N`. This report confirms only the lower half
`max(deg P,deg Q) >= ceil((N-1)/(W-1))`; the upper half remains open.

## Typed Verdict Block

```text
LANE              DEG-AF-VS-N-REVIEW
SCOPE             Keller, noninvertible, H2 unless a subsection explicitly
                  says it is only a representative plane-curve computation.

PROMOTE           SG-INV with reparametrisation and normalization-length
                  repairs; BUDGET=IDENT; DEG-DELTA(a); DEG-DELTA(b) with its
                  `b_1|b_0` escape; (R1)-(R4) as necessary filters;
                  MERIDIAN-FLOOR; lower half of N-VS-MAPDEG; fixed-N ledger
                  non-derivability; B2 beta <= floor(delta_aff/2); B3
                  k <= delta_aff-delta_c; n=4,(2,3),k=1 EMPTY; the cusp+nodes
                  family as affine-singularity representatives.

DO NOT PROMOTE    "no other singularity" if it means projective singularity;
                  `2g(E)=...` with geometric genus in disconnected cells;
                  any upper bound on n_min or delta_aff in terms of N;
                  any Keller realisation of the representative curves;
                  any closure of OPEN[N-VS-MAPDEG] upper half;
                  the citation "Jelonek degree bound only from 1999-2002."

MEASURED          SymPy 1.14.0 over Q. Required samples:
                  k=2: (t^3,t^4+t^2), degree 4, one infinity place,
                       one (2,3) cusp, two ordinary nodes, no other affine
                       singularity.
                  k=3: (t^3,t^5+7t^4+3t^3+t^2), degree 5, one infinity place,
                       one (2,3) cusp, three ordinary nodes, no other affine
                       singularity; delta_infty=2.
                  k=5: (t^3,t^7+t^2), degree 7, one infinity place,
                       one (2,3) cusp, five ordinary nodes, no other affine
                       singularity; delta_infty=9.
                  Remaining printed k<=11 cases also pass the same resultant,
                  squarefree, tangent, and triple-fibre checks.

REPAIR SUMMARY    SG-INV: add affine reparametrisation invariance and identify
                  #gaps with dim_C(C[t]/C[a,b]), hence affine delta.
                  DEG-DELTA(b): exact AM-SG is the banked delta-sequence
                  theorem; Tschirnhausen removes only represented principal
                  coordinate-degree cases.
                  MERIDIAN-FLOOR: uses generic meridian cycle type only;
                  compatible with CUSP-PARITY and ORBIFOLD-CAGE.
                  Family: no other affine singularity, not no other
                  projective singularity.
                  Literature: Jelonek coordinate-degree bound confirmed, but
                  source repaired to Jelonek 1993 Theorem 15.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25583`.
- Body SHA-256:
  `3aa1af2a3c01de959d7201986235a03d0939fb6635d4951b2c2d1a48fbae9f64`.
- Frozen basis: `9c8412a92e5c74cf915b903e788ad9eee3128409`.
