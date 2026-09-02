# Desk lane: MF-RATIONAL — can the generic member of a Keller pencil be rational?

Lane: `MF-RATIONAL`. Date: 2026-09-02. Agent: grok-4.6.
Desk derivation plus exact integer enumeration (`python3`; no Groebner, no
AWS, no ledger edit, no `jc2-lean`). No `charge_basis` line: this report
asserts no new exit price.

## 0. Custody, typing, scope

The four frozen charged copies were hashed with `shasum -a 256` **before any
was read**; all four match the charge exactly:

```text
5c11369a6b5d6198206dce722d7c1d657d687d2b074003a5970eb883a5fdfa65  mf-defect-mult-vs-beta-grok46-20260902.md
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  meridian-floor-sharpen-opus5-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  meridian-floor-sharpen-review-gpt55-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  n-vs-mapdeg-review-gpt55-20260902.md
```

Abbreviations: **MD** = charged MF-DEFECT producer; **MFS** = MERIDIAN-FLOOR-SHARPEN
producer; **MR** = its gpt-5.5 review; **NVR** = N-VS-MAPDEG review.

Typing, as charged. MF-EXACT at MR-CONFIRMED with the S-known / W-only repair
(MR:30-36, 141-149). MERIDIAN-FLOOR+ at NVR-CONFIRMED (NVR:53-60, 290-314):
`p(W-S) >= N-1` with `p <= n-1`, hence `n >= ceil((N-1)/(W-S))+1` and
`2 g_L + theta_inf >= W-S+1`. MF-DEFECT at MD's stated strength
(PROVED-HERE / UNREVIEWED): `2 g_L + theta_inf >= 2`; the S-known floor is
never attained. Case (A) EMPTY; no `Z(G)=1`; no A2. SMOOTH-KILL and 7.B'
banked as in MD: `S >= 1`, `n >= 3`, and at `W=2` one has `(s, mu)=(1,2)`.
Coordinator ~11:05Z defect-budget note: respected.

## 1. Verdict, up front

```text
(Q) OPEN[MF-RATIONAL]  NOT CLOSED as a theorem g_L >= 1 for all N.
    THEOREM MF-RATIONAL-N2: for N=2 the numerical type g_L=0 is empty
    (no solution of MF-EXACT + MF-DEFECT + MERIDIAN-FLOOR+ + theta_inf <= N
    + n >= 3). For N >= 3 the type is nonempty: the equality case
    (g_L, theta_inf)=(0,2), W-S=1, n=N is a solution of every consumed
    identity and is realised by an explicit rational function
    phi(z)=P(z)/z^m of degree N on P^1.
    Literature (Kaliman / AMS, Zaidenberg-Lin, C*-classification,
    Neumann-Norbury 1998, Miyanishi-Sugie, simple-type classification)
    kills fibres cong C, fibres cong C*, the all-fibres-irreducible
    subcase, and simple type; none of those is the remaining Keller type
    (theta_L = nS + theta_inf >= 5, some reducible smooth fibre, a
    dicritical horizontal of degree >= n).
    Bounded quantity remaining: g_L in {0,1,...,p_a(D_F)}; if g_L=0 then
    the pair (W-S, n, theta_inf) lies in the finite list of Sec 4, with
    2 <= theta_inf <= N, theta_inf >= W-S+1, n(W-S)=N-2+theta_inf, and
    theta_L = nS + theta_inf <= D_F.
    A NO (g_L >= 1 always) is NOT claimed. If proved, it would upgrade
    MF-EXACT to n(W-S) >= N+1 and drop every crossing price by one.
```

## 2. Recalled identities, at confirmed typing

Generic target coordinates `(u,v)`, generic line `L={u=gamma}`,
`h := u o F`, `C_L := F^{-1}(L) = {h = gamma}`. Jacobian constant makes `h` a
polynomial **submersion**: every fibre of `h` is smooth and reduced, and
`deg C_L = D_F := max(deg P, deg Q)` for generic `u` (MR:100-105). Transitive
monodromy of `C_L \ F^{-1}(A_F) -> L \ A_F` makes `C_L` irreducible
(MR:107-116). The compactified `v`-map `pi : X_L -> P^1` of degree `N` is
MF-EXACT (MR:141-149):

```text
n (W - S)  =  N - 2 + 2 g_L + theta_inf,
theta_L    =  n S + theta_inf,
chi(C_L)   =  N - n W.
```

