# Hostile review: coordinate-fibre connectedness theorem

Date: 2026-08-31 UTC
Reviewer: Grok 4.6 (independent different-model adversarial referee)
Charged packet (frozen copy): `block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md`
Supporting frozen inputs: wild-valuation structure packet; wild-valuation pre-review
Producer: Sol 5.6 Ultra

No charged file was edited. No canonical ledger was edited. `jc2-lean` was not inspected. No CAS was used. Arithmetic is desk-level. No exit price is asserted.

## 0. Custody and hash verification

Frozen copies were hashed before mathematical reading. All three matched.

```text
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474
  .../block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5
  .../block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
8abde87c3e9320ae1b75e90d4c4c26e4a7a16dc685398bf446b5b33b230f9787
  .../block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
```

The connectedness packet additionally names a prior valuation hostile review among *its* frozen inputs. That file is not among the three copies charged to this review and is not used below. Exhaustivity was checked in the two supporting charged files. No CAS was run.

## 1. Disposition

The connectedness theorem is **PROVED**.  For the charged pair on the exact
ring, `C(f)` and `C(g)` are algebraically closed in `K=Frac(R)`, so each
general coordinate fibre is geometrically integral.  The intrinsic argument
from rationality, `R^*=C^*`, and `{f,g}=kappa` survives every attack below.
The constant bracket is used once, non-decoratively.  Degree four is not
used for primitivity.

The pre-review's boundary route is correctly typed `OPEN` at
census-exhaustivity: that interface is absent from the two supporting frozen
inputs, and the intrinsic proof does not use it.  Riemann--Hurwitz (2.5)
follows from connectedness plus total mate degree four.  The partition table
and (3.2) still consume the structure packet's general-slice ledger (3.1);
connectedness alone does not produce `d_h`.  Special fibres remain `OPEN`.

```text
C(f)^alg ∩ K = C(f)                                   CONFIRMED
C(g)^alg ∩ K = C(g)                                   CONFIRMED
general C_h geometrically irreducible                 CONFIRMED
boundary route OPEN at exhaustivity                   CONFIRMED
(2.5-repaired) from connectedness                     CONFIRMED
(3.2)/table from connectedness+(3.1)                  CONFIRMED
(3.6) consistency clause                              CONFIRMED
OPEN[SPECIAL-FIBRES]                                  CONFIRMED
"cofinite pi(S)" as written                           GAP (wording)
```

Hardest failed attack: a quadratic intermediate field `C(t)` with `f=t^2`
and `t in R`.  It dies at `P'(t)=2t in R^*`.  Next hardest: two punctures
giving `O(T_f)=C[t,t^{-1}]`.  It dies at `R^*=C^*`.  Hardest surviving
correction: the word "cofinite" for `pi(S)`.

## 2. Weakest exact hypotheses

Let `C` be algebraically closed of characteristic zero, and let

```text
R = C[A,U,Z]/(U^2-A-A^2 Z),          K = Frac(R).
```

Assume `f,g in R` with `{f,g}=kappa in C^*`, where `{,}` is a Poisson
bracket on `R` (equivalently `X_g` is a `C`-derivation of `R` and
`X_g(f)=kappa`).  No further input is required for algebraic closedness of
`C(f)` and `C(g)` in `K`: not `[K:C(f,g)]=4`, not a model `Y`, not a branch
curve `B`, not a fibre census, and not non-local-finiteness.

Degree four is required only for the repaired identities of §5.  The
general-slice ledger (3.1) is an additional consumed input for (3.2) and the
four-row table.  Etaleness of `pi=(f,g)` on `S=Spec R` is not an extra axiom:
it follows from smoothness of `S` and `kappa != 0`.

## 3. Main argument: relative algebraic closure of `C(f)`

Put `E_f=C(f)`, let `L_f` be the algebraic closure of `E_f` in `K`, and write
`delta_f=[L_f:E_f]`.  Write `T_f` for the normalization of `A1_f` in `L_f`
and `Tbar_f` for its smooth projective model.

### 3.1 Ring facts, independently of `f,g`

The polynomial `q=U^2-A-A^2 Z` is degree one in `Z` with content
`gcd(A^2,U^2-A)=1` in `C[A,U]`, hence irreducible.  So `R` is a domain and
`dim R=2`.

