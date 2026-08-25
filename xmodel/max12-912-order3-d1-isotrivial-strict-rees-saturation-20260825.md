# D1 isotrivial strict-Rees saturation theorem and gate design

Date: 2026-08-25  
Status: **EXACT SOURCE REDUCTION / PREREGISTRATION DESIGN**

## Charged exact sources

```text
a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf  cases/max12_912_order3_fibre_20260824/order3_fibre.py
b9df8e900f4f07017a8d04bb30888356a4dbf0fc68ec0ad966a0bd7985f2080c  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
a7bd6275cf44aee87b8aa7b706fe67317d89e15dd776d4425b63074a57e95991  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-20260825.md
```

No component calculation is charged here.

## 1. The descended two-parameter Rees equations

Let `D_ell(s,A,k)` denote the **unshifted raw descended tail**.  Thus the
compiled rows are

```text
R_ell=D_ell-delta_ell,
delta_3=mu,       delta_6=nu,       delta_8=1,
delta_ell=0 otherwise.                                  (1)
```

This distinction is load-bearing: the formulas below use `D_ell`, not the
already shifted `R_ell`.

Put `q=s-1`, `w_i=9-i`, and normalize coefficient infinity by

```text
B_i=Lambda^w_i A_i.
```

The frozen tails are weighted homogeneous of weight `12+ell` when
`wt(A_i)=9-i` and `wt(k)=6`.  Character descent changes only powers of `s`
and does not change this weight.  Multiplying `D_ell=delta_ell` by
`Lambda^(12+ell)` therefore gives the exact polynomial Rees equations

```text
Phi_ell(q,Lambda,B)
 =D_ell(1+q,B,Lambda^6 k)-Lambda^(12+ell) delta_ell=0.   (2)
```

A strict branch has `ord(Lambda)>3 ord(q)`.  The algebraic substitution

```text
Lambda=q^3 rho                                             (3)
```

encodes that strict inequality by requiring `q,rho` both to vanish on the
boundary and both to be nonzero at the generic point.  Equations (2) become

```text
Psi_ell(q,rho,B)
 =D_ell(1+q,B,q^18 rho^6 k)
  -q^(3(12+ell)) rho^(12+ell) delta_ell=0.              (4)
```

Accordingly, the currently registered formula (4) is **SOURCE-CORRECT**, if
its symbol `T_ell` means the unshifted raw descended polynomial `D_ell`.
It is not correct if `T_ell` means the compiled shifted row `R_ell`; in that
case one must first undo (1), or equivalently scale the load symbols inside
the row as well.

Merely saturating (2) by `q Lambda` and then setting `q=Lambda=0` does not
isolate the strict sector: it also sees slopes at or below three.  The chart
(3), followed by the `rho=0` boundary, is essential.

## 2. Exact isotrivial ordinary-tail chart

Adjoin the etale local coordinate `t` with

```text
s=t^3,       tau=t-1,       q=t^3-1=tau u(tau),
u(tau)=3+3tau+tau^2,
```

where `u(0)=3` is a unit.  The compiler uses

```text
a_i=t^(i mod 3) A_i,       e_ell=(2ell mod 3).
```

Its monomial-by-monomial descent is exactly the identity

```text
r_ell(a,k)=t^e_ell D_ell(t^3,A,k),                     (5)
```

where `r_ell` is the ordinary frozen Faber tail.  Hence the eight descended
equations are, over `L(t)`, the isotrivial ordinary-tail fibre

```text
(r_1,...,r_8)(a,k)=(0,0,mu,0,0,nu,0,t).               (6)
```

Only the eighth target moves with the base coordinate.

Set

```text
C_i=t^(i mod 3) B_i,
rho_t=u(tau)^3 rho.
```

Then `Lambda=q^3 rho=tau^3 rho_t`.  Equations (4) are carried by an
invertible etale/unit coordinate change to

```text
widehat_Psi_ell(tau,rho_t,C)
 =r_ell(C,tau^18 rho_t^6 k)
  -tau^(3(12+ell)) rho_t^(12+ell) gamma_ell(tau)=0,     (7)

gamma_3=mu,       gamma_6=nu,       gamma_8=1+tau,
gamma_ell=0 otherwise.
```

Thus (7) is an exact accelerator for (4), not a specialization or an
approximation.  It preserves the strict boundary, projective coefficient
point, formal arcs, and all local saturation questions.

## 3. Exact saturation criterion

Fix a characteristic-zero constant field `L` and declared constants
`k,mu,nu`, or keep those symbols in the coefficient ring if a theorem is to
hold uniformly on load space.  In either chart let

```text
I=(Psi_1,...,Psi_8),
K=I:(q rho)^infinity,                                  (8)
J=K+(q,rho),
H=J:(B_0,...,B_7)^infinity.                            (9)
```

The ordinary chart uses `(tau rho_t)` in place of `(q rho)`.  Saturation in
(8) takes the closure of the locus on which both parameters are nonzero; it
removes components supported wholly on either coordinate axis.  Saturation
in (9) is performed **after** taking the boundary and removes only the
irrelevant affine coefficient point.

The proved boundary radical is the common-cubic prime.  Use the triangular
coordinates

```text
p=B_7/3,       c=B_6/3,
x_4=B_5-3p^2,
x_5=B_4-6pc,
x_6=B_3-p^3-3c^2,
x_7=B_2-3p^2c,
x_8=B_1-3pc^2,
x_9=B_0-c^3.                                           (10)
```