`theta_inf` = number of points of `X_L` over `infty_L`; the remaining `n S`
source-infinity places lie over `L cap A_F` with meridian type
`1^a * prod_l mu_l^{s_l}`. No affine ramification. SHARP-CHAU (MR:378-397):
`n S + theta_inf <= D_F`. Always `1 <= theta_inf <= N`.

MF-DEFECT: `2 g_L + theta_inf >= 2`. MERIDIAN-FLOOR+: `2 g_L + theta_inf >= W-S+1`.
Hence if `g_L=0` then `theta_inf >= max(2, W-S+1)` and
`n(W-S) = N-2+theta_inf >= N`. Standing: `S >= 1`, `n >= 3`.

The other pencil coordinate `v` restricts to `C_L` as a holomorphic map
`v : C_L -> A^1` of degree `N`, étale (because `{u,v}=const != 0`), non-proper
exactly over the `n` points of `L cap A_F`.

## 3. Task (1): classical submersion-and-rational-fibre theorems

Write `h = u o F`. This is a polynomial submersion `C^2 -> C` of degree `D_F`,
primitive (generic fibre irreducible). If `g_L=0` it is a **rational polynomial**
in the sense of Neumann–Norbury. The place count is not the classical one:

```text
theta_L = n S + theta_inf  >=  n + 2  >=  5
```

(`S>=1`, `theta_inf>=2`, `n>=3`). The classical list, with applicability:

**Gutwirth / AMS / Kaliman.** A polynomial with a smooth fibre `≅ C` is a
variable (Gutwirth; AMS; Kaliman, Pacific J. Math. 154 (1992) and 203 (2002)).
Applies only to `(g_L, theta_L)=(0,1)`, already excluded by MF-DEFECT
(`theta_L >= nS+2 >= 5`). Control: `F_m=(x,y^m)` attains `(0,1)` and is not étale.

**Zaidenberg–Lin.** Classification of polynomial embeddings of `C` into `C^2`,
including cuspidal `t |-> (t^k, t^l)`. A submersion has no singular fibre, so
the only remaining Z-L fibre is a smooth `C`, which is AMS. Neither an example
with `theta_L>=5` nor a kill.

**The `C*`-fibre case.** Kaliman, Pacific J. Math. 174 (1996): primitive rational
polynomials with a fibre `≅ C*`. Generic `C*` is `theta_L=2`, incompatible with
`theta_L>=5`. A *special* fibre of `h` may still be `C*`; that is not a
contradiction and does not constrain the generic fibre.

**Neumann–Norbury 1998.** Bull. Austral. Math. Soc. 58 (1998), 501–503,
Theorem 2: a rational polynomial with all affine fibres irreducible is a
coordinate (so Razar / Heitmann / Lê–Weber is empty). Proof: Miyanishi–Sugie /
Saito, Osaka J. Math. 17 (1980), Lemma 1.6, `delta-1 = sum_c (r_c-1)`, plus
NN Proposition 3 / Kaliman 1992 Cor. 2 (gcd of horizontal degrees = number of
generic-fibre components; places per component = (sum of degrees)/gcd). All
`r_c=1` forces `delta=1` and `theta_L=1`. This is MD Steps 3–4, already used
to kill `(0,1)`. For `theta_inf>=2` the same formula forces some `r_c>=2`, so
`h` is outside the 1998 hypothesis. Razar, Israel J. Math. 32 (1979), 97–106,
likewise needs all fibres irreducible. Miyanishi–Sugie at `g_L=0` gives only
`delta>=2`, compatible, not a kill.

**Simple type.** Neumann–Norbury, Pacific J. Math. 204 (2002), Theorem 1.1:
horizontals all of degree 0 or 1; three families `f1,f2,f3`, each with a
*birational* (not étale of degree `N>=2`) partner. Lê, Publ. RIMS 44 (2008),
Theorem 3.2, and Chau, Ann. Polon. Math. 93 (2008): a simple polynomial in a
Jacobian pair is invertible. These would kill `g_L=0` if `h` were simple. It is
not. A dicritical `C_l` of `F` (`s_l>=1`) is horizontal for `h=u o F`: `F` maps
`C_l` onto a component of `A_F`, and generic `u` is nonconstant on `A_F`
(Lemma A). The generic fibre meets `C_l` in the `n s_l` source-infinity places
over `L cap A_F`, so `deg(h|C_l)=n s_l >= n >= 3`. Simple type is empty for
noninvertible Keller maps under H2.

