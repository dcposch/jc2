# Hostile combined review: AS F-only `p=3,D=7` D7 source license and 13-component cap boundary

Different-model hostile review (Claude, 2026-08-24) of the conjunction of two
frozen targets.  Both are required together; the verdict below is for the
conjunction at its exact frozen scope.

| Item | Value |
| --- | --- |
| Target 1 | `xmodel/as-fonly-d7-vertical-d7-cap-boundary-20260824.md`, SHA-256 `3576de6cfba306230477fe7955e2ae159cc3dd241b4613b96d0ff57a05bbbfad` |
| Target 1 case | `cases/as_fonly_d7_vertical_d7_cap_boundary_20260824/`, manifest `5dfd46d47b27fb6d9bc094b24389ef39255e6a073fc7ef09ab8941b30ff49f65`, freeze `91a5c0a947d32287abb6223f41ceb385aaee4744e666e21748f77ae9ec70827a` |
| Target 2 | `xmodel/as-fonly-d7-vertical-d7-source-license-20260824.md`, SHA-256 `772d3627965037846f291ca5289c3cab26375e7bcea9edb095a95381fed84b27` |
| Target 2 case | `cases/as_fonly_d7_vertical_d7_source_license_20260824/`, manifest `7c23f45df72ec3cdbf7ff75ebeda50281fe140d0fe346277801873560f73135c`, freeze `bc1c126701bf8741e5d4171726c13d414a52bf462fe0d540e44d1947605a5a38` |
| Smallest false identity | none found |
| Smallest missing hypothesis | the stratified support argument silently identifies the `F3(h)` minimal primes with all components meeting `h!=0`; closed by the reviewer-supplied quasi-homogeneity lemma in Section 4, provable from the frozen rows alone — non-blocking |
| Overall verdict | **CONFIRMED** (conjunction, exact frozen scope) |

## 0. Execution capability and method

This review session had no shell: `Bash` is absent and `Monitor` is
permission-denied.  I therefore could not run the two manifests, the two
portable replays, the Singular scripts, or any `shasum`.  Per the registered
protocol for shell-less review sessions, the verdict rests on (i) full
byte-level inspection of every program in both cases and of the consumed
generator chain, (ii) independent hand algebra reproving the displayed
identities, (iii) the frozen attestation web (FREEZE, EXPECTED, manifests,
upstream reviews), whose internal consistency I checked exhaustively.
Section 6 lists exactly which items rest on frozen attestations rather than
re-execution, and a staged script
`/tmp/verify-as-d7-cap-boundary-combined-20260824.sh` closes every such gap
on any shell-enabled session.  Programs were inspected, not trusted for PASS:
every runtime `assert` in all five replay programs was traced and its
mathematical content independently justified or refuted below.

Files read in full: both target reports; both FREEZE, MANIFEST,
EXPECTED_OUTPUT_SHA256, README; `audit_full_e1_degree7.py`;
`audit_d7_source.py`; `audit_d7_joint.py`; `audit_hgeneric_minass.sing`;
`audit_hzero_minass.sing`; `audit_boundary_containment.sing`;
`OPTIONAL_FULL_MINASS.md`, `run_optional_full_minass.sh`, the three optional
`.sing` runners; both `replay_all.sh`; the consumed
`generate_corrected.py` and `generate_degree10_gate.py`; the consumed
state-sufficiency report; the consumed corrected D9/D8 source review.

## 1. Full integer source at order 27 (prompt point 1)

**Expansion identity.** I re-derived by hand, from
`Pmap=x-x^3+3U+9C`, `Qmap=y+3V+9D`:

```text
det J-1 = 3(U_x+V_y-x^2) + 9[C_x+D_y+K] + 27M + 81N,
K=(U_x-x^2)V_y-U_yV_x,  N=C_xD_y-C_yD_x,
```

so `(det J-1)/27 = E/3+M+3N` with `E=L/3+K+C_x+D_y`, `L=3L1` — identity (1)
of the license is exact.

**Charged divisibility.** In the charged vertical normal form
(`U0=h x^2y+p y^4+2r xy^3+q x^3y+2t x^4`,
`V0=2h xy^2+x^2y+r y^4+s xy^3+t x^3y+w x^4`, no degree-five layer),
`L = 6h·xy+6r·y^3+3q·x^2y+3s·xy^2+9t·x^3+3fa·x^2y^3+6fb·x^5+6fc·y^5+3fd·x^3y^2`
by direct differentiation — every coefficient divisible by 3, so `L1=L/3`
exists formally with `deg L1<=5`.  Verified against the program assertions.

