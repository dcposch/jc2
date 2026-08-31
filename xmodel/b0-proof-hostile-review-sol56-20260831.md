# Hostile review: B0 proof report

## 0. Verdict key and review scope

The three frozen inputs were hashed before they were read.  All three SHA-256
values match the charge exactly:

```text
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  b0-trivial-dicritical-proof-opus5-20260831.md
264ddba858b0eb54544fbf612a390c5ded9bd07eb37729b2700965015e369462  trivial-dicritical-literature-registry-grok46-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

`CONFIRMED` means the displayed proof establishes the stated claim at its
declared scope.  `REFUTED` means a specific inference is false.  `GAP` means
the conclusion may be true but the cited hypotheses or argument do not prove
it.  I defaulted to `REFUTED`, rederived every load-bearing identity, and did
not inspect `jc2-lean`, alter a charged input, or run a CAS.

## 1. Custody and promoted-input audit

The construction (`Y=Spec B`, normality, finite flat `q`, open `U`, pure
boundary), four boxes and per-component `a_D>=1`, the smooth-stratum covering
lemma, `e_j=1+v_j(dx wedge dy)`, the `chi_c` toolkit, and `(E)` are used at
exactly the scopes promoted in integration §1.  The reducible Euler
calculation starts from the promoted *aggregate* identity, not illicit
componentwise copies.  Proposition 4.1's purity use is separately checked in
§6 below.

The custody exceptions are:

- **`A_F=B` — CONFIRMED not consumed.**  It is mentioned only as a possible
  downstream consequence of closing the residual OPEN.
- **H2 — the §6 "not consumed" wording is REFUTED literally.**
  Irreducibility is an explicit hypothesis and is essential in Lemma 3.4,
  Theorem 3.5, Corollary 3.7, Theorem 4.2, and Corollary 5.1.  This is not an
  illicit import, but it is consumption as a stated assumption.
- **H3 — GAP in Theorem 4.2's `(M)` sentence.**  The displayed B0 proof does
  not use H3, but `(M)` does.  Add H3 or the Orevkov/Chau affine-line bridge
  given in §7.
- **`b=0` and `f(z)=2` — CONFIRMED not assumed.**  The former is derived
  after all `mu=1` primes are excluded; `a=2` follows from
  `a+2s_1=4`, so the census value is unused.
- The report's line 57 citation to integration "§9" is wrong; the dictionary
  `e_j=mu_l, delta_j=s_l, a=f(z)` is recorded at integration lines 114–117.
- The promoted covering lemma does not say that contracted `L_C` points can
  occur only over `Sing A_F`; report lines 437–438 exceed its scope.  The
  direct Orevkov-model repair in §7 is needed instead.

Thus the flagship B0 exclusion under explicit H2 has clean custody.  The
claims of H3-free `(M)` and of a promoted source for the `epsilon_p`
bookkeeping do not.

## 2. Primary-literature verification

The five reopened files have the report's hashes:

```text
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7  refs/chau1999_apm71_full.pdf
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3  refs/do.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
```

- **[O-4.2] — CONFIRMED.**  `jc86.pdf` p. 7, with the algebra continuing on
  p. 8, gives the exact `N-1` equality, finitely many nonnegative jumps, and
  equality in Corollary 4.3 precisely when every affine quotient point has
  `mu_x=mu_l`.  Orevkov indexes `x in pi(l)-{infinity}`.  The report's initial
  definition over `x in l'` is ill-typed unless it writes
  `mu_{pi(x)}f*` or explicitly identifies the quotient points.

- **[O-5.2] — CONFIRMED.**  Statement on p. 8 and proof on pp. 8–9 require
  only the pointwise equality `mu_x f*=mu_l f*` at the selected quotient
  point.  No global `corr_l=0` hypothesis occurs.  Global vanishing is a
  valid sufficient condition for applying it everywhere.  The conclusion is
  exactly a nonsingular local embedding of the restriction to `l`.