**Chau 2010, both components rational.** Chau, arXiv:0804.3172v3 (VJM 42
(2014)), Theorem 2: a Keller map with both coordinates rational is invertible.
If `g_L=0`, both coordinates of a generic target frame are rational, so the
*statement* would close the question. It is **not consumed**. The proof arranges
`deg P < deg Q`, forms `G_F=Q/P`, and infers from a tree dual graph that
`{P=0}` meets `D_infty` in one point (`theta_inf=1`). Two defects: (i) the
degree drop for generic equal-degree coordinates uses Chau's Lemma 1, whose
embedding-of-affine-fibres step is not a genus inequality for compact models;
(ii) unique intersection needs `D_infty` to be the whole connected transform of
`L_infty`, which is the content of the arrangement. First arXiv versions were
withdrawn (Cassou-Noguès). FALLACY-v2: not filled by unrepaired citation.
Chau Section 5 leaves the one-rational-component question open and *suggests*
two polar branches — the equality type of Section 4, not a theorem.

**Nollet–Xavier / Chau 2011.** GAFA 14 (2004), Cor. 1.3, and Ann. Polon. Math.
101 (2011), Theorems 2–3: `F^{-1}(ell)` irreducible rational for *every* line
through a generic `q` implies invertibility. Lines through a fixed `q` still
include tangents to `A_F` and lines through `Sing(A_F)`. The hypothesis is
strictly stronger than generic `L`.

**Negative control.** `f=x(1+x y)` is a submersion (`f_x=1+2xy`, `f_y=x^2`)
with generic fibre `≅ C*` and special fibre `C union C*`. Rational, not a
variable. So “submersion + rational generic fibre ⇒ variable” is false in the
ambient class; `theta_L>=5` and an étale degree-`N` partner are essential.

**Summary of (1).** Every classical kill applies to a type with `theta_L <= 2`
or with all fibres irreducible or with all horizontals of degree 1. The remaining
Keller type, if `g_L=0`, has `theta_L >= 5`, at least one reducible smooth fibre,
and a horizontal of degree `>= n >= 3`. None of the listed theorems excludes it.

## 4. Task (2): Riemann–Hurwitz on `P^1` and existence

Assume `g_L=0`. Then `X_L ≅ P^1` and `C_L ≅ P^1` minus `theta_L` points. The
map `v : C_L -> A^1` extends to a rational function `phi : P^1 -> P^1` of
degree `N`.

**Poles versus punctures.** The charge's phrase “poles are exactly the
`theta_L` places” mixes two sets. As a meromorphic function on `X_L`, `v` has
poles precisely at the `theta_inf` places over `infty_L` (where `v -> infty`).
The remaining `n S` punctures of `C_L` lie over the `n` finite points of
`L cap A_F`: there `v` takes finite values, with ramification indices `mu_l`.
Those `n S` points are *not* poles of `v`. They *are* ramification points of
`phi` (since `mu_l >= 2`). Treating all `theta_L` punctures as poles would force
`n S=0`, contradicting `S>=1`; that is a fallacy, not a proof.

**Riemann–Hurwitz.** A degree-`N` map `P^1 -> P^1` has total ramification
`R=2N-2`. Affine ramification of `phi` is empty (`v` étale on `C_L`). The
contribution over the `n` points of `L cap A_F` is `n(W-S)`. The contribution
over `infty` is `N - theta_inf`. Hence

```text
n(W-S) + (N - theta_inf)  =  2N - 2,
```

which is MF-EXACT at `g_L=0`. Riemann–Hurwitz is tautological on the identity;
it adds the fibre-cardinality bound `theta_inf <= N` already in the typing.

**Admissible numerical types.** Combined with MF-DEFECT, MERIDIAN-FLOOR+,
`n>=3`, `S>=1`, `W-S>=1`:

```text
theta_inf  =  n(W-S) - N + 2,
max(2, W-S+1)  <=  theta_inf  <=  N,
n  >=  max( 3, ceil((N-1)/(W-S)) + 1 ).
```

Desk enumeration (exact integer arithmetic): **no solutions at `N=2`**. For
`N>=3` the list is nonempty. The equality case of both MF-DEFECT and
MERIDIAN-FLOOR+ is attained for every `N>=3`:

```text
W-S=1,   n=N,   theta_inf=2,   S=1,   W=2,   a=N-2,
theta_L = N+2,   cycle type 1^{N-2} * 2^1 over each of n points.
```

