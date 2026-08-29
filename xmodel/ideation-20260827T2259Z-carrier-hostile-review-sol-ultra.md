# Hostile review of the post-T3 nonlinear gate carriers — round `20260827T2259Z`

Date: 2026-08-27  
Reviewer: **Sol Ultra** (OpenAI, runtime family `gpt-5.6-sol`)  
Targets: sealed Fable5, Grok46, and Sol submissions  
Status: **different-model review of Fable5 and Grok46; same-model screen of Sol only.**

No JC2 theorem, face exclusion, endpoint decision, or uniform finite gate bound
is claimed here.

## 0. Executive verdict

All three lanes found the same underlying carrier, up to coordinates:

```text
P_F(0)=p,                 P_F^8=sum_(i=0)^14 F_i s^i P_F^i,
kappa_F(s)=[P_F(s)^2 dX] in H^1_dR(V_H)[[s]],
V_H={p^4=H}->U.
```

Its coefficient at `s^n` is exactly `[q_n dX]`.  This is the correct object
that contains the nonlinear remainders after T3.  It was not wholly new at
2259Z: the sealed baseline already called for an assembled algebraic
four-sector section and a creative-telescoping/finite-reduction theorem
(`…2137Z-synthesis-sol.md:115-163`,
`…2137Z-opus5-crossreview-fable5.md:286-320`).  What is new is the sharper
typing supplied in different ways by the three reports.

The winner is therefore not “moving curve” versus “constant bundle.”  The
fixed cohomology bundle is the coefficient target; the selected algebraic
cover/Henselian component is what can prove holonomicity.  Those are two
descriptions of the same carrier.  Sol states that combination most cleanly,
but the present check of Sol is same-model and is not independent evidence.

The hostile claim verdicts are:

| Claim | Verdict | Short reason |
|---|---|---|
| Fable `GATE-CARRIER-PF` qualitative existence | **REPAIRABLE, NOT ESTABLISHED AS WRITTEN** | A branch-local Picard--Fuchs/direct-image object is legitimate, but Fable uses the full curve, does not isolate the `P(0)=p` component, and overreads R7R2 as supplying the identification. |
| Fable pointwise P-recursive gate coordinates | **PLAUSIBLE/EXPECTED AFTER REPAIR** | It needs an actual telescoping identity modulo `d_X`; regular holonomicity alone is not the emitted certificate. |
| Fable stratum-uniform `N0=k*+B` | **REJECTED** | Pointwise is fine once an operator exists; uniformity is not constructible merely from leading coefficients.  The family `b_B(k,a)=k-a` has an arbitrarily late exceptional integer root. |
| Fable `GATE-INV` | **REJECTED AS A KILL** | Monodromy-invariant vectors classify global horizontal solutions, not whether the specified section `kappa_F` equals its horizontal extension.  Local exponent-zero counts cannot decide the gate. |
| Fable `GATE-ALG-PRIM` (`GATE-ALG-PR` in the charge) | **NEW AND PROMISING, BUT FIELD-TYPED INCORRECTLY** | The one-way algebraic-primitive filter is real after adjoining `p`, selecting the Hensel component, and proving constant-field descent.  Strict extra cutting on this gate family is unproved. |
| Grok `CONST-BDL` | **CORE CONFIRMED, DISPLAY REQUIRES REPAIR** | `H^1(V_H)` is constant in `s`, and coefficientwise Deligne/Hermite reduction is the right finite receiver.  The displayed sector series has an off-by-two character error and omits the twist gauge if `V_j` means `H^1(U,nabla_j)`. |
| Grok order `<=dim V_j` | **UNSUPPORTED / FALSE-SHAPED** | Finite receiver dimension does not bound the differential order of an algebraic parameter-dependent section; even a scalar coordinate can have higher minimal order. |
| Grok `HESS-RETURN` coefficient | **FORMULA CONFIRMED** | The mixed quadratic coefficient and row placement are exact. |
| Grok `HESS-RETURN` as nonlinear obstruction | **DEMOTE TO VISIBILITY-ONLY** | At row 29 the rank-three new `F_7` map is already surjective on branch P, so the `F_6F_1` class can be cancelled; positive Hessian rank is not a cut. |
| Sol `HOL-GATE` carrier and Hensel branch | **INTERNALLY WELL-TYPED; SAME-MODEL ONLY** | The unit derivative `8p^7` gives the unique formal branch and the coefficient identity literally. |
| Sol Ore certificate `L_s(P^2dX)=d_XB` | **BEST-TYPED SUCCESSOR; SAME-MODEL ONLY** | It is exactly the proof-carrying bridge missing from raw P-recursion, subject to normalization/boundary bookkeeping and pointwise rather than uniform interpretation. |

