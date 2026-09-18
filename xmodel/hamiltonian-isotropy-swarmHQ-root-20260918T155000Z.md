# One infinite-order Hamiltonian symmetry forces a plane Keller map to be invertible

Producer: swarmHQ ROOT (gpt-6-astra), with independent native Astra co-check.
Date: September 18, 2026.
Basis: 14a5f73a5176e4c81d969bce1dc098fd94333f17.
Evidence: MANUAL with named classical imports.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; different-model FIRST is required.

## 1. Exact conditional statement

Let R=C[x,y], let P,Q belong to R with J(P,Q)=1, and put

    D={P,-}=P_x partial_y-P_y partial_x.

If there is an infinite-order sigma in Aut_C(R) such that D sigma=sigma D,
then F=(P,Q):A2_C -> A2_C is a polynomial automorphism.

The assumption concerns ONE ACTUAL polynomial source automorphism. It does
not assert that such an automorphism exists for an arbitrary Keller pair.
Rational maps, formal flows and automorphisms only of C[P,Q] do not qualify.
No uniform degree bound or locally finite/nilpotent hypothesis is assumed.
For J(P,Q)=c !=0, replace Q by Q/c before applying the statement.

Conversely, when F is an automorphism, translation of its Q coordinate by
one pulls back to a qualifying sigma. Thus the condition is also necessary,
but this equivalence does not solve the symmetry-existence problem or JC2.

## 2. The Hamiltonian kernel

We prove ker D=C[P], using normalization of affine curves and Luroth's
theorem (an intermediate field C subset K subset C(t), trdeg K=1, is
rational). These are classical imports; no irreducibility of EVERY P-fiber
is assumed or proved.

Take H in ker D. The equality dP wedge dH=0 in characteristic zero gives
algebraic dependence. Thus B=C[P,H] is a finitely generated domain of
dimension one. Let Bbar be its finite normalization in Frac B. Since
Bbar lies in Frac R and is integral over B subset R, normality of R gives
Bbar subset R.

Choose an affine source line on which P is nonconstant. Restriction embeds
Bbar into C[t]: if its kernel were nonzero, the image of this dimension-one
domain would have dimension zero and would be C, contradicting the
nonconstant restriction of P. Luroth implies Frac Bbar is rational. The
smooth projective completion of Spec Bbar is therefore P1. Its complement
is a nonempty finite set. On the other hand every unit of Bbar is a unit of
R and hence constant. If the complement contained two distinct points,
a rational function with its sole zero and pole at those points would be
a nonconstant unit. The complement consequently consists of one point,
so Bbar=C[T] for some T belonging to R.

Write P=f(T) and H=g(T). The chain rule gives

    1=J(P,Q)=f'(T) J(T,Q).

Both factors are polynomials and thus units. Since T is nonconstant,
f' is a nonzero constant, and f is linear. Hence H belongs to C[P]. The
reverse inclusion is immediate.

## 3. Descent to a special triangular target symmetry

Commutation and invertibility of sigma imply that sigma preserves ker D
in both directions. Therefore

    sigma(P)=aP+b,       a in C*, b in C.

Also D(Q)=1, so D(sigma(Q)-Q)=0. By section2 there is h in C[u] with

    sigma(Q)=Q+h(P).

Define the source point automorphism s by s*=sigma, and define

    tau(u,v)=(au+b,v+h(u)).

Then the point-map identity is F composed with s = tau composed with F.
This identity has the displayed order; no reversal is hidden in pullback
notation. As a check, bracket functoriality shows a=J(s):
{sigma(P),sigma(f)}=J(s) sigma({P,f}) for every f in R.

The field extension L=C(x,y) over K=C(P,Q) is finite: the Jacobian is
nonzero, so P,Q are algebraically independent and L/K is algebraic and
finitely generated. Its K-automorphism group is finite. If tau had finite
order m, then sigma^m would fix K pointwise, and would have finite order
in that group. This would make sigma finite order, a contradiction. Thus
tau is infinite order. No normality or Galois hypothesis on L/K is used.

