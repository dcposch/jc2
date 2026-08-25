# Preregistration: cyclic-D1 passport versus the full `k != 0` order-three lower fibre

Date: 2026-08-25  
Status: **DESIGN FROZEN BEFORE ANY CAS RUN**  
Execution: **AWS Linux only**

## 1. Exact question and scope

Work in characteristic zero on the nontrivial order-three Kummer branch of
the unbounded-total partial-`y` `(9,12)` cell.  This gate tests the smallest
balanced terminal passport, `D=e=1`, against the complete lower Faber fibre
on the previously unhandled chart `k != 0`:

```text
r1=r2=r4=r5=r7=0,       r3=mu,       r6=nu,
9*r8'=j/u,
```

with `k,mu,nu` differential constants and with **all** `mu,nu` values
retained.  It is not a selected-Q8 calculation.  The `k=0` divisor is kept
as an emitted boundary/control and is not claimed covered by a result on the
localized chart.

Every `D=1` balanced passport is affine-equivalent on the source line and
scalar-equivalent on the target to the following exact fixture:

```text
s = T = x/(x-1),           t^3=s,
x = t^3/(t^3-1),           r8=t,
u = t^2/(t^3-1)^2,
h = u^3 = x^2*(x-1)^4,     j=-3,
9*d(r8)/dx = -3/u.
```

Only affine changes of `x` are used, so polynomiality in `x` is preserved.
The question is whether any geometric component of the exact coefficient
incidence admits a degree-one section over `P1_s`, after a finite extension
of the constant field, and whether such a section satisfies both complete
Taylor polynomiality families.  Higher-degree covers of `P1_s` are not
sections in the prescribed Kummer field and are not accepted as witnesses.

## 2. Frozen inputs

| Input | SHA-256 | Licensed role |
|---|---|---|
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | order-three Kummer typing, polynomial `h`, noncube/history conditions |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` | different-model confirmation |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` | universal Faber form and complete lower differential system |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` | different-model confirmation |
| `xmodel/max12-912-order3-global-terminal-belyi-classification-audit-20260825.md` | `28f33b993726b4bd7441a79a8f4208983dbbd0c5e4113d839a78af1b8cc7b6c6` | branch-wide terminal passport |
| `xmodel/max12-912-order3-global-terminal-belyi-classification-review-grok-20260825.md` | `5da99825e099232832b0cf91fc02b29cb9460a2f675e2a69ab1769f204cf9fc9` | different-model confirmation and residual obligations |
| `cases/max12_high_row_probe_20260824/shared_faber_probe.py` | `69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f` | reviewed sparse Faber arithmetic engine |
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` | reusable eight-tail producer, **not a reviewed theorem** |
| `cases/max12_912_order3_terminal_belyi_classification_20260824/replay.py` | `495844f1d51c0f230223d143f36b54679865244581fb60974c268da4c756a4bb` | D1/D2 terminal controls |

The adapter must call the parent `pin_inputs()` explicitly before importing
any compiled tail.  A second implementation must rebuild `F12`, `F6`, the
inverse root, and all eight tails directly from the reviewed shared Faber
source.  Equality of all eight sparse coefficient maps and digests is a
prerequisite for consuming any CAS result.

## 3. Exact character descent and eight source rows

Use the frozen campaign generator `sigma(u)=zeta*u`.  Since `t=r8` and
`sigma(r8)=zeta^2*r8`, one has `sigma(t)=zeta^2*t`.  Thus
`sigma(a_i)=zeta^(-i)*a_i` is represented by

```text
a_i=t^eps_i*A_i(s),
eps_i = 0,1,2 according as i = 0,1,2 mod 3.
```

For a tail, however, `sigma(r_l)=zeta^l*r_l`, so the quotient exponent is
**not** `eps_l`.  Let

```text
eta_l = 0,2,1 according as l = 0,1,2 mod 3.
```

