# Exact quotient–remainder producer for the full rational certificate

2026-09-09/10. MANUAL ALGORITHM/PROOF DESIGN; producer-only, not reviewed,
implemented or executed. First action23:52:04UTC; controlling original
stop00:12:00UTC, final3-minute reserve00:09. Both targets were absent.

## 1. Outcome and the unchanged endpoint

The coordinator's quotient–remainder sketch admits a complete, finite exact
algorithm under accepted17m's hypotheses. It retains every coefficient-algebra
component, requires no irreducible factorization, and never treats a product
algebra or a polynomial remainder algebra as a field. The only potentially
nontrivial rational linear system has at most35 rows and280 columns. A
successful result reconstructs exactly one of the OLD certificate forms:

1. UNIT: nine multipliers of degree at most25, padded to the original1638
   rational entries and satisfying all217 coordinates of sum h_i f_i=q^5;
2. SEPARATOR:217 rational entries annihilating ALL1638 old columns and
   assigning value1 to q^5.

This is an algebraic size bound, not a measured cost or a diagnosis of the
closed CPU-capped attempt. No matrix, coefficient, gcd, factor, certificate
or point was computed. No code or execution is authorized. The small system
does NOT replace the old full checker. Its target-specific equivalence must
not be advertised as row equivalence for arbitrary217-dimensional targets.

History: the multiplier argument is KNOWN accepted17m section3; the
coordinator proposed this algorithmic use at2320 cross. The present contribution
is its explicit finite splitting, maps, exceptional cases and full-certificate
read-back. No literature novelty is claimed and no corpus was searched.

Let P be the monic rational normalization of the literal accepted p, and
B=Q[v]/P, finite etale of rank7. Do not replace P by a selected irreducible
factor. All nine indexed f_i and q lie in B[T], degree at most5, with zeros,
duplicates and componentwise drops allowed. Set b=q^5 and V=B[T]_(degree<=30).
The fixed coordinate order is (k,l),0<=k<=30,0<=l<=6. Original columns are
v^l T^j f_i for1<=i<=9,0<=j<=25,0<=l<=6. Accepted17m already proves that
the guarded quotient is zero exactly when b is in the column space; otherwise
a rational separator exists. We consume that theorem, including reducedness
and its degree bounds, rather than reproving saturation or source attachment.

## 2. Exact splitting, inverse tests and termination

Maintain a finite partition P=product P_a into pairwise coprime monic
rational polynomials. Initially the partition has only P. Each leaf carries
A_a=Q[v]/P_a, the projection pi_a:B->A_a, and its idempotent embedding into
B, all as exact rational polynomial maps. Let e_a=deg P_a. A leaf need not
be a field. Every P_a stays squarefree because it divides squarefree P.

At a node, reduce every coefficient of all nine f_i modulo P_a. If all are
zero, mark the node ALL-ZERO. Otherwise select the largest T-degree d among
these reduced polynomials and the smallest input index i_a attaining d.
Let c_a be that polynomial's coefficient of T^d, represented by its unique
polynomial of v-degree<e_a. This representative is nonzero. Compute in Q[v]
the monic g=gcd(P_a,c_a), with a literal Bezout identity when needed.

If g=1, an identity u*c_a+w*P_a=1 proves the inverse c_a^-1=u mod P_a;
mark the node REGULAR with this chosen raw generator and its degree. If
0<deg g<deg P_a, put h=P_a/g. Squarefreeness gives gcd(g,h)=1.
Conversely, c_a invertible modulo P_a would give an identity forcing every
common divisor of c_a and P_a to divide1, so this is an exact unit test.
Find U*g+W*h=1 over Q[v], retain BOTH children g and h, and process each
afresh. The possibility g=P_a would contradict the nonzero reduced c_a;
it is an inconsistent-state refusal, not a branch to discard.

The binary CRT is literal:

    A_a -> Q[v]/g x Q[v]/h,       x -> (x mod g,x mod h),
    (x_g,x_h) -> (W*h)*x_g + (U*g)*x_h mod P_a.

Thus W*h is1 modulo g and0 modulo h, and U*g is the converse. The two
idempotents sum to1, are orthogonal and square to themselves. Composing
these maps through the tree retains the embedding of every final leaf.
Equivalently, with Q_a=P/P_a and J_a*Q_a=1 mod P_a, the final idempotent
is E_a=J_a*Q_a mod P. The embeddings send x to E_a times any rational
polynomial lift of x; different lifts give the same B element. Hence

    x=sum_a E_a*pi_a(x),   sum_a E_a=1,   E_a E_b=0 (a!=b).

Each individual embedding lands in E_a*B and sends1 to E_a, not to1_B;
the complete product recombination is unital. No individual leaf is
substituted for the whole coefficient algebra.