**Degree caps (4).** `deg(C_x+D_y)<=6` is immediate from `deg C,D<=7`.
`deg K(U0,V0)<=6` holds because `A0=U0_x-x^2` and all four base derivatives
have degree at most 3.  All three caps are asserted at runtime in the license
program and reproven here by hand.

**Frobenius divisibility.** Every exponent in
`UF=fua·y^6+fa·x^3y^3+fb·x^6`, `VF=fc·y^6+fd·x^3y^3+fv·x^6` is `0 mod 3`, so
every first derivative has all coefficients divisible by 3; the divided
derivatives are `UF_x/3=fa·x^2y^3+2fb·x^5`, `UF_y/3=2fua·y^5+fa·x^3y^2`,
`VF_x/3=fd·x^2y^3+2fv·x^5`, `VF_y/3=2fc·y^5+fd·x^3y^2` — matching lines
275–278 of the frozen generator exactly.  The double-Frobenius bracket
`UF_x·VF_y-UF_y·VF_x` is `9·(homogeneous degree 10)`, hence divisible by
nine, hence zero mod three after one division — as asserted.

**Degree-seven completeness.** `[E]_7=[K]_7` (the three caps kill the rest);
`[K]_7=[K_single]_7` (`[K0]_7=0` by the cap, `K_double` is homogeneous of
degree 10); `3|[K]_7` formally.  Hence `[E1]_7` is well defined before any
gate and equals the single-Frobenius `[K/3]_7`.  This is a genuine degree
argument about the full integer source, not an extrapolation of the D9/D8
generator: the license program builds `E1_7`, `M`, `M0` from its own integer
polynomials and touches the frozen generator only afterward, as a regression.
I confirmed the cap-boundary case alone would not have licensed this (its
`audit_d7_source.py` never bounds `deg K0`), so the conjunction requirement
is real and correctly enforced.

**Hand recomputation of the raw degree-7 Frobenius row.** I fully expanded
`[K_single/3]_7 =
(UF_x/3)·[V0_y]_2+[A0]_2·(VF_y/3)-(UF_y/3)·[V0_x]_2-[U0_y]_2·(VF_x/3)`
by hand.  Mod 3, the eight monomial coefficients are

```text
y^7: 2·fua·h;  xy^6: fc·h+2·fua;  x^2y^5: fc;  x^3y^4: 2·fa·h;
x^4y^3: 2·fa+fd·h;  x^5y^2: 2·fd;  x^6y: 2·fb·h;  x^7: 2·fb+fv·h.
```

Rows `y^7, xy^6, x^2y^5, x^5y^2` match the displayed rows (3)/(4) with no
`M`-contribution, and the remaining rows match after the registered digit
substitutions contribute exactly `d6_1`, `Rr+fa`-cancellation, `d6_4`, and
`Tt+2fb` respectively — the latter bookkeeping is machine-asserted twice from
two independent constructions (`assert actual == predicted` in both audit
programs, frozen PASS), and is consistent with my raw expansion in every
independently computable coefficient, including all signs.

**Internal hashes.** `canonical_hash` is a deterministic serialization
(sorted monomials, canonical JSON).  The values
`c5e95b5e…` (`[E1]_7`) and `4cf87c8c…` (`[E1+M]_7`) are quoted identically in
the license report and the license FREEZE.  I cannot recompute SHA-256
without a shell; recomputation is staged.  No inconsistency exists anywhere
in the frozen web.

## 2. The eight D7 rows and forced substitutions (prompt point 2)