The Jacobian is `(q_A,q_U,q_Z)=(-1-2AZ, 2U, -A^2)`.  Vanishing forces `A=U=0`,
whence `q_A=-1 != 0`.  Thus `S` is smooth, so `R` is regular, hence normal.
This does not use etaleness of `pi`.

On `D(A)` one has `Z=(U^2-A)/A^2`, so `R_A ≅ C[A,A^{-1},U]` and `K=C(A,U)`.
In particular `K` is purely transcendental of degree two.

### 3.2 Units

A unit of `R` remains a unit in `R_A`.  The ring `C[A,A^{-1}][U]` has unit
group `C^* · A^Z`, so the image is `c A^n` in `K`.  The height-one prime
`P=(A,U)` has `R/P ≅ C[Z]`.  In the DVR `R_P` the relation
`U^2=A(1+AZ)` and `1+AZ notin P` give `P R_P=(U)`, hence

```text
ord_P(U)=1,     ord_P(A)=2.
```

A global unit has order zero at `P`, so `n=0` and `R^*=C^*`.  The same
conclusion follows from the charged completion `R^_P=C[Z][[u]]` with
`A=u^2+O(u^4)`, but the DVR computation does not need that isomorphism.

### 3.3 Structure of `L_f`

The extension `K/C` is finitely generated, so `L_f/E_f` is finite.  Separability
is free in characteristic zero.  The tower `C(f,g) subset L_f(g) subset K`
shows `delta_f` divides `[K:C(f,g)]` whenever that degree is finite, but the
killing argument never uses the integer 4.

Transcendence: `g` is transcendental over `L_f`, else `K` would have
transcendence degree one over `C`.

The inclusion `L_f subset K=C(A,U)` is a dominant rational map `A2 --> Tbar_f`.
A general line meets the domain of definition in a nonconstant rational map
`P1 --> Tbar_f` (some element of `L_f` is a nonconstant rational function of
`(A,U)`).  Luroth for curves therefore gives that `Tbar_f` is rational, hence
`P1` over `C`.  The parenthetical "generalized Luroth" in the packet is the
curve case, not the false several-variable statement.

### 3.4 Affine ring inside `R`

The ring `O(T_f)` is the integral closure of `C[f]` in `L_f`.  Any `t` in
that ring is integral over `C[f] subset R` and lies in `K`.  Normality of `R`
puts `t` in `R`, so `O(T_f) subset R` and `O(T_f)^* subset R^*=C^*`.

The packet's appeal to normality of `Y` is superfluous for this inclusion.
The factorization `Y -> T_f x A1_g -> A2` is used only by the unused
boundary route.

### 3.5 One puncture

`T_f` is `P1` minus the points of `Tbar_f` over `f=infinity`.  A finite
morphism of projective curves is surjective, so at least one point is
removed.  If two or more points are removed, `O(T_f)` has a nonconstant unit:
after sending one removed point to infinity the coordinate minus a second
removed value is invertible, and already `P1 minus two points` is `G_m`.
This is forbidden by `R^*=C^*`.  Hence exactly one point is removed,

```text
O(T_f)=C[t],           f=P(t) in C[t],           deg P = delta_f.
```

The last equality is `[C(t):C(P(t))]=deg P`.  Injectivity of `C[t]->R` holds
because `t` is transcendental over `C` and `R` is a domain.  Here `t in R`.

Riemann--Hurwitz on `Tbar_f -> P1_f` is *not* used.  It would only force some
finite ramification if `delta_f>1`; the intrinsic argument replaces that
branch by units plus the bracket.

### 3.6 Where `kappa` is used

The identity `{P(t),g}=P'(t){t,g}` is the chain rule for the derivation
`X_g`.  Both factors lie in `R`: `P'(t)` is a polynomial in `t in R`, and
`{t,g}=X_g(t) in R`.  Their product is the unit `kappa`, so each factor is a
unit of the domain `R`.  Thus `P'(t) in R^*=C^*`.  Because `C[t]->R` is
injective, the polynomial `P'` itself is a nonzero constant.  Characteristic
zero then forces `deg P=1`, hence `delta_f=1`:

```text
C(f)^alg ∩ K = C(f).
```

Without `kappa in C^*` the same rationality-and-units analysis still produces
`f=P(t)` with `t in R`, but `deg P` need not be one.  That is the classical
disconnected-fibre picture `f=t^2` on a polynomial ring.  The constant
bracket is therefore necessary and is used at exactly this line.  It is
equivalent, given `R^*=C^*` already proved, to the Jacobian of `(f,g)` being
a unit of `R`.

