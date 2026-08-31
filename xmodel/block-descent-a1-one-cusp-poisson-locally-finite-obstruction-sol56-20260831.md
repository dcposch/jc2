# One-cusp pseudo-plane: locally finite Hamiltonians, ML firewalls, and an exact etale countercontrol

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra (`one_cusp_poisson` lane)  
Frozen basis: `b6a73150edc586af1f14a14a9c86efa3b10e2958`  
Lifecycle: **FINAL EXACT CONDITIONAL OBSTRUCTION / MIXED-MIXED HORN OPEN**

## 0. Verdict

Work in the exact primitive `(mu,r)=(2,2)` pseudo-plane ring

```text
R=C[A,U,Z]/(U^2-A-A^2 Z),
{A,U}=2A^2,   {A,Z}=4U,   {U,Z}=2+4AZ.                 (0.1)
```

The locally-nilpotent observation in the charged ideation can be made both
rigorous and strictly stronger.

> **Locally-finite Hamiltonian theorem.**  For every nonconstant `H in R`,
> the following conditions are equivalent:
>
> ```text
> X_H={H,-} is locally finite;
> X_H is locally nilpotent;
> H lies in C[A].                                      (0.2)
> ```
>
> No locally finite Hamiltonian derivation of `R` has a slice.

The proof uses the published full automorphism formula for this exact
pseudo-plane.  Every automorphism has

```text
A |-> lambda^2 A,
U |-> lambda U+A^2 Q(A),                              (0.3)
```

and scales the canonical symplectic form by `lambda^(-1)`.  Consequently no
nontrivial algebraic torus action preserves the symplectic form.  The
Zariski closure of the flow of a locally finite Hamiltonian derivation is
therefore unipotent, which makes the derivation locally nilpotent.  Every
additive action fixes `A`, so its kernel is `C[A]`.  Finally a locally
nilpotent derivation with a slice would give `R=C[A,s]`, contradicting
`Pic(R)=Z/2`.

Thus a hypothetical pair

```text
f,g in R,       {f,g}=c in C*                         (0.4)
```

forces **both** commuting Hamiltonian derivations `X_f` and `X_g` to be
non-locally-finite.  Moreover each of `f,g:Spec(R)->A1` is a smooth
surjection whose generic fibre is not `A1`.  This is a real narrowing, but it
does not exclude the mixed/mixed horn.  Proving that a Hamiltonian derivation
with a slice is locally nilpotent without using the special pseudo-plane
geometry would be circular: on `A2` that assertion is equivalent to JC2.

The Makar--Limanov, Derksen, Picard, and `A1`-fibration shortcuts stop at
exact countercontrols.  In fact this same surface has the degree-two
nonproper etale endomorphism

```text
eta(A,Z,U)=(U^2, 4Z, U(1+2AZ)).                       (0.5)
```

It sends the ruling coordinate `A` to the mixed function `U^2`, does not
preserve `ML(R)=Dk(R)=C[A]`, and induces the zero map on
`Pic(R)=Z/2`.  Hence none of those invariants is functorial enough under an
etale map to force a target coordinate to align with the unique additive
ruling.  Formula (0.5) is not a map to `A2` and does not supply a slice; it
is a firewall, not a horn witness.

The exact surviving target is therefore:

```text
two algebraically independent, non-locally-finite Hamiltonians f,g,
{f,g}=c, [Frac(R):C(f,g)]=4,
with the charged (3,1)+(2,2) boundary packet.          (0.6)
```

## 1. Frozen inputs and external theorem

The direct campaign inputs are

```text
0e2e09c8a81cead797483cfd91f093c98ccba48ca50767056aa42ac709214b94
  xmodel/block-descent-a1-quartic-cycle1-invariant-ring-quartic-gate-control-sol56-20260830.md
985f66316961ddd8555ae96516cadef0cba26c30854f4bdc99a157a06dc5f045
  xmodel/block-descent-a1-quartic-cycle1-ruling-aligned-log-jacobian-obstruction-sol56-20260830.md
7a596c650a3f107fb493a3f9ff1caceac6b27a4728d111450c16f9a61e25032f
  xmodel/ideation-20260831T0512Z-opus5.md
```

