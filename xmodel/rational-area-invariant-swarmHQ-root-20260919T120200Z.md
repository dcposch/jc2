# A rational area-preserving map with a rational invariant is birational

Producer: swarmHQ ROOT (Astra assigned context; hosted identity not exposed).
Date: September 19, 2026 UTC.
Frozen public basis: 2730e5d5f98b64bff4a51e460c3e91117efa60d9.
Evidence: MANUAL, with the classical function-field/curve correspondence,
characteristic-zero differential identities, and finite-map change of variables.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; same-model co-check is not FIRST.
No literature-novelty or JC2-resolution claim.

## 1. Statement and significance

Let H:A2_C --> A2_C be a dominant RATIONAL self-map. Suppose

    H*(dx wedge dy) = dx wedge dy

and there is a nonconstant r in C(x,y) with r composed H = r.
Then H has generic degree ONE, hence is birational.

The original rational pencil need not be geometrically connected and its
geometric generic components may have any genus. Polynomiality of H is
not assumed. If H is polynomial, its Jacobian is exactly1 and the inherited
birational Keller theorem makes it an automorphism.

This excludes degree-greater-than-one rational donors simultaneously
preserving the EXACT area form and a rational first integral. The theorem
does not produce a rational invariant for an arbitrary Keller map.
It is not a JC2 proof or a test for all rational donor constructions.

## 2. Compact-curve lemma

Let C be a smooth projective integral curve over an algebraically closed
field k of characteristic zero. Let f:C -> C be nonconstant of degree d,
and let eta be a nonzero rational differential satisfying f*eta=eta.
Then d=1.

Assume d>1. At a point p, characteristic-zero local uniformizers give

    ord_p(f*eta) = e_p * (ord_{f(p)}(eta)+1) - 1,

where e_p is the ramification index. In particular, p is a pole of f*eta
if and only if f(p) is a pole of eta. The finite pole set S thus satisfies
f^(-1)(S)=S.

If S is nonempty, f maps S onto S: every target point has a preimage,
and every preimage of a pole belongs to S. Consequently f|S is a
permutation. Each pole has exactly one geometric preimage under f,
so its ramification index is d. Fix a pole p and an iterate g=f^m
fixing it. The index at p is d^m. Writing a=ord_p(eta), invariance gives

    a = d^m*(a+1)-1.

Since d^m>1, a=-1. This is a simple pole with NONZERO residue. The local
residue pullback identity now gives

    res_p(eta) = res_p(g*eta) = d^m * res_p(eta),

impossible in characteristic zero. Thus an invariant eta cannot have poles
when d>1. No bound on genus or on the number of punctures was used.

If S is empty, eta is a nonzero regular differential. Descend the curve,
finite map, differential and their identities to a subfield k0 of k
finitely generated OVER Q, using their finitely many defining coefficients.
Choose models retaining smoothness, geometric integrality, properness,
map degree d and regularity/nonvanishing of eta; these properties descend
after including the finite defining data. Embed k0 into C. This is NOT
an embedding required to fix all complex constants of a larger field.
After scalar extension there is a compact complex curve, the same degree-d
map and a nonzero holomorphic differential still satisfying f*eta=eta.

The real two-form i*eta wedge conjugate(eta) has positive finite integral I.
Away from finitely many branch values, f is a d-sheeted oriented covering;
the branch sets have measure zero. Change of variables therefore gives

    0 < I = integral f*(i*eta wedge conjugate(eta)) = d*I < infinity.

This contradicts d>1 and proves the lemma. The argument covers every
pole-free genus; it does not assume the differential originally had no poles.

## 3. Removing geometric disconnectedness

Put L=C(x,y), sigma=H*, and N=[L:sigma(L)], the generic degree of H.
Let K be the relative algebraic closure of C(r) in L. It is finite over
C(r), since L/C(r) is finitely generated of transcendence degree one.

