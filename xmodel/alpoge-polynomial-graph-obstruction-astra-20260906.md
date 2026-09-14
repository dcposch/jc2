# Polynomial graph restriction of the explicit 3D map: a uniform obstruction

2026-09-06; root/Astra; basis0d39df3c9fd69c939a8420c54d03228b9077777d.
Lifecycle PRODUCER-CHECKED; different-model review pending. This is a
delimited failed plane-construction mechanism, not a JC2 theorem.

## Exact statement

Over any characteristic-zero field, define

```
P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
R=2x-3x^2 y-x^3 z.
```

For EVERY polynomial H in k[x,y], restrict to z=H(x,y). No affine-linear
map k^3->k^2 applied to these three restricted outputs has nonzero constant
Jacobian in (x,y). This includes every constant z-slice, every polynomial
graph degree, and every rank-two linear output projection. Precomposing the
graph parametrization by a polynomial automorphism of the plane does not
change this conclusion.

No statement about other graph orientations, general embedded planes,
nonlinear three-output projections, rational graphs, or arbitrary 3D maps
is made. In particular x=0 gives (P,Q)=(z+4y^2,y), a plane automorphism;
it is an explicit negative control against extending the theorem to all
graph orientations.

## Degree-uniform proof

Write d=deg H when H is nonconstant, and d=0 when H is constant, including
H=0. In the nonconstant case let h be its nonzero degree-d homogeneous
part and put T=x^3 h. In the constant case H=c put
T=x^2(cx+3y). Then T is nonzero homogeneous of degree d+3 and
T_x is nonzero of degree d+2. For d>0, T is divisible by x^3, so T_x=0
would contradict characteristic zero; for d=0,
T_x=3cx^2+6xy is visibly nonzero, including c=0.

The leading total-degree forms of the three restricted outputs are

```
p=y^3 T,       q=3y^2 T,       r=-T,
```

of respective degrees d+6,d+5,d+3. For d>0 the z-terms dominate
the z-free terms; for d=0 their two same-degree contributions combine
into the displayed T, so the constant case is not discarded.

Direct differentiation gives

```
J(p,q)=-3y^4 T T_x,
J(p,r)= 3y^2 T T_x,
J(q,r)= 6y   T T_x.
```

All three are nonzero. They are therefore the leading forms of the
actual three Jacobian minors after restriction, whose exact degrees are

```
deg J(P_H,Q_H)=2d+9,
deg J(P_H,R_H)=2d+7,
deg J(Q_H,R_H)=2d+6.
```

If M is the constant2x3 projection matrix, the new Jacobian is the
Cauchy--Binet linear combination of these three minors with coefficients
the three2x2 minors of M. If rank M=2, not all coefficients vanish.
The three positive degrees are distinct, so the highest degree whose
coefficient is nonzero cannot cancel. The new Jacobian is nonconstant.
If rank M<2 it is zero. Output translations have no effect. A plane
polynomial automorphism has nonzero constant Jacobian and injectively
pulls back nonconstant polynomials, proving the last assertion.

Thus this entire construction family can be ruled out before solving
for H, independently of a degree cutoff. The proof does not infer the
two-dimensional Jacobian from the three-dimensional determinant.

## Controls, provenance, and limits

The explicit map was checked against the displayed formula in
[Zihan Zhang's July20 derivation](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html),
read on September6 at13:59UTC. The linked original Alpoge X announcement
returned403; this does not close the campaign's social coverage hole.
The theorem above is self-contained for the displayed three polynomials
and needs no trust in the map's announced 3D noninjectivity or any other
result in that source. No external novelty claim is made.

History checksum: current APPROACHES, the entire historical46-row table,
the1210synthesis, and terminal-report text searches for polynomial graph,
graph section, polynomial section, and graph/projection descent. Existing
avenues34/35 already warn that a constant3x3 determinant does not imply a
constant2x2 minor; this calculation extends that check to an explicit
unbounded graph family and all constant projections. The exact uniform
formula was not located in that bounded search, which is not proof of
novelty. The noncanonical triangular-action proposal in sol-lateral remains
a different mechanism and is not excluded here.

Tiny checker: box/alpoge-polynomial-graph-20260906/check.py,
SHA256 ff07e2d6915b21fd6ea9a112b01e63f897859d3781faed2c7490aeb128c354bc.
It checks H=0,1,-2x+3y+1,x^2+y and all three leading minors, plus the
x=0 orientation control. The rational H=-3y/x can cancel x^3H+3x^2y,
showing why polynomiality is essential to the displayed leader argument;
it is not asserted to produce a polynomial pair or counterexample.

Commands, each capped at30seconds with script512MiB/25s limits:

```
python3 box/alpoge-polynomial-graph-20260906/check.py
python3 -O box/alpoge-polynomial-graph-20260906/check.py
python3 box/alpoge-polynomial-graph-20260906/check.py --mutate
python3 -O box/alpoge-polynomial-graph-20260906/check.py --mutate
```

Normal and -O positive runs PASS; both mutated runs fail at the required
graph-chain leading-form check. The mutation actually suppresses the
graph-chain derivatives by substituting into the ambient(x,y)minor before
differentiating H. A zero-Assert AST gate remains active in both modes.
Combined four-run time5.88s. An initial draft checker compared expanded
and factored SymPy expressions with structural equality; it failed before
publication and was repaired by expanding both sides. No mathematical
formula changed. Finite controls check transcription, not all H; the
proof above covers all degrees.

Immediate disposition: do not launch a polynomial-z-graph/linear-projection
search. Other proposed descents must identify their distinct mechanism
before receiving compute. No heavy CAS, AWS action, counterexample,
unrestricted plane obstruction, or blanket3D-to2D impossibility is claimed.
All root writers have finished before transactional finalization.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5874`.
- Body SHA-256:
  `2fe1629cadebae89aafb70b5feca76211c5d4806761629432997562ff1d666f4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