The load-bearing external input is the automorphism classification specialized
in (0.3).  It is equation (5.12) of A. Dubouloz and K. Palka, *The Jacobian
Conjecture fails for pseudo-planes*, Adv. Math. 339 (2018), 248--284,
DOI `10.1016/j.aim.2018.09.020`, itself invoking Miyanishi--Masuda's full
automorphism theorem.  The exact arXiv v2 PDF used here is

```text
https://arxiv.org/pdf/1701.01425v2
SHA-256 41150cfda4fdf477efefc7d2ce55bc5fb49941705620b567b3333df5fe84281e.
```

Their variables `(u,v,w)` are our `(A,Z,U)`.  Their surface
`S(2,2,1)={u(1+uv)=w^2}` is literally (0.1), not merely birational to it.
For `k=2` and `rbar=1`, their formula reads exactly (0.3), with the third
coordinate uniquely determined by the hypersurface equation.

The report proves the consequences of that formula directly.  It does not
claim a new proof of the published automorphism classification.

## 2. Intrinsic geometry of the exact ring

Put

```text
q=U^2-A-A^2Z.
```

The gradient is

```text
q_A=-1-2AZ,       q_U=2U,       q_Z=-A^2.
```

If `A!=0`, then `q_Z!=0`; if `A=0`, the equation gives `U=0` and
`q_A=-1`.  Thus `Spec R` is smooth.

There is one prime over `A=0`,

```text
P=(A,U).
```

At its generic point `1+AZ` is a unit and
`U^2=A(1+AZ)`, so

```text
div(A)=2P.                                             (2.1)
```

After inverting `A`,

```text
R[A^(-1)]=C[A,A^(-1),U]
```

is factorial.  Nagata localization therefore says that `Cl(R)` is generated
by `[P]`, and (2.1) says its order divides two.  The class is nonzero: if
`P=div(h)`, then `h^2/A` has zero divisor and is a unit, so `A` would be a
square up to a complex scalar in

```text
Frac(R)=C(A,U).
```

The ordinary `A`-adic valuation of this rational function field has value
one on `A`, ruling that out.  Smoothness now gives

```text
Pic(R)=Cl(R)=Z/2<[P]>.                                 (2.2)
```

The same localization proves

```text
R^*=C*.                                                (2.3)
```

Indeed a unit becomes `c A^n` in `R[A^(-1)]`; regularity of it and its
inverse along `P` forces `n=0`.

## 3. The Poisson structure is globally symplectic

The three brackets in (0.1) annihilate `q`, hence descend to `R`.  They have
rank two everywhere: `{A,U}=2A^2` is nonzero on `D(A)`, while on `A=0`
the equation gives `U=0` and `{U,Z}=2`.

Let `omega` be the inverse symplectic form.  On `D(A)` it is

```text
omega=dA wedge dU/(2A^2).                              (3.1)
```

The alternative expressions using `(A,Z)` or `(U,Z)` show that (3.1)
extends regularly and nowhere vanishing across `P`.  In particular every
Hamiltonian vector field preserves it:

```text
L_(X_H) omega=d(i_(X_H)omega)=d(+/- dH)=0.             (3.2)
```

This is the essential extra hypothesis missing from a generic derivation
with a slice.

## 4. The automorphism character has no symplectic torus in its kernel

Specializing the published automorphism formula, every `phi in Aut(R)` has
unique data `lambda in C*`, `Q in C[A]` with

```text
phi(A)=lambda^2 A,
phi(U)=lambda U+A^2Q(A),                               (4.1)
phi(Z)=lambda^(-2)Z+2lambda^(-3)UQ(A)
       +lambda^(-4)A^2Q(A)^2.
```