**Substitution chain audited byte-by-byte.**
`normal` (accepted rows) pins `u3_2=h, v3_1=2h, v3_2=1, u4=(p,2r,0,q,2t),
v4=(r,s,0,t,w), u5=v5=0` — identical to the `U0,V0` hard-coded in both audit
programs.  I re-derived by hand all seven entries of the order-9 degree-6
pivot dictionary `sub` (`c7_1=-k6[0]-d7_0`, `c7_2=k6[1]`, `d7_2=k6[2]`,
`c7_4=-k6[3]-d7_3`, `c7_5=k6[4]`, `d7_5=k6[5]`, `c7_7=-k6[6]-d7_6`) from
`[E]_6=[K0]_6+C7_x+D7_y` with the mod-3 derivative coefficients
`(1,2,2,1,2,1,1)·(c7_1,c7_2,d7_2,c7_4,c7_5,d7_5,c7_7)` — exact match.
Likewise all six `sub6` pivots (`c6_1,c6_2,d6_2,c6_4,c6_5,d6_5` with unit
constant coefficients `1,2,1,1,2,1`) from `[E]_5=L5+[K0]_5+C6_x+D6_y`, where
`L5=fa·x^2y^3+2fb·x^5+2fc·y^5+fd·x^3y^2` is exactly the hand-computed
degree-5 part of `L/3`.  The D8 `pivot_sub` asserts each pivot coefficient is
the exact constant `{():1}` before solving; `coord`
(`r=Rr+sh, t=Tt+wh, p=Pp+Rr·h+2s·h^2, q=Qq+Tt·h+2w·h^2`) is triangular and
invertible.  **No division by any ring variable — in particular by `h` — and
no radical occurs anywhere in the chain.**

**The forced deductions.** From the eight rows, ideal-theoretically over
`F3` (not merely pointwise over a field): `(fc)` gives `fc=0`; then
`(fc·h+2fua)` gives `fua=0`; `(2fd)` gives `fd=0`; then `(Rr+fd·h)` gives
`Rr=0`; `2·fua·h` becomes redundant; `d6_1+2fa·h`, `d6_4+2fb·h`,
`Tt+fb+fv·h` solve `d6_1=fa·h`, `d6_4=fb·h`, `Tt=-(fb+fv·h)` with unit
coefficients.  The eliminated block is unit-triangular, so the substitution
is an exact scheme isomorphism onto the eleven-variable joint scheme —
justifying both (1) of the report and the "original ideal, not radical"
claim.  The `forced` dictionary in `audit_d7_joint.py` implements exactly
this (with `2=-1` conventions all correct).

**Negative control.** Omitting the divided Frobenius source while keeping
all later substitutions changes all eight rows (`changed == [0..7]`
asserted, frozen PASS); consistent with my raw expansion, which puts a
nonzero Frobenius term in every row.

## 3. Reconstruction of the seven D8 equations (prompt point 3)

`audit_d7_joint.py` rebuilds the seven core equations at run time from the
frozen generator's `core_matrix`, `core_rhs`, `remaining_vars`
(`d7_1,d7_4,d7_7,d6_1,d6_4`) by the identity `row = rhs + Σ coeff·var`,
which is exact by construction regardless of representation; the displayed
(5) is asserted equal to the reconstruction after the forced substitutions.
So (5) is source-linked, not a hand transcription.  Two independent
structural cross-checks I performed:

- The X-columns of (5) are exactly the state-sufficiency theorem's matrix:
  rows `e0..e3` carry the staggered `-(P+Qz)` convolution block and rows
  `e4..e6` the `-h^3·Id` block of `M(X,Y)=(-A·X+B·Y, -H·X-A·Y)` after the
  forced `Y=(fa·h, fb·h)` — matching the independently CONFIRMED `7 x 5`
  displayed core.
- Every term of (5) as displayed in the report matches the `predicted` list
  in `audit_d7_joint.py`, coefficient by coefficient (checked all 13 terms
  of `e2`, and note `fa·fb^2+2fa·fb·fv·h+fa·fv^2·h^2 = fa·(fb+h·fv)^2`).

No division by `h` and no radical is used to form (5).

## 4. Stratified support proof (prompt point 4) — the sharpest attack