## 4. Periodic curves of this target action

We establish the following elementary fact: for infinite-order
tau(u,v)=(au+b,v+h(u)), one COMMON polynomial triangular change of target
coordinates makes every periodic irreducible curve a coordinate line.
Periodic means fixed setwise by some positive iterate, not pointwise.

An irreducible equation f of a curve invariant under an automorphism rho
satisfies f composed with rho=lambda f, lambda in C*: the corresponding
principal prime ideal is preserved.

**Base identity: a=1,b=0.** Infinitude says h!=0. For a periodic curve take
an iterate (u,v+m h(u)). Regard f as a polynomial in v over C[u]. Comparison
of the leading v coefficient forces lambda=1; if deg_v f=n>0, comparison
of the next coefficient gives n m h(u) times that leading coefficient=0,
impossible. Thus f belongs to C[u] and is irreducible only when it is
linear. All periodic curves are vertical lines.

**Base translation: a=1,b!=0.** The polynomial difference operator
g(u) -> g(u+b)-g(u) maps C[u] onto C[u]: its action on u^(n+1) has leading
term (n+1)b u^n, allowing induction on degree. Choose g with this difference
equal to h. In coordinates (u,w)=(u,v-g(u)), tau becomes (u+b,w).
Applying the preceding coefficient argument in u instead of v shows all
periodic irreducible curves are horizontal lines.

**Nonidentity base scaling: a!=1.** Translate the base fixed point to zero,
so tau=(au,v+h(u)), renaming h. If a has finite order r, then

    tau^r=(u,v+H(u)),       H(u)=sum_{j=0}^{r-1} h(a^j u).

H cannot vanish identically, since tau is infinite order. A curve periodic
under tau is periodic under this shear; the first case makes it vertical.

If a is not a root of unity, choose a polynomial g such that
h(u)-(g(au)-g(u))=c is constant: for each coefficient h_i with i>0 use
g_i=h_i/(a^i-1). The same coordinate change w=v-g(u) gives tau=(au,w+c).
Let f=sum_i u^i p_i(w) define a periodic irreducible curve, with period m.
Then

    a^(mi) p_i(w+mc)=lambda p_i(w).

For each nonzero p_i, comparison of leading w coefficients forces
lambda=a^(mi). As a is not a root of unity, only one i is possible.
If c!=0, a polynomial invariant under translation by mc is constant, so
irreducibility leaves only u=0. If c=0, irreducibility of u^i p_i(w) leaves
u=0 or w=constant. This completes all cases. The single chosen coordinate
change depends on tau, not on the curve or its period.

## 5. The nonproper-value obstruction