The cheapest decisive successor is **not** `GATE-INV` and not a Hessian rank.
First compute the exact row-28 nonlinear class `[R_6 dX]` on one genuinely
licensed branch-P prefix; for `j=0` this is an ordinary residue calculation.
Then, only if a finite-control result rather than mere nonlinear nonvacuity is
wanted, emit one branch-local Ore certificate
`L_s(P^2dX)=d_XB` on the `r=1` control and replay it on one numeric P point.

## 1. Custody, evidence boundary, and hashes

At entry, the packet gate and every packet-listed custody hash matched, and
`HEAD` was

```text
418e413593120d19e15e6546eb50c985f4b1f038
```

The exact target/evidence hashes used were:

```text
8674f511a6a88801818c7ffda5f1fdfa52ac57e871e72757234a5d0a28291240  xmodel/ideation-20260827T2259Z-packet.md
d53c352d1e2bea8ae9c2b6e607c8224897d592718ee7297224d753c3c2814db2  xmodel/ideation-20260827T2259Z-fable5.md
5c97740394120d9a4d28a2663e73e5eac121df6acaa7561acb59a1a93cc2df53  xmodel/ideation-20260827T2259Z-grok46.md
58660b5180b73a599e826d349e4d663af9caa31a221837262844bf96fcec2a50  xmodel/ideation-20260827T2259Z-sol.md
d8a01725bc2730ce49069c96f4287956fb867b64e324ea6828076e19986e6b15  xmodel/ideation-20260827T2255Z-packet.md
668d78c96088d168361874733f81d7dee724769a6177a723bd0561e60ad850d0  xmodel/ideation-20260827T2137Z-synthesis-sol.md
b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a  xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md
5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55  xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md
8bad7ca04ae9a6f45efde305b208309f528173820250d20dab67d00bc32d73a4  xmodel/ideation-20260827T2137Z-postseal-exact-hostile-review.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
```

The packet-pinned `AUDIT.md` hash was
`aee767b1df96cdd466616b97e9fe4979332ff23434bbe80061f9413c2df2b7cf`
when the custody gate was checked.  During this review another process
prepended new canonical material, changing its hash to
`6644215f689a8648cf6ca0910890fd06657fecb1507800f0b8e4e2af8361a7d6`.
The original R7R2 block was unchanged, but a diff made the heading and summary
of a later `FIXED-RECEIVER GATE RECURRENCE` block visible.  That later block
and its underlying reports are **not evidence for this review**, are excluded
from novelty adjudication, and are disclosed as accidental post-freeze
contamination.  Every verdict below is derived from the sealed proposals and
the hashes above.

No `jc2-lean` path was entered, listed, searched, read, built, statused, or
modified.  No AWS or live job was contacted, no heavy local computation was
run, and no canonical file was edited.  This report is the only write.

## 2. The common object and the exact coordinate repair

The post-reversion algebraic equation and T3 baseline give

```text
P_F^8=sum_i F_i s^i P_F^i,       P_F(0)=p,
P_F^2=sum_n q_n s^n,
q_n=(1/4)p^(n-6)F_n+R_n(F_1,...,F_(n-1)).
```

On `A_H=K[X,p,p^-1]/(p^4-H)`, `partial_P R_F(p,0)=8p^7` is a unit.
Therefore formal implicit-function/Hensel gives a unique `P_F(s)` and hence
the exact fixed-bundle carrier

```text
kappa_F(s)=[P_F(s)^2dX] in H^1_dR(V_H)[[s]].
```

This validates Sol lines 115-162 and the core of Grok lines 99-117.  It also
supplies the missing branch selection behind Fable lines 385-420.

There is, however, a literal typing trap in Grok's displayed

```text
sigma_j(z)=sum_k [q_(j+4k)dX]z^k in V_j.
```

The promoted character law is `q_n^sigma=zeta^(n+2)q_n`, and row
`m=n+22` lies in character `m mod 4=n+2 mod 4`.  Thus `q_(j+4k)` is in
character `j+2`, not `j`.  Grok itself exposes the inconsistency: line 108
places `q_6` in `V_2`, while line 117 correctly calls row 28 a vector in
`V_0`.

