# Monomial-boundary Jacobian divisibility: the analytic nodal control fails at the first polynomial-support gate

UTC: 2026-08-29  
Producer: Sol / coordinator  
Frozen repository basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: `PRODUCER_EXACT / DIFFERENT-MODEL REVIEW REQUIRED`  
Claim ID: `MONOMIAL-BOUNDARY-DIVISIBILITY/v1`

## Result

Let `K` be a field, let `u>=2`, and use the literal monomial boundary chart

```text
x=t*s^u,       y=s^(-1).
```

Suppose `F,G in K[x,y]` have no negative `s`-powers after this substitution,
so that

```text
f(s,t)=F(t*s^u,s^(-1))=sum_(k>=0) a_k(t)s^k,
g(s,t)=G(t*s^u,s^(-1))=sum_(k>=0) b_k(t)s^k
```

are finite elements of `K[s,t]`. Then the coefficient of `s^(u-2)` in

```text
f_s*g_t-f_t*g_s
```

is divisible by `t`. In particular, `Jac_(x,y)(F,G)` cannot be a nonzero
constant: if it were normalized to one, then

```text
df wedge dg = dx wedge dy = s^(u-2) ds wedge dt,
```

whose `s^(u-2)` coefficient is the unit `1`, a contradiction.

This is an exact obstruction for a pair that is simultaneously regular in
the **literal monomial chart**. It is not a theorem about a translated or
iterated blow-up/Puiseux chart, a chart containing Laurent powers of `t`, or
one in which either polynomial still has a boundary pole.

## Proof

Every affine monomial becomes

```text
x^A*y^B = t^A*s^(u*A-B),       A,B>=0.                 (2.1)
```

For `1<=k<=u-1`, an equality `u*A-B=k` cannot have `A=0`, since it would
give `B=-k`. Hence every monomial contributing to `a_k` or `b_k` has
`A>=1`, and therefore

```text
t divides a_k(t), b_k(t)       for 1<=k<=u-1.          (2.2)
```

Direct differentiation gives

```text
[s^(u-2)](f_s*g_t-f_t*g_s)
 = sum_(i+j=u-1) ( i*a_i*b_j' - j*a_i'*b_j ).          (2.3)
```

In every nonzero first summand `i>0`, so `1<=i<=u-1` and `t|a_i`.
In every nonzero second summand `j>0`, so `1<=j<=u-1` and `t|b_j`.
Thus every summand, and hence (2.3), is divisible by `t`. On the other hand,

```text
dx wedge dy=s^(u-2) ds wedge dt,                       (2.4)
```

so a unit Jacobian requires (2.3) to equal `1`. This is impossible in
`K[t]`. The same proof works for any nonzero constant Jacobian.

The argument is an identity in the coefficient ring. It does not infer an
arc from a finite jet, identify a flag with a place, or use reducedness.

## The nodal analytic control

The reviewed control uses `u=3` and

```text
P=t^2,       Q=t^3+t,
R=sqrt(1+3s^2/2),
f=t^2+(2/3)(R-1),       g=t^3+tR.
```

Its first nonzero transverse coefficients are

```text
a_2=1/2,       b_2=3t/4,
```

and indeed

```text
2(a_2*Q'-P'*b_2)=1.                                  (3.1)
```

Equation (3.1) shows that the unconstrained Bezout gate passes. But (2.2)
requires `t|a_2` for polynomial origin, while `a_2=1/2`. Thus this same
coefficient is already the exact polynomial-support violation; no nonlinear
continuation or square-root argument is needed to reject this control as a
polynomial-origin germ in the literal chart.

More generally, allowing arbitrary lower positive layers does not repair the
problem. Formula (2.3) includes all pairs `i+j=u-1`, and polynomial support
makes each term divisible by `t`.

This corrects the post-cutoff Sol ideation statement that the nodal control
passes the first polynomial-origin gate. It passes only the free
`K[t]` Bezout equation after forgetting the Newton-support submodules.

## Relation to banked evidence and novelty

The Newton-support mechanism is `KNOWN`: the hostile Section-7 audit with
full SHA-256
`af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe`
already observed, for `u=3`, that a pure `s^2` term is outside the affine
polynomial monomial semigroup. The present contribution is a
`NEW EXACT GENERALIZATION / NEW APPLICATION`: it keeps every positive layer,
computes the complete Keller coefficient (2.3), and shows that the whole
coefficient lies in `(t)` for every `u>=2`.

The reviewed nodal analytic-control evidence remains valid at its licensed
scope. Its Fable report has full SHA-256
`28e22f20da290adbceff2edd508b75ef498ed6723d1e93616b5ebf3fad8f2104`
and body SHA-256
`cf1ba18a699de9f9107b86ec8fe253e867f762a52e6c8f821832683efd460011`;
the binding integration has full SHA-256
`a7b39d985c9e50688506cb9a176a93e89a309de079e025cb4f28430c4e7ded10`
and body SHA-256
`24675cfe3a07aa9cd05a46fc4842b32f0b86ddf1d322ac9731dfe19bed3eb8ad`.
Those reports already deny polynomial/rational origin. This note sharpens
where polynomial origin first fails; it does not retract the analytic
countermodel to pointwise strictness.

## Controls and firewalls

- **Laurent-support control.** The analytic nodal pair has exact Jacobian one
  and violates precisely `t|a_2`; therefore deleting (2.2) must make the
  contradiction disappear.
- **All-layer control.** For `u=3`, (2.3) reads
  `a_1*b_1'-a_1'*b_1+2(a_2*Q'-P'*b_2)`. If all four positive-layer
  coefficients are divisible by `t`, both terms vanish at `t=0`.
- **Endpoint control.** Formula (2.3) retains `i=u-1,j=0` and
  `i=0,j=u-1`; silently dropping either endpoint is invalid.
- **Scope firewall.** A later translation or blow-up can replace the simple
  semigroup (2.1), and localizing a chart can change which coefficient
  functions are regular. Such a client must rederive its own support module.
- **No global conclusion.** This excludes one literal toric realization and
  strengthens the discriminator for `STRICT-COLLIDE-POLY`; it does not prove
  QCS, exclude every boundary component of a hypothetical counterexample,
  produce a global selector, or prove JC2.

## Next discriminator

Before launching nonlinear rational-termination work for a boundary client,
compile its exact polynomial-origin support module and apply (2.3). For the
literal nodal control the lane stops immediately: `POLYNOMIAL_ORIGIN_EMPTY`.
The surviving question is whether the actual Section-7 geometry lands in
this monomial-chart scope or in a translated/iterated chart with a different
support module. That is an occurrence/selector problem, not a continuation
problem for the rejected analytic ansatz.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6119`.
- Body SHA-256:
  `e8a2a5211833529f783a49daa2738ddc7f7bd42a063ff5a0c998d8af69baa231`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
