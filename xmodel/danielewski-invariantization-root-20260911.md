# Scalar-pair invariantization preserves every Laurent weight

ROOT / manual proof / PRODUCER-CHECKED pending independent review.
September11,2026. Research resumed19:29UTC; publication reserve19:40,
HARD19:43UTC. Basis0d39df3c9fd69c939a8420c54d03228b9077777d.
No scientific computation, AWS allocation, regular scalar pair, global
exclusion or JC2 resolution is asserted.

## 1. Claim and exact rings

Over C put

    T=Spec C[x,t,Z]/(t^2-1-x^2 Z),
    S=Spec C[A,U,Z]/(U^2-A-A^2 Z),
    sigma(x,t,Z)=(-x,-t,Z),
    omega=dx wedge dt/x^2.

The form omega extends to a regular nowhere-zero form on T. Near x=0
it is dx wedge dZ/(2t); x and t have no common zero. There is a regular
nowhere-zero form Omega on S characterized by q*Omega=omega below.

CLAIM A: the following existence statements are equivalent:

1. Some H,G in O(T) satisfy dH wedge dG=c omega, c in C*.
2. Such a pair exists with both coordinates sigma-invariant.
3. Some h,g in O(S) satisfy dh wedge dg=c' Omega, c' in C*.

CLAIM B: for any pair in1, one can construct a pair in2 with exactly the
same finite Laurent weight support in EACH coordinate, not just the same
interval endpoints. If desired the scalar c is unchanged by rescaling the
second output. No bound on ordinary degrees is claimed.

The explicit maps used are classical. The attachment here is the existence
equivalence and exact support preservation for our present two searches.
No assertion of global novelty is made.

## 2. Three explicit maps and their exceptional loci

Define

    q:T->S,      (x,t,Z) |-> (x^2,xt,Z),
    j:S->T,      (A,U,Z) |-> (2U,1+2AZ,Z),
    E:T->T,      (x,t,Z) |-> (2xt,2t^2-1,Z).

All are morphisms: substitution checks their defining relations. In
particular (2t^2-1)^2-1=4t^2(t^2-1)=(2xt)^2 Z, and E=j composed q.

The invariant ring is exactly C[x^2,xt,Z]. Indeed every element is uniquely
a(x,Z)+t b(x,Z). Sigma-invariance makes a even and b odd in x. This gives
the displayed generators and their relation U^2=A+A^2Z.

The cover q is finite etale of degree2. Set B=1+AZ. The principal opens
A!=0 and B!=0 cover S, since B-AZ=1. On the first, adjoin x with x^2=A
and set t=U/x; on the second, adjoin t with t^2=B and set x=U/t. Both
are finite etale quadratic algebras, since the adjoined roots are units.
Equivalently sigma acts freely: x=t=0 is impossible on T.

Let L_minus={Z=0,t=-1} inside T. The map j identifies S with T minus
L_minus. On Z!=0 its inverse has A=(t-1)/(2Z), U=x/2; on t+1!=0 use
A=x^2/(2(t+1)), U=x/2. These formulas agree by the equation of T, satisfy
the equation of S, and are inverse to j. The two opens cover precisely
T minus L_minus. Conversely j cannot meet L_minus, since Z=0 forces its
t-coordinate to be1. Thus E has degree2, is etale, and its image is exactly
T minus L_minus, because q is surjective. E is NOT an automorphism or a
finite selfmap. L_minus is an entire affine x-line, not just one point.

This is not the different line D_minus={x=0,t=-1}. Removing D_minus
gives the affine-plane chart

    i(x,y)=(x,1+x^2y,2y+x^2y^2).

Confusing these two missing divisors would falsely construct a plane map.

## 3. Volume multipliers and the existence proof

Sigma preserves omega, so the free etale quotient descends it to Omega.
On A!=0 explicitly

    Omega=dA wedge dU/(2A^2),       q*Omega=omega.

Directly on a dense open of T,

    E*omega=d(2xt) wedge d(2t^2-1)/(2xt)^2=2 omega.

Both sides are global regular forms, hence the equality holds everywhere,
including t=0 and x=0. Since q is faithfully flat, E=j q then gives
j*omega=2 Omega. Alternatively this last identity follows by substituting
Z=(U^2-A)/A^2 on the dense chart of S.

