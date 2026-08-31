# Hostile review: PI1S4-CLOSE-RESIDUAL r2

## 0. Integrity, scope, and verdict key

The three frozen inputs were hashed before reading.  All match exactly:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  pi1s4-close-residual-r2-opus5-20260831.md
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  pi1-s4-decision-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

The CLOSE report incorporates the prior binding integration `bbd48de1...` by reference (CLOSE 25, 39; current integration 3-4, 18).  I located that exact artifact read-only and verified SHA-256 `bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963`; its lines 56-66 are therefore usable to audit the inherited promotion rather than merely trusting the paraphrase.

`CONFIRMED` means the stated conclusion and typing follow at the cited scope. `REFUTED` means a displayed claim, proof step, or label is false. `GAP` means the conclusion may be true but the written argument does not prove it.  Line references `C`, `D`, and `I` mean respectively the frozen CLOSE report, decision report, and current coordinator integration.  No CAS was run, no `jc2-lean` path was inspected, and no file other than this report was written.

Overall verdict: **PROMOTE-AS-CORRECTED, not wholesale.**  The degree-`<=4` no-`S_4` closure survives, and `(4,2)` is closed.  The advertised blanket negative about outer block collapse is false; Theorem A'(5) has a cabling error; and the `(6,4)` semigroup lower bound reverses inclusion.  Consequently the general `(M-INF)` mechanism and the claimed nodal closure through degree seven do not survive.

## 1. Typed restatement and promoted scope for `D_1`

1. **CONFIRMED — residual structure, with inherited-source custody made explicit.**  The exact prior integration promotes Theorem 4.3(1)-(4), adds `Sing D_1 cap D_0=empty`, and promotes the repaired consequences `s_0=c_0=1`, both normalizations `A^1`, and Corollary 4.4 (`xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md` 56-66).  Thus C 42-48 consumes at the right repaired-`N=4` residual scope: `A_F=D_1 union D_0`, the degree-four connected cover with branch locus `D_1`, the `S_4` quotient, and the double-smooth-branch/disjoint-transposition description.  The current integration preserves that ledger by saying it extends the prior one (I 3-4); CLOSE-derived additions themselves remain provisional (I 63-77).

2. **CONFIRMED — `delta_aff >= 1`.**  Corollary 4.4 promotes that `D_1` is affine-singular.  Each promoted singularity consists of two smooth branches of contact `k_p>=1`, hence `delta_p=k_p>=1`.  Every use at C 93-98, 413-424, and 482-500 concerns this same residual `D_1`; there is no scope leak.  This conclusion does not require nodality.

3. **CONFIRMED — polynomial normalization.**  From `normalization(D_1)=A^1`, a polynomial birational parametrization exists.  Swap coordinates and shear equal leading degrees to obtain `d=deg p>n=deg q>=1`; then `deg D_1=d`, and in the stated infinity chart `a=d-n`, `b=d` (D 49-68; C 50-56).

4. **CONFIRMED — correction of the Puiseux-pair gloss.**  For `p=t^(2m)`, `q=t^m+t`, the map is birational, while `a=m`, `b=2m`.  Writing `v=s^m+s^(2m-1)` and replacing `s` by `s(1+s^(m-1))^(1/m)` gives first non-`m`-divisible exponent `3m-1`; the germ has one characteristic pair although `gcd(a,b)=m`.  Thus C 61-72 correctly rejects the deleted parenthetical from D 457-458; the current integration had already deleted it (I 38-41).

5. **CONFIRMED — contact lemma and `(4,2)` rigidity.**  After choosing `v=s^a`, a smooth tangent germ is `u=phi(v)`.  It can cancel only exponents divisible by `a`, so its contact is a multiple of `a` below the first characteristic exponent `beta_1`, or is `beta_1` itself (C 74-91).  At `(d,n)=(4,2)`, contact four forces odd `beta_1>4`; the genus sum is three and `delta_aff>=1`, hence `beta_1=5`, `delta_infty=2`, `delta_aff=1`.  The sole affine singularity is therefore an ordinary node (C 93-98).

