# Full-Weyl Kummer control for Euler-localized line selection

Author: Astra geometry. MANUAL / UNREVIEWED, not promotion.
First action 2026-09-12 02:00:03 UTC; original reserve02:18/HARD02:21
unchanged. Sole TASK SHA c3a7b2bda57e8d47f544c81179e0a3aa152353c6f63854a59ed3d5f1ae81f4d7
matched before FRESH_WHOLE. No other scientific input.

## Weyl module, simplicity and Euler localization

Verdict: the proposed example works. Its Euler localization has dimension2
and no delta-stable line, despite full Weyl action, algebraic finite
monodromy, regular holonomicity and zero algebraic de Rham cohomology.
It supplies no realization as an actual Keller source quotient. Standard regular-singular
D-module terminology is separated below from the elementary arguments
establishing the obstruction.

Write G=(p-1)(p-2),
M1=C[p,G^-1]e with dp(he)=(h'+G'h/(2G))e, and
M2=C[q,(q-1)^-1]f with dq(hf)=(h'+h/(2(q-1)))f.
Multiplication and these derivatives satisfy the Weyl commutators;
the two factors commute on M=M1 tensor_C M2. They realize the algebraic
branches e²=G and f²=q-1. Their local monodromies are signs; the product
connection likewise has finite monodromy. Its rational connection has
only regular singularities, including infinity.

Here is a direct simplicity argument, also proving cyclic generation.
For a nonzero Weyl submodule T of M1, clearing the denominator of one
section shows that I={g in C[p]:ge in T} is a nonzero polynomial ideal.
Choose its generator g. Since G dp preserves polynomial sections,
g divides Gg'+G'g/2, hence g divides Gg'. Every root of g must lie at1
or2. If g has positive multiplicity m at a in {1,2}, multiply dp(ge)
by p-b, where b is the other point. This is a polynomial section in T
whose multiplicity at a is m-1: its leading factor is m+1/2, not zero.
This contradicts divisibility by g. Thus e belongs to T.

From dp e=(1/[2(p-1)]+1/[2(p-2)])e, multiplication by p-1 or p-2
produces both simple principal parts. Differentiating (p-a)^-n e gives
coefficient -n+1/2 on the next principal part at a; the remaining mixed
fraction decomposes into parts of order at most n at a and1 at b.
Induction generates all principal parts and hence all M1. Thus T=M1.
The identical one-point argument proves simplicity and cyclicity of M2.
These simple extensions of the stated connections are their middle
extensions. Standard facts that regular-singular middle extensions are
regular holonomic, and exterior products preserve regular holonomicity,
supply that terminology for M; they are not needed for rank or no-line.
Factor holonomicity also follows directly from cyclicity and the nonzero
first-order polynomial annihilators.

Set z=ep, w=eq. No nonzero M1 section is C[z]-torsion: at p=1 it has
leading exponent lambda=m+1/2 for an integer m. For a polynomial P(z)
of degree n, its leading local term has coefficient P_n times
1^n lambda(lambda-1)...(lambda-n+1), which is nonzero. Lower powers
cannot cancel that most singular term. The same proof at q=1 applies
to M2 over C[w]. Both inject into their respective Euler localizations.
Tensoring these injections over C embeds M into a direct sum of copies
of C(z) tensor_C C(w), a localization of the domain C[z,w]. Therefore
M is B=C[z,w]-torsion-free, not merely torsion-free separately in z,w.

## Rank, absence of a line and acyclicity

Put V1=C(z) tensor_C[z] M1. The commutators extend multiplication by p
and dp to this localization, with scalar shifts z->z-1 and z->z+1.
Here p is invertible: dp*z^-1 is its two-sided inverse, using
p dp=z and dp p=z+1. All inversions here are Euler polynomials, not
extra source-coordinate divisors.

The connection equation 2G dp e=G'e, multiplied by p and reordered, is

    [2(z-3)p²-3(2z-3)p+4z]e=0.

To prove independence, suppose P(z)e+Q(z)pe=0 after clearing Euler
denominators. At either branch alpha=1,2, let n be the maximum degree
of P,Q. Its most singular coefficient is a nonzero multiple of
P_n+alpha*Q_n, since the exponent1/2 has no zero falling factorial.
Both values must vanish, forcing P_n=Q_n=0, a contradiction. Thus
(e,pe) is independent. On its span, multiplication by p has shift z->z-1
and matrix

    A(z) = [[0, -2z/(z-3)],
            [1, 3(2z-3)/(2(z-3))]].

Its determinant2z/(z-3) is nonzero. Hence this span is stable under
p and p^-1, and under dp=p^-1 z. Cyclicity of M1 proves it is all V1.
Thus dim_C(z) V1=2, including independence and spanning.

For V2=C(w) tensor_C[w] M2, direct calculation gives
dq f=(w-1/2)f and qf=w/(w-3/2)f. The span C(w)f is therefore stable
under q,dq and contains the cyclic generator. Torsion-freeness makes its
dimension exactly1. Tensoring these bases and then passing to
E=C(z,w) proves dim_E V=2 for V=E tensor_B M.

On the displayed tensor basis, delta=p dq acts by (w-1/2)A(z) with
shift sigma(z,w)=(z-1,w+1). It is invertible and fixes t=z+w. Suppose
it preserved an E-line. Removing the nonzero scalar w-1/2 gives an
A(z)-stable semilinear line over C(t)(z). Choose a rational vector v(z,t)
and a nonzero rational multiplier lambda satisfying
A(z)v(z-1,t)=lambda(z,t)v(z,t). Outside finitely many complex values of t,
specialization retains all denominators, v and lambda as nonzero rational
functions of z. It gives a p-stable line L over C(z) in V1.

The nonzero scalar action on L is bijective, so L is also p^-1-stable
and dp=p^-1 z-stable. Clearing Euler denominators shows L intersect M1
is nonzero; it is a Weyl submodule. Simplicity would make it all M1,
whose Euler localization has dimension2, contradicting dim L=1.
Therefore there is NO delta-stable E-line. The specialization and
intersection steps use neither a source field nor an assumed rank theorem.

For H(z,w) nonzero, a nonzero kernel vector of z-r+delta H would yield
delta m=-(z-r)/sigma(H)*m in V, hence a forbidden line. For H=0,
B-torsion-freeness already excludes a kernel. Thus every operator in the
specified family (r>=0) is injective on M.

Finally let v_k=(q-1)^k f, k in Z. These form a C-basis of M2 and
dq v_k=(k+1/2)v_(k-1). Thus dq is bijective. Its inverse contracts the
two-term algebraic de Rham complex of M2. The de Rham complex of M is
the tensor product of the two factor complexes over C, so that contraction
(with the usual degree sign) contracts it too. ALL its algebraic de Rham
cohomology groups vanish; no finiteness or spectral-sequence assumption
is needed for this explicit contraction.

## Source mismatch, control and scope

For an actual polynomial Keller pair p,q, each polynomial p-1,p-2,q-1
is nonconstant and hence a nonunit of C[x,y], so its zero locus is nonempty.
Etaleness makes the inverse image of each smooth target line reduced.
No two have a common divisorial component: p-1 and p-2 are comaximal,
and a common component with q-1 would map to a point, contradicting
quasi-finiteness of an etale map. Their product is thus nonconstant and
squarefree in the UFD C[x,y]. It cannot have a polynomial square root.
Indeed its odd prime valuations also rule out a rational square root.

Accordingly the literal algebraic radical e*f used to construct this
module cannot be a polynomial source section with that square relation.
This does NOT identify module vectors with elements of
N=C[x,y]/C[p,q], nor exclude arbitrary irreducible monodromy constituents
or abstract differential-module subquotients in such an N. The control
shows that full Weyl action, finite algebraic monodromy, finite Mellin
rank and de Rham acyclicity ALONE do not force a delta-line. A genuine
polynomial-source selection theorem would need additional input.

Changed-object control: replace M1 by C[p,(p-1)^-1]sqrt(p-1).
The one-point calculation gives Mellin rank1, with p acting on its basis
by z/(z-3/2) and shift z->z-1. The tensor product then has rank1 and
its whole Euler localization is a delta-stable line, with multiplier
(w-1/2)z/(z-3/2). The other structural properties and acyclicity remain;
the two distinct nonzero branch points in the independence argument are
what make the original rank2/no-line example different.

QUANTITY: B-torsion-freeness, dim_E V=2, and absence of a delta-line,
all established above. CHEAPEST TEST: the direct local-exponent,
cyclicity and rational-line audit; manual planning15 minutes,
computational/numerical wall UNMEASURED. OPEN: none in these explicit
deductions, subject to independent review and the labeled standard
regular-holonomic facts. No actual-Keller, annihilator-exhaustion,
novelty or JC2 theorem is claimed.

Own-scope/collision check: exact report, manifest, PINS and custody were
absent at first action. Only the designated leased report and own
PINS/custody are authored. TASK and every existing file remain untouched.
Final WHOLE readbacks, postpins, marker-last publication and exact expected
verification are recorded in custody. No scientific process, external
input, peer, worker, protected tree, shared edit, canonical OPEN or
automatic descendant is used or created.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8959`.
- Body SHA-256:
  `eaa63ea184b52e06d00eb6bdeea5ee7ccf29354a915b8152169c443ed750ca69`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
