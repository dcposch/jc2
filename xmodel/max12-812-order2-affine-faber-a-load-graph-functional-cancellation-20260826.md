# Affine-Faber `A`: load-graph cancellation in the row functional

Date: 2026-08-26

Status: **EXACT COEFFICIENT CONSEQUENCE; SUCCESSOR NAVIGATION ONLY.**

## 1. Frozen source

The complete normalized functional

```text
K=E*H3+H5
```

was reconstructed from all seven frozen ordinary-Faber rows and emitted as
371 exact monomials in

```text
e0a64e55ea21c41ee06e635740f7b8af375ce64855638cc44109afb8b384492a
  cases/max12_812_order2_affine_faber_a_full_k_multisupport_20260826/RESULT.md
```

with exact-Q/F65521 exponent agreement.  The finite field is only a
software control.  This note reads exact-Q coefficients from that frozen
support and does not enlarge its scope.  The graph used below is charged to
the corrected ordinary-Faber classification and its promotion:

```text
77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e
  xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md
4ddc0e4837e1581129fddad70fc7b5c029d642e644f4fd8ab478a4dec59bded3
  xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-hostile-review-grok-20260826.md
817b96968a4a5abecfc785cc0fe2bba57c50d0a5cd52dabe2bccdef26e8846af
  xmodel/max12-812-order2-exact-square-affine-faber-support-promotion-20260826.md
```

## 2. The two first load-bearing coefficients

Set the kernel and complement variables to zero and retain the terms that
are linear in the center `a` or the normal scale `lambda`.  Exact Q gives

```text
[lambda]K
 =lambda*M*E*(15*K10*E^4/1024
              -3*K6*E^2/64
              +K2/8),                              (2.1)

[a]K
 =a*(25*K10*E^7/1024
     -9*K6*E^5/128
     +K2*E^3/8
     -mu2*E+4*mu4).                                (2.2)
```

Here `[a]` and `[lambda]` mean the homogeneous degree-one parts after the
other positive-weight variables are set to zero.  Equation (2.2) does not
discard the separately typed cubic target term `20*mu2*a^3`.

On the repeated-`A` closed point put `D=E^2/4`.  The corrected affine-Faber
`A` graph is

```text
K6   =K10*(15*D/8)      =K10*(15*E^2/32),
K2   =K10*(15*D^2/16)   =K10*(15*E^4/256),
mu2  =K10*(-5*D^3/64)   =-K10*(5*E^6/4096),
mu4  =0.                                           (2.3)
```

Substitution in (2.1)--(2.2) gives, coefficientwise,

```text
15/1024-45/2048+15/2048=0,
100/4096-135/4096+30/4096+5/4096=0.               (2.4)
```

Thus both first load-bearing directions cancel on the exact affine graph.
This is the local algebraic reason a raw support hull can report an early
load wall that disappears after predecessor/graph reduction.

## 3. Correct transverse coordinates for a general load fan

Use deviations from (2.3), not the three raw loads independently:

```text
d6 =K6-(15*E^2/32)*K10,
d2 =K2-(15*E^4/256)*K10,
dm =mu2+(5*E^6/4096)*K10,
d4 =mu4.                                           (3.1)
```

The change is polynomial and two-sided, with inverse obtained by adding
the displayed graph terms.  Equations (2.1)--(2.2) become

```text
[lambda]K=lambda*M*E*(-3*E^2*d6/64+d2/8),          (3.2)

[a]K=a*(-9*E^5*d6/128+E^3*d2/8-E*dm+4*d4).        (3.3)
```

On `D(E*M)`, the first possible transverse load-normal walls are therefore

```text
v(d6)+v(lambda),   v(d2)+v(lambda),
v(d6)+v(a),        v(d2)+v(a),
v(dm)+v(a),        v(d4)+v(a),                    (3.4)
```

not the corresponding raw central-graph load forms.  Coefficient-factor
subfaces arise when either linear combination in (3.2)--(3.3) vanishes;
they must retain the next 371-term support and the complete predecessor
ideal.

## 4. Minimal successor client

The next multigraded client should substitute (3.1) into the frozen exact
371-term polynomial before constructing any Newton hull.  It should:

1. emit exact coefficient groups in `(a,lambda,X,Y,R*,S*,d6,d2,dm,d4,K10)`;
2. factor coefficients over `Q[E,M]` and record every localization;
3. use (2.4) as a positive control and a one-coefficient perturbation as a
   negative control;
4. reduce each equality face by the registered first-normal and affine
   predecessor ideals before declaring a cone;
5. keep the old center-truncated q6 input as an omission-negative control.

The fixed delayed ray remains the first positive fixture: its reviewed
predecessor reduction closes all `q>0`.  The first new target is a slope
where one form in (3.4) ties the intrinsic `3*v(lambda)`.

## 5. Firewall

Equations (2.1)--(3.3) are exact normalized coefficient identities.  They
do not prove that a raw source arc lies on the affine graph, determine the
valuations of the four deviations, compute their equality-face ideals, or
cover another load ray.  This is not a source/Rees overlap, relative fan,
order-two, maximum-twelve, or JC2 result.
