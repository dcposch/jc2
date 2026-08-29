# Independent implementation audit: total-Rees `T-rs` chart

Date: 2026-08-26

Status: **AUDIT ONLY.  CURRENT CLIENT SPECIFICATION IS NOT LAUNCHABLE.  NO
TOTAL-REES, MOVING-`p`, OR CAMPAIGN VERDICT.**

## 0. Classification and custody

Every substantive assertion below is prefixed by one of:

- **[T] theorem**: proved here from stated hypotheses;
- **[S] frozen-source deduction**: literal deduction from the charged files;
- **[P] implementation proposal**: a fail-closed computation still to be run;
- **[U] unresolved**: not established by the frozen evidence.

No `AGENTS.md` exists in or above the repository.  I read every file charged
in the assignment completely.  The four principal pins recompute as
`6995a991...`, `22d32f18...`, `99e45e34...`, and `aaf20f09...`; the V2, V1,
and owner compiler pins recompute as `8abeda32...`, `feb37116...`, and
`9d499882...`. **[S]** The transitive source is the 569-monomial frozen
`tails.json` (`d72f774c...`, canonical digest `6eed03d4...`) consumed by the
owner through `compile_square_load_ladder.py`.  Inspection was read-only; no
CAS was run.

## 1. Standard chart and finite-prefix claims

Let `A` be a commutative ring, `I=(f_0,...,f_n)` a finitely generated ideal,
and

```text
R(I)=image(A[X_0,...,X_n] -> A[t]),  X_j |-> f_j t.
```

No noetherian hypothesis is needed for the following presentation.  On
`D_+(f_i t)`, define the degree-zero chart even when `f_i` is a zero divisor:

```text
C_i=(R(I)_(f_i t))_0=A[f_0/f_i,...,f_n/f_i] subset A[1/f_i].
```

Here the last algebra means the image in `A[1/f_i]`; if localization is the
zero ring, so is the chart. **[T]** For variables `y_j`, `j != i`, the map

```text
q:A[y_j] -> A[1/f_i],       y_j |-> f_j/f_i
```

has kernel

```text
ker(q)=(f_i y_j-f_j:j != i):f_i^infinity,           (1.1)
```

and its image is `C_i`.  Proof: after localizing at `f_i`, the displayed
linear relations eliminate all `y_j`.  Hence an element is in the kernel
exactly when some power of `f_i` puts it in the linear-relation ideal.
Equivalently (1.1) is the elimination ideal

```text
(f_i y_j-f_j, 1-u f_i) intersect A[y_j].            (1.2)
```

Thus the formula in the design is correct, including zero-divisor torsion.
The unsaturated bilinear quotient is only the symmetric presentation and is
not generally the Rees chart. **[T]**

The base-change warning is essential.  For `A -> B`, there is a natural
surjection

```text
R_A(I) tensor_A B -> R_B(IB),
```

but it need not be injective; consequently a total chart tensored with `B`
need not equal the chart constructed from `IB`.  Saturation and quotient do
not commute in general.  Equality must be tested scheme-theoretically, not
by radicals. **[T]** Flat base change is sufficient for equality of Rees
algebras (and hence charts); the specialization `rho=0` is not known flat on
the source or its Rees algebra. **[U]**

For a quotient `A_g -> A_full=A_g/L`, the induced map

```text
A_g[I/f_i] -> A_full[(I A_full)/bar(f_i)]            (1.3)
```

is surjective: its generators are the images of `A_g` and `f_j/f_i`.
This remains true if `bar(f_i)` is nilpotent or zero, using the image-in-
localization convention. **[T]** Therefore a certificate that makes an
element a unit at a finite prefix survives later quotient equations.  It
does *not* show that a prefix chart is the restriction of a correctly emitted
full source, that omitted jets cannot contribute to that prefix, or that
base change commutes with the chart. **[T]** The four extra hypotheses listed
in the obligation table are therefore necessary compiler obligations, not
consequences of (1.3). **[S]**

## 2. The intended Kummer substitution

The frozen owner literally emits

```text
p_frozen = 2*sigma*ell1 + 2*sigma^2*ell2 + 2*sigma^3*ell3,
c = sigma^2*(cs + sigma*cs1 + sigma^2*cs2),
r = (p_frozen^2 + sigma^2*(rs+sigma*rs1+sigma^2*rs2))/4.   (2.1)
```

