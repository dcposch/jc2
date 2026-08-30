# Hostile rereview: D3 sectioned one-support global control and genus-two ramification obstruction

Date: 2026-08-30 UTC  
Reviewer: Fable 5, compact hostile rereview lane  
Reviewed body: `xmodel/bd-a2-d3-sectioned-global-control-ramification-obstruction-sol56-20260830.md`  
Context: the preceding review lane was terminated operationally before producing a
report; this audit was performed independently from the charged inputs only.  No
sibling external-model prompt, log, report, or receipt was read.  Receipt status
for this lane is `ABSENT`, as expected; no `charge_basis` line is emitted because
no new exit price is asserted — every block-exclusion price consumed here comes
from the two promoted coordinator theorems charged below.

## 0. Verdict summary

| # | Charged claim | Verdict |
|---|---|---|
| 1 | `G=(Sx+Tz)^3+S^2Ty^3+T^3x^2y` integral, normal, finite flat of target degree three; `Sing(X)={p_0 (level two, t=0), p_infinity (A_2)}` complete | **CONFIRMED** |
| 2 | Sectioned minimal model `V^2=U^3-t^4`, `IV*+IV`, rational; realizes exactly `m=1, T=2t_0, D=-2F_(t_0), rho(Y)>=12` | **CONFIRMED** |
| 3 | Level-two germ `X^3+ty^3+t^5y`, weights `(7,6,3)`: quasismooth, irreducible, rational central curve, complete four-arm quotient census, tree, `p_g=2` | **CONFIRMED** (census completed below) |
| 4 | Residual ramification normalization: birational completeness, absolute irreducibility, genus two from both `9q^7+9tq^4+4t^5=0` and `a^4(3-2a)^3=-12t^8`, all branch places | **CONFIRMED** |
| 5 | Conditional proper-block obstruction: genus-two strict transform in the boundary of the morphic first-leg image | **CONFIRMED, conditional exactly as charged** |
| 6 | Desk replay; pricing as surface-level positive control plus control-specific block exclusion | **CONFIRMED** |

No `GAP`, no `REFUTED`.  Five non-blocking notes (Section 3) supply missing
one-liners and sharpenings; none changes a promoted statement.

## 1. Custody

All four charged SHA-256 hashes reverified byte-exact on disk:

```text
0178cb0c23c2bb50bc436b5ee6f41b8935a09cf0ca5f68fc3c5fde1d7da6b9d4  source report
f7cba66318887c4c34182c6d91821fd7d4f7f20ed78d30e9846106f52e558bc5  artifact json
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de  hodge-level-divisor coordinator
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d  rational-forest morphic coordinator
```

Artifact internals reverified: file 16293 bytes; body = first 15960 bytes ends in
the standalone `<!-- BODY-END -->` line; body SHA-256 recomputed
`cc63787378346bba5055b573186fe30b709340c968bd2cf465afc5729d962a73`, matching both
the seal and the custody record.  Charged inputs, Git state, ledgers, and
`jc2-lean` untouched.

## 2. Itemized findings

### Item 1 — CONFIRMED

Machine (this lane): coefficient extraction of the binary cubic
`(x^3, 3x^2z+y^3, 3xz^2, z^3+x^2y)` replayed; the common-zero chase
(`x=0`, then `y=0`, then `z=0`) is exact, so `pi` is quasi-finite, hence finite
(proper), and miracle flatness applies to the CM hypersurface over the regular
target.  The singular census was independently machine-checked in **all six**
affine charts `{S=1,T=1} x {x=1,y=1,z=1}` (the source replay checks only the
`t=0` slice): the Jacobian ideal is the unit ideal in four charts, cuts exactly
the origin in `(S=1,z=1)` (that is `p_0=(T=0,[0:0:1])`), and cuts exactly
`(s,x,z^2)` in `(T=1,y=1)` (that is `p_infinity=(S=0,[0:1:0])`).  So
`Sing(X)={p_0,p_infinity}` is complete.  The `A_2` normal form
`w^3+s^2+x^2`, `w=z+sx`, is an exact polynomial identity.  Integrality: the
generic fibre of the coefficient projection is a smooth plane cubic, hence
integral; a vertical factor is excluded because the `(S,T)`-coefficients of
`x^3` and `x^2y` in `G` are `S^3` and `T^3`, coprime (Note N1: the source says
"primitive" without this one-liner).  Normality is then Serre `S_2+R_1`.

