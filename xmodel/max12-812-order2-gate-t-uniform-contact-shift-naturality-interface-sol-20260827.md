# Gate T: uniform contact-shift naturality and endpoint-linker interface

Date: 2026-08-27

Status: **FORMAL DESIGN THEOREM, DERIVED HERE; IMPLEMENTATION AND
DIFFERENT-MODEL HOSTILE REVIEW STILL REQUIRED.  THIS CAN REPLACE SERIAL
PER-GRADE ACTUAL-TOTAL BUILDERS FOR THE STRICT UNIQUE-`AC` FAN ON
`D(rho)`, BUT IT DOES NOT REPLACE ANY D1 ENDPOINT OR ITS LIFECYCLE REVIEW.**

## 1. Minimal theorem

Work over a characteristic-zero coefficient ring and in its
`sigma`-adic formal power-series ring.  At formula level keep the unsplit
constant `p0` free and write the actual-total input series as

```text
P  = p0 + 2*sum_(i>=1) ell_i*sigma^i,
S  = sum_(i>=0) cs_i*sigma^i,       Q = sum_(i>=0) rs_i*sigma^i,
Az = sum_(i>=0) az_i*sigma^i,       Ac = sum_(i>=0) ac_i*sigma^i,
Ez = sum_(i>=0) ez_i*sigma^i,       Ec = sum_(i>=0) ec_i*sigma^i.
```

Here `cs_0=cs`, `rs_0=rs`, and the analogous campaign aliases for the first
three `A` and `C` jets are understood.  Define

```text
Ctot = sigma^2*S,
Rtot = (P^2 + sigma^2*Q)/4,
N3 = sigma^3*Az,                    N2 = sigma^3*Ac,
N1 = sigma^3*(P*Az+Ez)/2,           N0 = sigma^3*(P*Ac+Ec)/2,

F6=2P,                              F5=2Ctot,
F4=P^2+2Rtot,                       F3=2P*Ctot+sigma^2*N3,
F2=Ctot^2+2P*Rtot+sigma^2*N2,       F1=2Ctot*Rtot+sigma^2*N1,
F0=Rtot^2+sigma^2*N0.                                      (1.1)
```

For arbitrary nonnegative contact shifts `(a,c,r)`, quotient by the lower
jet ideal

```text
az_i=ac_i=0 (i<a),   ez_i=ec_i=0 (i<c),
cs_i=rs_i=0 (i<r).                                  (1.2)
```

There is a continuous substitution

```text
p0 -> p,
Az -> sigma^a*A_z,              Ac -> sigma^a*A_c,
Ez -> 2*sigma^c*C_z,            Ec -> 2*sigma^c*C_c,
S  -> sigma^r*B_z,              Q  -> 4*sigma^r*B_c,          (1.3)
```

which retains every moving `P` jet, every load series, and every target.
Under (1.3), (1.1) becomes identically

```text
Kc = sigma^(r+2)*B_z,
Kr = P^2/4 + sigma^(r+2)*B_c,
N3 = sigma^(a+3)*A_z,           N2 = sigma^(a+3)*A_c,
N1 = sigma^3*(P*sigma^a*A_z/2 + sigma^c*C_z),
N0 = sigma^3*(P*sigma^a*A_c/2 + sigma^c*C_c),        (1.4)
```

and hence becomes the charged D1 primitive source coefficient by
coefficient.  The factors `4` on `R` and `2` on `C` are forced, not
conventional.

Let `Tail_j` be any of the seven frozen 569-tail polynomials in
`F0,...,F6` and the three delayed load series, with its licensed target
subtracted.  Polynomial evaluation commutes with every ring homomorphism,
and coefficient extraction commutes with a continuous `sigma`-adic
homomorphism.  Therefore, simultaneously for all seven rows and every
`g>=0`,

```text
delta_(a,c,r)([sigma^g] Tail_j^total)
  = [sigma^g] Tail_j^D1.                              (1.5)
```

Equation (1.5) is a formal-power-series identity.  It is not an induction
whose proof must be rerun at grades 22, 24, 26, 28, or 38.  Truncating both
sides modulo `sigma^(T+1)` gives every finite endpoint comparison at once.

The proof is the displayed substitution into (1.1), followed by functoriality
of addition, multiplication, delayed series shifts, the fixed tail
polynomials, and coefficient extraction.  It does not depend on a row being
nonzero, on `rho` parity, or on a later face quotient.

Only after this unsplit formula-level theorem do we make the finite-flat
Kummer base change `p0 -> -2*rho^2`.  On the D1 side the moving-root quotient
has `p=-2*lambda_0^2`; either deck embedding sends `rho` to
`epsilon*lambda_0`.  This separates the formal functor from the generic
root chart and from the custody of a compiler which hard-codes the Kummer
substitution.