Its quartic square factor is therefore

```text
K=z^4+p_frozen*z^2+c*z+r
 =(z^2+p_frozen/2)^2 + sigma^2*((cs+...)*z+(rs+...)/4).
```

This is a literal source convention, not an analogy. **[S]** The Kummer
central fibre in the successor design is `L_rho=z^2-rho^2`, so its total
extension must replace the *constant term* of `p_frozen`, not the whole
series:

```text
p_tot = -2*rho^2
        +2*sigma*ell1+2*sigma^2*ell2+2*sigma^3*ell3,       (2.2)
c_tot = sigma^2*(cs+sigma*cs1+sigma^2*cs2),
r_tot = (p_tot^2+sigma^2*(rs+sigma*rs1+sigma^2*rs2))/4.    (2.3)
```

At `sigma=0`, (2.2)--(2.3) give `K=(z^2-rho^2)^2`; at `rho=0` they recover
(2.1) exactly. **[T,S]** The instruction “extend ... to `p=-2*rho^2`” is
malformed if interpreted literally: it deletes `ell1,ell2,ell3`, changes the
frozen source, and cannot admit a two-sided specialization map. **[S]**

The root-value formulas in the successor design are also recovered exactly:
for `R(z)=cs*z+rs/4`, `C(z)=(c1*z+c0)/2`, and `A(z)=a1*z+a0`,

```text
R(+rho)=rs/4+cs*rho,   R(-rho)=rs/4-cs*rho,
C(+rho)=(c0+c1*rho)/2, C(-rho)=(c0-c1*rho)/2,
A(+rho)=a0+a1*rho,     A(-rho)=a0-a1*rho.           (2.4)
```

**[S]** No additional root-value variables are needed for `T-rs`; adding
them only enlarges the presentation and introduces redundant relations.
They are appropriate later on `D(rho)` if both orientations and the deck
action are checked. **[P]**

The currently frozen truncation has only the jets displayed in (2.1).
Whether those are all jets capable of affecting every coefficient through
grade 12 after (2.2) is not proved by any charged artifact. **[U]** A support
census must precede source generation; missing jets must cause failure, not
be silently set to zero. **[P]**

## 3. Extraction ring and grading

The old extractor is univariate only because `rho=0` was imposed in the
owner.  Its operation—successive exact division by `sigma`, followed by
`sigma=0`—remains valid over a coefficient ring containing an independent
`rho`. **[T]** No bivariate Rees homogenization is required merely to form
the polynomial family of `sigma` coefficients.  The smallest honest ambient
ring is

```text
Q[rho, sigma, z,
  ell1,ell2,ell3, cs,cs1,cs2, rs,rs1,rs2,
  a0,a1,aa0,aa1,aaa0,aaa1, c0,c1,e0,e1,ee0,ee1,
  k,k1,k2c,k6,k6_1,k2,k2_1,mu2,mu4,mu6,J]          (3.1)
```

augmented by every jet found by the census.  Use the `sigma` filtration
`deg_sigma(sigma)=1`, with `rho` and coefficient jets of degree zero for
coefficient extraction.  For diagnostics retain the independent bigrading
`deg(rho)=(0,1)`, `deg(sigma)=(1,0)`; do not collapse it by setting
`rho=sigma^m`. **[P]** The source polynomials obtained from the frozen tails
and (2.2)--(2.3) lie in the even subring `Q[rho^2,...]`. **[T]**

The extractor must first prove a common exact `sigma^N` divisibility and the
multiplication-back identity in (3.1), then define `G_{N,ell}` as the
coefficient in `sigma`.  It must never specialize `rho` before extraction.
**[P]** It is presently unresolved whether the first common order remains
exactly 10 over `Q[rho]`; the old `sigma^10` assertion cannot be copied from
the `rho=0` client. **[U]** If it does, the same iterative extraction yields
polynomial families `G10`, `G11`, `G12` in `rho`; otherwise the earliest
order discrepancy is the desired obstruction. **[P]**

## 4. Exact `D_+(rs)` computation and comparison

Let `P` be (3.1), let `E_12` be the complete set of raw coefficient equations
through grade 12 from the common emitter, and put `A_12=P/E_12`.  This is a
prefix only; it may be used because of (1.3) after completeness is certified.
**[P]** Introduce exactly