- **[O-5.3] and [O-Rem] — CONFIRMED only when separated.**  Lemma 5.3 on
  p. 9 assumes `N>2`, the whole `L_F` is the single `l`, and
  `mu_l=N-1`; it proves biregularity onto a nonsingular affine curve.  The
  componentwise prohibition is asserted only in the unproved closing Remark
  on p. 10.  Corollary 3.8 supplies an independent proof.

- **[Z-6.5b] — CONFIRMED, with a missed consequence.**  Printed p. 457/PDF
  p. 27 (proof on printed p. 458/PDF p. 28) gives jump iff a critical point
  of the immersed parametrization, and separately `mu_D=1` implies that
  parametrization is smooth.  Its convention ignores *all* intersections of
  smooth local branches, not just transverse ones.  Therefore, under the
  report's claimed on-the-nose dictionary, `mu_D=1` forces `corr_D=0`.  This
  refutes one of the two claimed surviving rank-five profiles.  Żołądek's
  statement is stronger than Orevkov 5.2, not equivalent to it "on the
  nose."

- **[Z-6.7] — CONFIRMED.**  Printed p. 458/PDF p. 28, completed on p. 459/29,
  gives `mu_D=l-k`; direct differentiation restores the suppressed unit
  `-k` in `Jac theta~= -k v^(l-k-1)`.

- **[C-3.1] — CONFIRMED.**  The setup is printed p. 293/PDF p. 7 and the
  chain-rule formula is p. 294/8.  The raw determinant identity is algebraic
  and remains valid for a dicritical series even though the surrounding
  Lemma 3.1 comparison assumes `a_phi+b_phi>0`.

- **[C-3.6ii] — CONFIRMED, page pin corrected.**  The theorem starts on
  printed p. 296/PDF p. 10, but item (ii), `a_phi=b_phi=0` and the degree
  ratio, is on printed p. 297/PDF p. 11.

- **[C-4.4] — CONFIRMED; the report's scope gloss is REFUTED.**  The
  statement is printed p. 304/PDF p. 18 and proof p. 305/19.  Its theorem
  assumes Keller plus monicity in `y`; Jung supplies `d>e>1` inside the
  proof.  That condition is not an extra hypothesis.

- **Chau 2004 and Domrina–Orevkov.**  Chau's Lemma 1 (arXiv/PDF p. 4)
  confirms both directions of the dicritical-series cover of `A_F`, and
  Theorem 1 (p. 2) gives polynomial parametrizations used in the optional H3
  repair above.  `do.pdf` p. 6 really prints the unique-dicritical
  `mu=1 =>` unbranched slogan, but Orevkov's budget does not justify it when
  corrections remain; the report correctly does not consume that inference.

- **AMS usage — mathematically CONFIRMED, strict primary custody GAP.**
  Orevkov p. 10 and Chau p. 305 state the needed rectification/divisibility
  forms.  Once the charged proof has a smooth closed `A^1`, its use and the
  resulting cyclic complement group are correct.  The original
  Abhyankar–Moh or Suzuki paper is not among the five hashed PDFs.

The charged report's claim that all citations use local PDF page numbers is
therefore false for both journal scans; the printed/PDF pairs are recorded
above.

## 3. Propositions 2.1–2.3: chart dictionary and Route 1

1. **Proposition 2.1 — CONFIRMED after a terminology correction.**  In Chau's
notation the parameter term is
`xi*x^(1-n_phi/m_phi)=xi*t^(n_phi-m_phi)` after `x=t^(-m_phi)`.
Thus
`det D Phi=-m_phi*t^(n_phi-2m_phi-1)`.  After exchanging the two source
coordinates in Żołądek's alteration,

```text
(k,l,v,u)=(m_phi,n_phi-m_phi,t,xi),   l-k=n_phi-2m_phi.
```