**Corrected promoted statement.**  At the repaired residual scope, all data in C 42-59 and the implication `Sing_aff(D_1) nonempty => delta_aff>=1` are binding.  The condition `(C1)` means only `gcd(d,n)=1`; it must not be replaced by a count of local Puiseux pairs at `Q`.

## 2. Whether the promoted data constrain `(d,n)` for `D_1`

1. **CONFIRMED in substance — nothing pins `(C1)` or bounds `d` above.**  The current integration independently records that no promoted datum bounds `deg D_1` (I 81-85).  The `(2,1,1)` generic sheet profile and disjoint-transposition local profile constrain cover monodromy, while `mu=2` is a dicritical/cover multiplicity.  No promoted map identifies any of those with the pole degrees `d,n`.  Doing so would conflate a cover series, a physical place, and a flag.  The local `A_(2k-1)` relations are invisible because disjoint transpositions satisfy all of them (D 146-160).

2. **REFUTED literally — C 145-150 says none of the data “sees” degree.**  They do give lower constraints:

   - `n>=2`: if `n=1`, then `q=alpha t+beta` and eliminating `t` makes `D_1` the smooth graph `x=p((y-beta)/alpha)`, contrary to promoted singularity.
   - `d>=3`: either the genus formula plus `delta_aff>=1`, or the fact that `d` fibre meridians map to transpositions generating `S_4`, excludes `d<=2`.
   - Since the coprime Main Theorem is now promoted (I 30-47) and the residual supplies an `S_4` quotient, any surviving residual has `gcd(d,n)>=2`; hence `d>=4`.  C 157-170 eventually reaches this conclusion, but it contradicts the preceding blanket wording.

3. **CONFIRMED — the Euler route is an identity.**  Stratifying the four-sheeted cover gives `chi_c(Y)=3` independently of the number and contacts of affine double points (C 108-134; independently D 525-536).  The boundary count also gives three.  Equality of two invariant computations is a consistency check, not a degree obstruction.

4. **CONFIRMED — no usable Orevkov-chain pin.**  Orevkov 1990 was neither officially obtained nor promoted (D 494-509; I 96-97).  The inherited Orevkov lemma used to repair the `mu=1` component is degree-free and is not a degree theorem for the `mu=2` component `D_1`.  The resolution identity `deg D_1=l_1.Phi^*H` would require base-point/pole data absent from the promotion set.

**Corrected statement and recommendation — PROMOTE-AS-CORRECTED.**

> Promoted data force `n>=2`, `d>=3`, and, after the promoted coprime no-`S_4` theorem is combined with the residual quotient, `gcd(d,n)>=2` and `d>=4`.  They neither force coprimality nor give an upper bound on `d`.  Thus `OPEN[PI1S4-D1-DEGREE]` remains valid.

## 3. Cable/block analysis and the `n \mid d` obstruction

1. **CONFIRMED — tubular factorization and exponent.**  Put `g=gcd(d,n)`, `d=gd'`, `n=gn'`.  The leading Puiseux terms give `d'` tubes of `g` strands, and their centres trace the torus braid `delta_(d')^(n')`.  After a simultaneous braid conjugacy,
   `rho_inf=C_g(delta_(d')^(n')) iota`, with `iota in B_g^(d')` (C 181-201).  Exponent sums give
   `e(iota)=(d-1)^2-2 delta_inf-n(d-g)` (C 203-215).  At `g=1`, `iota=1` because the kernel is `B_1^(d')`, not because exponent zero alone would imply triviality.

2. **CONFIRMED — Lemma 3.3.**  Internal Hurwitz moves preserve each ordered block product.  A cabled crossing sends two subtuples `(A,B)` to `(P_A B P_A^(-1),A)`, hence their products to `(P_A P_B P_A^(-1),P_A)`, exactly the outer Hurwitz action (C 217-232).