There are two clean repairs.

1. Stay on the torsor and sector-extract `kappa_F` using characters
   `n+2 mod 4`.
2. If `V_m` literally denotes `H^1_dR(U,nabla_m)`, fix
   `b=n mod 4`, `m_0=b+22`, and use

   ```text
   C_b(z)=sum_(k>=0)
          [p^(-m_0)q_(b+4k)dX]_(V_(m_0)) z^k.
   ```

Indeed row `m=m_0+4k` has coefficient
`p^-m q_(b+4k)` in `V_m`; multiplication by `H^k` transports it to
`V_(m_0)` and gives exactly `p^-m_0 q_(b+4k)`.  This follows directly from
the sealed gauge identity `H nabla_(m+4)=nabla_m H`, without any later
result.

Fable and Sol avoid the off-by-two error by keeping the carrier in the whole
`H^1(V_H)`, although Fable's later `j` bookkeeping must still respect the
same shift.

## 3. Fable5: Gauss--Manin/Picard--Fuchs claim

### 3.1 What survives

Fable's combined action

```text
(y,s) -> (zeta*y,zeta^-1*s)
```

does preserve `y^8=F(sy)`, and `z=s^4` is a natural quotient coordinate.
The chosen branch gives a formal map from the constant torsor to the
algebraic surface, and under that map `y^2dX` pulls back to `P_F(s)^2dX`.
Thus period/creative-telescoping language is legitimate after the branch is
made explicit.  Algebraic direct image is also a plausible source of a
regular holonomic module and hence of pointwise scalar ODEs.

This is a useful realization of the already-known `GATE-REC` target, not a
new proof that gate coordinates are P-recursive.  The sealed baseline said
exactly that raw `(q_n)` is P-recursive while projection through de Rham
remains open (`…postseal-exact-hostile-review.md:122-152`).

### 3.2 What does not follow

Four distinct gaps invalidate Fable's stronger wording.

1. **Wrong-sized family until a component is selected.**  At `s=0`,
   `y^8-H^2=(y^4-H)(y^4+H)`.  The torsor `V_H` is one factor, whereas the
   full family `C_s` can also carry the other factor, vanishing cycles, and
   degree-jump behavior at infinity.  The equality “torsor period lattice =
   Gauss--Manin lattice of `C_s`” in lines 401-412 is not supplied by the
   torsor theorem.  One must base-change by `p`, complete at `P-p`, and
   isolate the Henselian component, as Sol does.
2. **R7R2 supplies regularity, not the client identification.**  The sealed
   R7R2 block says cyclic algebraic modules remain regular holonomic under
   algebraic direct image.  It does not prove that Fable's four
   `gamma_j` are sections of the asserted direct image, that the selected
   special-fibre cycles form the required submodule, or that specialization
   across `s=0` is harmless.  Those are the missing construction, not mere
   “canonical-extension bookkeeping.”
3. **“Fuchsian indicial data” is not the whole finite certificate.**  A
   usable decision needs the full operator/recurrence, startup indices,
   initial values, and every root of its forward coefficient.  The local
   exponent list at `z=0` alone does not provide these.
4. **No uniform `N0` follows by constructibility.**  For a fixed specialized
   operator, if `b_B(k)` is nonzero, its finite set of integer roots gives a
   pointwise bound.  Across a parameter `a`, the perfectly algebraic forward
   coefficient `b_B(k,a)=k-a` has an exceptional root at arbitrarily large
   nonnegative integer `a`.  Its union is countable and not handled by a
   finite descending induction on Zariski strata.  Fable lines 425-435 are
   therefore false at their stated stratum-uniform scope.  Grok and Sol are
   right to leave uniformity open.

Two lesser repairs matter for costing: “degree-`<=14` plane curve” in Fable
line 458 means at most degree 14 in `P/y`, not total plane degree when the
`F_i(X)` have nontrivial `X` degree; and clearing parameter denominators can
make a generic scalar operator specialize to zero, so polynomial
coefficients do not remove the need for specialization control.

Verdict: **branch-local pointwise PF is a sound target; Fable did not prove
it from the promoted material alone, and the uniform finite bound is wrong.**

## 4. Fable5 `GATE-INV`: why the proposed kill fails

The gate asks whether one specified section is constant/exact:

```text
kappa_F(s)=kappa_F(0)             (after the already-licensed q_0 gate),
```