Because sigma fixes C(r), it sends K into K. Its restriction is an
injective linear endomorphism of the finite-dimensional C(r)-space K,
so is an automorphism. The group Aut(K/C(r)) is finite. For some e>=1,
tau=sigma^e therefore fixes K pointwise, and

    [L:tau(L)] = N^e.

This degree identity follows by applying sigma repeatedly to the finite
field extension L/sigma(L) and multiplying degrees in the resulting tower.

The field K is algebraically closed in L, and characteristic zero gives
separability. Thus L/K is a regular one-variable function field. Its smooth
projective K-curve is geometrically integral. The K-embedding tau induces
a finite self-map of that curve; extending to an algebraic closure of K
preserves its degree N^e. These are the classical smooth projective
curve/function-field correspondence and scalar-extension degree facts.
We work with this projective curve, not a possibly punctured affine pencil
chart, so affine base points cause no extension assumption.

## 4. The invariant relative differential

Since K/C(r) is finite separable, the exact sequence of field differentials
identifies

    Omega^1_(L/K) = Omega^1_(L/C) / (L*dr).

Here dr is nonzero. Wedge multiplication by dr identifies the one-dimensional
L-space on the right with Omega^2_(L/C). Consequently there is a unique
nonzero RELATIVE differential class eta such that

    dr wedge eta = dx wedge dy.

The wedge means: choose any absolute representative of the relative class;
adding a multiple of dr changes nothing. We do NOT require an invariant
absolute representative.

The map tau fixes K and dr, and exact area preservation persists under
iteration. Pulling back the displayed identity shows tau*eta=eta as a
relative differential. After geometric scalar extension it becomes a
nonzero invariant rational differential on the smooth projective curve.
The lemma in section2 gives N^e=1, hence N=1, proving the theorem.

## 5. Scope checks and relation to earlier work

Exact area preservation cannot be replaced by arbitrary nonzero constant
Jacobian in this RATIONAL theorem. The fixed map

    H(x,y) = (x^2, y/x)

has Jacobian2, generic degree2, and invariant r=xy. Its relative logarithmic
differential is multiplied by2, not fixed. This map is not polynomial and
is not a JC2 counterexample. Normalizing one output by a constant can
destroy a previously fixed rational invariant.

The [positive-genus invariant theorem](positive-genus-invariant-swarmHQ-root-20260919T035200Z.md)
already excludes degree>1 POLYNOMIAL self-maps preserving a geometrically
integral positive-genus pencil, without assuming constant Jacobian. Its
genus-one step needs the nonempty affine puncture set. The present theorem
instead needs exact area preservation, but permits rational maps, any
genus and disconnected original pencils. Neither statement should be
silently substituted for the other outside its hypotheses.

Matched birational conjugacy transports an invariant rational function,
but need not preserve the displayed STANDARD area form. More generally,
the proof would use a specifically transported invariant rational two-form;
we make no claim that an unrelated source/target normalization supplies one.
Independent changes at the two ends do not preserve a self-map invariant
automatically. No arbitrary two-ended repair exclusion follows here.

ROOT reconstructed the proof and a reused native Astra handle independently
co-checked the relative class, constant-field descent, degree, pole cycles,
residues, and finite-data analytic reduction. Native author completion was
12:00:04 UTC. This is same-model manual checking, not independent FIRST.
Scoped searches of frozen public and HQ histories found no completed exact
version; that is not an exhaustive novelty audit. No new source theorem,
CAS, scientific computation, cloud worker or proof assistant was used.
No new donor family, invariant-existence assertion or mathematical descendant
is proposed. Different-model review is pending; JC2 remains unresolved.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised `OPEN[...]` entries.

Author completion: 2026-09-19 12:04:49 UTC, after whole-body readback and
the collision check. No computation beyond document-integrity tooling.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8235`.
- Body SHA-256:
  `f30579024e1101d56f9281a9d391508e90f121e3506fee2093670e43ab261bd6`.
- Frozen basis: `2730e5d5f98b64bff4a51e460c3e91117efa60d9`.