The gcd normalizations agree because replacing `n_phi` by `n_phi-m_phi`
does not change their gcd with `m_phi`.  These are the same *alteration
formula*.  Żołądek's map is not necessarily an honest local-coordinate chart
(his Remark 6.4 records its factorization through a ramified quotient), so the
report should not call the two objects literally the same chart without that
qualification.

2. **Proposition 2.2 — CONFIRMED.**  Put local target coordinates `(w,tau)`
with `D_l={tau=0}`.  At a generic point,
`tau o F_phi=t^mu u`, with `u` a unit, while
`partial_xi(w o F_phi)` is a unit.  Hence

```text
d(w o F_phi) wedge d(tau o F_phi)
  = unit*t^(mu-1) dt wedge dxi + higher t-order,
```

so `ord_t det D F_phi=mu_l-1`.  Chau's chain-rule identity then gives
`mu_l=n_phi-2m_phi=l-k`.  Theorem 3.6(ii), printed p. 297 (PDF p. 11),
makes both components of `F_phi` holomorphic at `t=0`; therefore the exponent
is nonnegative.  For `mu_l=1` the displayed determinant is the nonzero
constant `-m_phi J`, and conversely a nonvanishing determinant on `t=0`
forces exponent zero.  Thus the alteration map `F_phi` is locally
biholomorphic at every point of that parameter line exactly when `mu_l=1`.

3. **Proposition 2.3 — REFUTED as a theorem about Route 1.**  The calculation
does prove only that the *order and gcd data* leave the numerical choice
`l=k+1` (`gamma=l/k=1+1/k`) unobstructed.  It does not prove that the Keller
hypothesis is "fully consumed": the identity `det D F_phi=constant` imposes
coefficient equations at every order, and compatibility with a global
polynomial map, dicriticality, the other valuations, and the quotient chart
has not been realized.  Exhibiting admissible integers is a floor, not an
attainment theorem.  Safe replacement: **the single Jacobian-order/gcd
argument cannot close B0 by itself**; no conclusion about all one-chart or
valuative arguments follows.

## 4. Lemma 3.4 and Theorem 3.5

**Lemma 3.4 — CONFIRMED (one omitted equality argument supplied).**  Let
`S=Sing D`, `s=#S`, `nu=sum(r_p-1)`, and let the normalization be
`P^1` minus `c>=1` points.  Then

```text
chi_c(D)=2-c-nu,             chi_c(D-S)=2-c-nu-s,
chi_c(F^-1(D))=a chi_c(D-S)+sum_{p in S} a_p.
```

Substitution in `(E)` gives, with no sign change,

```text
(N-a) chi_c(D-S) = N-1-Ns+sum a_p,                         (3.1)
(N-a)(2-c)-(N-a)nu+as = N-1+sum a_p.                       (3.2)
```

Here `N-a>0` because a generic point of `D` has at least one boundary
preimage.  If `D` is smooth, (3.2) is
`(N-a)(2-c)=N-1`; since `c>=1`, this forces `a=1,c=1`.
In branch (ii), Orevkov 5.2 gives `nu>=s`.  With `c>=1`, (3.2) implies

```text
(a-1)+(N-2a)s+sum a_p <= 0.                                (3.3)
```

All terms are nonnegative exactly where the report says: `a>=1`,
`2a<=N`, and `a_p>=0`.  Hence `a=1,s=0,sum a_p=0`.  The text's phrase
"`s=0`, hence `nu=0`" is not by itself valid; equality in both preceding
bounds (or (3.2) with `a=1,s=0`) supplies `c+nu=1`, hence `c=1,nu=0`.
Both branches therefore yield a smooth `D isomorphic to A^1`.  This also
pinpoints the genuine use of `2a<=N`: it is solely the sign of
`(N-2a)s` in (3.3).