## 2. Parametric shifted-root jet map

Let the moving Hensel root be

```text
lambda(sigma)=sum_(i>=0) lambda_i*sigma^i,
lambda_0=epsilon*rho, epsilon in {+1,-1},
lambda(sigma)^2=-P(sigma)/2.                          (2.1)
```

On `D(rho)`, its coefficients exist uniquely and satisfy

```text
2*lambda_0*lambda_n
 = -ell_n - sum_(1<=i<n) lambda_i*lambda_(n-i).       (2.2)
```

For every `(a,c,r)`, define the shifted root-value series

```text
A_plus/minus = sigma^(-a)*(Ac plus/minus lambda*Az),
C_plus/minus = sigma^(-c)*(Ec plus/minus lambda*Ez)/2,
R_plus/minus = sigma^(-r)*(Q/4 plus/minus lambda*S).  (2.3)
```

These are regular after (1.2).  Their leading associated-graded map is

```text
A0_plus/minus = ac_a plus/minus rho*az_a,
C0_plus/minus = (ec_c plus/minus rho*ez_c)/2,
R0_plus/minus = rs_r/4 plus/minus rho*cs_r.           (2.4)
```

For jet `n`, the same formula is triangular:

```text
A_n^plus/minus = ac_(a+n)
  plus/minus sum_(i=0)^n lambda_i*az_(a+n-i),
C_n^plus/minus = (ec_(c+n)
  plus/minus sum_(i=0)^n lambda_i*ez_(c+n-i))/2,
R_n^plus/minus = rs_(r+n)/4
  plus/minus sum_(i=0)^n lambda_i*cs_(r+n-i).         (2.5)
```

At each level the new diagonal block has determinant a nonzero rational
multiple of `lambda_0`.  Thus every finite shifted-jet map, and its inverse,
is triangular and regular on `D(rho)`.  The deck involution
`rho |-> -rho` sends `epsilon |-> -epsilon` and exchanges the two
orientations.  This is the correct uniform replacement for the erroneous
stage-zero composition withdrawn by the Kummer erratum: it acts on the
first nonzero shifted pairs, not on the stage-zero pairs killed by the
contact quotient.

Nothing in (2.1)--(2.5) is regular at `rho=0`; the ramified fibre remains a
separate Gate-T obligation.

## 3. Uniform finite-jet bound

The endpoint primitive inventory also removes the need for an ad hoc
"later jets do not enter" proof in every contact.  If a licensed primitive
has fixed delay `b` and contains series families `X_f` with exponents `e_f`
and contact orders `nu_f`, its first grade is

```text
w = b + sum_f e_f*nu_f.                              (3.1)
```

Its coefficient at grade `g<=T` is a sum over relative jet indices whose
sum is `g-w`.  Consequently every individual relative index is at most
`T-w`.  For a family `f`, the exact required ceiling is

```text
max_f(T) = max(T-w(M) : licensed primitive M contains f),        (3.2)
```

with the leading-only convention `0`.  The same calculation applies to
the delayed `k10`, `k6`, and `k2` loads and to the fixed target schedule.
For a moving root, (2.2) shows that a root jet through level `n` uses only
`ell_1,...,ell_n`; no hidden connection jet occurs.

Thus an endpoint manifest containing its complete licensed primitive list
mechanically derives both its source maxima and its Hensel-root depth.
For `(a,c,r;d,G,T)=(2,5,3;3,17,20)`, (3.2) reproduces

```text
p/A/C=3, R=1, k10=2, k6=0, k2=0; targets absent.     (3.3)
```

Here `T` is always the terminal grade of the reviewed chamber theorem.  It
is not uniformly the first `C^2` grade `10+2c`.  The exceptional pole-three
cell, the `a=7,8,9` load walls, and the `a>=10` grade-38 source ceiling use
different obstructions and sometimes different ceilings.  In particular,
the `a>=10` endpoint stays at `T=38` even when `AC` first appears after
grade 38.  Formula (3.2) must consume the chamber's reviewed *polar*
primitive inventory; raw valuations of the unreduced `F_i` can overpredict
because the frozen tail polynomial cancels them.

## 4. Frozen interface

A uniform linker should consume one immutable source-schema object and one
immutable endpoint manifest.  The source schema must pin:

```text
schema version;
the seven formulas (1.1);
load delays k10=4, k6=12, k2=20;
target schedule mu2=28, mu4=32, mu6=36, J=38;
the byte and canonical hashes and 1..7 census of all 569 tails;
the coefficient-name/weight aliases;
the total-emitter implementation hash.
```