```text
qcs, qc0, qc1
```

with intended values `cs/rs,c0/rs,c1/rs`.  In `P[qcs,qc0,qc1,u]` compute

```text
L=(E_12,
   rs*qcs-cs, rs*qc0-c0, rs*qc1-c1,
   1-u*rs),
K_rs_tot=L intersect P[qcs,qc0,qc1].                (4.1)
```

Then

```text
C_rs_tot=P[qcs,qc0,qc1]/K_rs_tot                   (4.2)
```

is the actual total standard chart; localization at the registered `k` is
performed separately (or with another inverse variable) and every inverse
must be recorded. **[T,P]** Computing only the three bilinear equations is
forbidden.

Compute, in identical named variables,

```text
K_after = K_rs_tot + (rho),
K_before = saturation of
  (E_12|rho=0, rs*qcs-cs,rs*qc0-c0,rs*qc1-c1) by rs. (4.3)
```

Require reduced standard bases to prove literal ideal equality
`K_after=K_before`; print membership multipliers both ways.  A radical match
is failure. **[P]** Notice that `K_before` is only the blowup of the complete
literal specialization, not automatically the frozen cusp client.

Let `F_0` be the frozen raw `p=0` coefficient algebra through grade 12,
localized at `k*rs`.  The two maps required after (4.3) are

```text
alpha: (C_rs_tot/(rho))[1/k] -> F_0[1/(k*rs)],
       qcs |-> cs/rs, qc0 |-> c0/rs, qc1 |-> c1/rs;

beta:  F_0[1/(k*rs)] -> (C_rs_tot/(rho))[1/(k*rs)],
       every frozen source name |-> the identically named class.          (4.4)
```

Represent `1/rs` and `1/k` by registered inverse variables, not textual
fractions.  Validate both composites on every generator and prove equality
of the complete raw row ideals under both maps. **[P]** The reviewed identity

```text
32768*g12_6-35*k*rs^4
 =-4096*rs*g10_2-8192*cs*g10_3                  (4.5)
```

is an exact frozen-source theorem, and omitting `g10_3` leaves the nonzero
`-1536*cs*c0*c1`. **[S]** It supplies no part of (4.3)--(4.4). **[S]**

For a total lift, set

```text
Delta=32768*G12_6-35*k*rs^4
      +4096*rs*G10_2+8192*cs*G10_3.                (4.6)
```

After the source-map checks, `Delta|rho=0=0`, so polynomial division gives
`Delta=rho*H`; this is automatic in the ambient polynomial ring, not yet an
ideal certificate. **[T]** The validator must additionally express the
desired registered-unit numerator as

```text
s = sum_i H_i*Phi_i + rho*H_chart                   (4.7)
```

inside (4.2), with `s` a product of nonnegative powers of `k` and `rs` times
a nonzero rational constant.  Multiplication back in the unsaturated
polynomial presentation is mandatory. **[P]**

The `rho^2` sentinel requires a distinction.  Because (2.2)--(2.3), the
frozen-tail emitter, and (4.6) contain `rho` only through `rho^2`, the
*canonical polynomial difference* `Delta` is even; if its constant term
vanishes then `Delta` is divisible by `rho^2`. **[T]** This does not imply
that an arbitrary chart membership multiplier, elimination witness, or
representative of (4.7) is divisible by `rho^2`; redundant root-value
variables can visibly introduce odd terms. **[T]** Therefore require
`rho^2 | Delta` and multiplication back, but reject a blanket requirement
that every new chart coefficient or `H_chart` be `rho^2`-divisible.  The
stronger sentinel in the obligation table is false as stated. **[S,T]**

## 5. Compiler and validator contract

**[P] Compiler-level pseudocode:**