Substitution verifies the last line and preservation of `q`.  From (3.1),

```text
phi^*omega
 =d(lambda^2A) wedge d(lambda U+A^2Q(A))
    /(2(lambda^2A)^2)
 =lambda^(-1)omega.                                   (4.2)
```

Now let an algebraic torus `T` act on `Spec R`.  The `lambda` in (4.1)
gives a character `lambda:T->G_m`.  If that character were trivial, the
action would land in the additive `Q`-subgroup of (4.1).  A morphism from a
torus to a unipotent group is trivial (the image lies in a finite-dimensional
coefficient subspace), so every nontrivial torus has nontrivial `lambda`.
Equation (4.2) then proves:

```text
No nontrivial algebraic torus action on Spec(R) preserves omega.  (4.3)
```

Notice that the standard hyperbolic action has weights
`wt(A),wt(U),wt(Z)=(2,1,-2)` and weight `-1` on `omega`, in agreement
with (4.2).

## 5. Locally finite Hamiltonians are locally nilpotent

Let `D` be a locally finite derivation of `R` satisfying `L_D omega=0`.
Choose a finite-dimensional `D`-stable vector subspace `V` containing `1`
and a finite set of algebra generators of `R`.  The analytic one-parameter
subgroup

```text
exp(tD)|V
```

acts by algebra automorphisms of `R`.  Let `G` be its Zariski closure in
`GL(V)`.  Multiplicativity and every defining relation are closed conditions,
so `G` is a connected commutative linear algebraic group acting on `R`.
Equation `L_D omega=0` gives `exp(tD)^*omega=omega`; this is also closed,
so all of `G` preserves `omega`.

If the torus part of `G` were nontrivial, it would contradict (4.3).
Therefore `G` is unipotent.  Its Lie algebra acts nilpotently on `V`, so
`D|V` is nilpotent.  Since `V` generates `R`, every element of `R` is killed
by some power of `D`.  Thus

```text
D locally finite and volume preserving  =>  D locally nilpotent. (5.1)
```

Every Hamiltonian derivation is volume preserving by (3.2), proving the
first implication in (0.2).

## 6. Additive actions, ML/Derksen, and the slice obstruction

An additive action gives a homomorphism `G_a->Aut(R)`.  Its `lambda`
component in (4.1) is trivial because `Hom(G_a,G_m)=0`.  Hence every locally
nilpotent derivation `delta` satisfies

```text
delta(A)=0.                                            (6.1)
```

For a nonzero `delta`, localize at `A`.  Then

```text
R_A=C[A,A^(-1),U],
R_A tensor_(C[A,A^(-1)]) C(A)=C(A)[U].
```

A nonzero locally nilpotent derivation of the one-variable polynomial ring
over `C(A)` has kernel `C(A)`.  Also

```text
R intersect C(A)=C[A]:                                (6.2)
```

localization first gives a Laurent polynomial in `A`, and regularity along
`P` removes every negative exponent.  It follows that

```text
ker(delta)=C[A]                                       (6.3)
```

for every nonzero locally nilpotent derivation.  Consequently

```text
ML(R)=Dk(R)=C[A].                                     (6.4)
```

If `H` is nonconstant and `X_H` is locally finite, Section 5 makes it a
nonzero locally nilpotent derivation; since `H in ker(X_H)`, (6.3) gives
`H in C[A]`.  Conversely, for `H in C[A]`,

```text
X_H=H'(A)X_A,
X_A(A)=0,       X_A(U)=2A^2,       X_A(Z)=4U,
```

which is locally nilpotent.  This completes (0.2).

Finally, suppose a locally nilpotent `delta` had a slice `s`, so
`delta(s)=1`.  The slice theorem and (6.3) would give

```text
R=ker(delta)[s]=C[A,s],
```

whose Picard group is zero, contradicting (2.2).  Thus no locally finite
Hamiltonian has a slice.