Each endpoint manifest must contain:

```text
(a,c,r_floor), exact versus closed orders, d, G, T;
the lower-jet ideal (1.2);
the complete licensed primitive inventory and its hash;
mechanically derived maxima (3.2);
load and target policy;
the D1 source convention and compiler/source-inventory hashes;
the endpoint result, promotion, and hostile-review hashes;
the exact localization factors and root-allocation convention;
the endpoint status: promoted, confirmed-but-unpromoted, or pending;
the bridge/quotient markers and every explicit scope exclusion.
```

The linker must fail closed unless it can:

1. derive the shifted renaming/scaling map from `(a,c,r_floor)` and (3.2),
   rather than accept a hand-written map;
2. derive all lower vanishings and prove every omitted jet is above `T`;
3. compare the endpoint's coded D1 primitive formulas with (1.4), including
   every load and target which can enter by `T`;
4. instantiate (2.2)--(2.5) through the required depth for both signs;
5. pin the endpoint evidence and preserve its exact localization and
   theorem type; and
6. emit a contact-specific link certificate, without changing the endpoint
   lifecycle label.

It must also distinguish four evidence layers in its output: (i) the
formula-level identity (1.5), (ii) semantic agreement of each named compiler
with (1.1)/(1.4), (iii) frozen compiler/tail custody, and (iv) the reviewed
D1 endpoint.  A hash or a serialized row is not a proof of layer (i), while
layer (i) does not certify that a particular compiler implements the formula.

An endpoint is linkable only when its obstruction is an identity in the
seven literal `Phi`/`SourcePhi` rows (possibly after the registered
localization and root allocation), or when a reviewed analytic-to-Faber row
bridge is present through `T`.  A handwritten analytic `H` with no such
bridge must be rejected.  This is material for the confirmed `(8,3,8)`
cell: the link must select its later literal odd-row certificate, not the
documented analytic-bridge attempt which produced no theorem.

The smallest implementation is desk-scale: symbolic primitive comparison;
tail functoriality plus the pinned 569 census without expansion; support-table
validation for the eleven reviewed endpoint families; and provenance checks
for literal-row obstructions.  An exact-Q/finite-field expansion of all seven
rows through the maximum used strict-fan ceiling (`T=38`) is optional defense
in depth, not the proof of (1.5) and not a prerequisite for each contact.

Mandatory mutation controls should reject: stage-zero pairs in place of
shifted pairs; factors `1` in place of `4` or `2`; deletion of a moving
`2*sigma*ell1` term; the naming error `k2c -> k2load`; use of the `C^2`
ceiling at the exceptional/load-wall/grade-38 chambers; an analytic-only
`(8,3,8)` certificate; and relabeling a frozen `rho=0` face row as a
general-`rho` row.

## 5. What this replaces, and what it does not

Once the theorem, schema, and linker receive independent hostile review,
new strict unique-`AC` transports need no serial `ACT-TOT-G22`,
`ACT-TOT-G24`, and later custody producers.  They need only a small endpoint
manifest/link certificate; independent endpoint review can continue in the
background.

The interface does **not**:

- promote the confirmed `(a,d)=(8,3)` endpoint, which still lacks its narrow
  lifecycle promotion;
- create or review any D1 endpoint, prove the strict-fan ledger exhaustive,
  or reconcile mixed endpoint theorem types;
- apply to equality faces, positive-order leading loads, `k=0`, or a contact
  not represented by a complete manifest;
- cover the six staged Rees charts, the terminal/Taylor receiver, or reverse
  the direction of a scheme map without finite-jet factorization;
- extend (2.3) to `rho=0`; or
- prove either global `G2` obligation, Gate T, order two, maximum twelve,
  JC2, or a counterexample.

Until hostile review and a frozen implementation pass, (1.5)--(3.2) may be
used only as a clearly labeled provisional source-transport theorem.

## 6. Independent design reconciliation

The independent Grok design

```text
8867c66a8e436107d059269e18347ef8ef01bbf8fdaa44ccec6b58fcef874944
  xmodel/max12-812-order2-gate-t-strict-uac-uniform-transport-design-grok-20260827.md
```

agrees that serial general-`rho` grade exporters are not mathematical proof
obligations and that the formal emitter is natural under the parameterized
shift.  Its useful corrections are incorporated above: retain `p0` until
the separate Kummer step, take `T` and support from the reviewed chamber
rather than a universal `C^2` formula, separate four evidence layers, require
literal-Faber provenance, and test the load-wall and `k2c` traps.  It also
identifies eleven existing D1 endpoint families.  They remain eleven
independent emptiness inputs; this uniform theorem transports them but does
not replace them by one residue argument.