**The h=0 fibre: completeness reproven by hand, independently of Singular.**
Setting `h=0` and clearing units, the fibre ideal is
`F=(Pa, Pb+Qa, Pc+Qb+2fa·fb^2, Qc, fa·s, fa·w)` with `a=X0+fa·s`,
`b=X1+fa·w+fb·s`, `c=X2-fb·fv+fb·w`.  On the `fa∈p` branch, the four
convolution generators are the coefficients of `(P+Qz)(a+bz+cz^2)`, and since
the coordinate ring of any irreducible component is a domain, the product
vanishes iff `P=Q=0` or `a=b=c=0`: exactly `H5` and `H1`.  On the `fa∉p`
branch, `s,w∈p`, and the four subcases on membership of `P,Q` yield exactly
`H6` (`P,Q∈p` forces `fb∈p`), `H4` (`P∈p,Q∉p`), `H3` (`Q∈p,P∉p`), `H2`
(`P,Q∉p` forces `X0,X1,X2-fb·fv,fb∈p`).  I verified `F⊆Hi` for all six,
primality of each (e.g. `H3` is `(5 linears)+(g)` with `g` linear and
primitive in `X2`; `H4`'s seven-generator display is the six-generator prime
plus the redundant `Q·fv·X1-fa·fb·X2 = fv·(QX1-fa·fb^2)-fa·fb·(X2-fb·fv)`;
`H1`'s third generator equals `-(s·gen4-(w-fv)·gen5)`), pairwise
incomparability (all 30 pairs), and the dimensions `6,4,4,4,7,5` by explicit
quotient rings.  **The six displayed fibre primes are therefore the complete
minimal-prime list of the fibre as a theorem, not merely a Singular output.**

**The h-generic base: elimination reproven by hand.** Over `F3(h)`, rows
`e4..e6` solve `X0=fa·s`, `X1=fa·w+fb·s+fv·h·s+2fa·s·h^{-3}`,
`X2=2fa·w·h^{-3}+2fb·fv+fb·w+2fv^2·h+fv·h·w` uniquely; substituting into
`e0..e3` I reproduced all four generators of `audit_hgeneric_minass.sing`
term-by-term, including every `h^{-3}` coefficient and sign.  The count
eight with dimensions `3^6,4^2` and the identification of the two
dimension-four primes as `(s,fa,fv-w)` and `(s,w,fb+h·fv)` are asserted by
the script (two-way Gröbner reduction, `seenG6=seenG8=1`) and attested by the
frozen output hash; completeness of this list is the one decomposition I
could not reproduce by hand (Section 6).

**Graph closures.** On `(s,fa,fv-w)` and `(s,w,fb+h·fv)` the solved `X`
vanishes identically (hand-checked: e.g. on `G8loc`,
`X2=2fb·fv+2fv^2·h=2(-h·fv)fv+2fv^2·h=0`), so the closures are the primes
`G6=(s,fa,fv-w,X0,X1,X2)` and `G8=(s,w,fb+h·fv,X0,X1,X2)`, both prime
(polynomial quotient rings), both of global dimension 5, and `I⊆G6`, `I⊆G8`
(hand-expanded; the cancellations are `3P·fb·w+3P·w^2·h≡0` type).  The six
dimension-3 primes closures have global dimension 4.  `H2` restored is
exactly the fibre of `G8` (`fb+h·fv ≡ fb mod h`), so `H2` is not globally
minimal — hand-verified and script-verified.

**The sharpest attack found, and its resolution.** The frozen argument
identifies "the `h!=0` localized components" with the eight `F3(h)` minimal
primes.  `F3(h)` is the localization at *all* nonzero polynomials of
`F3[h]`, so a hypothetical component of `V(I)` contained in `{h=c}`, `c≠0`
(an `F3`-prime containing an irreducible `f(h)≠h`) would be invisible both
to the `F3(h)` computation and to the `h=0` fibre computation, and would be a
fourteenth component.  No frozen byte addresses this.  **It is, however,
provable from the frozen rows alone:** assign weights
`(h,P,Q,s,w,fa,fb,fv,X0,X1,X2)=(1,9,6,7,4,8,5,4,15,12,9)`.  I checked every
monomial of every row: `e0,…,e6` are quasi-homogeneous of weights
`24,21,18,15,18,15,12`.  Minimal primes of a graded ideal are graded; a
graded prime `p` with `p∩F3[h]≠0` contains some `f(h)≠0`, hence (distinct
powers of `h` having distinct weights) contains a monomial `c·h^i`, hence
`h`.  So every minimal prime of `I` either contains `h` or is `h`-dominant:
no vertical components at `h=c≠0` exist, and the `F3(h)` list is exactly the
set of components meeting `h≠0`.  This closes the hypothesis; it is a
missing sentence in the writeup, not a false claim.

**Containment logic (all hand-verified).** The polynomial ring is catenary,
so strict prime containment forces strict dimension drop; equality of a
closure with a fibre-supported prime is impossible since `h` lies in one and
not the other.  Hence: no closure (dim ≤ 5) can be strictly contained in
`(H1,h),(H5,h),(H6,h)` (dims 6,7,5) — so those three are minimal; `H3,H4`
(dim 4) could only sit inside the two dim-5 closures, excluded by the
nonzero remainders (`fa∉H3`, `fb∉H3`, `fa∉H4`, `fb∉H4` — hand-checked, and
the script checks the full generator sets both ways); dim-4-in-dim-4 is
excluded by catenary strictness.  An irreducible set in a finite union lies
in one member, so the support decomposition
`V(I)=⋃(8 closures)∪V(H1)∪…∪V(H6)` yields exactly the maximal members:
**thirteen components, dimension histogram `4^8, 5^3, 6^1, 7^1`** — with
`4^8 = 6 closures + H3 + H4`, `5^3 = G6 + G8 + H6`, `6^1 = H1`,
`7^1 = H5`.  Arithmetic and logic check completely.  No embedded or
nonreduced structure is misreported: `minAssGTZ` output is used only as
support; both reports state explicitly that the seven-row ideal is not
replaced by its radical.

## 5. Literal-F3 census (prompt point 6)

Program logic audited: the matrix/rhs affine model is validated per-state by
an independent brute force over all 27 `X` values for every one of the 6561
bases (`assert direct == 3^(3-ra) if compatible else 0`), so the census
cannot be wrong unless the seven rows themselves are wrong.  Independent
hand results:

- `rank A ∈ {0,3}` always: for `h≠0` rows `e4..e6` are `2h^3·Id`; at `h=0`
  the X-matrix is the staggered `P,Q` block, rank 3 unless `P=Q=0`, rank 0
  then.  So `(0,0)+(0,1)` must total `3^5=243` — and `87+156=243`.
- Rank-0 compatibility at `h=0,P=Q=0` is exactly `fa·fb^2=fa·s=fa·w=0`, i.e.
  `fa=0` or `fb=s=w=0`: `81+9-3=87` states, hand-proven, matching (12) and
  the code's `81+6` disjoint variant; these are precisely the `F3` footprints
  of `H5` and `H6`.
- `(3,3)+(3,4)=6318=6561-243`; compatible `=87+1158=1245`; points
  `=87·27+1158=3507`; `h`-splits `831+207+207=1245`,
  `3093+207+207=3507` with `3093=87·27+744`; the 207/207 at `h=1,2` are
  consistent with unique-`X` compatibility on the localized variety.
- Projection histogram: 243 keys, weighted sum
  `44+8+72+40+28+576+132+150+108+1944+405=3507` — exact.
- Controls: I evaluated all four representatives by hand through the eight
  source rows and seven joint rows.  The 3-fibre point passes with
  `T+fb+fv·h=1+2+0≡0`; the 9- and 729-fibre points pass trivially; the
  81-fibre point fails the last row with value exactly `1` and satisfies the
  other seven — "fails exactly (14)" is correct, and the gate is a one-row
  shrink, not empty.
- Literal-`F3` counting is never conflated with closure geometry in either
  report; the explicit disclaimers are present and respected.

Stream hashes (`b37698c1…`, `bfb2b6bd…`) are deterministic by construction;
values attested, recomputation staged.

## 6. Items resting on frozen attestations (execution gaps)

Unverifiable in this shell-less session, all staged in
`/tmp/verify-as-d7-cap-boundary-combined-20260824.sh`:

1. All SHA-256 values: the two report hashes, two manifest hashes, the two
   freeze self-hashes (`91a5c0a9…`, `bc1c1267…` appear only in the
   registered review prompt), the five cap-boundary and one license replay
   output hashes, the two census stream hashes, and the two internal `E1`
   hashes.  Every hash that appears in more than one frozen byte was checked
   for mutual consistency; zero discrepancies.
2. The two replays' PASS lines (attested `FULL PORTABLE REPLAY PASS` in both
   FREEZE files, backed by the output-hash pinning above).