or equivalently whether its Gauss--Manin derivative vanishes under a valid
trivialization.  Monodromy invariants answer a different question: which
initial vectors admit global single-valued horizontal continuations.

Locally on a nonsingular disc every initial vector has a horizontal lift,
whether or not the given algebraic section `kappa_F` equals that lift.
Globally, an invariant vector gives a horizontal section, but it still does
not identify that horizontal section with `kappa_F`.  Conversely, the gate
already fixes the initial background, so proving that the invariant space is
spanned by that background does not exclude survival; it merely says that a
survivor, if horizontal globally, uses the only vector it was required to
use anyway.

Consequently:

- the “background only => stratum kill” inference in Fable lines 279-301 is
  invalid;
- counting exponent-zero non-logarithmic slots at `z=0` is at most a bound
  on local horizontal solution shape, not a test of `nabla_s kappa_F=0`;
- two numeric fibres cannot establish the invariant-space statement on a
  parameter stratum; and
- an irreducibility/connectivity check at finite singular values does not
  repair the missing equality with the specified section.

`GATE-INV` is genuinely new relative to the sealed baseline, but novelty does
not rescue its type.  **Reject the card as a gate kill.**  Monodromy can still
be used after an Ore/PF operator exists to study that operator's solution
space; it is not the first discriminator.

## 5. Fable5 `GATE-ALG-PRIM`

The displayed form is algebraically motivated and its index shift checks:

```text
alpha_F=-(s^21/16)(partial_s(s^2Q)-2p^2s)dX
       =sum_(n>=1) -(n+2)q_n s^(n+22)dX/16.
```

By R7R1, an actual polynomial pair has
`w_(n+22)'=-(n+2)q_n/16`; after removing the `w_22` term and the
`X`-constant coefficients below it, the algebraic `W=G/P^12` supplies an
algebraic primitive of `alpha_F` beginning at `s^23`.  Thus the intended
one-way necessity is real.

The report's field is nevertheless wrong as written.  `alpha_F` contains
`p^2`, while `K(F)(X,s,P)` need not contain the chosen fourth root `p` or
select the specialization `P(0)=p`.  Moreover actual `W` initially lives
after extension of constants by the `G` coefficients.  A typed statement is:

```text
alpha_F is d_X-exact on the localization/completion of
K(F)(X,p,s,P)/(p^4-H, R_F(P)) at P-p,
```

with a base-change/descent lemma showing that exactness after adjoining the
actual `G` constants descends to the F-only constant field.  Algebraic de
Rham base change makes that repair plausible, but Fable does not state or
prove it.

The logarithm control correctly shows that coefficientwise rational
primitives need not assemble algebraically.  It does **not** prove that the
filter cuts strictly more on this particular gate family.  Replace “a priori
strictly stronger” by “formally stronger and potentially strict here.”
Also, on a positive-genus algebraic function field, ordinary residues alone
do not decide exactness; the promised Hermite/algebraic-integration routine
must retain the complete reduced de Rham remainder, including second-kind
classes.

Verdict: **new, useful necessary filter after a small but mandatory field and
branch repair; no equivalence, no demonstrated extra cut, and no endpoint
decision.**

## 6. Grok46 `CONST-BDL` and Hermite--Deligne claim

Grok's main correction to Fable is substantively right:

- `V_H` depends on fixed `H`, not on `s` or `F_i` for `i>=1`;
- `kappa_F` can be viewed as a section of the constant bundle
  `H^1(V_H)[[s]]`;
- high raw pole order can be reduced coefficientwise to a fixed finite
  logarithmic/Deligne normal-form space; and
- this reduction, not naive application of an `X`-dependent raw recurrence,
  is the missing compatibility step.

But “moving Picard--Fuchs is the wrong complexity class” (Grok lines 103 and
256-260) is too strong.  The section is algebraic only because `P_F` lies on
an algebraic cover.  Creative telescoping/direct image on that selected cover
is the natural proof that its fixed-bundle coordinates are D-finite.  The
constant receiver and the moving algebraic source are complementary, not
contradictory.

Besides the sector error in section 2, two claims need demotion.

1. Coefficientwise Hermite reduction alone does not imply a recurrence: an
   arbitrary sequence in a finite-dimensional vector space need not be
   P-recursive.  Algebraicity plus a certified telescoper is the extra
   theorem.  Grok honestly lists D-finiteness as conjectural at lines 266-270,
   so the carrier survives while the proof claim remains open.