This is the `N=4`, `n=4` type flagged by MR:179-182: if the Chau-lane value
`n=4` is attained at `N=4`, `W=2`, then necessarily `(g_L, theta_inf)=(0,2)`.
Further types exist (e.g. `N=3`: `(n, theta_inf)=(3,2)` or `(4,3)`; `N=4`:
also `(5,3)`, `(6,4)`, and `(W-S,n,theta_inf)=(2,3,4)`). The list for each `N`
is finite because `theta_inf <= N` caps `n(W-S) <= 2N-2`.

**THEOREM MF-RATIONAL-N2.** Let `F` be a noninvertible plane Keller map of
geometric degree `N=2` under H2, and let `L` be a generic line. Then `g_L >= 1`.

*Proof.* If `g_L=0` then `theta_inf = n(W-S) <= N=2`, while
`n(W-S) >= n >= 3`, a contradiction. ∎

(Vacuous if the N=2 column is independently empty.)

**Existence, equality case, `N>=3`.** Move the two poles to `0` and `infty`:

```text
phi(z)  =  P(z) / z^m ,    deg P = N,   P(0) != 0,   1 <= m <= N-1.
```

Pole orders `(m, N-m)` contribute `N-2` over `infty`. The equation
`z P' - m P = 0` has degree `N` and misses `0`; generic monic `P` gives `N`
simple finite critical values of type `1^{N-2} * 2^1`, the meridian type of the
equality case. So such a rational function **exists** for every `N>=3` (as a
branched cover, not a Keller realisation).

**Small cases `N=3,4`.** `N=3`: `(n,theta_inf)=(3,2)` (equality) and `(4,3)`
(generic cubic with `infty` regular). `N=4`: equality `(4,2)`; also `(5,3)`,
`(6,4)` at `W-S=1`, and `(W-S,n,theta_inf)=(2,3,4)`. Hurwitz numbers for these
partitions on `P^1` are positive. The equality case already exhibits a solution
for every `N>=3`, so the Hurwitz problem does not exclude `g_L=0`.

## 5. Task (3): the exact remaining obstruction

Since (1)–(2) do not exclude `g_L=0` for `N>=3`, the additional Keller datum
needed is as follows.

If `g_L=0` for a noninvertible Keller map under H2, then `h=u o F` is a
primitive rational polynomial submersion with: (i) generic fibre irreducible of
genus 0 with `theta_L >= 5`, of which `nS` places lie on dicritical horizontals
of degrees `n s_l` and `theta_inf` lie over target infinity; (ii) all affine
fibres smooth, some reducible with components disjoint in `C^2`, `delta>=2`,
and `r_c <= theta_inf` (MD Step 2: every component carries a polar branch);
(iii) not simple type (dicritical horizontal of degree `>= n`); (iv) on every
fibre a holomorphic `v`, étale of degree `N` on the generic fibre onto
`A^1` minus `n` points, with meridian ramification over those points and poles
exactly the `theta_inf` places (equianalytic in the finite value of `h` by MD
Step 1 / Chau 2010 Theorem 4); (v) numerical type in the finite list of
Section 4, cheapest the equality case `(0,2)`, `W-S=1`, `n=N`, `theta_L=N+2`
(Chau 2010 Sec 5's suggested “two polar branches”: a suggestion, not a theorem).

Missing, and not supplied by the rational-polynomial classification: a theorem
that no submersive non-simple rational polynomial with `theta_L>=5` admits an
étale degree-`N` partner with this ramification. NN 2002 classifies only simple
type. Kaliman 1992's “at most one non-section” is not used (Cassou-Noguès
counterexample, non-submersive class). A repair of Chau 2010 Theorem 2 would
close the question in one step; that repair is a separate desk.

## 6. Opens raised, with bounded quantities

```text
OPEN[MF-RATIONAL]  (sharpened, not closed).  Can g_L=0 occur for a
   noninvertible Keller map under H2 and generic L, for some N>=3?
   BOUNDED QUANTITY: g_L in {0,1,...,p_a(D_F)}; if 0, then
   (W-S, n, theta_inf) belongs to the finite list defined by
   theta_inf = n(W-S)-N+2 with max(2, W-S+1) <= theta_inf <= N and
   n >= max(3, ceil((N-1)/(W-S))+1), and theta_L = nS+theta_inf <= D_F.
   The N=2 slice is empty (THEOREM MF-RATIONAL-N2).
   Price of a NO: n(W-S) >= N+1 (identity-level +1). Integer S-known
   floor becomes ceil((N+1)/(W-S)), which exceeds ceil(N/(W-S)) iff
   W-S divides N; at W=2, n_min >= N+1 and C(N) <= N, one unit beyond
   MD's W2-COLUMN. Not a claim that tabulated Phi rises at every cell.
   No cell claimed empty.

Carried unchanged: OPEN[DELTA-AFF-VS-N], OPEN[N-VS-MAPDEG] (upper half),
OPEN[MIN-EMBED-DEGREE], OPEN[ANTICANON-DEFECT]. Not re-raised:
OPEN[MF-DEFECT], OPEN[MULT-VS-BETA].
```