**Theorem 3.5 — CONFIRMED.**  Once Lemma 3.4 gives `D=A^1`, AMS rectifies
the closed embedding, so `pi_1(C^2-D)=Z`.  The branch locus is nonempty and
is a union of components of the irreducible `A_F=D`, hence `Br=D`.
The open subset `q^-1(C^2-D)` of irreducible `Y` is connected, so its
degree-`N` monodromy is transitive.  Since the base group is generated by
one meridian, its image is the cyclic group generated by that single
permutation; transitivity forces that permutation to be an `N`-cycle.
The generic fibre formula, however, gives it `a=1` fixed point.  This is a
direct contradiction.  No assertion that an arbitrary curve-complement
group is generated by one meridian is being used; that fact enters only
after AMS has made the curve a line.

## 5. Corollaries 3.6–3.8

- **Corollary 3.6 — CONFIRMED as a consequence of Theorem 3.5.**  The
  campaign degree floor supplies `N>=3`.  The advertised scope comparison is
  **REFUTED**: Chau 4.4 states singularity for every component under its
  Keller-plus-monic hypotheses; `d>e>1` is obtained inside Chau's proof by
  Jung, not imposed as an extra hypothesis.  This is a useful independent
  AMS/monodromy proof, not a stronger theorem than Chau 4.4.

- **Corollary 3.7 — CONFIRMED for irreducible `A_F`.**  Equality
  `sum mu_l=N-1` in Orevkov's budget makes every correction zero.  All
  dicriticals then dominate the same irreducible component, and
  `a+sum s_l mu_l=N` with every `s_l>=1` gives `a<=1`; the promoted lower
  bound gives `a=1` (indeed every `s_l=1`).  Thus `2a<=N`, contradicting
  Theorem 3.5(ii).  Hence `sum mu_l<=N-2`, equivalently
  `sum corr_l>=1`.  Żołądek identifies this with a critical point of an
  *immersed parametrization*.  The report's further gloss "i.e. a locally
  irreducible singularity" is **REFUTED**: a critical, nonprimitive
  parametrization can have a smooth reduced image.

- **Corollary 3.8 — CONFIRMED.**  A term `mu_l=N-1` exhausts the exact
  budget, leaving that dicritical unique and correction-free.  Its image is
  then all of `A_F`, so Corollary 3.7 applies.  This supplies the proof absent
  from Orevkov's closing Remark and does not use the Remark circularly.

## 6. Rank-four profile census and Proposition 4.1

**Profile table — CONFIRMED as the complete integer partition of the
Orevkov budget.**  The positive costs `mu_l+corr_l` sum to three, so the six
listed multisets are exactly the refinements of `3`, `2+1`, and `1+1+1`.
There is an unused stronger filter: Żołądek 6.5(b) says `mu_D=1` makes the
parametrized curve immersive everywhere and, together with its jump iff
critical-point statement, forces `corr_D=0`.  Thus rows containing `(1,1)`
or `(1,2)` already contradict the report's asserted Orevkov–Żołądek
dictionary.

**Proposition 4.1 — CONFIRMED, and it applies purity to the right object.**
The proof does not apply Zariski–Nagata purity to Orevkov's merely continuous
collapsed map `f*`.  It applies it to the promoted finite flat morphism
`q:Y->C^2`, with `Y` normal and the target regular.  Codimension-one points
of `Y` in `U` are unramified by Keller, while a boundary prime is generically
ramified exactly when its `mu_l>=2`.  If every dicritical is trivial, `q` is
unramified in codimension one; purity rules out a branch locus supported at
only the correction points.  Hence `q` is finite etale.  Since `Y` is
irreducible and `C^2` has no nontrivial connected finite etale cover, its
degree would be one.  The correction jumps of `f*` do not invalidate this
argument; rather, purity shows that such isolated jumps cannot occur without
a ramified boundary divisor in the finite model.

## 7. Theorems 4.2–4.3 and Corollary 4.4