3. Completeness of the `F3(h)` `minAssGTZ` list (count 8, dims `3^6,4^2`)
   and the identities of the six dimension-3 base primes, which no frozen
   byte displays (they live in the hash-pinned `hgeneric` output).  The
   fibre decomposition, by contrast, is fully reproven by hand here.
4. The consumed generator chain (`generate_corrected.py`,
   `generate_degree10_gate.py`) is outside the two target manifests; its
   integrity is protected indirectly (any drift changes the deterministic
   replay outputs) and by its own frozen case.

## 7. Optional runners and scope (prompt points 5 and 7)

The three eleven-variable `minAss` runners encode the byte-identical seven
generators (verified against `audit_boundary_containment.sing` and the joint
audit), carry the preregistered discriminator (count 13, histogram
`4^8,5^3,6^1,7^1`, per-component source containment), are excluded from
`replay_all.sh`, and are consumed nowhere: FREEZE says "Timeout/OOM is no
verdict; disagreement quarantines".  The stratified proof stands without
them, as required.  Both reports and both freezes carry exact refusal
scopes: one D7 carry checkpoint; no next carry, no recurrent bounded state,
no all-depth lift/no-lift, no characteristic-zero map, no counterexample, no
JC2 conclusion; census literal-`F3` only; support only, no radical
replacement.  The consumed upstream verdicts are quoted accurately: the
corrected D9/D8 source review is CONFIRMED with degree seven explicitly
excluded ("the smallest honest unexamined successor row"), and the
state-sufficiency review is CONFIRMED at the displayed-matrix tier.  No
smuggled claim was found in any frozen byte.