## 7. FALLACY-v2 audit

`n`, `n_min`, `D_F`, `g_L`, `theta_inf`, `theta_L`, `delta`, `S`, `W-S` kept
apart; poles of `v` are not the `nS` dicritical places; S-known floor is not
`MFb`. No exit price; no `charge_basis`. MF-EXACT at `g_L=0` is an identity,
not a Keller attainment. Section 4 functions are branched covers, not
embeddings. Chau 2010 Theorem 2 recorded, not promoted. Nollet–Xavier not
applied to a Zariski-open of lines. Simple-type theorems not applied to
non-simple `h`. Kaliman's “at most one non-section” unused. Enumerator: the
displayed Diophantine constraints; positive control `N=4` equality type
(MR:179-182); negative control `N=2` empty. No `sat()`, no remainder degree,
no `Z(G)=1`, case (A) unused. Had `phi(z)=P(z)/z^m` failed the ramification
count, the output would have been a kill at the equality case only.

## 8. Typed verdict block

```text
LANE              MF-RATIONAL
SCOPE             Keller, noninvertible, H2, case (B). Case (A) EMPTY;
                  A2 untouched; no Z(G)=1. Citations as in Sec 3.

PROVED HERE       (PROVED-HERE, UNREVIEWED)
                  MF-RATIONAL-N2   N=2: g_L=0 is numerically empty, so
                                   g_L >= 1 if such an F exists.
                  MF-RH-EXIST      for N>=3 the equality type
                                   (g_L, theta_inf)=(0,2), W-S=1, n=N
                                   solves every consumed identity and is
                                   realised by phi(z)=P(z)/z^m on P^1.
                  NEVER-SIMPLE     u o F has a horizontal of degree
                                   n s_l >= n >= 3; simple-type theorems
                                   do not apply.

CONSUMED          MF-EXACT at MR-CONFIRMED (S-known vs W-only).
                  MERIDIAN-FLOOR+ at NVR-CONFIRMED
                    (2 g_L + theta_inf >= W-S+1).
                  MF-DEFECT at MD typing (2 g_L + theta_inf >= 2;
                    polar equianalyticity; every component carries a
                    polar branch). 7.B', SMOOTH-KILL, Lemma A, SHARP-CHAU
                    as banked. Coordinator ~11:05Z: respected.

CONTROLS          N=2: no Diophantine solution (Sec 4).
                  N=4 W=2: equality type is MR's (0,2) at n=4.
                  Non-Keller F_m attains (0,1); not étale.
                  Non-Keller x(1+x y): submersion, generic fibre C*,
                  not a variable — ambient class does not force g_L>=1.

NOT CLAIMED       g_L >= 1 for N>=3; any cell EMPTY; any Keller
                  realisation of (0,2) or of phi(z)=P(z)/z^m;
                  Chau 2010 Thm 2 as a theorem in this ledger;
                  +1 to tabulated Phi at every cell; anything about
                  case (A), A2, or Z(G).

OPENS RAISED      OPEN[MF-RATIONAL]  g_L=0 for some N>=3?  Bounded:
                  g_L <= p_a(D_F); if 0 then (W-S,n,theta_inf) in
                  the finite list of Sec 4.  Price of a NO: n(W-S)>=N+1.

SUCCESSOR         Repair or refute Chau 2010 Thm 2; classify submersive
                  non-simple rational polynomials with theta_L>=5 against
                  an étale degree-N partner. Gate unchanged.

DEVIATIONS        Citations with exact location, not from refs/. Desk
                  CAS: python3 Diophantine list, under 1 s. Chau 2010
                  Thm 2 recorded and not promoted.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18425`.
- Body SHA-256:
  `86e9d5fbd1b4c8621ef545d8a2993ee9b8675d0bf02173c1c234dd0d9e567a87`.
- Frozen basis: `c513bcef9863771057803c0e45f9f42e4154f3ef`.