### Item 2 — CONFIRMED

The section `[S:T] -> [-T:0:S]` kills `G` identically.  I rederived the
Weierstrass model from scratch: the line `y=0` cuts each fibre in `3*(section
point)`, an inflection; with `x'=x+tz`, `u=x'/y`, `v=z/y` the fibre is
`u^3+t^3(tv-u)^2w+tw^3=0`, and the machine-verified exact identity

```text
F_W(-t*u, t^4*v-t^3*u, w) = -t^3*(u^3+t^3*(t*v-u)^2*w+t*w^3),
F_W(U,V,W)=U^3-V^2*W-t^4*W^3,      det L=-t^5,
```

gives `V^2=U^3-t^4` over `C(t)`.  Kodaira/Tate typing: `(v(c4),v(c6),v(Delta))
=(inf,4,8)` at `t=0` is minimal `IV*`; the rescale at infinity gives
`(inf,2,4)`, minimal `IV`; `e=8+4=12`, fundamental line degree one, so the
relatively minimal sectioned model is a rational elliptic surface and `X` is
rational.  Claim (2.4) is in fact **forced exactly**: the reduction above is a
linear substitution with scale `-t^3` and determinant `-t^5`; invariant weights
(degree-6 invariant, weight 6; discriminant degree 12, weight 12) give
`c6_plane = t^(-18)*t^30*864t^4 = c*t^16` and `Delta_plane = c'*t^32` as exact
polynomial identities in the `S=1` chart, and the degrees 18 and 36 then force
`c6_plane=cS^2T^16`, `Delta_plane=c'S^4T^32` with no other zeros — which
independently re-proves smoothness of all other fibres and level zero at
infinity.  Exact CFS level: `(16-4)/6=(32-8)/12=2` at `t=0`, `0` elsewhere, so
`T=2t_0` with one support point (the "one-support" of the row name).  With the
section, this is exactly the second row of the promoted four-row gate
(`m=1, T=2t, D=-2F_t, rho(Y)>=12`); the gate's rationality input is discharged
directly, not assumed.  Two independent confirmations of the row data:

- `D=-2F_0` directly: `K_S=-F` for the sectioned rational elliptic surface and
  the gate's `K_S=F+D` give `D=-2F`; support at `t_0=0` by the base support
  equality.
- Euler ledger: `e` of a smooth `(3,3)` divisor is `36`; `mu(p_0)=30`
  (semiquasihomogeneous, `(14*15*18)/126`), `mu(A_2)=2`, so `e(X)=4`
  (cross-checked fibrewise: triple line `+2`, cuspidal cubic `+2`); the two
  exceptional trees add `13+3-2=14`, so `e(Y)=18`, `b_2=rho(Y)=16`,
  `K_Y^2=-6`.  Thus `rho(Y)=16>=12`: the row bound is realized, non-sharply.
  Coherence: relative minimalization contracts exactly six vertical
  `(-1)`-curves, all over `t=0` (13 fibre components down to the 7 of `IV*`),
  while the fibre at infinity (cuspidal strict transform + two `A_2` curves)
  is already the 3-component `IV`.

### Item 3 — CONFIRMED, census completed

Expansions (3.1)/(3.3) and the partial-derivative case analysis (3.4) are exact
(machine + hand): the principal part `f_21=X_1^3+ty^3+t^5y` is quasismooth, and
the two discarded terms have weights 25 and 29.  The central curve
`C: f_21=0` in `P(7,6,3)` is rational: every degree-zero monomial has `X_1`
exponent divisible by 3, and `X_1^3/t^7=-(r^3+r)` with `r=y/t^2`, so the
degree-zero field is `C(r)`; irreducibility because `t*y*(y^2+t^4)` is not a
cube.  The four-arm census is complete: the stacky locus meets `C` in exactly
the `y`-chart point over `t=0` plus the three `t`-chart points
`xi=0, eta=0,+i,-i`; the `X_1`-chart contributes nothing; all four are smooth
one-branch points, so quotient resolution attaches four disjoint bamboos and
the reduced dual graph is a star tree.  This lane computed the census
explicitly (the source stops at "four bamboos"):