**Theorem 4.2 — CONFIRMED for B0 and the numerical/monodromy conclusions;
GAP for `(M)` at the stated proof scope.**  Proposition 4.1 kills the three
all-trivial rows; Corollary 3.7 kills `(2,0)+(1,0)` when both images equal the
irreducible `A_F`; Corollary 3.8 kills `(3,0)`.  Thus only `(mu,corr)=(2,1)`
remains.  The generic fibre equation gives `a+2s_1=4`, hence
`s_1=1,a=2`; absence of a trivial boundary prime gives `b=0`, and the
meridian is a transposition.  A transitive group generated by transpositions
is the full `S_4`.

The displayed proof never establishes H3, whereas integration §1 promotes
`(M')`, and therefore `(M)` after `b=0`, only under H2+H3.  With
`chi~=chi_c(normalization(A_F))`, its promoted no-H3 form differs from `(M)`
by `(N-a)(1-chi~)`.  Thus the safe statement from the proof is `(M)` only
after adding H3.  There is a short source repair: Orevkov Lemma 2.1(a)–(c), in
the same hashed `jc86.pdf`, makes `l-L_infinity` an affine line; equivalently
Chau 2004 Theorem 1 polynomially parametrizes every component.  A finite
surjection from `A^1` to the normalization forces that normalization to be
`A^1`.  The report does not state this bridge, so it may not claim that H3
was "never consumed."

**Theorem 4.3(1)–(4) — CONFIRMED, with one missing sentence in (4).**  The
budget and the preceding exclusions force exactly `(2,0)+(1,0)` over
distinct components.  The generic equations give `s_1=1,a_{D_1}=2` and
`a_{D_0}=4-s_0`.  Purity gives `Br=D_1`; the connected etale cover has a
transitive image generated by conjugate transpositions, hence an `S_4`
quotient and a nonabelian complement group.  Orevkov 5.2 makes all affine
branches smooth.  At `p in Sing(D_1)-D_0`, the fibre budget forces two
branches, no affine point, and two disjoint transposition orbits.  In fact
`Sing(D_1) cap D_0` is empty: there `2 beta_p>=4` and `t_p>=1`, already
exceeding degree four.  This omitted observation is needed later.

**Theorem 4.3(5) — REFUTED as displayed.**  Even accepting its definitions
and fibre equation
`2 beta_p+t_p+a_p+eps_p=4`, expansion of the aggregate Euler identity gives

```text
2r_1+s_0c_0+sum_p(s_0k_p-t_p)-sum_p eps_p = 1+2s_0,
```

not the report's formula with `+sum eps_p`.  The claimed nonnegative-term
argument and its `c_0,r_1` conclusions therefore do not follow.  Moreover,
the promoted covering lemma concerns affine preimages; it does not license
the report's separate assertion about contracted `L_C` boundary points.

There is a stronger safe replacement directly in Orevkov's model.  Lemma
2.1 says each finite-value boundary chain has one `L_F` component meeting
`L_infinity` once; contraction of its `L_C` chain produces a point already
on `pi(l)`, not an additional fibre point.  Thus no separate `eps_p` occurs.
Also the original smooth curve `l_i-L_infinity` is `A^1` (the quotient image
need only be viewed topologically here).  Its finite map to the image
normalization is a polynomial map `A^1->A^1`; because `corr_i=0`, Orevkov 5.2 makes it
unramified at every finite point, so its degree is one.  Consequently

```text
s_0=s_1=1,  a_{D_0}=3,  a_{D_1}=2,
normalization(D_0)=normalization(D_1)=A^1,
2r_1+c_0+sum(k_p-t_p)=3,
```

and in fact `r_1=c_0=1` and `t_p=k_p`.  This source-based repair removes the
charged report's `C^*` and `s_0=2,3` alternatives.