These identities, including the rational Bezout witnesses, are the precise
projection/recombination contract for any future implementation.

Every genuine split replaces one positive integer degree by two smaller
positive degrees with the same sum. Total leaf degree stays7, so there are
at most7 leaves and6 splits, hence at most13 node visits. A node scans a
fixed finite coefficient list, uses at most one such leading-coefficient
gcd, then terminates or splits. Rational Euclidean gcd terminates because
nonzero remainder degree strictly decreases; its scalar divisions are only
by nonzero rationals. This proves mathematical termination, without a
bit-height or time bound. No polynomial gcd in A_a or in a later remainder
algebra, generic coefficient inverse, root selection or complete field
factorization is required.

Choosing the largest degree ensures that, on each REGULAR leaf, every f_i
has degree at most d and the selected generator has the same degree d on
every underlying field factor: its leading coefficient is a unit. Degree
drops on the other leaf after a split are recomputed, not ignored. The
algorithm uses this one selection rule; no alternative pivot farm is proposed.

## 3. Exceptional leaves, including the localized affine line

Complete the partition before combining decisions; every leaf/map remains
in the record. On a REGULAR leaf with d=0 the selected raw f_(i_a)=c_a is
a unit constant. Put h_(i_a)=c_a^-1*b_a and all other h_i=0. Their degrees
are at most25. This is an immediate component UNIT witness even if q_a=0.

On an ALL-ZERO leaf the ideal is0. If q_a=0, b_a=0 and all multipliers0
give the required witness; localization at zero is the zero ring. If q_a
is nonzero, b_a=q_a^5 is nonzero because A_a[T] is reduced: its coefficient
algebra is a product of characteristic-zero fields. No assumption that
q_a is a unit on every factor is needed. Choose a nonzero rational coordinate
beta of b_a in the basis v^l T^k (l<e_a,k<=25), and let chi be extraction
of that coordinate divided by beta. Then chi(b_a)=1. Composing chi with
coefficientwise pi_a:V->A_a[T]_(degree<=30) gives a rational separator of
the OLD columns, since every f_i projects to0. Every other leaf receives
zero functional. This is a full global NONZERO certificate, not a statement
that the other leaves are proper, or that this surviving localized affine
line is finite-dimensional. No evaluation or explicit point is required.

One such leaf is sufficient for a global separator; a future implementation
may omit the remaining local DECISIONS after its full certificate verifies,
but must retain the partition, all source inputs and the zero extension.
It may not relabel unexamined local decisions UNIT. If no such leaf exists,
the constant and ALL-ZERO leaves are already settled positively; proceed
with all REGULAR positive-degree leaves together. If none remain, their
empty small system is consistent and the exceptional witnesses glue to UNIT.

## 4. Remainder algebras and the at-most35 by280 system

For a REGULAR leaf with1<=d_a<=5, write raw f_(i_a)=c_a*fhat_a with
fhat_a monic of degree d_a, and set C_a=A_a[T]/(fhat_a). Over ANY commutative
coefficient ring, division by a monic polynomial produces a unique remainder
of degree<d_a: cancel the highest T-term using coefficient1; uniqueness
follows because a nonzero multiple fhat_a*Q has degree d_a+deg Q. This
last assertion holds despite zero divisors, since its leading coefficient
is exactly the nonzero leading coefficient of Q.

Consequently C_a is finite free over A_a with basis1,T,...,T^(d_a-1), and
over Q with basis v^l T^j,0<=l<e_a,0<=j<d_a. C_a MAY BE NONREDUCED. No
separability, reducedness, root enumeration or inverses inside C_a are used.
Let R_a denote this exact monic remainder map. In C_a form all columns

    R_a(v^l T^j pi_a(f_i)),
    i in the original nine indices except i_a, j<d_a, l<e_a,

including zero/duplicate columns, and target R_a(b_a). This is an
e_a*d_a by8*e_a*d_a rational system. Its column span W_a equals the ideal
generated by the eight remaining remainders: every multiplier in C_a has
a unique expansion in the displayed Q-basis. This uses multiplication in
the possibly nonreduced C_a, not a field-span approximation.

Take the direct sum of these systems, with leaf coordinates and original
generator labels explicit. Put r=sum e_a*d_a over positive-degree leaves.
Since sum_all_leaves e_a=7 and d_a<=5, r<=35 and the number of columns is
8r<=280. The target has r<=35 rational entries. The matrix bound does not
count its target vector or proof-tracking storage, and says nothing about
actual rank or nonzero counts. The all-zero-leaf coordinate functional
is a separate direct branch, not an
extra280-column matrix; degree-zero witnesses likewise need no matrix.