For (0.4), `c^(-1)X_f` has slice `g`, and `-c^(-1)X_g` has slice `f`.
Both derivations are therefore non-locally-finite.  This conclusion does not
use the quartic field condition; that condition remains extra information.

There is also a precise `A1`-fibration consequence.  The nonzero bracket
makes `df` and `dg` pointwise independent, so each coordinate morphism is
smooth.  Each is surjective: if, for example, `f` omitted `a in C`, then
`f-a` would be a unit, contradicting (2.3).  If the generic fibre of `f`
were `A1`, the standard affine-surface `A1`-fibration construction would
give a nonzero locally nilpotent derivation with kernel `C[f]`.  Equation
(6.3) would force

```text
C[f]=C[A],
```

and hence `f=alpha A+beta`.  But `{A,-}` vanishes along `P`, so such an `f`
cannot be one coordinate of (0.4).  Thus both `f` and `g` have non-`A1`
generic fibres.  Uniqueness of the additive ruling is useful only after the
missing generic-fibre assertion; it does not supply that assertion.

### 6.1 An exact smooth `C*`-fibre control without a slice

The mixed function `U` shows that the non-`A1` alternative is real, not a
formal loophole.  Its Hamiltonian field satisfies

```text
X_U(A)=-2A^2,             X_U(Z)=2+4AZ.
```

These two values never vanish simultaneously, so `U:Spec(R)->A1` is smooth;
it is surjective by (2.3).  For `t!=0`,

```text
R/(U-t)=C[A,A^(-1)],
Z=(t^2-A)/A^2,
```

so the fibre is `C*`.  At `t=0` the smooth fibre is the disjoint union

```text
P={A=U=0} isomorphic to A1,
Q={U=0,1+AZ=0} isomorphic to C*.                       (6.5)
```

Nevertheless `X_U` has no regular slice.  In
`Frac(R)=C(U,A)`, every rational solution of `{U,s}=1` is

```text
s=1/(2A)+h(U),             h(U) in C(U).               (6.6)
```

Along `P`, `ord_P(A)=2` and `ord_P(U)=1`; cancelling the order `-2` pole of
`1/(2A)` forces `h` to have a pole of order two at `U=0`.  But
`div(U)=P+Q`, while `A` is a unit at `Q`, so the same `h(U)` creates an
uncancelled order-two pole along `Q`.  Thus (6.6) never lies in `R`.

This is the exact analogue of a Broughton-type smooth fibration at infinity:
smoothness and a `C*` generic fibre do not manufacture a polynomial mate.
Any proposed `C*`-fibration closure must distinguish a genuine Keller
coordinate from this control.

### 6.2 Cofinite image forces a hyperbolic generic fibre

The slice and the quartic field condition sharpen the generic-fibre statement
further.  Let

```text
h=(f,g):Spec(R)->A2.
```

It is etale, hence open.  Its open image has finite complement.  Indeed, if
an irreducible target curve `V(p)` were omitted, then the nonconstant element
`p(f,g)` would have no zero on `Spec(R)` and hence would be a unit,
contradicting (2.3).  Thus

```text
h(Spec(R))=A2-E,              E a finite set.           (6.7)
```

Choose a general `a` such that the vertical line `{f=a}` misses `E`.  Then

```text
g:C_a=f^(-1)(a)->A1
```

is a **surjective etale map of degree four**.  The degree is exactly the
field degree `[Frac(R):C(f,g)]=4`.

This also rules out a `C*` generic fibre.  If `C_a=C*` with coordinate `t`,
then a regular etale map has Laurent derivative with no zero on `C*`, hence

```text
dg/dt=c t^n.
```

The exponent `n=-1` cannot be the derivative of a Laurent polynomial; for
`n!= -1`, integration gives `g=alpha t^(n+1)+beta`, whose image omits
`beta`.  It is not surjective.  Together with the `A1` exclusion above, a
hypothetical quartic pair therefore has a hyperbolic affine generic fibre:

```text
generic C_a is neither A1 nor C*.                      (6.8)
```

There is a finite degree-four ramification ledger for the surviving curve.
Let `Cbar_a` have genus `gamma`, let `S=Cbar_a-C_a`, split `S` into the
`r_infty` points over infinity and `s_fin` points over finite target values,
and write `e_p` for the ramification index of the completed degree-four map.
All ramification lies in `S`, so Riemann--Hurwitz gives

```text
sum_(p in S_fin)(e_p-1)+(4-r_infty)=2gamma+6,
sum_(p in S_fin)e_p=2gamma+2+r_infty+s_fin.            (6.9)
```

Surjectivity says that over each finite target value the sum of the `e_p`
for deleted points is at most three.  Equations (6.8)--(6.9), coupled to the
charged surface boundary, are the smallest honest curve-classification
successor.  The smooth `U`-fibration in Section 6.1 fails precisely at the
surjectivity/slice step and does not evade (6.8).

## 7. Exact etale countercontrol on the same surface

Define `eta^*:R->R` by

```text
A'=U^2,        Z'=4Z,        U'=U(1+2AZ).              (7.1)
```

Direct substitution using `U^2=A(1+AZ)` gives

```text
(U')^2=A'(1+A'Z'),                                    (7.2)
```

so this is an endomorphism.  Direct bracket calculations give

```text
{A',U'}=4 eta^*{A,U}=8(A')^2,
{A',Z'}=4 eta^*{A,Z}=16U',
{U',Z'}=4 eta^*{U,Z}=4(2+4A'Z').                      (7.3)
```

Because the Poisson tensor is nondegenerate, (7.3) says that the differential
is a symplectic similitude with nonzero constant multiplier.  Hence `eta` is
etale.  Generically `U` satisfies `U^2=A'`, while `Z=Z'/4` and
`A=(U'/U-1)/(2Z)`, so its function-field degree is at most two.  It is
exactly two: the nontrivial field involution

```text
U |-> -U,       Z |-> Z,       A |-> -A-1/Z
```

fixes all three expressions in (7.1).  This is the degree-two endomorphism
written in Dubouloz--Palka Example 5.3 / equation (5.8).

It has three exact consequences which block tempting shortcuts.

First,

```text
eta^*(A)=U^2 notin C[A]=ML(R)=Dk(R).                  (7.4)
```

Thus ML and Derksen are automorphism invariants, not covariant invariants of
an arbitrary etale map.

Second, let

```text
Q=(U,1+AZ).
```

The divisor of `U` is `P+Q`.  Pulling back `div(A)=2P` through (7.1) gives

```text
eta^*P=P+Q,
[Q]=-[P]=[P] in Pic(R)=Z/2,
eta^*[P]=0.                                           (7.5)
```

So even etale pullback can annihilate the entire torsion Picard group.

Third, `X_(U^2)` is non-locally-finite by (0.2), although on the subring
`eta^*R` it is four times the pullback of the locally nilpotent ruling
Hamiltonian `X_A`, by (7.3).  An etale extension can therefore turn a ruling
flow into a wild Hamiltonian flow on the ambient ring.

The map is nonproper (as proved in the cited paper); it cannot be a finite
degree-two cover from this Q-acyclic surface to itself, since finite covering
multiplicativity would give `e(R)=2e(R)` while `e(R)=1`.

Nothing in (7.1) is a pair of functions mapping to `A2`.  In particular it
does not solve (0.4) and is not a JC2 counterexample.  It proves only that
Picard, ML/Derksen, and uniqueness of the additive ruling do not by themselves
force an etale morphism to respect that ruling.

## 8. Derivation firewalls and affine-plane controls

Three distinctions are essential.

1. A derivation with a slice need not be locally nilpotent, even if locally
   finite.  On `C[x,y]`,

   ```text
   D=partial_x+y partial_y,       D(x)=1
   ```

   is the smallest control.  Its divergence for `dx wedge dy` is one, so it
   does not contradict Section 5.