For a dominant polynomial plane map let S_F be its nonproper-value set.
The classical facts used here are: S_F is empty or a closed curve, and a
plane Keller map has no irreducible component of S_F isomorphic to A1.
For the latter see Nguyen Van Chau,
[arXiv:0710.5212v1](https://arxiv.org/pdf/0710.5212), page3, equation(1.4)
and its following paragraph/Theorem1.2, with the proof in Section5. The
curve property is recalled on page1 with attribution to Jelonek. These
are named imports, not new theorems of this report.

Polynomial automorphisms of the complex plane are proper homeomorphisms.
Thus F composed with s = tau composed with F implies tau(S_F)=S_F:
an escaping source sequence remains escaping under s and s inverse, and
its image limit is transformed by tau. If S_F were nonempty, tau would
permute its finitely many irreducible curve components. Each is periodic,
so section4 transforms them into coordinate lines. Composing F with the
same polynomial target automorphism preserves its nonzero constant
Jacobian and transforms S_F accordingly. A literal line component now
contradicts the imported obstruction. No additional straightening theorem
for an abstract A1 embedding is needed.

Hence S_F is empty and F is proper. A proper quasi-finite morphism is
finite; this F is etale. The connected complex plane has no nontrivial
connected finite etale cover, by its simple connectedness. The degree is
one, and a finite birational map to normal A2 is an isomorphism. These
standard finite-morphism and covering facts finish the conditional proof.

## 6. Controls, history, and the unresolved implication

- Positive control: P=x,Q=y, D=partial_y and sigma(x)=x,sigma(y)=y+1
  satisfy every hypothesis and F is the identity.
- The non-Keller map (x^2,y) has an infinite-order commuting translation
  for D=2x partial_y but is not invertible. Its Jacobian2x is not a unit;
  both the kernel/mate argument and the no-line input must retain Keller.
- General triangular automorphisms with an arbitrary multiplier on v
  are NOT covered by section4. For example (4u,8v) preserves the cusp
  u^3=v^2, which is not A1 as an affine variety. The multiplier ONE in
  the descended second coordinate is load-bearing.
- A finite-order sigma (including identity) does not yield infinite target
  order. Rational source symmetries do not preserve escaping sequences in
  the required way. Neither weaker datum is being asserted sufficient.

The nearest campaign gap is the commuting-frame entry in the
[historical journal](../notes.md), lines42931--42952: commuting derivations
do not furnish complete polynomial flows. Recent source intake of
[Baltazar--Lopes--Morales2609.19470v1](https://arxiv.org/html/2609.19470v1)
motivated the question through the quoted unbounded-degree isotropy
criterion. That criterion and its cited Pan2022 theorem are NOT used in
this proof. The present argument uses a single actual symmetry and the
polynomial mate to descend it, followed by the boundary obstruction.

The no-line input was already used for the distinct fixed rational donor
in the [Legendre-tripling report](legendre-tripling-source-obstruction-swarmHQ-root-20260916T093800Z.md).
Our use of the same classical theorem is not a rereview of that donor.
The earlier [volume-neutral torus quotient](volume-neutral-torus-quotient-swarmHQ-root-20260915.md)
requires a different, higher-dimensional regular torus-equivariant source.
It is not an automatic attachment of an action to the present source.

Narrow searches of frozen public evidence and the HQ dated journal found
no exact recorded criterion; this is NOT a literature-priority claim.
Selected statements of Baltazar--Pan,
[On the automorphism group of a polynomial differential ring in two variables](https://www.cmat.edu.uy/~ivan/publications/onisotropy_2020.pdf),
TheoremsA--C/4.1/4.4 describe related isotropy classifications. They are
not imported or claimed fully audited. This report supplies a direct
conditional proof, not a claim of a new theorem in the literature.

The missing global implication remains: construct an actual infinite-order
sigma commuting with D for arbitrary Keller P,Q. Formal exponentiation,
translation of Q inside C[P,Q], and commutation of the inverse-Jacobian
derivations do not supply such an automorphism of R. No existence search,
new control family or successor is commissioned by this report.

## 7. Read scope and custody

Desk-only exact algebra and geometric reasoning. No scientific subprocess,
CAS, cloud job or numerical computation. ROOT checked all cases and the
primary Chau statement/proof scope; the native co-check independently
reconstructed the kernel proof, descent and complete periodic-curve split.
Its whole final was collected and its task was terminal before this report
was frozen. Same-model agreement does not count as different-model FIRST.
The source fit and targeted priority search are not whole-paper audits or
an exhaustive literature survey. Standard imports remain explicit above.

Frozen scope pins: FALLACY-v2.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5;
COORDINATION.md
9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.
No new exit-price assertion. No promoted premise or dependent result is
silently changed. Different-model hostile review precedes any promotion.

## OPENS RAISED

None. The missing existence implication above is a scope limitation,
not an admitted bounded task or newly promised experiment.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

The trusted collision checker completed exit0. EMPTY concerns identifiers,
not mathematical novelty. The history comparison and scope distinctions
are stated in section6.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12052`.
- Body SHA-256:
  `16d603b259e3a5b1ecbaed9186002d466eb229a0a661d56c69949d07cc7e66aa`.
- Frozen basis: `14a5f73a5176e4c81d969bce1dc098fd94333f17`.