Finite exact Gaussian elimination over Q decides whether the combined
target belongs to W=direct_sum W_a. In the consistent case retain a rational
solution. Otherwise retain a rational functional mu vanishing on W and
having value1 on the combined target: extend a basis of W by that target
and use its coordinate functional. This existence/construction needs only
nonzero rational pivot division. No number-field component is chosen. A
resource-bounded future implementation may stop INCONCLUSIVE; mathematical
termination does not promise completion under any particular cap.

## 5. UNIT read-back: raw generator, quotient and all old slots

On each positive-degree leaf, the small rational solution reconstructs
polynomials h_i in A_a[T] of degree<d_a for i!=i_a. Set

    N_a=b_a-sum_(i!=i_a) h_i*pi_a(f_i),
    Qdiv_a=N_a/fhat_a,    h_(i_a)=c_a^-1*Qdiv_a.          (1)

Here Qdiv_a is a quotient polynomial, distinct from the CRT complementary
factor Q_a=P/P_a. Small consistency says R_a(N_a)=0, so monic division is
exact. Formula(1) multiplies
the RAW f_(i_a), not its normalized replacement. Omitting c_a^-1 is wrong.
The label h_(i_a) is a generator cofactor, not the source guard factor h0.

Degree control is literal: deg b_a<=25 and deg(h_i*pi_a(f_i))<=2d_a-1<=9,
so deg N_a<=25. Therefore deg Qdiv_a<=25-d_a when nonzero, and the same bound
holds for h_(i_a); zero/cancellation cases only lower degrees. The other
cofactors have degree at most d_a-1<=4. The exceptional witnesses in section3
also have degree<=25. Thus for every original input index define

    h_i(T)=sum_a E_a*lift(h_(i,a)(T)) in B[T].            (2)

The CRT operation has no T-degree increase. Componentwise identities and
sum E_a=1 give sum_i h_i f_i=b in B[T]. Reduce every coefficient to the
original basis1,v,...,v^6 and pad ALL nine cofactor polynomials through T^25.
This is the old1638-entry rational vector, with no generator removed or
reordered: the coefficient of v^l T^j in h_i occupies zero-based wire
index ((i-1)*26+j)*7+l. Its products have degree<=30, so the original full217-coordinate
checker tests exactly the global identity, including every high zero row.

Conversely, any original identity projects to every leaf and then modulo
fhat_a. Reduce its other multipliers modulo fhat_a; their degree<d_a
representatives supply a small solution. Thus the small positive-degree
tests together with the exceptional decisions are complete for THIS b=q^5.
There is no hidden reverse source map or finite-point assumption.

## 6. SEPARATOR pullback, including every long old column

Define rho:V->C=direct_sum C_a by coefficient projection followed by R_a
on each positive-degree leaf. It is Q-linear, and its component maps are
ring homomorphisms on all B[T] before restricting to V. A small inconsistent
system supplies mu:C->Q with mu(W)=0 and mu(rho(b))=1. Put

    lambda_(k,l)=mu(rho(v^l T^k)),  k=0..30,l=0..6.     (3)

Then lambda is exactly a217-entry rational functional on V and lambda(b)=1.
The zero-based wire index of lambda_(k,l) is7*k+l.
To check every old column, fix ANY original i,j,l with j<=25. On a leaf
where i=i_a its image is0. Otherwise pi_a(v^l)*R_a(T^j) is an element of
C_a, hence a rational linear combination of its basis v^u T^t,t<d_a.
Multiplying by R_a(pi_a(f_i)) expresses that column image as a combination
of the SMALL columns. This holds for j>=d_a as well as smaller j, and for
each leaf even when the pivot indices differ. Therefore rho(M-column)
lies in W, so lambda annihilates ALL1638 old columns, not just280short ones.

For completeness, W is exactly rho(im M): each leaf-supported small column
lifts as E_a*lift(v^l)*T^j*f_i, which lies in im M since j<=d_a-1<=4<=25 and
its B coefficient expands in the original seven-element basis. The other
leaves see0. This identity does NOT assert ker rho subset im M. Formula(1),
and the bound deg b<=25, are what make small consistency imply an old UNIT
certificate; no claim of equivalence for arbitrary V-targets is needed.

For an ALL-ZERO leaf with q_a!=0 use section3's chi*pi_a instead of(3),
still outputting all217 coordinates and zero-extending over other leaves.
Both kinds of negative certificate are checked by the SAME old full
checker: every1638column pairing is0, and the full target pairing is1.
Nothing in the small producer, a rank flag, a selected branch label, or a
modular calculation replaces that check. Accepted17m then gives the
generic nonzero guarded quotient; a separator is not a character or point.

## 7. Manual changed-object controls