Standard spreading-out in characteristic zero now gives geometric integrality
of `C_f=V(f-a)` for all `a` in a nonempty Zariski open of `A1`.  Smoothness
of those fibres is separate: `S` is smooth and `d(f,g)` is invertible, so
`pi|_S` is etale, the projection `A2->A1_f` is smooth, and `f:S->A1` is
smooth.  A smooth curve is connected if and only if it is irreducible.

### 3.7 Attacks that fail

- *Relative algebraic closure not finite.*  False for a finitely generated
  extension.
- *`Tbar_f` of positive genus.*  Unirational curves over `C` are rational.
- *`O(T_f)` not inside `R`.*  Needs only normality of `R`, which is the
  empty Jacobian locus of `q`.
- *`P'(t)` a nonconstant polynomial which becomes a unit in `R`.*  Forbidden
  by `R^*=C^*` together with injectivity of `C[t]->R`.
- *Degree four essential for primitivity.*  Unused.
- *Silent use of `(BC)`.*  Section 3.3 of the packet never mentions `B`,
  `Y-S`, or a vertical line.  It uses only the ring inclusion from 3.2,
  which does not use `(BC)`.

## 4. Candidate intermediate field

**Candidate A (one puncture, polynomial of degree `>1`).**  Let `delta_f=2`,
`L_f=C(t)`, `O(T_f)=C[t] subset R`, and `f=t^2` after an affine change of
`t` (complete the square in characteristic zero).  Then
`kappa={f,g}=2t{t,g}`.  The factor `2t` lies in `R` and must be a unit, so
`t in C^*`, contradicting transcendence of `t`.  The same kill applies to
any `P` of degree `2` or `4`.  This is the unique point at which `kappa`
is needed.

**Candidate B (two punctures).**  Let `T_f ≅ G_m`, `O(T_f)=C[t,t^{-1}]`,
and `f=t+t^{-1}` (the standard degree-two map `G_m->A1`).  Then `t` is a
nonconstant unit of `O(T_f) subset R`, contradicting `R^*=C^*`.  The
bracket is not reached.

**Candidate C (subfield `C(A)`).**  The field `C(A)` is algebraically closed
in `C(A,U)=K`.  If `C(A) subset L_f` then `f in C(A) ∩ R`.  An element
`P(A,Z)+U Q(A,Z)` of `R` lies in `C(A)` only if `Q=0` and `P` is independent
of `Z`, so `f in C[A]`.  Then `kappa=f'(A){A,g}` forces `f'(A) in R^*=C^*`,
hence `f` is affine in `A` and `L_f=C(A)=C(f)`.  The candidate survives only
in the trivial case already allowed by `delta_f=1`.

No other isomorphism type exists: rationality plus `R^*=C^*` reduce every
nontrivial `L_f` to Candidate A or B.

## 5. Symmetry for `g`

Interchange `f` and `g`.  The ring, its fraction field, its unit group, and
normality are unchanged.  Skew-symmetry sends `{f,g}=kappa` to
`{g,f}=-kappa in C^*`.  If `g=Q(t)` with `t in O(T_g) subset R`, then
`kappa=Q'(t){f,t}` and `Q'(t)` is a unit of `R`, hence constant, hence
`deg Q=1`.  Nothing in §§3.1--3.6 prefers a coordinate.  The unused
boundary route would swap vertical lines for horizontal lines; the intrinsic
route does not.

**Verdict: CONFIRMED.**

## 6. Boundary route and `OPEN[census-exhaustivity]`

The packet's `(BC)` is: every ramified prime divisor of `Y-S` maps into `B`.
A search of the two supporting frozen inputs for a statement of that
strength, or of the phrase "sole irreducible nonvertical boundary image",
finds neither.

What those files actually contain:

- Structure, definition of `R_bd=Y-S` as "the ramification boundary" of the
  finite normalization `Y->A2`.  This names `Y-S`; it does not list its
  irreducible images.
- Structure, "unique ramified factor" of the completed fibre over the
  *generic point of `B`*, i.e. uniqueness of the ramified sheet in the
  partition `(2,1,1)`, not uniqueness of `B` among branch components.
- Structure, "`B` is neither a vertical nor a horizontal line".  A property
  of `B`, not an exclusion of extra components.
