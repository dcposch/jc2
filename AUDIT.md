# AUDIT.md — campaign evidence and trust-boundary ledger

This file began as the soundness audit of GGV Proposition 4.3 subcase (2), the
`(8,28)` family, and now carries promoted campaign claims and corrections. It
is not a live queue or avenue-ranking document; see `COORDINATION.md` and
`APPROACHES.md` for those roles.

> **SELECTED-Q8 FROZEN-`d4` POLYNOMIAL-`c` LANDING-CENTRE PROMOTION
> (2026-08-25 15:25Z).**  From the pinned six quotient rows
> `(e1,e3,e5,e7,e2,e4)`, substitute `d4=1,d2=2+u`, put
> `A=x3-2*x5`, and work over the polynomial ring
> `Q[w,u,x1,x3,x5,c]`.  For
> `C=I:(w*x5*A)^infinity`, the frozen Box02 `std/dp` endpoint computes
> `GC=std(C)` and then
> `GL=std(GC+(w,u,x1,x3,x5))=(1)`.  Since no polynomial in `c` is inverted
> and the centre does not specialize `c`, the selected horizontal closure in
> this frozen-`d4` slice has no landing at that centre for any finite
> geometric `c`.
>
> The scope-repaired V2 report SHA is
> `46a955fa0ef90b3b042b42fbeac7631171bb1e4b1537e7d09f53c3054eb887da`.
> Fresh read-only Grok review SHA
> `f5a985135c6e747e3a534d23af44604adbf26ea2ae39da2acba946db89f5406c`
> returns `CONFIRMED` with no repairs; its manifest/freeze SHAs are
> `1605d57f739c7a23b3bd1b6e0b69b75984cce90cc093bd7dbe6922358c43f5b3`
> and
> `b99cb20f828e5ffafc2d23c88b970835e482666540b2fe3b173742993169dfeb`.
> The original Box02 result manifest/freeze SHAs remain
> `5c3fa2d4235b4b21f4c9754e0038a94ce874ca14dfcdbf14ed99e29cfe588ac9`
> and
> `a716262617be8fa35eaab82f18f0f3909b7217b8567d17b2ce0fa1f768ecbdcb`.
> The historical output marker `C_PARAMETER_BASIS` encloses `GL`, not `C` or
> `GC`.
>
> **Firewall:** this is one host/engine/order and no original-generator
> cofactor identity or Box02 in-run version capture.  It proves neither
> `GC=(1)` nor global selected-open emptiness.  Moving `d4`, the rest of the
> rank-drop line and full `Hsrc`, coefficient and other projective infinity,
> Taylor/terminal realization, trajectories, all `(9,12)`, maximum twelve,
> and JC2 remain open.

> **TD6 `V=H=0,D(U)` SOURCE-UNIT PROMOTION (2026-08-25 15:02Z).**  In the
> fixed source-typed A3 section with
> `q_beta(t)=t+beta*t^2+t^25`, impose `V=H=0` and invert `U`.  Frozen V62D
> has exact ranks `38/132` at first stage and `37/94` at previous/pole stage.
> Previous compatibility rows 11 and 13 yield an exact direct original-row
> source certificate with unit residual; the normalized displayed Bezout
> pair has zero second weight, so the row-11 dependency alone already gives
> the contradiction.  Both the source-coefficient and pivot ledgers have
> radical support exactly `{U}`.  Two AWS executions agree on the proof
> artifacts byte for byte.
>
> Case manifest/freeze and producer-report SHAs are
> `a35040ee57baabe6e33260ea012ffb3e5c90513d0022b4cd746fd6f87c018120`,
> `7a8162981a690972574425e6bb905af71184bd0333b46666bb42f1446c0f6001`,
> and `52736b96b9b7fab88ae277e00039cb67ffbce7b2c1e976c31b3f7d897adc6322`.
> Hostile review SHA
> `ec0ada3d2508fcad7406472934b84ee3ec7c52d768a735264ac9f99a79231403`
> returned `CONFIRMED`.  The review notes that the certificate source-pins
> rather than embeds the original row polynomials and that its lightweight
> verifier is custody/marker-oriented.  These limitations forbid detached
> use of the witness but do not alter the exact pinned conclusion.
>
> **Licensed conclusion:** this closes only `V=H=0,D(U)` (the
> `V=0,D(U)` leaf) for all `beta` inside the fixed A3 q2 section.  It is not
> raw `U=0`, either `P3`/`QH` divisor, a whole-`H=0` cover, a whole-A3 or
> full-TD6 theorem, SP-2, landing, or JC2.

> **TD6 REPAIRED H-OPEN SOURCE-DAG PROMOTION (2026-08-25 14:12Z).**  In the
> fixed source-typed A3 section with
> `q_beta(t)=t+beta*t^2+t^25`, impose `H=C-3U^2=0`.  Frozen V64 exactly
> replays current row 13 through the single previous edge `('X-1',14)` and
> original first rows; the cached quadratic row `('X-1',0)` is a separate
> positive control and is not an N13 edge.  Genuine P12 has 2,885 terms, 28
> nonzero first rows, and 1,640 multiplier terms, replays directly through
> original first rows, and composes with `N13=(k/25)beta` to the unit residual
> `-k/50`.  Previous-14 omission, singleton-current omission, and live
> P12-without-N13 controls all fail as required.  The complete coefficient-
> leaf plus pinned-P12 denominator radical is exactly
> `{U,V,P3,QH}`, where
> `P3=V^4-32V^2U^3+128U^6` and
> `QH=V^4+8V^2U^3-64U^6`.
>
> The exact promoted scope is therefore **only**
> `H=0,D(U*V*P3*QH)` inside this fixed A3 q2-beta section.  The four divisor
> strata remain independent source-rebuild obligations; this is not a
> whole-`H=0`, whole-A3, TD6, SP-2, landing, or JC2 theorem, and it does not
> audit all unused rows.  Case manifest/freeze and producer-report SHAs are
> `51722a5dd366b29411487d2c7f38684172cc24332d04cc4b94772ca9cdf13222`,
> `b47493ab7e4626905d9d0cb2123193ff53b37ded996f69cc0fe4f741cfc552be`,
> and `096a3f67f22dc26a8e14dabfb920d1f45a8404af7b835050a015f344992afa39`.
> Hostile review SHA
> `e78af060f0feeabe90cf5bdbf26b19162d10deff7c41a0de029e0cbeca6bfb0f`
> returned `CONFIRMED`.
>
> The review preserves five non-theorem custody/scope nits: the declared
> 63-file `SOURCE.sha256` is not a 100-file archive inventory and omits the
> executed parent even though V64 hash-pins and recomputes that parent before
> import; the r6d IP is not embedded in run artifacts; the DAG lists the row-0
> lift-cache block before printing the explicit N13 restriction; the portable
> verifier is a custody/marker gate rather than algebra; and QH essentiality
> is not proved.  None licenses dropping QH or broadening the exact open.

> **AS CHRONOLOGICAL Q4 PROMOTION (2026-08-25 12:40Z).**  At exactly the
> three displayed source-replayed Q5 parents `0000`, `0270`, and `0513`, the
> complete 68-by-12 degree-five order-81 system (five Q4 divergence rows plus
> all 63 recomputed terminal rows) is consistent with rank pairs `4/4`,
> `8/8`, and `8/8` and kernel dimensions `8,4,4`.  Literal integer replay
> passes the 197 parent rows, Q4 modulo 243, and terminal degrees 7--12
> modulo 729.  The omission control shows that the five-row J-only section
> breaks two terminal rows at base `0270` and four at base `0513`.
> Producer/review SHAs are `8407cabc700df48ccde9ca894d5e6a8944434cc7de65403ff217ceddc4251b1a`
> and `6a77ff242a4d56461878a25dec7a3321e923f9c29a780ebad6e41d94f9fc6779`;
> the hostile verdict is `CONFIRMED`.  This promotion is pointwise at three
> Q5 parents.  It is not whole-Q5 coverage, Q3--Q0, a complete map modulo
> 243, an all-depth lift, a counterexample, or JC2.

> **AS CHRONOLOGICAL Q3 PROMOTION (2026-08-25 12:45Z).**  Consuming each
> complete displayed Q4 affine fibre above and adjoining order-81 homogeneous
> `(H4,J4)`, the exact 67-row Q3-plus-terminal systems are consistent with
> rank four and kernel dimensions `14,10,10`.  Exact division by 81 in
> degree three, by 243 in terminal degrees 7--12, full-cube affinity,
> particulars, kernel bases, omission controls, and literal integer replay
> were independently reconstructed.  The inherited Q4-kernel columns are
> identically zero at Q3; the ten-column `(H4,J4)` operator is identical at
> all three parents, so each Q3 fibre is the full Q4 fibre times a
> six-dimensional affine solution space.  Producer/review SHAs are
> `737b45f6509c959fa45a55158cdd705462f5de804827cf0c00e24ca0ffca7a31`
> and `81a9531d622b1f0ded90eb5701386ce059c6a60a24c4a469f9bff0d99281b973`;
> verdict `CONFIRMED`.  Degrees one and two remain at valuation three, so
> this is not Q2/Q1/Q0, a complete map modulo 243, whole-Q5 coverage,
> all-depth survival, a counterexample, or JC2.

> **AS DISPLAYED DEGREE-AT-MOST-THREE Q2/Q1 PROMOTION (2026-08-25
> 14:17Z).**  At each of the same three fixed Q5 predecessor points, consume
> the entire reviewed Q4/Q3 affine fibre and adjoin every displayed
> homogeneous degree-three, degree-two, and degree-one output digit at orders
> 27 and 81.  Constants are absent because their derivatives vanish.  The
> exact 91-row `/27` system has rank six on ten active coordinates and exactly
> 81 accepted assignments per parent.  On all `3*81=243` branches, the
> `/81` map is affine on every remaining displayed coordinate and
> inconsistent: row 8, `[x^2y]`, is identically zero in the remaining
> variables with residual constants `2,2,1` at parents `0000,0270,0513`.
> Added degree-one columns are not dummy variables: the trace pair changes
> the `/27` rank from five to six and the accepted count from 27 to 81;
> degree-one columns also change non-row-8 `/81` equations and lift ranks
> `6,7,7` to `7,9,9`, but none hits row 8.  Producer/review SHAs are
> `36e3d5e141ca48a1a23e07a7f179666456ad91b1bd69efdc6f473bc0a5fc5a16`
> and
> `922727b3224931f45533cb1d340653d9a1210c57a8ead3c918d7c90c3be14165`;
> verdict `CONFIRMED` for the explicitly displayed family.  The Gaussian
> parent remains pinned at producer/review SHAs `44834700...` / `47eaa4b...`.
> **Source-complete coverage still fails:** higher-degree order-27 digits,
> source reparametrizations, other carry directions, and the rest of the
> predecessor scheme are not covered, and the affine-output normalization
> lemma does not identify these three incomplete fibres with a global complete
> chart.  Therefore this is not complete Q3-fibre exclusion, not exclusion of
> three structural bases, not a `79 -> 76` reduction, and not a complete
> map/no-lift/counterexample/JC2 theorem.

> **AS GLOBAL Q9 ROW-8 SCALAR NON-OBSTRUCTION (2026-08-25 14:40Z).**
> Over all 79 compatible structural bases of the corrected current Q10
> source, the exact affine compiler reconstructs 33,225 Q10 states and
> 11,881 nonempty Q9 fibres, projects each complete 32-variable Q9 fibre to
> `(q1,q2,q3,q4)=(c2_1,c2_2,d2_0,d2_1)`, and evaluates
> `omega=carry(q1+2*q3)+2*h*carry(2*q2+q4) (mod 3)` with the corrected
> source orientation.  The frozen V2/V3 executions count
> `8,096,356,425,843` completions and exactly
> `2,698,785,475,281` occurrences of each scalar value; every nonempty fibre
> is `zero-partial`.  Producer/review SHAs are
> `2518c72bac173993ffe3f092da9f84f4b7b7a08411cc01762833c8e90ff40a93`
> and
> `903d11810ae57ac97161b7f2ef69f1d35df24b0fe1e0edd8ffba486f2d42281c`;
> the different-model verdict is `CONFIRMED`.  The original preregistration
> swapped the `x`/`y` carry labels; nonmutating erratum SHA
> `2b2fcef41a9d1b5d5dea788a50d7d288148214e28a39a4ac2d3e6da36cc4f9a5`
> and the corrected source/replay supersede it, while V1 remains a negative
> control.  V2 and V3 are separate executions of closely related code, not
> independent implementations.  **Licensed conclusion:** `omega` is not an
> obstruction at Q9 alone.  **Refused:** Q8-through-Q3 restoration, a
> complete map modulo 243, all-depth survival, a characteristic-zero point,
> a counterexample, or JC2.

> **AS THREE-FIBRE COMPLETE FIXED-D7 OUTPUT-CONE PROMOTION MODULO 243
> (2026-08-25 15:28Z).**  At each of the reviewed pinned Q3 fibres `0000`,
> `0270`, and `0513`, let
> `F=F_*+27U+81V`, where `U,V` range over every coefficient of both
> degree-at-most-seven output polynomials.  Equivalently, the compiler solves
> a 72-coordinate `Z/9` congruence module.  It imposes every one of the 91
> coefficients of `det J(F)-1` in total degrees zero through twelve and
> directly reconstructs an integer representative with determinant
> congruent to one modulo 243.  Fresh-fresh terms are multiples of 729; 72
> doubling controls, all 1,296 cross-component pairs, and the complete
> Q3-kernel/fresh mixed designs verify the exact linear/Bockstein reduction.
>
> The mod-3 rank/kernel is `27/45` at all three fibres.  Bockstein
> rank/kernel is `36/81` at `0000` and `43/74` at both `0270` and `0513`,
> yielding nonempty modules of sizes `3^81`, `3^74`, and `3^74`.
> Producer SHA is
> `9ac1edbb9a757addf4b8a4923b510cd63770e539a54156d6543cecabaa039cd4`;
> fresh different-model review SHA is
> `2322e0bc0b89280c567d8aecbdce4f42319faf0d8fba9265bea5a81936ffa869`
> with verdict `CONFIRMED`.  Case manifest/freeze SHAs are
> `7aba646cfc648a3c487160542006e3ca898a19ec42bff2adc738ac1a9f83a52d`
> and
> `379c072d60be55d83f62a0e4d86d7426d30a95f3175c7c625b9b8dc381e75b94`.
> The review independently traced the source chain, orientation, seed,
> degree support, Bockstein arithmetic, and exact three-fibre scope.
>
> **Firewall:** this proves complete order-27/order-81 fixed-D7 output cones
> only over the three displayed Q3 fibres.  It does not impose the next
> order-243 digits or terminal modulus 729, cover the whole Q5/global
> predecessor scheme, construct an all-depth `Z_3` lift, produce a collision
> or counterexample, or settle JC2.

> **Q8 RAW-OVERLAP ORDINARY/FITTING PROMOTION (2026-08-25 13:33Z).**
> On the pinned six-row source `I=(e1,e3,e5,e7,e2,e4)` restricted to
> `A3: w=x1=x3=x5=0`, let `M` be the six-by-three normal Jacobian in
> `(x1,x3,x5)` and `N=[M|F_w]`.  Two exact AWS engine/order lanes prove
> `I3(M)=((d2-d4-1)^2)` with its doubled scheme structure and the
> exact-rank ordinary-`delta w=1` incidence closures
> `K3=(d2,d4)`, `K2=K1=K0=(1)`.  Thus the only ordinary horizontal tangent
> locus is the line `d2=d4=0` with `c` free; there
> `dx1=dx3=dx5=0`, so the tangent stays in the boundary sheet.  The
> independent two-equation screen is
> `(d2-2*d4,d4*(d4-2))`; its other point `(4,2)` fails by
> `729*L7=-432`.  The doubled rank-drop line, including its rank-one point
> `(d2,d4)=(2,1)`, has no **ordinary** `delta w=1` tangent.
>
> Producer-report / case-manifest / replay-stdout SHA-256 values are
> `fca71aaa93f250eb1e13b70fb5abbe97875488fedb54c85abf1499fc31a247df` /
> `1045040f598f9b999738f718f792d1e0e126f8113b4a5412e30f6da1c37e5cf1` /
> `c80c5c62bff716a84ab0ea20d2787bd061fc8fceee80623682419a80d598c54a`
> for Fitting and
> `e421aec08ad53e72e77f872d4b518875cade6189d0880a5de0170f0305133dbe` /
> `a3f4cb3be0afe395966bcaba92ffde13b537bd36502d10db7556b39264a0d6be` /
> `009937d287e92e057b5e2562d510abde2d062cece42c102e68d5000c04b2a65c`
> for the tangent screen.  The immutable raw Grok review
> `6bdbd48a08e099f4ed3ef6e81078cf8b69fb65429f50b8235ee9a45b087abe67`
> has a text-corrupted preface but coherent mathematical sections 2--9; its
> nonmutating cleanup
> `0c29a5c19758257a3dd926865811ef73ef2ebe99adf8702313aa26822390d0f1`
> and separate read-only confirmation
> `449854242c96869698d93bea52f39be564a70f0322bba94bc681b4e5d4e2d02e`
> restore custody and confirm the verdict `CONFIRMED` without broadening.
> This is an **ordinary first-order/Fitting theorem only**.  It does not
> exclude ramified or weighted arcs, `delta w=0`, higher jets, the full
> selected saturation `I:(w*x5*(x3-2*x5))^infinity`, coefficient infinity,
> Taylor/terminal realization, trajectories, the whole `(9,12)` cell,
> maximum twelve, or JC2; all remain open.

> **Q8 FINITE-CYLINDER PROMOTION (2026-08-25 13:00Z).**  Exact independent
> AWS engines give rank five for the full
> six-row source Jacobian along
> `x5=d2=d4=0, x1=x3=a, c*a=1`, `a!=0`, while the contained cylinder has
> dimension two.  The resulting regular-local/domain argument identifies
> the source and cylinder germs and excludes landing from `D(x5)` at every
> finite point of that cylinder.  Producer/review SHA-256 values are
> `d33ba8c125ec32b74f18c67620d19a82484abcf558b0f1a9b3fc99bfe8ba2da1`
> and
> `6a55006112a55c2792844e2197fe88f1dadecc551d42006b334f0ad40d19d5a7`;
> the hostile verdict is `CONFIRMED`.  The computed unit minor is the
> five-by-five minor on source rows `(e1,e3,e7,e2,e4)` and columns
> `(d2,d4,x1,x3,x5)`; the dimension-drop step uses that regular local rings
> are domains, Cohen--Macaulay, and catenary.  This theorem says nothing about
> `a=0`, coefficient infinity, the overlap rank-drop strata, terminal/Taylor
> realization, other leaves, or JC2.

> **LATEST Q8 SPECIALIZATION FIREWALL (2026-08-25 11:49Z).**  The exact
> calculation in
> `xmodel/max12-912-order3-nu-q8-w0-localized-fibre-classification-20260825.md`
> (SHA-256
> `bb09d7dd5d2eda3aafda2272403e0cb2e6a03e43f657ee524929e5c88cf4e1d0`)
> classifies the naively specialized finite affine scheme at
> `w=0, x5*(x3-2*x5)!=0`.  Its hostile review (SHA-256
> `fa649cd0a799d7f8cdbd702cdbb02c2660b57d2fa674a7177c0a3307cfcc23e4`)
> found no mathematical hole in the length-eight scheme isomorphism, the
> `r6`/Jacobian unit claims, or the non-Q8 emptiness, but returned
> `CONFIRMED_WITH_REPAIRS` for custody and exact wording.  This theorem must
> **not** be cited as the special fibre of the closure of the punctured source
> until saturation by `w*x5*(x3-2*x5)` has been performed before
> specialization.  The exact successor computes
> `I:(w*x5*(x3-2*x5))^infinity`; raw finite and projective boundary jobs are
> controls only.  Separately,
> `(I+(x5*(x3-2*x5))):w^infinity` is the horizontal boundary incidence and
> does not by itself select irreducible components generically contained in
> that boundary.  No trajectory-landing, coverage, or JC2 conclusion may
> consume either overreading.

> **LATEST TD6 SCOPE QUARANTINE (2026-08-25 07:42Z).** This entry supersedes
> every same-day audit or note that claims or implies a whole/all-`beta`
> fixed-`A3` closure.  V43/V44/V45 prove exact `P12`/`N13` identities only on
> a common localization and explicitly do not include the full staged `N13`
> source lift; V34/V41 emit additional pivot denominators.  Consequently the
> generic-open, `H=0`, `B3=0`, and rational-line packages are quarantined from
> whole-atlas composition, although their immutable localized identities and
> custody remain valid.  The direct original-row `U=0` and V46
> `V=0, C=-U^2` incompatibilities do not consume that staged `N13` lift and
> remain valid at their stated narrow scopes.  Promotion now requires either
> a denominator-free full source identity or cleared localized identities
> with an explicitly replayed Bezout equation.  See the nonmutating erratum
> `xmodel/td6-c1-c2-c3-q2-n13-localization-scope-erratum-20260825.md`, SHA-256
> `4f6e2bf34cc7c4ea04f66e57a949fb04d4356941ee3762642ca050840f25e1b9`
> (case manifest/freeze SHAs `75c6cb496808ff0c9fd58f3988f6b556dd6c8951390c5573c64f4a2c101765ca`
> / `ea69b7a086d19a7b0448237d8f6b00ebb79abdcfc3c3c424b7ed450b5382d026`).

## Founding audit — GGV Proposition 4.3 subcase (2), the (8,28) family

> **SUPERSEDING EVIDENCE ERRATUM (2026-08-23).** On a characteristic-zero
> input, msolve 0.10.1's `-g` **unit-basis short circuit** can print `[1]`
> from the first machine-prime computation and return before CRT or rational
> reconstruction, while still printing
> `#field characteristic: 0`.  Consequently the archived characteristic-zero
> `[1]` outputs are modular trace evidence, not Gröbner bases or membership
> certificates over Q.  This supersedes the original Claim 6 inventory and
> every later proof-tier reading of the same output surface in this file.
> The files under `dist/jc72108-theory-bundle-v1/` are an immutable historical
> snapshot and still contain the superseded wording; they must be regenerated
> from the corrected canonical sources before any further distribution.
>
> The generic chart `chartG` remains an exact internal theorem because
> `jc72108/systems/open_8_28_c2_chartG.q.ms` itself contains the generator
> `-1`; its one-term certificate is independent of msolve.  No rational
> cofactor is archived for `cCa2` or `cCa6`, so the campaign's own three-stratum
> characteristic-zero proof is incomplete.  Finitely many modular unit
> ideals do not repair that gap without an effective bad-prime bound or a
> reconstructed rational certificate.  Separately, the full `(72,108)`
> exclusion retains exact characteristic-zero support from the independently
> replayed Helali and Suzuki artifacts documented in `jc72108/CROSSCHECK.md`
> and retained in `archive/crosscheck.tgz`; inference from those explicit
> systems to the degree family remains conditional on the GGV-Horruitiner
> reduction, normalization, and transcription bridge.

Audited claim (2026-08-01): **Subcase (2) of Proposition 4.3 of
Guccione–Guccione–Valqui/Horruitiner (arXiv:2204.14178) — the (8,28) family,
(deg P, deg Q) = (108,72), reduced to [P,Q] = x^2 with prescribed Newton
polygons — has no solutions over any field of characteristic 0.**

Proof skeleton being audited:

```
Prop 4.3 s2 statement                                  [trusted-external]
  → Generator A transcription        (lib/jc.py SystemA, cases/emit.py)
  → torus normalization fix_ones     (lib/jc.py, emit.py emit_normalized)
  → Cascade3 b-elimination           (lib/reduce3.py, moves from lib/reduce.py)
  → two_chart decomposition          (lib/chartelim.py two_chart)
      V(core) = V(chartG) ∪ V(core + prod(pivots))
  → kill-split of the complement     → cCa2 (a2:=0) ∪ cCa6 (a6:=0)
  → per-stratum evidence:
      chartG: exact symbolic −1 derivation + modular corroboration
      cCa2:   first-prime/mod-p [1] traces; no internal Q certificate
      cCa6:   first-prime/mod-p [1] reports; no internal Q certificate
```

Composition: a solution over any char-0 field K is a solution over the
algebraic closure K̄ (claim 1); it can be torus-normalized within K̄ (claim 2);
the normalized solution survives to the Cascade3 core (claim 3) and hence lies
in one of the three strata (claims 4, 5).  The intended final step requires a
Q-coefficient certificate `1 = Σ h_i f_i` on every stratum.  The internal
record supplies that step only for `chartG`, so this proof skeleton stops at
`cCa2`/`cCa6`.  The separate external exact-certificate route is summarized in
the erratum above.  Subcase (1) is **not** covered by this internal audit.

Verification-status legend:
- **proved-in-code** — the property is enforced by an assertion/test in the repo.
- **numerically-audited** — checked at random exact points; script may live
  only in session transcripts (flagged where so).
- **regression-validated** — the identical pipeline re-derives the known-empty
  solved cases (Props 4.1, 4.2, 4.4).
- **trusted-external** — imported from outside this codebase (GGV chain, msolve).

---

## Claim 1 — Generator A faithfully transcribes Prop 4.3 subcase (2)

**Statement.** The system `open_8_28_c2` (cases/emit.py:45-48) has solution set
(over any field) equal to the set of pairs (P,Q) demanded by Prop 4.3 s2 under
the conservative ("nonorigin") reading of the Newton-polygon convention, and
containing the solution set under the strict reading.

**Why it holds.**
- *Support = hull ∩ Z².* Unknowns are one coefficient per lattice point of
  hull(cornersP) and hull(cornersQ) (`SystemA.__init__`, lib/jc.py:143-199;
  `lattice_points`, lib/jc.py:113-139, with `ccw_order` asserting strict
  convexity). Any P with N(P) ⊆ polygon is representable; nothing outside the
  hull is allowed, exactly as in the Prop 4.3 shape constraint. Lattice counts
  for all four subcase polygons (25, 47 and, for subcase (1), 61, 125) are
  hand-verified via Pick's theorem in tests/test_jc.py:14-27.
- *Equations.* `E = bracket(P,Q) − x^2`; **every** coefficient of E over its
  full bivariate support is an equation (lib/jc.py:184-188). The bracket
  [P,Q] = P_x Q_y − P_y Q_x (lib/jc.py:92-94) is property-tested:
  antisymmetry, Leibniz, [x,y] = 1 (tests/test_jc.py:29-42), plus a
  known-solution substitution test (tests/test_jc.py:44-62).
- *Corner attainment.* The saturation equation t·∏(listed corner coeffs) = 1
  (lib/jc.py:190-199) forces every listed non-fixed corner coefficient ≠ 0.
  If all vertices of the polygon are attained, hull(supp) equals the polygon
  exactly — so saturation is precisely "N(P) = the stated polygon".
- *Origin convention ("nonorigin") and the strict reading.* In `nonorigin`
  mode the (0,0) coefficients are left unconstrained (lib/jc.py:190-195).
  Under GGV's convention that (0,0) always belongs to N(P), no origin
  constraint is the faithful reading. Under the strict reading ((0,0)
  coefficients also ≠ 0), the strict variety = nonorigin variety ∩
  {a_(0,0) ≠ 0, b_(0,0) ≠ 0} ⊆ nonorigin variety. **Emptiness of the
  nonorigin variety therefore settles both readings by inclusion** — this
  retired the separately-launched `_strict` runs (../notes.md, 2026-08-01
  entry). No extra compute needed.
- *Bracket sign convention.* If GGV's convention is the opposite sign, a
  GGV-solution satisfies our [P,Q] = −x^2; then (P, −Q) satisfies
  [P,Q] = +x^2 with identical support and corner nonvanishing. Emptiness is
  convention-independent (README.md "Semantics").

**Status.** proved-in-code (tests above) + regression-validated: the same
generator + pipeline re-discards all five solved cases — e.g.
reg_9_24_c3 core EMPTY [1] mod 65521 in 2.3 s (README.md; runs/
reg_9_24_c3_v6.p65521.out, reg_9_24_c3_chartG/chartC.p65521.out, all
basis-length 1). The *statement* transcribed (polygon data, subcase split,
rhs x^2) is trusted-external (claim 8); the corner data in emit.py was
transcribed by hand from the paper and has no independent machine check —
see obligations.

---

## Claim 2 — Torus normalization is lossless for emptiness

**Statement.** Let k = 2 (rhs x^k). Over an algebraically closed field, the
system `open_8_28_c2_n` — which fixes coeff_P(8,16) = coeff_Q(12,24) = 1
(`FIX`, cases/emit.py:79-80) — is empty iff `open_8_28_c2` is empty.

**Why it holds (the lemma, stated precisely).** For λ, α ∈ K̄^× let
φ_λ(x,y) = (λx, μy) with **μ = λ^−(k+1)**, and act by
(P,Q) ↦ (α·(P∘φ_λ), α^{−1}·(Q∘φ_λ)).
- The chain rule gives [P∘φ, Q∘φ] = λμ·([P,Q]∘φ) = λ^{−k}·([P,Q]∘φ), and
  [P,Q] = x^k ⇒ ([P,Q]∘φ) = λ^k x^k, so the transformed pair again satisfies
  [P,Q] = x^k. The α-scaling preserves the bracket exactly. Supports and
  corner (non)vanishing are preserved.
- The coefficient of P at (i,j) is multiplied by α·λ^w, and of Q by
  α^{−1}·λ^w, with weight **w = i − (k+1)j**. Given a solution with
  c_P := coeff_P(8,16) ≠ 0 and c_Q := coeff_Q(12,24) ≠ 0 (both are non-origin
  listed corners, forced ≠ 0 by saturation), we need
  αλ^{w_P}c_P = 1 and α^{−1}λ^{w_Q}c_Q = 1. Multiplying:
  λ^{w_P+w_Q} c_P c_Q = 1. Here w_P = 8 − 3·16 = −40, w_Q = 12 − 3·24 = −60,
  so w_P + w_Q = −100 ≠ 0 and λ exists in K̄^× (algebraic closure supplies a
  100-th root); then α := (λ^{w_P}·c_P)^{−1} settles both equations.
  So every solution is torus-equivalent to a normalized one; conversely a
  normalized solution is a solution. Hence emptiness transfers both ways
  **over algebraically closed fields** — sufficient, since claim 1's
  composition passes through K̄.

**Why the hypothesis is machine-checked.** `emit_normalized` computes
det = (i_P − (k+1)j_P) + (i_Q − (k+1)j_Q) and **asserts det ≠ 0**
(cases/emit.py:87-89; here det = −100); `SystemA` asserts fix_ones points are
listed corners (lib/jc.py:166-167). The lemma statement is recorded in the
`fix_ones` docstring (lib/jc.py:154-160).

**Status.** Lemma: pen-and-paper (above; not yet in any test). Hypothesis
det ≠ 0: proved-in-code. Pipeline behavior on normalized systems:
regression-validated (all `_n` solved cases re-discarded).

---

## Claim 3 — Every Cascade3 move preserves the corner-localized variety

**Statement.** Let W = { points with all Generator-A equations = 0 and every
listed non-fixed corner coefficient invertible }. Each Cascade3 step
(lib/reduce3.py) replaces the current system by one whose solution set is in
natural bijection with W projected along eliminated variables; in particular
W = ∅ iff the final core system is empty.

**Why it holds.**
- *Setup.* Cascade3 drops the degree-7 t-saturation and instead adjoins
  c·ic − 1 = 0 for each corner variable c (lib/reduce3.py:28-34).
  Equivalence: ∃t with t·∏c_i = 1 ⟺ ∏c_i ≠ 0 ⟺ each c_i ≠ 0 ⟺ ∃ inverses.
  Same (a,b)-projection, so emptiness is unaffected. `units` = corner vars +
  their inverses; these are invertible at every point of W.
- *M1 (contradiction).* An equation reduced to a nonzero rational constant,
  or to k·m with k ∈ Q^× and m a product of units, has no zeros on W
  (units invertible) → status EMPTY (lib/reduce3.py:56-64; semantics
  documented in lib/reduce.py:6-9). Over Q, "k ≠ 0" is exact.
- *M2 (monomial zero-forcing).* Equation k·m = 0 with exactly one distinct
  non-unit variable v in m (any multiplicity e): at a field-valued point,
  units cancel and v^e = 0 ⇒ v = 0. Substituting v := 0 everywhere
  (`_kill_var`, lib/reduce.py:43-45) is an isomorphism onto W ∩ {v = 0} = W.
- *M3 / b-pivot elimination with unit-monomial pivots.* `_pick_pivot`
  (lib/reduce3.py:107-126) accepts a b-variable v only if: v occurs in the
  chosen equation in a single monomial m0, to the first power, and every
  other factor of m0 is a unit. Then the equation reads q·u·v + rest = 0
  with q ∈ Q^×, u a unit monomial — invertible at every point of W — so
  v = −u^{−1}·rest/q =: g is *forced*. u^{−1} is realized polynomially as
  the mirror product of inverse variables (`invmon`, lib/reduce3.py:138),
  and `_inv_reduce` (lib/reduce3.py:92-105) rewrites c·ic → 1, i.e. reduces
  modulo the adjoined relations — sound as functions on W. Forgetting v is
  then a bijection (solutions of new system) ↔ (solutions of old), inverse
  v := g(point). Emptiness preserved in both directions.
- *Termination and b-linearity.* Generator-A equations are bilinear (each
  monomial has ≤ 1 a-var and ≤ 1 b-var, degree ≤ 1 each, because P is
  a-linear and Q is b-linear in their coefficients). Eliminating only
  b-variables keeps every monomial b-degree ≤ 1 forever — substitutes are
  never raised to powers (`_subst_linear`, lib/reduce3.py:81-90; module
  docstring lines 1-13) — so each pivot really is a linear solve and the
  cascade ends after ≤ #b steps. a-degrees may grow (harmless: msolve takes
  over on the core). The MAXTERMS_EQ guard only *aborts* (status
  "aborted-swell"); an aborted mid-cascade state is still a sound system.
  For open_8_28_c2 the cascade completed; the two Q-corner variables b3
  (2,1) and b43 (12,21) are the only surviving b's, since pivots skip units.
- *The ghost audit.* The elimination log (`C.elim`, list of (v, g)) was
  audited numerically: sample random exact points of the core, reconstruct
  every eliminated b ("ghost" variables) by back-substitution through the
  log, and evaluate the **original** Generator-A equations — all vanish.
  This checks the bookkeeping (`_subst_linear`/`_inv_reduce`) end-to-end.

**Status.** Move-level arguments: pen-and-paper (above; module docstrings
state them). Bookkeeping: numerically-audited — but the ghost-audit script
exists only in session transcripts (no "ghost" artifact is committed to the
repo; searched 2026-08-01) → obligation. Whole cascade:
regression-validated (solved cases stay EMPTY through the same path).
Field caveat: M1/M2 verdicts and all Fraction arithmetic are exact over Q;
transfer to F_p additionally needs p to divide no cleared numerator or
denominator (see claim 6 caveat).

---

## Claim 4 — The two_chart identity

**Statement.** For the finished core C,
`two_chart(C)` (lib/chartelim.py:54-99) returns leaves (chartG, chartC) with
**V(core) = π(V(chartG)) ∪ V(chartC)**, where chartC = core equations +
prod(pivot coefficients) = 0, and π forgets the fresh u-variables. Hence
core empty ⟺ both leaves empty.