RAW NORMALIZATION. Over Q take f1=2T, other f_i=0, q=T. Division by the
monic pivot T gives Q=T^4, but the raw cofactor is T^4/2. Forgetting c^-1
produces2T^5 rather than q^5=T^5. The unchanged full checker detects it.

LOST COMPONENT. Over Q x Q, f1=(1,T), all other f_i=0, q=(0,1). The
first leaf has a constant unit generator and zero target; the second has
remainder algebra Q and target1 with zero small columns. Its constant
functional, projected from the second component only, is a global separator.
Keeping only the first component or globally inverting an idempotent is false.

NONREDUCED C IS REAL. Over Q choose pivot f1=T^2, f2=1+T, other f_i=0,
q=1. In C=Q[T]/T^2 the correct short multiplier is h2=1-T and N=T^2,
giving h1=1. Replacing C by its reduced quotient suggests h2=1 and N=-T,
which is NOT divisible by T^2. It breaks exact read-back even though a true
UNIT certificate exists. Monic division, not radicalization, is required.

ALL-ZERO GUARD BRANCH. All f_i=0 over Q: q=0 gives the zero UNIT vector;
q=1 gives the constant-coordinate separator. For a nonconstant nonzero q,
q^5 likewise has a nonzero coefficient and gives the direct functional,
while the surviving localization can still be an affine line with points
removed. No finite quotient algebra is invented for this branch.

TARGET-DEPENDENT COMPRESSION. With f1=T, others0 over Q, rho annihilates
T^30, but im M from degree<=25multipliers only contains multiples of T of
degree<=26. Thus the arbitrary target T^30 has consistent zero remainder
without an old-window solution. It is outside the permitted deg b<=25;
this witnesses why the target-specific degree proof cannot be omitted.
For the actual target, formula(3) nevertheless covers every old column up
through the T^30 coordinate, and the old checker must keep all those rows.

COEFFICIENT REDUCEDNESS. Accepted17m's B'=Q[e]/e^7, all f_i=0,q=e has
zero localization but nonzero q^5. The present algorithm must refuse such
a replacement of B: gcd-splitting need not be coprime and its negative
certificate would lack17m's interpretation. Nonreduced C_a is permitted;
nonreduced COEFFICIENT B is not part of this contract.

## 8. Binding, limits and completion

Future implementation must bind the literal full p wire, derive its monic
P only by the known nonzero rational leading coefficient, and preserve the
original modulus wire for the unchanged checker. It must bind nine indexed
rows, q and both degree envelopes to the same accepted artifact; every split
factor/Bezout identity, projection/idempotent, leaf pivot/raw leading unit,
monic modulus, component basis and short solution/functional must remain
auditable. Exact equality of the reconstructed OLD certificate against the
original rows is the final acceptance boundary. Intermediate arithmetic
failure or a resource cap gives INCONCLUSIVE, not NONZERO. No change to the
accepted parser, authority, supervision or checker is specified or needed
by this mathematical design; a new candidate producer and its binding would
still need separate code preparation/review/registration.

The final rational certificate uses the existing canonical rational-string
wire and input/acceptance bindings, not a new component-selected input. No
floating coefficients or unaudited precomputed matrix replace that framing.

Only the dimension bound and mathematical finite termination are proved.
Split costs, coefficient heights, matrix density, native API behavior,
construction/RREF phase costs and runtime improvements remain unmeasured.
The closed217attempt supplies no phase diagnosis. This task cannot select
new caps, workers, alternate engines, a retry, source-point reconstruction
or a source/global conclusion. Every B component stays in the equivalence;
one correct separator needs only one surviving component but proves no
classification of all the others. The accepted properness/existential-point
interface remains17m's generic scope, not a new source composition here.

Exactly NEXT-DESIGN-PINS.json and its9listed objects were pinned before
WHOLE reads. READ-SCOPE.md records all boundaries; no linked provenance or
actual coefficient file was accessed. All reasoning is manual. No code,
mathematical subprocess, web/AWS/SSH/proc/agents or shared/protected writes.
Only own apply_patch text and documentary metadata/publication were used.

## OPEN(S) RAISED

No new canonical OPEN ID and no missing mathematical map under the stated
hypotheses. The unimplemented quantity is one faithful producer emitting an
OLD full certificate; cheapest next step is FIRST independent review of this
manual design, not execution. Runtime cost is unknown and not estimated.
Implementation, binding and any later experiment require separate authority.

## COLLISIONS

EMPTY — own targets absent before begin; no corpus scan or novelty claim.
Own WHOLE/raised-OPEN/collision checks precede the unique completion marker.
All writers become IDLE after terminal custody handoff before the original cap.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19000`.
- Body SHA-256:
  `c6694cec0c950d1d0c6f9244f0c1a052fc14eccc363766dcc55966e1689820a8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