- Structure lines 387--412, the consumed rank-four census
  `generic B:(2,1,1)`, `c:(3,1)`, `n:(2,2)`, together with the general-slice
  clause "there are no other finite deleted points".  The listed types are
  fibre types along `B`, `c`, and `n`.  They are not stated as an exhaustive
  partition of all points of `A2`, and a general-slice emptiness statement
  cannot see a vertical component supported at one exceptional `a_f`.
- Pre-review line 101, the unproved sketch that a vertical ramified divisor
  would contradict "the sole irreducible nonvertical boundary image `B`".
  That is the only occurrence of the sole-image language, and it is
  explicitly a proposed repair, not a frozen theorem.

The control `A2->A2`, `(x,y)|->(x^4+x,y)` restricted to `D(4x^3+1)`, is
correctly a counter to inferring `(BC)` from a cofinite or even surjective
image: deleted ramification still maps onto vertical lines while retained
sheets cover those lines.  It is not claimed to realize `R`.

Section 3.1 of the packet (Stein/RH forcing a finite ramified value) is
correct as a statement about covers of `P1`, and the production of a divisor
`D` of `Y` with `pi(D)={f=a}` is correct given the factorization through
`T_f x A1_g`.  The last implication `pi(D) subset B` is exactly `(BC)` and
is not supplied.  Typing

```text
OPEN[census-exhaustivity-f]
OPEN[census-exhaustivity-g]
```

is therefore accurate, and the intrinsic proof does not fill the gap by
cap or analogy.

One related but distinct consumption: structure (3.1) uses the general-slice
"no other finite deleted points" clause to set `s_fin=deg(f o beta_B)`.  An
extra *horizontal* or *non-coordinate* ramified component would pollute a
general `f`-fibre, whereas an extra *vertical* component would not.  The
packet's §7 OPEN is the full statement that `B` is the entire branch image,
which is stronger than the vertical-only interface of the `f`-boundary
route.  That stronger OPEN is correctly recorded; it is not an input to
primitivity.  It is an unclosed hypothesis of consumed (3.1), recorded in
§7 below.

## 7. Repaired identities and partition table

Assume now `[K:C(f,g)]=4`, so the completed mate has degree four, and assume
`Cbar_h` is connected of genus `gamma_h` by §§3--5.

### 7.1 (2.5)

On each completed fibre the local formulae (2.1)--(2.3) of the structure
packet remain componentwise: at a finite place `D=(kappa/e)z^{1-e} partial_z`,
at infinity `D=-(kappa/e)z^{e+1} partial_z`.  Summing,

```text
deg Zero(X_h|C_h) = sum_{Sigma_infty}(e_p+1) = 4+r_h,
```

using `sum_{infty} e_p=4`.  A meromorphic vector field on a connected smooth
projective curve of genus `gamma_h` has `deg div = 2-2gamma_h`, so

```text
deg Pole = (4+r_h) - (2-2gamma_h) = 2gamma_h+2+r_h.
```

Riemann--Hurwitz is the same identity: `2gamma_h-2=-8+sum_all(e_p-1)` with
`sum_infty(e_p-1)=4-r_h` recovers the pole sum `2gamma_h+2+r_h`.  This is
(2.5-repaired).  It uses connectedness and degree four, not (3.1).

The pre-review's multi-component ledger is

```text
deg Zero = 4+r,     deg Pole = 2G+4-2delta+r,     deg div = 2delta-2G,
d = 2G+4+r-2delta   (under (3.1)).
```

At `delta=1` and `G=gamma` these collapse exactly to (2.5-repaired) and,
once (3.1) is used, to (3.2-repaired).  The specialization is arithmetic, not
an extra geometric hypothesis.

### 7.2 (3.2) and the four rows

Connectedness does not identify the finite places with the intersections
against `B`.  That is structure (3.1): after avoiding the finite bad set
`{c,n,Sing(B),Sing(Y)}` union critical values of `h o beta_B` union
tangencies, every finite deleted place is transverse of index two and
`s_fin=d_h=deg(h o beta_B)`.  Then the pole sum equals `d_h`, so

```text
d_h = 2gamma_h+2+r_h.                                 (3.2-repaired)
```

The pole orders of the mate over infinity form a positive partition
`lambda_h` of four of length `r_h`.  The complete list is