**Why it holds.** For each remaining b (here b3, b43), a pivot equation is
split as coeff·b + rest = 0 with b strictly linear (monomials with b-degree
≥ 2 disqualify the equation, lib/chartelim.py:68-76 — vacuous here by claim
3's b-linearity, but re-checked). The generic leaf adjoins a fresh u with
**u·coeff = 1** and substitutes **b := −u·rest**, dropping the pivot
equation (lib/chartelim.py:83-95); chartG for open_8_28_c2 gained u75, u76
(visible in the emitted variable order, runs/open_8_28_c2_chartG.q.out).
- (⊇) A chartG-point defines b := −u·rest; substituted equations hold by
  construction, and the dropped pivot equation holds:
  coeff·(−u·rest) + rest = rest·(1 − u·coeff) = 0. A chartC-point is
  literally a core point. So both leaves map into V(core).
- (⊆) At a core point, either every chosen pivot coeff is ≠ 0 — set
  u_i := coeff_i^{−1}; the pivot equations force the b's to the substituted
  values, giving a chartG-point — or some coeff = 0, so
  prod = ∏ coeff_i = 0 (lib/chartelim.py:94) and the point lies in chartC.
- *Caveat (checked for this run).* In general a later pivot coeff could
  involve an earlier u, which would make chartC's added generator ill-posed;
  in the open_8_28_c2 run both chosen pivot coefficients were single
  monomials in original core variables (`info` records length 1 for each),
  so prod is a genuine core-variable monomial. The general-position code
  does not enforce this — flagged in obligations.

**Status.** Identity: pen-and-paper (docstring lib/chartelim.py:55-58 states
it). Instantiation for open_8_28_c2 (monomial pivots, two u's):
numerically-audited via the claim-7 point audit (chartG points reconstruct
to original solutions) and regression-validated (reg_9_24_c3 chartG/chartC
both EMPTY [1], runs/). The exhaustive-branching variant `eliminate_bs`
(lib/chartelim.py:101-170) was not used for the final decomposition.

---

## Claim 5 — The kill-split of the complement

**Statement.** For open_8_28_c2 the pivot product is a monomial
prod = (unit factors)·a2^α·a6^β with α, β ≥ 1, so
**V(chartC) = V(core + a2) ∪ V(core + a6)** — the emitted kill-branches
cCa2 (a2 := 0) and cCa6 (a6 := 0). chartC empty ⟺ both branches empty.

**Why it holds.** On the corner-localized locus every unit factor of prod is
invertible, and field points have no zero divisors, so prod = 0 ⟺ a2 = 0 or
a6 = 0. Substituting a2 := 0 (resp. a6 := 0) into the core is an isomorphism
onto V(core) ∩ {a2 = 0} (a2, a6 are interior P-coefficients, not corner
variables, so no saturation forbids their vanishing). Evidence that the
emitted systems are exactly these substitutions: the variable line of
systems/open_8_28_c2_cCa2.*.ms omits a2 (and keeps b3, b43, ia1, ia22, ib3,
ib43), that of open_8_28_c2_cCa6.*.ms omits a6; both otherwise agree with
the core.

**Status.** Identity: pen-and-paper (elementary). Instantiation:
numerically-audited/reconstructed — the split-emitter session script is
**not committed** (systems/ artifacts + ../notes.md 2026-07-30 entry are the
record; prod's exact unit part and exponents α, β are not archived) →
obligation. Union coverage chartG ∪ cCa2 ∪ cCa6 = full reduced variety is
asserted in ../notes.md (2026-07-31) and follows from claims 4 + 5.

---

## Claim 6 — What the archived msolve `[1]` output actually certifies

**Correct algebraic criterion.** If a rational Gröbner basis calculation or
an independently verified identity really establishes `1 ∈ I ⊂ Q[vars]`,
then `1 = Σ h_i f_i` for rational cofactors and the stratum has no point over
any characteristic-zero field.  The localization equations in these systems
make ordinary ideal membership the right criterion.

**The archived output does not establish that premise.** In msolve 0.10.1,
the characteristic-zero `-g` path starts at a machine prime.  If that modular
basis is `[1]`, the unit-basis branch can return before multimodular
reconstruction; the printer nevertheless repeats the input characteristic as
zero.  Thus a complete header followed by `[1]:` authenticates a completed
first-prime calculation, not a basis over Q.  This warning is specific to the
unit short circuit: a successful non-unit characteristic-zero run continues
through CRT/rational reconstruction, and its printed non-unit basis remains a
Q-level result within the ordinary trust placed in the engine.

**Corrected inventory:**

| stratum | archived `-g` trace | exact internal Q certificate | modular corroboration |
|---|---|---|---|
| chartG (27 vars) | char-0 header + first-prime `[1]` | **YES:** literal generator `-1`, one-term cofactor | `[1]` at the recorded primes |
| cCa2 | char-0 header + first-prime `[1]` | **NO:** Singular lift timed out; `jc72108/runs/cCa2_lift.txt` is empty | `[1]` at the recorded primes |
| cCa6 | historical fleet report of the same output surface; no local Q output | **NO:** lift not attempted/completed | historical multi-prime `[1]` reports; local p-output is not archived |

The cCa2 and chartG `.q.out` files contain only the eight-line header and
`[1]:`; they contain neither a rational basis reconstruction nor cofactors.
No cCa6 rational output is present locally.

**Why several primes still are not a proof.** A characteristic-zero system
can become the unit ideal at finitely many exceptional primes.  For example,
`(p_1 p_2 p_3 x - 1)` has a rational zero but reduces to the unit ideal at
each `p_i`.  Therefore two, three, or any other fixed finite number of
modular `[1]` verdicts is corroborating evidence only unless their size or
product exceeds a proved effective bad-prime bound, or the modular data are
reconstructed and verified as an exact rational certificate.  The bounds
calculated in `jc72108/CERT-UPGRADE.md` put the banked primes far below such a
threshold.

**Mod-p caveat.** The historical `leaf_to_msolve` path also lacked a guard
against coefficient loss during per-equation denominator clearing.  Later
reduced re-emissions strengthen the modular evidence but cannot promote it to
characteristic zero.

**Status.** `chartG` is theorem-grade internally.  `cCa2` and `cCa6` are
modular/trace-grade internally.  Exact characteristic-zero exclusion of the
full external case-2 coefficient system is supplied separately by the Helali
replay in `jc72108/CROSSCHECK.md`; it is not a cofactor certificate for these
two internal chart ideals.

---

## Claim 7 — The symbolic −1 on chartG, and its numeric audit

**Statement.** On the generic chart, the Cascade3 + two_chart substitution
chain reduces **original Generator-A equation #3** (one explicit coefficient
of [P,Q] − x^2) to the constant −1. Hence chartG is empty by pure algebra —
a theorem-fragment independent of F4 — valid over every field in which the
chain's denominator primes are invertible (so over all char-0 fields, and
all F_p away from finitely many explicit primes).

**Why it holds.** Each step of the chain multiplies by explicit units and
performs the forced linear substitutions of claims 3-4, so it is an
ideal-membership derivation: −1 ∈ I(chartG) with an explicitly recomposable
cofactor chain. The artifact systems/chartG_culprit.sing contains the chart
system with the literal generator −1 as its first entry; Singular's
lift(I,1) on the chart accordingly succeeded instantly with a **1-term
cofactor** (1 = (−1)·(−1)) — trivial, because the unit is already a listed
generator, but it confirms the emitted system is the one carrying the
symbolic contradiction.

**Numeric audit** (../notes.md, 2026-07-30 AUDIT MILESTONE): at 6 random
exact-rational chart points, using **only** the original equations plus the
stored substitution logs: equation #3 evaluates to exactly −1 at all 6
points; 51/92 pivot equations vanish identically; no other equation reduces
to a nonzero constant. Exact rational arithmetic — no rounding. Regression
contrast: the solved case's chartG exhibits **no** such collapse (its
emptiness needed real F4), so the collapse is a structural feature of
(72,108) s2, not a pipeline artifact.

**Status.** numerically-audited (6 exact points; audit script transcript-only
→ obligation). The standalone-lemma write-up (which bracket coefficient
equation #3 is; the substitution chain as a self-contained derivation) is
owed (../notes.md TODO). Once written, this upgrades chartG to
proved-on-paper, independent of msolve.

---

## Claim 8 — TRUST BOUNDARY (explicit)

Everything above reduces the headline claim to the following trusted inputs:

1. **GGV Prop 4.3 itself** — that the (108,72) Jacobian pair analysis
   reduces to the two stated subcases with those polygons, corners, and
   [P,Q] = x^2, including the internal branch bookkeeping of the §4 proof
   (subcases (1)+(2) exhausting the family). Unverified here; parts of the
   supporting chain (1401.1784 / 1605.09430 / 1406.0886 / 1708.07936 /
   2204.14178) are **arXiv-only/unrefereed**; the published J. Algebra
   version of 1401.1784 omits Cor. 7.12 (Heitmann JPAA 64 (1990) Thm 2.24
   covers it independently) — see ../plan-72-108.md "Risks"/"Phase 0".
   Exact arXiv versions must be pinned in any writeup.
2. **msolve correctness for the modular screens.** The recorded `[1]`
   verdicts are first-prime/mod-p evidence.  Agreement at 2-3 primes and on
   two machines mitigates implementation accidents but does not turn those
   screens into a characteristic-zero certificate.
3. **Steps still lacking machine-checkable certificates:**
   - Cofactor certificates 1 = Σ h_i f_i: **chartG — obtained** (trivial
     1-term lift, systems/open_8_28_c2_chartG.lift.sing / chartG_culprit.sing);
     **cCa2 — Singular lift(I,1) TIMED OUT** (runs/cCa2_lift.txt is empty;
     input systems/open_8_28_c2_cCa2.lift.sing); **cCa6 — lift not
     attempted**. Until cCa2/cCa6 lifts (or an equivalent reconstructed
     certificate) exist and are re-verified by an independent exact checker,
     those two internal strata have no characteristic-zero proof.
   - Cascade3 / two_chart / kill-split correctness: mathematically argued
     (claims 3-5) and numerically audited, but the audits are
     session-transcript-only and there is no formal write-down and no
     committed re-runnable audit script.
   - The Prop-4.3-to-emit.py polygon transcription (claim 1) has no check
     against the paper other than eyes + the lattice-count tests.
4. **Not** in the trust boundary: torus normalization (claim 2, self-
   contained lemma + asserted hypothesis), the strict-vs-nonorigin
   convention question (settled by inclusion), and the bracket sign
   convention (settled by negation).

5. **Separate external completion.** `jc72108/CROSSCHECK.md` records exact
   Helali and Suzuki replays for both Proposition-4.3 subcases, with the
   archived bundles retained in `archive/crosscheck.tgz`.  Those certificates
   preserve the conditional `(72,108)` exclusion without using the internal
   cCa2/cCa6 traces.  Their perimeter is the faithful normalization and
   transcription of the explicit coefficient systems and the correctness and
   exhaustiveness of the upstream GGV-Horruitiner Proposition-4.3 reduction;
   the lower
   bound 125 additionally uses the upstream enumeration saying this is the
   sole remaining family below 125.

---

## Remaining obligations before any public claim

- [ ] **Commit the audit scripts**: ghost audit (claim 3), 6-point symbolic
      audit (claim 7), and the chart/kill-split emitter session code
      (claims 4-5), as re-runnable tests under tests/.
- [ ] **Write the standalone −1 lemma** for chartG: identify equation #3's
      bracket position, lay out the substitution chain, state the excluded
      denominator primes (upgrades chartG to paper-grade).
- [ ] **Certificates for cCa2 and cCa6, if a self-contained internal proof is
      still desired**: rerun cCa2 lift with more
      time/memory or extract cofactors by other means; attempt cCa6 lift;
      then verify all three certificates with the independent FLINT/Nemo
      checker (../plan-72-108.md Phase 4).
- [ ] **Second GB engine** (Singular/Macaulay2/Groebner.jl) reproducing
      [1] at one prime for each stratum — removes single-engine risk even
      before lifts land.
- [ ] **Archive fleet trace artifacts** into runs/: cCa6 first-prime and p-run
      outputs, third-prime outputs, with full headers, initial-prime logs,
      input hashes, random seeds, msolve versions, and host info.  Do not label
      a characteristic-zero-header `-g` output as a Q certificate.
- [ ] **Prime-hygiene check**: verify no cleared numerator/denominator in
      any emitted stratum system vanishes mod 65521 / 1048573 / 2147483629;
      add the missing guard to `leaf_to_msolve`.
- [ ] **Record prod(pivots)** exactly (unit part, α, β) from a committed
      re-run of the two_chart step; assert its non-unit support is {a2, a6}.
- [ ] **Formal write-down** of claims 2-5 as lemmas with proofs (this file
      is the outline; ../notes.md flags the write-down as owed).
- [ ] **Pin arXiv versions** of the GGV chain; flag unrefereed links; note
      the Prop 4.3 dependency explicitly in the writeup; optionally probe
      the raw unreduced formulation for partial independence (char-0 lane,
      README "Findings").
- [ ] **Subcase (1)** — not an obligation for *this* claim, but required
      before any "(72,108) family discarded / bound = 125" statement.
      Scope discipline: the public claim matching this audit is
      "Prop 4.3 subcase (2) is empty over char 0, conditional on Prop 4.3".

## Committed artifact — pivot product (obligation 1, recorded 2026-08-02)
Deterministic re-run of Cascade3(level_dir=(2,1)) + two_chart on
open_8_28_c2 (nonorigin, fix_ones per FIX):
  prod(pivots) = -1/5 * a2((1, 1))^2*a6((2, 4))*ia1^2*ib43
Non-unit support asserted == {a2 (P-point (1,1)), a6 (P-point (2,4))} — PASSED.
Hence V(complement) = V(core + a2*a6 = 0) = V(core, a2=0) ∪ V(core, a6=0),
which is exactly the cCa2/cCa6 split used throughout.

## Pinned external versions (obligation 3)
- arXiv:2204.14178v1 (GGV-Horruitiner, 29 Apr 2022) — Prop 4.3, THE dependency.
- arXiv:1401.1784 (GGV; J. Algebra 471 (2017) 13-74 — journal omits Cor 7.12).
- arXiv:1605.09430, arXiv:1406.0886, arXiv:1708.07936 — arXiv-only (unrefereed).
- msolve (Homebrew build, local; git master built 2026-07-27 on ultramem/jc-b).

## msolve parenthesis hazard (2026-08-09)

SHEET6-R1-REVIEW.md discovered msolve 0.10.1 SILENTLY MIS-PARSES
parenthesized polynomial input (micro-test: `x-(3+1)` yields GB `[x+1]`).
Sweep of all 401 shipped .ms files (systems/**, recursive): exactly ONE
contained parentheses — systems/r1/r1_gmband_core.ms (the new R1 engine's
emission; its EMPTY verdict retracted on this + independent grounds).
ALL 400 other systems (72,108 leaves, farm, dc2, sheet6) are fully
expanded monomial sums — no parentheses — so every prior verdict stands.
Standing rule added: .ms emitters MUST emit expanded monomial sums only;
any new emitter gets the paren-sweep + a satisfiability smoke test
(constant-term row check: a system whose rows all lack constant terms
cannot be [1] — guard against impossible verdicts) before its verdicts
are banked.

## msolve mod-p coefficient-reduction hazard (2026-08-10)

### The hazard, and its TRUE boundary (established by micro-test)

SHEET6-R1-25LOCUS.md §4b discovered that feeding msolve 0.10.1 a p>0
char line with char-0-style bignum coefficients silently corrupts the
system (r1_25chain_core: spurious GB=[1] at three primes; the same
system with coefficients pre-reduced into [0,p) gives the correct
487-elt GB). Root cause isolated TODAY by micro-test (/tmp/redtest):
**msolve's integer-token parser clamps at LONG_MAX = 2^63-1
(9223372036854775807)**. Verified: `x+9223372036854775807*y` parses to
exactly the LONG_MAX value mod p, and every larger token (2^64, a
9.6e21 coefficient from the c1 leaves) parses to the SAME clamped
value — silently, exit 0. Conversely, coefficients in [p, 2^63) are
reduced correctly mod p at parse time: unreduced-vs-reduced twin files
at magnitudes 65522 / 445440 / 1337656320 produce BYTE-IDENTICAL
Gröbner bases. So the corruption condition is
  some |coefficient| > 2^63-1  (NOT merely >= p),
though the standing rule below mandates full reduction into [0,p)
regardless, because relying on the parser's internal reduction is
exactly the kind of trust this campaign does not extend.

### 110-file inventory (full scan of systems/**/*.ms, 2026-08-10)

Scan: line 2 read as char, every integer token of the body compared
against it (chunked streaming reader; full list with per-file class
and max coefficient BANKED at ops/modp_contam_inventory_20260810.txt).
110 files have char p>0 and max coefficient >= p, splitting at the
true hazard boundary into:

- **49 CORRUPT-class (max coeff > 2^63-1 — msolve genuinely mangles):**
  - 16 systems/c1_* leaf files at p65521 (max 9.6e21 / 1.6e21);
  - systems/open_8_28_c1_v6.p65521.ms (1.6e21);
  - 3 systems/ordtest_*.ms (1.6e21);
  - systems/reg_7_21_partial.p65521.ms, reg_9_27_partial.p65521.ms;
  - 27 systems/farm/* p65521 partial/core files (max up to 9.3e30),
    ALL 27 dispatched in the live farm queues (14 box01 + 13 box02
    per systems/farm/queue/*/queue.txt).