Given H,G in1, put h=H composed j and g=G composed j. These are regular
on S and dh wedge dg=2c Omega, proving1=>3. Pullback along q proves3=>2,
and2=>1 is immediate. The transformed pair on T is exactly

    H_hat=H composed E,       G_hat=G composed E.

It is sigma-invariant and has scalar2c. Dividing G_hat by2 retains scalarc.
This is precomposition by a NONPROPER etale morphism, not averaging, nor a
claim of source- or target-automorphism equivalence with the initial pair.

For completeness, any such pair would give a JC2 counterexample upon
restriction along i. Its Jacobian is c because i*omega=dx wedge dy. If
that plane map had a polynomial inverse with second coordinate b, the
function b(H,G) would extend y=(t-1)/x^2 across all T. But y has an order2
pole at the generic point of D_minus, where x is a uniformizer and t-1
is a unit. Contradiction. This is a sufficient construction endpoint;
no converse reduction from an arbitrary JC2 counterexample to T is proved.

## 4. Exact weight support, including negative blocks

Grade O(T) by wt(x)=1, wt(t)=0, wt(Z)=-2. In O(T)[x^-1] every regular
function has a unique finite expression H=sum_m x^m p_m(t). Its negative
blocks satisfy

    (t^2-1)^k | p_m(t),        k=ceil(-m/2), m<0.       (1)

One elementary proof uses the two plane charts t=1+x^2y and t=-1+x^2v.
Taylor order a produces x-exponent m+2a and y- or v-exponent a. Different
m cannot cancel at fixed exponent pair. Polynomiality requires vanishing
order at least k at each of t=1 and t=-1, exactly(1). The converse follows
by the same expansions. For m>=0 there is no restriction.

For every integer m the pullback of a single block is

    E*(x^m p_m(t))=x^m p'_m(t),
    p'_m(t)=2^m t^m p_m(2t^2-1).                       (2)

For m>=0 this is polynomial. For m<0 write p_m=(t^2-1)^k a(t).
Equation(2) becomes

    p'_m=2^m 4^k t^(m+2k) (t^2-1)^k a(2t^2-1),

with m+2k either0 or1. This proves polynomiality AND the same regularity
divisibility without ignoring the apparent t-pole. A nonzero a remains
nonzero under the nonconstant substitution, so the block never disappears.
Different m remain different weights. Therefore the ENTIRE support set is
preserved. Also p'_m(-t)=(-1)^m p'_m(t), exactly sigma-invariance.

