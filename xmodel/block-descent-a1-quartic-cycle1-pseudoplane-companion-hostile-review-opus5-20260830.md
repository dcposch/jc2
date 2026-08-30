# Hostile review: `R4-CYCLE-1` pseudo-plane and companion-divisor threat map

Reviewer: Opus 5, independent hostile referee
Date: 2026-08-30 UTC
Subject: `xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md`
Overall disposition: **CONFIRM_WITH_CORRECTIONS** — the mathematics reproduces,
no proposed shortcut survives, the horn is genuinely open, and one structural
finding collapses the producer's three successors to one.

## 0. Custody

All ten charged hashes reproduce exactly:

```text
7d40e7ee6d5970c51d62f73bafaf11670cb32c06bd51859876ab526f0fdf8bab
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md   OK
c75951528ed3b2d5aa3ebe15b5186893e4da3aac131ca1ca931eee4968ba631c
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md.artifact.json   OK
0b01b3901363097e25e03fe67d0644c287ee3ef1701acd4e9ee1e166da05ca54
  ops/block_descent_a1_quartic_cycle1_pseudoplane_replay.py   OK
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md   OK
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md   OK
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md   OK
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md   OK
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md   OK
38baa55d6e2d54bf3fa5329e1623d983b4e6ac6eaddf7fd7dbb60b2cd1675578
  ladder/SHEET6.md   OK
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad
  refs/zoladek2008_official.pdf   OK
```

Seal and manifest reproduce:

- file bytes `18423`, matching `artifact.file_bytes`;
- the unique standalone `<!-- BODY-END -->` is line 499; `head -c 18090` ends
  exactly at the end of that line, matching `artifact.body_bytes` and
  `custody.source_bytes`;
- `sha256(head -c 18090) = c21f168a64e9c30452f49b1e820d21d57bdb03718cbd4bb580431a46538cad2a`,
  matching `artifact.body_sha256`, `custody.source_sha256`, and the in-file seal;
- frozen basis `4393243bccdbe1a32d80fe8c770c2c8b909f4c01` exists as a commit
  object in the repository.

No `CUSTODY_FAIL`.

**Disclosure 1.** The report's own §1 frozen list contains one file *not*
charged to me, `xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md`
(`f9720718...0ff8`). I did not open it. Seven of the eight repository inputs
listed in §1 are charged and their hashes match the values printed there. None
of the conclusions I confirm below depends on that eighth file: every input I
actually consumed traces to a charged coordinator integration.

**Disclosure 2 (narrow primary-source check).** The load-bearing surface lemmas
are Miyanishi, *Lectures on Geometry and Topology of Polynomials*,
arXiv:1504.07179 — a primary source for named theorems, not present in this
packet's `refs/`. I fetched it to `/tmp` only. Its SHA-256 is
`ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4`, identical to
the value recorded in the charged cubic funnel (line 88) and independently
re-verified by the charged GPT-5.5 review (line 24). I read only the statements
of Lemma 1.4.3, Corollary 1.4.4, Definition 1.4.5, Lemma 1.4.16, Lemma 2.5.2 and
Theorem 2.5.10, plus the two short proofs needed to pin generators. Nothing was
written into the repository.

This review makes no exit-price assertion, so no charge-basis line is emitted.

## 1. Verdict table

| # | Item | Verdict |
|---|------|---------|
| 1 | Minimal row; `C=A1, Q=0, e(U)=1` | **CONFIRMED** |
| 2a | At most one multiple fibre (Miyanishi 1.4.16) | **CONFIRMED** |
| 2b | No-multiple `=> U≅A2` | **CONFIRMED** (uncharged Kambayashi–Wright step) |
| 2c | Scope of the promoted `td<=5` theorem | **CONFIRMED** (over-charged; see 3.3) |
| 2d | `Pic(U)=Z/mu<[Phi]>`, rational acyclicity | **CONFIRMED** (citation upgrade) |
| 2e | `K_U~0` and the typed-formula quarantine | **CONFIRMED** (source erratum noted) |
| 3 | `U-g1(A2)` finite; units sequence; Kummer; `mu|d1` | **CONFIRMED** |
| 4 | Companion `T`: étale, Cartier, `2/1/0`, `e(T)=-3`, `e(U-T)=4`, `pi(U)=A2-{n}` | **CONFIRMED** |
| 5 | `div_Y(pi^*b_i)=2R_i+S_i`, `[S_i]=-2[R_i]`, injection, different | **CONFIRMED** (under-argued; repaired) |
| 6 | 36 transporter sets; cusp/node packet; no canonical character | **CONFIRMED** (strengthened) |
| 7a | §6 cusp-node ruling firewall | **CONFIRMED** as a firewall; scope narrower than §0.5 claims |
| 7b | §7 "genuinely new first-leg datum" (7.3) | **REFUTED** — the first leg is free |
| 7c | Independent search for a contradiction | none found; sharp control supplied |
| 8 | Replay hashes, modes, mutation | **CONFIRMED**; two sub-checks vacuous/sampled |
| 9 | Successor ranking `EXTENSION` (§8 item 2) | **REFUTED** as a route |

The report's headline verdict — the row is not excluded, and the three named
shortcuts are blocked — survives in full. The corrections are about provenance,
one over-claim in §7, and the ranking of successors.

## 2. Item 1 — the exact minimal row and `C=A1, Q=0, e(U)=1`

**CONFIRMED**, rederived without using the producer's arithmetic.

Charged row: `h=b0(R)=1`, `k=b0(B)=1`, `n22=1`, `beta1(B)=1`, `n4=0`,
`|T31|=m=1`, `deg pi=4`, generic `(2,1,1)` on every branch component (this last
is the standing hypothesis of the nodal-control map §2, and is *equivalent* to
`T31` being finite, hence implied by `|T31|=1`; the quartic report never
restates it — a minor exposition gap, not a defect).

Stratify the target and use `e_c` additivity plus `e_c=e` for complex varieties.
Over `A2-B` the map is étale of degree four and the whole fibre lies in `U`
(because `pi(R)=B`). Over a point of `B` the fibre partition is one of
`(2,1,1),(3,1),(2,2),(4)` — an exhaustive census, since in a fibre of a finite
flat map a point of local length one is exactly an étale point and a point of
local length `>=2` is exactly a point of `R`. Counting étale points gives
`u=2,1,0,0` respectively. Hence

```text
e(U) = 4(1-e(B)) + 2(e(B)-m-n22-n4) + m
     = 4 - 2e(B) - m - 2n22 - 2n4.
```