- **61 word-sized (p <= max coeff < 2^63 — msolve parses correctly;
  hygiene violations, not corruptions):** the open_8_28_c2 stratum
  files (cCa2/cCa6/chartC/chartG/v6/v6s at p65521 and p1048573, max
  1.34e9), the reg_9_24_c3 mod-p suite, reg_9_24_c1/c2_v6.p65521,
  24 systems/conjE/*.p65521.ms (max 67200), 14 farm files
  (4_12mn34d64, 9_24mn23d99, 7_42*_c1_partial).

systems/r1/* mod-p emissions: ALL verified reduced (max coeff < p) —
the R1 rebuild's emitters already reduce; every R1 mod-p verdict in
SHEET6-R1.md §8.20/§10.3/§10.5/§11 used clean inputs. dc2, zheglov,
sheet6-engine systems: zero hits (exact-arithmetic or char-0 lanes).

### Cross-reference: does ANY accepted campaign verdict rest on these?

This subsection audits the separate integer-token/parser hazard only.  Its
"clean" labels do **not** authenticate characteristic-zero `[1]` output; the
2026-08-23 superseding erratum applies independently.

**VERDICT: NO accepted campaign verdict rests on a corrupted input.
Contaminated-verdict count = 0.** Per relied-upon verdict class:

1. **(72,108) subcase (2) — the claim-6 inventory.** The char-0-header
   files are outside this parser hazard, but only `chartG` has an internal
   exact certificate; cCa2/cCa6 are first-prime traces. The mod-p
   corroboration lanes at p=65521/1048573 DID use unreduced files,
   but all are word-sized (max 1.34e9 < 2^63): msolve parsed the
   intended systems. Re-verified empirically today (see re-runs). The
   third prime 2147483629 > 1.34e9: those emissions are reduced by
   construction. chartG additionally rests on the symbolic -1 (claim
   7), msolve-free. The full subcase-(2) characteristic-zero verdict stands
   via the separate exact Helali/Suzuki record, conditional on the shared
   reduction/transcription bridge; it does not stand on the internal msolve
   traces.
2. **(72,108) subcase (1).** The 16 c1_* leaves + open_8_28_c1_v6
   ARE corrupt-class — but produced NO accepted verdict: every c1
   lane run died without verdict (notes.md 2026-08-06/07: Xeon all-Z
   leaf FAILED at 940GB/30h; ultramem I-leaf retired; leaf program
   CLOSED, novelty rule). Subcase (1) is settled via the EXTERNAL
   Helali + Suzuki artifacts (CROSSCHECK.md): Helali = gmpy2/flint
   exact char-0 number-field certificates, Suzuki = exact char-0 +
   F_23 descent with recorded pivot residues, byte-identical
   regeneration — NEITHER uses msolve or unreduced mod-p input.
   **The c1 corruption never touched an accepted verdict.**
3. **Regression/validation verdicts.** reg_9_24_c3 mod-p suite
   (14/14 G0 sweep) used word-sized files — parsed correctly;
   re-verified today. reg_7_21/reg_9_27 partials are corrupt-class
   but no completion/verdict was ever banked for them (G0 stands at
   3/5 via other lanes). ordtest_*: runs errored (runs/ordtest_*.err),
   no verdicts.
4. **Sheet-6 R1.** All r1 mod-p files reduced (see above), so their modular
   verdicts are clean with respect to this parser hazard.  The claimed
   characteristic-zero upgrades for the ZU/UZ leaves, Q0 family/control, and
   Q2 l13 stratum used the same first-prime `-g` output surface and are
   reclassified as modular/trace evidence absent exact cofactors.  In
   particular, the active l13 "proof-tier" base and its characteristic-zero
   downstream consequences are open.
5. **conjE.** The 96 characteristic-zero-header `[1]` files are first-prime
   traces, not rational Gröbner certificates.  `CERT-UPGRADE.md` gives an
   exact two-row identity for the `(i,ell)=(1,1)` B-subset family; the other
   five reported HOLD rows remain modular/trace-grade.  None proves
   Conjecture E or is load-bearing for a global JC2 conclusion.
6. **Farm (deg<=150 frontier).** The ONLY at-risk class with live
   verdict exposure: 27 corrupt-class p65521 jobs are in the remote
   queues, and the boxes bank smallest-first — the early banked
   EMPTYs (box01 6 EMPTY, jc-b 9 outputs as of 2026-08-10, not yet
   pulled locally) plausibly include corrupt-class jobs (e.g.
   7_42*_c3_core.p65521 at 5.1MB, 8_28mn32d108_c1_core.p65521 at
   15.7MB are among the smallest). No farm verdict is yet relied upon
   in any headline claim (README farm checkbox is open), so the
   contaminated-ACCEPTED-verdict count stays 0 — but **ACTION
   REQUIRED at next fleet poll: quarantine every farm mod-p verdict
   whose input is in the 27-file corrupt list; re-emit those inputs
   reduced (ops/reduce_msp.py) and re-queue.** Sizing: 27 files,
   4.3GB total (largest 593MB 12_36mn32d144_c1_partial); .q.ms
   char-0 twins and the 14 word-sized farm files are unaffected.

### Re-runs performed today (reduced re-emissions, local msolve -g 2)

Reducer: ops/reduce_msp.py — reduces every non-exponent integer token
into [0,p); built-in guard = independent-parser round-trip (exact
bignum evaluation of every row at 2 random points mod p, original vs
reduced, plus no-token->=p and row-count asserts). All 12 emissions
guard-PASS (systems/redcheck/), outputs banked in runs/redcheck/:

| system (reduced) | result | vs banked original |
|---|---|---|
| open_8_28_c2_chartG.p65521 | [1], <1s | header+verdict IDENTICAL |
| open_8_28_c2_cCa2.p65521 | [1], 291s | matches banked [1] |
| open_8_28_c2_cCa2.p1048573 | [1], 277s | matches fleet [1] |
| reg_9_24_c3_v6/chartG/chartC .p65521 | [1], 0-3s each | IDENTICAL |
| reg_9_24_c3_v6/chartG/chartC .p1048573 | [1], 0-3s each | matches |
| conjE i3l2B12 / i3l3B6x9 .p65521 | [1], <1s | matches |
| open_8_28_c2_cCa6.p65521 | TIMEOUT 1500s locally (fleet nucleus was ~7h/48T — expected); word-sized => parse-safe; reduced emission staged in systems/redcheck/ for optional big-box re-check |

Every re-run reproduces its banked verdict exactly — direct empirical
confirmation that the word-sized contaminated inputs were parsed as
intended (the [0,p) reduction changes nothing), on top of the
micro-test boundary proof.

### Standing rule (added to the emitter checklist, alongside the
parenthesis rule)

**Every .ms emission with char p > 0 MUST have all coefficients
reduced into [0,p) before it ships.** Checklist per new emitter/file:
(1) expanded monomial sums only, no parens (2026-08-09 rule);
(2) coefficients reduced into [0,p) — verifier: max integer token of
the body < char line (the 110-file scan one-liner), reducer:
ops/reduce_msp.py; (3) independent-parser round-trip at the target
prime; (4) constant-term satisfiability smoke test. NEVER bank a
mod-p verdict from a file violating (2) — even word-sized violations
(currently parse-safe) are barred, since parser internals are not a
trust anchor and the 2^63 clamp is silent (no warning, exit 0).
Related: ops/msolve-issue-draft.md (paren hazard) should gain the
2^63-clamp finding before filing upstream.
## Ops checklist addendum (2026-08-11)
On every box restart/reuse: crontab -l FIRST; remove any deadline/poweroff/lifecycle entries before launching work (two incidents: jc-b poweroff loop, ultramem jc_deadline kill).

## External trust ledger (2026-08-12)
- Chau, Ann. Polon. Math. 71 (1999), Theorem 4.4 (full text banked at
  refs/chau1999_apm71_full.pdf; verified on-page pp. 304-305): load-bearing
  for the every-fiber Prop 5.8 upgrade (SOL-PROP58.md). Published +
  refereed; hypotheses Keller + monic in y.
- GPT-5.6-Sol, generalized zero-chain rigid law (xmodel/sol-td7-law.md,
  2026-08-13): td-7 class-B/C cell is T1-dead iff d_p | d_q (iff M = d_p
  iff kbar in {3,4}); on-axis ZCH (nu+1)|l recovered as the mu=1 case.
  PROMOTED after dual verification: zero-shared-reasoning engine check
  62/62 (xmodel/td7-law-engine-check.md; independent reduced-equation
  derivation from BOOK-OFFAXIS R1.0, exact sympy over QQ(A)) + Grok
  hostile proof audit SOUND, all 5 attacks held (xmodel/
  grok-td7-law-review.md). Effect: td-7 book 62 -> 6 live cells
  ((9,15,7,3),(10,15,7,5),(15,25,8,5),(15,25,12,5),(18,27,13,9),
  (39,65,32,13); 53 routes, 35 budget-equality), 1636/1689 routes
  removed by theorem. The six are certified LOCAL T1 survivors
  (explicit admissible solutions); next tier = transport/global.

## SUPERMIND/GUO BOUNDED CERTIFICATE INTAKE (2026-08-24)
xmodel/intake-supermind-guo-20260824.md (producer) and
xmodel/review-external-intake-grok.md (different-model hostile review:
**CONFIRMED WITH GAPS**). This is an artifact/provenance intake, not an
independent proof count and not an unconditional degree theorem.
- PROMOTED AT THE STATED ARTIFACT TIERS: the SuperMind first-layer and Case-II
  exact Python checks; the pinned Case-I Singular characteristic-zero
  52-dimensional/good-specialization full-rank terminal; Guo's authoritative
  790-file manifest and its exact/hash/regression/conditional audits; the
  degree-21 passport enumeration; the advertised characteristic-zero FGLM
  *program* replay; and the two row-split polynomial identities.
- EXACT CROSSWALK: SuperMind and Guo use the same two Proposition-4.3 Laurent
  systems under a lossless renaming, and their Helali/Suzuki reductions give
  exact zero remainders to the common quintic. Neither proof path invokes
  msolve `-g`.
- GAPS/QUALIFIERS: the SuperMind Python regeneration of the pinned Case-I
  `.sing` file capped; Guo's Sage-only lift, `V(c)`, `D != 0`, and `D=E=0`
  terminal expansions were not rerun. Guo's FGLM script uses Singular
  `modStd(I,1)` on a nonhomogeneous global-order ideal: the advertised program
  replay passes, but it is not to be described as a fully rational `std`
  certificate.
- NO GLOBAL PROMOTION: coordinate equivalence and artifact correctness do not
  establish social or derivational independence. Both bounded exclusions
  still depend on the GGV-Horruitiner reduction/transcription bridge. Thus no
  unconditional exclusion of every `(72,108)` counterexample, no unconditional
  degree-125 theorem, and no implication for JC2 is recorded here.

## Lift retirement (2026-08-13)
cCa2/cCa6 char-0 lift certificates: RETIRED under the last-chance rule
(no LIFT-CERT at the post-outage ultramem check; runs killed).
**CORRECTION (2026-08-23):** those lifts were load-bearing for the campaign's
own characteristic-zero chart proof.  Three independent modular `[1]`
verdicts plus satisfiability/emission guards are strong evidence but do not
imply `1` belongs to the rational ideal.  The internal cCa2/cCa6 proof status
is therefore open.  The separately replayed exact Helali/Suzuki systems
preserve the conditional external `(72,108)` conclusion.
Ultramem access note: use `gcloud compute ssh ultramem-1` (plain ssh key
not authorized); current IP 136.65.11.117 (changes on restart).

## 729-row re-emission (2026-08-13)

TEMPLATE 2c-E5 erratum (SHEET6-TEMPLATE.md §2c, 2026-08-12): the cleared
E5 row constant is 243 = 3^5, not the 729 an earlier draft baked; the
corrected row is 4*(a_i-b)*HM + 243*S_M^3*(a1-a2)^4*a_i^2*c_i*W_i^4 = 0.
H_M is unit-rescalable (HM -> 3*HM maps the 243-row onto the 729-row),
so no banked verdict flips; emitted files carrying the stale constant
are re-emitted for hygiene so downstream consumers do not inherit it.

Findings per engine — all three were (b) stale in code AND (c) stale in
prior emissions:
- cases/r1_q0_gate.py: e5e6_rows() (-> r1_q0_sat_p*) and phase_famemit()
  (-> r1_q0_fam*) used 729; patched to 243 (comment breadcrumbs cite the
  erratum).
- cases/r1_q2_screen.py: phase_emit() (-> r1_q2_l*_p*) and phase_exact()
  (-> r1_q2_l13.ms char 0) used 729; patched to 243.
- cases/r1_12_sat.py: phase_minsat() and phase_corr() used cW =
  729*7^36*144; patched to 243*7^36*144.  (The e5port/emit 81-constant
  rows derive via the RETRACTED mult-4 port, not the 2c-E5 H_M row —
  untouched; the 729 inside the e5port transport identity is lam_i^3's
  9^3, legitimate.)

Re-emitted (26 files; originals kept as *.stale729, nothing deleted):
- Q0: r1_q0_sat_p{105337,105673}.ms + .rows.txt (the rows.txt pinned-HM
  / implied-s1F annotations change by exactly 1/3 mod p, as forced);
  r1_q0_fam.ms; r1_q0_fam_p{105337,105673}.ms.
- Q2: r1_q2_l13.ms (char 0); r1_q2_l{4,8,12,13}_p{105337,105673}.ms;
  r1_q2_l8_sub{16,23,30}_p{105337,105673}.ms (row-subset probes with no
  in-repo emitter: re-emitted surgically — corrected E5 rows generated
  by the engine's own emit path, all other rows byte-identical).
- 12sat: r1_minsat.ms; r1_12sat_corr.ms; r1_12sat_corr_p{105337,
  105673}.ms.
Unaffected by construction: every ctlA/ctlB control (E5/E6 rows
dropped), the relaxed base tiers (r1_q0_p*), the r1_12sat e5port family,
all leaves.  r1_23sat.ms matches the raw integer 12*729*7^36*144 only as
an expanded chain-core coefficient on x-monomials — the chain engine
emits NO E5-analogue rows (EMPTY BY DERIVATION, sec 20.0); not stale.

Verification (all PASS):
- Per file vs its .stale729 twin: exactly the two E5 rows differ;
  paren-free; every changed row reduced into [0,p); independent-parser
  identity stale_row(W, 3*HM) == 3*corr_row(W, HM) at random points
  (FC.parse_eval), 24/24 .ms files — pins the ratio-3 W-side change and
  the unchanged HM-side in one shot.  Label-only rows.txt regenerated
  with zero drift.
- Engine guards: q0_gate a7 anchor PASS (both primes); q2_screen pert 13
  PASS (2/2 deliberate perturbations caught); r1_12_sat e5port PASS.
- 12sat engine-fused re-runs REPRODUCE the banked verdicts exactly:
  r1_minsat.ms char-0 NONEMPTY; r1_12sat_corr.ms char 0 + both primes
  NONEMPTY (~1s walls; engine appended them to runs/*_runs.log).

Why no verdict flips (and what was deliberately NOT re-run):
- NONEMPTY class (minsat, 12sat_corr): exact variety bijection
  (HM|H12 -> 3x, tH -> (1/3)x; no E6/s1F coupling in these systems) —
  provable invariance, plus the empirical reproduction above.
- EMPTY class (r1_q0_sat_p*, r1_q0_fam[_p*], r1_q2_l13[.ms/_p*]): NOT
  re-screened; the banked EMPTY verdicts refer to the .stale729 bytes.
  Robustness at the modular tier: the banked ctlB_satonly controls
  (quotient rows + s1F saturation, NO E5/E6 rows) are `[1]` at the recorded
  primes, and ctlB's rows are a SUBSET of the full tier's rows, so
  EMPTY(ctlB) => EMPTY(full) over those same finite fields for ANY E5/E6
  rows, 243 or 729.  The fam characteristic-zero-header `[1]` is only a
  first-prime trace, so this subset argument supplies no Q-level kill.
  FLAG: should any future run of a corrected EMPTY-class twin fail to
  reproduce EMPTY, that falsifies the subset argument -> review.  The
  l4/l8/l12/sub* strata carry only TIMEOUTs (no verdicts) — nothing to
  flip.
- Pre-existing, unchanged: the E6 literal 16777216 (2^24) token in the
  q0_sat/q2 mod-p emissions exceeds p (word-sized, parse-safe per the
  2^63 micro-test); it is byte-identical to the stale banked inputs and
  was deliberately NOT altered, to keep byte-parity outside the E5 rows.
  Standing-rule [0,p) reduction of that literal remains an obligation
  for those emitters.
- Restored: systems/r1/r1_full_core.rows.txt (byte-identical copy from
  runs/r1chain_prebuild_snapshot/) — missing from systems/r1 before this
  task (pre-existing gap) and a required input of the q2 guard
  (ME.core_name_map).

## H5a resolution (2026-08-13)
The Notation 3.5 GAP at doubly realized vertices (SIGRAY-AUDIT rows
26/37/92) is RESOLVED at proof tier: the P/coarse reading is incoherent
(nonintegral D_{h,F} against printed Stmt 3.8; conflict with Prop 5.5),
so Q/jump/max kappa_F = nu_F kappa_G / nu_G is the unique uniform repair,
and Q + printed Stmt 3.17(ii) + Prop 9.3(e) force the E5 transport
identities. Proof: xmodel/sol-h5a.md (GPT-5.6-Sol); hostile replay SOUND
incl. printed-page verification and witness construction:
xmodel/grok-h5a-review.md. Consequence: the §11a 17-cell td-7 book is
unconditional under the filed perimeter; the 2-cell sub-book requires
CONJECTURE U_7C (nu_F = nu_G on relevant case-III edges) — genuinely
new, unproven, unrefuted (an exact non-Keller model permits inequality);
no cheap empirical discriminator exists (review finding 5).

## First cell-level tower kill (2026-08-14)
(9,15,7,3)@mu0=2 of the td-7 §11a book: DEAD at the tower tier (no global
Prop 4.2 ladder; level-1 clash, terminal-independent). Adversarial history
preserved in full: Grok SOUND-WITH-ERRATA -> Case C repair; Sol BROKEN
(same gap, pre-repair snapshot) -> M_U=4/free-characteristic extension
(universal nu_X>=2 refactor) -> Sol STILL-BROKEN (in-perimeter neutral
insertions, real gap) -> N1-N4 closure (Sol's sketch formalized) -> Sol
CONFIRMED-KILL. Artifacts: TOWER-9-15.md, cases/towers/t9_15_{direct,
trunk}.json, cases/tower_check.py (696 gates). Book: 17 -> 16 live cells.

## Second cell-level tower kill (2026-08-14)
(10,15,7,5)@mu0=3: TOWER-DEAD (Grok single-pass SOUND, no errata —
xmodel/grok-t10-review.md; machinery core was already triple-reviewed).
Spine == rollout arithmetic exactly (panel-constant apparatus validated).
Consequence: nu_U = nu_G = 7 makes the kill reading-independent; with
(9,15) the forced-nu sub-book is EMPTY and CONJECTURE U_7C is MOOT for
td-7. Book: 15 live cells, all ARITH-DEAD-PREDICTED (TOWER-ROLLOUT.md).

## Third + fourth cell-level tower kills (2026-08-14)
(58,87,43,29)@15 (family rep, k-symbolic frame in m for all six 2/(2k+1)
members) and (25,35,17,5)@8 (kbar=7 outlier, formulas kbar-generic):
TOWER-DEAD, Grok batch review SOUND (xmodel/grok-t58-t25-review.md).
Tripwire verified both ways: rollout (7,15) arrival E5-refuted (n=-1),
corrected (37,15) ledger exact and covered. Blast radius: n>=1 omission
contaminates 7/16 rollout MIN-WITNESS columns (prediction table only) —
NOT the §11a census, NOT any kill. td-7: 13 live cells, all
arith-dead-predicted; uniform theorem next (obligations U-OB1..5).

## TD-7 PANEL CLOSURE (2026-08-14)
THEOREM (TOWER-UNIFORM.md, PROMOTED): every cell of the E5-corrected
td-7 class-B/C book dies at the tower tier — 17/17 (4 certificates +
13 witness instantiations), full perimeter (filed routes, all arrivals/
M_U/free-characteristic/padding/insertion stacks/E5 reroutes),
reading-independent. Lemmas: L-A (R1.3+St8.4/P3 corollary), AM
(absorbing-M), WIN (budget-admissible competing-vertex form; the raw
menu-ratio prose was corrected per review), E5F (uniform n>=1 law,
closed forms). Review chain (seven passes, three model families):
grok-tower-review, sol-tower-review/-rereview/-final (t9_15);
grok-t10-review; grok-t58-t25-review; grok-uniform-review +
sol-uniform-review (both green), 14 errata folded, gates 1559/1559.
Engine: cases/tower_check.py uniform mode; certificates cases/towers/.
Chain effect: off-axis td=7 needs no coefficient emitter; the sheet
ladder's next rungs are td-11/13 (refile + port).

## Witt-Bockstein stratum rigidity (2026-08-14)
PROMOTED: for plane Keller pairs over F_2 on the registered Mondello-
hull-plus-one-L1-shell stratum, the W_2/Cartier lifting obstruction
NEVER vanishes ([xy]E_F = 1 as an identity on the complete four-P
classification, 1152/1152 nonzero incl. all odd-degree data) — no
char-0 counterexample seed lifts from this stratum. Sol construction
(xmodel/sol-witt.md, engine cases/witt_check.py) + Grok hostile review
SOUND (xmodel/grok-witt-review.md). Disproof door closed on the
stratum; the lane's continuation (other strata) is optional and
unranked.

## ODD-PRIME FIRST-WITT SURVIVOR (2026-08-24)
xmodel/round2-witt-oddprime-20260824.md and
cases/round2_witt_oddprime/ (exact producer plus independent replay), with
xmodel/review-witt-oddprime-claude.md (different-model hostile review:
**CONFIRMED**).
- PROMOTED AT THE FINITE-FIELD/`W_2(F_3)` TIER ONLY: over `F_3`,
  `(P,Q)=(x-x^3,y)` has Jacobian one, generic degree three, and the distinct
  marked points `(0,0)` and `(1,0)` collide at `(0,0)`.  Its unrestricted
  first Witt obstruction vanishes.
- EXPLICIT LIFT: in `W_2(F_3)=Z/9`,
  `(P_2,Q_2)=(x+8x^3,y+3x^2y)` has exact integer determinant
  `1+27x^2+72x^4`, hence determinant one modulo 9, and the same marked
  collision persists.  Independent implementations, a third hostile
  recomputation, and the frozen manifest all agree.
- CONSEQUENCE AT THIS SCOPE: the promoted characteristic-two obstruction on
  the registered Mondello stratum is not a blanket first-Witt obstruction at
  odd primes or on other supports.
- NOT SHOWN: no `W_3`, bounded-support compatible all-Witt tower, `Z_3` or
  characteristic-zero polynomial lift, germ, or JC2 counterexample follows.
  The displayed correction already enlarges support.

## UNRESTRICTED-SUPPORT ALL-WITT ARTIN--SCHREIER CONTROL (2026-08-24)
xmodel/witt-tate-control-20260824.md (exact closed-form producer plus internal
audit), with xmodel/review-witt-tate-control-claude.md (different-model hostile
review: **CONFIRMED**). This is a separate descendant/control, not a widening
of the finite `W2-SURVIVOR` case above.
- PROMOTED AT THE ALL-WITT / RESTRICTED-ANALYTIC CONTROL TIER: for every odd
  prime `p` and `n>=1`, over `W_n(F_p)=Z/p^n`,
  `F_n=(x-x^p, y*sum_{j=0}^{n-1}(p*x^(p-1))^j)` has exact integer determinant
  `1-p^n*x^(n*(p-1))`, hence determinant one modulo `p^n`. The maps are
  compatible under every Witt truncation and the fixed distinct points
  `(0,0),(1,0)` collide at every level. Each map is finite etale of rank `p`.
- LOAD-BEARING ESCAPE: `Q_n` has exactly `n` monomials and degree
  `1+(n-1)(p-1)`. Thus support and degree grow linearly. The inverse limit is
  the nonpolynomial restricted-analytic/rational bidisc map
  `(x-x^p,y/(1-p*x^(p-1)))` in `Z_p<x,y>`, still finite etale of rank `p`,
  determinant one, and noninjective. It is not a polynomial endomorphism of
  affine two-space.
- CONSEQUENCE AT THIS SCOPE: no later finite Witt obstruction can kill this
  seed when growing support is allowed, and compatible lifting through every
  finite level does not by itself yield a characteristic-zero polynomial.
  The missing uniform-support-or-polynomial-limit criterion was already
  stated in `xmodel/sol-witt.md` section 6; this is its first explicit
  same-seed witness.
- NOT SHOWN: no bounded-support or uniformly bounded-degree tower, alternate
  polynomial lift, impossibility theorem for other lifts, complex polynomial
  map, germ, or JC2 counterexample follows.
- GOVERNANCE: the coordinator accepts this as the synthesis's single
  explicitly provisional, closed-form descendant while review ran, not as a
  same-generation enumerative `W3`/support-search cap. It is now independently
  confirmed; the W search root remains stopped.

## TD11-CLASH promotion at exact-core tier (2026-08-14)
PROMOTED: the td-11 entry-clash theorem at its honest tier — entry
packets (all three L6 entries), direct hierarchies, single-word-deep
configurations, exact-core audited states (12/10/8, zero non-exempt
violations); Lemma 11A-RES (the sole 5/8 intruder is mu-robustly
H8-dead); Lemma CAP-DEN; near-miss ledger rows 1-9 incl. self-found
row 5 and historicized row 8. OPEN residue, named exactly: beyond-core
px2 states (grammar unbounded, R=1+Delta/nu; both restoration paths
stated §13.0), 129 nested 11-C decorated rows, multi-word-deep
families (NF-Z-dagger per-entry checks), nu=1 resonance chains, the
future Q+E5/E5F refile. Review chain (5 rounds): grok-td11-review
(SOUND-WITH-ERRATA), sol-td11-review (BROKEN), restatement,
sol-td11-rereview (STILL-BROKEN, narrowed), exit-b exact-core
restatement, sol-td11-final (cores CONFIRMED, inventory COMPLETE,
editorial), editorial pass. Gates td11 58/58. Corollary: td-11 NF-D
depth closed for single-word configurations.

## td-11 nested-rows closure (2026-08-14)
PROMOTED: all 129 nested 11-C decorated skeleton rows DEAD-AT-TIER —
62 by inner-merge H8, then the remaining 67 = 31 unrealizable + 12
AB-self-refused (general den-criterion at k | i_G = 2) + 3 split-resolved
+ 21 DEAD-OUTER (NF-M parametric X_out pin at the outer vertex). The
109-object free-nu_A sweep (incl. the in-window-live (6,16)@2 shape)
is census-unrealizable throughout (nu_A != 2 needed, nu_A = 2 pinned).
Review chain: grok-td11-block2-review (reopened 24), repair,
grok-67-final (YES, gap closed), errata fold (sign lemma -> closed form
kbar = 2(1+nuQ)/(1-nu(A-Q))). Gates nfm 25/25. td-11 OPEN inventory:
beyond-core, NF-P slice, refile.

## td-11 CONDITIONAL EMPTINESS CERTIFICATE (2026-08-15)
PROMOTED with wording riders: every configuration of the audited
td-11 class-B/C layer (411-row instrument-backed quotient of the
~2e8 raw route space) is TOWER-DEAD; emptiness is CONDITIONAL on
seven named fail-closed classes (FC1-FC7: beyond-core, cap-free
grammar, refile, current-state arrivals, post-merge strata, nu=1
provenance, merge-schema finiteness) held KEEP-AS-POSSIBLY-LIVE.
Sol's scope-hole chart + 5 siblings enter and die OUTER-DEAD.
Review chain: grok-census-review (SOUND-WITH-ERRATA, FC7 + real
re-derives + genuine td-7 replay — folded), sol-census-review
(BROKEN, M_G scope hole — repaired, +252 rows), sol-census-final
(EARNED; provenance-wording riders NOT load-bearing — fold next
editorial pass). Engine cases/td11_census.py gates 8/8; td-7
replayed through the same two-pole engine. The td-11 panel now
rests on: this certificate + discharging/closing FC1-FC7.

## FOUNDATIONS SCOPE ENTRY (2026-08-17, dual-adjudicated)
The end-to-end reduction (Keller counterexample -> GGV polygon data ->
sheet data -> enumerated book entry) is NOT currently a theorem
(REDUCTION.md, Sol; cross-review Grok SOUND-WITH-ERRATA). Real gaps:
(G1) GGV minimal-pair selection is existential, not a normalization of
every counterexample; (`G2-PSC`) NO transport theorem carries GGV corner data
through Sigray's normalization — the sheet construction does not consume
GGV data as written; (G5) NO upper bound on td. Gap 4 adjudicated: the
td-7 book carries its §11a completeness certificate and td-11 its
conditional certificate (Grok), but a UNIVERSAL full-configuration
landing theorem for the b>=2 sector does not exist (Sol) — both true.
HONEST SCOPE of promoted ladder results: book-relative (every
configuration in the enumerated books dies), pending the book-landing
theorem. The reduction consolidation (T-chain + gap repairs) is now a
top-tier theory objective alongside residue-A.

## td-12 type-(3,5) book (2026-08-18)
PROMOTED AT THE HONEST / LIST-RELATIVE TIER: all 14 entry-level cells
of the td-12 type-(3,5) book (poles 2 x (6,1,2,5) — the single
below-bound filed entry) are TOWER-DEAD on the ENUMERATED 74-gap
candidate list (78 raw): 6 SPINE-DEAD-H8 + 8 CLASH-DEAD-FIRSTDEATH,
conditional on the SEVEN named fail-closed classes (a)-(g).
List-completeness is LIST-RELATIVE with residuals named (Lemma
FD-TRICHOTOMY); the u=1 gap-1/3 candidate is exhibited UNREFUSED =
the named load-bearing residual (class (c)/NF-P). No X vertex exists
at this entry: the kill is the first-death refusal theorem (den-
refusal of every enumerated candidate maximal gap), replacing the
td-7/td-11 X-clash pattern. TDBOUND consequence: the filed ladder's
live frontier is exactly {residue-A} plus the unadjudicated
above-bound entries (td 8, 10, 12-(2,3)/(2,5), 14). Review chain:
grok-td12-review (SOUND-WITH-ERRATA — round-2 errata folded: 74/78
candidate recount vs the stale 54, corrected budget-10 core
multipliers, de-tautologized spine checks, citation hygiene). Engine
cases/td12_book.py, 14 gates, exit 0. Source: BOOK-TD12.md.

## D23 FIBER-LOCAL NONEMPTINESS (2026-08-19)
PROMOTED AT THE FIBER-LOCAL / MOD-p TIER: on the radical_point chart fiber
of the D21 window (the CORE2 object, SHEET6-DIRECTIONB 7.S3), the depth-23
Row_22 obstruction does NOT eliminate the window: V(row22red) is nonempty
over the algebraic closure of F_p at p = 105337, 105673, 200257.
Chain: NF reduction of the 6 compat rows against the banked 397-element
fiber GB (8.S4 payload; point-identity gates 72/72 x2 primes) -> affine
structure A = C.diag(uW1^2,uW2^2,uW1^2,uW2^2), C constant rank 2 -> exact
rank-2 residual g1,g2,g3 with V(fiberGB+g) = proj V(row22red), EMPTY iff
EMPTY (rank pinned by saturated scales) -> msolve GB 509 elements != [1]
at all three primes (det23 lanes, 63s each; det23_p*.out banked).
Witnesses: 6 explicit F_p points per prime at 105337/105673, verified
400/400 emission rows in python-flint, back-solved to FULL 72-variable
depth-23 configurations (54/54+76/76+77/77 rows; cases/d23_witnesses_*.json,
8.S6). Survivor locus dimension 11 (all three primes; g's cut codim 2).
Review: Grok hostile recompute CONFIRMED all load-bearing claims incl.
bidirectionality + scope honesty (xmodel/grok-det23-review.md); Sol
independent structural convergence + 85% prior (xmodel/sol-avenues3.md).
SCOPE LIMITS (explicit): one radical fiber of 36; mod p only (no char-0
statement); chart-local; says nothing about the other fibers or about
DEPTH-STAB germ certification (e-spec unbanked, experimental readings
fail closed). Supersedes: the row22compat/row22red 12h timeouts (now
explained as nonempty-GB grinds; rc=124 x3 + x2 banked, third lane killed
at 305GB post-confirmation, rc=137).

## FILTERED DIFFERENTIAL NEWTON LEMMA (2026-08-19)
PROMOTED AT THE ABSTRACT-THEOREM TIER: the filtered Newton/Hensel lifting
theorem for the Euler/Ore linearization (xmodel/sol-newton-lemma.md
Theorem 3.1 + Cor 3.2 + supporting lemmas): over any field (incl. char p),
a residual of global t-order D lifts to a formal solution whenever
D >= 2e+1, where e = the delayed-parametrix loss of the linearization;
Euler terms need no conjugation. Proof: Sol (Route B contraction);
review: Grok hostile replay CONFIRMED (xmodel/grok-newton-review.md).
SCOPE WITHHELD (per both documents): no promoted e+ at any point, no
D23/D25 germ certified, CYCLIC-30/BRIDGE-30/PARAM-30/FILTER-30
application gates open. This closes CONJECTURE E-HENSEL and supplies the
mechanism awaiting a D25 survivor with a certified e+.

## FIBER EQUIVARIANCE THEOREM (2026-08-20)
PROMOTED (scoped algebraic theorem + exact D25 realization): the 36
radical fibers of the D21 window form a single free orbit (G-torsor) under
G = (C3)^2 x (C2)^2, acting by diagonal scalings with entries in
{+-1, +-omega, +-omega^2} subset F_p at both banked primes; the fiber
transports are F_p-SCHEME isomorphisms, and the character identity
F_{l,g.lambda}(T_g x) = chi_l(g) F_{l,lambda}(x) holds as an exact
monomial-dictionary identity on all 9,792 generator-edge row pairs of the
parked D25 systems (residuals R1-R5 character 0). Proof: Sol
(xmodel/sol-pcc-orbits.md); review: Grok hostile recompute CONFIRMED
(xmodel/grok-orbits-review.md). RESIDUAL GAPS (named, minor): un-rerun
source-pkl weights; 216 witness checks pending; future-emission fidelity
must be re-gated per new emission. CONSEQUENCE: one fiber decides all 36
at D25 (and at any depth whose emission passes the fidelity gate) --
per-fiber cost /36 permanently; the atlas support identity is explained.

## D25 FAMILY NONEMPTINESS + CELL STRUCTURE (2026-08-21)
PROMOTED AT THE MODULAR TIER (p = 105337 and 105673; emission-fidelity
caveat inherited from SHEET6-DIRECTIONB sect 9; chart-local as always):
the depth-25 residue-A family systems are NONEMPTY of dimension 14 --
and moreover each of the 36 fiber systems is 16 DISJOINT COPIES OF A^14
over F_p (union: 576 cells), identified by an exact certificate: 2 lift
pivots (minor = unit x uW1^2 uW2^2) + 8 Laurent-unit base pivots with
well-founded DAG, hcore/hlin ideal-membership from raw rows, explicit
per-fiber witnesses vanishing 34/34, Jacobian ranks 14/18. NO Groebner
basis was required; the 48h union lanes are superseded.
Chain: Sol certificate (xmodel/sol-ideas-0821.md) -> independent
mechanical replay CONFIRMED (cases/d25_certificate_replay.json, 9.S2;
negative controls 24/24) -> Grok hostile recompute CONFIRMED
(xmodel/grok-d25cert-review.md: 72/72 fibers, freeness verified).
The pre-registered ECO-D25 codim-2 prediction is REFUTED (height-1 cut).
CONSEQUENCE: the residue-A window survives depth 25 family-wide with
smooth rational cell structure; the kill direction has now failed at
D23 and D25; the discriminating question moves to germ certification
(corrected e+ on the A^14 cells vs the Newton criterion) and, on the
kill side, to whatever mechanism could terminate a cell tower that
grows codimension strictly slower than depth.

## PURE-BOUNDARY JACOBIAN IDENTITY + G5 CLASS-KILL (2026-08-23, dual-confirmed)
Two EXACT, hand-checkable results from the G5/rooftop lane
(xmodel/sol-rooftop.md), independently CONFIRMED by Grok adversarial
recompute (xmodel/grok-rooftop-review.md, direct computation + toy checks).

(1) PURE-BOUNDARY JACOBIAN IDENTITY. Let f,g in k[x,y], F,G their degree-d,e
homogenizations, J(f,g)=f_x g_y - f_y g_x. Chain rule gives
dF/dX = Z^{d-1} f_x(X/Z,Y/Z), so
    F_X G_Y - F_Y G_X = Z^{d+e-2} * J(f,g)(X/Z,Y/Z).
KELLER case J=j in k*:  F_X G_Y - F_Y G_X = j * Z^{d+e-2}  (all critical
contributions created at the line at infinity). Grok toy-verified on the
elementary automorphism f=x+(y+x^2)^2, g=y+x^2 (LHS = Z^4 exactly) plus five
more pairs; homogeneity, dehomogenization, and monomial-uniqueness all clean.
Corollary: det D[F^beta:G^alpha:Z^N] = c*F^{beta-1}G^{alpha-1}Z^{N+d+e-3}.
TIER: EXACT, dual-model confirmed. This is the polynomial-origin datum the
formal countermodels lack.

(2) G5 CLASS-KILL (permanent NO-GO). The family f_B=x^{Balpha}+y,
g_B=x^{Bbeta}+y^{Bbeta-1} (coprime 2<=alpha<beta) has: finite normalized
multi-Rees algebra, antinef/complete rooftop (definitional), and the balanced
common leading power F_d=(X^B)^alpha, G_e=(X^B)^beta (so even J(F_d,G_e)=0),
YET normalized rooftop energy
    E_MR = td/(alpha beta) = d(e-1)/(alpha beta) = B^2 - B/beta  ->  infinity.
Grok CONFIRMED td=d(e-1) (Gauss-irreducibility of P(X)-v, deg_x = d(e-1)>e)
and the energy arithmetic on six triples. Non-Keller (J not constant), so not
a G5 counterexample -- it REFUTES the implication class
{finite generation, rooftop convexity, common leading power} => uniform bound.
Also Hodge index / Teissier-Rees-Sharp / reverse-AF give e_inf(I,J)<=N^2, i.e.
E_MR >= 0 -- the WRONG SIGN (G5 needs the upper/near-max bound).
CONSEQUENCE: any proof along this rooftop route MUST use the full Keller
identity (1), not finite generation, convexity, Hodge, mixed volume, or the
leading-form shadow of Keller. CORRECTION: KJN(C),
deg Psi = alpha beta * td <= C(alpha beta)^2, gives the type-relative ceiling
td <= C alpha beta; it is not equivalent to an absolute G5 ceiling unless a
separate theorem supplies a bounded/cofinal type menu with valid provenance.
The EXACT, dual-model-confirmed tier here applies to the identity and the
class-kill, not to the still-conjectural KJN estimate.

## RAW BOUNDARY PASSPORT/CAPACITY PROBE RETURNS COSTUME (2026-08-24)
xmodel/round1-boundary-passport-20260824.md and
cases/round1_boundary_probe/ (exact QQ producer run; coordinator byte-identical
replay), with xmodel/review-round1-proof-gates-claude.md (different-model
hostile review: **CONFIRMED**). This is a route-falsification result, not a
theorem about every possible compactified boundary invariant.
- Exact control suite: identity; `T_n=(x,y+x^n)` for n=2,4;
  `T_4^{-1} o T_4`; the promoted Henon automorphisms at r=0,1; and the
  non-Keller class-kill member only as a negative control. One explicit
  boundary blow-up chart is included.
- VERDICT **COSTUME** for the tested raw proposals. Gradient-cokernel
  Fitting/Smith splits, log-coframe Smith splits, and action-primitive pole
  orders vary under polynomially equivalent presentations and/or the explicit
  blow-up; tame and Henon automorphisms make them arbitrarily large, while
  exact orbit minimization returns the identity data. The stable Keller-suite
  outputs are the log-determinant volume orders and zero residues of exact
  meromorphic differentials, both consequences of `J=1` rather than stronger
  capacity data.
- KILLED AT THIS SCOPE: untwisted action-residue charge, raw primitive pole
  order as an invariant budget, raw `Q`/`Fitt_1`/Smith filtration as a
  coordinate-free passport, unsigned raw log-coframe/localized-Chern charge,
  and raw boundary exponent as a uniform consumable cap.
- NOT KILLED: the exact pure-boundary identity; use of `Q` as a checksum after
  a proved choice-independent minimization/compactification; boundary-twisted
  forms; or a signed global invariant using complete polynomial data. Those
  redesigns first owe covariance/minimality and positivity, and no theorem lane
  is opened by the present computation.

## TRACE-REGULARITY AUDIT: CURRENT CONTACT PACKET IS INSUFFICIENT (2026-08-24)
xmodel/round1-trace-regularity-20260824.md and
cases/round1_trace_probe/ (exact producer run; coordinator byte-identical
replay), with xmodel/review-round1-proof-gates-claude.md (different-model
hostile review: **CONFIRMED**).
- EXACT CHARACTERISTIC-ZERO REDUCTION: for a generically finite plane Keller
  map of function-field degree `d`, regularity of the first `d` field power
  traces of `x` and `y` is equivalent to integrality/finiteness and hence to
  automorphy. This is an honest reformulation of the missing finiteness step,
  not a shortcut to it; the required cutoff `d` is itself unbounded.
- EXACT UNDERDETERMINATION CONTROL: two denominator-42 formal completions have
  identical retained support, contacts, gcd chain `42 -> 6 -> 2 -> 1`, indices
  `(7,3,2)`, leading data, and full `m=1` principal parts, but their `m=2`
  residues are respectively 84 and 168. The varying coefficient sits at
  offset 126, beyond the last retained level 79.
- CONSEQUENCE AT THIS SCOPE: the current contact-only packet does not determine
  the quadratic trace principal part. The missing datum is an
  affine-target-divisor-tagged completed branch pairing, including coefficient
  convolution and residue-field traces. Do not build a general TRACE-REG
  engine from the current packet.
- NOT SHOWN: the formal pair is not a Keller countermodel; TRACE-REG is not
  refuted; no nonautomorphic Keller map is produced; and no claim is made that
  every augmented packet is insufficient or that a universal trace cutoff is
  impossible.

## NORMALIZATION/DIFFERENT RECEIVER DOES NOT FIX QUADRATIC MOMENTS (2026-08-24)
xmodel/round2-norm-moment-sep-20260824.md and
cases/round2_norm_moment_sep/ (exact producer), with
xmodel/review-norm-moment-sep-grok.md (different-model hostile review:
**CONFIRMED**).
- PROMOTED AT THE FORMAL-LOCAL CONTROL TIER: for `t=u^42`, the two exact
  Darboux completions
  `x_b=u^-84+u^-42+u^-30+u^-10+u^-5+b*u^42`,
  `y_b=42*q*u^41/(d x_b/du)`, with `b=1,2`, have the same finite local
  algebra, different `(42u^41)`, conductor exponent, selected contact/gcd
  decoration, coordinate valuations, local Jacobian two-form, and complete
  first trace principal part.
- DECISIVE SEPARATION: the `t^-1` coefficients of `Tr(x_b^2)` are 84 and 168.
  Thus the displayed local algebra/different/contact/Jacobian packet does not
  determine even the quadratic coordinate moment.  Coordinate multiplication
  data differ, as they must, and can carry the missing information.
- HARD STOP HONORED: the preregistered native-source type gate was not run once
  `DIFFERENT-INSUFFICIENT` fired.  No claim is made that a native GGV packet
  cannot populate a richer target-divisor-tagged receiver.
- NOT SHOWN: these are formal-local controls, not polynomial Keller maps; no
  global polynomial-origin identity is excluded, TRACE-REG is unaffected at
  its honest finiteness-equivalent scope, and no JC2 conclusion follows.

## G2-BD/KJN FORMAL SEPARATION + PUISEUX gcd DICTIONARY (2026-08-23; terminology corrected)
The unification lane (xmodel/sol-unify.md) asked whether one Keller bound
closes both local objectives. It found a NOTATION COLLISION in the "shared
nu" and two non-implications in a weakened formal system; the earlier
"independent walls" verdict is superseded by the scoped reading below.
- EXACT Puiseux gcd dictionary (Lemma 1.1): for a pole branch with denominator
  kappa_i and characteristic gcd-drops nu_j, prod_j nu_j = kappa_i (telescoping
  gcd chain, e_s=1 by minimality). Residue-A ladder: 1 -x7-> 7 -x3-> 21 -x2->
  42, so kappa(P_i)=42=7*3*2.
- The ROOFTOP nu_P is only the LEAF decoration (final factor 2); the DEPTH
  product is over ALL characteristic vertices (7*3*2). The Belyi passport
  {2,3} ramification is a degree-4 QUOTIENT invariant AFTER common-carrier
  cancellation -- the factor 7 lives in the same genome but nowhere in the
  passport. Carriers cancel exactly: (C^4 h1)^3/(C^3 f)^4 = h1^3/f^4.
- KJN(C) =/=> UCD: formal countermodel (Lemma 2.2) inserts r characteristic
  vertices (q=q'=2, w=2 preserved) keeping td=6, deg Psi=36, E_MR=1 fixed
  while kappa_i = 42*2^r -> infinity. Even restricting factors to {2,3} fails.
- UCD =/=> KJN(C): formal family (Lemma 3.1) kappa_P=6 fixed, b_P=b odd -> inf,
  giving E_MR=b, td=6b -> infinity.
Both countermodels are FORMAL (satisfy the tree/arithmetic identities, no known
polynomial-origin Keller realization). CORRECTED CONSEQUENCE: they separate
the post-residue-A carrier predicate `G2-BD` from the type-relative KJN
predicate in the weakened formal system. They say nothing about `G2-PSC`, the
global GGV-to-Sigray transport/fidelity obligation, and do not prove
non-implication inside the class of actual polynomial Keller maps. The
dictionary is exact but this separation is single-model/banked formal
evidence, not a promoted two-way independence theorem. The unrestricted K2C
bridge proposed here is explicitly superseded by the later dual-confirmed
Henon refutation; only appropriately restricted minimal/nonautomorphic
residue-A variants remain open.

## TYPE-RELATIVE KJN: LOCAL SUFFICIENT LEMMA RPMC(C) => KJN(C) (2026-08-23; corrected)
The former G5 lane (xmodel/sol-kjn.md) gives a proved-in-lane sufficient
reduction from a LOCAL one-root capacity lemma to type-relative KJN. It does
not reduce the absolute td-ceiling without the separate type-menu/provenance
theorem stated below.

EXACT structures (all char 0; F,G degree d=Balpha,e=Bbeta homogenizations;
M=d+e-2; accepted input: the dual-confirmed pure-boundary identity
F_X G_Y - F_Y G_X = j Z^M):
- GRADIENT MATRIX FACTORIZATION (the Keller-specific object). A=[[F_X,G_X],
  [F_Y,G_Y]] has det = j Z^M, so the cokernel Q has Fitt_0(Q)=(Z^M): Q is
  supported scheme-theoretically on the M-fold thick line M*L_inf with NO extra
  Jacobian curve. After removing exceptional monomials, the transformed det is
  a UNIT off the strict transform of Z=0. This is the exact datum that ordinary
  ramification effectivity, Chern/Hilbert data, and coprimality all discard.
  (Its Hilbert poly chi(Q(t)) = M t + (3M-(d-1)^2-(e-1)^2)/2 still scales
  quadratically in B, so ordinary invariants alone give no B-independent bound.)
- ENERGY LOCALIZATION (EXACT). Common leading power forces F_d=xi H^alpha,
  G_e=eta H^beta, deg H=B, div_{Linf}(H)=sum mu_i P_i, sum mu_i=B. The rooftop
  energy splits with NO cross-terms over proper roots: E_MR = sum_i E_i,
  E_i = (1/2) sum_{p > P_i} (R_p/alpha - S_p/beta)^2.
- Coprimality lower quantum (EXACT): each nonzero R_p/alpha - S_p/beta has
  |.| >= 1/(alpha beta), so its square >= 1/(2(alpha beta)^2) -- a lower bound,
  not the needed upper bound.

CONJECTURE RPMC(C) (root-weighted pure-minor capacity): for each proper root,
E_i <= C mu_i / B, under the pure-minor identity hypothesis.
THEOREM 7.1 (PROVED conditional reduction): RPMC(C) => KJN(C). Sum E_i over
roots, sum mu_i = B => E_MR <= C => deg Psi = (alpha beta)^2 E_MR <=
C(alpha beta)^2. So RPMC(1) => sharp KJN(1) => td <= alpha beta at each
provenanced fixed type. CORRECTION: an absolute/cofinal TDBOUND conclusion
also requires an independently justified bounded type menu, and even that
would not close the transport, source, landing, or coverage gaps needed to
make the full book ladder unconditional.

SEPARATION FROM THE CLASS-KILL DECOY (EXACT, sec 8). The non-Keller control
f_B=x^d+y, g_B=x^e+y^{e-1} has Q_B = d(e-1)X^{d-1}Y^{e-2}Z - e X^{e-1}Z^{d-1}
!= j Z^M (an EXTRA Jacobian curve), yet at the first boundary valuation its
log-effectivity coefficient equals +1, IDENTICAL to a Keller pair. Therefore
log-effectivity alone cannot be the Keller step; the separating datum is
precisely the VANISHING of the residual Jacobian curve in the transformed
gradient cokernel. E_MR = B^2 - B/beta for this family violates RPMC's C mu/B
demand, with no contradiction because the matrix-factorization hypothesis fails.
TIER: reduction + all listed structures EXACT/PROVED (single-model, sol-kjn);
RPMC(C) is the open local lemma. NOT YET Grok-reviewed.

Bridge status (companion, xmodel/sol-k2c.md): UNRESTRICTED K2C is FALSE
(explicit Henon automorphism tower, td=1, kappa=42*2^r -> inf). The review was
pending when this entry was drafted; the next entry records Grok's independent
confirmation. Thus unrestricted UCD does NOT follow from the bounded-td data.
No KJN => `G2-BD` theorem is established; the restricted route still needs its
own UCD-A-min bound (degree-minimal nonautomorphic type-(2,3) residue-A). The
two local predicates remain unbridged; the only conditional bridge presently
named is CONJECTURE K2C-min.

## UNRESTRICTED K2C REFUTED: HENON AUTOMORPHISM TOWER (2026-08-23, dual-confirmed)
Theorem 2.1 of xmodel/sol-k2c.md, independently CONFIRMED by Grok hostile
recompute (xmodel/grok-k2c-review.md) with explicit hand computation.
Generators H_q(u,v)=(v, v^q - u), J=1, inverse (u,v)->(u^q - v, u). Fix r>=0,
s=r+4, indices q=(7,3,2,...,2); P_0=x,P_1=y,P_{i+1}=P_i^{q_i}-P_{i-1};
(f_r,g_r)=(P_s,P_{s+1}). Then (all CONFIRMED (i)-(vi)):
  - Phi_r is a polynomial AUTOMORPHISM of A^2, J=1, hence td=1;
  - pole orders at the unique place infinity: n_0 = prod_{j=1}^{s-1} q_j =
    7*3*2^{r+1} = 42*2^r; characteristic indices (7,3,2,...,2);
  - pole Puiseux denominator kappa_r = 42*2^r -> INFINITY;
  - deg f_r = kappa_r, deg g_r = 2 kappa_r;
  - the FULL pure-boundary identity holds: (F_r)_X(G_r)_Y-(F_r)_Y(G_r)_X =
    Z^{3 kappa_r - 2} (Grok verified Z^124 at r=0 by direct expansion).
CONSEQUENCE: bounded td + polynomial origin + the full boundary identity do
NOT bound kappa -> UNRESTRICTED K2C is FALSE. Grok confirms the scoping is
legitimate: the family is one-pole, reduced type (1,2), degree-minimizes to a
linear automorphism (kappa=1), never type (2,3), does not realize residue-A.
NET: unrestricted UCD does not follow from bounded td plus polynomial origin
and the boundary identity. Because this automorphism never realizes residue-A,
the construction addresses neither `G2-PSC` nor the restricted `G2-BD`
obligation. That residue-A route still needs UCD-A-min; the only conditional
bridge presently named is CONJECTURE K2C-min. TIER: EXACT, dual-confirmed.

## TYPE-RELATIVE KJN CHAIN: RPMC(C) <=> PC(C), POLAR-EXCESS BRIDGE (2026-08-23; corrected)
xmodel/sol-rpmc.md executes two of the three sol-kjn §7 bullets EXACTLY (single
-model tier), reducing RPMC to a concrete polar-capacity bound.
- THICK-LINE DEGENERATION (EXACT/PROVED). At a root of multiplicity mu, the
  gradient cokernel is a free k[[u]]-module of rank M=d+e-2; z-multiplication
  has ONE Jordan block of length M over k((u)), exactly TWO blocks (r, M-r) at
  u=0 with 1<=r<=d-1, M-r>=e-1, and Smith form diag(1,...,1,u^c,0), c=alpha*mu-1.
  So exactly ONE transverse elementary-divisor defect of exact size alpha*mu-1;
  all jump COUNTS determined, jump EXPONENTS not.
- POINT-BASIS = INTERSECTION DEFECT (EXACT/PROVED). With n_P =
  i_P(F-lambda Z^d, G-nu Z^e) and Delta_P = alpha*beta*B*mu - n_P (a nonnegative
  integer): E_P = Delta_P/(alpha beta) and sum_{p>P}(beta R_p - alpha S_p)^2 =
  2 alpha beta Delta_P. Hence the stronger quantum E_P >= 1/(alpha beta).
- EXACT POLAR BRIDGE (PROVED, pure-minor used exactly): on the normalization
  branches gamma of a general F-fiber above P (m_gamma = ord_gamma z),
  Delta_P = sum_{gamma|P} max{0, ord_gamma F_X - (d-2) m_gamma}.
- REDUCTION: CONJECTURE PC(C): sum_gamma max{0, ord_gamma F_X - (d-2)m_gamma}
  <= C alpha beta mu / B. By the above, PC(C) <=> RPMC(C), and Theorem 7.1
  gives the one-way implication RPMC(C) => KJN(C). No converse from KJN to the
  rootwise capacity bound is proved.
- KELLER SEPARATION (EXACT): for the class-kill decoy the residual Jacobian
  curve adds branch order de-d-1; intrinsic polar excess is only 1 while the
  actual defect is de-d, so the bridge (0.6), freeness, and nilpotence all fail
  exactly because Fitt_0 != (Z^M). Sanity gate holds.
STATUS: PC(C) <=> RPMC(C) => KJN(C) (type-relative). The remaining step on
this sufficient route is to bound
the intrinsic polar excess of the generic fiber at a Keller root by C alpha beta
mu/B. No finite B-independent C obtained. TIER: DECISIVE PARTIAL (single-model).

## TWO LOCAL SUFFICIENT ROUTES, NOT BOTH FOUNDATIONAL WALLS (2026-08-23; corrected)
The type-relative mass route (xmodel/sol-pc.md) and post-residue-A bounded-delay
route (xmodel/sol-ucda.md), both at the single-model tier. Neither addresses
the separate global transport obligation `G2-PSC`.

Type-relative KJN route: PC(C) <=> CONJECTURE DIR(C)
(displaced-intersection retention). For general
lambda,nu at a boundary root of mult mu (c=alpha*mu-1):
    n_P = i_P(Phi - lambda z^d, Gamma - nu z^e) >= e(c+1)(1 - C/B^2).
Since e(c+1) = alpha beta B mu, DIR(C) <=> PC(C) <=> RPMC(C) => KJN(C). PC's
1/B factor is thus a 1/B^2 RELATIVE intersection-retention bound.
New EXACT structures (PROVED):
 - canonical fiber differential omega = dy/f_x = -dx/f_y = dg/j; polar-excess
   term a_gamma = ord_gamma F_X - (d-2)m_gamma = -ord_gamma omega - 1; adjunction
   SIGNED identity Delta_inf - K_inf = 2 - 2 g_C - s (does NOT cap the positive
   part; the finite-end compensator K_inf is uncontrolled).
 - Smith telescope: higher z-filtration torsion tau_q <= min(q,M-q)(alpha*mu-1),
   i.e. every higher jump bounded by the first Smith defect c=alpha*mu-1.
 - semicontinuity gives n_P <= i_P (UPPER); DIR needs a LOWER bound. Wrong way.
STATUS: DIR(C) is a sufficient crux for type-relative KJN. Any finite
B-independent C gives td <= C alpha beta; an absolute/cofinal TDBOUND theorem
additionally needs an independently justified bounded type menu and provenance.

`G2-BD`: CONJECTURE A-SCALE => UCD-A-min => bounded delay. These are one-way
sufficient implications, with no converse claimed. DECISIVE NEGATIVE on using
degree-minimality alone:
by the char-0 coordinate-cusp theorem a type-(2,3) rectangular cusp pair is
ALREADY Aut-orbit degree-minimal at every common scale, so degree minimality
gives NO bound deg f <= Phi(6,(2,3)). (Contrast: the Henon type-(1,2) tower is
removable because V-U^2 is a coordinate; that mechanism is absent for reduced
type with both entries > 1.) Constant Jacobian gives only ord_t f_y = 3-kappa_i
(compatibility); branch conductor c(P_i)=2 delta(P_i) >= 2(kappa_i-1) is a LOWER
bound. Neither caps kappa_i.
A-SCALE: a+b <= B_A for orbitwise degree-minimal nonautomorphic residue-A pairs
(Sigray rectangle base (a,b)) => kappa_i <= deg f = 2(a+b) <= 2 B_A =: K_A.
Conditional K_A=42 only under the global-coordinate-tail hypothesis.
STATUS: A-SCALE is a sufficient `G2-BD` crux for this residue-A architecture;
a counterexample sequence to that bound, if one exists, lives in the
non-removable type-(2,3) carrier direction.

CORRECTED LOCAL MAP: DIR(C) <=> PC(C) <=> RPMC(C) => KJN(C), and
A-SCALE => UCD-A-min => `G2-BD`. KJN remains type-relative; none of the reverse
arrows just omitted is established. The Henon result dual-confirms only the
failure of unrestricted K2C/UCD. The local reductions remain single-model,
DECISIVE PARTIAL; they do not close `G2-PSC`, source, landing, or coverage.

## NO TWO-WAY LOCAL DIR/A-SCALE UNIFICATION: DIFFERENT/CONTACT LEDGER (2026-08-23; corrected)
xmodel/sol-bridge2.md compares the two local sufficient routes (DIR for
type-relative KJN, A-SCALE for `G2-BD`). CORRECTED VERDICT: no equivalence or
common controlling invariant is obtained; this is not a promoted symmetric
independence theorem and does not concern `G2-PSC`.
- EXACT different/contact ledger (PROVED): on a pole branch gamma of a general
  f-fiber, with m=ord z, p=pole order of g, I_gamma = contact with the other
  branches of the fiber germ:
     ord_gamma F_X = (d-2)m + p,   c(gamma) + I_gamma = (d-3)m + p + 1,
  hence the branch polar defect Delta_gamma = p (= 3 on residue A, the pole
  order of g), while the conductor 2 delta(gamma) measures the branch different.
  The common ledger carries an UNCONTROLLED CONTACT term I_gamma.
- CONSEQUENCE: a bound on the polar excess (DIR) does NOT, in the formal
  ledger, bound the conductor/kappa_i; the l=0,nu=2 tower keeps Delta_gamma=3
  while kappa_i, delta -> infinity. In the other direction, A-SCALE does imply
  a coarse residue-A DIR bound by bounding the whole degree scale. Thus the
  established comparison is asymmetric: DIR does not recover A-SCALE, while
  A-SCALE supplies a coarse DIR only on the fixed residue-A inventory.
- CONCRETE residue-A germ arithmetic (all EXACT): characteristic exponents
  (b1,b2,b3)=(54,74,79), approximate-root generators (42,54,398,1199), conductor
  c(P_i)=2278, delta(P_i)=1139, contact I_i=4656, d=168, m=kappa=42, p=3. The
  ledger closes with no slack (ord F_X = 6975 = 6972 + 3). DIR ratio
  B*Delta_P/(alpha beta mu) = 84*6/(6*63) = 4/3, so DIR(4/3) is EQUALITY on the
  filed residue-A root (independent of the large conductor 2278).
- DECOYS (Henon automorphism tower, non-Keller class-kill) BOTH have intrinsic
  polar excess 1 and conductor -> infinity, but are excluded by ORTHOGONAL
  mechanisms: Henon by orbit-minimality, class-kill by pure-Jacobian support
  (Fitt_0=(Z^M)). Neither Delta nor delta alone excludes both; no local
  no-decoy rigidity statement using only either displayed invariant is
  presently established.
- Equivalent reformulation of a **uniform residue-A conductor ceiling** (not
  of `G2-BD` or A-SCALE): CONJECTURE CONTACT-DEFICIT
  `(d-3)kappa_i - I_i <= K_A`. By the ledger with pole order `p=3`, this is
  exactly `c(P_i) <= K_A+4`; combined with
  `c(P_i) >= 2(kappa_i-1)`, it is a sufficient route to UCD-A-min and hence
  `G2-BD`. No converse from carrier boundedness or A-SCALE is asserted.
TIER: ledger + arithmetic EXACT/PROVED (single-model); the no-equivalence
assessment is banked but not hostile-reviewed/promoted. NET: no present local
lemma merges the two sufficient routes. This does not rule out a stronger
future theorem proving both, and it leaves `G2-PSC` and the other foundational
landing/coverage obligations untouched.

## DIR CENSUS + THE ALGEBRAIZATION CONVERGENCE (2026-08-23)
xmodel/sol-dircensus.md, full rootwise census of the td<=12 books.
- R_P = B*Delta_P/(alpha beta mu_P), Delta_gamma = pole order of g.
- Max FULLY-SPECIFIED filed R_P = 4/3 (residue-A Y-root, equality); actual
  Keller controls (Henon) only 1/2. But td<=12 type-(2,3) book rows FORCE
  max_P R_P >= 3/2, 5/3, 11/6, 2 (td=9,10,11,12) under any Keller lift; these
  are weighted averages so the mass-bearing root can be larger still. => C=4/3
  is NOT a supported DIR ceiling.
- DIR(C) <=> CONJECTURE RPC: sum_{gamma|P} p_gamma <= C alpha beta mu_P/B. The
  pure-minor identity gives only Delta_P <= alpha beta B mu_P (R_P <= B^2), the
  wrong B-scale. VERDICT: DIR NEUTRAL, no finite C supported (single-model).
- DIR counterexample lead (additive pole-mass axis): [3A;A,1,2]^2, pole profile
  (3A,3A), td=6A; any Keller lift => max R_P >= A -> infinity.
CONVERGENCE ASSESSMENT: both local conjectures have formal counterexample families
(A-SCALE: carrier tower kappa=42*2^r; DIR: [3A;A,1,2]^2 pole-mass tower), and
BOTH are gated by the SAME meta-question -- do these formal Newton/entry
families ALGEBRAIZE to actual polynomial Keller pairs? Algebraize(either) =>
JC2 counterexample (provided the advertised nonautomorphic realization and
provenance are certified). CORRECTION: failure to algebraize these particular
families would not prove the universal bounds, much less JC2; other formal
families and the source, `G2-PSC`, landing, off-axis, and type-provenance gaps
remain. TIER: census EXACT/book-relative; the convergence claim is a
single-model lead assessment, not a stopping rule or promoted reduction.

## DATED STRATEGY-STATUS CORRECTION — G2 SPLIT AND ARROWS (2026-08-23)

This entry explicitly supersedes every overloaded `G2`, `KJN <=> RPMC`, and
`UCD-A-min <=> A-SCALE` reading in the same-day roadmap entries above. It does
not retract their exact local identities; it corrects their global strategic
interpretation and status. The current detailed dependency theorem is
`ladder/REDUCTION.md`; this entry records the evidence/status correction.

- **`G2-PSC` (packet/sheet compatibility)** is the missing global theorem
  transporting a selected GGV packet/corner, with provenance, to a specified
  decorated Sigray pole tree faithfully enough for the book machinery.
- **`G2-BD` (bounded delay/carrier)** begins only after residue-A has been
  reached and asks for the carrier/delay bound needed to enter a finite book.
  Neither scoped obligation implies the other.
- A hybrid proof using GGV restrictions in the Sigray stage owes `G2-PSC`. A
  pure Sigray proof may bypass `G2-PSC` by selecting/minimizing the hypothetical
  counterexample wholly in that frame, but then it may not claim the unused
  GGV farm as input and still owes Sigray source, all-branch landing/coverage,
  `G2-BD` where used, and type/td control.
- The correct same-constant local arrows are
  `DIR(C) <=> PC(C) <=> RPMC(C) => KJN(C)`. There is no proved converse
  `KJN => RPMC`. KJN yields only `td <= C alpha beta` at a provenanced fixed
  type; absolute/cofinal control needs an independent bounded type menu with
  bounded constants.
- The correct architecture-scoped delay arrows are
  `A-SCALE => UCD-A-min => G2-BD`. No converse holds on present evidence, and
  restricted UCD-A-min does not imply the unrestricted UCD refuted by Henon.

STATUS: the pure-boundary identity/class-kill and unrestricted Henon
obstruction are dual-confirmed at their stated scopes. The KJN/RPMC/PC/DIR,
UCD-A-min/A-SCALE, formal countermodel, and DIR/A-SCALE comparison work is
single-model decisive partial unless separately reviewed later. In particular,
there is no promoted independence theorem joining `G2-PSC`/`G2-BD` to the
G5/type-ceiling side, no promoted merger theorem, and no implication making
the complete book ladder unconditional.

## D43 FULLY-RECONSTRUCTED RESIDUE-A FAMILY = NONEMPTY (2026-08-23, MOD-p / INTERNAL)
xmodel/sol-d43full.md; cases/d43_full_{family.py,certificate_p*.json,floor_p*.json}.
Fixed Sigray scale B=84, fiber a00pp, p=105337 & 105673. NOT char-0, NOT a
polynomial Keller map -- explicitly INTERNAL/UNREVIEWED/MOD-p.
- The fully graph-preserving family (218 nonredundant rows = 34 parked + 95 old
  graph bands 6-24 [the D21/D23/D25 reconstruction dropped by the prior
  overapproximation] + 89 late graph bands 26-42, in 184 vars) is NONEMPTY at
  both primes. Explicit 184-coordinate witness per prime satisfies all 218
  generators AND the independent full survivor gate (184/184 pristine residuals
  zero, s9_nu_ge_43 PASS, 18/18 floor checks; negative control tf1_57+=1 breaks
  18 rows). Method: exact 101-var slices only (no full-file msolve), decoded
  points replay all 184 graph rows.
- CORRECTION to the 2026-08-23 ~08:35 D43 note: the earlier "94 nonzero old
  coefficients" was a WITNESS-FAILURE count, not a missing-generator census; the
  properly reconstructed system imposes all 95 old-graph rows and is NONEMPTY.
- CONSEQUENCE: NO first depth kill. The fixed-B=84 residue-A carrier SURVIVES
  through depth 43. Floor ell+ >= 37 unchanged (window lower bound; e_plus still
  E_PLUS_CANDIDATE / certified=null; D75 = first Newton-cert depth). This is a
  live A-SCALE/carrier signal, but tests only FIXED B=84 depth -- it does NOT
  disprove A-SCALE (unbounded B), lift to char-0, or algebraize. Grok review
  pending. The A-SCALE resolution now hinges on the ALGEBRAIZATION gate, not on
  more fixed-scale depth.

## D43-FULL NONEMPTY: GROK-CONFIRMED + ALGEBRAIZATION GATE MAPPED (2026-08-23)
- grok-d43full-review.md CONFIRMS the 2026-08-23 D43-full entry: Completeness
  COMPLETE (10.8 omitted class present; no second overapproximation), Witness
  SOUND (independent replay both primes, 184/184+34/34 rows vanish incl. 10
  out-of-slice band-42 rows, floor_gate 18/18 byte-equal), Scope HONEST.
  Tier upgrade: MOD-p result is now DUAL-CONFIRMED. Scoped caveats (not holes):
  witness is the CELL ORIGIN (FREE=0), so the separate §10.7 fact "0/42 completed
  D25 points prolong at rung 26" stands (NONEMPTY != every point prolongs); 9
  band-10 rows degenerate to identities at the origin; old-graph hash audit is
  weaker than the late-graph byte regression.
- sol-lift.md maps the algebraization gate (mod-p -> char-0 -> polynomial Keller)
  as 8 stages: stage 0 (mod-p witness) DONE; stage 2 (char-0 point) settled by
  relative-smoothness/Hensel (KNOWN THEOREM) once a common integral model exists;
  stages 3-8 (inverse-limit survival, convergence/algebraicity, global gluing,
  polynomial+J=const, unbounded scale) all OPEN, stage 7 HARDEST. VERDICT: no
  known obstruction AND no known construction -- the carrier is modularly viable,
  not demonstrably algebraizable. Two primes+CRT do NOT give char-0; one Z_p-point
  does. Candidate obstructions (GCT-A/K2C/A-CONDUCTOR) all conjectural.
- NEXT (bounded, decisive): char-0 lift of the B=84 witness (relative smoothness
  => Hensel). Launched as sol-clift. B=168 scale test + reorg held for DC.

## D43 CHAR-0 LIFT SCREEN: p^2 PASSES, STAGE 2 OPEN (2026-08-23)
xmodel/sol-clift.md; cases/d43_char0_lift.py + d43_char0_lift_p105337.json.
- EXACT POSITIVE: coefficient radicals (r3, zeta42, A1, A2, h) Hensel-lifted to
  Z/p^2 (all defining residuals zero); the pristine 184-row Euler source system
  has rank J = 129 = rank[J | -F/p] and an explicit 24-coordinate correction
  replays 184/184 rows zero mod p^2 (direct reevaluation, not linear
  prediction). NO first-order local obstruction to lifting the D43 witness.
- EXACT: full special-fiber Jacobian rank of the 218-row system at the witness
  is 131 (tangent dim 53), with a certified unit 131x131 minor (det=810 mod p).
- NOT OBTAINED: common integral 218-row model (the d43red band .pkl checkpoints
  are ABSENT locally -- artifact-recovery item, likely box01), all-218 integral
  p^2 replay, local Krull dimension (Singular std capped 10 CPU-min), localized
  generation, p-flatness => the unit minor is NOT a standard-smooth certificate;
  Stacks 02H6 not invocable. X_43(C) != empty REMAINS OPEN.
- VERDICT: STAGE 2 OPEN -- no local obstruction found, no Hensel certificate.
  Next concrete item: recover/re-derive the band checkpoints to build the
  common integral model, then the dimension/flatness certificate.

## D43 MODULAR SOURCE/NF FIDELITY REVIEWED WITH SCOPED GAP; STAGE 2 OPEN (2026-08-23/24)
xmodel/sol-d43int.md (producer) and xmodel/review-d43-nf-fid-grok.md
(different-model hostile review: **CONFIRMED WITH GAPS**).
- EXACT, DUAL-MODEL CONFIRMED: the fully reconstructed modular presentation has
  184 variables and 218 rows = 34 parked + 95 old graph + 89 late graph rows at
  both primes; the row/eta census, checkpoint schema/prime/band/fiber, and all
  recorded canonical hashes replay. The 34 parked rows are the prime-specific
  D25 `.ms` files; the checkpoint payloads contain no integral or trace data.
- PRODUCER-FULL + INDEPENDENT SPANNING CORROBORATION at p=105337: the producer
  replay reconstructs all 184 checkpoint rows coefficient-by-coefficient as
  `R_raw = R_NF + sum Q_j G_j` (24.9M raw / 38.9M NF / 102.9M quotient-trace
  terms), dictionary-exact against the checkpoints. Grok independently parsed
  the 509 reducers and rebuilt tuple grevlex division on 2,355 groups across 62
  rows, including every group through band 14 and a row at every later band;
  zero mismatches. It also checked a bijection and origin evaluation on all
  382,824 groups. The remaining 122 fat-row dictionary remainders and the full
  producer replay were not regenerated, so this clause is corroborated rather
  than fully dual-recomputed.
- SCOPE CORRECTION: this establishes that the **checkpoint NF rows** are the
  stated modular source reductions. At band 42 the final `rung_kernel` assembly
  adjoins the `Xf_alpha`/`Xg_beta` P4P1 correction; those names are absent from
  the checkpoints and the 184 source-to-NF traces. Thus “all assembled graph
  polynomials are covered by those checkpoint traces” would overstate the
  reviewed result. The separately hashed modular assembly/census still passes,
  and the source-honesty gate below now accounts for the sidecar explicitly.
- Bandwise local-normal-form engine (nested pivots + product criterion, no std):
  localized generation on the fixed parked fiber PASSES through band 32; band 34
  is a 300s timeout (not a nonzero remainder). The 9 band-10 origin identities
  are locally generated by earlier pivots (not a hidden quadratic cut).
- STILL OPEN (stage 2): common integral presentation (the D23 reducer basis and
  parked rows exist only as prime-specific modular objects), all-218 p^2 replay,
  local dimension 53, generation by the 131 unit-minor equations, p-flatness,
  any Z_p / char-0 point. The reviewed source-defined D25-to-D27 one-band
  signal below makes its full-cell compatibility locus the next discriminator.
  Decide that locus before integral D43 engineering; only a separately reviewed
  coherent stratum could license re-emission over the radical number ring with
  reducer-to-parked traces and non-origin local membership.

## D43 BAND-42 P4P1 SIDECAR IS SOURCE-DERIVED AND ORIGIN-ONLY (2026-08-24)
xmodel/round2-p4p1-honesty-20260824.md and
cases/round2_p4p1_honesty/ (exact producer plus independent replay), with
xmodel/review-p4p1-honesty-grok.md (different-model hostile review:
**CONFIRMED; exact-source / MOD-p compiler-interface tier**).
- EXACT SOURCE IDENTITY: the sidecar correction is
  `42*S_M*G_M*(3*alpha-2*beta)*p(eta)^4*p'(eta)`. A direct four-term Euler
  expansion and an independent factored-product derivation agree before
  specialization; the actual `rung_kernel` subtraction matches all ten rows.
- EXACT BASE-IDEAL STATUS: neither checkpoint contains `Xf_alpha` or
  `Xg_beta`. At both registered primes, all twenty sidecar coefficients are
  nonzero constants and hence remain unchanged under the registered
  509-element `I23` Groebner bases. The correction is not zero modulo the base
  ideal and is load-bearing away from its sidecar zero line.
- VERDICT `ORIGIN-ONLY`: at the named completion `alpha=beta=0`, used by the
  modular origin witness, the correction vanishes; at the fixed control
  `(alpha,beta)=(1,0)` it changes all ten rows. Therefore no wrong mathematics
  invalidates that origin witness. The defect was the provenance/scope slogan:
  checkpoint source traces do not themselves cover the later sidecar.
- REVIEW HARDENING: the hostile reviewer independently derived the identity,
  executed the live `rung_kernel` assembler on empty input and all ten real
  checkpoint rows at both primes, and recomputed every exact `I23` normal form.
  The sidecar-zero locus is the line `3*alpha-2*beta=0`; nonzero graph
  reconstruction witnesses away from that line are outside this origin gate.
- CLEAN WORDING: “checkpoint rows are source-to-NF traced modulo `I23`; final
  assembly adjoins the displayed exact source-derived sidecar, which vanishes
  at the named origin.” No integral emitter, general D43 nonemptiness,
  compatible tail, germ, characteristic-zero point, or JC2 inference follows.

## D25-TO-D27 SOURCE TRANSITION: ONE-BAND FREE-TAIL SIGNAL (2026-08-24)
xmodel/round1-dtransition-20260824.md and
cases/round1_dtransition/ (producer), with
xmodel/review-dtransition-grok.md (different-model hostile review:
**CONFIRMED**).
- SCOPE: exact modular arithmetic at `p=105337,105673`, fiber `a00pp`, one
  chart, four named points, and band 26 only. The unreduced recurrence gives a
  typed projection `X27 -> X25`, adding exactly ten band-26 rows and ten
  first-occurrence coordinates without changing a lower row. It imports no
  D43 or `D43-NF-FID` artifact.
- POSITIVE POINTWISE SIGNAL: at each of two named witnesses,
  `rank(A)=rank([A|b])=4`; the affine fiber has dimension six, and all twelve
  displayed kernel lifts (six at each prime) replay through the unreduced
  source recurrence to band 26.
- NEGATIVE POINTWISE SIGNAL: at each of two deterministic interior points,
  `rank(A)=4` but `rank([A|b])=5`; exact left-cokernel pairings are nonzero, so
  those points do not prolong through this band.
- VERDICT `FREE-TAIL-SIGNAL`: compatible one-band fibers exist over the two
  witnesses while other D25 points are cut. The same lifted directions leave
  nonzero residuals at bands 30, 36, and 40. Therefore this proves no
  component, dominance, full-cell rank statement, band-28 persistence,
  compatible inverse system, formal germ, characteristic-zero point, or
  polynomial Keller map. The registered next gate is the source-defined
  compatibility locus on one full promoted D25 cell, stopping before band 28.

## D25 CELL-0 BAND-26 COMPATIBILITY LOCUS IS NONEMPTY, RANK AT LEAST FIVE (2026-08-24)
cases/round1_dtransition_fullcell/ and
xmodel/round1-dtransition-fullcell-20260824.md (producer), with
xmodel/review-dtransition-fullcell-grok.md (different-model hostile review:
**CONFIRMED**).
- SCOPE: `p=105337`, fiber `a00pp`, promoted cell-0 `A^14`, fixed
  `(W1,W2)=(31931,9457)`, and the source-defined band-26 compatibility problem
  only. The six functions are the canonical left-cokernel contractions of the
  unreduced ten-row source block after exact D25 and band-24 triangular
  pullback. No D43 artifact enters.
- NONEMPTY + LOWER RANK BOUND: the cell origin is a certified common zero. Its
  exact `6 x 14` Jacobian has rank five, witnessed by a nonzero `5 x 5` minor
  of determinant 39793. Hence the compatibility locus on this modular cell is
  nonempty and the generic differential rank is at least five. The
  preregistered rank-six-at-origin gate failed.
- MIXED FULL-CELL BEHAVIOR: the deterministic same-cell point with free
  coordinates `1,...,14` is cut by compatibility; its function vector is
  `(23070,55420,82249,287,11111,1237)` and its Jacobian again has rank five,
  with displayed minor 104469. Thus the pointwise witness/interior split was
  not merely a comparison between different cells.
- SOURCE/TANGENT CHECK: the full reconstruction and a scratch rerun are
  byte-identical. Independent differentiation confirms the cell, 86-row
  D21/Row-22, prefix, and band-24 frontier chains. The shared-prefix derivative
  is `1-C_k`; replacing it by `-C_k` changes the origin minor and makes the
  sequence-point frontier tangent inconsistent at `x68=uf18`.
- OPEN UPPER BOUND: the constant row vector
  `(104372,48519,44983,31248,84848,1)` annihilates function values and
  Jacobians at the two registered points and four hostile extra probes, but no
  global polynomial-identity certificate was obtained. Do not infer generic
  rank exactly five, dimension, reducedness, or component structure.
- NO DESCENT INFERENCE: nothing here proves a non-origin compatible rank-six
  point, band-28 persistence, a compatible inverse system, formal germ,
  characteristic-zero point, algebraization, polynomial Keller map, or JC2
  counterexample. The licensed provisional continuation was the separate
  source-stationarity gate, not another depth computation; it has since
  returned producer/replay `NO-TYPED-STATIONARITY` because the current full
  source does not classify its first x-side directions. The following entry
  records its separate hostile confirmation.

## D SIX-BAND PURE-Y LAW CONFIRMED; FULL SOURCE NOT TYPED (2026-08-24)
xmodel/round2-dstate-gate-20260824.md and cases/round2_dstate_gate/
(exact producer plus independent replay), with
xmodel/review-dstate-grok.md (different-model hostile review:
**CONFIRMED**).
- POSITIVE SCOPED RESULT: at the two registered modular D25 witnesses, the
  unreduced pure-`y` source through band 40 has the corrected 30-input /
  30-output six-band state, including `H_29` at start 36. The shifted
  first-occurrence layers at bands 26, 32, and 38 are exact `10 x 10` types;
  their truncation squares commute coefficientwise, dual and grouped source
  derivatives agree, and `M_38-2*M_32+M_26=0` after six-shift relabeling.
- FIRST FULL-SOURCE INTERFACE: independently,
  `[t^42]E_full=[t^42]E_y+42*S_M*G_M*(3*alpha_1-2*beta_1)*p(eta)^4*p'(eta)`.
  Both partials are nonzero over `Q` and at both registered primes.
- VERDICT `NO-TYPED-STATIONARITY`: the current constructor has no x-side
  argument; its 30 streams contain neither `alpha_1` nor `beta_1`; and no
  source-derived held/derived/independent classification, chain rule,
  six-shift relabeling, or projection map for them is banked. Choosing one
  would invent the state map.
- NOT SHOWN: the three-layer affine check is not an all-depth stationarity
  theorem. No finite full-source state, Ore/Spencer/Fitting or syzygy object,
  band-28 persistence, D43 result, inverse system, germ, characteristic-zero
  point, algebraization, polynomial Keller map, or JC2 inference follows.
  The frozen `UNBOUNDED-STATE` label is not implemented as a producer branch;
  future reuse must close that driver-completeness gap. It does not alter this
  verdict because the omitted factor directions form a finite but untyped list.
- FROZEN-SOURCE DOCUMENTATION CAVEAT: the header of `cases/valuation_e2.py`
  still narrates the earlier 29-output candidate (`E_29=0`, start sum 240),
  although the same file later records its refutation. The source byte is
  preserved because several manifests pin it. This confirmed entry supersedes
  that header for live state: include `H_29` at start 36, giving 30 outputs and
  start sum 276; the legacy tool's 29-output diagnostic remains historical.

## EXACT-COFRAME PRIORITY + FIXED BROUGHTON/COHN NO-GO (2026-08-24, DUAL-CONFIRMED)
`xmodel/exact-coframe-gate-20260824.md` and
`cases/exact_coframe_gate_20260824/` (exact producer/replay), with
`xmodel/exact-coframe-gate-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**) and the citation-preserving
`xmodel/exact-coframe-gate-20260824-erratum.md`.
- CLASSICAL ONE-WAY CERTIFICATE: if both rows of
  `M in SL_2(C[x,y])` are closed, polynomial integration gives
  `M=J(P,Q)`. Jung--van der Kulk plus the chain rule puts the determinant-one
  Jacobian of every plane automorphism in `E_2(C[x,y])`. Literal
  `M notin E_2` therefore gives a characteristic-zero plane Keller
  nonautomorphism. This uses no quotient `SL_2/E_2` and no normality claim.
- PRIORITY CORRECTION: the bridge/reformulation is not campaign-new. Wright's
  1978 weak Jacobian theorem supplies the converse for a **full** Jacobian in
  `GE_2`; its exact Theorem 6/page-250 wording is frozen from primary-research
  restatements because the original Elsevier body was inaccessible. The
  canonical DOI is `10.1016/0022-4049(87)90004-1` despite the 1978 year.
- COHN LINEAGE: the standard Cohn matrix is non-elementary by Cohn Proposition
  7.3 and Park's leading-row certificate. Entry substitution `y -> 2y`
  preserves nonmembership and gives
  `C_B=[[1+2xy,x^2],[-4y^2,1-2xy]]`; its first row is
  `d(x+x^2y)`. The frozen report's reference to Cohn section 8 is corrected to
  the end of section 7. The retrieved arXiv:2412.03688 artifact is v1,
  2024-12-04; an unsupported 2026 manuscript date is withdrawn.
- SCOPED NEW NEGATIVE: every determinant-one polynomial completion of the
  fixed first row is uniquely `L(h)C_B`. Its second row is closed exactly when
  `(1+2xy)h_y-x^2h_x=6y`. On the preregistered three-term support the exact
  linear map has rank 3 and augmented rank 4, with an explicit unit
  certificate. Globally, the weight recurrence forces
  `c_n=(-1)^n(n+3)` and an uncancelled terminal term for every finite
  polynomial. The rational/formal control
  `h=y^2(3+2xy)/(1+xy)^2` has precisely the nonterminating series.
- SOURCE HAZARD: Shpilrain--Yu Proposition 2.4's printed claim that an
  arbitrary second row beneath a gradient first row in `GE_2` must itself be
  a gradient is false as printed: `L(y)` is elementary, has first row `dx`,
  and has non-closed second row `(y,1)`. Wright assumes a full Jacobian; this
  stronger assertion is not imported.
- SCOPE: this closes only the complete fixed-first-row / one-left-shear
  Broughton/Cohn family. It does not close `E_2 C E_2` with a changed first
  row, produce a Keller pair, or prove/disprove JC2. No second shear, support
  widening, or generic sparse search is licensed by this result.

## NORMALIZATION RANK-TWO NO-GO (2026-08-24, KNOWN-THEOREM/REDERIVATION TIER)
`xmodel/completion-pair-gate-20260824.md` (self-contained producer proof), with
`xmodel/completion-pair-rank2-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**).
- PROMOTED AT KNOWN-THEOREM/REDERIVATION TIER: a complex plane Keller map
  cannot have function-field degree two. For
  `A=C[P,Q]`, `B=C[x,y]`, and the normalization `R` of `A` in `Frac(B)`,
  Zariski Main embeds `Spec B` as an open in `Spec R`. Rank two, trace
  splitting, and `Pic(A)=0` give
  `R=A+Az ~= A[z]/(z^2-h)` with `Tr(z)=0` and
  `Omega_(R/A)=(R/(2z))dz`. Keller etaleness on the open chart makes `z` a
  unit of `B`; since `B^*=C^*`, scalar trace forces `z=0`, a contradiction.
  Equivalently, every squarefree branch factor gives the forbidden principal
  boundary relation `div_X(q_i)=2E_i`.
- WORDING CAVEAT: `j(U)=X` gives finiteness; concluding automorphy in general
  also invokes triviality of connected finite etale covers of `A^2_C`. The
  rank-two unit/trace contradiction itself does not need that extra sentence.
- KNOWNNESS: quadratic extensions are Galois, so this statement follows from
  the classical Galois case (Campbell/Razar/Wright/Bass--Connell--Wright).
  Orevkov, *On three-sheeted polynomial mappings of C^2*, Theorem 1.1, defines
  multiplicity as generic fibre cardinality and proves that a complex plane
  Keller map has multiplicity neither two nor three. Thus a rank-three
  continuation is also known-closed; this says nothing about polynomial total
  degree three.
- GLOBAL LOW-SHEET CHECKSUM: the preceding producer proof itself stops at
  rank two, but **generic mapping/topological degree four is not open**.
  Domrina, *On four-sheeted
  polynomial mappings of C^2. II. The general case*, Izv. Math. 64:1 (2000),
  1--33, proves that no four-sheeted complex plane polynomial map has nonzero
  constant Jacobian (MathNet `im273`). Żołądek, *An application of
  Newton--Puiseux charts to the Jacobian problem*, Topology 47 (2008),
  Theorem 6.12, proves invertibility for topological degree at most five.
  Hence the first open mapping/topological degree is six, consistently with
  `ladder/SHEET6.md`. The round-0719 packet's global reading of “ranks at
  least four untouched” was a priority error and licensed no quartic replay.
- SCOPE: this rank-two gate is not a new theorem, a finiteness proof in
  arbitrary rank, or a JC2 result. Its local proof does not rederive the
  separate known rank-four/five theorems.

## WEIGHTED D LEVEL-TWO SOURCE GATE (2026-08-24, DUAL-CONFIRMED SOURCE-TYPING TIER)
`xmodel/weighted-d-source-gate-20260824.md` and
`cases/weighted_d_source_gate_20260824/` (exact producer/replay), with
`xmodel/weighted-d-source-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**).
- FROZEN-PERIMETER VERDICT: at basis
  `dd11599b07eb05591b5c006791005eef19457d8e`, all 25 registered source hashes
  match, but no promoted producer supplies a named normalized full-polynomial
  source completion and typed tangent maps through
  `alpha_1,beta_1,alpha_2,beta_2`. P4P1 symbols are external compiler
  variables; `eplus43` is an unreviewed zero/independence constructor choice
  and stops before factor level two.
- EXACT AMBIENT ALGEBRA: the coordinate change through `q^2=t^84`, the
  unreduced identity
  `B_full=R^2 C^5 B+R C^5(theta R)A+R^2 C^4(theta C)D`, and every displayed
  level-42/84 chain-rule term independently replay. Level 84 contains the old
  carrier `c_1`; `c_2` drops out only because `B_0=D_0=0`.
- PROMOTED STOP: `NO-TYPED-SOURCE/NO-QUOTIENT` means that no quotient test is
  presently licensed, not that a mathematical quotient is nonexistent. The
  free formal span is an acceptance target, not `T_src`; it cannot certify
  `TWO-DRIVER`, a Hankel pivot, a recurrence, or a state dimension.
- RESURRECTION: require one producer artifact reconstructing the first two
  factor levels from `phi_f,phi_g` (or an exact R2/h-Newton model), with the
  named point, stable source labels, tangent maps, relations, and full chain
  rule. Another external sidecar or modular D row is not enough.
- SCOPE: no band 28/deeper D, D43 integral, syzygy/Spencer/Fitting, germ,
  characteristic-zero point, polynomial Keller map, or JC2 inference follows.

## HAMILTONIAN KAPPA CLASS + `x+x^n y` FAMILY NO-MATE (2026-08-24, DUAL-CONFIRMED SCOPED TIER)
`xmodel/hamiltonian-kappa-gate-20260824.md` and
`cases/hamiltonian_kappa_20260824/` (exact producer/replay), with
`xmodel/hamiltonian-kappa-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**).
- EXACT CLASS: for a polynomial `P` with unimodular gradient, choose a
  polynomial vector field `V(P)=1` and put
  `kappa(P)=[div V] in C[x,y]/D_P(C[x,y])`.  The syzygy module of
  `(P_x,P_y)` makes this independent of `V`.  Subtracting `hD_P` and applying
  the polynomial Poincare lemma proves
  `kappa(P)=0` iff some polynomial `Q` satisfies `[P,Q]=1`, with all signs
  independently checked.
- PRIORITY: Friedland 2001 already defines this cokernel and its
  Gauss--Manin operator, whose value at one is `kappa(P)`.  Dimca--Saito type
  the same element as `partial_t[dx wedge dy]` in the Brieskorn module.  No
  primary source or gate result supplies a finite universal receiver forcing
  this class to be nonzero for every noncoordinate.
- SCOPED FAMILY THEOREM: for every integer `n>=2`,
  `P_n=x+x^n y` has unimodular gradient.  The weight
  `w(i,j)=i-(n-1)j` exhausts all monomials that could contribute to
  `[P_n,Q]=1`; coefficient recursion gives a nonzero infinite chain and an
  uncancelled terminal term for every finite polynomial.  Hence no polynomial
  mate exists.  The replay passed 4,979 exact checks and the rational/formal
  slice is correctly nonpolynomial.
- SCOPE: this is a controlled infinite-family theorem whose members are not
  Keller coordinates; literature novelty is not claimed.  The class is an
  exact reformulation of the missing mate, not a new global obstruction.  No
  generic sparse widening, universal receiver, proof, or counterexample to
  JC2 follows.

## DUAL-PENCIL INFINITY DEFECT IS JUMP-ONLY, NOT THE PROPOSED DIVISOR (2026-08-24, DUAL-CONFIRMED DEFINITION STOP)
`xmodel/dual-pencil-definition-gate-20260824.md` (corrected producer), with
`xmodel/dual-pencil-hostile-audit-20260824.md` (internal hostile source audit:
**PASS WITH SCOPED CORRECTION**) and
`xmodel/dual-pencil-review-grok-20260824.md` (different-model review:
**CONFIRMED**).
- EXACT CORE: for a Keller pair and every nonzero direction
  `H=aP+bQ`, `H` is a polynomial submersion.  Suzuki's primitive
  factorization gives connected generic fiber and total infinity defect
  `delta(H)=1-chi(G_H)=b_1(G_H)>=0`.
- ENDPOINT: `delta(H)=0` makes the generic fiber `A^1`; the resulting
  coordinate direction, together with its Keller mate, makes the original
  pair an automorphism.  Thus any hypothetical nonautomorphic Keller pair has
  positive defect in every pencil direction.
- TYPE VERDICT: the universal defect therefore has horizontal support over
  the whole dual line, not a finite effective divisor.  Subtracting the
  generic value leaves only a jump cycle and destroys the proposed
  degree-zero endpoint.  At constant polynomial degree, Siersma--Tibar
  Proposition 5.1 gives a nonpositive jump coefficient; at the possible
  degree-drop direction the coefficient remains uncontrolled.  This corrects
  the producer's original sign assertion without changing
  `PRIOR-ART / JUMP-ONLY / TYPE-FAIL`.
- SCOPE: the signed jump cycle is a resolution-independent finite formal
  cycle, but no finite **effective** divisor with the proposed degree-zero
  endpoint, GRR formula, new positivity obstruction, or JC2 result follows.
  No dual-pencil descendant is licensed without a genuinely new typed object.

## AS109 SUPPORT GRAMMAR STOP + CARRY CORRECTION (2026-08-24, DUAL-CONFIRMED CORRECTED SPECIFICATION TIER)
`xmodel/as109-support-gate-20260824.md` and
`cases/as109_support_20260824/` (frozen specification and exact controls),
with `xmodel/as109-support-review-grok-20260824.md`, the frozen
`xmodel/as109-support-gate-20260824-erratum.md`, and
`xmodel/as109-carry-erratum-review-grok-20260824.md` (different-model
follow-up: **CONFIRMED**).
- REGISTERED STOP: a cap of eight correction slots does not bound literal
  exponents.  For every `m>=1`, the exact triangular automorphism
  `G_m=(x+109y^m,y)` gives a two-slot first layer and a five-slot two-layer
  union after exact successor transport; its exponents remain unbounded.
  Nonlinear residual support
  changes along the exact source-gauge orbit, so no finite exhaustive graph
  exists without a proved gauge section or groupoid transition rule.  No
  enumerator or AWS job ran; no cap-eight existence or nonexistence statement
  follows.
- CARRY ERRATUM: for integral digit lifts, put
  `C_1=L(A_0,B_0)-x^108` and `K=C_1/109` after the first congruence.  The
  correct second digit is
  `K+L(A_1,B_1)+N_0=0 mod 109`; marked-section equations have analogous
  evaluation carries.  A five-slot countercontrol passes the frozen
  uncarried `E1/E2` but has
  `det J-1=109^2*x^108 mod 109^3`.  This supersedes claim 2 of the original
  review only at the inference from the correct determinant expansion to an
  uncarried generic second digit.
- SURVIVING OBSTRUCTION: the parametric triangular family has `C_1=0` and
  its successor equation over `Z`, so its carry is identically zero.  Hence
  `NO-FROZEN-GRAMMAR`, the unbounded-support witness, and the stopped scope
  survive the correction exactly.
- CONDITIONAL HENSEL BRIDGE: any exact polynomial
  `F in Z_109[x,y]^2` reducing to `(x-x^109,y)` with `det J_F=1` has the
  following property: for each fixed residue `b`, the 109 source balls
  `(a,b)+109Z_109^2`, indexed by `a`, each map bijectively onto the target
  ball `(0,b)+109Z_109^2`.  It is therefore noninjective over `Q_109`;
  adjoining finitely many
  coefficients and two preimages gives a finitely generated characteristic-
  zero field that embeds in `C`, hence a complex Keller counterexample.  This
  assumes an exact lift and does not assert one exists.
- CONDITIONAL CONTRACTION: let `U'` be a finite free gauge-fixed coefficient
  module and `W` a finite residual module with
  `x^108 in W`, `L(U') subset W`, and `N(U') subset W`.  An integral right
  inverse `R:W->U'` whose image is the chosen section makes
  `T(u)=R(x^108-109N(u))` a strict contraction.  `CLOSED-SUPPORT + UNIT-L`
  would therefore construct the exact lift needed above.  No known support
  meets these hypotheses.
- SCOPE: this is a corrected specification stop plus two conditional
  resurrection lemmas.  There is no `HEIGHT-CERT`, `NO-CYCLE-AT-8`, found
  lift, characteristic-zero inference, proof, or counterexample to JC2.

## D73 DIRECTION-COLLISION STRICTNESS HAS AN EXACT EQUALITY CONTROL (2026-08-24, DUAL-CONFIRMED LOCAL TIER)
`xmodel/d73-strict-or-equality-20260824.md` (producer), with
`xmodel/d73-strict-or-equality-review-grok-20260824.md` (different-model
hostile review: **CONFIRMED**).
- EXACT LOCAL GERM: in the infinity chart `s=y^-1`, `t=xy^4`, put
  `q=t+t^25`, `g=q(t)`, and
  `f=t^15+s^3/(3q'(t))`.  Both `dx wedge dy` and `df wedge dg` equal
  `s^2 ds wedge dt`, so the analytic germ has Jacobian one exactly.  Its
  height-four data match sharp SP-2:
  `(k_f,l_f)=(60,15)`, `(k_g,l_g)=(100,25)`, `pi(G)=4`, `kappa_G=1`, and
  direction multiplicity 15.
- EQUALITY: on `f=0`, a holomorphic unit change gives `S^3=t^15`.  There are
  exactly three normalized branches, each with `y`-pole order five, first
  contact `21/5`, and `Lambda=1`.  Hence the collided direction has
  `sum Lambda=3=pi(G)-1`, attaining Proposition 7.3's lower bound despite
  multiplicity greater than one.
- GENERIC-FIBER TYPE CHECK: for small generic `a`, the fifteen simple roots
  of `t^15=a` lie in one local neighborhood, but their values
  `q(t_i)` are pairwise distinct.  Each puncture has local multiplicity three
  while the cover over any one target value has degree three.  Adding all
  fifteen multiplicities would illegally mix fifteen different `g`-fibers.
- SOURCE WORDING: Sigray Proposition 7.3 says equality holds **if** the
  direction root is simple; it states no converse.  The two former
  `iff mult=1` readings in `ladder/SHEET6-LROOT.md` are corrected to the
  one-way statement.  Direction multiplicity alone therefore cannot force
  the hoped-for strict extra delta unit.
- SCOPE: `f` is rational/analytic, not a global polynomial in `(x,y)`.  This
  is a local equality control, not a Keller counterexample, a realization or
  kill of any of the eight terminal classes, or a global equality theorem.
  The remaining implication must use global polynomial realizability,
  opposite-side compatibility, or an additional branch elsewhere on the
  same compactified fiber.  No proof or counterexample to JC2 follows.
- REVIEW METADATA: some Grok reports across this and successor batches contain
  inaccurate human-written review windows. The authoritative automatic runner
  times and frozen hashes are recorded in the immutable
  `xmodel/review-window-erratum-20260824.md` and its cumulative `-v2`
  successor; no mathematical verdict changes.

## AS109 INDEPENDENT-SLOT + QUADRATIC-Y NO-GOS (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/as109-closed-support-gate-20260824.md` and
`xmodel/as109-quadratic-coupling-gate-20260824.md`, with hostile
different-model reviews `xmodel/as109-natural-nogo-review-grok-20260824.md`
and `xmodel/as109-quadratic-review-grok-20260824.md`: **CONFIRMED**.

- INDEPENDENT-SLOT THEOREM: report/review SHA-256 are
  `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` /
  `3b0d369c678a518614be0218c434eec97c43af0747aa8a26906256e12d2b13d5`.
  In a full independently variable literal-slot module, a unit right inverse
  at `x^108` forces `(0,x^108 y)`. Nonlinear closure and polarization then
  force every `x^(108k)` into the finite residual module, a contradiction.
  This excludes the raw independent-slot certificate, not genuinely coupled
  modules or arbitrary fixed support.
- QUADRATIC FIELD THEOREM: report/review SHA-256 are
  `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` /
  `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2`.
  Over every characteristic-zero field, a Keller pair whose two coordinates
  have `y`-degree at most two is a polynomial automorphism. The cubic
  Jacobian coefficient makes quadratic tops proportional; a target `GL_2`
  operation makes one coordinate affine; the mixed coefficient gives
  `b_2=k a_1^2`; a polynomial target shear removes it; the affine pair has an
  explicit triangular inverse. No algebraic closure, source substitution, or
  nonconstant denominator is used.
- AS109 CONSEQUENCE: an exact lift with both correction `y`-degrees at most
  two would be an automorphism over `Q_109`, contradicting the already
  reviewed 109-ball Hensel noninjectivity. Thus a surviving lift needs
  essential coefficient coupling and, at this tier, `y`-degree at least
  three in one correction. No lift, arbitrary-support no-go, or JC2 inference
  follows.

## TD6 CENTERING ESCAPE + FINITE-JET CONTROL (2026-08-24, DUAL-CONFIRMED STOP TIER)

`xmodel/td6-global-compatibility-gate-20260824.md` (producer SHA-256
`b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17`)
with `xmodel/td6-global-compatibility-review-grok-20260824.md` (review
SHA-256
`f3e468f415fdd7bd1aa85962090d34a55bf6ff15d469c28373347cf1c7cc42ac`):
**CONFIRMED `CENTERING-ESCAPE / FINITE-JET-CONTROL / STOP`**.

- BARE LEMMA: in the zero-centered chart `x=t s^R`, `y=s^-1`, every positive
  `s^k` coefficient of a polynomial holomorphic there is divisible by
  `t^ceil(k/R)`. If both members of a Keller pair were holomorphic in that
  same chart, the Jacobian would vanish at `t=0`, an exact contradiction.
- CENTERING ESCAPE: LR2 does not force the shared lower truncation to zero.
  The legal choice `x=s+t s^4`, `y=s^-1` has the polynomial Eggers coordinate
  `T=xy^4-y^3=t`, so the bare divisibility inference is not available.
- GLOBAL POLYNOMIAL CONTROLS: explicit pairs inside the fixed SP-2 rectangles
  reproduce its height-four patterns and three-branch
  `sum Lambda=3` mechanism. Their centered Jacobian errors have exact orders
  three and six. Neither pair is Keller. A characteristic-zero Bezout
  recursion in `Q[T][[x]]` constructs arbitrary finite one-sided Keller jets
  only after dropping the degree cap; degrees grow and no convergence,
  algebraization, or opposite-chart statement follows.
- NEXT GATE: fixed `Q[x,y]` rectangles, explicit common-centering
  coefficients, the opposite r9/M2 chart, and exact global `J=1` must be
  imposed together. No terminal class is killed or realized. The two
  LaTeX-only producer slips are frozen in
  `xmodel/td6-global-compatibility-format-erratum-20260824.md`; code and math
  are unchanged.

## SECANT IDEMPOTENT REMOVES COLLISION SATURATION (2026-08-24, DUAL-CONFIRMED ACCELERATOR TIER)

`xmodel/fresh-connection-gate-20260824.md` (producer SHA-256
`666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`)
with `xmodel/secant-idempotent-review-grok-20260824.md` (review SHA-256
`6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9`):
**CONFIRMED**.

For `I=(F(x,y)-F(u,v))`, diagonal ideal `Delta=(x-u,y-v)`, constant
Jacobian `c`, and any polynomial secant matrix `A`, put
`e=c^-1 det A` in `C=S/I`. The adjugate gives `e Delta=0`; restriction to
the diagonal gives `1-e in Delta`; hence `e^2=e`, uniquely among elements
with those two properties. Moreover

```text
I:Delta = I:Delta^infinity = I+(det A)
```

as schemes, with `eC` the reduced diagonal quotient and `(1-e)C` the off
factor. Different secant conventions give the same class modulo `I`. This is
a substantial software simplification to one explicit third generator, but
making that ideal unit for all characteristic-zero Keller maps is exactly
injectivity/JC2. The identity is standard neighboring secant/Bezoutian and
collision-ideal algebra; no priority novelty is promoted.

## PROJECTIVE COLLISION CONNECTEDNESS IS COSTUME (2026-08-24, DUAL-CONFIRMED NEGATIVE TIER)

`xmodel/secant-projective-connectedness-gate-20260824.md` (producer SHA-256
`cabfa347efc22b90b1c4c0808ceb1e1ac0bce235d35e8e28d9f27cc6bc614fb2`)
with `xmodel/secant-projective-review-grok-20260824.md` (review SHA-256
`99b7649365a3fbae34932c2bacc03ad141507f74a6ca55d2945bc427e0404957`):
**CONFIRMED `COSTUME / NEED-Z-SATURATED-INFINITY-DATUM`**.

- The honest projective closure is cut out by `K:Z^infinity`, not the two
  naive homogenized difference equations `K`. A nontrivial tame automorphism
  gives an exact control: the naive complete intersection contains two whole
  infinity surfaces; saturation exponent four removes them and leaves only
  the diagonal, while the secant off ideal saturates to `(1)` at exponent
  three.
- Over `F_3`, the Artin--Schreier Keller collision has honest saturated
  diagonal/off components meeting scheme-theoretically on the doubled line
  `(X-U,Y-V,Z^2)`. Thus affine etaleness can move all contact to the boundary
  without contradiction.
- Consequently projective complete-intersection connectedness supplies no
  general obstruction and kills no named characteristic-zero family. A live
  descendant needs the source-derived saturated boundary-intersection cycle
  on a pinned compactification. No proof or counterexample follows.

## AS109 CUBIC-Y NO-GO (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/as109-cubic-coupling-gate-20260824.md` (producer SHA-256
`198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820`)
with `xmodel/as109-cubic-review-grok-20260824.md` (review SHA-256
`2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef`):
**CONFIRMED**.

- FIELD THEOREM: every Keller pair over an arbitrary characteristic-zero
  field whose two coordinate `y`-degrees are at most three is a polynomial
  automorphism. Equal cubic tops reduce by constant target `GL_2`; an
  affine/cubic top reduces by `g-k f^3`; lower cases use the quadratic theorem.
- GENUINE `(2,3)` CASE: UFD valuations normalize the leading coefficients to
  `h^2,h^3`. A constant target addition aligns the two rational depression
  shifts and gives
  `f=z^2+U`, `g=z^3+Vz+W`, `z=hy+r`. The Jacobian equations are
  `V'=3U'/2`, `W'=0`, `hU'V=j`. Polynomial constant terms give the monic
  equation `r^3-(3D+2c)r+2(G-w)=0`; integral closure makes `r,U,V`
  polynomials. Their unit product then contradicts `V'=3U'/2`.
- DESCENT/SCOPE: automorphy descends from the algebraic closure by uniqueness
  or faithful flatness. No source coordinate change, support cap, `x`-degree
  bound, or finite-Witt inference is used. An exact AS109 lift with both
  correction `y`-degrees at most three would be an automorphism over `Q_109`
  and contradict Hensel noninjectivity. Thus a surviving lift needs
  `y`-degree at least four in one correction. No quartic theorem, lift,
  arbitrary-support no-go, novelty claim, or JC2 decision is promoted here.

## SECANT x AS109 IS LOCAL-RANK COSTUME (2026-08-24, DUAL-CONFIRMED NEGATIVE TIER)

`xmodel/secant-as109-cross-gate-20260824.md` (producer SHA-256
`f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf`)
with `xmodel/secant-as109-review-grok-20260824.md` (review SHA-256
`16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029`):
**CONFIRMED `COSTUME / NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM`**.

- The seed collision algebra has `t=x-u`,
  `I_0=(t(1-t^108),y-v)`, `e_0=1-t^108`; its off factor is the product of
  108 copies of `F_109[u,y]`. The 108 CRT projectors and their Teichmuller
  lifts record the already-known Hensel collision sheets.
- On every off sector `x-u` is a unit and the adjugate identity gives
  `e=(x-u)^-1(a_22 f_1-a_12 f_2)`. Scheme-theoretically
  `(f_1,f_2,e)=(f_1,f_2)` after localization, and at a collision
  `de=(x-u)^-1(a_22 df_1-a_12 df_2)`. Thus a compiler that already includes
  matching-precision collision equations gains coefficient/tangent rank zero
  from the raw secant row, including its carried digit equations.
- Trace, norm, factor count, and derived support are ranks or consequences of
  the analytic split, not new bounded polynomial constraints. Resume only
  with an independently constructed finite normalization, bounded polynomial
  branch algebra, or global elimination datum that couples all 108 sectors
  and adds positive rank. No contradiction, finite constraint, lift, or JC2
  decision follows.

## AS109 QUARTIC-Y NO-GO (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/as109-quartic-discriminator-gate-20260824.md` (producer SHA-256
`8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`)
with `xmodel/as109-quartic-review-grok-20260824.md` (review SHA-256
`3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e`):
**CONFIRMED**.

- FIELD THEOREM: over every characteristic-zero field, a Keller pair whose
  two coordinate `y`-degrees are at most four is a polynomial automorphism.
  Equal/top-divisible cases reduce to the independently re-proved cubic base;
  the only new actual pair is `(3,4)`.
- GENUINE `(3,4)` CASE: after UFD normalization and aligned depression,
  `f=z^3+uz+v`, `g=z^4+az^2+bz+c`. The five coefficient rows are
  `4u'-3a'`, `4v'-3b'`, `2au'-3c'-ua'`,
  `bu'+2av'-ub'`, and `bv'-uc'`. They give
  `(4u/3+2alpha)v=delta` and the constant Jacobian row. Polynomial constant
  terms yield a degree-ten monic eliminant for the rational shift; integral
  closure makes all depressed coefficients polynomial, and every
  conserved-product branch then contradicts a nonzero constant Jacobian.
- AS109 CONSEQUENCE/SCOPE: no exact AS109 lift has both correction
  `y`-degrees at most four. A survivor needs `y`-degree at least five in one
  correction, with arbitrary `x`-degree and coefficient coupling still
  allowed. No quintic theorem, arbitrary-support no-go, lift, priority claim,
  or JC2 decision follows.

## TD6 TWO-CHART FIRST BAND AND NUMERICAL NEXT-ROW KILL (2026-08-24, DUAL-CONFIRMED FINITE TIER)

The first-band producer/review
`xmodel/td6-two-chart-first-band-20260824.md` /
`xmodel/td6-two-chart-first-band-review-grok-20260824.md` have SHA-256
`cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2` /
`265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25`.
The next-row producer/review
`xmodel/td6-two-chart-next-row-20260824.md` /
`xmodel/td6-two-chart-next-row-review-grok-20260824.md` have SHA-256
`32124d20ec84ef59d5b116639176b12053f5da6de1a9458dd4a2095d6b1618f0` /
`12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f`.
Both hostile reviews are **CONFIRMED**.

- FIRST BAND: one licensed SP-2/r9-M2 specialization uses common centering
  `(1,1,1)`, the selected F1 orbit polynomial, zero dead stretch, and
  `A=1/9` in the unchanged `(15,60)/(25,100)` rectangles. One shared global
  coefficient system has exact rank `3508/3602`, nullity 94. Its deterministic
  rational witness satisfies all stated transport rows, `[s^-2]J=0`, and
  `[r^0]J=1`; it fails the next rows and is not Keller.
- NEXT ROW: exact affine parameterization of the entire 94-space freezes
  `f1=-384t^14/25`,
  `g1=-128/125-(128/5)t^24`, and
  `[t^13]f2=66927/625`. Hence every point satisfies
  `[s^-1 t^13]J=-18858/3125`, an exact `Q-EMPTY` certificate. The apparent
  quadratic next band collapses to affine-linear; the pole row is unnecessary
  for the contradiction.
- SCOPE: the first band is nonempty and the next band empty only for these
  selected numerical moduli. SP-2 and all eight td6 terminal classes remain
  alive. The valid successor varies the licensed common centering, F1 orbits,
  dead stretch, and pole parameter while preserving their source-typed
  transport. Further bands at this dead numerical point add no information.

## AS109 QUINTIC-Y NO-GO (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/quintic-y-frontier-preflight-independent-20260824.md` (producer
SHA-256
`598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978`)
with `xmodel/quintic-y-review-grok-20260824.md` (review SHA-256
`ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e`):
**CONFIRMED**.

- FIELD THEOREM: every Keller pair over an arbitrary characteristic-zero
  field whose two coordinate `y`-degrees are at most five is a polynomial
  automorphism. The confirmed quartic theorem handles all lower patterns;
  the only new actual pairs are `(2,5)`, `(3,5)`, and `(4,5)`.
- NEW PAIRS: `(2,5)` has an uncancellable `3rho^5/8` finite-pole term and a
  final polynomial unit-product contradiction. `(3,5)` has a cubic first
  integral; finite-pole leading equations have subresultant 441, while every
  nonconstant polynomial point on the resulting singular Weierstrass cubic
  gives `R'Psi(R)` with `deg Psi=6` and nonzero leading coefficient.
  `(4,5)` has two polynomial first integrals; weighted `(2,3,4)` finite-pole
  equations have no point (resultant `-12180258816` on the nonzero branch),
  and every polynomial-infinity branch gives a nonzero term of degree
  `8q-1` in the constant Jacobian row.
- AS109 CONSEQUENCE/SCOPE: no exact AS109 lift has both correction
  `y`-degrees at most five. A surviving coupled section must allow
  `y`-degree at least six. Sextic pairs, arbitrary support, existence of a
  lift, priority, and JC2 remain open.

## AS109 GENERIC DEGREE, `A_infinity`, AND DECK-DESCENT REDUCTION (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

The producer/review pairs
`xmodel/as109-hensel-global-degree-cross-gate-20260824.md` /
`xmodel/as109-degree-cross-review-grok-20260824.md` have SHA-256
`7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133` /
`fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6`;
`xmodel/as109-ainfinity-deck-descent-gate-20260824.md` /
`xmodel/as109-ainfinity-review-grok-20260824.md` have SHA-256
`f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b` /
`a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76`.
Both hostile reviews are **CONFIRMED**.

- DEGREE/SPLIT: conditionally on an exact integral AS109 lift, with
  `M=Q_109(P,Q)`, `L=Q_109(x,y)`, and `d=[L:M]`, complete-ring parameter
  Hensel gives 109 distinct `M`-embeddings into the target-tube fraction
  field. Hence `d>=109` and
  `L tensor_M E = E^109 x A_infinity`, with
  `dim_E A_infinity=d-109`. After descent to a finitely generated coefficient
  field and abstract embedding in `C`, the **generic degree `d`** persists;
  the displayed 109-adic tube splitting is not transported to `C`.
- VALUED MEANING: after height-one localization/completion, the 109 integral
  roots are precisely the Hensel sheets; every other geometric root has a
  negative source valuation. Thus `dim A_infinity` is the exact sum of
  valued-initial multiplicities at negative extended weights, axes included.
  A fixed finite support admits a finite exact discriminator. Mixed volume or
  generic tropical intersection is not that discriminator.
- TWO MISSING KEYS: finiteness of the formal fibre algebra over the complete
  target ring would force `d=109` and `A_infinity=0`, but abstract etale and
  Zariski-Main data do not. A rational `L`-factor of the self-fibre algebra is
  exactly an element of `Aut_M(L)`, but a formal permutation of the 109 split
  factors does not descend. `A_infinity=0` together with a descended
  109-cycle would give a cyclic Galois degree-109 Keller extension and a
  contradiction; neither key is proved.
- CONTROLS/SCOPE: triangular non-Keller maps realize every `d>=109` and every
  residual rank while retaining the same local split, and can have trivial
  rational deck group. No degree congruence, `109|d`, properness, lift
  obstruction, or JC2 conclusion follows from local Hensel data alone.

## MOSKOWICZ PRIME-DEGREE PROOF IS UNSUPPORTED (2026-08-24, DUAL-CONFIRMED SOURCE-AUDIT TIER)

`xmodel/moskowicz-prime-degree-source-audit-20260824.md` (SHA-256
`929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210`)
with `xmodel/moskowicz-prime-degree-review-grok-20260824.md` (SHA-256
`a32082a89077b17bb9f9df4d2b518d8e7ad6de4e126a35cf0d49b446bb0d5a06`):
**CONFIRMED `REFUTED-AS-PROOF / HEADLINE NOT ESTABLISHED`**.

- The load-bearing first case of arXiv:2407.13795v1 attributes to a
  MathOverflow answer the implication that a stated rare-monomial property
  forces extension degree two. The answer proves no such universal
  implication. Exact Kummer controls
  `C(s^n,v) subset C(s,v)`, with `x=s+v`, `y=s+2v`, satisfy that property for
  every `n>=2`, so the printed inference is false.
- These controls are not Keller subfields. They refute the proof step, not
  the prime-degree statement itself, and produce no counterexample.
- The paper's second case is repairable: after choosing a nonzero generic
  linear parameter, Wang's intersection theorem and Gwozdziewicz's
  injectivity-on-one-line theorem show that a complex Keller map with
  `xy in C(P,Q)` is an automorphism. This repaired implication does not use
  prime degree. The paper cannot be consumed to exclude degree 109.

## AS109 `xy` MEMBERSHIP ROUTE STOPS (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

`xmodel/as109-xy-membership-gate-20260824.md` (SHA-256
`09d5654aeeeee55f9c5766e75f1a975db12a5701258efb25b04606fb4fc72729`)
with `xmodel/as109-xy-membership-review-grok-20260824.md` (SHA-256
`04c4d3dc8342141c4b1cb615e232a00053a056825fddbe55dd3ba5c2b44b8ac0`):
**CONFIRMED `SHARP NO-GO FOR MEMBERSHIP`**.

- On the tube `(P,Q)=(109S,1+109T)`, the Hensel sections satisfy
  `x_a y_a = a mod 109`; their 109 images are distinct. Therefore
  `[M(xy):M]>=109`, so `xy` lies in neither `M=Q_109(P,Q)` nor the target
  ring. Nonmembership survives coefficient-field extension to `C`, closing
  the proposed client of the repaired Moskowicz implication.
- If separately `A_infinity=0`, then `d=109`, `L=M(xy)`, and the tube-local
  monic minimal polynomial reduces to `Z^109-Z`. Its trace, norm, and
  discriminant are split-etale tautologies and yield no obstruction. This is
  not a global integral equation over `Q_109[P,Q]`.
- The univariate root-translation test is equivalent to supplying the missing
  descended deck action; it is not forced by symmetric coefficients. No lift
  is excluded or constructed.

## SEXTIC PARTIAL-`y` CLOSURE AND BOUNDED-SIX SYNTHESIS (2026-08-24, DUAL-CONFIRMED FIELD-THEOREM TIER)

The genuine sextic leaves and synthesis have the following producer/review
SHA-256 pairs:

- `(4,6)`: `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac` /
  `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c`;
- `(5,6)`: `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4` /
  `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70`;
- bounded-six synthesis: `1078bbdd47ccf085900b93b165ee268d314d2cc4e387b30ad81c4a40817e12f3` /
  `81669337bf038ae2bb2d81c20bec7ef92a97eaeaa03f906d0a20c33bf20a9115`.

All three hostile reviews are **CONFIRMED**. Over every characteristic-zero
field, every Keller pair whose two actual partial `y`-degrees are at most six
is a polynomial automorphism. The proof ledger closes `(4,6)` by its
imprimitive local-normalization branches and `(5,6)` by the third integral,
weighted common-factor identity, two polynomial boundaries, and infinity
contradiction; target reductions cover every other pair. Therefore an exact
AS109 lift has at least one correction of `y`-degree at least seven.

This entry promotes mathematical validity only. It makes no novelty claim:
the separate source-shear history audit may supply a shorter classical proof
and a stronger frontier. No arbitrary-support AS109 no-go, lift existence,
or JC2 inference follows.

## TD6 SYMBOLIC-MODULI THIRD-BAND CHAIN (2026-08-24, DUAL-CONFIRMED FINITE-FAMILY TIER)

The moduli-uniformity, paired-point, and moduli-uniform third-band
producer/review SHA-256 pairs are respectively:

- `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06` /
  `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b`;
- `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2` /
  `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7`;
- `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` /
  `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef`.

All three hostile reviews are **CONFIRMED**.

- UNIFORM NEXT ROW: on the retained x-boundary/F1 pattern,
  `[s^-1 t^13]J=(6/5)(5E2-2E1^2)`, independently of common centering and of
  pole/dead-stretch data absent from that coefficient. The real form is
  negative definite, but over `C` its zero curve carries a genuine
  56-dimensional paired finite-band survivor on the normalized slice.
- PAIRED POINT: the first explicit quadratic point on that curve dies at the
  next centered row, where the whole 56-family has
  `[s^0 t^0]J=81/15625`. This kills only that point.
- UNIFORM THIRD BAND: on the entire moduli curve, the constant centered row
  cuts to an irreducible sextic `F(S)`. Adjoining the cubic pole scale gives a
  degree-18 field; the remaining centered equations have homogeneous rank
  `25/58`, and an exact left syzygy has nonzero residual, including
  `(136875/29)A`, at all 18 conjugates. Hence the fixed normalized reduced-
  boundary family is empty at this band.
- SCOPE/NEXT: SP-2 and every terminal class remain alive because x-boundary,
  dead-stretch, centering, and other boundary moduli were fixed. The valid
  successor varies one such datum and tests its pairing with the existing
  left syzygy; another band on the empty family is invalid.

## PARTIAL-`y` SOURCE-SHEAR HISTORY STOP AND FIRST TRUE FRONTIER (2026-08-24, DUAL-CONFIRMED CLASSICAL-THEOREM TIER)

`xmodel/as109-partial-y-history-stop-20260824.md` (SHA-256
`6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe`)
with `xmodel/as109-partial-y-history-review-grok-20260824.md` (SHA-256
`f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd`):
**CONFIRMED `ALL MAXIMUM ACTUAL y-DEGREE <=8 IS CLASSICAL; FIRST
FUNDAMENTAL REMAINDER (6,9) WITH 3|H`**.

- SHEAR THEOREM: for actual degrees `m=da`, `n=db`, `gcd(a,b)=1`, the top
  Jacobian row gives `a_m=alpha h^a`, `b_n=beta h^b`. With `H=deg h` and a
  sufficiently large triangular source shear `y -> y+x^L`, the exact total
  degrees are `a(H+dL)`, `b(H+dL)` and their gcd is `H+dL`.
- CLEAN CLASSICAL INPUTS: if `gcd(H,d)=1`, Dirichlet makes this gcd prime and
  Nagata's repair of Appelgate--Onishi applies. If `gcd(H,d)=2`, it can be
  made `2p` and the independent Guccione--Guccione--Valqui theorem applies.
  Magnus is only the coprime-total-degree theorem; the gap in Zoladek's
  neighboring argument is not consumed. The field statement descends from
  `C` to every characteristic-zero field.
- COVERAGE/PRIORITY: every pair with partial gcd at most two is therefore
  classical. Equal-degree `GL_2` and divisible-degree target shears then cover
  all 81 ordered pairs with maximum actual `y`-degree at most eight. Hence
  the campaign's `(4,6)`, `(5,6)`, and bounded-six proofs remain correct
  alternate certificates but are not first exclusions. Consecutive-degree
  widening is stopped as duplicate history.
- FIRST REMAINDER: at maximum nine, the only fundamental residue is `(6,9)`
  with `3|H`; `(9,9)` is derivative through target reduction. The leading
  family `F=K^2`, `G=K^3`,
  `K=z^3+u t^2 z+v t^3`, has zero binary Jacobian and a positive-dimensional
  leading-boundary locus. It is not Keller; it proves only that the earlier
  coprime finite-map certificate does not transfer. The valid successor is a
  gauge-quotiented transverse deformation and cokernel test, not generic
  coefficient search.
- AS109 COROLLARY: conditionally on an exact lift, maximum actual `y`-degree
  at most eight is impossible by reviewed Hensel noninjectivity. Maximum
  exactly nine reduces, by an integral target operation and possible swap, to
  `(6,9)` with `3|H`. Its first non-top `y^13` row is automatically divisible
  by `109^2`; an exact primitive-core control rules out a universal first-row
  valuation contradiction. No lift, arbitrary-support no-go, or JC2 result
  follows.

## GCD3 `(6,9)` FIRST COMMON-CUBIC GATE (2026-08-24, DUAL-CONFIRMED STRUCTURAL TIER)

`xmodel/gcd3-69-common-cubic-first-gate-20260824.md` (SHA-256
`f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8`)
with `xmodel/gcd3-69-common-cubic-first-gate-review-grok-20260824.md`
(SHA-256
`5416440bc12bb50ecebfdfa520082aa9e88a26069b43deb13bdaabfcd1690503`):
**CONFIRMED `KUMMER SPLIT / FULL-CUBIC BOUNDARY TYPE-FAIL /
COMMON-CUBIC UNION UNIQUE DS / FIVE PLUS KAPPA`**.

- SOURCE NORMALIZATION: after `a_6=h^2,b_9=h^3` and `s^3=h`, the `y^13`
  row makes `delta=3A-2B` constant. A nontrivial cubic Kummer action forces
  `delta=0`; a cube core makes `h` a constant times a polynomial cube but
  leaves `delta!=0` live. The depression `z=sy+A/6` is over `k(x)(s)`, not a
  polynomial source automorphism, and its two boundary values are polynomial
  but need not vanish.
- BOUNDARY FIREWALL: a chosen boundary root licenses reduction only modulo
  its minimal polynomial. Reduction modulo the full depressed cubic requires
  an independently proved orbit of degree three; squarefreeness alone is
  insufficient. An exact split-root perturbation is a `TYPE-FAIL` of the
  stronger boundary inference, not of any conclusion derived from extra
  Jacobian rows.
- CONSTANT-W SCHEME: after solving the eight high binary rows, the residual
  radical has exactly the common-cubic surface and one order-three
  Davenport--Stothers curve. They meet set-theoretically only at the triple
  cubic; the original scheme is nonreduced along the common component. The
  DS identities, constant Wronskian `378*lambda^7`, and nonzero resultant are
  exact and independently reconstructed.
- SOURCE HIGH ROWS: in the aligned nontrivial-Kummer branch, all eight high
  source rows integrate exactly. Kummer weights and constant target gauges
  leave five moving coefficients plus one weight-zero `kappa` in that chosen
  target pin. The later dual-confirmed target-translation erratum shows that
  `kappa` itself is gauge and `kappa^2+mu` is invariant. A path persisting on
  the common component has
  `f=K^2,g=K^3+kappa*K` and zero source bracket. One associated-graded common
  point does not prove such persistence.
- CONDITIONAL DS STOP: only under pure DS entry, weighted Euler gives
  `(lambda^7)'=j/(81s)`. Exact finite/infinity valuations, the reviewed
  `3|deg(h)` residue, and both polynomial boundaries exclude that pure path.
  Entry from the full source system is not inferred.
- SCOPE/NEXT: this does not solve the four lower Pfaffian rows, terminal row,
  filtered boundary/component persistence, or cube mismatch, and does not
  exclude `(6,9)` or decide JC2. The licensed successor is precisely those
  lower rows in the target-pinned five-plus-`kappa` form, componentwise with
  the true minimal boundary factor, while `delta!=0` runs independently.

## AS109 WILD-SYMPLECTIC COMPLETED-BIDISC GATE (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

`xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256
`c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`)
with `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md`
(SHA-256
`a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a`):
**CONFIRMED `GAUGE-TRIVIAL / CONTROL-ONLY`**.

- COMPLETED TORSOR: conditionally on an exact integral lift of
  `(x-x^p,y)`, `Z_p<x,y>` is finite free etale of rank `p` over
  `Z_p<P,Q>`. The special Artin--Schreier translations lift uniquely to a
  free constant-`C_p` torsor action on the closed unit bidisc, and the chain
  rule makes every deck transformation determinant one.
- GAUGE TRANSITIVITY: any two determinant-one restricted-analytic lifts of
  the same special map are uniquely right-equivalent by a near-identity
  restricted-analytic symplectomorphism. Thus unrestricted completed
  cohomology has one gauge orbit. The statement does not provide a rational
  or polynomial deck map, act on `A_infinity`, or imply generic degree `p`.
- FIRST DIGIT: the exact norm, order, divergence, and invariance equations
  form one affine orbit under divergence-free right gauges. Nevertheless
  every solution has `[x^(p-1)y]Q1=1`; independent exact compilers at
  `p=3,5` give quotient dimension zero and recover the rational cotangent
  tower through depths two through four.
- SCOPE/NEXT: the forced monomial is a first-digit floor, not an unbounded
  support theorem, and the growing cotangent representative is not known to
  be minimal. A valid successor must define minimal support or degree inside
  the unique completed orbit with uniformly bounded polynomial gauges, or an
  algebraic boundary conductor invariant under a specified bounded
  equivalence. No `p=109` brute force, lift, fixed-support exclusion,
  `A_infinity` conclusion, or JC2 decision follows.

## AS109 BOUNDED POLAR CONDUCTOR (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

`xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256
`2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
with `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md`
(SHA-256
`bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`):
**CONFIRMED `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`**.

- EXTERIOR DIVISOR: for every odd prime `p`,
  `C_p=(x-x^p,y/(1-p*x^(p-1)))` is an integral restricted-analytic
  determinant-one lift. Over `Qpbar` its rational second coordinate has
  exactly `p-1` reduced affine vertical polar components, all at valuation
  `-1/(p-1)` and outside the closed unit bidisc. This divisor is neither the
  projective line at infinity nor the residual factor `A_infinity`.
- NO POLYNOMIAL CANCELLATION: for every polynomial Keller right map
  `phi=(X,Y)`, without assuming invertibility or JC,
  `gcd(1-p*X^(p-1),Y)=1`. Thus the rational pole cannot cancel. Under a
  polynomial symplectic automorphism the polar divisor pulls back
  isomorphically; under a merely Keller right map only noncancellation, not
  preservation of the component count, is claimed.
- CANONICAL CONDUCTOR: conditionally on a polynomial lift `F`, the reviewed
  completed-orbit theorem gives the unique identity-branch gauge in the
  orientation `C_p o Phi_F=F`. The maximum total degree `kappa_n(F)` of its
  canonical reduction modulo `p^n` tends to infinity. A uniform degree bound,
  or a uniform bound on the nested support cardinalities, would make
  `Phi_F` polynomial and contradict the no-cancellation lemma.
- FINITE CAPS: every fixed simultaneous map/gauge degree pair fails at some
  finite Witt depth by a finite-tree inverse-limit argument. At the first
  natural caps `D_F=D_phi=p`, depth two survives and depth three is empty for
  every odd prime. Exact independent controls give coefficient/augmented
  ranks `12/13` and `32/33` at `p=3,5`, with forbidden monomials `x^4y` and
  `x^8y`; additional `p=7,11` checks are controls only.
- SCOPE/NEXT: this does not exclude a polynomial lift or give a growth rate,
  identify `A_infinity`, descend a deck action, compute at `p=109`, or decide
  JC2. The licensed successors are a quantitative lower growth law for
  `kappa_n` or intrinsic-cap elimination, and an independently proved
  comparison with the valued initial systems governing `A_infinity`.

## TD6 SMALLEST Q-BOUNDARY DEFORMATION (2026-08-24, DUAL-CONFIRMED TWO-POINT TIER)

`xmodel/td6-boundary-q2-deformation-gate-20260824.md` (SHA-256
`f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0`)
with `xmodel/td6-boundary-q2-deformation-review-grok-20260824.md` (SHA-256
`6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c`):
**CONFIRMED `TWO-EXACT-EMPTY-SPECIALIZATIONS / STOP`**.

- SOURCE/SCOPE: inside the already-cut normalized SP-2 chart-pattern
  control, retain the fixed rectangles, center, zero dead stretch, reduced
  F1 pattern, r9 relation, sextic, and degree-18 pole field, and deform only
  `p=t^15`, `q_B=t+B*t^2+t^25`. This is the smallest displayed q-jet, not a
  complete SP-2 boundary normal form.
- `B=1`: the exact chain has ranks `3508/3602`, then `36/94`, then tangent
  rank `25/58`, and is empty at the centered input row `t^4`. Its residue
  differs from the frozen `B=0` residue by exactly `-14012/145`, so the
  obstruction is genuinely `B`-sensitive rather than copied unchanged.
- ADAPTIVE POINT: at the exact secant-cancellation candidate
  `B_*=rho_0/(14012/145)` in the degree-18 field, the full `B`-dependent
  rebuild has ranks `3470/3602 -> 132`, `+38 -> 94`, `+38 -> 56`, tangent
  rank `25/56`, and is again empty at `t^4`. The residual has nonzero
  `1,A,A^2` components, directly refuting affine secant extrapolation.
- SCOPE/NEXT: neither generic `B` nor the one-parameter family is killed;
  other q-jets, centering, dead stretch, F1 data, SP-2, all terminal classes,
  and JC2 remain open. The licensed successor is symbolic fraction-free
  elimination over `E[B]` plus separate treatment of every pivot/rank-jump
  locus. Sampling or an adjoint shortcut alone is not a certificate.

## GCD3 `(6,9)` ALIGNED LOWER-PFAFFIAN SUCCESSOR (2026-08-24, DUAL-CONFIRMED BRANCH-EXCLUSION TIER)

`xmodel/gcd3-69-lower-pfaffian-successor-20260824.md` (SHA-256
`7671785519bf4e55b602f117740bd8d8571c6982a8916235407a2bb0a2263043`)
with `xmodel/gcd3-69-lower-pfaffian-successor-review-grok-20260824.md`
(SHA-256
`a000619d8b5597add21716d525856c459ff57d5a2b2ab75b85de5d9d08970b27`):
**CONFIRMED `ALIGNED NONTRIVIAL-KUMMER BRANCH EMPTY`**.

- LOWER EXACTNESS: after the independently reconstructed eight high rows,
  the four zero lower one-forms have potentials
  `alpha4=dI4`, `alpha3=dI3`,
  `alpha2-(a4/2)alpha4=dI2`, and
  `alpha1-(a3/3)alpha4-(a4/3)alpha3=dI1`. Kummer weights force
  `I4=I3=I1=0` and leave `I2=mu`.
- INVARIANT FIBRE: independent Singular decompositions in a different
  monomial order, using both GTZ and SY algorithms, give exactly two reduced
  sheets (plus one embedded prime contained in the zero-bracket sheet).
  On `P_A`, `f=K^2+d` and
  `g=K^3+(kappa+3d/2)K`, so the source bracket vanishes identically.
- ELLIPTIC SHEET: `P_B` is `Y^2=3X^3+4096C`. Its terminal one-form pulls
  back to `(7Y^2-12288C)dY/(147456X)`. For `C!=0`, exact finite-place
  valuations force an impossible negative valuation of the polynomial core.
  At `C=0`, the sheet is either zero bracket or the shifted
  Davenport--Stothers path; the reviewed terminal ODE and every boundary
  case force the nontrivial Kummer core to be a cube.
- REPLAY/TRUST: the registered Python replay inserted rather than re-integrated
  the high-row `b`-polynomials. The reviewer independently performed the
  sequential integration, rebuilt the potentials and decomposition, and
  rederived both determinants and the full valuation lattice. The shortcut
  is therefore a coverage note, not evidence for the verdict.
- SCOPE/NEXT: this excludes only the aligned nontrivial-cubic-Kummer branch.
  It does not close the aligned cube core with extra constants, `delta!=0`,
  the independent cube-mismatch branch, all of `(6,9)`, or JC2.

## GCD3 TARGET-TRANSLATION ERRATUM (2026-08-24, DUAL-CONFIRMED SCOPED CORRECTION)

`xmodel/gcd3-69-target-translation-erratum-20260824.md` (SHA-256
`43fa36968bb90414748330c1b4a5d5169a0eaa21b1925623764e96204e049c78`)
with `xmodel/gcd3-69-target-translation-erratum-review-grok-20260824.md`
(SHA-256
`f4cb57ca765138ed2decab01b12a7f884c37f9a847d80e90162ee751bb3df837`):
**CONFIRMED `KAPPA GAUGE / NO MATHEMATICAL EXCLUSION CHANGES`**.

- LEGAL ACTION: the target translation `(f,g) -> (f+q,g)` preserves all
  degree pins and sends `a0 -> a0+q`, `kappa -> kappa-3q/2`. Thus
  `q=2kappa/3` gauges `kappa` to zero. The first-gate and successor phrases
  “essential `kappa`” and “five plus essential `kappa`” were wrong or
  pin-dependent.
- TRUE INVARIANTS: `I4,I3,I1` are unchanged,
  `mu -> mu+3kappa q-9q^2/4`, and `C=kappa^2+mu` is invariant. So are the
  elliptic coordinates `X,Y`, the curve, and its terminal form. On the
  zero-bracket sheet, `d -> d+q` while `kappa+3d/2` is invariant.
- EFFECT: no high-row identity, lower potential, primary component,
  determinant, terminal ODE, valuation argument, or aligned-branch exclusion
  fails. The clean canonical parameter is `C`, not `kappa`. Cube mismatch,
  arbitrary `(6,9)`, and JC2 remain open.

## GCD3 `(6,9)` CUBE-MISMATCH LAURENT GATE (2026-08-24, DUAL-CONFIRMED REDUCTION TIER)

`xmodel/gcd3-69-cube-mismatch-gate-20260824.md` (SHA-256
`6a2799dfe46828c70462d51a842a3fc0adf0515b8ded7a576cdb837d81847d20`)
with `xmodel/gcd3-69-cube-mismatch-review-grok-20260824.md` (SHA-256
`2648eef3b8091970655a94743c6c181343a94534b6454f43c579b310331ba7d7`):
**CONFIRMED `FABER--LAURENT REDUCTION / FINITE-POLE DICHOTOMY`**.

- FULL HIGH-ROW FORM: in the polynomial cube core, set `w=f^(1/6)` and
  `g=[H(w)]_+` with
  `H=T^9+dT^8+sum(c_j T^j)`. All nine integration constants are retained.
  Target gauges remove `c6,c0`; for `d!=0`, convenient residual invariants
  are `mu=8dc3-9c2` and `nu=8dc1-7c7c2`. The `d=0` quotient is separate.
- LOWER TRIANGLE: if `H(w)-g=sum(r_n w^-n)`, exact Laurent extraction gives
  a triangular five-row system of determinant `6^5`, equivalent to
  `r1'=r2'=r3'=r4'=0` and `6r5'=j/s`. An independent finite-binomial Faber
  reconstruction and reverse integration order recovered every identity.
- RATIONAL POLES: if nonconstant polynomial `s` admits the required rational
  primitive, it must be `C0(x-a)^m`, `m>=2`; constant `s` is the other case.
  Simple roots, more than one distinct root, degree one, and logarithmic
  primitives are impossible. This constrains trajectories but does not itself
  control all coefficient-boundary poles.
- CONTROLS/SCOPE: the regular local formal survivor is genuine. The tested
  ordinary square/double `d`-arcs fail, a Davenport--Stothers tangent survives
  first order, and the triple point is exceptional. Neither `d!=0`, `d=0`,
  ramified/Puiseux common landings, an actual `(6,9)` Keller pair, nor JC2 is
  excluded. The licensed successor is exact global rational/Puiseux
  trajectory classification followed by reconstruction in the original rows.

## AS ALGEBRAIC-GAUGE GROWTH AT `p=3`, DEPTH FOUR (2026-08-24, DUAL-CONFIRMED FINITE-TABLE TIER)

`xmodel/as-gauge-growth-p3-depth4-gate-20260824.md` (SHA-256
`bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660`)
with `xmodel/as-gauge-growth-p3-depth4-review-grok-20260824.md` (SHA-256
`fecc4e758727b540cef9951ca59162f77cb2d8ff5876132e72f6175350891919`):
**CONFIRMED `MINIMUM EQUAL CAPS 3,5,7 THROUGH DEPTH FOUR`**.

- EXACT TABLE: on the identity branch at `p=3`, total-degree equal caps have
  minima `n2=3`, `n3=5`, `n4=7`. At depth three, caps three and four have
  rank/augmented-rank `15/16` and `21/22`; cap five has positive cotangent.
  At depth four, caps five and six are empty, including a unit certificate
  over `F_3`; cap seven has positive cotangent.
- INDEPENDENCE: the reviewer rebuilt the commuting-variable mod-81
  expansions, all integer carries, and the generic-simplex matrices with a
  second sparse engine and reversed column order. A wording correction does
  not change the certificate: `a_[x3]=0` follows from the degree cap, while
  `b_[x^2y]=0` follows from divergence; the displayed integer combination
  reduces to the claimed unit over `F_3`.
- SCOPE/NEXT: the values agree with `(n-1)(p-1)+1` for these three depths but
  do not prove the law, any `n>=5` statement, a lift or no-lift theorem,
  `p=109`, `A_infinity`, or JC2. Depth five, cap eight versus the cap-nine
  positive control, is the next exact discriminator.

## TD6 JET-ORBIT ADJOINT GATE (2026-08-24, DUAL-CONFIRMED TRANSVERSALITY TIER)

`xmodel/td6-jet-orbit-adjoint-gate-20260824.md` (SHA-256
`28a8869cf91f5e7d1e3601c52ee21742eca9187e57d7ac1065f22bcbd0ee402b`)
with `xmodel/td6-jet-orbit-adjoint-review-grok-20260824.md` (SHA-256
`2cd542615dfcc7b15dab3796adba0c91b84dcba606da6ff442b3d69dd4fb79f9`):
**CONFIRMED `Q2 TRANSVERSE / NONZERO FIRST DERIVATIVE / POLYNOMIAL
SUCCESSOR LICENSED`**.

- ORBIT QUOTIENT: the full infinitesimal reparametrization
  `t -> t+epsilon*t^2` moves chart, `p`, and `q` by
  `(t^2,15t^16,t^2+25t^26)`. In the fixed linear-chart section, adjoining
  the q2-only vector raises the source-orbit rank from seven to eight, so q2
  is the sole smallest transverse boundary slot there. Four target gauges
  have zero Jacobian sensitivity, and `(S,D,L,A)` is rigid of rank `4/4`.
- ADJOINT IDENTITY: exact dual-number elimination has ranks
  `3470 -> 132`, `38 -> 94`, `38 -> 56`, and current homogeneous rank
  `25/56`, with no first-order rank flag. Differentiating the normalized left
  syzygy gives
  `c'(0)=lambda0^T b'(0)+lambda'(0)^T b0=-4720/29`. The frozen-left-kernel
  shortcut is false (`lambda'` has support three), and the old secant
  `-14012/145` is not the derivative.
- INDEPENDENCE: the reviewer wrote separate two-form compilers, dual-number
  arithmetic, and Dual Gaussian elimination, reproduced the ranks, residue,
  derivative, syzygy digest, orbit/gauge controls, and the counterexample to
  freezing `lambda`. Both registered replays also matched byte-for-byte.
- SCOPE/NEXT: a nonzero derivative at an already inconsistent point proves
  only that the obstruction moves. It licenses exact elimination over
  `E[B]` with printed degree bounds and every exceptional rank stratum; it
  does not kill the `B`-family, centering, dead stretch, SP-2, a terminal
  class, or JC2.

## TD6 LICENSED Q2 PENCIL EMPTY (2026-08-24, DUAL-CONFIRMED FAMILY TIER)

`xmodel/td6-boundary-qb-pencil-gate-20260824.md` (SHA-256
`5e1f6b44e143360a41550ae552b20bef02325414f96c5fd469ba4d016eb5eb22`)
with `xmodel/td6-boundary-qb-pencil-review-grok-20260824.md` (SHA-256
`5c238f2bd3cf11422093184e1563f7671d0abd4b8f06a6fb5dfd7d380ac51319`):
**CONFIRMED `TD6-QB-LICENSED-FAMILY-EMPTY / EXACT-E[B]-BEZOUT / NOT-SP2`**.

- EXACT FAMILY: at every point of the frozen degree-18 sextic field, the
  normalized family `p=t^15`, `q_B=t+B*t^2+t^25` has no solution for any
  `B`, even after extending the residue field. Exact staged elimination over
  untruncated `E[B]` has ranks
  `3470/3602 -> 38/132 -> 38/94 -> 25/56`.
- NO HIDDEN STRATUM: all 101 normalized leads are nonzero elements of `E`
  independent of `B`; the pivot exceptional product is therefore one. The
  reviewer reconstructed every consumed section from the raw 3,602-column
  transport matrix and independently obtained zero homogeneous remainders.
- COMPATIBILITY IDEAL: ten exact current-band left-null conditions were
  recomputed against the original rows. In particular,
  `N4=rho-(4720/29)B+(11364/145)B^2-(4096/145)B^3+16B^4` and
  `N13=((252-342S+144S^2-36S^3)/25)B`. The displayed coefficient and `rho`
  are units; an independently checked Bezout identity gives
  `gcd(N4,N13)=1` over `E[B]` and after field extension.
- SCOPE/NEXT: this kills exactly one licensed one-parameter q2 deformation in
  the fixed normalized section. It does not cover common centering, dead
  stretch, other boundary jets, SP-2, landing, any terminal class, or JC2.
  The smallest matrix-changing successor is common centering.

## AS `p=3` DEPTH-FIVE MINIMUM SEVEN (2026-08-24, DUAL-CONFIRMED FINITE-TABLE TIER)

`xmodel/as-gauge-growth-p3-depth5-d7-minimum-20260824.md` (SHA-256
`618a954ea683fd8444dafc4511c9aed708ea88459c524d747b815d48c6618f65`)
with `xmodel/as-gauge-growth-p3-depth5-d7-minimum-review-grok-20260824.md`
(SHA-256
`7006d82c4f6ff9943433bb4447bb95d3f94d6a76ea28ba1088bcc9aac774621f`):
**CONFIRMED `D_MIN(3,5)=7 / PROPOSED LINEAR CAP LAW FALSE`**.

- EXACT MINIMUM: the frozen total-degree-simplex system
  `B_(3,5)(7,7)` has an explicit point modulo 243. Independent sparse,
  dense, SymPy, and Singular expansions reproduce both bounded gauge and map,
  `C_3 o (A,B)=(P,Q)`, and both determinant-one identities. Reduction modulo
  81 maps every depth-five cap-`D` point to the reviewed depth-four system,
  which is empty for `D<=6`; hence the minimum is exactly seven.
- LAW FALSIFIED: the reviewed minima through depths two through five are
  `3,5,7,7`, not the proposed `(n-1)(p-1)+1`, whose depth-five value is nine.
  The separately reviewed cap-eight producer (report/review SHAs
  `3cca09d0c31b46ed12b8510e0d343fd097b2727e2b8ff3aef464c334d48dba6f` /
  `2c3f961a5f0e537abef82db9243723289864d3ae901179adedaa554617d975c7`)
  remains a correct but nonminimal cancellation motif.
- SCOPE/NEXT: this is a minimum for a simultaneous map-and-canonical-gauge
  cap at one prime and depth. It neither gives a compatible tower nor
  excludes a bounded-degree map whose gauge grows. No polynomial/Tate lift,
  `p=109`, `A_infinity`, deck-descent, or JC2 conclusion follows.

## AS DEPTH-SIX CARTIER STOP FOR ONE D7 RESIDUE (2026-08-24, DUAL-CONFIRMED POINTWISE TIER)

`xmodel/as-gauge-growth-p3-depth6-cartier-d7-point-20260824.md` (SHA-256
`9bff27d0aed6294633c7e5726a7d1c0d7e0fb8a5629809790da783c62b41fea4`)
with `xmodel/as-gauge-growth-p3-depth6-cartier-d7-point-review-grok-20260824.md`
(SHA-256
`99f703a8c97afde81ff41065c1f69e34b7739d321f2020ce54949ea144adf567`):
**CONFIRMED `FROZEN D7 RESIDUE CARTIER-TERMINAL AT DEPTH SIX / NOT SYSTEM EMPTY`**.

- EXACT CLASS: for the frozen depth-five minimum witness,
  `R=(det J(A,B)-1)/243 mod 3` has `[x^2*y^2]R=-1`. Independent integer,
  characteristic-zero, mod-3, SymPy, and Singular computations reproduce the
  representative and residual.
- INVARIANCE: every next digit `A+243U,B+243V` changes the residual by
  `U_x+V_y`. In characteristic three the `x^2*y^2` coefficient of both terms
  is zero, so no polynomial `U,V` of any degree changes this Cartier class.
  The obstruction is invariant under changing integer representatives of the
  same residue modulo 243.
- SCOPE/NEXT: this one residue class has no determinant-one gauge lift modulo
  729 at any cap. It does not empty `B_(3,6)(7,7)` or any fixed-map-degree
  system: other depth-five residues may have zero Cartier class. The honest
  successor is the full depth-five locus intersected with all Cartier and
  depth-six support rows, or the direct fixed-map-degree tower with no gauge
  cap. No all-depth, lift, `A_infinity`, deck-descent, or JC2 result follows.

## GCD3 `(6,9)` CUBE-TRAJECTORY CLOSURE (2026-08-24, DUAL-CONFIRMED BRANCH-EXCLUSION TIER)

`xmodel/gcd3-69-cube-trajectory-kuranishi-20260824.md` (SHA-256
`069f6280332b44d93dcad17801dc7136d4a79fb06ace101c2dce8a4e746b5e7b`)
with `xmodel/gcd3-69-cube-trajectory-kuranishi-review-grok-20260824.md`
(SHA-256
`7bcf18d69344acc2277a0184ca1aeeb717ebad35c3aacf91421874b7e59f5cc9`):
**CONFIRMED `POLYNOMIAL-CUBE TRAJECTORY EMPTY AFTER THE REVIEWED
FABER--LAURENT LANDING`**.

- COVERAGE: after `h=s^3`, `s in k[x]`, the reviewed landing gives
  `r1'=...=r4'=0`, `6*r5'=j/s` and forces nonconstant rational `s` to one
  repeated-root power. The closure treats constant and nonconstant `s`,
  `d!=0` and `d=0`, every legal Faber constant, all rank-zero/crossing
  strata, and both original polynomial boundary jets. It imports no
  nontrivial-Kummer weight vanishing.
- DECISIVE GEOMETRY: distinct first-load weights close the ordinary orbit
  and boundary strata. The formerly dangerous mixed `rho3,rho4` fibre is a
  smooth genus-one curve when `mu!=0`; when `mu=0`, its rational cusp has two
  pole places, incompatible with the one-pole terminal forms. The remaining
  zero-bracket, double-root, triple-point, and shifted Davenport--Stothers
  strata are excluded by exact bracket, valuation, boundary-resultant, or
  projective arguments.
- SCOPE: this closes exactly the polynomial-cube branch after the frozen
  landing. It does not alone establish the cube/noncube partition handoffs,
  degree recursion, a maximum-twelve theorem, or JC2.

## GCD3 `(6,9)` COVERAGE COMPOSITION AND MAXIMUM-ELEVEN THEOREM (2026-08-24, DIFFERENT-MODEL-CONFIRMED THEOREM TIER)

`xmodel/gcd3-69-coverage-composition-20260824.md` (SHA-256
`7eda0a469585247479d46c8f5f2ce95d2643ae8541f0d7f9c80e1c8537fffb0c`)
with `xmodel/gcd3-69-coverage-composition-review-claude-20260824.md`
(SHA-256
`d9522acbb35c5097cb3d3c947be12c10868f109af4d30c9713870f5ec6e9a33f`):
**CONFIRMED `NO (6,9),3|H / EVERY MAXIMUM ACTUAL y-DEGREE <=11
KELLER PAIR IS AN AUTOMORPHISM`**.

- `(6,9)` EXHAUSTION: after scalar extension, the primitive leading core is
  either a noncube in `k(x)` or a polynomial cube. The noncube branch derives
  `delta=0` by Kummer weight and lands exactly in the reviewed aligned
  lower-Pfaffian exclusion. The cube branch retains every weight-unforced
  constant and lands exactly in the reviewed Faber--Laurent/trajectory
  exclusion. The dichotomy is disjoint and exhaustive, including constant
  cores, repeated factors, and mixed cube factors. Thus no characteristic-
  zero Keller pair has actual partial `y`-degrees `{6,9}` with `3|H`.
- DEGREE THEOREM: source shear plus the repaired prime-gcd and independent
  `2p` theorems close `gcd(H,d)<=2`; equal/divisible target reductions recurse
  with strict measure decrease. Independent enumeration checks all 78
  unordered and 144 ordered pairs through maximum eleven. Hence over every
  characteristic-zero field, every Keller pair with
  `max(deg_y(P),deg_y(Q))<=11` is a polynomial automorphism. Descent uses the
  unique inverse/faithful flatness.
- FRONTIER/PROCESS: at maximum twelve the first new primitive pairs are
  exactly `(8,12)` and `(9,12)`; this is a checksum, not their exclusion.
  Claude independently hand-derived every load-bearing identity and hand-
  traced the frozen replay, but its adapter exposed no shell. The coordinator
  separately ran the registered SHA-256 check and replay successfully on the
  frozen bytes, including terminal payload
  `d7e030685c84e7c7366524e4b28f8516a5bf9d5060c3ebdba3990ca2e243ecd4`.
- SCOPE: this is an unbounded-`x` partial-`y` theorem. It is not a new
  total-degree result, a maximum-twelve theorem, arbitrary-support JC2, or a
  counterexample. A targeted web/primary-source sweep found no public
  duplicate, but that is not a novelty or priority proof.

## AS MAP-ONLY `p=3,D=7` TRIANGULAR TERMINAL POINT (2026-08-24, DUAL-CONFIRMED POINTWISE TIER)

`xmodel/as-fonly-p3-d7-depth6-triangular-terminal-20260824.md` (SHA-256
`5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb`)
with `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-review-grok-20260824.md`
(SHA-256
`75ff0c8588c633fcf53e17104bf77cdc74fba30bc9c02aa776b23ad0baaa2318`):
**CONFIRMED `ONE MAP-ONLY D7 RESIDUE SURVIVES MODULO 3^6 AND IS
CAP-TERMINAL MODULO 3^7`**.

- EXACT POINT:
  `P=x+2*x^3+441*x^5+108*x^7` and
  `Q=y-6*x^2*y+18*x^4*y-27*x^6*y` have determinant one modulo `729`.
  The congruent clean lift with `x^7` coefficient `1566` has determinant
  `1-729*x^12` modulo `2187`.
- TERMINALITY: a next map digit at cap seven changes the residual only by a
  divergence of degree at most six and therefore cannot cancel `x^12`.
  The literal representative's quotient is `x^6-x^12` modulo three; the
  `x^6` term is divergence-removable. The reviewer independently rebuilt the
  integer determinant, exhaustive accepted-digit enumeration, clean lift,
  and terminal degree bound.
- SCOPE: this refutes emptiness of the map-only `D=7` system through depth
  six and supplies a terminal positive control. It neither empties the full
  next-depth locus nor supplies a compatible all-depth tower, polynomial
  characteristic-zero lift, counterexample, or JC2 result.

## AS MAP-ONLY BALANCED CYCLOTOMIC TERMINAL FAMILY (2026-08-24, DUAL-CONFIRMED INFINITE FINITE-DEPTH TIER)

`xmodel/as-fonly-p3-balanced-cyclotomic-terminal-family-20260824.md`
(SHA-256
`8d6873550d06136f3a725160161500a844b43c9793a90c59798e5dc2b3c4c8e4`)
with
`xmodel/as-fonly-p3-balanced-cyclotomic-terminal-family-review-grok-20260824.md`
(SHA-256
`d4803d27735b815cfb0ef3c8120def1a935912ef9427acb0c9b05d00d3d4b1dd`):
**CONFIRMED `FOR EVERY ODD m>=3, ONE D=2m+1 AS RESIDUE SURVIVES
THROUGH DEPTH 2m AND IS SAME-CAP TERMINAL AT DEPTH 2m+1`**.

- IDENTITY/INTEGRALITY: with
  `A_m=(1+z)*(1+...+z^(m-1))` and `B_m=A_m(-z)`, oddness gives
  `A_m*B_m=1-z^(2m)`. Setting `z=3*x^2`, taking `P_m' = A_m(z)` with zero
  constant and `Q_m=y*B_m(z)` gives coefficients in `Z_(3)`, exact total
  degree `D=2m+1`, special fibre `(x-x^3,y)`, and the exact identity
  `det J(P_m,Q_m)=1-3^(2m)*x^(4m)` over `Q_3[x]`.
- SURVIVAL/TERMINALITY: the map survives modulo `3^(2m)`. At the next digit
  the residual is `-x^(4m)+U_x+V_y` modulo three. At the family cap,
  `deg(U_x+V_y)<=2m`, so the displayed residue has no lift. The same degree
  comparison gives the pointwise corollary that it remains terminal for
  every cap `D'<=4m`; the first divergence cap that can see the monomial is
  `4m+1`.
- CONTROLS/SCOPE: `m=3` recovers the separately reviewed `D=7` point;
  `m=5` gives a complete `D=11` residue through depth ten. Even `m` fails the
  cyclotomic identity, with smallest failure `m=2`. This is an arbitrarily
  deep compiler regression family of different finite degrees, not a
  compatible tower at fixed degree, full-locus classification, uniform death
  bound for other residues, characteristic-zero lift/no-lift, counterexample,
  or JC2 inference.

## AS MAP-ONLY `p=3,D=7` ASSOCIATED TOP COMPONENTS (2026-08-24, DUAL-CONFIRMED NONREDUCED-CHECKPOINT TIER)

`xmodel/as-fonly-p3-d7-associated-top-components-20260824.md` (SHA-256
`e50297762088b17e3a01d98e4a76823ec6f33abe02df8b05f50486a3224c30a3`)
with
`xmodel/as-fonly-p3-d7-associated-top-components-review-grok-20260824.md`
(SHA-256
`7593a9a822c07a3d5daf67b30c46028f0ba84b7978c038d7ec1bc6af62168f8a`):
**CONFIRMED `THE FIRST-DIGIT CARRY ROWS OF DEGREES 12 AND 11 HAVE
THREE REDUCED LAYER-7/6 COMPONENTS AND ONE LOAD-BEARING EMBEDDED PRIMARY
COMPONENT`**.

- SOURCE/ROWS: for `P=x-x^3+3U`, `Q=y+3V`, the exact integer identity is
  `det J=1+3*(U_x+V_y-x^2)+9*K` with
  `K=(U_x-x^2)*V_y-U_y*V_x`. The checkpoint includes homogeneous divergence
  degrees six/five and carry degrees twelve/eleven. The fixed term
  `-x^2*V_y` has degree at most eight and cannot enter those carry rows.
- TOP LAYER: the 16-variable/20-row degree-seven ideal has dimension four,
  exactly two dimension-four minimal primes, and two primary components. One
  is a nonprime thickening; the original ideal is nonradical, with no embedded
  prime at this one-layer stage.
- LAYERS 7/6: attaching all degree-six coefficients and degree-eleven carry
  gives 30 variables/38 rows, dimension ten, and three minimal primes of
  dimensions `10,10,8`. Complete primary decomposition has a fourth,
  dimension-six embedded component supported on zero degree-seven layer plus
  the eight derivative-visible degree-six zeros. The six Frobenius degree-six
  coefficients remain free on the two dimension-ten branches. The triangular
  control projects to the origin on every associated-prime support.
- SCOPE/NEXT: the nonreduced structure is load-bearing for accepted-digit and
  Fitting recursion and must not be replaced by its radical. Carry degrees
  ten through seven, the divided integer carry/Cartier row, accepted second
  digits, the full `D=7` locus, all-depth lifting, characteristic zero, and
  JC2 remain open. The smallest honest successor attaches degree ten
  componentwise while preserving all primary structure.

## MAXIMUM-12 SHARED FABER HIGH-ROW LANDING (2026-08-24, DIFFERENT-MODEL-CONFIRMED EXACT TIER)

`xmodel/max12-partial-y-shared-faber-probe-20260824.md` (SHA-256
`d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036`)
with
`xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md`
(SHA-256
`e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c`):
**CONFIRMED `COMPLETE UNIVERSAL HIGH-ROW FABER INTEGRATION / EXACT
MAXIMUM-12 ROUTE WIDTHS / LOWER FIBRES OPEN`**.

- UNIVERSAL LANDING: for monic depressed `f,g` of degrees `(m,n)` over a
  characteristic-zero differential field, put `w=f^(1/m)` and
  `F_j=[w^j]_+`.  If `deg_z(f_x*g_z-f_z*g_x)<=m-2`, unitriangularity and the
  fixed-`w` identity force the unique expansion `g=sum h_j F_j` to have every
  `h_j` differential-constant.  With
  `H(w)-g(z(w))=sum r_l w^-l`, the remaining system is exactly
  `r1'=...=r_(m-2)'=0`, `m*r_(m-1)'=j/u`; the terminal sign is positive and
  the triangular determinant is `m^(m-1)`.
- EXACT CELLS: an independent Newton/product engine reconstructed all eleven
  high rows in `(8,12)` and `(9,12)`, both first integrated rows, every
  per-branch `r1,r2` digest, and the three legal target gauges.  High-row
  quotient widths are `7,10,16` on Kummer orders `4,2,1` and `9,17` on orders
  `3,1`; two-row local controls are `5,8,14` and `7,15`.
- ALLOCATION/SCOPE: aggregate mandatory-route widths `33` versus `26` (or
  local controls `27` versus `22`) license allocating `(9,12)` next.  The
  widest single branch and raw gate can favor `(8,12)`, so no global
  simpler-cell theorem is claimed.  Neither lower invariant fibre nor either
  Taylor-boundary family is classified; neither frontier is empty, and no
  maximum-twelve, counterexample, or JC2 conclusion follows.

## MAXIMUM-12 KUMMER PREFLIGHT (2026-08-24, DIFFERENT-MODEL-CONFIRMED EXACT TIER)

`xmodel/max12-partial-y-kummer-preflight-20260824.md` (SHA-256
`30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07`)
with
`xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md`
(SHA-256
`2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe`):
**CONFIRMED `EXACT MAXIMUM-12 ROUTING / KUMMER ORDERS / BOUNDARY
PROVENANCE / CONDITIONAL BINARY GATE`**.

- ROUTING: the only primitive maximum-12 cells are `(8,12)` and `(9,12)`.
  Their unresolved history classes are `4|H` and `3|H`; the latter is exact
  classwise.  At pair level its `H=0`, coefficient-`x`-degree-at-most-one
  corner is already closed by the frozen `L=2` shear to total gcd six.
- KUMMER ROW: for `(m,n)=(dr,ds)`, the next row is exactly
  `d*u^(d*(r+s)-1)*(s*A-r*B)'`; depression gives
  `delta=s*A-r*B` and mismatch `-delta/r`.  On the **monic-core divisor
  class order**, every nontrivial Kummer branch forces `delta=0`.  This
  includes the genuine order-two leaf inside `(8,12)`; the remaining orders
  are `4,2,1` and `3,1`.
- BOUNDARY/GATE: both complete original Taylor-jet families remain charged.
  The conditional binary Wronskian has common-power locus `(K^r,K^s)` and
  tangent ranks 11 in both cells, kernels 7 and 8.  This is local linear
  degeneracy, not a global component theorem.
- CUSTODY/SCOPE: the coordinator reran all four frozen hash checks and
  reproduced payload SHA-256
  `eb1e72d69193cded40438981907f62972725945c39a18e34891dd8f5b3645bf1`.
  No lower fibre, Taylor family, maximum-twelve cell, counterexample, or JC2
  conclusion follows.

## AS `p=3,D=7` DIVIDED-CARRY ERRATUM (2026-08-24, DIFFERENT-MODEL-CONFIRMED CORRECTION TIER)

`xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md`
(SHA-256
`cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194`)
with
`xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-review-grok-20260824.md`
(SHA-256
`4e915fb6f7e8701d1932b2b28df76db35859520bc94ffe8fb08a1cd679936ae8`):
**CONFIRMED `THE QUADRATIC BRACKET CARTIER SLOT VANISHES, BUT THE FULL
SOURCE-HONEST RESIDUAL HAS ONE ADDITIONAL DIVIDED-LINEAR ROW`**.

- EXACT QUOTIENT: with `L=U_x+V_y-x^2` and
  `K=(U_x-x^2)*V_y-U_y*V_x`, first-digit admissibility makes `L/3`
  integral and the next residual is
  `L/3+K+C_x+D_y` modulo three.  The basic Cartier coefficient of `K`
  vanishes universally, while that of `L/3` is `u5_3+v5_2`.
- CORRECTED SCHEME: on the named deep branch the source-honest ideal has 40
  variables and 30 rows, reduced-Groebner size 269 in the registered order,
  dimension 18, radical size 44, and is nonradical.  Its exact localization
  cover is `I=Q0 intersect Q1 intersect E`; the pieces are navigation aids,
  not primary or minimal-component assertions, and none replaces `I`.
- QUARANTINE: the predecessor's 29-row completeness, dimension 19, and
  two-piece cover are retracted.  The old bytes remain preserved as a
  negative control.  The already reviewed degree-12/11 associated-top rows
  are unaffected because the divided-linear quotient has too low a degree.
- CUSTODY/SCOPE: all registered producer, cover, radical, integer-identity,
  and manifest replays pass on the coordinator host.  No accepted second
  digit, full `D=7` locus, all-depth lift/no-lift, characteristic-zero map,
  counterexample, or JC2 conclusion follows.

## PINCHUK QUASI-POLYNOMIAL SOURCE AUDIT (2026-08-24, PRIMARY-SOURCE GAP/CORRECTION TIER)

`xmodel/pinchuk-quasipolynomial-reduction-source-audit-grok-20260824.md`
(SHA-256
`bbc8c1df4993301babed4fff5717f89bcae7fd849448e1c221884ab345ca9774`):
**LOCAL IDENTITY CONFIRMED / THEOREM 3.4 TERMINATION GAP / NOT A GLOBAL
JC2 REDUCTION**.

- LOCAL PROMOTION: Pinchuk 2021 Theorem 4.1 is correct for the stated exact
  degrees with matched leading coefficients.  Over `C(x)` in the separate
  fibre variable it gives
  `deg(p^r-q^k)=d*(k*r-k-r)+1+deg(r*p'*q-k*p*q')`.
  For `(k,r,d)=(4,3,3)`, the extremal number is 16.  This is the exact local
  identity used on the coprime `(9,12)`, `k=mu=nu=0` spectral face; it is
  not a classification of that face.
- GLOBAL QUARANTINE: Theorem 3.4's six local polygon cuts check, but the
  printed remainder walk lacks a well-founded termination argument and does
  not establish that its only terminal state has constant leading Jacobian.
  Its rational-power source changes also leave `C[x,y]`.  It is not licensed
  as a global JC2 reduction, `G2-PSC`, or polynomial normal form.
- CLASSIFICATION CORRECTION: Pakovich--Zvonkin 2014 gives the weighted-tree
  dictionary and classifies **unitrees**, not all minimizing equality pairs.
  The passport `(3^12)|(4^9)` is not a unitree.  No explicit literature list
  may be imported; a self-contained finite three-point-cover/descent argument
  must carry any maximum-12 rigidity claim.
- TYPE NOTE: `J(f,W)=3*(g^2-k*f^2)J(f,g)` requires `k` differential-constant;
  the reviewed Faber coefficient `k` has exactly that status, and the live
  DZ20 client has `k=0`.  A variable `k(x)` would contribute an extra chain-
  rule term.  This 2021 paper is unrelated to the real Pinchuk maps and does
  not change Avenue 24.

## MAXIMUM-12 `(9,12)` ORDER-THREE DZ20 EXCLUSION (2026-08-24, DIFFERENT-MODEL-CONFIRMED BRANCH TIER)

`xmodel/max12-912-order3-dz20-stabilizer-valuation-20260824.md` (SHA-256
`4a5ec8b08aab7a9ba5d7c22593efeb67621fea720128dd7051972f52cc9191e5`)
with
`xmodel/max12-912-order3-dz20-stabilizer-valuation-review-grok-20260824.md`
(SHA-256
`a8d7282ff98a0dfd998c52bfc60eed7e9f64ff89e6a988682ef8e80202229300`):
**CONFIRMED `THE NONTRIVIAL ORDER-THREE k=mu=nu=0 TRAJECTORY IS EMPTY
ON THE DEGREE-16 SPECTRAL FACE`**.

- SPECTRAL/PASSPORT: on the named Faber leaf, the elementary tail identity
  gives `deg_z(g^3-f^4)=16` and terminal nonvanishing follows from
  `9*r8'=j/u`.  The rational function `beta=g^3/f^4` is a degree-36
  three-point cover with exact passport
  `(3^12)|(4^9)|(20,1^16)` and Riemann--Hurwitz defect `70=70`.
  Finiteness comes from transitive permutation triples of the fixed passport,
  not from a Pakovich--Zvonkin unitree list.
- STABILIZER/DESCENT: the unique index-20 point fixes source infinity and
  depression kills translation.  Every residual source stabilizer has order
  `e in {1,2,4}`.  Exact Kummer covariance yields the three lattices
  `(e,N,a,S)=(1,20,2,14),(2,10,1,4),(4,5,2,4)` and
  `R=C*h^(-S)*v^(-N)`.  Local cancellation eliminates the apparent
  multiplicity-three resonance; infinity then forces `h` to be a cube,
  contradicting exact Kummer order three.
- COPRIMALITY FIREWALL: for an actual Keller trajectory,
  `D=f_x*g_z-f_z*g_x=j/u` is a nonzero `z`-constant.  Any
  `gcd_z(f,g)` divides `D`, so noncoprime components seen in a projected
  coefficient fibre are artifacts and must be saturated or labelled before
  trajectory use; there is no common-factor Keller trajectory stratum.
- CUSTODY/SCOPE: the coordinator reran the frozen manifest and reproduced
  the registered replay exactly.  This excludes only the nontrivial
  order-three `k=mu=nu=0` trajectory.  Nonzero invariant loads, the
  order-one core, `(8,12)`, the original Taylor-boundary families,
  maximum-twelve coverage, a counterexample, and JC2 remain open.

## TD6 FULL-COKERNEL CENTERING TANGENT (2026-08-24, DIFFERENT-MODEL-CONFIRMED TRANSVERSALITY TIER)

`xmodel/td6-centering-tangent-gate-20260824.md` (SHA-256
`15b08835512839d044c049b11ba889be1fbf06c52dc9ad6487e714910ac774d3`)
with `xmodel/td6-centering-tangent-review-grok-20260824.md` (SHA-256
`3d33ed766a4ea02b79bee1dd13b144c2f3adbfd7a0dbb571314c36679b92d13a`):
**CONFIRMED `CENTERING-TRANSVERSE / FULL-COKERNEL-INJECTIVE /
NO-COMMON-LINEARIZED-ROOT / C1-PENCIL-LICENSED` IN THE REGISTERED
NORMALIZED SECTION**.

- EXACT DIFFERENTIAL: the three common-center jets survive quotient by the
  registered regular source reparametrizations and four rectangle-preserving
  determinant-one target gauges.  Independent differentiation of all 3,602
  transport columns and both later parameterizations reproduces ranks
  `3470/3602 -> 38/132 -> 38/94 -> 25/56`, with every derivative rank-change
  flag zero.
- FULL COKERNEL: all ten current compatibilities, including the derivatives
  of their left-null vectors, give an exact `10x3` map of rank three and
  kernel zero.  The augmented rank is four, so
  `D C(v)=-C(1,1,1)` has no solution.  Independent minors, reverse-order
  elimination, residual hashes, and both registered replays agree.
- SCOPE/NEXT: the base control is already a nonsolution.  Injective
  sensitivity there is not a tangent-space calculation at a solution and
  does not kill remote or nonlinear centering roots, SP-2, a terminal class,
  or JC2.  It licenses the exact matrix-changing `c1` pencil and a stagewise
  exceptional-fibre atlas; it does not license a one-shot affine model after
  nonlinear substitutions.

## MAKAR-LIMANOV NEWTON-SHAPE AND MATE-RECOVERY INTAKE (2026-08-24, PRIMARY-SOURCE CONDITIONAL TIER)

`xmodel/websweep-20260824T1916Z-makar-shape-recovery-audit-codex.md`
(SHA-256
`cf910d136d59661e646563e4eb0ec8f5c256b0780b0bb2ed6a38328ace72df4b`)
and
`xmodel/websweep-20260824T1916Z-properties-jacobian-mate-audit-codex2.md`
(SHA-256
`84f4fb2738e18b1cc34a627d19a5bf2f96b5584d9ec35ecbe082a514ad5b94e6`):
**NEW CONDITIONAL NECESSARY CONDITIONS / NO CURRENT CAMPAIGN-FRAME
EXCLUSION / RECOVERY DOES NOT SUPPLY MATE EXISTENCE**.

- SHAPE: in Makar-Limanov's specially reduced complex-counterexample frame,
  the ratio-two case with the stated first vertical right edge is impossible.
  If the barred/smallest-monomial vertex is
  `v0=D*(a,b)`, `gcd(a,b)=1`, then the number of admissible right edges is at
  most `Omega(D)-1`.
- PROPERTIES: conditional on the paper's shaped-counterexample setup and
  imported resolution/recoverability inputs, the leading total degree
  satisfies `Omega(D)>=3`, where prime factors are counted with
  multiplicity.  The paper reports 19 surviving total degrees through 100,
  including 72, but publishes no implementation or coverage certificate;
  its table is not yet independently reproducible.
- RECOVERY: if a polynomial mate already exists, it is unique modulo
  `C[f]`, and finite declared branch/degree data can reconstruct and verify a
  normalized representative.  The paper gives no unconditional existence
  test, a priori mate-degree bound, or choice-independent finite algorithm
  for arbitrary `f`.
- TYPE FIREWALL: these Newton data are not Sigray topological degree, not
  automatically GGV packet data, and not maximum actual partial `y`-degree.
  They currently exclude none of `(72,108)`, residue-A, TD6, `(8,12)`, or
  `(9,12)`.  Any client must first prove the source-normalization bridge and
  must fail closed on unresolved symbols, table typos, and publisher-version
  drift.  The smallest licensed software is a provenance-bearing exact row
  checker plus bounded Faber/mate certificate packaging, not a mate finder.

## TD6 LICENSED `c1` LINE EMPTY (2026-08-24, DIFFERENT-MODEL-CONFIRMED FIXED-SECTION TIER)

The three producer reports
`xmodel/td6-c1-line-kill-gate-20260824.md`,
`xmodel/td6-c1-first-stage-localized-gate-20260824.md`, and
`xmodel/td6-c1-raw-transport-fibres-gate-20260824.md`, together with hostile
reviews
`xmodel/td6-c1-line-kill-review-grok-20260824.md` and
`xmodel/td6-c1-raw-transport-fibres-review-grok-20260824.md` (review SHA-256
`d2f8a204ca0e9cdf0c985b7940468e9ef6ef038ac17b245054a6e3a4fe87e7f9` /
`c524122ca098193075f39205d1833f9e310f8607956c1115ca97b9655fda767d`):
**CONFIRMED `THE COMPLETE LICENSED NORMALIZED SECTION
(c1,c2,c3)=(C,1,1) IS EMPTY`**.

- COVER: `C=0`, `C=3`, `C(C-3)J!=0`, and `J=4C^2+20C+1=0` are an exact
  exhaustive cover over every extension of the coefficient field.  Raw
  original-row rebuilds cover the two transport exceptions and the `J`
  quotient; the denominator-cleared polynomial identity covers the open.
- CERTIFICATE: transport and first ranks are `3470/3602` and `38/132` on
  every stratum.  The genuine quadratic current row has a full original-row
  certificate with remainder `-k/50`, and `k` has an explicit inverse in the
  frozen field.  The obstruction is therefore a nonzero unit after scalar
  extension.
- SCOPE: this is one fixed normalized one-parameter center section.  It does
  not cover simultaneous `c2,c3` motion, other boundary/dead-stretch/F1/pole
  moduli, TD6, SP-2, a terminal class, or JC2.  An injective sensitivity map
  at the base nonsolution and a line theorem do not imply a neighborhood.

## MAX12 PARITY-NORMAL `Q12` CHECKPOINT QUARANTINED (2026-08-24, DIFFERENT-MODEL REFUTATION)

Producer report
`xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md` (SHA-256
`9616396705d071efac3cf52332c5007a4a045989940bcc8743a545e87f763a1c`)
with hostile review
`xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md`
(SHA-256
`fc0b0216784bdcec8f9b0955c5a6c71d57870ae2265ed927f306d19d31a79c30`):
**REFUTED / QUARANTINED BEFORE PROMOTION**.

- SMALLEST ERROR: the report displays the reviewed actual-fibre substitution
  `x1=x5*p^2*(v+1)+x5^2*(3v+1)/(9v)`, but its replay substitutes
  `x1=x5*p^2*(v+1)+x5^2/(27v)`.  The latter does not satisfy `r2=r4=0`.
  The determinant depends on `x1`, so a passing replay certifies an off-fibre
  identity.
- EXACT COUNTERCHECK: at `p=v=1` on the correct chart,
  `det(J_N)=25275425185572323328`, whereas the claimed formula gives
  `169664962152837939200/243`.  The reviewer reconstructs a residual
  squarefree octic `Q8`, coprime to `Q12`; that identity remains reviewer
  evidence until independently frozen and reviewed as a replacement.
- ROLLBACK: the `Q12` producer package and the dependent frozen formal-branch
  package are byte-preserved and quarantined.  No descendant may consume
  them.  The correct-chart determinant must reproduce the old wrong slice as
  a negative control before any `Q8` successor is promoted.
- UNAFFECTED: the involution typing and completeness of the normal `4x4`
  block survive.  The separately reviewed parity genus-five exclusion,
  full-absorption theorem, and DZ20 exclusion do not use the wrong `x1` and
  remain promoted.  No maximum-twelve or JC2 conclusion ever depended on the
  quarantined checkpoint.
- DESCENDANT REVIEW: the dependent formal-branch package is independently
  `REFUTED` by
  `xmodel/max12-912-order3-nu-q12-formal-branch-review-claude-20260824.md`
  (SHA-256
  `5efb648c0e351dce8179bc0524949faa67d7e8a4389be73296ebaae918ed137c`).
  Its equivariant IFT template is sound, but the genuine determinant is a
  unit at every `Q12` root because `gcd(Q8,Q12)=1`; consequently the alleged
  second germ is empty and those artificial `Q12` contacts are parity-trapped
  at all orders.  This licenses no new `Q12` route and changes no live scope.

## AS VERTICAL D8 CAPPED-ADJUGATE STATE THEOREM (2026-08-24, DIFFERENT-MODEL-CONFIRMED MATRIX TIER)

`xmodel/as-fonly-d7-vertical-state-sufficiency-20260824.md` (SHA-256
`410235081a54470a377d8d107a1982d34d507040718b945d11ee99dc4d1e5fe4`)
with hostile review
`xmodel/as-fonly-d7-vertical-state-sufficiency-review-grok-20260824.md`
(SHA-256
`6ab373bf9214c54f506cd368473aff02ed472a20e9797037f83a9745c384bc17`):
**CONFIRMED FOR THE DISPLAYED CORRECTED `7x5` MATRIX AND ITS LITERAL-`F3`
COMPARISON**.

- EXACT STATE: with `H=h^3`, the capped coefficient map is
  `M(X,Y)=(-A*X+B*Y,-H*X-A*Y)`, `deg X<=2`, `deg Y<=1`.  Its adjugate obeys
  both products `Msharp*M=M*Msharp=(A^2+H*B)I`.  On nonzero determinant,
  divisibility of the two adjugate numerators together with the two quotient
  degree caps is necessary and sufficient.  The determinant-zero strata have
  the reviewed one-line criteria; the only specialized ranks are `5,3,2,0`.
- EXHAUSTIVE CONTROL: an independent implementation agrees with direct rank
  on all `3^13=1,594,323` literal assignments and all `314,127` compatible
  assignments, including the frozen stratum totals, fibre histogram, and
  stream hashes.  Removing only the quotient caps creates exactly `202,176`
  false positives, so the caps are load-bearing state data.
- SCOPE/NEXT: the theorem is unconditional for the displayed matrix.  Its
  interpretation as the exact AS successor remains conditional on the still-
  active different-model review of the corrected integer-source column.  It
  is not the next divided carry, an algebraic-closure component theorem, an
  all-depth lift/no-lift result, a characteristic-zero map, a counterexample,
  or JC2.  The licensed arithmetic successor imposes the next source-divided
  carry on the two capped quotient polynomials while retaining every
  determinant-zero stratum and nilpotent predecessor component.

## MAX12 ROOT-FREE UNORDERED CRITICAL-VALUE NORM (2026-08-24, DIFFERENT-MODEL-CONFIRMED STRATIFICATION TIER)

`xmodel/max12-912-order3-critical-value-norm-20260824.md` (SHA-256
`7339478798e00894c7b975c60aca821ec7ff2da383ffe5165a93cfa361bb6cb6`)
with hostile review
`xmodel/max12-912-order3-critical-value-norm-review-grok-20260824.md`
(SHA-256
`b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e`):
**CONFIRMED EXACT COEFFICIENT-FIELD CASE SPLIT ON THE NORMALIZED LOADED
ORDER-THREE FIBRE**.

- ROOT-FREE IDENTITY: over the quadratic algebra `z^2=s`, write
  `f^4=F0+F1*z`, `g^3=G0+G1*z`.  Then
  `C(T)=Norm(g^3-T*f^4)` is quadratic and
  `disc_T(C)=4*s*(G0*F1-G1*F0)^2`; `C(1)` is exactly the norm of
  `g^3-f^4`.  Independent reconstruction matches the monic quadratic
  resultant and the actual on-fibre Wronskian, including its scaling from
  arbitrary nonzero constant `nu` to the `nu=1` chart.
- EXHAUSTIVE OPEN SPLIT: after localizing at `s*Norm(F)`, the disjoint leaves
  are full absorption, exactly one absorbed root, equal non-unit critical
  values, and unequal unabsorbed values.  The double-root `s=0` and
  `B`-meets-`f` strata remain explicit.  Parity is only a positive control
  inside the equal-value locus; no selected root or premature coprimality
  firewall is used.
- SCOPE/NEXT: this stratifies but excludes no residual leaf and supplies no
  Taylor or terminal equation.  The licensed successor attaches the original
  seven rows and both Taylor families leafwise, using cube-divisor signatures,
  exact four-point Hurwitz genus, and descended differential dynamics only
  after their hypotheses are proved.  Other loads, order one, `(8,12)`,
  maximum twelve, a counterexample, and JC2 remain open.

## MAX12 GENUINE `Q8` NON-PARITY FORMAL BRANCH (2026-08-24, DIFFERENT-MODEL-CONFIRMED FORMAL-LOCAL TIER)

`xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md` (SHA-256
`37ce842eece0e79f0768bdfd492be70905bb83ba62af93965b4c4a2a3d6f03a3`)
with hostile review
`xmodel/max12-912-order3-nu-q8-formal-branch-review-grok-20260824.md`
(SHA-256
`32750e4e350919d7d52984feab06d3cd2d801386caec5848f7c5750bf9e8e846`):
**CONFIRMED EVERY LOADED `Q8` PARITY CONTACT OF THE GENUINE SEVEN-ROW
COEFFICIENT FIBRE LIES ON A SECOND SMOOTH NON-PARITY FORMAL COMPONENT**.

- FRESH LINEAGE: all eight source tails and involution characters were
  reconstructed on the correct `1+3v` chart.  No quarantined `Q12` report,
  replay, determinant, or branch is consumed.  Independent Gaussian and gcd
  work reconfirms the corrected `Q8` determinant at every algebraic root.
- FORMAL GEOMETRY: both the normal and invariant blocks have rank exactly
  three at every loaded `Q8` point; all named localization factors are units,
  `Q8` is squarefree, and `gcd(Q8,num(R6'))=1`.  Equivariant implicit
  elimination leaves `t*Phi(s,t^2)=0`, with
  `Phi(s,0)=unit*det(J_N)` and `dPhi/ds!=0`.  Hence the completed seven-row
  fibre is the reduced union of the parity branch `t=0` and a distinct smooth
  non-parity branch `s=psi(t^2)`.
- SCOPE/NEXT: this is positive formal coefficient-fibre geometry, not an
  algebraic or rational Keller trajectory.  It does not impose `r8`, the
  terminal differential, Kummer descent, either Taylor family, or
  coprimality, and says nothing about components disjoint from parity.  The
  licensed successor normalizes the new branch and pulls back `r8` before
  any `(9,12)`, maximum-twelve, counterexample, or JC2 inference.

## MAX12 SELECTED-`Q8` GLOBAL QUOTIENT (2026-08-25, DIFFERENT-MODEL-CONFIRMED ALGEBRAIC-COMPONENT TIER)

`xmodel/max12-912-order3-nu-q8-global-quotient-gate-20260824.md`
(SHA-256
`2102e5d730af7d9bd4a434a99ea9b7213cdf08016becd0e49061f5210ec0feaa`)
with hostile review
`xmodel/max12-912-order3-nu-q8-global-quotient-gate-review-claude-20260824.md`
(SHA-256
`49e8d9092e257a003f39171d0ec53fca91cc8f5c6e02841816f88aad127e6b39`):
**CONFIRMED AT STRICT `k=mu=0,nu!=0` SELECTED-COMPONENT SCOPE**.

- EXACT QUOTIENT: after the parity quotient of the geometric `p=1` chart,
  the punctured non-parity branch is modelled by six source-compiled rows in
  `(w,c,d2,d4,x1,x3,x5)`, with weight-zero outputs
  `n=r6/p^9`, `q=r8/p^10`.  The unique algebraic component through each Q8
  contact is a smooth one-dimensional component; the two modular standard
  bases are routing evidence only and do not classify the whole open scheme.
- LOCAL/BOUNDED CERTIFICATES: the exact lift through `w^5` over
  `Q[v]/(Q8)` is unique with all displayed coefficients units.  The frozen
  finite boxes exclude the listed low Pade types, every tested
  `H(w,Z)` rectangle with at most 48 monomials, and all
  `1<=deg_n,deg_q<=4` relations.  Nothing outside those boxes is inferred.
- SCALE/TERMINAL DESCENT: along an actual fixed-load trajectory,
  `pi=p^9=nu/n`, `S=r8^9=nu^10 Z`, and therefore
  `nu^10 h^3 (Z')^9=j^9 Z^8`.  This uses the full off-parity output `n`, not
  the parity-only identity that fails off parity.
- RESIDUAL REVIEW CLOSURE: the review's shell conditions were discharged on
  AWS and frozen in
  `xmodel/max12-912-order3-nu-q8-global-quotient-aws-custody-20260825.md`
  (SHA-256
  `64d01a190ddd729fc1b3e3b16b64bad1a7d05ee9471a1f8ebd1fb59150dad93b`).
  The replay returned rc zero with stdout SHA `d05eeb86...`, byte-identical
  to the frozen payload; the independent probe returned rc zero with stdout
  SHA `6e6acff2...` and terminal `PROBE-DONE`.  The custody manifest/freeze
  hashes are `07cad415...` / `da73c423...` and verify locally.
- SCOPE: removed affine/projective boundaries, both Taylor families, a
  global quotient equation, normalization/genus, rational trajectory,
  all-`(9,12)`, maximum twelve, counterexample, and JC2 remain open.

## MAX12 SELECTED-`Q8` TERMINAL BELYI CLASSIFICATION (2026-08-25, DIFFERENT-MODEL-CONFIRMED CORRECTED NECESSARY TIER)

`xmodel/max12-912-order3-terminal-belyi-classification-20260824.md`
(SHA-256
`5d8806db54eb2056dd7aafe6fb7dc342c68be1bef7cba06b96beeeaa765273fc`)
with hostile review
`xmodel/max12-912-order3-terminal-belyi-classification-review-claude-20260824.md`
(SHA-256
`713e41def64d0fc313d254cae5d660e412f5ba9b69bd4d7c0e6c212a4688c52b`)
and recorded erratum
`xmodel/max12-912-order3-terminal-belyi-classification-erratum-20260825.md`
(SHA-256
`0221a683fc88daeb162d84096e94200989dd3853d3f319455bf13f4e1dd93b1f`):
**CONFIRMED WITH THE EXPLICIT HYPOTHESIS `Z` NOT IDENTICALLY ZERO**.

- CORRECTED CLASSIFICATION: every selected-branch rational solution with
  `Z!=0` has `Z=T^3` and
  `h=C*T^2/(T')^3=C*A^2*B^4/(A'B-AB')^3`.  Polynomiality is equivalent to
  every finite Wronskian root lying over zero or infinity of `T`, with each
  zero multiplicity of `T` at most three.
- DEGREE SPLIT: the unequal-degree strata are incompatible with the
  noncube condition and `3|deg(h)`.  In the balanced case
  `deg A=deg B=D`, `lambda=T(infinity)`, and
  `e=ord_infinity(T-lambda)` give `r+s=e+1` and
  `deg(h)=3(e+1)`.  The map has exactly three branch values with complete
  passport `(alpha_i<=3)` over zero, `(beta_j)` over infinity, and
  `(e,1^(D-e))` over `lambda`, saturating Riemann--Hurwitz.
- ERRATUM: without `Z!=0`, the displayed terminal identity also admits the
  trivial family `Z=0`, so three unrestricted producer sentences were
  literally too broad.  Frozen bytes remain unchanged; every promotion uses
  `k=mu=0,nu!=0,Z!=0`.  Along an actual trajectory the original row
  `9*r8'=j/u`, `j!=0`, forces `Z` nonconstant, so the registered
  actual-trajectory theorem is unaffected.
- POSITIVE CONTROLS/SCOPE: cyclic controls show the necessary classification
  alone excludes no trajectory and does not reconstruct coefficient-fibre or
  Taylor data.  The later exact terminal/Kummer converse and even-contact
  control remain separate producer-tier successors.  No selected-Q8
  trajectory, `(9,12)` cell, maximum-twelve case, counterexample, or JC2
  conclusion follows.

## MAX12 SELECTED-`Q8` INFINITY PASSPORT AND PRIMITIVE CONTACT GROUPING (2026-08-25, DIFFERENT-MODEL-CONFIRMED CONDITIONAL GLOBAL TIER)

The infinity/passport report
`xmodel/max12-912-order3-nu-q8-infinity-contact-passport-20260824.md`
(SHA-256
`89691023f2703eba5c0cd29d65bc8732d837905fe41b01f64ae9d3b908068168`),
the Galois-primitivity report
`xmodel/max12-912-order3-nu-q8-galois-primitivity-20260825.md`
(SHA-256
`9f37fc3fc7933b911bea56258f677da77a823caa8daf9ce01c03b0884c502c8f`),
and their joint hostile review
`xmodel/max12-912-order3-nu-q8-infinity-primitivity-review-claude-20260825.md`
(SHA-256
`c77a73307bfda48fdde7792c523e09ee4d565c5782bcf71ed13d13b1d613a57c`):
**CONFIRMED AT THE REGISTERED ACTUAL-TRAJECTORY, SELECTED-COMPONENT, AND
FINITE-FIELD-CERTIFICATE SCOPES**.

- INFINITY/PASSPORT: for an actual loaded order-three trajectory whose
  Kummer-fixed quotient image lies on the selected component through a
  corrected-`Q8` contact, the induced map from `P1` to the projective
  normalization is nonconstant and surjective, and that contact's
  normalization point has complete preimage `{x=infinity}`.  The balanced
  terminal index is
  `e_pass=2*ord_infinity(a0)`, hence even and at least two;
  `deg(h)=3*(e_pass+1)=3 mod 6`, and every survivor attains equality in the
  Mason--Stothers bound.  The exact `e_pass=2` noncube control satisfies the
  original row `9*r8'=j/u`; it is a terminal/Kummer control, not a Keller
  pair.
- PRIMITIVITY: the corrected octic is irreducible modulo 7 and has squarefree
  factor pattern `[1,7]` modulo 53.  Dedekind therefore supplies an
  eight-cycle and a seven-cycle in its Galois action.  The action is
  transitive and primitive, so the Galois-equivariant partition of the eight
  contacts by the unique geometric component through each is either one
  block of eight or eight singleton blocks.  Equivariance uses the
  `Q`-defined divided quotient scheme and uniqueness of the component through
  each contact; it is not an extra computed assumption.
- CONDITIONAL COMBINATION: a selected component containing two contacts
  cannot carry such a trajectory, because two distinct normalization points
  would both have to equal the single image of `x=infinity`.  Thus the
  all-eight alternative carries no registered actual trajectory.  The eight
  singleton alternative remains completely open, as do components disjoint
  from the contacts.
- CUSTODY/REPLAY: infinity manifest/freeze SHAs are `a9e8748f...` /
  `8d695040...`; primitivity manifest/freeze SHAs are `1a3e44b9...` /
  `f25fa86f...`.  The no-shell review's residual replays were executed on
  Box02 at
  `/home/ubuntu/jc2q8-box02/out/q8_infinity_primitivity_review_residual_20260825T0312Z`:
  the infinity and primitivity payloads matched byte-for-byte at SHAs
  `8d13cb67...` and `f5b37f95...`, the latter with rc zero and empty stderr.
- SCOPE/NEXT: this neither proves the singleton components exist globally
  with the required Taylor data nor excludes a trajectory on one of them.
  Exact component grouping, normalization/genus, every charged coefficient
  and Taylor pole, both Taylor polynomiality families, removed boundaries,
  `(9,12)`, maximum twelve, a counterexample, and JC2 remain open.

## MAX12 SELECTED-`Q8` MOD-127 PROJECTED COMPONENT (2026-08-25, DIFFERENT-MODEL-CONFIRMED COMPONENT-EXISTENCE TIER)

The repaired nonmutating successor
`xmodel/max12-912-order3-nu-q8-p127-component-reviewed-successor-20260825.md`
(SHA-256
`7d28a7b4b7d3ecd3179efc73f0251754fbfea87614b6eb6daef2d7d649dba202`),
incorporating the independent hostile review
`xmodel/max12-912-order3-nu-q8-sparse-contact-component-review-claude-20260825.md`
(SHA-256
`ebd0024dfe2ea1623f22ba483b93d76dd9ff2aabe5f9f96eabc7b115928c7164`):
**CONFIRMED OVER `Fbar_127` THAT A RELEVANT SELECTED-QUOTIENT SOURCE
COMPONENT PROJECTS ONTO `H`**.

- EXACT DEGREE/CONTACT GATE: origin-augmented sparse mixed volume gives
  `deg(pi_*Z)<=658`.  The proof now uses only stored positive-order lifts:
  80 distinct order-eight fibres, all excluding `w=25`, plus the frozen
  `w=25` order-64 fibre.  Their normalized contact is
  `80*8+64=704>658`; the older `123+63+68*7=662` count is explicitly
  superseded and is not consumed.
- REVIEW REPAIRS: the pushforward is defined on the normalization of the
  projective graph closure; source-closure points outside the affine chart
  are included in the generic-line bad set; the unit relative Jacobian makes
  `w-w_i` a uniformizer and hence forces separability in characteristic 127;
  and the distinct isolated sparse-root count bounds the pushforward degree.
  Box03 was an independent execution replication of the pinned Normaliz
  pipeline, not an independent implementation.  No numerical or mathematical
  claim changes.
- SCOPE/NEXT: this is existence of at least one `H`-supported projected source
  component modulo 127 only.  Source degree one, a global coordinate graph,
  all-190/all-eight contact coverage, characteristic-zero no-merger, Taylor
  realization, terminal differential descent, rational trajectories,
  `(9,12)`, maximum twelve, a counterexample, and JC2 remain open.

## MAX12 SELECTED-`Q8` PINNED PLANE-CURVE INTEGRALITY (2026-08-25, DIFFERENT-MODEL-CONFIRMED STANDALONE-CURVE TIER)

The exact producer report
`xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-20260825.md`
(SHA-256
`b3cddbce9a118c60bf789df374941367a327b6608871a562ddffceebc3b900d0`)
and hostile review
`xmodel/max12-912-order3-nu-q8-p127-candidate-plane-integrality-review-claude-20260825.md`
(SHA-256
`f2e24aa5baa336067479eab7549f74bd2ceda7f61b5da2a049ea75be73d835dc`):
**CONFIRMED THAT THE PINNED MONIC DEGREE-190 POLYNOMIAL `H(w,v)` IS
IRREDUCIBLE OVER `F_127(w)` AND GEOMETRICALLY INTEGRAL OVER `F_127`**.

- ARITHMETIC IRREDUCIBILITY: the squarefree specializations at `w=25` and
  `w=47` have irreducible-degree partitions `(2,188)` and `(1,3,186)`.
  Their proper subset-sum sets are disjoint.  Monicity and integrality over
  the integrally closed ring `F_127[w]` force every hypothetical rational-
  function-field factor to specialize without degree drop, giving the
  contradiction.
- GEOMETRIC INTEGRALITY: the exact point `(w,v)=(71,50)` lies on `H` with
  `H_v=104!=0`.  Arithmetic irreducibility makes Galois transitive on any
  geometric components; the rational smooth point would then lie on every
  conjugate component and be singular.  A repeated geometric component is
  separately excluded by the `w=25` squarefreeness certificate.
- REVIEW/CUSTODY: the hostile reviewer read the full pinned JSON and source,
  hand-rederived 30 specialized coefficients and the complete proof, and
  found no required repair.  The coordinator independently reran the exact
  case on AWS r6a with byte-identical input/result/audit outputs and rc zero.
  The nonmutating replay manifest is
  `cases/max12_912_order3_nu_q8_p127_candidate_plane_integrality_aws_20260825/REVIEW_REPLAY_MANIFEST.sha256`
  (SHA-256
  `cba71f0cac64099f3bc144455c1543bb8c5e4ca2064ccce7797fe9c934022374`).
  Optional successor hardenings are an explicit maximum-support-key assertion
  and automatic inclusion of the cross-case candidate JSON in manifests.
- SCOPE: this theorem concerns the standalone explicit plane curve only.  It
  does not by itself prove selected-Q8 quotient membership, source-component
  identity, coordinate reconstruction, contact membership,
  characteristic-zero lifting, a trajectory exclusion, maximum twelve, or
  JC2.  Those arrows must be supplied by their separately reviewed packages.

## MAX12 SELECTED-`Q8` PINNED PLANE-CURVE POSITIVE GENUS (2026-08-25, DIFFERENT-MODEL-CONFIRMED STANDALONE-CURVE TIER)

The exact point-count producer
`xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-20260825.md`
(SHA-256
`c4c4ebdf59a95ff84c37ebbedcd46608fb32f34077790c9bdbdaac776f64a00a`)
and hostile Grok review
`xmodel/max12-912-order3-nu-q8-p127-positive-genus-point-count-review-grok-20260825.md`
(SHA-256
`1b79cddc6f3107c9bc722c21135fb0c87fa3e9793311c071c7a5a57a55d5bb8e`):
**CONFIRMED THAT THE SMOOTH PROJECTIVE NORMALIZATION OF THE PINNED
GEOMETRICALLY INTEGRAL CURVE `H/F_127` HAS POSITIVE GENUS**.

- EXACT COUNT: over `F_(127^2)`, the frozen fibre-gcd enumeration gives
  `16,174` affine points, of which `16,168` are smooth and `6` singular.
  The `16,168` smooth affine points inject into the normalization, whereas a
  genus-zero curve with the already reviewed smooth `F_127`-point would be
  `P1` and have only `127^2+1=16,130` points.  Uncounted points at infinity
  and branches over singular affine points can only strengthen the lower
  bound.
- EXECUTION/REVIEW: Box02 and r6d ran the identical pinned python-flint
  implementation with different 16-shard and 8-shard partitions.  Every
  adjacent Box02 pair equals the corresponding r6d block, and four sampled
  fibres passed a direct-evaluation-versus-gcd control.  This is a two-host
  partitioned replay, not by itself engine diversity.  After that review, an
  independent pure-Singular implementation on AWS r6a reproduced exactly
  `16,174/16,168/6` across 16 fail-closed shards.  Its report
  `xmodel/max12-912-order3-nu-q8-p127-positive-genus-singular-cross-engine-20260825.md`
  has SHA-256
  `5ec2ce70d3ed6e680338143dd745805a728b017a4ef039095aa7a7cadbe4be1b`,
  and its case manifest has SHA-256
  `214abb00e2de20a205ffc86839752f69c0f27610fd002bd7431d7a82fb4cb20a`.
  The hostile reviewer independently checked the field modulus,
  partitions, fibre formula, singular-point test, totals, and genus
  implication.  Review custody is frozen under
  `cases/max12_912_order3_nu_q8_p127_positive_genus_point_count_review_grok_20260825/`
  with manifest SHA-256
  `8e7a31fd59f352d3df935465df54763e78adf3a1ff461b1bf19d6e84df2768f0`.
- SCOPE: this is a theorem about the standalone pinned plane curve only.  It
  proves no quotient membership, characteristic-zero specialization,
  source-component identity, trajectory exclusion, `(9,12)`, maximum
  twelve, or JC2.  Those compositions remain separately review-gated.

## MAX12 SELECTED-`Q8` RATIONAL CONTACT ON `H` (2026-08-25, DIFFERENT-MODEL-CONFIRMED MOD-127 EXISTENTIAL TIER)

The nonmutating reviewed erratum
`xmodel/max12-912-order3-nu-q8-p127-rational-contact-residual-reviewed-erratum-20260825.md`
(SHA-256
`c470fd253d59cc2f3377e5a2c03baa345c22b365522a3eb17ae320992fb5d925`),
incorporating hostile review
`xmodel/max12-912-order3-nu-q8-p127-rational-contact-residual-review-claude-20260825.md`
(SHA-256
`658341959f39cdcad00e5f42d440af8bdb7fb2454b6676c96e6b00bddb10b562`):
**CONFIRMED THAT AT LEAST ONE OF THE THREE RATIONAL FULL CONTACTS
`v=26,58,67` LIES ON AN `H`-SUPPORTED MOD-127 SOURCE COMPONENT**.

- CORRECTION: the affine sparse value `658` bounds plane degree; it does not
  imply `A+B<=658` for the closure in `P1_w x P1_v`, because the
  bihomogenized target lines share the base point `(infinity,infinity)`.  The
  old residual constant `35,582` and equal-contact threshold `4,448` are
  retired.
- REPAIRED BOUND: the independently frozen coordinate bounds `A<=176` and
  `B<=550`, minus one `H` summand of bidegree `(21,190)`, give residual
  `(a,b)<=(155,360)` and
  `I(H,R)<=190*155+21*360=37,010`.
- CONTACT GATE: the three distinct full source branches have exact contact
  lower bounds `16,384+16,384+8,192=40,960>37,010`.  Their full internal
  Jacobians and localizers are units, so their local intersection
  contributions are legitimate and additive.  The conclusion is existential
  only: it identifies neither the contact nor all eight contacts, and proves
  no characteristic-zero component statement by itself.

## MAX12 SELECTED-`Q8` ARITHMETIC FULL-CONTACT BRIDGE (2026-08-25, DIFFERENT-MODEL-CONFIRMED ARITHMETIC-LOCAL TIER)

The exact producer report
`xmodel/max12-912-order3-nu-q8-char0-mod127-contact-bridge-20260825.md`
(SHA-256
`39ae622919f5eba41e4e1a18d6777749d38c34a1be4a10569f65295815a11490`)
and hostile review
`xmodel/max12-912-order3-nu-q8-char0-mod127-contact-bridge-review-claude-20260825.md`
(SHA-256
`571221ad8a87c23a1ad15b4b77da3c8b9332c4d93a521d2ef6c143d5f143046d`):
**CONFIRMED AT THE COMMON INTEGRAL SIX-ROW SOURCE AND EIGHT MARKED CONTACT
COMPLETIONS**.

- INTEGRAL MODEL: all six divided source rows have 127-integral coefficients
  and reduce coefficientwise to the frozen mod-127 rows.  The graph rows for
  `v` and `inv` invert `x5*(x3-2*x5)` but not `w`; therefore they retain the
  marked `w=0` contacts and present the same localized six-row scheme used by
  the reviewed characteristic-zero and mod-127 consumers.
- CONTACT COMPLETION: after a complete unramified splitting-DVR extension,
  the monic corrected octic has eight integral roots with distinct
  reductions.  The exact eight-coordinate contact section reduces to the
  frozen mod-127 section, and the full relative `8 x 8` determinant is a unit
  at every contact.  Formal implicit-function theory gives arithmetic
  completed local ring `R[[w]]`, with fibre completions `K[[w]]` and
  `k[[w]]`; the characteristic-zero germ is the already reviewed selected
  branch by uniqueness.
- CUSTODY/SCOPE: producer/replay completed rc zero on r6d; case manifest and
  freeze SHAs are `d7abdade...` / `e9744c64...`.  Review found only
  nonblocking phrasing and a static import-pin hardening.  This is a local
  specialization bridge, not a global `H`-component lift, degree-one theorem,
  all-eight grouping, Taylor realization, maximum-twelve theorem, or JC2
  result.

## MAX12 SELECTED-`Q8` POSITIVE-GENUS TRAJECTORY EXCLUSION (2026-08-25, DIFFERENT-MODEL-CONFIRMED STRICT SELECTED-LEAF TIER)

The repaired V2 composition
`xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-v2-20260825.md`
(SHA-256
`d7e73783191d70a86e5c8786b735d0a596034c1d492559049d13433b8e889209`)
and hostile Grok review
`xmodel/max12-912-order3-nu-q8-selected-contact-positive-genus-exclusion-repaired-v2-review-grok-20260825.md`
(SHA-256
`f8d5208d9e915f694a9df1c9ae9014612e87c172b794c94bbfcf30f98bdb7996`):
**CONFIRMED THAT AN ACTUAL ORDER-THREE TRAJECTORY CANNOT LAND ON A
SELECTED `k=mu=0, nu!=0` COMPONENT MEETING A CORRECTED-`Q8` CONTACT**.

- ATTACHMENT: the common full-source completion is `R0[[w]]`.  The selected
  generic component has zero closure ideal there and a unique reduced
  special branch.  Over `Fbar_127` that branch identifies the unique
  geometric `H`-supported component through the existential winning full
  contact.  V2 passes first to its finite field of definition and the
  corresponding unramified DVR, before using geometric integrality or genus.
- GENUS OBSTRUCTION: the independently reviewed point count gives
  `g(Htilde)>0`; dominance makes the attached special component have positive
  geometric genus.  If the selected characteristic-zero component were
  dominated by the trajectory `P1`, then after a finite DVR extension its
  function field would be rational.  Properization and the divisorial
  valuation of the attached special component give a ruled residue field;
  geometric Lueroth would force that special component to have genus zero, a
  contradiction.  No unproved arithmetic-genus or global-reducedness claim
  is used.
- PROPAGATION: the reviewed primitive partition is one all-eight component
  or eight singleton characteristic-zero components.  Infinity already
  excludes the all-eight alternative; in the singleton case the eight
  characteristic-zero components are `Qbar`-isomorphic, so the genus
  obstruction propagates.  This makes no claim that all eight special fibres
  are `H`-supported.
- CUSTODY: the V2 producer case manifest/freeze SHAs are
  `1d252c9a80251dd9a549ea4fe9d57f3372c3d39a42e484e33262948631fc999f` /
  `8ffd390c952353a4e651693d952a05383196d7ae813d9efd70c5d54ddde63087`.
  The final-review custody manifest/freeze SHAs are
  `39ce1e9217d0a970822d5a11e899155f475d6492223780b2e1d4e1c043a997b4` /
  `51250f2e3029f1ec0f02954124cdbbaa40eb0a72ab0706faa904f1f5dc7e8ec1`;
  all pins verify.
- SCOPE: the theorem is conditional on the upstream cube/Faber and global-
  quotient landing of an actual trajectory in this selected contact leaf.
  It excludes neither components disjoint from the corrected contacts, every
  `nu!=0` component, the polynomial core, `(8,12)`, all `(9,12)`, maximum
  twelve, an arbitrary Keller pair, nor JC2.

## AS RESIDUE-BALL COLLISION AND FIXED-SUPPORT COMPACTNESS (2026-08-25, DIFFERENT-MODEL-CONFIRMED CONDITIONAL GLOBAL LEMMA)

The repaired theorem
`xmodel/as-fonly-residue-ball-collision-compactness-theorem-repaired-20260825.md`
(SHA-256
`81ab0e5cce46d2ad93968500362275ae4a7dbf2d3cf080c54ace531218135d71`),
its nonmutating V2 erratum
`xmodel/as-fonly-residue-ball-collision-compactness-theorem-repaired-v2-erratum-20260825.md`
(SHA-256
`d50426b36d2881ed577568c0c256f7f45f8f7154805b0f97512cc3e54be1ee2f`),
and final hostile Grok review
`xmodel/as-fonly-residue-ball-collision-compactness-theorem-v2-review-grok-20260825.md`
(SHA-256
`0cd7051300bf3938f6b389b1407a46f9a0c7a2d737e209a44c89c00c49e32a30`):
**CONFIRMED THAT COLLISION IS AUTOMATIC FOR A COMPLETE FIXED-SUPPORT
ALL-DEPTH LIFT OF THE AS RESIDUE MAP; IT IS NOT AN EXTRA SOLVER CONDITION**.

- FINITE RINGS: if `F=(P,Q)` over `Z/3^n Z` has the literal polynomial
  identity `det J(F)=1` and reduces to `(x-x^3,y)`, then for every target in
  the residue ball over `(0,0)` each of the three source balls over
  `(0,0),(1,0),(2,0)` contains exactly one preimage.  The digit equation is
  `JF(x_k)h=(z-F(x_k))/3^k mod 3`; invertibility gives existence and
  uniqueness, while the distinct x-residues give unit-separated moving
  collisions.  The colliding points need not be the marked integer
  representatives.
- COMPACTNESS/TRANSFER: if the same finite allowed monomial sets and all
  determinant-coefficient equations have solutions at arbitrarily deep
  powers of three, nested compact coefficient cylinders (equivalently a
  finitely branching solution tree) give one compatible `Z_3` map.  Its
  Hensel collision gives a `Q_3` point of the finite-type affine
  coefficient/collision scheme; base extension and Nullstellensatz give a
  `Qbar`, hence complex, constant-Jacobian map with a genuine collision.
  Actual support may shrink inside the fixed allowed sets but may not grow;
  a degree cap is only one possible choice and is not synonymous with a
  lacunary fixed support.
- CONTROLS: the frozen AWS replay checks the AS reduction, determinant, three
  moving preimages, and unit separation modulo 9 and 27, with a singular-
  Jacobian negative control.  These are finite-depth regressions only and do
  not evidence all-depth survival.
- CUSTODY: the final V2 review package is
  `cases/as_fonly_residue_ball_collision_v2_review_20260825/`; its manifest
  and freeze SHAs are
  `68164533ab105fc394d15f693f2fd0f6b200d5d67a0be47765e3321b68bc03f3` /
  `d56b2432de79221dcca11e19385e0f429eca43d9342915fbc86741221ef493d8`.
- FIREWALL: the lemma consumes only a complete fixed-support map scheme with
  every determinant row, exact integer reconstruction, one residue
  component, and arbitrarily deep survival.  Filtered high bands, changing
  supports, gauges that do not reconstruct the map, and finitely many depths
  do not qualify.  In particular, the current Q5/H6 state still owes Q4
  through Q0 and is not a complete map modulo 243; no collision or JC2
  inference attaches to it.

## AS F-ONLY D7 CORRECTED DIVIDED-FROBENIUS TOP CARRY (2026-08-25, DIFFERENT-MODEL-CONFIRMED FINITE-STATE TIER)

The source erratum
`xmodel/as-fonly-d7-next-top-carry-frobenius-erratum-20260825.md`
(SHA-256
`1129f2c93db930a3040e1626cc34dcfd818e824b356cbd63baac4e8d37c9ea0c`),
the corrected Q11/Q10 reports
`xmodel/as-fonly-d7-vertical-next-top-corrected-shards-20260825.md` /
`xmodel/as-fonly-d7-vertical-next-top10-corrected-shards-20260825.md`
(SHA-256
`4d9cebdaaefb7aff260d4d5bec5f24d88ec66cc8613bf5571a81778a70e10082` /
`b636b00a0c6bc9673cda46efa312b311c71e70c5dd24e92823b2bff205b3a817`),
and hostile review
`xmodel/as-fonly-d7-corrected-top-carry-review-claude-20260825.md`
(SHA-256
`f3dadb7176dfbaa8673d85c813e5ab672a3d8f85d0b40a9d234bac33f2d6d78c`):
**CONFIRMED AT THE DISPLAYED DEGREE-12/11/10 SOURCE AND EXACT FINITE-CENSUS
SCOPE**.

- SOURCE CORRECTION: after the accepted `L,E,F` gates, the next determinant
  residual is `F1+N+T mod 3`.  Its top rows are
  `N12={C7,D7}`,
  `Q11={C7,D6}+{C6,D7}+({UF,D7}+{C7,VF})/3`, and
  `Q10={C7,D5}+{C6,D6}+{C5,D7}+({UF,D6}+{C6,VF})/3+{UF,VF}/9`.
  The divisions are exact over the integers, with nonzero controls
  `2*x^5*y^6` and `x^5*y^5`.  No other divided term can reach degrees
  12--10.
- QUARANTINE: the old pure-bracket degree-11 count `602343` and completion
  count `439108047`, together with the stopped pure degree-10 runner, are
  wrong-source diagnostics and may not be consumed.  The N12 row/count and
  every earlier full-C5/first-Cartier gate are unaffected.
- EXACT CENSUSES: of 1,085,103 visible predecessor states, exactly 629,115
  satisfy N12; exactly 260,847 also satisfy corrected Q11; and exactly 33,225
  of those, over 159 of 2,187 structural bases, satisfy corrected Q10.  The
  six unconstrained degree-six Frobenius spectators give exactly
  `729*260847=190157463` and `729*33225=24221025` completions at the two
  stages.  These are nested survival counts, not obstructions or lifts.
- CUSTODY: result-manifest/freeze SHA-256 pairs are
  `a9bc1277...` / `e2339110...` for the erratum,
  `a9a73b2d...` / `7f06a1b9...` for Q11, and
  `7ee3ae60...` / `e73b854b...` for Q10.  Their frozen verify scripts were
  executed on Box02 and returned rc zero with terminal PASS strings; stdout
  SHA-256s are `969b7bb1...`, `dc9ada96...`, and `ad380ca3...`, with empty
  stderr.  An independent one-shard corrected monolithic run also returned
  rc zero (stdout SHA `6e303e3a...`), reproducing N12 count `629115` and
  ordered stream SHA `0fa6cb58...` byte-for-byte against the unaffected old
  prefix, while giving corrected Q11 count `260847` and ordered stream SHA
  `93e7298a...`.  This closes the review's named monolithic-agreement debt.
- SCOPE/NEXT: degree nine and below, canonical carry/state sufficiency there,
  recurrence, all-depth lifting, bounded support, collision preservation,
  characteristic-zero polynomial algebraization, a counterexample, and JC2
  remain open.  The licensed successor is the exact affine-Kuranishi/
  Cartier-cokernel transition on the frozen Q9 solution fibres, not literal
  enumeration of their trillions of completions.

## AS F-ONLY D7 Q9 SOURCE-STATE GATE (2026-08-25, DIFFERENT-MODEL-CONFIRMED CANONICAL-REPRESENTATIVE TIER)

`xmodel/as-fonly-d7-vertical-q9-source-state-gate-20260825.md`
(SHA-256
`6fb2ce4bcea7ab35102ca60198509f99b1bc1c058dea4181d87641f56ce847ae`)
with hostile review
`xmodel/as-fonly-d7-q9-source-state-review-claude-20260825.md`
(SHA-256
`ab0c98be9a5793213d2273695162b29f7391837f83d445d38ac016ffe21cee0c`):
**CONFIRMED FOR THE DISPLAYED CANONICAL-INTEGER Q9 EXTENSION PROBLEM AND
EXACT FINITE CENSUS**.

- SOURCE/STATE: the complete degree-nine row is
  `G9=M9/3+{C,D}9+T9`,
  `T=A*Z_y+W_x*V_y-U_y*Z_x-W_y*V_x`.  Together with `E1`, `E3`, and `F6`
  this gives 23 affine rows in 32 restored coefficients
  `C2,D2,C4,D4,W7,Z7`.  The single-Frobenius term
  `({UF,D5}+{C5,VF})/3` is included automatically by forming `M` over the
  integers; no other divided term can reach degree nine.  Every division is
  exact before reduction.
- EXACT CENSUS: among the 33,225 corrected-Q10 states, 11,881 are compatible
  and 21,344 incompatible.  Compatible rank/fibre counts are
  `6615` at rank 13/fibre `3^19`, `2106` at rank 15/fibre `3^17`, and
  `3160` at rank 16/fibre `3^16`, over 79 of 2,187 structural bases.  The
  relevant completion total is `8096356425843`; restoring the six proven
  spectator Frobenius coefficients multiplies it exactly by 729 to
  `5902243834439547`.
- NONEMPTY CONTROL: the reviewer hand-checks, independently of the AWS
  census, the compatible state `c5_5=2` with restored `w7_7=2`, rank 13 and
  fibre `3^19`.  This is nonemptiness of the displayed finite extension
  problem, not an all-depth survivor.
- WORDING ERRATUM: immutable producer wording is corrected by
  `xmodel/as-fonly-d7-q9-source-state-wording-erratum-20260825.md`
  (SHA-256
  `dd607ad56bb43b358e9a9cbda1d82abd5903038bb41bb545a4153b3e1466f2a4`).
  Spectator-freeness is proved by typed support, not a new-band runtime
  assertion; `M9/3` integrality is inherited from the D98 degree-nine rows
  with `KFdiv9=0`, not caused by the corrected-Q10 row.  Neither correction
  changes a row, division, rank, count, witness, or scope.
- CUSTODY: the result manifest/freeze hashes are `06b7c540...` /
  `97755c63...`.  After a deliberately preserved first deployment missing
  its transitive source closure failed closed, the complete closure was
  shipped to Box02; `verify_frozen_results.sh` returned rc zero, terminal
  `PASS-Q9-FROZEN-HASH-AND-AGGREGATE-CHECK`, stdout SHA `09a44521...`, and
  empty stderr.
- SCOPE/NEXT: the theorem uses the frozen canonical-integer representative
  convention.  Degree eight and below, representative-independent state
  sufficiency, recurrence, all-depth lifting, bounded support, collision,
  characteristic-zero algebraization, counterexample, and JC2 remain open.
  The licensed successor is the affine-Kuranishi obstruction on whole Q9
  solution fibres.

## AS F-ONLY D7 FIRST PREDECESSOR COMPLETE Q9/Q8/Q7 FIBRE EXCLUSION (2026-08-25, PRODUCER-EXACT / INDEPENDENT PROOF-CHECK; SOURCE-COMPILER REVIEW PENDING)

`xmodel/as-fonly-d7-first-predecessor-full-q9-rawq7-exclusion-20260825.md`
(SHA-256
`fe32d0bf3a3451546f9bfc77cc0a7e107e82b2bc834a4a6311919e002f2b6530`):
**PROVISIONAL EMPTY CLAIM FOR THE COMPLETE 19-TRIT Q9 FIBRE OVER THE FIRST
Q9-COMPATIBLE CORRECTED-Q10 PREDECESSOR ONLY; THE DRAT CHECK VERIFIES THE
EMITTED CNF, NOT YET THE SOURCE-TO-FORMULA COMPILER**.

- EXACT SCOPE: in the frozen 30-coordinate predecessor ordering, fix
  `c5_5=2` and every other predecessor coordinate to zero.  There is no
  assignment over `F_3` to all 19 Q9-kernel coordinates, all 32 raw Q8
  restoration digits, and all 18 raw Q7 restoration digits satisfying the
  23 explicit Q9 rows, 22 explicit Q8 rows, 19 explicit Q7 rows, and 46
  terminal coefficient rows in total degrees 9--12.  The Q9 matrix has rank
  13 in 32 restored coefficients, so this is the complete affine Q9 fibre,
  not the earlier 13-trit Q8-compatible subchart.  Q8 and Q7 remain raw:
  there is no fixed-RREF-section, zero-section, or representative
  extrapolation premise.
- SOURCE/CERTIFICATE: the formula reimposes all 23 Q9 source rows as a
  self-audit, uses exact divided-carry constraints with 32-bit residues
  modulo 729, and inherits the hash-pinned reviewed raw-Q7 circuit.  Boolector
  1.5.118 returned UNSAT.  Pinned Z3 4.16.0 bit-blasted the same SMT payload
  (SHA `0061e1cc...`) to a 6,184,696-variable, 29,430,517-clause CNF (SHA
  `a25c7ed0...`); CaDiCaL 1.7.3 emitted DRAT SHA `b8dbb064...`, and independent
  `drat-trim` returned `s VERIFIED` with 67,643 core clauses, 883 core lemmas,
  6,570,804 resolution steps, and zero RAT lemmas.
- POSITIVE CONTROL: deleting the terminal rows makes the embedded prior point
  SAT.  Direct integer replay then verifies all 23/22/19 source rows,
  recursive-versus-literal `/243` agreement, and exactly one nonzero terminal
  coefficient.  Thus neither the source equations nor the accepted chart are
  accidentally inconsistent.
- CUSTODY: case manifest/freeze SHAs are
  `827f2d28004feae007bea0a50868755e94f921d05a720df6e21fa543afdeed35` /
  `3864e7883e9edc899cc18be8ad9516eb5bef4a24fdf8876753db2cce3efad8bf`.
  The oversized full-custody archive is identified by SHA-256
  `601076db6aa5f27e74315657baf7c5a87c2ad64982011612064ee26c1c3f5649`.
- REVIEW/COVERAGE/REFUSAL: the frozen report itself remains `PROVISIONAL
  PENDING DIFFERENT-MODEL SOURCE/COMPILER REVIEW`.  Conditional on that
  review, this kills exactly one of the 11,881 Q9-compatible corrected-Q10
  predecessor states, with its whole Q9/Q8/Q7 fibre.  **The
  remaining 11,880 states within the same 79-base vertical problem are still
  open.**  The separate `a` and `g` endpoint families, nonreduced incidence,
  other associated-top branches, all-depth lifting, bounded support,
  characteristic-zero algebraization, a counterexample, and JC2 are outside
  scope.  The next gate is a single symbolic-predecessor formula, not 11,880
  uncoordinated certificates.

## AS F-ONLY D7 FIRST Q9-WITNESS TO Q8 KURANISHI OBSTRUCTION (2026-08-25, DIFFERENT-MODEL-CONFIRMED POINTWISE TIER)

`xmodel/as-fonly-d7-q9-witness-q8-kuranishi-pointwise-20260825.md`
(SHA-256
`0227176cf1f257c0b8981bea0de0b6a2a169763cbcb274ef9d966047c544c09b`)
with hostile review
`xmodel/as-fonly-d7-q9-witness-q8-kuranishi-pointwise-review-claude-20260825.md`
(SHA-256
`3dccb4c61414a51940d36ede271c32aa43df67a17cc965d6e05078a275e1988c`):
**CONFIRMED FOR ONE FROZEN CANONICAL Q9 ASSIGNMENT ONLY**.

- EXACT TRANSITION: at predecessor `c5_5=2` and Q9 assignment `w7_7=2`,
  with every other charged coordinate zero, the 22-row Q8 transition in 32
  restored coefficients has accepted/full rank pairs `(13,13)` / `(13,14)`,
  a 19-dimensional accepted-image kernel, Kuranishi rank zero, and cokernel
  dimension nine.
- OBSTRUCTION CERTIFICATE: the left-null vector `e_21`, the `x^8` row of
  `G8`, annihilates the whole coefficient matrix and pairs to `2` with the
  RHS.  Independent reconstruction reduces the entire bad row to the
  undivided term `T8=14*x^8=2*x^8 mod 3`; the plus-one orientation control
  pairs to zero.  The matrix/RHS hashes are `addcbc1e...` / `f2c3b732...`.
- REQUIRED DISCLAIMER: this does not kill the 19-dimensional Q9 fibre.  The
  reviewer explicitly exhibits the compatible point `w7_7=1,z7_6=1` and
  derives the affine obstruction formula on the fibre.  The later producer
  computation of its 13-dimensional zero locus is therefore a successor,
  not part of this pointwise promotion.
- CUSTODY: result manifest/freeze SHAs are `c68c43d...` / `7dde1c07...`.
  The review's staged independent checker ran on Box02 with rc zero, stdout
  SHA `03a0aacf...`, and empty stderr, reproducing the matrix/RHS and every
  rank/certificate assertion.
- SCOPE/NEXT: other points of the same fibre, other Q9 fibres/rank classes,
  Q8 state sufficiency, lower carries, recurrence, all-depth lifting,
  bounded support, characteristic-zero algebraization, a counterexample,
  and JC2 remain open.

## AS F-ONLY D7 FIXED Q9/Q8 BRANCH TERMINAL (2026-08-25, DIFFERENT-MODEL-CONFIRMED FIXED-BRANCH TIER)

`xmodel/as-fonly-d7-q7kernel-next-high-carry-exclusion-20260825.md`
(SHA-256
`cc2cf6417c5d27d5868bc86a6b2d02aac10a2b4976d9548a9d01bc5584db0172`)
with hostile review
`xmodel/as-fonly-d7-q7kernel-next-high-review-claude-20260825.md`
(SHA-256
`02d1c6f2cde4840541df7ef2cd9ff194e753ca205f33dd0cf81fd4c101ccf7ae`)
and nonmutating review erratum
`xmodel/as-fonly-d7-q7kernel-next-high-review-erratum-20260825.md`
(SHA-256
`456b9261a2b5d9a93dcbbbfd3fc791a4d987712276bef48cdfdcb4556cb03da4`):
**CONFIRMED TERMINAL BELOW THE DISPLAYED FIXED PREDECESSOR AND Q9/Q8
POINT**.

- FIXED STATE: the predecessor is `c5_5=2` with its other 29 coordinates
  zero; the canonical Q9 survivor is `w7_7=z7_6=1`, equivalently
  `W7=x^7,Z7=x^6*y`; the Q8 restored vector is zero.  This is one point of
  the earlier 13-dimensional Q8-survivor chart, not that whole chart.
- WHOLE Q7/Q6 FIBRE: the 19-row Q7 transition in 18 restored digits is
  homogeneous of rank nine.  Its exact kernel is `c6=0`, `d6_6` free, and
  `div(W5,Z5)=0`; all `3^9=19,683` states were exhausted in 27 disjoint AWS
  shards.  Every state has a nonempty nine-dimensional Q6 fibre because its
  seven-row divergence map has rank seven.
- TERMINAL CARRY: on every Q7 state the recursive source carry and literal
  `(det J-1)/243` calculation agree, with
  `R12=R11=R9=0` and `R10=x^10`.  Hand reconstruction identifies the unit as
  `C_x*Z_y=10*x^10=x^10 mod 3`.  Q6 digits enter only through the degree-at-
  most-eight `S` channel and degree-six divergence; the fixed branch's other
  unrestored lower channels likewise cap at degree eight.  No later
  cap-seven correction can cancel degree ten, so every completion below this
  fixed state is terminal.
- CUSTODY: aggregate JSON/ordered-stream SHAs are `87f63bdd...` /
  `6e4df883...`; result-manifest/result-freeze SHAs are `a1eafec7...` /
  `30754347...`.  All shard sentinels are present and stderr entries empty.
  The no-shell reviewer independently rederived the kernel, carry identity,
  Q6 degree bound, and terminality; its custody caveats do not change the
  mathematical verdict.
- SCOPE/NEXT: the thirteen other Q8-chart directions and their interactions
  with Frobenius spectators, other Q9 predecessors, representative/carry
  translation, the full cap-seven system, all-depth lifting, bounded support,
  collision, characteristic-zero algebraization, a counterexample, and JC2
  remain open.  The producer-exact global unreduced affine-chart map is a
  successor and is not promoted here.

## TD6 FIXED TWO-CENTER SECTION `(C,1,U)` EMPTY (2026-08-25, DIFFERENT-MODEL-CONFIRMED FIXED-SECTION TIER)

`xmodel/td6-c1-c3-two-center-cover-gate-20260824.md`
(SHA-256
`2ada2d70fbdb9db2cf6d93c3b8d3ba0b1f19be1dd5530365a0b3b235e230fbd6`)
with hostile review
`xmodel/td6-c1-c3-two-center-cover-review-claude-20260825.md`
(SHA-256
`56c4ece1224c723f8bbe107f0c9af6776dc0affcb03923a394628838923bde19`)
and AWS custody supplement
`xmodel/td6-c1-c3-two-center-cover-review-aws-custody-20260825.md`
(SHA-256
`2ca099947a7b53508a98b73a903c9a46b80cde83f81fdb925c3b139d1a331dd1`):
**CONFIRMED EMPTY AT THE FROZEN FIRST-BAND/P12 GATE OVER EVERY FIELD
EXTENSION OF `Q`**.

- SOURCE TYPE: the centering jet is
  `x=C*s+s^2+U*s^3+t*s^4` with `t` retained as a system unknown, and all
  transport patterns, rhs normalization, pole data, and original 28-row
  source typing are frozen.  `c2=1` is a restriction, not a proved gauge;
  `c2=0` and general `c2` are not covered.
- OPEN COVER: with `H=C-3U^2`, the locus `U*H!=0` is covered by generic and
  B-local original-row certificates whose chart factors use polynomials
  `B,T`; the exact resultant `Res_C(B,T)=64U^10` leaves no shared zero off
  `U=0`.  Both genuine P12 reductions are the unit `-k/50` in the frozen
  coefficient field.
- EXCEPTIONAL DIVISORS: all of `U=0` is first-band-inconsistent, including a
  raw unit-chart rebuild at the origin.  On `H=0`, the raw certificate applies
  off `U*P(U)` for `P=128U^6-32U^3+1`; `P` is irreducible and squarefree,
  and the direct rebuild over `Q[U]/(P)` has certified inversions and the same
  unit remainder `-k/50`.  The intentionally failing V6 denominator contains
  `P` and is retained as the negative control; V7 works in the quotient and
  never divides by `P`.
- CUSTODY: the producer manifest SHA is `e3af7ba9...`.  The no-shell review's
  independent probe was executed on Box03 after only a harness repair that
  selects the payload directory rather than a macOS AppleDouble entry.  It
  returned rc zero; 108 explicit PASS checks plus four INFO lines and a final
  `PROBE PASSED` occupy 114 stdout lines.  Probe/stdout/time-stderr SHAs are
  `af2b9164...` / `5dbd5025...` / `d2c1ae07...`; the custody manifest/freeze
  hashes are `feebc1b3...` / `8c503ad5...` and verify.
- SCOPE/NEXT: this kills one fixed normalized two-parameter section only.
  Simultaneous general centers, the `c2=0` boundary, other dead-stretch/
  boundary/F1/pole moduli, full TD6, SP-2, a landing theorem, a maximum-degree
  theorem, and JC2 remain open.  The active trivariate `(C,V,U)` atlas and
  universal-adjoint test are successors, not consequences already proved.

## TD6 FIXED THREE-CENTER `H=P3=0` RAW CURVE EMPTY (2026-08-25, DIFFERENT-MODEL-CONFIRMED FIXED-SECTION TIER)

`xmodel/td6-c1-c2-c3-p3-raw-curve-aws-20260825.md`
(SHA-256
`a15c85c5bfd2a4219c2f7540b5e2577f5af123c18b40483a2749118c5ac2bcab`)
with hostile review
`xmodel/td6-c1-c2-c3-p3-raw-curve-review-claude-20260825.md`
(SHA-256
`def9c7392f156b88252e5f143af505aa684e1135bc99b7beb5ff203d2238788c`)
and terminology erratum
`xmodel/td6-c1-c2-c3-p3-raw-curve-erratum-20260825.md`
(SHA-256
`c40a508382ec369c0bf5e7cc38f2d2c0246467dbfc633403409f9c999f4bc8df`):
**CONFIRMED EMPTY ON THE WHOLE SET-THEORETIC `H=P3=0` RAW CURVE OF THE
FIXED SOURCE-TYPED THREE-CENTER SECTION**.

- FUNCTION FIELD: with `H=C-3U^2` and
  `P3=V^4-32V^2U^3+128U^6`, the tower
  `Q(U)[Z,V]/(Z^2-32Z+128,V^2-ZU^3)` is a degree-four field and equals the
  function field of the irreducible curve `P3=0`; no component or nilpotent
  adapter is lost.
- EXACT OBSTRUCTION: two exact pivot orders give transport rank
  `3470/3602`, first-band rank `38/132`, and genuine P12 remainder `-k/50`.
  Their original-row lifts use respectively 28 rows/1,540 terms and 38
  rows/2,152 terms, with plus-one controls.  All cleared certificate divisors
  are powers of `U`, with complete charts `U^17` and `U^19`, so every point
  of the curve off `U=0` is excluded over every field extension of `Q`.
- COMPLEMENT: `P3(0,V)=V^4` and `H(0,C)=C`, so the set-theoretic complement
  is the raw origin.  Its separately frozen 21-original-row unit-chart
  certificate is transport-band incompatible.  The immutable producer
  called it first-band incompatible; the cited erratum corrects only that
  mechanism label and strengthens neither the set nor the conclusion.
- COMPOSITION/CUSTODY: together with the previously frozen `H=0` open,
  `V=0`, `U=0`, and origin strata, this removes the remaining raw `H=0` debt
  of this fixed section.  Producer manifest/freeze SHAs are `95869889...` /
  `ddbf7dff...`; the ascending/reverse stdout SHAs are `c38471a0...` /
  `900c3829...`.  A second readable-source hostile review
  `xmodel/td6-c1-c2-c3-p3-raw-curve-source-review-claude-20260825.md`
  (SHA-256
  `8a3a67d4007efda38bf4ad0223c576b5f470ddef3218514932751e15fb3b8148`)
  read the full 24-file import closure and independently confirmed the
  quotient tower, source replay, denominator logic, origin certificate, and
  H-cover.  Its only caveats are evidentiary and do not change the verdict.
- SCOPE/NEXT: raw `B3`, a neighborhood in center space, a gauge covering
  `c2=0` or arbitrary centers, boundary/dead-stretch moduli, full TD6, SP-2,
  a landing theorem, maximum degree, and JC2 remain open.  The active exact
  `B3` divisor atlas is a successor, not part of this promotion.

## SELECTED-Q8 NO-MERGER DRAFT REFUTED AND REPAIRED (2026-08-25, CORRECTED ABSTRACT LEMMA DIFFERENT-MODEL-CONFIRMED)

The conditional producer lemma
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`
(SHA-256
`ef0119505d3378781f75fcefd9febe3efb0581e1d7b5c7009c900d251a653170`)
is superseded by the nonmutating erratum
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-erratum-20260825.md`
(SHA-256
`ed7bf01a1d87bf2e0733be8cc0f3d5d8a6b10f13743de8fd1d38e4cb1061a194`),
whose independent hostile review is
`xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-erratum-review-claude2-20260825.md`
(SHA-256
`cc722b523e4d7111724f236fe56ed9815e47618b7f12425a55442b3ebcc63de8`):
**THE ORIGINAL ABSTRACT LEMMA IS FALSE AS WORDED; THE CORRECTED ABSTRACT
LEMMA IS CONFIRMED, WHILE ITS GLOBAL Q8 APPLICATION REMAINS UNDISCHARGED**.

- COUNTEREXAMPLE: over `R=k[[pi]]`, the scheme
  `Spec R[x,y,z]/(xz,yz,pi*xy)` has reduced special fibre
  `V(z) union V(x,y)`, a plane plus a line `C`.  At the origin `C` is the
  unique one-dimensional component, and the total scheme is flat/reduced at
  `eta_C`; nevertheless the generic fibre is the union of three distinct
  coordinate axes, and the closures of two of them contain the origin.  A
  higher-dimensional vertical component invalidates the producer proof's
  local-containment step.
- REPAIR: require `C` to be the unique irreducible special-fibre component
  through each marked point **in every dimension**; more strongly, in the
  intended application one may prove that the full source special-fibre local
  ring is a regular one-dimensional local ring.  With that hypothesis, each horizontal
  curve closure contains `eta_C`; at `eta_C`, flatness plus reduced special
  fibre makes the local ring a one-dimensional domain, so only one horizontal
  generic component can dominate `C`.
- WORDING: use scheme-theoretic closure, not “integral closure inside X.”
  Normalization is unnecessary and is not generally a closed subscheme of
  `X`.  The first hostile CLI attempt produced no report because its response
  exceeded the configured output limit and remains failed closed; the cited
  second review independently verified both the counterexample and every
  commutative-algebra step of the repair.
- Q8 EFFECT: the separately reviewed arithmetic contact bridge now supplies
  full contact coordinates, scheme identity, regular one-dimensional contact
  completions, and integral specialization of the eight local branches.  It
  does not by itself prove that the `H`-supported special component is
  generically reduced/multiplicity one or that all eight closures dominate
  that same component.  Those remaining checklist items still block the
  global no-merger application.  No all-eight component lift,
  selected-trajectory exclusion, maximum-twelve theorem, or JC2 theorem is
  promoted by this abstract lemma.

## SELECTED-Q8 `b=1` SLOPE-TWO NEXT-ORDER CONTROL (2026-08-25, DIFFERENT-MODEL-CONFIRMED ROUTING TIER)

Producer report
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-b1-slope2-next-order-control-20260825.md`
(SHA-256
`4f1f4b66abb57bb8c912427359e86f4e54b6563f8a7ae31f5d64bcaba656095f`)
and hostile review
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-b1-slope2-next-order-control-review-grok-20260825.md`
(SHA-256
`6bf95a6ebdc12d39020b00b60933bab100315834cd8385ac57a70448e490347e`):
**CONFIRMED ONLY FOR THE NORMALIZED UNRAMIFIED `x5=t` FIRST-JET FAMILY**.

- At the selected leading cone over `(d2,d4)=(2,1)`, the exact substitution
  `x5=t`, `x3=5t/3+X2t^2`, `x1=U2t^2`,
  `w=-4t^2/9+W3t^3`, with first jets of `c,d4,u`, makes every leading row
  vanish.  The next odd equations reduce to three affine equations whose
  first two force `Q1=-16/27` and `c-6B1+9U2=11/9`; the third differs by the
  nonzero constant `108`.  Hence the next-coefficient ideal is `(1)` for
  every finite `c` in this strict chart.
- Box02 `std/dp` and Box03 `slimgb/block` agree exactly.  Frozen
  manifest/freeze/replay-output SHAs are `39275137...` / `9ab69a8d...` /
  `717620e4...`.  Review-run SHA is `57ef0139...`; its custody note discloses
  a faithful substantive transcription from two streamed adapter chunks,
  rather than a byte-identical raw-stdout file.
- FIREWALL: this kills no mixed-order or ramified/Puiseux arc, earlier
  coefficient drift, moving-`d4` pointed germ, full horizontal saturation,
  coefficient infinity, terminal/Taylor realization, trajectory, full
  `(9,12)`, maximum-twelve cell, or JC2.  The full pointed moving-`d4`
  saturation and coefficient-projective chart remain decisive.
