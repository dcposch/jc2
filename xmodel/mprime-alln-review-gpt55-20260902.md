# Hostile review: MPRIME-ALLN Path-1 all-degree classification

Lane: MPRIME-ALLN-REVIEW  
Model: gpt-5.5  
Date: 2026-09-02  
Report target: 18-28 KB  
Charged inputs:

```text
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.6u044N/inputs/mprime-alln-h2-opus5-20260902.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.6u044N/inputs/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

Both SHA-256 hashes were verified before reading. I label the first file `MI`
and the coordinator integration file `CI`. I also checked the local promoted
source files for `[P5]`, `(M')`, Theorem (E), `[P7]`, and the rank-four census:
`b0-all-n-eta-criticality-sol56-20260831.md`,
`b0-all-n-hostile-review-grok46-20260831.md`,
`round1033-sheet-gate-opus5-20260831.md`,
`round1033-sheet-gate-hostile-review-sol56-20260831.md`,
`n20-escape-kill-opus5-20260901.md`,
`n20-escape-hostile-review-sol56-20260901.md`, and
`block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md`.

## Executive verdict

```text
LEMMA A           CONFIRMED, with dependency note.
SMOOTH-KILL       CONFIRMED.
PROP 6.1          CONFIRMED.
NODAL-ALL-N       CONFIRMED as a necessary numerical gate; no realization claim.
THEOREM PROFILE   CONFIRMED, with B3 kept as an open residual.
CUSP-KILL         CONFIRMED, conditional on the cited classical theorems.
COR 7.2           CONFIRMED.
N4-PIN            CONFIRMED.
Controls          CONFIRMED: three-route (K), R_max spot checks, rank-four census.

Coordinator claim "H2 complete at every degree"    REFUTED / overpromoted.
```

The mathematical classification in `MI` is not an all-degree closure of H2. It
is an all-degree profile reduction with explicit survivors. This is already
stated by `MI`: the H2 branch is "not closed at all degrees" (MI:39-44,
751-758), with four typed OPENs in section 9. By contrast, `CI` says "Under H2
... complete at every degree" (CI:67-73). That coordinator sentence must not be
promoted from the reviewed material. The safe promotion is the profile theorem
plus the typed residuals.

## 1. LEMMA A and the old `[P5]` route

**Verdict: CONFIRMED.**

The old promoted route is genuinely vacuous after Theorem 7.B. The source
`[P5]` theorem is conditional: if an affine-image dicritical has `mu_0=1`, then
`s_0=1`, the dicritical cover is an isomorphism to the normalization, and
`D~ ~= A^1` (`b0-all-n-eta-criticality`:175-192). Its proof uses the
trivial-dicritical hypothesis explicitly at the differential step
(`b0-all-n-eta-criticality`:127-150; review confirmation at
`b0-all-n-hostile-review`:69-85). The coordinator's promoted Theorem 7.B says
the opposite antecedent holds under H2: no affine-image dicritical has `mu=1`
(CI:22-32). Therefore `[P5]` does not supply H3 in the H2/7.B regime. The
vacuity warning in `MI` is real (MI:102-106, 148-156).

Lemma A avoids that route. It uses Orevkov Lemma 2.1 to get, for every
affine-image dicritical, `l ~= P^1` and `l' = l cap Phi^{-1}(A^2) ~= A^1`
(MI:126-129). The local source/review files confirm this as degree-free and not
dependent on H2 or H3 (`b0-all-n-hostile-review`:57-67;
`n20-escape-hostile-review`:100-118). The map `Phi|_l : P^1 -> closure(D_l)` is
a nonconstant morphism of projective curves, hence finite onto its image. Its
restriction factors through the normalization as a finite surjection
`h_l : A^1 -> D~_l` (MI:130-133).

The rationality and one-place-at-infinity argument is sound. The finite
surjection extends to projective completions, so the projective normalization
of `D_l` is dominated by `P^1` and has genus zero. Since `D~_l` is affine and
`h_l(A^1)` lies inside it, every point of the boundary
`bar D~_l - D~_l` must be hit by the single point `infinity` of `P^1`; the
boundary is nonempty and has exactly one point (MI:135-143). Therefore
`D~_l ~= A^1`. Under H2, `A_F` has one component and it is the image of a
dicritical, so H3 follows.

Dependencies consumed: Orevkov Lemma 2.1, finite normalization of curves,
Luroth/Riemann-Hurwitz-level rationality, and the standard fact that components
of `A_F` arise as dicritical images. No use of 7.B, `[P5]`, `(M')`, or any
unreviewed enumeration is hidden in the proof.

## 2. SMOOTH-KILL

**Verdict: CONFIRMED.**

Assume `s=0`. Lemma A gives `D ~= A^1`, so `chi_c(D)=1` (MI:180-182). Because
now `D_0=D`, the sheet-gate covering lemma applies to all of
`E=F^{-1}(D)`, giving a degree-`a` finite topological/algebraic covering over
`D`; hence `chi_c(E)=a chi_c(D)=a` (MI:184-185). Theorem (E) is available at
this scope: it needs the Keller map to be proper and etale over
`A^2-D`, plus compactly supported Euler additivity and finite-covering
multiplicativity (`round1033-sheet-gate`:365-390;
`round1033-sheet-gate-hostile-review`:189-197). No H3-free or smoothness
mismatch is present. The equation gives `1=a` (MI:185-186).

The two Abhyankar-Moh-Suzuki applications are also at their exact scope. First,
`D` is a closed embedded copy of `A^1`, so a target automorphism rectifies it to
`{v=0}` (MI:188-191). With `a=1`, `E -> D` is a degree-one etale cover, hence
`E ~= A^1`; a source automorphism rectifies it to `{x=0}` (MI:191-193). Since
`F` is etale, the pullback of the reduced divisor `{v=0}` is reduced. Its zero
set is `{x=0}`, so `F_2=cx`, and the constant Jacobian forces
`F_1=lambda y+g(x)`, an automorphism (MI:195-201). This contradicts the
standing noninvertibility.

No hypothesis mismatch was found in either challenged step: `chi_c(E)=a
chi_c(D)` uses the covering lemma only after `D_0=D`, and Theorem (E) is a
Keller theorem, not a theorem requiring smooth `A_F`.

## 3. Local law, `(K)`, and Proposition 6.1

**Verdict on Proposition 6.1: CONFIRMED.**

The pointwise law

```text
N - a_p = r_p W + K_p,    K_p >= 0
```

is re-derived in `MI` (MI:222-246), with the only borrowed campaign step being
the already-reviewed "no extra finite `L_C`-fibre points" clause (MI:237-240).
At a smooth point this recovers `[P3]`, `N=a+W` (MI:248-249). Subtracting gives

```text
a - a_p = (r_p-1) W + K_p.                    (L)
```

Summing and comparing with `(M')` gives

```text
sum_p K_p = a - 1.                             (K)
```

The three advertised derivations agree. Route 1 is `(L)` plus `(M'-def)`
(MI:253-258). Route 2 is Orevkov's
`sum_l (mu_l+corr_l)=N-1` after substituting
`corr_l=mu_l(s_l-1)+sum_t k_t` and using the polynomial-map Riemann-Hurwitz
count (MI:258-262). Route 3 is the promoted `ALL-N (4.6)` identity (MI:256,
763-766). Algebraically, Route 2 gives
`W + sum_t k_t = N-1`; since `W=N-a` and the smooth-stratum terms have zero
defect, this is exactly `sum_p K_p=a-1`.

Proposition 6.1 is then immediate. If `s=1`, `(M'-def)` gives
`a-a_p=(a-1)+(r_p-1)W`, so `a_p=1-(r_p-1)W`. With `W>=2` and `a_p>=0`, one must
have `r_p=1` and `a_p=1` (MI:442-450). This is strictly weaker and cleaner than
the old one-node exclusion: a single singular point is forced to be unibranch,
not impossible.

## 4. NODAL-ALL-N and enumeration

**Verdict: CONFIRMED as a necessary numerical gate.**

Under the stated hypothesis that every branch of `A_F` is smooth, a singular
point cannot be unibranch; hence every singular point has `r_p>=2`, and
`beta=0` (MI:340-344). From `(L)`, `a_p>=0` gives
`r_p W <= N`; at multibranch points this implies `2a>=N` and
`K_p <= D_gap := 2a-N` (MI:264-272, 342-345). From localization `(C3)`, at most
`R=sum_l(s_l-1)` points have positive `K_p` (MI:291-295, 345). Combining with
`(K)` gives

```text
a - 1 <= R D_gap.                              (5.3)
```

The 7.B input is exactly the bound on `R`: every `mu_l>=2`, so
`sum_l s_l <= floor(W/2)`, and because `m>=1`,
`R=sum_l(s_l-1)<=floor(W/2)-1` (MI:351-356). Thus the exact integer gate is

```text
a - 1 <= (2a-N) R_max(N-a),
N/2 < a <= N-2,    N-a >= 2.                   (5.4)
```

I independently enumerated (5.4). The first survivors are exactly the table in
`MI`:

```text
N=17: (a,W,D_gap,Rmax)=(11,6,5,2)
N=18: (12,6,6,2)
N=19: (13,6,7,2)
N=20: (12,8,4,3), (14,6,8,2)
N=21: (13,8,5,3), (15,6,9,2)
N=22: (14,8,6,3), (16,6,10,2)
N=23: (13,10,3,4), (15,8,7,3), (17,6,11,2)
```

The clean bound `R <= W/2-1` gives (5.5):

```text
N(D_gap-2) >= D_gap^2 + 6D_gap - 4.
```

For `D_gap=1,2` it is impossible; for `3,4,5,6,7,8` it gives thresholds
`23,18,17,17,18,18`, and parity removes `D_gap=6` at `N=17` (MI:363-374).
This proves no all-smooth-branch case below `N=17`.

I also checked `R_max(W)` directly from its definition by dynamic programming
over profiles `(s_i,mu_i)` with `s_i>=1`, `mu_i>=2`, and
`sum s_i mu_i=W`:

```text
W=5:  Rmax=0, profile (1,2)+(1,3)
W=6:  Rmax=2, profile (3,2)
W=9:  Rmax=2, profile (3,2)+(1,3)
W=15: Rmax=5, profile (6,2)+(1,3)
```

These match the formula in `MI`: even `W` gives `W/2-1`; odd `W` gives
`max(W/p_min(W)-1,(W-5)/2)` (MI:354-356). No floor/attainment error was found:
the table is a table of numerically admissible data, not a witness table.

The `N<=7` part is genuinely 7.B-free. If 7.B is withdrawn and `mu=1` is
allowed, the exact maximum becomes `R=W-1`; enumerating the weakened inequality
has no solution for `N<=7` and first survives at
`(N,a,W,D_gap,R)=(8,5,3,2,2)`, exactly as `MI` states (MI:396-399).

## 5. THEOREM PROFILE

**Verdict: CONFIRMED, with a promotion guard.**

The case split is exhaustive and disjoint:

```text
(0) D smooth.
(A) D singular and every singular point is unibranch.
(B) D has a multibranch point.
```

Inside (B), either every branch is smooth, or at least one branch is singular.
If every branch is smooth, this is (B1). If a singular branch exists and there
is no unibranch singular point, this is (B2). If a unibranch singular point also
exists, this is (B3). These alternatives do not overlap (MI:413-430).

The (B2) enumeration is consistent with the same inequality but with the
localization count degraded from `R` to `R+beta`:

```text
a - 1 <= (R_max(W)+beta)(2a-N).
```

Independent enumeration gives minimal admissible `beta`: none for `N<=4`, `2`
for `5<=N<=10`, `1` for `11<=N<=16`, and `0` at `N>=17`, matching MI:432-436.
This is only a necessary numerical allowance; it does not construct a profile.

The B3 collapse is correctly limited. At a cusp the multibranch ceiling
`K_p<=D_gap` is unavailable, and `(K)` only gives `K_cusp<=a-1`; one cusp can
carry the whole excess in the inequality bookkeeping (MI:428-438). I found no
downstream step that smuggles in a stronger general B3 conclusion. Section 8
uses special `N=4` facts (`W=2`, `R=0`, `s_1=1`) to prove uniqueness of the
singular-branch point; section 9 keeps B3 open for the general horn (MI:626-651,
704-712). That is the right scope boundary.

Promotion guard: the theorem profiles H2; it does not close H2. The report's
OPEN list remains part of the theorem package.

## 6. CUSP-KILL and Corollary 7.2

**Verdict on CUSP-KILL: CONFIRMED, conditional on Lin-Zaidenberg and Campbell.**

In case (A), Lemma A gives `D~ ~= A^1`. Since every point of `D` is unibranch,
the normalization map is bijective; as a finite morphism it is proper, hence a
homeomorphism on complex points. Thus `D` is an irreducible plane curve
homeomorphic to `C` (MI:483-490). The cited Lin-Zaidenberg theorem has exactly
the needed form: an irreducible affine plane curve homeomorphic to `C` is taken
by an automorphism of `C^2` to `{x^p=y^q}` with `gcd(p,q)=1`; smooth-kill rules
out `p=1` or `q=1` in this singular case (MI:491-494). No rational-cuspidal
classification stronger than Lin-Zaidenberg is being imported.

Assume `E=F^{-1}(D)` is irreducible. Then `E_0=F^{-1}(D_0)` is a connected
finite etale cover of `C^*`, hence is `C^*` (MI:507-518). The unique point over
the cusp has the same analytic type as `(D,p)` because `F` is a local
biholomorphism. Therefore the normalization of `E` is `C^*` with one point
filled, i.e. `A^1`, and `E` is also homeomorphic to `C` (MI:516-520).
Lin-Zaidenberg applies to `E`; the local analytic type identifies the unordered
pair `{p',q'}` with `{p,q}`, so
`pi_1(C^2-E) ~= G_{p,q}` (MI:520-523).

The group-theoretic kill also checks. Let
`G=G_{p,q}=<alpha,beta | alpha^p=beta^q>`, `Z=<z>`, and let
`H=pi_1(C^2-E)` be the index-`N` subgroup from the etale complement cover
(MI:496-505). Put `Z_H=Z cap H` and
`Delta=H/Z_H ~= HZ/Z <= G/Z`. Because
`G/Z ~= Z/p * Z/q` is nonelementary virtually free and has nonzero rational
Euler characteristic, the centralizer of a finite-index subgroup is trivial.
Thus `Z(H)=Z_H`, and `Delta ~= H/Z(H) ~= Z/p * Z/q`. Multiplicativity of
rational Euler characteristic gives
`chi(Delta)=M chi(G/Z)` but also `chi(Delta)=chi(G/Z) != 0`; hence `M=1`.
So `HZ=G`, and because `Z` is central, `H` is normal in `G` (MI:524-532).

A normal connected finite etale complement cover is a Galois cover of degree
`N`, and since it is the etale locus of the generically finite Keller map, the
function-field extension `C(x,y)/C(F_1,F_2)` is Galois. Campbell's cited theorem
is exactly the needed classical input: a Keller map with Galois function-field
extension is invertible (MI:531-533; cited in the sheet gate at
`round1033-sheet-gate`:174-176). Therefore the irreducible-`E` cusp case is
impossible for a counterexample.

I did not reprove Lin-Zaidenberg or Campbell from primary papers in this lane;
the verdict is "confirmed against exact consumption", not "classical theorems
byte-verified". If either external theorem is not allowed as input, the cusp
horn reverts to GAP at precisely this dependency.

**Verdict on Corollary 7.2: CONFIRMED.**

For any Keller counterexample, the complement map
`C^2-F^{-1}(A_F) -> C^2-A_F` is connected finite etale of degree `N`. If its
subgroup `H` were normal, the cover would be Galois and the same extension
argument plus Campbell would force invertibility (MI:554-558). Therefore `H`
is non-normal. Equivalently the monodromy permutation group is transitive but
not regular: for a connected degree-`N` covering, a normal subgroup gives a
regular transitive image of order `N`; non-normality gives a nontrivial point
stabilizer in the monodromy image, hence order `>N` (MI:560-563).

## 7. N4-PIN and rank-four control

**Verdict: CONFIRMED.**

For `N=4` with a multibranch point, `(C1)` gives `2a>=4`, while the sheet-gate
ceiling gives `a<=N-2=2`; hence `a=2`, `W=2`, and `D_gap=0` (MI:595-596).
Theorem 7.B gives every `mu_l>=2`, so the weight equation forces one dicritical
`(s_1,mu_1)=(1,2)` and `R=0` (MI:596-597). From `(K)`,
`sum K_p=1`. At a multibranch point, `K_p<=D_gap=0`; then
`a_p=4-2r_p>=0` forces `r_p=2`, `a_p=0` (MI:597-600).

Since `R=0`, any positive `K_p` must come from a singular branch by Lemma 4.2.
Because `s_1=1`, Lemma 4.3 says every singular-branch point has `K_p>=1`.
With total budget `1`, there is exactly one such point `p_0`, with `K=1`
(MI:600-603). At that point
`a_p=4-2r_p-1>=0`, so `r_p=1` and `a_p=1` (MI:603-604). All other singular
points are double points of two smooth branches, with `a_p=0`, `K_p=0`.

The cycle types read off from the same local law:

```text
generic point of A_F:       two affine fixed sheets plus one boundary 2-cycle -> (2,1,1)
cusp p_0:                  one affine sheet plus one boundary 3-cycle        -> (3,1)
each double point:          two boundary 2-cycles, no affine sheet            -> (2,2)
```

Finally, if `k` is the number of double points, then `nu=k`; Lemma A gives
`chi_c(A_F)=1-k`, and Theorem (E) gives
`chi_c(F^{-1}(A_F))=1-4k` (MI:591-605). At `k=1`, this reproduces exactly the
promoted rank-four census:

```text
generic B: (2,1,1), cusp c: (3,1), omitted node n: (2,2), e(T)=-3
```

The source census states those four numbers with `B` irreducible and
normalization `A^1` (`block-descent-a1-one-cusp-wild-valuation-structure`:387-395).
`MI` reproduces them without consuming that census as input (MI:607-620). This
is a strong consistency control, not a new proof that `k=1` in every horn;
`MI` correctly says `k` is not pinned by `(M')` alone (MI:638-641).

## 8. FALLACY-v2 audit

No new exit-price assertion is made in this review, so no `charge_basis` line
is required.

Flag/place/series: The reviewed proof keeps source points `t in l'`,
normalization places `h_l(t)`, physical singular points `p`, and cover series
orders `mu_l`/`mu_t` separate. The crucial count in Lemma 4.1 is per source
point and only then pushed to physical points via `eta^{-1}(p)` (MI:222-246).

Carrier/attainment and floor/attainment: `R_max(W)`, `beta`, and the `(5.4)`
tuples are upper allowances. The review found no claim that the `N=17` cell is
realized; it is only the first numerical survivor.

Pole/interior: The pole identities are used only after Orevkov's affine
dicritical setup has removed the point over infinity. The review did not find
an at-infinity point counted as a finite critical point.

Variable/ring map: The `Y`-picture and Orevkov picture are related through
valuations and residue fields in Lemma 1.1 (MI:65-80), not through matching
names. That is enough for `e_j=mu_l` and `delta_j=s_l`.

Prime label/derivative: `l'` is a punctured dicritical, not a derivative. The
report uses `D_gap=2a-N` to avoid clashing with geometric degree `N`.

No `sat()` wrapping, raw remainder degree, or merge-free/M-descent argument is
used here.

## Final promotion recommendation

Promote the following, with the stated scopes:

```text
LEMMA A: H3 follows from H2 by the dicritical A^1-to-normalization argument.
SMOOTH-KILL: irreducible A_F is singular.
PROP 6.1: s=1 implies the point is unibranch and a_p=1.
NODAL-ALL-N: all branches smooth implies N>=17; N<=7 part is 7.B-free.
THEOREM PROFILE: (0)/(A)/(B1)/(B2)/(B3), with B3 open.
CUSP-KILL and COR 7.2: conditional on Lin-Zaidenberg and Campbell.
N4-PIN: rank-four residual pinned as in MI section 8.
```

Do not promote `CI`'s "H2 complete at every degree" sentence. The reviewed
classification explicitly leaves the cusp horn and other singular-branch
residuals open; routing downstream work as if H2 were closed would be a
misread of the charged proof.

<!-- BODY-END -->