| `r_h` | `lambda_h` | necessary `d_h` |
|---:|---|---:|
| 1 | `(4)` | `2gamma_h+3` |
| 2 | `(3,1)` or `(2,2)` | `2gamma_h+4` |
| 3 | `(2,1,1)` | `2gamma_h+5` |
| 4 | `(1,1,1,1)` | `2gamma_h+6` |

These are all positive partitions of 4.  The rows are necessary, not
sufficient, and give no relation between the two coordinates.

**Verdict:** (3.2) and the table are **CONFIRMED** as consequences of
connectedness plus consumed (3.1).  They are **not** consequences of
connectedness alone.  The packet states the consumption; it does not smuggle
(3.1) out of the new primitivity argument.

### 7.3 (3.6) and the consistency clause

A supplied tuple is excluded if

```text
d_f<=2 or d_g<=2;
d_h-r_h-2 notin 2Z_(>=0) for some h;
gamma_h != (d_h-r_h-2)/2 for some h;
lambda_h is not a positive partition of 4 of length r_h.
```

The third line is the missing test.  Equivalently define
`gamma_h=(d_h-r_h-2)/2` and do not record an independent genus.  The
pre-review's counter-tuple `(d,r,gamma,lambda)=(5,1,17,(4))` passes the
three old tests (`d=5>2`, `d-r-2=2 in 2Z_(>=0)`, `lambda=(4)` of length 1)
and violates (3.2) because `2*17+2+1=37 != 5`.  The new clause excludes it
because `(5-1-2)/2=1 != 17`.

The first line `d_h<=2` is (3.2) plus `gamma_h>=0`, `r_h>=1`: the minimum
is `d_h=2*0+2+1=3`.  It is redundant once the consistency clause and
`r_h>=1` are enforced, but it is a correct necessary filter.

**Verdict: CONFIRMED.**

### 7.4 Provenance of (2.6)

Once a finite ramified place exists, the local calculation (2.6) is
unchanged.  Connectedness plus (2.5) gives pole sum `2gamma_h+2+r_h>=3>0`,
so such a place exists without (3.1).  Independently, a general transverse
meeting with noncoordinate `B` supplies an index-two place if `d_h>0`.
Either route is valid.  The overstatement that (2.6) follows from "degree
four alone" remains correctly withdrawn: a disconnected split control can
have vanishing finite ramification.

## 8. Special fibres, bad values, and §7 OPEN typings

The non-integrality locus of `f:S->A1` is a proper closed subset of `A1`,
hence finite.  At an excluded value the scheme fibre is still smooth and
reduced, because `f` is a smooth morphism, but the number of geometric
components is not determined by the charged data.  No connected single-genus
formula is claimed there.  That is the correct `OPEN[SPECIAL-FIBRES]`.

Nonemptiness does *not* follow from cofiniteness of `pi(S)`.  The image
`pi(S)` is typically the complement of a curve in `A2`, which is not
cofinite.  Nonemptiness does follow from `R^*=C^*`: `V(f-a)` is empty if
and only if `f-a` is a unit, hence constant, contradicting `{f,g}!=0`.
The same holds for `g`.  This is a wording defect in §3.4 of the packet,
not a defect in the theorem; see §9.

For the *table*, the exceptional set must be enlarged by the `h`-coordinates
of `c,n,Sing(B),Sing(Y)`, the critical values of `h o beta_B`, the tangency
values, and any coordinate-parallel branch values permitted by the
exhaustivity OPEN.  Outside that finite set, consumed (3.1) applies and the
completed mate is degree four with distinct transverse index-two finite
places.  At an excluded value the places must be recomputed on the
normalization of that fibre.  The packet states this.

The two §7 OPEN labels are correctly typed:

1. `OPEN[CENSUS-EXHAUSTIVITY]` belongs to the unused boundary route and to
   the consumed general-slice identification (3.1), not to primitivity.
2. `OPEN[SPECIAL-FIBRES]` is the component count and special-place ledger
   at the finite bad set.

No length-three cusp-boundary completion, no cusp Puiseux expansion, and no
existence theorem for any table row is supplied.  Those remaining OPENs from
the valuation packet are correctly left untouched.

The restatement of (1.11) and of the narrowed unmarked-germ wildness claim
matches the pre-review's safe replacement and is not re-litigated here.

## 9. Corrections, blast radius, and best falsification test

**Correction 1 (wording).**  Replace "cofiniteness of `pi(S)`" by the unit
criterion: `f-a` is never a unit.  Blast radius: the nonempty-fibre sentence
in §3.4.  The connectedness theorem and (2.5) are unaffected.

