# D1 strict coefficient-infinity: slope-uniform saturation gate

Date: 2026-08-25  
Status: **PREREGISTERED SOURCE/SCHEME GATE; NO RESULT**

## Exact source and reparameterization

Consume all eight independently reconstructed, reviewed descended rows

```text
R_l=T_l(s,A,k)-delta_l,
delta_3=mu, delta_6=nu, delta_8=1,
```

with weights `wt(A_i)=9-i`, `wt(k)=6`, and row weight `12+l`.
Put

```text
q=s-1, Lambda=q^3*rho,
Psi_l=T_l(1+q,B,q^18*rho^6*k)
      -q^(3(12+l))*rho^(12+l)*delta_l.
```

This is the weighted homogenization identity, not an interpolation.  Every
strict rational/Puiseux slope `m/n>3` is represented by

```text
q=tau^n, rho=tau^(m-3n), Lambda=tau^m.
```

Conversely, any arc with positive `q`- and `rho`-valuation has slope strictly
greater than three.  The symbol `rho` here is the new slope coordinate; the
old eighth target has already been normalized to `delta_8=1`.

## Registered ideals and verdicts

Over `Q[q,rho,B0,...,B7,k,mu,nu]`, compute

```text
I=(Psi_1,...,Psi_8),
K=I:(q*rho)^infinity,
H=((K+(q,rho)):(B0,...,B7)^infinity).
```

The characteristic-zero global computation is the arbiter.

- `H=(1)` excludes every strict coefficient-infinity formal/Puiseux arc
  whose projective leading coefficient is nonzero.  The bridge uses closure
  of the generic point after `q*rho` localization and projective saturation;
  a minimal pole normalization guarantees a nonzero leading `B`.
- `H!=1` is only the exact boundary survivor scheme.  It does **not** prove
  an arc, a rational section, Taylor polynomiality, or a D1 solution.
- `rho` a unit is the slope-three/bounded-sector control and is outside this
  strict boundary.  No statement about it follows from `H`.

The first implementation uses the exact polynomial automorphism

```text
B7=3p, B6=3c,
B_i=C_i(p,c)+X_i (0<=i<=5),
C=z^3+pz+c, f=C^3,
```

and saturates by `(p,c,X0,...,X5)`.  This is merely a common-cubic normal
coordinate system over `Q`; `p,c` remain variables.  It does not drop the
moving common-cubic directions.  A generic coefficient-field calculation
in `p,c` would be navigation only and would require separate discriminant,
double-root, `p`-axis, `c`-axis, and origin/rank strata before coverage.

## Isotrivial-twist accelerator and firewall

Over `L(t)`, put `tau=t-1`, so

```text
s=t^3, q=t^3-1=tau*(3+3tau+tau^2).
```

The original coefficient and tail characters differ from the descended
rows by powers of the unit `t`: `a_i=t^(i mod 3)A_i(s)` and

```text
r_l(a,k)=t^(2l mod 3) D_l(s,A,k).
```

Thus the ordinary tail target is

```text
(r1,...,r8)=(0,0,mu,0,0,nu,0,t).
```

With `C_i=t^(i mod 3)B_i` and
`rho_t=(3+3tau+tau^2)^3*rho`, the descended equations are carried by an
invertible etale/unit coordinate change to

```text
r_l(C,tau^18*rho_t^6*k)
 -tau^(3(12+l))*rho_t^(12+l)*gamma_l,
gamma_3=mu, gamma_6=nu, gamma_8=1+tau.
```

The compiler rebuilds every raw `D_l` from the ordinary tails and checks
this character identity monomial by monomial.  The twist licenses the exact
common-cubic normal coordinate change and quotienting its *certified tangent
image*.  It does not license deleting `p,c`, infer isotrivial rationality,
or replace the global ideal by a generic-load calculation.

For a rational descended arc, equivariance still filters denominators: the
generic common cubic has active weights two and three (`n=1`), the `c=0`
axis has `n|2`, and the `p=0` axis has `n|3`.  This filter is not needed for
an `H=(1)` exclusion and cannot promote a nonunit `H` to existence.

## Mandatory controls

1. Reconstruct all eight rows from the transitive frozen source and remove
   exactly the three target monomials.
2. For every raw monomial assert explicitly
   `sum_i (9-i)e_i+6e_k=12+l`; emit counts and row digests.
3. Verify all eight exceptional rows vanish after the common-cubic
   parameterization, exactly over `Q`.
4. Verify algebraically
   `q^18*rho^6 -> tau^(6m)` and
   `q^(3w)*rho^w -> tau^(mw)` for arbitrary `m/n>3`.
5. Synthetic strict-arc control must leave a nonunit boundary ideal.
6. A component supported only on `q*rho=0` must disappear under the first
   saturation.
7. Sequential saturation first by `q` and then by `rho` must agree in both
   ideal containments with saturation by `q*rho` on the source ideal.
8. A synthetic `rho`-unit slope-three arc must not appear at the registered
   strict boundary `rho=0`.
9. Saturation by the full irrelevant **ideal** must preserve a projective
   coordinate-axis point; saturation by the coordinate product must erase
   it and is retained only as a negative control.
10. Any source/closure/control failure is terminal and produces no evidence.

If the global `H` is nonunit or resource-inconclusive, the reviewed
common-cubic radical permits exactly two targeted projective charts:
`B7!=0` (`p!=0`) and `B6!=0` (`c!=0`).  These chart equations are imposed
only after the interior `q*rho` saturation.  The symbolic overlap retains
the invariant `c^2/p^3` and the discriminant-zero sublocus; it is not a
single generic sample.  No pivot may divide
`Delta=-4p^3-27c^2` without splitting `Delta!=0` from `Delta=0`; the latter
has `p*c!=0` points and is not covered by the axes.  Axis centres are not
imposed along the whole arc.

## Scope firewall

The reviewed Mason theorem identifies only the reduced order-zero support as
the common-cubic surface.  It does not determine scheme thickness or normal
deformations: finite loads raise the relevant `g^3-f^4` degree bounds, and
the `k!=0` normal pivot is unavailable because `q^18*rho^6*k` vanishes at
the boundary.  No fixed-total-D12, Taylor, existence, exclusion, or JC2
claim is licensed without the registered saturated computation and its
separate source/compiler review.