The boundary has reduced equations `x_4=...=x_9=0`, and its projective
irrelevant ideal is `(p,c)`.  A fail-closed chart calculation must cover:

1. the overlap `p c!=0`;
2. the `p`-axis centre `p!=0,c=0`;
3. the `c`-axis centre `c!=0,p=0`.

The overlap `pc!=0` must remain a symbolic chart.  It is not represented by
one generic numerical point: the weighted invariant `c^2/p^3` varies there,
and the cubic discriminant

```text
Delta=-4p^3-27c^2
```

can vanish while `pc!=0`.  Localization only at `pc` retains this locus.  If
a normal-form or Kuranishi calculation divides by `Delta`, it must add a
separate exact `Delta=0,pc!=0` chart.

First form (8) and specialize to the boundary; only then impose `c=0` or
`p=0`.  Imposing an axis on the whole family can miss arcs which leave that
axis away from their centre.  Saturation by the product `p c` sees only the
overlap and loses both axes.  Likewise, one must not saturate away the
transverse ideal `(x_4,...,x_9)` unless a separate theorem proves that no
loaded solution can remain in it.  The normal variables must be retained in
the deformation calculation even though their boundary radical is zero.

## 4. Why `H=(1)` is a slope-uniform exclusion

Let a rational strict branch have

```text
alpha=max_i pole(A_i)/(9-i)=m/n>3,       gcd(m,n)=1.
```

On `q=epsilon^n`, take

```text
Lambda=epsilon^m,
rho=epsilon^(m-3n),
B_i=epsilon^(m(9-i))A_i(1+epsilon^n).
```

Then all `B_i` are regular, at least one `B_i(0)` is nonzero, and the branch
defines a homomorphism from the Rees coordinate ring to a domain of formal
series.  It kills `I`, while `q rho` is nonzero at the generic point.  If
`F` lies in `K`, then `(q rho)^N F` lies in `I` for some `N`; cancellation in
that domain shows that the branch also kills `F`.  Its centre therefore
defines a nonirrelevant zero of `H`.  Consequently

```text
H=(1)  implies that no strict rational branch exists.                  (11)
```

This implication needs neither a bounded slope enumeration nor an
assumption that a formal branch is rational.  Equivalently, algebraic curve
selection says that any component of the saturated interior closure through
the projective boundary supplies a formal/Puiseux arc after a finite field
extension.  The converse is deliberately weaker: `H!=1` is at most an
algebraic/Puiseux accessibility result.  It does not make that arc rational
over `L(q)`, satisfy the exact D1 monodromy, or certify a constant-field
section.

For a rational branch, the already proved monodromy restriction gives
`n=1` on `pc!=0`, `n in {1,2}` at a `p`-axis centre, and `n in {1,3}` at a
`c`-axis centre.  These restrictions may discard surviving algebraic arcs;
they are unnecessary when (11) succeeds.

## 5. Why no fixed jet follows from this reduction

At a common cubic write

```text
f=K^3+E.
```

At scaled `k'=0`, the Laurent expansion is

```text
f^(4/3)
 =K^4+(4/3)K E+(2/9)K^-2 E^2-(4/81)K^-5 E^3+... .     (12)
```

The constant and linear terms in (12) are polynomials in `z`.  Since the
Faber tails are the negative Laurent part, every first derivative of the
tail map in a coefficient direction vanishes at `f=K^3`.  The derivative in
the scaled `k'` direction also has zero tails because `F_6(K^3)=K^2` is a
polynomial.  Thus the ordinary tail map has zero differential along the
entire exceptional common-cubic locus.

The exact isotriviality (6)--(7) makes the algebraic saturation finite, but
it does not make the singular Kuranishi problem linearly determined or put
a uniform bound on the contact order of arcs.  No conclusion from a fixed
`Lambda` jet, including the old order `20m`, is valid without an additional
finite-determinacy theorem.  The exact saturated ideal (8)--(9), computed
without truncation, is the safe next gate.

## 6. Fail-closed computational controls

Any AWS-only implementation should preregister all of the following.

- Reconstruct and hash the eight raw `D_ell`; verify (5) symbolically before
  using either chart.
- Check every exponent and target in (4) and (7), including the factor
  `gamma_8=t=1+tau` and the absence of `t` factors at rows 3 and 6.
- Recover the charged common-cubic boundary radical before interpreting a
  saturation result.
- Verify sequential saturation by `q` and `rho` agrees with saturation by
  `q rho`; include a synthetic component supported on each axis and check
  that it is removed.
- Include a synthetic accessible strict arc and check that its projective
  boundary survives; include a `rho`-unit slope-three arc and check that it
  is not counted at `rho=0`.
- Demonstrate that `pc`-product saturation loses both seeded axis controls,
  while the generic, `p`-axis, and `c`-axis chart union retains them.
- Emit each ideal in both original and ordinary coordinates, deterministic
  hashes, two-sided containment checks for any coordinate substitution, and
  exact unit/nonunit witnesses.
- Declare the constant base.  A calculation over `Q(k,mu,nu)` proves only a
  generic-load statement; it cannot silently cover `mu=0`, `nu=0`, other
  load strata, or a theorem uniform in all constants.  Fixed `r_8` load is
  the nonzero value `1` in (1).

## Firewall

This artifact proves the source equations, the etale isotrivial reduction,
and the sufficiency of the exact unit-ideal test.  It does not assert that
`H=(1)`, compute a saturation, bound a jet, promote a Puiseux arc to a
rational constant-field section, establish Taylor polynomiality, or close
D1, another passport, `(8,12)`, the maximum-twelve frontier, or JC2.