```text
P_y  (y-chart):  mu_6 acting (zeta^-1, zeta) on (X', v):  1/6(1,5) = A_5, chain [2,2,2,2,2]
P_t, Q_+, Q_-  (t-chart):  mu_3 acting (zeta^2, zeta):    1/3(1,2) = A_2, chain [2,2]  (x3)
central curve C_0 rational with C_0^2 = -3
```

Integrality control: Seifert `e=-d/(w1w2w3)=-1/6=-(b-5/6-3*(2/3))` gives `b=3`,
an integer (convention checked against `E_8`, which returns central `-2`).
Total: 12 exceptional curves in a tree; with the `A_2` at infinity, 14 — the
numbers used in the Euler ledger of Item 2, which closes.  `p_g(p_0)=2` by the
two positive lattice points `(1,1,1),(1,1,2)`; strengthening: the full germ is
Newton-nondegenerate for its diagram (the extra monomials lie strictly above,
and every face/edge truncation is torus-nondegenerate), so `p_g=2` holds for
the actual germ by Merle–Teissier, not only for the principal part.  The
source's warning that a rational-tree boundary does not imply a rational
singularity is correct and is exactly what makes this a genuine control.

### Item 4 — CONFIRMED

Class bookkeeping: `K_X=B|_X`, `Ram(pi)~(3A+B)|_X`, fibre degree
`(3A+B)*B*(3A+3B)=9=2+7`; `C_0` is totally ramified over `y=0` (the fibre cubic
degenerates to a perfect cube there), different coefficient two.  The dense
derivation of `9q^7+9tq^4+4t^5=0` replays exactly (`3F-tF_t=3u^2+2ty^3` on
`x=1`; substitution factor `-3q^2P/(8t^3)`).  **Independent second
derivation** (this lane, `z=1` chart, no shared coordinates): splitting the
ramification ideal as `(g_T, y*h)`, `h=(2t-x)y^2-3t^2x^3`, recovers `2C_0`
scheme-theoretically and yields

```text
Res_y(g_T, h) = 9*((x+t)^4*(2t-x)^3 - 12*t^8*x^7),
```

which with `a=(x+tz)/x` is literally `a^4(3-2a)^3=-12t^8` — equation (4.7)
reproduced without passing through (4.6).  Both directions of (4.7a) verify as
exact identities: `a(3-2a)q-2t^3=-P/(2t^2)` and `a^4(3-2a)^3+12t^8` is
divisible by `P` under `a=-3q^3/(2t)`; so the two models are birational, and
the parametrization (4.5) is birational onto `R'` with inverse `q=u/y`.
Absolute irreducibility: the Kummer square test at `a=3/2` (odd valuation 3)
is **sufficient over `C(a)`** because `-4K^4` is contained in `K^2` when
`i in K` (Note N2); the degree-eight cover is irreducible.  Genus two, three
independent ways:

1. Riemann–Hurwitz over the `a`-line, ledger (4.8): complete, since the cover
   ramifies only over zeros/poles of `a^4(3-2a)^3`; `2g-2=-16+(4+7+7)=2`.
2. Newton polygon of `P`: interior lattice points 2; torus nondegeneracy via
   the replay determinant `-2592` plus the three edge truncations
   `9q^4(q^3+t)`, `t(9q^4+4t^4)`, `9q^7+4t^5`, all torus-squarefree.
3. New, over the `t`-line (degree 7): places over `t=0` are `(1,1,1,1,3)`
   (polygon slopes; numerically corroborated: four roots at `|q|=(4/9)^{1/4}t`,
   three clustering as one `e=3` place), one totally ramified `e=7` place over
   `t=infinity`, and eight simple finite branch fibres at `7^7*t^8=-2^2*3^9`
   (machine: `Res_a = c*t^40*(823543t^8+78732)`, simple roots);
   `2g-2=-14+(2+6+8)=2`.