**Correction 2 (scope of the table).**  State explicitly that (3.2) and the
four rows consume structure (3.1) in addition to connectedness.  Blast
radius: none if the consumption already on the page is read literally;
misreading connectedness as a self-contained derivation of `d_h` would
illegally close the exhaustivity OPEN.

**Correction 3 (superfluous `Y`).**  The inclusion `O(T_f) subset R` uses
normality of `R` only.  Blast radius: none.

No correction to the primitivity argument is required.  No exit price is
asserted.

**Best next falsification test.**  The argument reduces every nontrivial
`L_f` to Candidate A or B.  Candidate B is a unit-group computation already
closed by `ord_P(A)=2`.  The remaining desk test is therefore Candidate A:
produce `t in R`, not in `C[f]`, with `f in C[t]` and `{f,g} in C^*`.
Equivalently, exhibit a nonconstant unit of `R`, or a nonconstant polynomial
`P in C[t]` of degree `>1` with `P'(t)` a unit of `R`.  Both are forbidden
by the identities in §3, so a genuine counterexample must break one of:
irreducibility of `q`, emptiness of the Jacobian locus, the identification
`R_A=C[A,A^{-1},U]`, or the chain rule for `X_g`.  Those four checks are
finite and do not require a model of `Y`.

A geometric restatement of the same test is: produce any pair on this ring
with constant Jacobian whose general `f`-fibre is disconnected.  The
classical polynomial example `f=t^2` on `C[t,s]` is available only if
`R^*` is larger than `C^*` or the Jacobian is allowed to vanish along `t=0`.

## 10. Per-claim verdicts

| Claim | Verdict | Attack |
|---|---|---|
| Frozen SHA-256 of the three charged copies | CONFIRMED | Recomputed; match. |
| `R` domain, `S` smooth, `K=C(A,U)` | CONFIRMED | Jacobian never vanishes; `q` irreducible of `Z`-degree one. |
| `R^*=C^*` | CONFIRMED | Units in `R_A` are `c A^n`; `ord_P(A)=2`. |
| `Tbar_f ≅ P1` | CONFIRMED | Unirational curve over `C`; Luroth. |
| `O(T_f) subset R` | CONFIRMED | Integral over `C[f]`, `R` normal. `Y` unused. |
| Exactly one puncture, `f=P(t)` | CONFIRMED | Two or more punctures produce a nonconstant unit. |
| `kappa` forces `deg P=1` | CONFIRMED | Chain rule; `P'(t) in R^*=C^*`; `C[t]->R` injective. |
| `{f,g}=kappa` needed, not decorative | CONFIRMED | Used exactly once; without it Candidate A lives. |
| `C(f)` algebraically closed in `K` | CONFIRMED | Candidates A--C killed as in §4. |
| Same for `C(g)` | CONFIRMED | Symmetric; only the unused boundary route changes direction. |
| General `C_h` geometrically irreducible | CONFIRMED | Standard spreading-out from the generic fibre. |
| `(BC)` present in frozen supporting inputs | REFUTED | Not in structure or pre-review as a theorem; sole-image language is the pre-review sketch. |
| Main proof silently uses `(BC)` | REFUTED | Intrinsic proof never mentions `B`. |
| Boundary route `OPEN` at exhaustivity | CONFIRMED | Last implication of §3.2 of the packet is `(BC)`. |
| (2.5-repaired) | CONFIRMED | Connectedness + mate degree 4; matches pre-review at `delta=1`. |
| (3.2-repaired) and four-row table | CONFIRMED | Connectedness + consumed (3.1). Not from connectedness alone. |
| (3.6) consistency `gamma_h=(d_h-r_h-2)/2` | CONFIRMED | Excludes `(5,1,17,(4))`; necessary for (3.2). |
| (2.6) provenance | CONFIRMED | Finite ramification sum `>=3` from (2.5); local once a place exists. |
| Special fibres classified | OPEN | Smooth reduced, component count not charged. Packet types this. |
| `pi(S)` cofinite | GAP | Image omits a curve. Replace by `R^*=C^*`. No theorem damage. |
| Exit price | — | None asserted. |

Overall: the central claim is **CONFIRMED**.  The honest OPEN on the
boundary route is **CONFIRMED**.  The only GAP is the cofiniteness wording.

<!-- BODY-END -->