Equivalently, if one names the generator satisfying `tau(t)=zeta*t`, then
`tau=sigma^2`, `tau(u)=zeta^2*u`, `tau(a_i)=zeta^i*a_i`, and
`tau(r_l)=zeta^(2*l)*r_l`; the same exponent tables result.  Every monomial
of `r_l/t^eta_l` has a nonnegative exponent divisible by
three in `t`; replace `t^3` by `s`.  The compiler must fail closed on any
monomial violating this statement.  The resulting exact rows over
`Q[s,k,mu,nu,A0,...,A7]` are

```text
R1=0, R2=0, R3=mu, R4=0,
R5=0, R6=nu, R7=0, R8=1.                 (3.1)
```

No selected component, parity involution, Q8 relation, modular row, or
Taylor truncation is substituted into (3.1).

## 4. Stage A: geometric degree-one section classification

The primary lane localizes only `k` and retains `mu,nu` as constant-base
parameters.  It must:

1. form the affine incidence `X_D1` cut out by all eight rows (3.1);
2. compute generic relative dimension and degree over
   `Qbar(k,mu,nu)(s)`;
3. compute an **absolute/geometric** decomposition, not merely a
   factorization over `Q(k,mu,nu,s)` (constant extensions such as
   `A^2-k` split over the campaign's algebraically closed constant field);
4. retain exactly the components whose normalized function field is
   `C'(s)` for a finite constant extension `C'/C`, equivalently whose map to
   `P1_s` has geometric degree one;
5. derive Fitting/discriminant loci in `(k,mu,nu)` where relative degree,
   dimension, or geometric factorization changes, and recursively repeat
   the degree-one test on every exact stratum;
6. reconstruct every accepted `A_i(s)` and substitute it into all eight
   original, un-divided tails in `Q(t)/(t^3-s)`.

An algebraic cover of degree greater than one, a modular point, a generic
rank, or a sampled specialization is navigation only.  A degree-one
component is not yet a trajectory: it proceeds to Stage B.

## 5. Stage B: both global Taylor families, with finite source-shear quotient

Write the true Taylor center as `r=u*R0(x)`.  The coefficient of `y^8` in
`P=f(uy+r)` is `9*h^3*R0`.  For the D1 fixture, `ord_0(h)=2` and
`ord_1(h)=4`; hence polynomiality bounds the finite poles of `R0` by `6`
at `x=0` and `12` at `x=1`.  Precomposition by the polynomial shear
`y -> y+q(x)` changes `R0 -> R0+q` and preserves the problem.  After this
exact gauge quotient, use the complete finite ansatz

```text
R0(s)=sum_(d=-6)^(-1) c_d*s^d + sum_(d=1)^12 c_d*s^d.  (5.1)
```

It has 18 parameters; the missing constant is the residual constant shear.
For every accepted Stage-A section, reconstruct `f` and the full Faber `g`
and impose, without omission,

```text
u^ell*f^(ell)(u*R0)/ell! in C[x],  0<=ell<=9,
u^ell*g^(ell)(u*R0)/ell! in C[x],  0<=ell<=12.         (5.2)
```

Here `x=s/(s-1)`.  A rational function of `s` lies in `C[x]` iff it is
regular away from `s=1` and regular at `s=infinity`; equivalently it has a
finite expansion `sum_(d=0)^N p_d (s/(s-1))^d`.  The implementation must
introduce those output coefficients and equate cleared numerators exactly;
testing finitely many values or a formal Taylor jet is forbidden.

A SAT section must be replayed by reconstructing the original `P(x,y)` and
`Q(x,y)`, checking all 23 coefficients are in `C[x]`, checking the eight
tail rows and `9*r8'=-3/u`, and checking the literal Jacobian is the constant
`-3` (or its explicitly rescaled Keller normalization).

## 6. Projective and load-boundary coverage

The following are mandatory, separately labelled outputs:

- the base points `s=0`, `s=1`, and `s=infinity` (`x=0,infinity,1`);
- the weighted coefficient-infinity divisor in the closure with weights
  `wt(a_i)=9-i`, `wt(k)=6`, `wt(mu)=15`, `wt(nu)=18`, `wt(r8)=20`;
- the load divisors `mu=0` and `nu=0`, their intersection, and every new
  Fitting/discriminant stratum found inside `k!=0`;
- the excluded localization boundary `k=0`, emitted unchanged for a later
  gate and never inferred from a `k!=0` result;
- the resultants `Res_z(f,f_z)` and `Res_z(f,g)`: accepted sections must be
  generically coprime; zero-resultant components remain explicit boundary
  strata rather than silently saturated away;
- the D1 passport collision boundary (`A` and `B` share a root), recorded as
  outside the balanced nontrivial passport rather than lost in an affine
  chart.

Purely vertical components at a base boundary are recorded but cannot count
as sections.  Saturation and closure must be checked in both directions.

## 7. Positive and negative controls

All controls are source replay, not evidence for the main outcome.

1. **Terminal D1 positive:** the displayed `t,u,h,r8,j` identities and
   noncube divisor `(2,4)` pass exactly.
2. **Terminal D2 positive:** replay both the cyclic `(1,5)` row and the
   reviewed even-contact `e=2` fixture; this protects passport orientation
   and the original terminal row.
3. **Lower-fibre source positive:** the common-cubic family
   `f=K^3`, `g=K^4+k*K^2` returns all eight tails zero.  It is deliberately
   on the `r8=0` terminal boundary and must fail the D1 combined gate.
4. **Taylor round-trip positive:** start from arbitrary polynomial Taylor
   coefficients and a polynomial source shear, convert to depressed
   `(f,g,u,R0)`, and reconstruct byte-identically.
5. **Character negative:** swap the exponents for character one and two;
   at least one monomial must fail the divisibility assertion before CAS.
6. **Taylor-center negative:** substitute `R0=0` for a fixture with nonzero
   center and require the original Taylor reconstruction to differ.

## 8. Outputs, theorem semantics, and stop rules

The frozen result package must contain:

- exact row source and transitive SHA closure;
- sparse row JSON and all eight row hashes from two constructions;
- affine and weighted-projective ideals for every processed load stratum;
- component ideals, two-sided containments, geometric degrees over `P1_s`,
  and Fitting/discriminant recursion;
- explicit rational section formulae or exact nonexistence certificates;
- the 18-parameter Taylor ideal for every section and its exact outcome;
- literal source replay for every accepted witness;
- a machine-readable coverage ledger separating `k!=0`, `k=0`, vertical
  boundaries, and unprocessed exceptional strata.

The primary run stops without theorem inference if any of the following
occurs: source constructions disagree; a required saturation/containment is
missing; generic relative dimension is positive without a certified
section classifier; absolute factorization is unavailable; an exceptional
load stratum remains unprocessed; or the exact job exceeds 2 hours or
128 GiB.  Modular data may choose an elimination order but cannot prove
emptiness or existence in characteristic zero.

The only promotable outcomes are:

- **D1/k-unit exclusion:** every geometric degree-one component on the full
  processed `k!=0` load stratification fails exact Taylor/Jacobian replay;
  or
- **explicit realization candidate:** one complete rational section passes
  all eight rows, the original terminal row, both Taylor families, generic
  coprimality, and literal Jacobian replay.

Neither outcome covers `k=0`, higher passports, the order-one Kummer leaf,
`(8,12)`, all maximum twelve, a counterexample, or JC2.

## 9. AWS execution contract

Every compiler, CAS, factorization, normalization, replay, and verifier must
run on a registered AWS Linux host.  Runners must refuse Darwin/non-Linux,
require an exact `JC2_AWS_TAG`, record hostname/PID/resource caps, hash the
source archive before and after transfer, and preserve stdout/stderr/time/RSS.
No substantive local execution is authorized.