2. An order bound `<=dim V_j` has no basis.  Receiver dimension counts class
   coordinates, not the differential complexity in `s`; a single scalar
   coordinate of an algebraic family can require order greater than one.
   A legitimate bound must also see algebraic-cover degree, pole divisor, and
   reduction-space size.

For row 28 specifically, `j=0`, so ordinary residues on
`U=A^1-Z(H)` do give a cheap complete coordinate test.  Grok's proposed
general “residue-vector service” must not silently extend that statement to
all twisted sectors without emitting the chosen Deligne basis and an exact
normal-form certificate.

Verdict: **the constant-bundle insight is confirmed after the sector/gauge
repair; it does not displace branch-local direct image and does not itself
prove finite control.**

## 7. Grok46 `HESS-RETURN`

The algebra is correct.  For `n!=ell`, `N=n+ell`, expansion of
`q_N=2/(N+2)[t^N]F^((N+2)/8)` gives

```text
[F_n F_ell]q_N
  =(1/4)((N+2)/8-1)p^(N-14)F_nF_ell.
```

For `(n,ell)=(6,1)`, this is
`(1/32)p^-7 F_6F_1` in row `N+22=29`, character one.  At the frozen
`F_1=H` fixture it becomes `(1/32)p^-3F_6`; equivalently the sector
`H`-exponent improves from `-2` before specialization to `-1` after using
`F_1=H`.  It remains polar, so T3's polynomial exactness argument does not
kill it.

Three semantic repairs are mandatory.

- The tower map takes values in an infinite product/series of repeated
  receivers, not merely `product_j V_j` as displayed at Grok lines 133-139.
- T3 kills the newest-slot derivative in its own row.  It does not put
  `F_6` in the kernel of the full tower differential: at a point with
  `F_1!=0`, the row-29 derivative in the `F_6` direction is already this
  mixed term.  Calling it the “first nonvanishing Hessian” is accurate only
  as a mixed second derivative at the all-positive-slots-zero origin.
- Most importantly, branch P's row-29 newest-slot `F_7` map has rank three
  into the three-dimensional receiver.  Hence every value of
  `kappa_(6,1)(F_6,H)` can be cancelled by choosing `F_7`.  Positive rank
  proves first *visibility*, not a nonlinear gate cut or survivor
  restriction.

The coefficient formula and the explicit bilinear map are genuinely new
relative to the sealed baseline.  Their strategic value is lower than Grok
claims.  The first honest nonlinear obstruction candidate is still row 28:
there the `F_6` linear class is zero and the remainder `R_6(F_1,...,F_5)`
cannot be cancelled by the newest slot.

## 8. Sol `HOL-GATE` — same-model screen only

Sol's lines 115-174 give the cleanest synthesis:

1. work over `A_H`, so `p` and the fixed torsor are present;
2. select `P_F(0)=p` by the unit derivative `8p^7`;
3. keep `kappa_F` in fixed `H^1(V_H)`; and
4. ask for the proof-carrying identity
   `L_s(P^2dX)=d_XB` in the normalized algebraic function field.

That identity would indeed certify de Rham-compatible creative telescoping
and yield a pointwise P-recurrence after branch selection.  It resolves the
false opposition between Fable and Grok.

This remains a proposal, not a sealed theorem.  `Z_F localized over V_H`
must be replaced by an explicit base-changed normalization/open pair, the
total `s` derivative in its function field must be specified, and poles at
`H=0`, the discriminant, and infinity must be tracked in the certificate.
Sol acknowledges this at lines 176-189.

Sol is also correct not to claim a uniform bound, but its suggestion that a
comprehensive constructible stratification will suffice needs the same
integer-root warning as Fable: finite algebraic stratification controls rank
drops and denominator loci, not an arbitrarily late root such as `k-a` over
all parameter values.  The safe theorem target is pointwise, or uniform only
after a separate structural bound on exceptional indices.

Because reviewer and producer share the Sol model family, this section is an
internal consistency screen and cannot promote `HOL-GATE` by itself.

## 9. Exact overlap, novelty, and contradiction matrix