## 8. Failed attacks (summary)

Order-27 expansion; `L/3` divisibility; the three degree caps; double-
Frobenius mod-9 vanishing; complete hand expansion of `[K_single/3]_7`
(all eight rows, all signs); triangularity and `h`-division-freedom of every
substitution layer (`normal`, `sub`, `sub6`, `pivot_sub`, `coord`, D7
`forced`); scheme-exactness of the D7 elimination; term-by-term match of
(5); hand re-derivation of the four `F3(h)` generators; complete hand
decomposition of the `h=0` fibre (six primes, dims, incomparability);
`H2`=fibre(`G8`); `I⊆G6,G8` with the mod-3 cancellations; all
containment/dimension steps; census arithmetic identities (`87`, `156`,
`6318`, `1245`, `3507`, `h`-splits, histogram sums); all four controls; the
81-fibre single-row failure value `1`; mod-3 semantics of every helper
(`norm`, `eadd`, `emul`, `derivative` with `n%3` skip, `esubstitute`,
linear-only `coefficient` use, Gaussian `matrix_rank_mod3`, `eval_expr`);
determinism of `canonical_hash`; cross-file hash web.  Every attack failed:
no false identity exists in the frozen conjunction.

## 9. Smallest missing hypothesis and promotable sentence

**Smallest missing hypothesis.** The frozen stratified argument nowhere
states or proves that no component of the joint scheme is supported inside
`{h=c}` for `c≠0`, which is needed to equate the `F3(h)` decomposition with
the full `h≠0` localization.  It is true, with the one-paragraph proof in
Section 4 (quasi-homogeneity under weights `(1,9,6,7,4,8,5,4,15,12,9)` plus
gradedness of minimal primes), checkable from the displayed rows alone.  No
numbered claim of either target fails; the omission is non-blocking.

**Exact promotable sentence.** Subject to the frozen replay attestations
enumerated in Section 6, the conjunction of the two targets proves exactly
this and no more: in the charged vertical `p=3,D=7` F-only normal form, the
full integer order-27 residual `(det J-1)/27=E1+M+3N` with
`3E1=E=L/3+K+C_x+D_y` has total-degree-seven part exactly
`[M]_7+[single-Frobenius K/3]_7` (because `deg(L/3)<=5`, `deg(C_x+D_y)<=6`,
`deg K(U0,V0)<=6`, and the double-Frobenius bracket is divisible by nine),
whose eight rows after the registered accepted-row, D9/D8-pivot, and
triangular-coordinate substitutions force `fua=fc=fd=R=0`, `T+fb+fv*h=0`,
`d6_1=fa*h`, `d6_4=fb*h`; the reviewed D8 core thereby becomes the displayed
seven-row original ideal in `(P,Q,s,w,h,fa,fb,fv,X0,X1,X2)`, whose literal-F3
census is `1245/6561` compatible states and `3507` compatible digit points
with the displayed rank table, `h`-slices, rank-zero description, projection
histogram, and representative controls (a one-row shrink), and whose
geometric support has exactly thirteen global minimal components with
dimension histogram `dim4=8, dim5=3, dim6=1, dim7=1` — the eight closures of
the `h`-nonzero components plus `H1,H3,H4,H5,H6` — as one D7 carry
checkpoint only, supplying no next carry, no recurrent bounded state, no
all-depth lift/no-lift, no characteristic-zero map, no counterexample, and
no JC2 conclusion.

## Verdict

CONFIRMED