For any nonzero block of degree d in t, deg(p'_m)=2d+m. This may grow
arbitrarily and gives no finite coefficient bound. It is nonnegative under
(1). In particular support preservation does not mean fixed ordinary degree.

Consequently, if any scalar pair exists, choose one of globally minimal
sum of Laurent interval widths among ALL scalar pairs. Its transformed
invariant pair has that same global minimum. For a particular pair minimal
only in its own target-automorphism orbit, we do NOT claim that E preserves
that orbit or orbit-minimality. The exact statement needed for unrestricted
support searches is simply nonemptiness equivalence at each support pair.

## 5. Attacks, controls, and what this does not solve

The weight-minus-two control Z pulls back to Z: its Laurent polynomial
p(t)=t^2-1 cancels all apparent denominator powers in(2). At weight-minus-one,
E*(xZ)=2xtZ, a nonzero odd-parity block. These directly test the even and
odd negative cases of the formula. For a bracket check,

    {x,Z}=2t,
    {E*x,E*Z}={2xt,Z}=8t^2-4=2 E*{x,Z}.

The general multiplier is {E*H,E*G}=2 E*{H,G}; a scalar obstruction is
not accidentally lost in the transformation. E* is injective because E is
dominant, so a nonzero nonconstant bracket error stays nonzero nonconstant.
Precomposition alone cannot turn a failed full identity into a scalar one.

Reynolds averaging is a meaningful negative control: both x and tZ are
anti-invariant, but {x,tZ}=3t^2-1 is invariant and nonzero. Averaging both
arguments gives zero bracket rather than this result. This is a control
against the averaging argument, not a claimed scalar-pair example.

The omitted-line calculation is a second negative control against reading
E as an automorphism or treating its image as the affine-plane chart.
The genuine chart coordinate y=(t-1)/x^2 has

    E*y=Z/(2t^2).

At t=0 the relation forces x and Z to be units, so this has a genuine
order2 pole. The classical selfmap does not regularize this rational pair.
Likewise higher t-degree growth prevents a finite-degree search conclusion.

The previous Newton reduction of a FULL pair to nonintegral endpoint ratio
n/m (coprime n>m>=2) is not closed here. Its endpoints and scalar errors are
preserved. In particular the known mixed-moment countercontrol cannot become
a scalar pair by invariantization. No integer-ratio theorem, squarefree-root
condition, generic-fibre classification, finite-jet algebraization, or
all-JC2 reduction follows.

## 6. Provenance, composition pass, and decision

Primary known maps: Dubouloz--Palka, arXiv1701.01425v2, Example4.3 and
Corollary5.2/Example5.3. Their coordinates (x,y,z) are our (x,Z,t).
The published embedding (w,4v,1+2uv) becomes j after the target
automorphism (x,y,z)->(2x,y/4,z) and (u,v,w)=(A,Z,U).
All required relation, image, etaleness, volume and support facts are derived
above, not deferred to a title or theorem about a neighboring surface.

Primary retained PDF:
box/pseudoplane-cover-discriminator-root-20260911/dubouloz-palka-1701.01425v2.pdf
SHA25641150cfda4fdf477efefc7d2ce55bc5fb49941705620b567b3333df5fe84281e.
ROOT hash-checked it and read selected extracted passages at the three named
items, plus current primary HTML https://arxiv.org/html/1701.01425v2 .
This is not a fresh whole-paper read.

Frozen campaign inputs, freshly read WHOLE at their unchanged hashes:

- xmodel/danielewski-two-chart-interface-root-20260911.md:
  9107e171cb1db948eabae96cad8961fbc3c1ceb6b8d8ddbe442c2381caed0033.
- xmodel/danielewski-newton-descent-reduction-root-20260911.md:
  c21beaa3693349cd2153f7ba0e6244c397d1bf3bade36807b7a0c09a0d256605.

Targeted history searches covered the canonical avenue/progress/audit/reduction
files and Markdown reports for invariantization, Chebyshev, two-chart and
quotient/support synonyms. Selected August31 one-cusp source sections already
record the pseudo-plane selfmap and failed functorial Picard/ML arguments.
Current external author notes at
https://raw.githubusercontent.com/nasqret/jacobian-counterexample/main/knowledge/plane-program.md
were read through their144 lines: the surface, rational pair and full
Chebyshev-family boundary failure are already recorded there. That mutable
web read is exploratory history, not a frozen mathematical input. No complete
repository-wide novelty audit is claimed.

Composition pass: the invariant-S target and unrestricted-T target are
different spaces of functions, but have equivalent NONEMPTINESS even for
prescribed Laurent supports. Hence do not run two separate existence programs
merely because one asks for invariance. Use whichever presentation helps the
next exact argument; the two-chart full-bracket acceptance test remains in
force. The prior report's broader function-space statement is literally true
but no longer motivates a separate existence allocation. Target-automorphism
orbit identification is neither needed nor justified.

Lifecycle decision: freeze this scoped equivalence for one high-value
different-model hostile gate before promotion or dependent research. No
expensive commitment, new scientific descendant or global ranking reversal.
The separate Astra primitive-boundary task retains its original clock and
is not a premise of this report. A missing-primitive-line obstruction for
arbitrary etale selfmaps would still need a new argument; the known doubled
line example is not such an obstruction.

## COLLISIONS and resources

KNOWN maps and surface problem; candidate new campaign attachment only.
No new canonical OPEN identifier. No CAS, scientific subprocess, coefficient
bound, worker or protected-project inspection. Documentary reads, hashes and
publication transaction only. The task reduces duplicated representations;
it does not resolve JC2. FULL/BROAD clocks are not reset by this micro-round.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11733`.
- Body SHA-256:
  `a65049996e3bf34ebd9f4ab0ecc07b43bf3af384819cf613942460cf1f676612`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