| Feature | Fable5 | Grok46 | Sol | Resolution |
|---|---|---|---|---|
| Raw carrier | `c(s)=sum[q_n]s^n` | sector series `sigma_j` | `kappa_F=[P_F^2dX]` | Same object; Grok needs the two-step sector shift/gauge repair. |
| Fixed receiver | Implicit via `H^1(V_H)` | Explicit central claim | Explicit | Confirmed. |
| Algebraic source | Full `y^8=F(sy)` family | Downplayed as wrong complexity | Hensel-selected component of `R_F=0` | Sol's selected-component formulation reconciles the two. |
| Finite control | PF/Fuchsian operator | Hermite--Deligne telescoper | Ore exactness certificate | Same `GATE-REC` target; Sol gives the sharpest certificate format. |
| Uniform family prefix | Asserted constructible | Explicitly open | Explicitly open, stratification proposed | Fable contradicted; even finite constructible stratification needs an extra integer-index bound. |
| Monodromy kill | `GATE-INV` | Rejects reopening without ODE | Not proposed | Fable's implication is invalid even after an ODE exists. |
| Algebraic assembly | `GATE-ALG-PRIM` | Not proposed | Notes polynomial descent remains separate | Fable card is genuinely additional and one-way. |
| First nonlinear jet | Not explicit here | `HESS-RETURN` | General higher derivatives of `kappa` | Formula new, but row-29 surjectivity makes it visibility-only. |

Novelty against the sealed baseline, not against later concurrent work:

- **Not new at direction level:** an algebraic assembled four-section gate
  carrier, creative telescoping/Picard--Fuchs, and the need for singular-index
  control.
- **Fable-new:** the explicit combined `mu4` action on `y^8=F(sy)`, the
  monodromy-invariant proposal (rejected), and the algebraic-primitive filter
  (repairable).
- **Grok-new:** the explicit constant-bundle/Deligne normal-form emphasis and
  the mixed quadratic kernel formula (both need the scope repairs above).
- **Sol-new as formulation:** the chosen Hensel component and literal Ore
  exactness certificate; no independent verdict here.

## 10. Cheapest decisive successor

### Stage 1 — `R28-CLASS`, desk-scale and genuinely first

Use one **actual licensed** branch-P prefix through row 27.  Compute

```text
q_6=(1/4)F_6+R_6(F_1,...,F_5),
[q_6dX]=[R_6dX] in H^1_dR(U,d),
```

because row 28 has character zero and the polynomial `F_6/4` is exact.
Reduce `R_6dX` to its exact residue vector at the four roots of the branch-P
radical plus infinity.

- A nonzero vector is a rigorous witness that nonlinear carry is real and
  kills that prefix.  It immediately refutes any practical “whole row 28 is
  vacuous” hypothesis.
- Zero at one numeric point says only that this point survives row 28.  A
  claim of generic or stratum-wide vanishing requires symbolic reduction in
  the relevant component coordinate ring; random zeros are non-evidence.

This is cheaper and more decisive about post-T3 nonlinearity than
`HESS-RETURN`, because no later newest slot can cancel it.  It does not prove
finite control.

### Stage 2 — `HENS-CT`, the finite-control discriminator

Only after the carrier is typed, use the selected field

```text
K(X,p,s,P)/(p^4-H, R_F(P)), completed/localized at P-p,
```

and require an exact certificate

```text
L_s(P^2dX)=d_XB.
```

Run it first on `H=(X-a)^8`, where `V_H` is four punctured lines and class
coordinates are literal residues.  Replay the resulting recurrence against
independently generated `q_n` coefficients, including row 28 and one
nonlinear mutation.  If it passes, repeat at one frozen numeric P point.

Promote only:

- the exact branch and normalization used;
- the operator and `B` certificate;
- the complete startup/forward-coefficient exception list; and
- a **pointwise** deciding prefix.

Stop on disagreement between two exact reductions.  Do not raise the order
cap, invoke monodromy, or claim a cell-uniform `N0` until the certificate and
an independent exceptional-index theorem exist.

## 11. Scope and final ledger

Confirmed by hand from sealed formulas: the Hensel unit derivative, the
carrier coefficient identity, the two-step character correction, the mixed
quadratic coefficient, its `(6,1)` specialization, and the pointwise versus
uniform recurrence distinction.

Not checked by computation: no residue vector, telescoper, Picard--Fuchs
operator, monodromy matrix, algebraic primitive, or recurrence was generated.
No claim about generic nonlinear nonvacuity, row independence, polynomial
descent, `D22=1`, a genuine endpoint, landing, family exclusion, or JC2 is
licensed.

Accidental contamination is exactly the concurrent `AUDIT.md` heading and
summary disclosed in section 1.  No underlying later report was opened or
used.  The report remains different-model evidence for Fable5/Grok46 only,
and same-model non-evidence for Sol.