3. **CONFIRMED — Theorem A'(1)-(4).**  Applying block products to `rho_inf.T=T` makes `BP(T)` fixed by `delta_(d')^(n')`.  With `U_(j-d')=P U_j P^(-1)`, fixedness is `U_j=U_(j-n')`; coprimality of `d',n'` makes all block products one `P`-conjugacy orbit.  Thus `H=<U_1,P>`, `P^(n')` is central in `H`, and if `n|d` (`n'=1`) every block product equals a common `c` and `P=c^(d')` (C 234-252).

4. **GAP — A'(5).**  C 252-253 falsely treats blackboard cabling of an outer full twist as global conjugation on all `d` entries.  Already for two blocks of two, `w=C_2(sigma_1)` sends `(A,B)` to `(P_A B P_A^(-1),A)`; `w^2` conjugates the first and second blocks by different words, not globally by `P_AP_B`.  A repair uses
   `Delta_d^2=C_g(Delta_(d')^2) Omega`, where `Omega` is the product of internal block full twists: after `P^(n')=1`, an **adjusted** internal braid `Omega^(-n')J`, not the claimed `J`, fixes the subtuples.  Promote the centrality consequence, not the written inner-fixedness sentence.

5. **REFUTED — “outer level alone never suffices when `n|d`.”**  Cyclicity of `H` only defeats the centrelessness rerun; it proves no universal insufficiency.  It is false at the very case cited.  For `(4,2)`, A'(4) gives
   `t_1t_2=t_3t_4=c`.  A product of two transpositions is `1`, a 3-cycle, or a double transposition.  In the first case the two blocks are repeated transpositions and generate at most `S_3` or `V_4`; in the second all factors lie on the same three-letter support; in the third the only factors are the two disjoint factors.  Thus the outer collapse alone already excludes `S_4`.  Conversely there is no uniform outer kill: at `(6,2)`, the blocks `((12),(12))`, `((23),(23))`, `((34),(34))` all have product one but their entries generate `S_4`.  Also, “`Z(H)=1` fails exactly when `n|d`” is false when `c=1`, and no converse was proved off `n|d` (C 255-267, 461-465).

6. **CONFIRMED-AS-CORRECTED — full `(4,2)` fixed tuples.**  Write `a=t_1`, `b=t_2`, `c=ab`, and `iota=sigma_1^(k_1)sigma_3^(k_2)` with `k_1+k_2=1`.  For the pair Hurwitz map `h(x,y)=(xyx,x)`,
   `h^(2m)=c^m(x,y)c^(-m)` and `h^(2m+1)=c^m(xyx,x)c^(-m)`.  If `k_1=2m+1`, fixedness gives
   `(t_3,t_4)=(c^m(aba)c^(-m),c^m a c^(-m))`; if `k_1=2m`, it gives the conjugates of `(a,b)`.  Both leave
   `a=c(aba)c^(-1)`, `b=cac^(-1)`, equivalently `c^3=1`.  Hence all entries lie in `<a,b><=S_3` (C 270-296).  The family at C 453-459 must define `c=ab` and use a curve-fixed integer `m_0` determined by `iota`; `m` is not an extra free parameter.

7. **REFUTED arithmetic.**  C 517-520 calls `(6,4)` an `n|d` row, but `4` does not divide `6`; its reduced pair is `(d',n')=(3,2)`.  The degree-six divisibility rows are `(6,2)` and `(6,3)`.

**Recommendation.**  Promote the tubular factorization, (3.2), Lemma 3.3, A'(1)-(4), and the corrected `(4,2)` classification.  Refute the blanket NEGATIVE interpretation and hold A'(5).

## 4. The `(M-INF)` reduction and noncoprime cases

1. **CONFIRMED — basic Nori reduction.**  With one fixed convention including all terminal multiplicity-one centres,
   `C'^2=d^2-sum m_j^2`, `sum m_j(m_j-1)=2 delta_inf`, and `M_inf=sum m_j`; the genus formula gives
   `C'^2-2 delta_aff=3d-2-M_inf` (D 281-301; C 300-306).  For a nodal affine curve `r=delta_aff`, so Nori's strict inequality is exactly the integral bound `M_inf<=3d-3`.  I independently streamed and hashed Nori's official PDF; Proposition 3.27 says the relevant kernel is finitely generated abelian, which is enough here.

2. **GAP-AS-WRITTEN / CONFIRMED-AS-CORRECTED — (4.1).**  The shared `C,L_inf` centres and the embedded-resolution centres are initial segments of the same infinitely-near-point chain.  Noether gives the sum on the shared segment as `d`; hence their union has exactly
   `M_inf=max(M_emb,d)` (C 308-323).  Delete “up to one trailing multiplicity-1 point”: an unresolved `+/-1` is not harmless at a sharp threshold.  With the report's terminal convention, equality is exact.

3. **GAP in the charged proof, but the identity is repairable.**  C 325-353 labels
   `(4.2) M_emb=m+beta_h-1`
   merely `CHECKED` on examples, then later uses it in the `PROVED-HERE` degree-seven claim.  For a singular branch it is true.  A short induction supplies the missing proof: after one tangent blow-up, if `beta_1-m>=m`, the new pair is `(m,beta_h-m)`; otherwise, after swapping coordinates, it is `(beta_1-m,beta_h-beta_1+m)`.  Adding the current centre's multiplicity `m` preserves `m+beta_h-1` in both cases.  At the terminal smooth tangent state `(1,k)`, the `k` multiplicity-one centres give `1+k-1`.  Thus (4.2) may be promoted only with this proof inserted.

4. **REFUTED as uniformly typed — scalar reduction.**  If `a=d-n=1`, the infinity branch is initially smooth, has no characteristic exponent, `M_emb=0`, and `M_inf=d`; `(M-INF)` is automatic.  C 361-363 incorrectly calls this `h=1`, `beta_1=d`.  If `a>=2`, then (4.1)-(4.2) give
   `M_inf=max(d,a+beta_h-1)`, and, since `d<=3d-3`,
   `(M-INF) iff beta_h<=2d+n-2`.
   This case split is the exact corrected reduction.

5. **CONFIRMED — gap identity; REFUTED — claimed bound mechanism.**  Set
   `S={deg_t h: 0!=h in C[p,q]}`.  Finiteness of normalization and the degree filtration give
   `delta_aff=dim C[t]/C[p,q]=#(N minus S)`; birationality makes `S` numerical, and products give `S superset <d,n>` (C 368-378).  But containment reverses gap sets: from `S superset <d,n,c>` one gets
   `N minus S subset N minus <d,n,c>`, hence an **upper**, not lower, bound on gaps.

6. **CONFIRMED — `(4,2)`.**  The rigidity in section 1 gives the `(2,5)` cusp, `M_emb=M_inf=6<=9`, `N_inf=10`, and `C'^2=6>2r=2`.  Nori therefore gives `pi_1(C^2-D_1)` abelian, hence `Z` (C 380-381, 396-404).  This is independent of the braid proof.

7. **GAP — `(6,4)`; its written verification is false.**  C 383-389 asserts that an odd `c` forces at least five gaps.  Besides the reversed containment, neither `c>=7` nor absence of further generators is proved.  An exact negative control is

   ```text
   p=t^6+(3/2)t^3+3/8,   q=t^4+t,
   p^2-q^3=(1/8)t^3+9/64.
   ```

   Thus `C[p,q]=C[t^3,t^4+t]`, its fraction field is `C(t)`, and its degree semigroup is `<3,4>`, with gaps `1,2,5`.  The degree-six curve has `delta_aff=3`, hence `delta_inf=7`, `beta_1=15`, and `M_inf=16>15`.  It has an ordinary triple point over `t^3=-1`, so it is not a residual `D_1`; it refutes the semigroup inference and the unrestricted `(6,4)` claim, while leaving the double-point residual case OPEN.  In that case the needed target is only `delta_aff>=4` (`beta_1<=13`), not the report's unsupported `>=5`.

8. **CONFIRMED-AS-CORRECTED — Theorem B-noncoprime.**  The valid theorem is:

   > If all affine singularities are nodes and the actual infinity resolution satisfies `M_inf<=3d-3`, then `pi_1(C^2-D)=Z`, with no coprimality assumption.

   Its unconditional degree-four abelian specialization is `(d,n)=(4,2)`.  C 396-401 should not state bare `deg D_1=4 => pi_1=Z`: at `(4,3)` the promoted coprime theorem yields no `S_4` representation even with tangency, but does not prove abelianness.

**Recommendation.**  Promote the exact case-split reduction, (4.2) with the induction above, the gap identity, `(4,2)`, and the conditional nodal theorem.  Do not promote the `(6,4)` check or a general gap-count bound.

## 5. Low-degree table and residual-closure rows

1. **CONFIRMED arithmetic / REFUTED heading.**  The values at C 413-424 follow from the genus formula, the coprime cusp formula, and promoted singularity: `d<=2` and `n=1` are impossible; `d=3,n=2` has one affine node; the two degree-four rows and three degree-five rows have exactly the displayed `(delta_inf,delta_aff)`.  But “low degrees are excluded by promoted data alone” is inaccurate: the table enumerates several live curve types, and their representation-theoretic exclusion uses Nori or the promoted Main Theorem.

2. **Row 1 — CONFIRMED, retype `PROMOTED/RE-DERIVED`.**  For coprime `(d,n)` and nodes, the infinity resolution gives `C'^2=nd` and `2r=(n-1)(d-1)`, with positive difference `n+d-1`; Nori gives `pi_1=Z` (C 433-437).  This is mathematically re-derived, but Theorem B was already explicitly promoted at I 42-45, so `PROVED-HERE` is not the clean dependency label.

3. **Row 2 — CONFIRMED, but `PROVISIONAL` is stale.**  The corrected coprime tangential no-`S_4` theorem is promoted in I 30-47.  The honest current label is `PROMOTED-CONSUMED`, not C 438-439's `PROVISIONAL`.  It proves only the representation-level conclusion in general, not `pi_1=Z` (D 465-472).

4. **Row 3 — CONFIRMED-AS-CORRECTED, `PROVED-HERE`.**  At `(4,2)`, the outer block products alone already prevent `S_4`; the full fixed-tuple solve independently forces `(ab)^3=1`.  The Nori calculation independently gives `pi_1=Z` (C 440-442).  Correct the tuple-family parameters as in section 3, but retain the “twice independently” conclusion.

5. **Row 4 — CONFIRMED conditionally.**  “Nodal plus an actually verified `M_inf<=3d-3` implies `pi_1=Z`” is correct and noncoprime (C 443-445).  The row may cite `(4,2)` as verified.  Delete `(6,4)`: its purported verification is a GAP.

6. **CONFIRMED but mistyped dependency — degree at most four.**  The no-`S_4` conclusion is valid: degree three is coprime/nodal; `(4,2)` is row 3; `(4,3)` is the promoted coprime tangential theorem.  In C 447-449, however, an “outright” theorem is assembled while one dependency is labelled provisional.  Under the current integration that dependency is now promoted, so promote the assembly rather than calling it self-contained `PROVED-HERE`.

7. **Sharpening missed by the charge.**  Degree five is also closed outright: `n=1` contradicts singularity and `n=2,3,4` are all coprime to five.  Therefore the exact current cutoff is

   > For a curve in the repaired residual configuration, `deg D_1<=5` is impossible; equivalently no prescribed `S_4` quotient exists in that range.

   This does not assert abelianness in the tangential coprime rows.  Any surviving residual now has `d>=6` and `gcd(d,n)>=2`.

**Row recommendations.**  Promote row 1 as an already-promoted theorem with a checked Nori derivation; promote row 2 at its representation-only scope; promote corrected row 3; promote row 4 only as an implication with no `(6,4)` example.  Promote the sharpened degree-`<=5` residual closure.

## 6. OPEN typings and leverage order

1. **REFUTED — C 482-504 (`M-INF` for every `d<=7`).**  The `(6,2)` calculation becomes sound once (4.2) is actually proved, and `(6,3)` is a one-pair calculation.  The `(6,4)` step remains unsupported.  Thus the nodal degree-seven closure is not proved, and the first failure of the written method is degree six, not degree eight.

2. **CONFIRMED-AS-SHARPENED — `OPEN[PI1S4-D1-DEGREE]`.**  No promoted upper bound on `deg D_1` exists (C 506-511; I 81-85), and this remains the highest-leverage external gap.  The payoff should be updated: a bound `deg D_1<=5`, not merely `<=4`, closes the residual without a nodality hypothesis.  Following this review, any survivor has `d>=6`, `n>=2`, and `gcd(d,n)>=2`.

3. **CONFIRMED with arithmetic corrections — `OPEN[PI1S4-NONCOPRIME-GENERAL]`.**  Case-by-case inner-braid/factorization analysis is still open beyond `(4,2)` (C 513-520).  At `(6,3)`, the possible one-pair exponents `beta_1=7,8,10` give
   `e(iota)=4,2,-2`, not only `{2,4}`.  The `n|d` degree-six targets are `(6,2)` and `(6,3)`; `(6,4)` is not one.

4. **REFUTED-AS-TYPED / OPEN after narrowing — `OPEN[M-INF]`.**  The embedded-resolution identity can be closed by the induction in section 4.  The general scalar inequality cannot: the explicit `(6,4)` triple-point example violates it.  The safe residual is

   > `OPEN[M-INF-RESIDUAL-DOUBLEPOINT]`: for a residual polynomial curve with only double smooth-branch affine singularities and `a>=2`, prove `beta_h<=2d+n-2` (or directly `M_inf<=3d-3`).

   The identity `delta_aff=#(N minus S)` is available, but `S superset <d,n>` alone points in the wrong direction; additional delta-sequence or double-point structure must be proved and used.

5. **CONFIRMED — `OPEN[PI1S4-TANGENTIAL-NONCOPRIME]`.**  Nori 3.27 applies to nodes, not `A_(2k-1)` tangencies.  Neither equisingular-at-infinity nodalization nor the proposed extension from Nori's nodal hypothesis to `B(C)>0` is promoted (C 532-541).  This remains independent of the numerical `M` issue.

6. **CONFIRMED — `OPEN[OREVKOV-1990-CUSTODY]`.**  No official copy was obtained or consumed in the charged lanes (C 543-545; I 96-97).  Nothing promoted here depends on it.

**Leverage order.**  First seek a degree bound `d<=5`.  Failing that, the first concrete frontier is degree six: solve the outer/inner tuple problems and the residual-double-point `(6,4)` infinity bound.  General tangential transport remains a separate topology gap.

## 7. Promotion recommendations and corrected statements

### Coordinator provisional rows (I 69-77)

| Row | Verdict | Recommendation |
|---|---|---|
| (a) degree-`<=4` closure | CONFIRMED with dependency retyping | PROMOTE-AS-CORRECTED, sharpen to degree `<=5` |
| (b) `(4,2)` killed twice | CONFIRMED-AS-CORRECTED | PROMOTE; outer block equality already kills it, and Nori independently gives `pi_1=Z` |
| (c) nodal-coprime/Nori | CONFIRMED | Record as already promoted (I 42-45), not novel `PROVED-HERE` |
| (d) scalar/gap mechanism | SPLIT | PROMOTE the case-split scalar identity and the gap identity; HOLD the general bound and REFUTE the `(6,4)` proof |
| (e) NEGATIVE for `n|d` | REFUTED as stated | PROMOTE A'(1)-(4); replace the blanket claim by failure of the centrelessness *argument* only |

### Closure theorem rows (C 433-445)

| Row | Verdict | Exact promotion |
|---|---|---|
| 1 | CONFIRMED | Coprime + nodal implies `pi_1=Z` |
| 2 | CONFIRMED; stale label | Coprime + tangency allowed implies no prescribed `S_4` quotient; do not assert abelianness |
| 3 | CONFIRMED-AS-CORRECTED | `(4,2)` implies no prescribed `S_4` quotient and, independently, `pi_1=Z` |
| 4 | CONFIRMED conditionally | Nodal + actually verified `M_inf<=3d-3` implies `pi_1=Z`; list `(4,2)`, not `(6,4)`, as verified |

### Exact replacement statements

1. **Residual scope.**  In the repaired `N=4` residual, `D_1` is a singular polynomial curve with only double points of smooth branches, carries the stated `S_4` meridian representation, and satisfies `delta_aff>=1`.  In normalized coordinates, `d>n>=2`.

2. **Degree information.**  A surviving residual must have `gcd(d,n)>=2` and `d>=6`.  No promoted datum bounds `d` above.  If `d<=5`, the required `S_4` representation is impossible.

3. **Block theorem.**  Lemma 3.3 and Theorem A'(1)-(4) hold.  If `n|d`, all block products are equal and the block-product group is cyclic; this invalidates the automatic centrelessness deduction but does not decide every row.  At `(4,2)`, equality of the two products of two transpositions already rules out `S_4`.  The full fixed tuples satisfy `(ab)^3=1` and have image at most `S_3`, with the cabling-determined integer declared rather than free.

4. **Infinity resolution.**  If `a=1`, `M_inf=d` and `(M-INF)` is automatic.  If `a>=2`,
   `M_inf=max(d,a+beta_h-1)` and `(M-INF)` is equivalent to `beta_h<=2d+n-2`.  The formula `M_emb=a+beta_h-1` is promoted only together with the blow-up induction in section 4.

5. **Semigroup statement.**  `delta_aff=#(N minus S)` for `S={deg h:0!=h in C[p,q]}`, and `S superset <d,n>`.  This containment alone supplies no lower bound on `delta_aff`.  The residual `(6,4)` inequality is OPEN.

6. **Nori statement.**  For any irreducible one-place polynomial curve with affine nodes, an infinity resolution satisfying `M_inf<=3d-3` gives `pi_1(C^2-D)=Z`.  At degree four, the unconditional abelian specialization established here is the pair `(4,2)`; the tangential `(4,3)` conclusion is only no-`S_4`.

7. **OPENs.**  Retain `OPEN[PI1S4-D1-DEGREE]` as highest leverage, with target `d<=5`; retain the general noncoprime tuple problem and tangential-noncoprime transport; replace general `OPEN[M-INF]` by the residual-double-point version.  Do not promote the claimed nodal closure through degree seven.

## Primary sources fetched or checked

- Madhav V. Nori, “Zariski's conjecture and related problems,” *Ann. Sci. ENS* (4) 16 (1983), 305-344.  Official PDF streamed from `http://www.numdam.org/article/ASENS_1983_4_16_2_305_0.pdf`; SHA-256 `1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45`.  Proposition 3.27 is journal p. 331/PDF p. 28 and states the kernel used above is finitely generated abelian under the nodal/self-intersection hypotheses.

- Masakazu Suzuki, “Affine plane curves with one place at infinity,” *Ann. Inst. Fourier* 49 (1999), 375-404, DOI `10.5802/aif.1678`.  Official Centre Mersenne PDF streamed from `https://aif.centre-mersenne.org/item/10.5802/aif.1678.pdf`; SHA-256 `fe318bf54cdd9ac0346a7dbbaa13d8ec1813ad89fc19cd59448b5eedee551a26`.  Theorems 4-5 (pp. 400-404) were checked for the delta-sequence/semigroup conditions; no such theorem reverses the elementary gap-containment direction.

Orevkov 1990 was not fetched or consumed.  The two PDFs above were streamed to the hash/text tools and were not saved, preserving the one-report-only write constraint.

<!-- BODY-END -->