```text
verify every frozen and transitive SHA; require registered AWS host
load canonical tails; verify 569-term census and weights
discover_needed_jets(max_sigma_grade=12, rho_independent=true)
FAIL unless discovered jets equal an explicit manifest

define P over Q with rho,sigma independent
define pTot by (2.2); define cTot,rTot by (2.3)
emit all seven Phi from the frozen tails, all loads and targets included
assert subst(Phi,rho,0) == literal frozen-owner Phi for every row
assert deck(Phi,rho->-rho) == Phi

find/prove common sigma order; multiply back every quotient
extract G10,G11,G12 without setting rho=0
assert subst(Gn,rho,0) == frozen gn for every available row
form E12 from every coefficient through grade 12

compute Ktot by elimination (4.1)
independently compute saturation by iterative colon until stable
assert the two Ktot presentations are equal
compute Kafter and Kbefore (4.3); require two-way ideal membership
construct alpha,beta (4.4); check both composites and all row ideals

form Delta (4.6); require Delta != assumed input
require subst(Delta,rho,0)==0, reduce(Delta,(rho^2))==0,
        and Delta==rho^2*(exact quotient)
obtain (4.7), multiply back before localization, audit denominators
emit certificates, bases, maps, variable/grade manifest, and hashes
```

**[P] Fail-closed validator:** accept only exact `Q` output plus a separately
compiled good-prime control; parse algebraic artifacts rather than trusting
`PASS` strings.  Require source hashes, variable order, grading, row count,
every multiplication-back identity, two-way ideal/map checks, the registered
unit list `{k,rs}`, and a denominator factorization.  Any undeclared symbol,
radical-only result, timeout, missing artifact, or modular-only result is
`FAIL/UNRESOLVED`, never pass.

Mandatory negative controls are:

1. delete `G10_3` from (4.6) after `rho=0`; require the exact nonzero residue
   `-1536*cs*c0*c1`;
2. replace `Ktot` by the unsaturated bilinear ideal; if unequal, print a
   torsion witness, while equality is an accepted certified outcome rather
   than a forced failure;
3. specialize `rho=0` before chart formation and compare with (4.3); the
   validator must detect inequality if present, but must accept proved
   equality—this is a diagnostic, not a theorem that failure must occur;
4. omit each source jet in turn, re-run the source-specialization hash and
   coefficient comparison, and require rejection whenever the jet lies in
   the declared support; also include one synthetic required-jet omission so
   the validator's rejection path is exercised;
5. inject `1/rho`, `1/cs`, `1/c0`, `1/c1`, any root-value denominator, and an
   unregistered standard-basis leading coefficient one at a time; require
   rejection.  Only rational constants and powers of registered `k,rs` may
   occur as denominators.

## 6. Earliest failure and replacement discriminator

**[S]** The earliest likely failure is before Rees algebra: a literal
`p=-2*rho^2` emitter fails the exact `rho=0` comparison because it removes
the moving `ell` jets.  The next likely failure is missing higher source jets
in a supposedly complete grade-12 family. **[U]** Rees base-change torsion is
mathematically plausible because the frozen grade-ten source is nonreduced,
but no charged evidence proves it actually occurs on `D_+(rs)`. **[U]**

The smallest exact discriminator is therefore not the proposed full `T-rs`
job. **[P]** Run `T-rs-0`, with no Rees or Gröbner computation beyond exact
coefficient comparison:

```text
(a) emit Phi_tot using (2.2)--(2.3) and the complete grade-12 jet manifest;
(b) prove Phi_tot|rho=0 equals the frozen owner Phi row by row;
(c) prove rho-deck invariance and determine the actual common sigma order;
(d) extract through grade 12 and recover all frozen g10/g11/g12 rows,
    including (4.5) and its omitted-g10_3 residue.
```

Only after `T-rs-0` passes should `T-rs-1` compute (4.1)--(4.4), and only
after that should `T-rs-2` seek (4.7).  This ordering diagnoses the source
rather than repairing the desired conclusion by assuming it. **[P]**

## 7. Launch recommendation

**Binary recommendation: NO-GO for the proposed `T-rs` client.** **[S]** Its
stated substitution is ambiguous and, under the literal reading, wrong; its
jet completeness and its common `sigma^10` prefix over independent `rho` are
unproved.  Launch only the replacement AWS preflight `T-rs-0` after freezing
(i) formulae (2.2)--(2.3), (ii) a mechanically generated grade-12 support/jet
manifest, (iii) exact row-by-row `rho=0` comparison targets, and (iv) the
negative-control contract above. **[P]**

No total-Rees or moving-`p` result is promoted.  Even a later `T-rs` pass
would establish only this one chart; the other five charts, terminal
receiver, and `D(rho)` overlap remain separate obligations. **[S]**
