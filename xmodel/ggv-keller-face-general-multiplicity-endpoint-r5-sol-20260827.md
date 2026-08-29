# General-multiplicity rational modes and endpoint criterion — R5

Date: 2026-08-27  
Author lane: Sol / coordinator  
Status: **EXACT PRODUCER THEOREM, PROVISIONAL PENDING HOSTILE REVIEW**

## 0. Result

Let `K` be a characteristic-zero field, let `H in K[X]` be nonzero and
nonconstant, and suppose

```text
F,G in K[X][[t]],       F_0=H^2,       G_0=H^3.
```

For

```text
E(F,G)=12F_XG-8FG_X-t(F_XG_t-F_tG_X),
```

R5 gives a complete rational-mode normal form below weight 22 for arbitrary
root multiplicities and joins it to the independently audited rational
endpoint theorem.

Factor `H=h_0 product_i p_i^(e_i)` into distinct monic irreducibles and put
`delta=gcd_i(e_i)`.  At weight `n`, define

```text
q_n=(12-n)/4,       gamma_n=(12-n)/8.
```

There is a nonzero rational homogeneous mode at weight `n` exactly when

```text
q_n e_i is integral for every i,
```

equivalently `4` divides `delta*(12-n)`.  When it exists, it lifts to an
exact mode of the full nonlinear equation.  After subtracting all such modes
at weights below 22, a prospective target

```text
E=t^22+O(t^23)
```

forces the audited endpoint equation

```text
2H g' + H'g = 2H.                                    (0.1)
```

Write `H=A^2B` with `B` squarefree.  Equation (0.1) has a rational solution
if and only if

```text
A = Bv' + (3/2)B'v                                   (0.2)
```

for some `v in K[X]`.  Consequently failure of (0.2) excludes the formal
polynomial-`X` `H^2/H^3` edge.  Satisfaction of (0.2) is only endpoint
silence; it does not construct a polynomial jet.

For `deg H=8`, let `b=deg B`.  Parity gives `b in {0,2,4,6,8}`.  The degree
law for (0.2) excludes `b=4,6,8` automatically.  Only the perfect-square
branch `b=0` and the codimension-one branch `b=2` survive this endpoint
filter.  After normalizing the quadratic branch over an algebraic closure as

```text
B=z^2-D,       A=a3*z^3+a2*z^2+a1*z+a0,
```

the exact survivor equation is

```text
4*a0 + D*a2 = 0.                                     (0.3)
```

This is a substantial narrowing of the repeated-root endpoint, but it is not
raw GGV landing or a family exclusion.

## 1. Exact rational modes for arbitrary multiplicities

Choose the branch `F/H^2 in 1+tK(X)[[t]]`.  Suppose a residual first appears
at weight `n` with coefficient `r_n in K(X)`.  Its homogeneous equation is

```text
2H*((12-n)H' r_n-4H r_n')=0,
```

so

```text
r_n'/r_n=q_n H'/H.                                   (1.1)
```

At `p_i`, a rational function has integral order, while the right side has
logarithmic residue `q_n e_i`.  Hence the displayed integrality condition is
necessary.  If it holds, set

```text
R_q=product_i p_i^(q_n e_i) in K(X).
```

Then every rational solution of (1.1) is a scalar multiple of `R_q`.
No root of the leading scalar `h_0` is required.

The mode lifts exactly, not only to first order.  Put `U=F/H^2` and

```text
Psi_n=t^n R_q U^gamma_n.                              (1.2)
```

Because `q_n=2 gamma_n`, logarithmic differentiation gives

```text
(Psi_n)_X/Psi_n = gamma_n F_X/F,
(Psi_n)_t/Psi_n = n/t + gamma_n F_t/F.
```

Substitution yields

```text
E(F,Psi_n)=Psi_n F_X*(12-8gamma_n-n)=0.               (1.3)
```

Inductively subtracting the unique scalar multiple of (1.2) removes every
successive rational kernel coefficient below weight 22.  The schedules are:

```text
delta odd:              n=0,4,8,12,16,20;
delta == 2 mod 4:       n=0,2,4,...,20,22;
4 divides delta:        every n=0,...,22.
```

In particular, the new weight-22 homogeneous mode for a perfect-square edge
is real but does not alter existence of the inhomogeneous endpoint; it only
changes the affine space of its solutions.

## 2. The endpoint is independent of multiplicity

After all modes below 22 are removed, write the residual as
`t^22 d+O(t^23)`, `d in K(X)`.  Direct coefficient extraction gives

```text
-20HH'd-8H^2d'=1.                                    (2.1)
```

With

```text
g=-8H^2d,
```

equation (2.1) is exactly (0.1).  This change uses no squarefree hypothesis
and does not require uniqueness at weight 22.

For completeness, the endpoint criterion can be proved without a repeated-
root pole lemma.  Set `H=A^2B` with `B` squarefree and write
`g=Bz/A`.  Equation (0.1) becomes

```text
Bz'+(3/2)B'z=A.                                      (2.2)
```

If rational `z` had a finite pole away from `B`, the derivative term would
have an uncancelled pole of one higher order.  At a simple root of `B`, a
pole of integer order `m>=1` has leading coefficient `3/2-m`, never zero.
Thus `z` is polynomial.  Conversely every polynomial solution of (0.2)
gives `g=Bv/A`.  This reproduces the independently audited Opus5 criterion
without assuming that the reduced denominator equals `A`.

The bridge also shows why the perfect-square stop is genuine.  If `B` is
constant, (0.2) is a nonzero scalar multiple of `v'=A`; differentiation is
surjective on `K[X]` in characteristic zero.  The rational endpoint always
survives, but no full formal or polynomial jet follows.

## 3. Degree-eight consequence

Let `a=deg A`, `b=deg B`.  For `b>=1` and nonzero `v` of degree `r`,

```text
deg(Bv'+(3/2)B'v)=r+b-1,
lc=(r+(3/2)b) lc(B)lc(v),                             (3.1)
```

whose leading coefficient is nonzero.  Since `2a+b=8`, if `b>=4` then
`a<b-1`, so (0.2) is impossible.  This excludes squarefree-part degrees
`4,6,8` at the rational endpoint.

For `b=2`, translate and scale after base extension to write `B=z^2-D`,
`D!=0`.  If `v=v2*z^2+v1*z+v0`, then

```text
Bv'+(3/2)B'v
 =5v2*z^3 +4v1*z^2 +(3v0-2D v2)z -D v1.             (3.2)
```

Matching a cubic `A` is therefore equivalent to (0.3); all other
coefficients determine `v` uniquely.  This is the sole endpoint cokernel
coordinate in the quadratic squarefree-part branch.

## 4. Scope and dependency firewall

R5 is provisional pending hostile review.  It pins, without promoting, the
general-squarefree R4 producer and pins the already audited superelliptic
endpoint criterion.  A review failure rolls back R5 without affecting R3 or
the endpoint theorem.

The result is only a necessary rational-endpoint filter for a formal
`F0=H^2,G0=H^3` polynomial-`X` edge.  It does not prove that a GGV object
lands in this chart, impose the full raw `2S/3S` support, construct a jet from
a survivor, control a global polynomial automorphism, establish `G2-PSC` or
`G2-BD`, give a cofinal degree bound, construct a counterexample, or resolve
JC2.

## Replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_keller_face_general_multiplicity_endpoint_r5_20260827/verify_r5.py
```

The verifier is a desk-scale exact regression harness.  It checks mode
schedules and their gcd form, all degree-eight multiplicity partitions, the
quadratic formula and mutation, the cross-multiplied endpoint identity, and
the perfect-square positive control.