All finite and infinite branch places are therefore accounted for in both
models.  The target discriminant `Disc_t(F)=-y^2*B_10` replays; `R'` maps
birationally onto the degree-10 residual branch curve (`12-2*1=10`), and its
closure in `X` is complete and irreducible.  Genus of the normalization: two.

### Item 5 — CONFIRMED, conditional exactly as charged

Decision: **yes** — under the antecedent, the complete genus-two strict
transform lands in the boundary, and the contradiction is valid.  Checked
point by point against the promoted morphic rational-forest coordinator:

- Interface fit: (5.2) is verbatim the promoted proper-block interface
  (`V=g1(A2) subset Y_sm minus Ram(g2)`, `g1` everywhere-defined, surjective,
  étale), applied with `g2=pi|_Y` under the assumed global identification
  (5.1).  `V` is smooth quasi-projective and morphically dominated by `A2`,
  so the forest theorem applies to `V` itself.
- Boundary membership: `R'` over the affine target lies in `Ram(pi)`, hence
  outside `V`; over target infinity it is outside `Y`; so `R' cap V` is empty
  and the strict transform of the complete curve `R'` sits in `W minus V`.
  Isolated complement points are absorbed by the boundary blowups; `W -> X`
  is a morphism, so the strict transform is not contracted; in a strict-SNC
  boundary it is the smooth normalization, of genus two.  The forest theorem
  forces every boundary component rational — contradiction.  Hence the
  restriction of `pi` over an affine plane is not the globally identified
  second leg of any actual proper block.
- Conditionality discipline: the antecedent (5.1) is the entire content; the
  source correctly refuses to derive it from a completed-algebra match, a
  finite jet, a rational map from `A2`, or abstract rationality of `X`.  This
  is exactly the boundary drawn by the promoted correction (the `P2 minus E`
  counterexample kills the rational-domination variant), and the source
  stays on the licensed side.  No carrier/attainment or floor/attainment
  substitution occurs; the obstruction consumed is component genus, which
  survives strict transform and boundary blowup.

### Item 6 — CONFIRMED

The embedded desk replay was rerun **verbatim** in this lane and printed
exactly `D3_SECTIONED_GLOBAL_CONTROL_RAMIFICATION_PASS`.  The split between
checked algebra and hand geometry is honest and correctly drawn in the
source's Section 6: the machine layer covers the polynomial identities,
discriminant factorization, torus-nondegeneracy determinant, Newton/lattice
counts, and the isolated-singularity Gröbner check; the hand layer invokes
miracle flatness, Serre's criterion, weighted-blowup/quotient resolution,
Kummer irreducibility with Riemann–Hurwitz, minimal-fibre classification, and
the two binding campaign theorems, both of which are hash-verified charged
inputs of this audit.  Pricing is correct and properly bounded: a
surface-level positive control for the row `(m=1, T=2t_0, D=-2F_(t_0),
rho>=12)` plus a control-specific **conditional** block exclusion; explicitly
not an intermediate-surface statement, not a universal row theorem, not a
Keller map, and no JC2 consequence.  The negative-control lesson (local
normality, solubility, raw degree, additive reduction, and rational-forest
topology cannot eliminate this row) is sound and worth keeping: `p_g=2` hides
behind a rational exceptional tree here.

## 3. Non-blocking notes

- **N1 (Item 1).** "Primitive" is asserted, not shown; the one-line proof is
  `gcd(S^3, T^3)=1` on the coefficients of `x^3` and `x^2y`.
- **N2 (Item 4).** For degree `8=2^3` the general Kummer criterion also
  requires `c notin -4K^4`; over `C(a)` this is subsumed by the square test
  since `-4d^4=(2id^2)^2`.  The source's scoping "over `C(a)`" makes its
  one-line argument complete, but the clause deserves the remark.
- **N3 (Item 3).** The four-arm census is qualitative in the source; the
  explicit types (`A_5 + 3*A_2`, central `-3`, Seifert `b=3` integral) are
  supplied above and cross-lock with the Euler/Picard ledger of Item 2.
- **N4 (Item 2).** The realized Picard number is exactly `rho(Y)=16`; the row
  constraint `>=12` is met with slack.  No defect — the row datum is a bound.
- **N5 (Item 2).** The source cites "the corrected local report" for the two
  CFS transformations; that file is uncharged here.  The independent flex
  rederivation above removes any dependence of this audit on it.