**Corollary 4.4 — CONFIRMED conditionally as written, and unconditional in
the repaired residual structure.**  With `r_1=1`, smoothness of `D_1` would
make it a closed embedded `A^1`; AMS would give cyclic complement group,
contrary to the `S_4` quotient.  The preceding disjointness observation puts
every singular point of `D_1` under part (4), so the asserted double-branch
description follows.

## 8. OPEN typings and the rank-five claims

**`OPEN[B0-N4-REDUCIBLE-PI1]` — GAP as "exactly" typed, but its implication
is correct.**  If every curve in the report's broad class had abelian
complement, Theorem 4.3(3) would contradict the required `S_4` quotient and
would close B0 at `N=4`; the same then excludes additional `A_F` components
and closes the transposition horn.  The representation-specific weakening is
also valid: every meridian maps to a transposition, and the two branch
meridians at each singular point map to disjoint transpositions.  The report
omitted, but the degree-four fibre budget proves, that no singular point of
`D_1` lies on `D_0`.

It is not the exact residual stated there.  The source repair above forces
`normalization(D_1)=A^1`, not `A^1 or C^*`.  The sharp acquisition is:

> Can an irreducible polynomial plane curve normalized by `A^1`, whose every
> affine singularity consists of exactly two smooth (not known transverse)
> branches, have an `S_4` quotient in which a branch meridian is a
> transposition and the two local meridians are disjoint transpositions?

Full abelianness is sufficient but stronger than necessary.

**`OPEN[B0-GENERAL-N]` — OPEN remains, but its `N=5` census is REFUTED.**
Under H2, Corollary 3.7 and the cost-four budget force multiplicities `(2,1)`
and one correction.  The report lists the correction on either dicritical.
But Żołądek 6.5(b) forces `mu=1 => corr=0`; hence
`(2,0)+(1,1)` is impossible and only

```text
(mu,corr)=(2,1)+(1,0)
```

survives.  Without the affine-line repair its covering-degree refinements are
`(s_2,s_1,a)=(1,1,2)` or `(1,2,1)`; the repair plus `corr_1=0` forces
`s_1=1`, leaving only the first.  Arithmetic satisfiability
of the report's relaxed inequality is not an attainment result and does not
prove that only a "genuinely new" kind of input could work.

**Corollary 5.1 — CONFIRMED under H2.**  The inequalities
`2m_nt+m_triv<=sum mu_l<=N-2`, together with `m_nt>=1`, give at `N=5`
`m_nt=1,m_triv<=1`, hence `m<=2`.

**Corollary 5.2 — CONFIRMED only at `N=4` under H2.**  The B0 part of
Theorem 4.2 derives `a=2,b=0` without `f(z)=2`; the census route is therefore
obsolete for that conditional horn, not without H2.

## 9. Consistency with the integration report

**CONFIRMED, except for wording and `(M)` scope.**  Integration §2 kept the
`b=1` transposition row provisional as a numerically admissible alternative;
it did not assert existence.  Theorem 4.2 therefore *eliminates that row
under H2* rather than "refuting SHEET-GATE Theorem 4.4."  Its B0 conclusion,
the H2 rank-five improvement, and the all-degree promoted `N-1` bound are
mutually consistent.  What cannot be promoted consistently is the report's
H2-only assertion of `(M)` without either H3 or the explicit source repair.

## 10. Promotion recommendations and acquisition target

**Overall recommendation: REJECT the bundle as charged; PROMOTE the core
B0 theorem and the items explicitly retained below.**  The rank-four H2
exclusion is real.  The bundle nevertheless contains a false Route-1
meta-theorem, a sign error in its claimed complete residual structure, an
unlicensed H3-free use of `(M)`, and a false two-profile rank-five census.

