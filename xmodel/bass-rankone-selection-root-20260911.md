# Rank one does not select the monic polynomial-G family

ROOT, MANUAL / UNREVIEWED. Opened September11 22:09UTC,2026.
Original publication reserve22:17/HARD22:20. Basis
0d39df3c9fd69c939a8420c54d03228b9077777d. Self-contained algebraic
discriminator; no scientific execution or external theorem premise.

Let B=C[t,z], E=C(t,z), sigma(t)=t, sigma(z)=z-1, and
U=B[delta;sigma], so delta b=sigma(b)delta. This matches
t=ep+eq, z=ep for delta=p partial_q. Define a rank-one E-space M=Ev
with semilinear action

    delta(bv)=sigma(b)a(z)v,
    a(z)=z(z-t-1)/(z-t/2-1).                             (1)

Restricting scalars makes M a B-torsion-free U-module. Every vector is
U-torsion: delta(bv)=[sigma(b)a/b](bv), and clearing the rational
coefficient's denominator supplies a nonzero polynomial-coefficient
first-order relation. Generic Euler rank is exactly1. Delta is bijective
since a is nonzero and sigma is an automorphism. M is not claimed to be
finitely generated over B, a holonomic Weyl module, or any actual Keller
source quotient. None of those extra properties is used or refuted here.

CLAIM. No nonzero w in M is killed by

    z-r+delta G(z,t-z),

for ANY r>=0 integer and ANY G in C[X,Y].

Write w=b(z)v with b in C(t)(z)^*. Put H(z,t)=G(z,t-z). Such an
annihilator would give

    z-r+H(z-1,t)a(z)b(z-1)/b(z)=0.                      (2)

If H=0 this is impossible. The rational quotient b(z-1)/b(z) tends
to1 at z=infinity over C(t), and a(z) has leading term z. Therefore
(2) forces deg_z H=0 and its coefficient to be -1; thus H=-1.
There can be no cancellation of a higher z-degree term against z-r.
Equation(2) then requires

    b(z-1)/b(z)=(z-r)(z-t/2-1)/(z(z-t-1)).              (3)

For every rational b over C(t), the divisor of b(z-1)/b(z) has total
multiplicity zero on each integer-translation orbit of finite points
of the algebraic closure of C(t). Proof: ord_alpha b(z-1)=
ord_(alpha-1)b(z); the difference telescopes on the orbit, because a
rational function has only finitely many zeros and poles. This also
handles non-linear irreducible factors of b after algebraic closure.

On the right side of(3), the zero r and pole0 lie in the same orbit.
But the zero t/2+1 and pole t+1 lie in distinct orbits from each other
and from that constant orbit: their differences are nonconstant in the
transcendental parameter t, hence cannot be integers. The orbit of t/2+1
has total multiplicity+1, violating the preceding necessary condition.
Equation(3) has no rational solution b. This proves the claim, including
r=0 where the constant-orbit factors cancel directly.

## What the countercontrol separates

Even rank1, B-torsion-freeness, U-torsion and invertible delta do not
select the ep-r+delta(polynomial G) form on any nonzero vector. A rank2
example excluding EVERY first-order relation would answer a different
question: the obstruction here persists after first-order existence is
already guaranteed. It is the rational coefficient's divisor along shift
orbits, not just the size of the localized space.

For orientation only, the rational multiplier(1) is the one suggested
by the independently derived nonmonic operator
2ep(eq+1)+delta(ep-eq) acting on sqrt(1-q(p+q)). Nothing in this proof
assumes that the formal-germ U-module is isomorphic to M. The control
has no polynomial Keller-source realization here. It refutes only an
inference from the listed abstract module properties, not a theorem
using additional source algebra, holonomicity or geometric input.

No novelty, general U-injectivity, actual source construction, degree bound
or JC2 conclusion. No new named OPEN or automatic successor. This proof
is to receive independent review with the rank/normalization discriminator,
not counted as promoted evidence before that gate. Own full readback,
marker-only-at-completion and expected transaction verification required.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3887`.
- Body SHA-256:
  `83499f86bc20fa726b7dce465f29f635cf52d72c88eaa8eb10ee9d904403f170`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