## 4. Maximum-safe theorem

Let `X` be `(Sx+Tz)^3+S^2Ty^3+T^3x^2y=0` in `P2 x P1`.  Then:

1. `X` is an integral, normal, rational surface; `pi: X -> P2` is finite flat
   of degree three; `Sing(X)` consists exactly of `p_0=(T=0,[0:0:1])` —
   semiquasihomogeneous of weights `(7,6,3)`, degree 21, `p_g=2`, exact
   CFS/Hodge level two, good resolution a star tree with rational `(-3)`
   central curve and arms `A_5, A_2, A_2, A_2` — and the `A_2` point
   `p_infinity=(S=0,[0:1:0])`.
2. The coefficient projection has the section `[-T:0:S]`; its relatively
   minimal model is the rational elliptic surface `V^2=U^3-t^4` with fibres
   `IV*` at `t=0` and `IV` at infinity; `c6_plane=cS^2T^16` and
   `Delta_plane=c'S^4T^32` exactly; `X` realizes row
   `(m=1, T=2t_0, D=-2F_(t_0), rho>=12)` of the promoted D3 four-row gate,
   with `rho(Y)=16` and `D=-2F_0` verified directly.
3. `Ram(pi)=2C_0+R'` with `C_0` the section, totally ramified over the line
   `y=0`, and `R'` a complete irreducible curve of normalization genus two,
   with plane models `9q^7+9tq^4+4t^5=0` and `a^4(3-2a)^3=-12t^8`.
4. **Conditionally**: if for some affine plane `A2 subset P2` the restriction
   `pi^(-1)(A2) -> A2` were globally the finite second leg of an actual proper
   block, the promoted morphic interface and rational-forest theorem would
   force the genus-two strict transform of `R'` into a strict-SNC boundary of
   a smooth completion of `g1(A2)` — a contradiction.  Hence no actual proper
   block has this restriction as globally identified second leg.

Nothing more: no universal row exclusion, no proper-block existence or
non-existence, no intermediate-surface claim, no Keller map, no JC2.

## 5. Cheapest universal successor

Extend the promoted four-row invariant-gate program (hodge coordinator,
Section 7 template) from the `m=3` rows to **this** row: on the exact global
coefficient family of sectioned one-support class-`(3,3)` surfaces with the
level-two point normalized to `t_0=0`, impose the exact-level-two gate
`t^8 | c4_plane`, `t^12 | c6_plane` together with the finite principal-open
upper disjunction `[t^12 does not divide c4 or t^18 does not divide c6]`, on
the literal integral-normal, generic-smooth open (no saturation closures), with
`Delta/t^24` as control.  For each survivor, price the residual ramification
component: decide whether `Ram(pi) - 2*(section)` always carries a complete
positive-genus component, which the promoted forest theorem then converts into
the same conditional second-leg exclusion row-wide.  The present control
proves the row and the obstruction are both nonempty, but one witness is a
floor, not attainment — the row-level claim needs the family computation.
Desk-scale shards stay local; any Gröbner or saturation shard beyond desk
scale goes to AWS.  Do not consume the triple-line first-jet packet while its
review is live.

## 6. Execution disclosure

This lane had a shell.  Run locally: the embedded desk replay verbatim
(PASS); six-chart Jacobian Gröbner census; the Weierstrass reduction identity;
the `z=1`-chart resultant elimination reproducing (4.7); both (4.7a)
identities; the `a`-line branch resultant `c*t^40*(823543t^8+78732)`; numeric
place clustering of `P(q,t)` at `t -> 0, infinity`; and the artifact body-hash
recomputation.  Heaviest computation: a degree-seven resultant and
four-generator Gröbner bases — no heavy CAS.  Hand geometry, machine-
corroborated where stated: miracle flatness, Serre normality, quotient-type
and Seifert census, Euler/Picard ledger, Riemann–Hurwitz ledgers, Kodaira
typing, and the two consumed binding theorems.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18374`.
- Body SHA-256:
  `c451103f41384b64cea511c3dcd33a8cc2aee8206ea0787fcc4bc258cc1b7867`.
- Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`.
