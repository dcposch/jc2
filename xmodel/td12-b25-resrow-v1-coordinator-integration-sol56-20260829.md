# Coordinator integration — TD12 B first resonant row

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`  
Lifecycle: `PROMOTED_RESROW_VACUOUS_AT_j17 / NO_ROUTE_KILL`

## 0. Evidence and disposition

Sol correction:

```text
edfec0a0d9abb8b24db9406bdc1147348114f198a4a9e92a10486bbe9131a720
  xmodel/td12-b25-resrow-v1-provisional-sol56-20260829.md
  body 11988 / 9c72c20e02efcb74fd351f7ac820268386a625dbfc60b855dc18a1e212766b4f
```

Independent Opus 5 hostile review:

```text
068ed91bae52d04aefb0fe5b941607f2918491d9808891fccf9846ce54fd9bad
  xmodel/td12-b25-resrow-sol56-hostile-review-opus5-40c-20260829.md
  body 37413 / 2e5a062fc0dc2e49c3fa5596d41c165aaead03ac91736d0ead040bd48a31d59c
```

The review independently recollected every coefficient from the Jacobian
equation, reran exact controls, and returned `PASS_WITH_REPAIR`. Its lane is
`DONE`, exit zero, with stable declared inputs and
`charge_basis_status=ABSENT`.

Binding disposition:

```text
PROMOTE THE CORRECT INTEGRATING FACTOR p^(I-i)
PROMOTE j=17 AS AN IDENTICALLY VACUOUS TOTAL-DERIVATIVE ROW
STOP TD12-B25-RESROW/v1 AT j=17
DO NOT LAUNCH j=42 WITHOUT ACTUAL SOURCE VALUES AND GAUGE CONTROL
```

## 1. Reviewed exact row theorem

At a named actual B occurrence, retain the promoted bridge notation

```text
nu=25, kbar=17, D=25i, O=kbar-D,
P0=lambda_f*p^i,
```

and write the reduced deviation coefficients as `T_j`. Coefficient collection
in `J(f^F,Dev)=x^(-u)` gives, for `j>=1`,

```text
i*lambda_f*p^(i-1) L_j[T_j] = R_j,
L_j[T]=25*p*T' + (25i+j-17)*p'*T.
```

At a resonance `j=17+25m`, put `I=i+m`. The exact conjugated equation is

```text
(p^I*T_j)' = p^(I-i)*R_j/(25*i*lambda_f)
            = p^m*R_j/(25*i*lambda_f).
```

The exponent is `I-i`, not `I-1`. The latter arose by dropping the outer
factor `p^(i-1)` and agrees only in the exceptional case `i=1`, which is not
on the reviewed B class.

At the first resonance, the two coefficients in every prior-tail summand
coincide by the product rule:

```text
R_17 = -(sum_(a=1)^17 (25i-a)*P_a*T_(17-a))' = -S_17'.
```

Therefore `R_17 d eta` has zero residue at every point of `P^1`, not merely
at the two deck orbits. It has no simple-pole part anywhere. Whenever the
preceding tail lies in `C[eta][1/p]`, the row is solved there by

```text
T_17 = -S_17/(25*i*lambda_f*p^i) + C_17*p^(-i),
C_17 in C.
```

Both terms have the correct B weight. Thus the proposed two orbit-residue
functionals are identically zero: `j=17` spends no condition. This is silence,
not evidence that the B route occurs or survives globally.

## 2. Route-general derivative collapse and sibling scope

For a landed-deviation recurrence with

```text
O=kbar-D,       D=nu*i,
```

the same coefficient collection gives

```text
R_kbar = -(sum_(a=1)^kbar (D-a)*P_a*T_(kbar-a))'.
```

This total-derivative identity uses only the landing equation and product
rule. For actual B and S polynomials the needed rational-kernel hypothesis is
safe because `p` is nonconstant and has simple zeros. A fully generic “kernel
iff” formulation should retain an appropriate primitive-divisor hypothesis.

Conditionally, if the S bridge supplies the same terminal reduced deviation
with `(nu,kbar,D)=(17,13,17i)` and `O=13-D`, then

```text
R_13=-S_13',
T_13=-S_13/(17*i*lambda_f*p^i)+C_13*p^(-i).
```

The S weight check passes. The current S material has not yet supplied a
reviewed terminal-deviation/landing recurrence, so this is a conditional
corollary, not a promoted S bridge theorem. Do not launch a separate S
`j=13` residue computation. The only narrow prerequisite is to type and
review that S landing recurrence.

## 3. Later resonances, repairs, and stop

At `j=42` the first resonant gauge `C_17` is still free, so any later pair of
residue equations is affine in an unpinned constant. No promoted packet
supplies `P_42`—indeed no positive-order `P_a` value is serialized—and no
reviewed map identifies the `P_a` index with B-window depth. The earlier
phrases “outside B24” and “two indices deeper” are therefore deleted.

Do not launch `j=42` until a source-bearing client supplies the required
`P_a` data and pins or eliminates `C_17`. The review's general higher-
resonance residue formula and generic nonvacuity controls are useful but
reviewer-originated and remain provisional; they do not license expansion.
Nonresonant existence in the on-weight rational ring also remains a typed
open question distinct from uniqueness.

The first approximate-root normalization remains
`c_g*lambda_f^(-3/2)` (or its squared tower form
`c_g^2/lambda_f^3`). Ledger constants do not enter the reduced recurrence.

No source value, serialized `PairRef`, B occurrence, uniform cap, gate/tree
landing, route exclusion or survival theorem, degree bound, exit price,
counterexample, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4891`.
- Body SHA-256:
  `c0d1e19d63bc1d6a27ffb80cc4376be11397e407669fdd90a4b60a33e0109d7a`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