With `e(B)=h-n22` (charged branch-topology (3.1); equally, the nodal-control §2
statement that `B` is homotopy equivalent to a circle gives `e(B)=0` directly),

```text
e(U) = 4 - 2h - m - 2n4 = 4 - 2 - 1 - 0 = 1.
```

This is the charged ledger `e(U)=4-2h-e(T31)-2n4` and the specialization
`e(U)=2-m`. Feeding the promoted ruling identity `e(U)=e(C)+Q`, `C in {A1,P1}`,
`Q>=0`: `e(P1)=2>1` kills the projective base, so `C=A1` and `Q=0`. The row is
the unique `m=1` row, and I reconfirm the whole `(0.1)` trichotomy: `m=0` gives
`e(U)=2`, i.e. `(A1,1)` or `(P1,0)`; `m=1` gives `(A1,0)`; `m>=2` gives
`e(U)<=0`, infeasible.

Two consequences worth recording, both used later:

- `Q=0` means every ruling fibre has exactly one reduced component, i.e. **every
  fibre is irreducible**; it does *not* exclude multiplicity, since a multiple
  fibre `mu*Phi` with `Phi` reduced contributes `q_t-1=0`. The report uses this
  correctly.
- The same ledger gives `e(Y)=e(U)+e(R)=1+1=2` and, independently, counting
  *all* fibre points `3,2,2,1`, `e(Y)=4+3(0-1-1)+2+2=2`. The two agree.

## 3. Item 2 — audit of every pseudo-plane step

### 3.1 At most one multiple fibre — **CONFIRMED**

Primary source, verbatim: *Lemma 1.4.16. Let `X` be a smooth affine surface with
an `A1`-fibration `rho : X -> A`, where `A` is isomorphic to `A1`. Let
`{m_1F_1,...,m_nF_n}` exhaust all multiple fibers of `rho` ... Suppose that
`n >= 2`. Then there are no non-constant morphisms from `A1` to `X` whose image
is transverse to the given `A1`-fibration `rho`.*

Hypotheses are **degree-free** — smooth affine surface, base `A1`, nothing about
typing or about the second leg. The reuse from degree three to degree four is
therefore legitimate, exactly as the report asserts in §1. The transversality
input is supplied correctly: `g1` is dominant and `rho` surjective, so
`h=rho o g1 : A2 -> A1` is a nonconstant polynomial; a general affine line `L`
has `h|_L` nonconstant, so `g1|_L : A1 -> U` is nonconstant with image not in a
fibre. No compatibility of `g1` with the ruling is used or needed.

### 3.2 The no-multiple row and `U ≅ A2` — **CONFIRMED**, one uncharged input

With `Q=0` and no multiple fibre, every *scheme* fibre is `div(rho^*(t-a))` with
reduced irreducible support, hence a reduced smooth `A1`. Miracle flatness
(`U` smooth hence CM, `A1` regular, equidimensional fibres) gives flatness;
smooth fibres then give a smooth morphism.