| Item | Recommendation and exact scope |
|---|---|
| Proposition 2.1 | **PROMOTE** the exponent/Jacobian dictionary for the alteration formulas, after replacing “same chart” by the qualified formulation in §3. |
| Proposition 2.2 | **PROMOTE** for every affine-image map-dicritical of a Keller map. |
| Proposition 2.3 | **DO NOT PROMOTE.** Replace it by: the determinant-order and gcd data alone do not exclude `l=k+1`. |
| Lemmas 3.1–3.3 | **PROMOTE.** Purity is applied to finite `q`; Orevkov 5.2 is pointwise, with global zero correction a sufficient hypothesis. Type corrections on `pi(l)`. |
| Lemma 3.4 | **PROMOTE** for irreducible `A_F`, `N>=3`, under either its smooth branch or “all corrections zero and `2a<=N`” branch, with the equality repair in §4. |
| Theorem 3.5 | **PROMOTE verbatim** at that scope.  Its AMS/cyclic-monodromy endgame is sound. |
| Corollary 3.6 | **PROMOTE the theorem**, but delete “strengthening of Chau 4.4”; call it an independent reproof. |
| Corollary 3.7 | **PROMOTE** `sum mu_l<=N-2` under irreducible `A_F`; replace “locally irreducible singularity” by “critical point of an immersed parametrization.” |
| Corollary 3.8 | **PROMOTE** for every noninvertible plane Keller map (the promoted degree floor supplies `N>=3`). |
| Proposition 4.1 | **PROMOTE** at `N=4` (indeed its all-trivial argument is degree-independent once there is more than one sheet). |
| Theorem 4.2 | **PROMOTE** under `N=4` and H2: no `mu=1`, unique `(2,1)` cost profile, `s_1=1,a=2,b=0,(delta,e)=(1,2)`, meridian a transposition, global group `S_4`.  Assert `(M)` only with H3, or insert and cite the checked affine-line-normalization lemma. |
| Theorem 4.3(1)–(4) | **PROMOTE**, adding `Sing D_1 cap D_0=empty`. |
| Theorem 4.3(5) | **REFUTED as printed.** Do not promote its `+epsilon` identity.  A promotable replacement deletes the extra `epsilon` term using Orevkov Lemma 2.1 and strengthens to `s_0=1` and both normalizations `A^1`, as in §7. |
| Corollary 4.4 | **PROMOTE conditional on `r_1=1`;** it holds throughout the repaired residual configuration. |
| Corollary 5.1 | **PROMOTE** under H2; at `N=5`, `m<=2`. |
| Corollary 5.2 | **PROMOTE** only for the `N=4`, H2 horn. |
| General-`N` OPEN | **RETAIN OPEN**, but at `N=5` replace “exactly two profiles” by the single `(2,1)+(1,0)` profile and record its covering degrees after the source repair. |

On Deligne–Fulton/Nori: **the descriptions in the charged report do not yet
decide the needed lemma.**  Deligne–Fulton concerns an irreducible projective
curve with ordinary nodes, whereas
`C^2-D=P^2-(bar D union L_infinity)` deletes a reducible divisor.  The affine
double branches here may be tangent, and the one place at infinity can be a
non-nodal singular/contact.  Abelianity of `pi_1(P^2-bar D)` would not by
itself imply abelianity after additionally deleting `L_infinity`.  The
report's former `C^*` alternative would moreover have two places at infinity,
although the source repair removes it.

Before either theorem can be invoked, an acquisition must check: (i) whether
“double point” means ordinary transverse node; (ii) whether the theorem has
an affine or reducible-divisor version; (iii) the exact projective closure and
intersection multiplicity with `L_infinity`; (iv) for Nori, which strict or
resolved divisor enters the self-intersection inequality and how infinitely
near/tangent points are counted; and (v) whether the conclusion is full
abelianity or merely centrality/commutativity of meridians sufficient to rule
out the specified `S_4` representation.  If those checks fail, one must run
van Kampen for `bar D union L_infinity` and test the prescribed transposition
images.  This is not safely typed as a mere quotation lookup.

<!-- BODY-END -->