2. Volume preservation plus a slice is not the same as Hamiltonianity on a
   surface with nonzero first de Rham cohomology.  On
   `C[s,t,t^(-1)]`, `D=partial_s+t partial_t` preserves
   `ds wedge dt/t` and has slice `s`, but

   ```text
   i_D(ds wedge dt/t)=dt/t-ds
   ```

   is not algebraically exact.  The exact pseudo-plane is Q-acyclic and our
   derivations are explicitly Hamiltonian, so this control only prevents an
   overgeneralization.

3. On `A2`, a universal assertion

   ```text
   Hamiltonian derivation with a polynomial slice => locally nilpotent
   ```

   is equivalent to JC2.  Indeed `X_f(g)=1` is exactly a Keller pair
   `{f,g}=1`.  If `X_f` is locally nilpotent, Rentschler plus the slice theorem
   makes `(f,g)` a polynomial coordinate pair; the converse is immediate.
   Hence no affine-plane derivation lemma of this strength is available as an
   independent input.

## 9. Theorem/gap map and cheapest successors

The exact status is:

| Proposed route | Exact result | Status for the horn |
|---|---|---|
| LND plus slice | Impossible by `Pic(R)=Z/2` | branch closed |
| Locally finite Hamiltonian plus slice | Locally finite implies LND by Sections 4--6 | branch closed |
| ML / Derksen | Both equal `C[A]` | only detects algebraic additive flows |
| Picard torsion | `eta^*:Pic(R)->Pic(R)` can be zero | no etale functorial obstruction |
| Unique additive `A1`-ruling | A Keller coordinate has non-`A1` generic fibre; (7.1) also moves `A` to `U^2` | rules out only the `A1`-fibre branch |
| Smooth `C*` fibration | `U` is smooth with generic fibre `C*`, but has no slice; a Keller coordinate cannot have generic fibre `C*` | branch closed |
| Etale selfmaps | Exact degree-two nonproper family exists | firewall, not map to `A2` |
| Mixed/mixed Keller pair | Both Hamiltonian flows must be non-locally-finite | open |

The highest-value exact successors are now:

1. **Boundary-to-algebraic-flow gate.**  Prove that the charged quartic
   `(3,1)+(2,2)` packet makes at least one of the two commuting Hamiltonian
   flows locally finite.  The theorem above would then close the horn
   immediately.  Without the boundary packet this is false as a plausible
   general principle and risks restating JC2.
2. **Hyperbolic fibre classification.**  Each coordinate of a Keller pair
   defines a smooth surjection with generic fibre neither `A1` nor `C*`.
   Enumerate the degree-four completion data in (6.9), then couple its finite
   deleted points and points over infinity to the charged boundary census.
3. **Wild-flow filtration.**  Use (0.3) and the hyperbolic weights
   `(2,1,-2)` to study a non-locally-finite `X_H` with a slice.  A successful
   theorem must consume the exact index-four field condition or boundary
   valuations.  Merely taking a highest homogeneous term cannot discard
   cancellations at the retained fibre.
4. **Etale-to-plane classification.**  Separate maps `R->R`, for which (7.1)
   supplies abundant countercontrols, from maps `C[s,t]->R` whose two images
   form an exact symplectic coframe.  The latter is the genuinely missing
   classification.

Do not promote an exclusion of the mixed/mixed one-cusp horn, local
nilpotence of an arbitrary Hamiltonian slice, functoriality of ML/Derksen or
Pic under etale maps, or preservation of the ruling by nonproper etale
endomorphisms.  No heavy computation is justified by this result.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20567`.
- Body SHA-256:
  `d25cf00344794cefc51eebf045f4c0daee52352d46d5352638a998ea432381bf`.
- Frozen basis: `b6a73150edc586af1f14a14a9c86efa3b10e2958`.