**Correction (hidden classification input).** The step "smooth with all fibres
`A1` `=>` `A1`-bundle" is *not* formal: it is Kambayashi–Wright (flat families of
affine lines over a one-dimensional regular base are Zariski-locally trivial
`A1`-bundles). Only after that is `rho` a torsor under a line bundle, so that
`Pic(A1)=0` and `H^1(A1,O)=0` give `U ≅ A2`. The charged GPT-5.5 review of the
cubic funnel flagged this explicitly ("One still needs the standard theorem that
a smooth `A1`-fibration over a smooth curve is an `A1`-bundle"); the quartic
reuse drops even that flag. The theorem is true and standard, so this is a
citation defect, not a mathematical one.

An alternative route that avoids it: Lemma 1.4.3(3) with all `m_P=1` gives
`Pic(U)=0` directly, which is already enough to contradict the surviving
`Pic(U)=Z/mu`, `mu>=2` conclusion — but the report needs `U ≅ A2` itself to
invoke the Keller theorem, so Kambayashi–Wright stays load-bearing.

### 3.3 The promoted topological-degree theorem — **CONFIRMED**, exact scope

Charged source, `refs/zoladek2008_official.pdf`:

- Definition 3.1 (p. 438): a **Jacobian map** is a *polynomial* map
  `P : C2 -> C2`, `(x,y) -> (f,g)`, with `Jac P = 1`.
- Theorem 6.12 (p. 461): *"Any Jacobian map `P` with `degtop P <= 5` is
  invertible."* `degtop` is the topological degree, the number of preimages of a
  generic point (Proposition 6.5, p. 458, is stated as a formula "for the
  topological degree").

Every hypothesis is discharged by the report's step:

1. `U ≅ A2` makes `pi|U` a morphism of affine planes, hence a *polynomial* map;
2. étaleness makes `Jac(pi|U)` a nowhere-vanishing regular function on `A2`,
   hence a unit of `C[x,y]`, hence a nonzero constant, normalizable to `1` by a
   linear change of the target (which does not move `degtop`);
3. `degtop(pi|U)=4`: for `y` outside the curve `B` the four points of
   `pi^{-1}(y)` all lie in `U`, and `C(U)=C(Y)` is of degree four over the
   target function field.

`4 <= 5`, so Theorem 6.12 forces invertibility, contradicting degree four. The
row is empty. **CONFIRMED.**

**Correction (over-charge).** Degree four does not need the `<=5` theorem.
Żołądek's own introduction (p. 432) records: *"He and A. Domrina proved that the
Jacobian Conjecture holds true for maps of geometrical degree `<=4`."* For
dominant polynomial maps of `C2` in characteristic zero, geometric degree =
field degree = topological degree, so Domrina–Orevkov alone closes the step, and
`refs/do.pdf` is banked per `ladder/SHEET6.md` line 83. This matters because
`SHEET6.md` lines 94–95 record a documented GGV criticism of a *neighbouring*
Żołądek gcd argument; the present step is insensitive to how that dispute
resolves, since it never needs the `5`-sheeted extension. I recommend the
campaign cite Domrina–Orevkov here and keep Theorem 6.12 for `degtop = 5`.

### 3.4 `Pic(U)=Z/mu<[Phi]>` and rational acyclicity — **CONFIRMED**, citation upgraded

Primary source, verbatim, *Lemma 1.4.3*: `X` smooth affine with an
`A1`-fibration `rho : X -> C`, `C ≅ A1` or `P1`. Then

- (1) any fibre is a disjoint union of affine lines with multiplicities;
- (2) if `C ≅ A1`, `rank Pic(X) = sum_P (r_P - 1)`;
- (3) if `C ≅ A1` and `r_P = 1` for every `P`, then
  `Pic(X) ≅ prod_P Z/m_P Z` with `m_P` the multiplicity of `rho^{-1}(P)`;
- (4) under the assumptions of (3), `X` is a `Q`-homology plane, i.e.
  `H_i(X;Q)=0` for `i>0`.

Both hypotheses of (3)–(4) hold in the charged row: `C=A1` and `r_P=1` for all
`P` (this is exactly `Q=0`). So `Pic(U)=Z/mu` and `H_i(U;Q)=0` for `i>0`.
**CONFIRMED.**

**Citation upgrade (material).** The report and the charged GPT-5.5 review both
route the cyclic statement through *Corollary 1.4.4*, which reads only
"`Pic(X)` is a cyclic group of order `m`" — it does **not** identify the
generator. The Kummer step of §2 needs `[Phi]` to have *exact order* `mu`, not
merely `|Pic(U)|=mu`. That stronger statement is supplied by Lemma 1.4.3(3) and
its proof, which shows the classes `[F_P]` generate with the *only* relations
`m_P F_P ~ 0`. So `Pic(U) = Z/mu` **generated by `[Phi]`, of exact order `mu`**,
is licensed — but by 1.4.3(3), not by 1.4.4. The report's displayed
`Pic(U)=Z/mu<[Phi]>` is therefore correct with the corrected citation.

Independent cross-check: 1.4.3(2) says `rank Pic(U) = sum(r_P-1) = Q`, so the
charged ruling identity `e(U)=e(C)+Q` reads `e(U)=e(C)+rank Pic(U)`; here
`1=1+0`. Consistent.

Terminology check: Definition 1.4.5 defines an **affine pseudo-plane** as a
smooth affine surface with (1) an `A1`-fibration over `A1` and (2) a unique
multiple fibre of multiplicity `d>=2`. The type `(d,n,r)` is an *additional*
condition (3) on the dual graph of a smooth completion. The report's §0.1 phrase
"affine pseudo-plane in the general, untyped sense" is therefore exactly right.

### 3.5 `K_U ~ 0` and the typed quarantine — **CONFIRMED**, with a source erratum

`pi|U` étale gives `omega_U ≅ pi^* omega_{A2} = O_U`, so `K_U ~ 0`. Trivial and
correct.

The quarantine in §2 lines 201–203 is **verified at the primary source and is
load-bearing**. Theorem 2.5.10 reads: *"Let `X` be an affine pseudo-plane **of
type `(d,n,r)`**. If `r != 2` then there are no étale morphism from `X` to
`A2`."* Its proof uses the completion of Definition 1.4.5(3) to get
`Pic(X)=Z/dZ` generated by `F_0` and `K_X ~ (r-2)F_0`. Nothing in the charged
row establishes condition (3) for our `U`. Had the producer applied 2.5.10
anyway, it would have closed the row on a false coverage assumption. The refusal
is correct and is the single most important restraint in the report.

**Source-level erratum (affects future campaign use, not this report).** Within
the typed class, `K_X ~ (r-2)F_0` and `Pic(X)=Z/dZ<F_0>` give
`K_X ~ 0  <=>  d | (r-2)`, i.e. `r ≡ 2 (mod d)`. Definition 1.4.5 constrains only
`r >= 2`, `n >= 1`, `d >= 2`, and Lemma 1.4.6 explicitly treats `r >= d`, so
`r = d+2` is an admissible type with `K_X ~ 0`. The printed inference "Hence
`K_X` is not `~ 0` unless `r = 2`" is therefore too strong as it stands, and the
charged cubic funnel §4.3 inherits it ("excludes an etale map to `A2` unless the
exceptional `r=2` row occurs"). The correct typed conclusion is
`r ≡ 2 (mod d)`, which enlarges the typed survivor set beyond `{r=2}`. This
does not touch any conclusion of the report under review, which uses neither
form.

### 3.6 Hidden assumptions inventory (obligation 2, last clause)

Charged and legitimate: `Y` integral, normal, affine, finite flat over `A2` of
rank four; `R` nonempty and pure of codimension one; `Sing(Y) ⊆ R` (this is what
makes `U` smooth); `g1(A2) ⊆ Y_sm - R`; `O(U)^*=C^*`; `bar-kappa(U)=-infinity`;
`G=S4`.

Uncharged or unstated, all true: Kambayashi–Wright (§3.2 above); the standing
"generic `(2,1,1)` on every branch component" (implied by `|T31|=1`, but not
restated); `e_c = e` for complex varieties and `e_c` fibre-integration
("constructible Fubini"), used in §3 of the report.

No hidden *irreducibility* assumption: the report correctly indexes by
irreducible components `B_i` throughout and never conflates `h=b0(R)=1` with
irreducibility (the nodal-control map §2 item 1 flags precisely this trap).

## 4. Item 3 — cofinite image, units sequence, Kummer, `mu | d1`

**CONFIRMED** in all four parts. Reconstruction:

**Cofiniteness.** `g1` étale hence open, so `V=g1(A2)` is open and `U-V` closed
of dimension `<=1`. Suppose `D != 0` is a divisor supported in `U-V` with
`D=div_U(b)`. Then `b` has neither zero nor pole on `V`, so `b|_V in O(V)^*`;
`g1^*b` and `g1^*b^{-1}` are mutually inverse elements of `C[x,y]`, hence
constants, say `g1^*b = lambda`. Since `g1^*` is a field embedding
`C(U) -> C(x,y)`, `g1^*(b-lambda)=0` forces `b=lambda` and `D=0`. So the free
abelian group on prime divisors in `U-V` injects into `Cl(U)=Pic(U)=Z/mu`, which
is finite; a nonzero free abelian group cannot. Hence `U-V` has no curve
component and is finite.

**The units/localization sequence.** For a normal integral `Y` and a union of
prime divisors, the exact sequence is

```text
O(Y)^* -> O(U)^* -> (+)_i Z[R_i] -> Cl(Y) -> Cl(U) -> 0,
```

the middle map being `f |-> (ord_{R_i} f)`. Since `O(U)^* = C^* ⊆ O(Y)^*`, the
image of `O(U)^*` is zero and `(+)_i Z[R_i] -> Cl(Y)` is **injective**; the same
sequence delivers `Cl(Y)/<[R_i]> ≅ Cl(U) = Pic(U) = Z/mu`. Both `(4.2)` and
`(4.3)` are this one sequence. The report's remark at line 311 that
`O(U)^*=C^*` is "load-bearing in (4.2)" is exactly right; the name "promoted
boundary-class theorem" is a misnomer — the content is excision plus the
promoted unit theorem. A derived structural fact the report does not state:
`Cl(Y)` is finitely generated of rank equal to the number of irreducible
components of `R`, containing `(+)_i Z[R_i]` with index `mu`.

**`g1^*(t-a)=cP^mu`.** `div_U(rho^*(t-a))` is the scheme fibre `mu*Phi`;
`g1` étale makes `g1^*Phi` reduced; `Pic(A2)=0` and factoriality of `C[x,y]`
give `g1^*Phi = div(P)` with `P` squarefree, whence
`div(g1^*(t-a)) = mu·div(P)` and `g1^*(t-a)=cP^mu`, `c in C^*`. Nonconstancy is
guaranteed because `rho o g1` is nonconstant.

**Kummer irreducibility — no escape.** The Vahlen–Capelli criterion: `X^n-alpha`
is irreducible over `K` iff `alpha` is not a `p`-th power in `K` for any prime
`p|n`, and, when `4|n`, `alpha` is not in `-4K^4`.

- *Primitive-divisor / `p`-th power escape:* if `(t-a)/c = s^p` in `C(U)` for
  `p|mu`, then `div_U(s)` is effective and equal to `(mu/p)Phi`, so `s` is
  regular (`U` normal affine), and `(mu/p)[Phi]=0` in `Pic(U)` contradicts the
  exact order `mu` established in §3.4 above. Closed.
- *`4|mu` exception:* vacuous over `C`, because `-4 = (1+i)^4`, so
  `-4K^4 = K^4 ⊆ K^2`, and `alpha` already avoids `K^2`. The report's phrasing
  ("since `C` contains all roots of unity ... no further exception") reaches the
  right conclusion; the sharp reason is the displayed fourth-power identity.
- *Residue-degree escape:* none is available, since the argument is a divisor-
  class argument on `U` and never passes through a residue field.

Hence `[K(P):K]=mu` and `mu | [C(x,y):C(U)] = d1`.

## 5. Item 4 — independent derivation of the companion curve

**CONFIRMED** in every part.

**Étaleness.** `T = U x_{A2} B` is the base change of the étale `pi|U` along
`B -> A2`; étaleness is stable under arbitrary base change, so `T -> B` is étale
*regardless of `B` being singular or reducible*.

**Fibre counts.** A point of `pi^{-1}(z)` lies in `U` iff it is étale over the
target iff its local length in the fibre is one. Reading the partitions:
`(2,1,1) -> 2`, `(3,1) -> 1`, `(2,2) -> 0`, `(4) -> 0`. With `T31={c}`,
`S22={n}`, `n4=0` and everything else `(2,1,1)`, the counts `2/1/0` follow, and
`c != n` because the partitions differ.

**Non-finiteness is real and correctly flagged.** `T -> B` has an empty fibre
over `n`, so it is not surjective, hence not finite. At `c` it is a local
isomorphism (étale with a single fibre point), so `T` reproduces the germ of `B`
at `c`, while the second companion sheet over a punctured neighbourhood of `c`
runs into `R` and does not extend. The report's line 213 ("It need not be
finite") is exactly the right caution.

**`e(T)=-3` and the compact-support question (obligation 4, last clause).** The
computation is `e_c` fibre-integration for a morphism of complex varieties:
`e_c(T) = int_B chi_c(T_z)`, which is additive over any constructible partition
of `B` and *insensitive to singularity or reducibility of `B`*. With `e(B)=0`,

```text
e(T) = 2·e_c(B-{c,n}) + 1·1 + 0·1 = 2(0-2)+1 = -3.
```

The report's phrase "constructible Fubini" is the correct justification and is
what makes non-finiteness harmless. (Had the producer instead argued via a
degree-two covering, it would have needed a finiteness step; over the non-normal
`B` that step requires normalizing and descending properness. The chosen route
avoids all of it.)

**Reduced principal Cartier status.** With `b = prod b_i` a reduced (squarefree)
equation of `B`, `div_{A2}(b) = B_red`; étale pullback preserves reducedness, so
`div_U(pi^*b) = T` is a reduced effective divisor, Cartier because `U` is smooth
and principal because `pi^*b in O(U)`. This is a statement on `U` only, as the
report stresses.

**Complement and its two Euler ledgers.** `pi(R)=B` gives `R ⊆ pi^{-1}(B)`,
hence `W=U-T = Y - pi^{-1}(B)`, a nonempty open of the *integral* `Y`, therefore
irreducible and connected; base change of a finite flat map makes
`W -> A2-B` finite étale of degree four, with the charged monodromy `S4`.

```text
e(W) = 4·e(A2-B) = 4(1-0) = 4,        e(W) = e(U)-e(T) = 1-(-3) = 4.
```

**`pi(U)=A2-{n}`.** `pi(U) ⊇ A2-B`; a point `z in B` is in `pi(U)` iff
`u(z)>=1`, true except at `n`. So `pi(U) = A2-{n}` exactly.

Internal consistency the report only half-states: `pi|U` *must* be non-finite,
because a finite étale cover of the simply connected `A2` is trivial and would
force `Pic(U)=0`, contradicting `mu>=2`. The omitted point `n` is precisely the
witness. The report's line 258 asserts non-finiteness; the above shows it is
forced, not incidental.

## 6. Item 5 — height-one equations, class lattice, different

**CONFIRMED**, with the residue-degree and multiple-ramification questions
settled literally, which the report asserts but does not argue.

**Exactly one ramified prime per `B_i`, with `f=1`.** Let `A = O_{A2, eta_i}`,
a DVR with uniformizer `b_i`. Since `Y` is normal, the semilocal ring above `A`
is a semilocal Dedekind domain and `sum_P e_P f_P = 4`. Base-changing to the
algebraic closure of the residue field, the geometric generic fibre has partition
`(2,1,1)`: exactly one point of multiplicity two. A prime `P` with `e_P = 2`
contributes `f_P` geometric points each of multiplicity two, so `f_P = 1`; two
such primes would force partition `(2,2)`, and `e_P in {3,4}` would force
`(3,1)` or `(4)`. Hence **`R_i` is unique with `(e,f)=(2,1)`**, and the residual
degree two splits as either two primes with `f=1` or one prime with `f=2`.

**`(4.1)` is literal in both cases.** Divisor coefficients are ramification
indices, and `e=1` for every unramified prime, so
`div_Y(pi^*b_i) = 2R_i + S_i` with `S_i` the reduced sum of the unramified
primes over `B_i` — one component in the inert case, two in the split case. The
report's one-line dismissal at lines 272–273 reaches the right answer; the
uniqueness of `R_i` is the missing half and is supplied above.

**Class relations.** `2R_i+S_i` principal gives `[S_i] = -2[R_i]`. By the
injection of §4, `2[R_i] != 0` in `Cl(Y)` (the free group `(+)Z` is torsion
free), so **`S_i` is nonprincipal on `Y`** — this is a *proof*, not an
observation, and the report should say so. Its restriction `T_i = S_i ∩ U` is
principal on `U` because `div_U(pi^*b_i)=T_i`. Localization predicts exactly
this, and there is no contradiction.

**Different.** Characteristic zero makes all ramification tame with separable
residue extensions, so the codimension-one different exponent is `e_P-1`:
`D_{Y/A2} = sum_i R_i`. Nonprincipal for the same reason.

**Cross-check the report does not make.** Riemann–Hurwitz for finite dominant
maps of normal varieties gives `K_Y = pi^*K_{A2} + sum_i R_i`, so
`[K_Y] = sum_i [R_i] != 0` in `Cl(Y)`, while `K_U ~ 0`. The two are compatible
precisely because `Cl(Y) -> Cl(U)` kills the `[R_i]`. This is an independent
confirmation that the §4 lattice is consistent rather than contradictory, and it
is the cleanest available refutation of any "the different should be trivial"
shortcut.

**Discriminant identity, derived here.** `disc(pi_*O_Y) = N(D_{Y/A2})` has
`ord_{B_i} = sum_P f_P d_P = 1`, so `div(disc) = sum_i B_i = div(b)` and

```text
disc(pi) = const · b.
```

The reduced branch equation *is* the discriminant up to a scalar. This is a
usable new handle for successors (it is what makes `b∘F` the pullback of a
canonical invariant rather than an arbitrary choice), and it also shows that the
sign character of `S4` corresponds to the double cover `sqrt(disc)`, which does
not lie in `C(Y)` because the point stabilizer `S3` is not contained in `A4`.

## 7. Item 6 — the 36 transporter sets and the cusp/node packet

**CONFIRMED and strengthened.** I recomputed everything with my own
implementation using a different data layout and composition convention from the
charged replay.

- For every ordered pair `(a,b)` of transpositions in `S4`,
  `{g : gag^{-1}=b}` has exactly `4` elements — a coset of the centralizer
  `C(a) = <a> x <a'> ≅ Z/2 x Z/2`, where `a'` is the transposition on the
  complementary pair.
- Every such `g` maps the fixed pair of `a` onto the fixed pair of `b`, and the
  induced parity multiset is `[0,0,1,1]` in all `36` cases. Structurally: the
  transporter set is a torsor under `C(a)`, and the companion parity is the
  projection onto the `<a'>` factor — a *surjective* character. So parity is
  equidistributed and is not a function of `(a,b)`.
- `<(12),(23)> = S3` (order 6); `<(12),(23),(34)> = S4` (order 24). Also, all
  `24 x 3 = 72` labelled cusp-plus-node packets generate `S4`, verified
  independently: `<a,b>=S3` on three letters fixing `w`, and any perfect matching
  contains a transposition moving `w`, so the group is transitive and contains a
  point stabilizer of index four, hence is `S4`.

**Obligation 6, decisive part — does anything canonically remove the ambiguity?**
I tested the three group-theoretic candidates named in the obligation:

```text
refine by sign (determinant) : both parities still occur in 36/36 pairs
refine by cubic resolvent    : both parities still occur in 36/36 pairs
refine by sign + resolvent   : both parities still occur in 36/36 pairs
```

So **no**: neither the determinant/sign character `S4 -> Z/2`, nor the resolvent
`S4 -> S3`, nor their combination, is constant on parity classes for any of the
36 ordered pairs. Concretely, for `a=b=(12)` the transporter set is
`{e,(12),(34),(12)(34)}` with parities `0,0,1,1`; the two even elements
`e,(12)(34)` already realize both parities, and the two elements with trivial
resolvent image are the same pair. The discriminant/norm candidates reduce to the
sign character and fail with it.

The genuine content of the ambiguity is arithmetic, not group-theoretic: it is
whether the two unramified primes over `B_i` are split (`f=1,1`) or inert
(`f=2`), i.e. whether the residue monodromy along `B_i` swaps the companion
sheets. That is a property of the *actual* cover, not of local packets. A remark
supporting the producer that the report does not make: near the `(3,1)` point `c`
the companion pair *is* canonically ordered, because exactly one of the two
companion sheets collides with the ramification pair at `c`; the ambiguity is
purely about propagating that labelling around `B_i`, which the residue
monodromy may obstruct. The "based infinity relation" the report leaves open is
therefore the right place to look, and no shortcut is available from the local
data. **CONFIRMED.**

One supporting derivation the report omits, which justifies its own vocabulary:
a `(3,1)` fibre cannot sit over a *smooth* point of `B`. At a smooth branch point
the local complement group is `Z` generated by one meridian, whose image is a
single transposition with orbits `(2,1,1)`. Since `Y` is normal, fibre points
correspond to orbits of the local group; so a `(3,1)` fibre forces `c in Sing(B)`
with local group `S3` acting on three sheets and generated by transposition
meridians — a cuspidal (unibranch, braid `B3`) germ being the minimal model.
Symmetrically, a `(2,2)` fibre forces at least two local branches at `n` whose
meridians are *disjoint* transpositions. The §5 packet `tau=(12), upsilon=(23),
sigma=(34)` is thus not merely "feasible", it is the forced local shape.

## 8. Item 7 — attacks on the control and the firewalls

### 8.1 The §6 cusp-node firewall — **CONFIRMED**, scope narrower than §0.5

I verified `Gamma: y^2 = x^3(x-1)^2` **exactly**, not by sampling:

- irreducible (`x^3(x-1)^2` is not a square in `C[x]`);
- `Sing(Gamma) = {(0,0),(1,0)}` exactly, by solving `F=F_x=F_y=0`;
- `(x,y)=(t^2,t^5-t^3)` is the normalization (`t = y/(x(x-1))`); the only
  off-diagonal collision is `t=1` with `t=-1`, from `u=-t`, `t^2=1`;
- `(x',y') = (2t, t^2(5t^2-3))` vanishes simultaneously only at `t=0`, with
  orders `(2,3)`: an ordinary cusp;
- tangents `(2,2)` and `(-2,2)` at `t=±1`, determinant `8`: an ordinary node;
- `e(Gamma) = e(A1) - 1 = 0`.

With `rho=x` on `A2`: all fibres are reduced irreducible lines (`Q=0`),
`O(A2)^*=C^*`, `K=0`, and `Gamma` is principal. So the crude implication
"principal curve with a cusp and a node `=>` a reducible ruling fibre" is
**false**. That is a real firewall against the naive shortcut.

**Correction (scope).** The control has `e(Gamma)=0`, not the charged
`e(T)=-3`; it is closed in `A2`, whereas `T` is non-finite over `B` and misses
`n`; and `A2` has no multiple fibre. So §6 blocks only implications that use
*nothing but* "principal + one cusp + one node". It does **not** block an
Euler-weighted or profile-aware coupling, and §0 item 5's "Section 6 gives the
exact control" overstates what §6 delivers. The body of §6 is honest about this
("This is a firewall, not a block control"); the abstract is not.

### 8.2 Attacks I ran and their outcomes

- **Purity / Zariski–Nagata.** `pi` ramifies in pure codimension one along `R`;
  `g1` and `pi|U` are étale. No violation, no leverage.
- **Hartogs / strong Zariski Main.** Blocked, and the block is now verified at
  primary source. Lemma 2.5.2 is a genuine countercontrol: the cyclic cover
  splits `mu*Phi` into `mu` affine lines and deleting `mu-1` of them leaves an
  open `A2` still mapping onto `U`, so cofiniteness of `U-g1(A2)` never upgrades
  to finiteness of `g1`. The report's §7 statement is exact.
- **Picard torsion.** `Pic(U)=Z/mu` with `mu>=2` is compatible with everything;
  it is in fact what *forces* `pi|U` to be non-finite (§5 above).
- **`Cl(Y)` / different.** Consistent lattice, reconfirmed by the
  Riemann–Hurwitz cross-check in §6 above. No contradiction.
- **The omitted node.** This is the attack that looks most promising and is
  decisively dead. The charged primary source predicts it: Żołądek Lemma 6.2
  (p. 457) states *"The preimages `P^{-1}(S_k)` are non-empty algebraic curves
  and the image of `P` is `C2 \ finite set`"*, with the immediately following
  remark that *"Some points of intersections `S_k ∩ S_l`, or of self-intersection
  of `S_k`, may have preimages only at infinity."* Here `B ⊆ A_F` and `n` is
  exactly a point where two branches of the non-properness curve meet. So
  `(7.1)` is not exotic — it is the textbook expectation, and the report's §7
  rederivation is Żołądek's own proof. **The report should cite Lemma 6.2; the
  citation strengthens its refusal to close the row.**
- **Second ruling defect.** A second *multiple* fibre is impossible
  unconditionally (Lemma 1.4.16 plus the existence of a transverse `A1`), so only
  `Q >= 1` is a live target; and `Q >= 1` would contradict `e(U)=1` outright,
  hence would close the row. This is the correct target, but §8 item 1's phrase
  "force a second multiple/reducible ruling fibre" contains a dead half.
- **Jacobian coupling of `rho` and `pi`.** Using `K_U ~ 0`, pick the nowhere-zero
  `omega = pi^*(dX ∧ dY)`; then `g1^*omega = lambda dx ∧ dy`, `lambda in C^*`,
  and `Jac(rho∘g1, b∘F) = lambda·g1^*(J)` where `J` is defined by
  `d rho ∧ pi^*db = J·omega`. Expanding the left side gives
  `c·mu·P^{mu-1}·Jac(P, b∘F)`, i.e. `P^{mu-1} | g1^*J`. This is *tautological*:
  writing `rho-a = w^mu·(unit)` locally already gives `ord_Phi(J) >= mu-1`. The
  identity is real but carries no new information. No contradiction.

**Result: I found no contradiction.** The report's verdict stands.

### 8.3 Decisive new finding — the first leg is free

**The claim in §7 that (7.3) is "the genuinely new first-leg datum" is
REFUTED.**

Primary source, verbatim: *Lemma 2.5.2. Let `X` be a `Q`-homology plane with
`kappa(X) = -infinity`. Hence there exists an `A1`-fibration `rho : X -> C`,
where `C ≅ A1`. Suppose that `rho` has a unique multiple fiber `dF`, where
`F ≅ A1` and `d >= 2`. Then `A2` is a Galois affine pseudo-covering of `X` with
Galois group `H(d)`.* The surrounding text gives `H(d) ≅ Z/dZ`, and the proof
produces a finite étale Galois cover `f~ : Y~ -> X` of degree `d` together with
an open `Y ⊆ Y~` with `Y ≅ A2` mapping *surjectively* onto `X`.

Every hypothesis holds for our `U`: it is a `Q`-homology plane (Lemma 1.4.3(4)),
`bar-kappa(U) = -infinity` (charged ruling theorem), the base is `A1`, and the
unique multiple fibre is `mu*Phi` with `Phi ≅ A1` and `mu >= 2`. Therefore:

```text
There always exists an etale surjection  g1^Miy : A2 -> U  of degree exactly mu.
```

Three consequences, none of which the report draws.

1. **The row is nonempty iff the pair `(U,pi)` exists.** The first leg is not
   independent data to be constrained; it is manufactured from `U` alone. Any
   exclusion argument must therefore exclude `(U,pi)`; conditions imposed on
   `g1` beyond "some étale surjection" cannot help, because one may always
   normalize `g1` to `g1^Miy`.
2. **The row is *sufficient*, not merely necessary, for a counterexample.**
   `F := pi ∘ g1^Miy : A2 -> A2` is a composite of étale maps, hence étale, hence
   `Jac F in C[x,y]^* = C^*`: a Keller map, of topological degree `4mu >= 8`,
   therefore noninvertible. So the surviving object *is* a JC2 counterexample.
   Equivalently, in contrapositive form:

   > **JC2 implies that no `Q`-homology plane with `bar-kappa = -infinity` and a
   > unique multiple `A1`-fibre admits an étale morphism to `A2`.**

   With this normalization, `(7.1)` sharpens to `A2 - F(A2) = {n}` *exactly*.
3. **Successor #1 (`R4-CYCLE-1-FUNCTION-PAIR`) cannot be decisive as posed.**
   The pair `(rho∘g1, b∘F) = (cP^mu, g1^*(pi^*b))` is a formal re-encoding of
   `(rho, pi^*b)` on `U` under a map that always exists. It may still be a
   convenient *tactic* — polynomial computations on `A2` can be easier than
   surface arguments on `U` — but any conclusion it reaches is a conclusion
   about `(U, rho, pi^*b)`, and "no current theorem couples the two polynomials"
   is not evidence of hidden strength.

This finding does not refute the report's headline; it *sharpens* it. It removes
the second disjunct of the §0 target ("or prove that the actual first leg forces
the companion closure to extend principally"), leaving exactly the first.

### 8.4 Successor #2 (`R4-CYCLE-1-EXTENSION`) — **REFUTED as a route**

Its stated intermediate goal is: "prove ... that some `T_i` defining section has
zero valuation along `R_i`." That goal is provably unreachable. `T_i` is
principal on `U`, and since `O(U)^* = C^*`, its defining function is unique up
to a nonzero constant; that function is `c·pi^*b_i`, whose valuation along `R_i`
is exactly `2` by `(4.1)` — never `0`. Equivalently, a function with
`div_Y = S_i` would make `2R_i` principal, contradicting the injection `(4.2)`.
So §4 has already settled the question in the negative, and the successor is
inert: it can only be restated as the contentless "derive some contradiction".
It must not be launched as posed.

### 8.5 Sharp control, since the funnel survives

I cannot exhibit a realized control: any object satisfying the full profile is,
by §8.3, a Keller counterexample, and cannot be priced as a routine example. The
sharp *statement* of what remains is therefore:

> **Pseudo-plane-to-plane gate.** Does there exist a smooth affine surface `U`
> with `bar-kappa(U) = -infinity`, `O(U)^* = C^*`, an `A1`-fibration `U -> A1`
> all of whose fibres are irreducible with exactly one multiple fibre `mu*Phi`
> (`mu >= 2`), `K_U ~ 0`, together with an étale quasi-finite morphism
> `pi : U -> A2` of degree `n >= 2`?

For `n = 1` the answer is no: étale of degree one over the normal `A2` is an
open immersion, and `Cl(A2) = 0` surjects onto `Cl(U)`, contradicting
`Pic(U) = Z/mu`. For `n >= 2` it is open, and Miyanishi's Theorem 2.5.10 is
precisely the partial answer for the *typed* subclass. The charged degree-four
row adds `n = 4`, `pi(U) = A2 - {n}`, `e(T) = -3`, `S4` monodromy, and the
`(0.4)` class lattice — extra structure that a solution may use but that is not
needed to state the gate.

## 9. Item 8 — what the replay does and does not certify

**Reproduced exactly.**

```text
ordinary / -O / -OO  stdout SHA-256 = f239c255f72d02ca28c57b918b443c1d8638beb790acb467ecbb726b85c88da9
payload_sha256       = 328df8df376dc974bd9aa5a672f3f8f6e64f35de9cf95163aabf6b737e0b6473
status               = PASS-QUARTIC-CYCLE1-PSEUDOPLANE-THREAT-MAP
transporter_profile_digest = 963f7196618ef1b4ed25132fc108fcfac3a14cbd3791b1811cb219dbc06dfe14
```

All three modes are byte-identical, matching the values printed in §9 of the
report. `--mutate-force-companion-parity` is rejected in **all three** modes with
exit status `1` and `RuntimeError: local inertia labels falsely force a companion
parity`. AST census: `0` `Assert` nodes and `16` `require` calls, so `-O`/`-OO`
cannot erase a check — the optimization-strip trap does not apply.

**What it genuinely certifies.**

1. All `36` ordered transposition transporter sets have size `4` with parity
   multiset `[0,0,1,1]` (I reproduced this independently, §7).
2. `<tau,upsilon>` has order `6` and `<tau,upsilon,sigma>` has order `24`, with
   the braid and commuting relations checked.
3. Given the hard-coded inputs `e(B)=0`, `e(U)=1` and fibre counts `2/1/0`, the
   two complement-Euler ledgers agree at `4` and `e(T)=-3`. This is a real
   consistency check of two independent routes, though not a derivation.

**What it does not certify — three corrections.**

4. **The class-lattice block (lines 160–172) is vacuous.** It fabricates its own
   literals — `sample_boundary_rank = 3`, `different = (1,1,1)`, rows `-2·e_j` —
   and then asserts properties of those literals: `require(any(v != 0 for v in
   different))` and `require(cls[j] == -2 and sum(abs(...)) == 2)` are tautologies
   about self-authored data. Nothing about `Cl(Y)`, the boundary injection, the
   localization quotient or the torsion is tested, and the rank `3` is unrelated
   to the charged number of branch components. The report calls it "an abstract
   free-boundary/torsion-quotient class model", which is honest, but the same
   sentence says the replay "checks" it. It checks nothing.
5. **The §6 curve control is sampled, not proved.** The parametrization identity
   is verified for `t in [-7,7]`, the collision set for `t in [-12,12]`, and the
   "derivative common zero" test is a tautology over the integers (`2t = 0`
   already forces `t = 0`). The underlying claims are nonetheless exactly true —
   I verified them symbolically in §8.1 — but the software supplies sampling
   evidence only, and a hostile reader should not treat the `PASS` banner as a
   proof of the cusp/node census.
6. **One mutation switch covers one of five claim families.** There is no
   negative control for the Euler ledger, the group orders, the class model, or
   the curve control. A single passing mutation does not distribute over the rest
   of the payload.

The report's own §9 firewall list — no proper-block sandwich, no ruling theorem,
no Miyanishi lemmas, no low-degree Keller theorem, no normal localization, no
different, no finite flatness, no existence of an actual cover, no JC2 — is
accurate and should be retained verbatim.

## 10. Item 9 — maximum-safe theorem, blast radius, cheapest decisive successor

### 10.1 Maximum-safe theorem

> **`R4-CYCLE-1` pseudo-plane funnel (reviewed form).** Assume a noninvertible
> complex Keller map with a proper intermediate field, charge the promoted block
> factorization `A2 -> Y -> A2` with `deg pi = 4`, `R = NonEt_Y(pi)_red`,
> `U = Y - R`, `B = pi(R)_red`, and charge the connected minimal-cycle row
> `h = k = 1`, `beta1(B) = n22 = 1`, `n4 = 0`, generic `(2,1,1)` on every branch
> component, `|T31| = 1`. Then:
>
> 1. `e(U) = 1`, so `C = A1` and `Q = 0`; the ruling `rho : U -> A1` has all
>    fibres irreducible and exactly one multiple fibre `mu*Phi`, `mu >= 2`. `U`
>    is an affine pseudo-plane in the untyped sense of Definition 1.4.5(1)–(2),
>    with `Pic(U) = Z/mu` generated by `[Phi]` of exact order `mu`,
>    `H_i(U;Q) = 0` for `i > 0`, `K_U ~ 0`, `U - g1(A2)` finite, and `mu | d1`.
> 2. `T = U x_{A2} B` is étale over `B`, non-finite, a reduced principal Cartier
>    divisor of `U` with geometric fibre counts `2/1/0` and `e(T) = -3`;
>    `W = U - T -> A2 - B` is connected finite étale of degree four with
>    monodromy `S4` and `e(W) = 4`; and `pi(U) = A2 - {n}` exactly.
> 3. For every irreducible `B_i` there is exactly one ramified height-one prime
>    `R_i`, with `(e,f) = (2,1)`; `div_Y(pi^*b_i) = 2R_i + S_i`;
>    `(+)_i Z[R_i]` injects into `Cl(Y)` with quotient `Pic(U) = Z/mu`;
>    `[S_i] = -2[R_i] != 0`, so each `S_i` is **provably** nonprincipal on `Y`
>    while `T_i = S_i ∩ U` is principal on `U`; `D_{Y/A2} = sum_i R_i`, and
>    `[K_Y] = sum_i [R_i] != 0`. Furthermore `disc(pi) = const · b`.
> 4. *(new)* Conversely, given any `U` and `pi` as in (1)–(2), Miyanishi Lemma
>    2.5.2 supplies an étale surjection `A2 -> U` of degree `mu`, whose composite
>    with `pi` is a noninvertible Keller map of topological degree `4mu >= 8`.
>    Hence the row is nonempty **if and only if** such a pair `(U,pi)` exists,
>    and its nonemptiness would refute JC2.

Do **not** promote: an exclusion of `R4-CYCLE-1`; a principal different or
principal `S_i`; a forced extra ruling component; a finite first leg; a companion
determinant/parity character; membership of `U` in Miyanishi's typed `(d,n,r)`
class; or the existence of a proper block.

### 10.2 Exact blast radius

The theorem is conditional on all of: a Keller counterexample existing; it having
a proper intermediate field; the second leg having rank exactly four; the
connected minimal-cycle row `h=k=1, beta1=n22=1, n4=0`; generic `(2,1,1)` on
every component; and `|T31|=1`. It is silent on `R4-CYCLE-0` (`m=0`, the
`(A1,1)`/`(P1,0)` rows), on any `h >= 2` row, on the disconnected branch horn
(already closed elsewhere), on block degree `>= 5`, on the primitive/no-block
horn, and on JC2 itself. Items (1)–(3) are conditional structure; item (4) is the
only unconditional implication and it points *away* from a proof — it says the
survivor would be a counterexample, so the remaining gate carries full JC2-grade
difficulty and cannot be discharged by bookkeeping.

Widened radius in one direction only: the gate of §8.5 is stated for arbitrary
degree `n >= 2`. Solving it in that generality would close **every** proper-block
row with `C = A1`, `Q = 0` and one multiple fibre, at every rank — not just
`R4-CYCLE-1`.

### 10.3 Cheapest decisive successor

Reordered, with reasons:

1. **`R4-CYCLE-1-PSEUDOPLANE-MAP` (promote to sole decisive successor).** By
   §8.3 this is not one option among three; it is the whole remaining content of
   the row. Its cheapest concrete form is a **type-coverage question in the
   literature, not a new computation**: does every affine pseudo-plane in the
   sense of Definition 1.4.5(1)–(2) with `K ~ 0` carry a boundary graph of type
   `(d,n,r)`? If yes, Theorem 2.5.10 applies and — with the erratum of §3.5 —
   restricts to `r ≡ 2 (mod d)`, at which point `U` is explicit and a degree-four
   étale quasi-finite map to `A2` with `pi(U) = A2 - {n}` and `e(T) = -3` becomes
   a finite check. If no, exhibiting an untyped `K`-trivial pseudo-plane is
   itself the first genuinely new object in the campaign. The charged cubic
   funnel §4.3 already flagged "type coverage OPEN"; this review upgrades it from
   a side note to the hinge.
2. **`R4-CYCLE-1-FUNCTION-PAIR` (retain as a tactic, not a theorem source).**
   Legitimate as a computational route toward `Q >= 1`, which would contradict
   `e(U) = 1` and close the row. Two repairs: drop the "second multiple fibre"
   half, which Lemma 1.4.16 already makes impossible; and stop describing the
   pair as new data, since it is a re-encoding of `(rho, pi^*b)` under a map that
   always exists.
3. **`R4-CYCLE-1-EXTENSION` — do not launch.** Refuted as a route in §8.4.

No AWS computation is justified. I agree with the report on that point and
strengthen it: the missing input is a surface-classification theorem, and §8.3
shows that no amount of first-leg arithmetic can substitute for it.

## 11. Summary of corrections requested

1. §2: name the Kambayashi–Wright input for "smooth `=>` `A1`-bundle".
2. §2: cite Domrina–Orevkov (degree `<= 4`) as the primary authority for the
   no-multiple endpoint, keeping Żołądek Theorem 6.12 as the `degtop = 5`
   extension; this insulates the step from the documented GGV dispute.
3. §2: attribute `Pic(U) = Z/mu<[Phi]>` to Miyanishi Lemma 1.4.3(3) (which pins
   the generator and hence the exact order used by the Kummer step), not to
   Corollary 1.4.4.
4. §2/§4.3-of-the-cubic-funnel: record that the typed conclusion is
   `r ≡ 2 (mod d)`, not `r = 2`.
5. §4: state that `R_i` is unique with `(e,f) = (2,1)` and give the geometric
   generic-fibre argument; state that nonprincipality of `S_i` is *proved* by the
   injection; add the Riemann–Hurwitz cross-check `[K_Y] = sum_i [R_i]`; rename
   "promoted boundary-class theorem" to what it is, excision plus `O(U)^* = C^*`.
6. §0.5: soften "Section 6 gives the exact control" to match the honest scope
   statement inside §6.
7. §7: cite Żołądek Lemma 6.2 (p. 457) for `(7.1)` and for the prediction that
   the omitted point is a self-intersection of the non-properness curve.
8. §7/§8: replace the claim that `(7.3)` is new first-leg data with the Lemma
   2.5.2 finding, and reorder the successors accordingly.
9. §1: the `S4` monodromy consumed in §3 is proved in the charged branch-topology
   coordinator integration §5, which is absent from the declared frozen-input
   list; either add it or point the citation at the file that carries the proof.
10. §9: mark the class-lattice replay block as decorative and the curve control
    as sampled.

Nothing in this review constructs a Keller map, proves that a rank-four proper
block exists or does not exist, treats `R4-CYCLE-0`, the disconnected branch
horn, block degree at least five, or the primitive/no-block horn, or proves or
disproves JC2. The typed disposition of the remaining gate is `OPEN`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `47716`.
- Body SHA-256:
  `eb4000c1a5d54bc159adfde607642d349a843773e42fc27179e5062c3d06c3aa`.
- Frozen basis: `3100714032224fcac4641f30a92d33426d165b85`.
