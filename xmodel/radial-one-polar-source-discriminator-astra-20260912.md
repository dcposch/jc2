# One radial polar: exact conductor reduction, unresolved source implication

MANUAL co-research, not FIRST or promotion. First action2026-09-12
22:35:09.043974670 UTC; reserve22:52/HARD22:55 unchanged. Five input pins
matched before bodies; four mathematical texts freshly WHOLE, COORD snapshot
exact-pin prior WHOLE reused. No extra body or execution was used.

## Verdict and dependencies

**GAP for the asserted one-polar implication.** No nonautomorphic polynomial
Keller pair is produced. There is a precise conditional strengthening: in a
finite canonical graph, one-polar membership makes the actual conductor
vertical for g. If, in addition, its multiplicities are uniform across the
WHOLE components of each supported g-fibre, the Keller pair is invertible.
Uniformity, including absence/presence of all fibre components, is not proved
by stability. This is not a theorem that the membership holds automatically.

The supplied finite-graph construction gives finiteness after a chosen source
shear and recomputed radial potential; it does not give finiteness for every
radial H in every fixed frame. I therefore explicitly assume R finite over B
when using its conductor. Membership cannot silently be carried through that
shear: H and B change. The arbitrary-frame question has at least this extra
unsettled attachment; the finite-frame question still has the gap below.

The new ROOT finite-generation/two-polar claims are PROVISIONAL inputs, not
promoted by this report or by an unseen live review. I reconstruct the needed
ring argument below. The supplied canonical-graph and fixed-volume conductor
identities are used at their stated exact finite-source scope; the new
one-polar deductions are themselves MANUAL/PROVISIONAL, one generation only.

## 1. What one membership actually proves

Put R=C[x,y], A=C[f,g], B=A[H], delta=D_f, with J(f,g)=1 and
dH=(x dy-y dx)/2-f dg. Then delta(f)=1, delta(g)=0 and
delta(H)=-E(g), E=(x partial_x+y partial_y)/2. These follow by evaluating
the displayed one-form on delta. Thus delta(H) in B implies delta(B) subset B;
also delta(R) subset R by the inverse-Jacobian formula. Only this derivation
is known to preserve B. Commutation with D_g does not make D_g preserve B.

Assume now the finite birational graph and its exact conductor
I={a in R:aR subset B}=cR, c=P_W(f,g,H)!=0. For a in I and r in R,

    delta(a)r = delta(ar)-a delta(r) belongs to B.

Hence delta(I) subset I, so delta(c)=h c for some h in R. This is a
Darboux equation, not delta(c)=0. No division by c in R has been made.

Factor c into irreducibles in the UFD R. If q occurs with multiplicity m>0,
the equation and characteristic zero give q dividing delta(q): reduce
delta(c)/q^(m-1) modulo q, where the other factors and m are nonzero.
The vector field delta is nowhere zero, since delta(f)=1. On the function
field of the irreducible curve q=0 it is a nonzero C-derivation, still with
delta(f)=1. Its constants are C: a nonconstant constant-of-derivation would
make that function field finite separable over a rational constant subfield,
forcing the derivation to vanish by uniqueness of separable extension.
Since delta(g)=0, g is a constant a on q=0. Therefore

    every irreducible factor q of c divides some g-a.

All g-fibres are reduced: a repeated factor of g-a would divide both partial
derivatives of g, contrary to the Keller identity. This proves vertical
conductor support, including reducible fibres and arbitrary conductor orders.
It says nothing here about verticality of the nonproperness divisor.

## 2. The exact extra condition that would close the argument

Suppose each supported fibre g=a occurs in c with the SAME multiplicity on
every irreducible component, counting an omitted component with multiplicity
zero. Unique factorization and reducedness then give c=k Q(g), k in C*,
Q in C[T]. In particular this holds if all conductor-supported g-fibres are
irreducible. It is substantially stronger than vertical support.

Choose the primitive irreducible relation P(U,V,W) of f,g,H; its W-degree is
positive. The identity c=kQ(g) gives P_W-kQ(V) in (P). Its W-degree is less
than deg_W(P), so it must be the zero polynomial. In characteristic zero,

    P=kQ(V)W+P_0(U,V).

Consequently H belongs to C(f,g). Since the canonical primitive-field
argument gives C(f,g,H)=C(x,y), F is birational.

For completeness, birationality plus the whole-plane Keller hypotheses
implies polynomial invertibility without assuming finite projection. Write
the rational inverse coordinate x=a(f,g)/b(f,g) in coprime target polynomials.
If an irreducible p divides b, p(f,g) is nonconstant and has an irreducible
source zero-curve. The Keller map is quasi-finite, so that curve maps densely
onto the target curve p=0. Coprimality makes a(f,g) nonzero generically on it,
whereas b(f,g) vanishes, contradicting regularity of x. Thus b is constant;
the same holds for y. Hence A=R.

The missing condition is precisely the across-components multiplicity
constraint, not the already-established tangency along each component.

## 3. Generic monogenicity: useful, but not the missing theorem

Let S=C[g] minus zero and K=C(g). Since c has only vertical factors, some
nonzero Q(g) is divisible by c in R (choose enough multiplicity). Thus
Q(g)R subset cR subset B, and localization gives

    S^-1 R = S^-1 B = K[f,H].

This equality is stronger than an assertion of equal fraction fields. It
does NOT say this curve algebra is finite over K[f]. The relative differential
module is zero by the Keller identity, so the monogenic relation has P_W a
unit of S^-1 R. That unit need not lie in K*.

Indeed UFD factorization describes all the possible extra units: if a/s is
a unit of S^-1 R then ab=st for some b in R and s,t in C[g] minus zero.
Consequently its numerator factors among irreducible components of special
g-fibres. Nonconstant generic-fibre units can therefore retain precisely the
component information that the vertical-support argument lost. Replacing
them by constants would silently impose another source hypothesis.

For a minimal logical check, K[u,w]/(u*w^2-1)=K[w,w^-1] is monogenic and
etale over K[u]: the derivative 2uw is a unit. Its map to A1_u omits zero,
is not finite, and has nonconstant units. This is only an elementary check
of the two forbidden inferences, not a proposed Keller control or new lane.

If all g-fibres were irreducible, that UFD unit description would give
(S^-1 R)*=K*. Then P_W in K* would force the relation linear in W and
S^-1 R=K[f], hence birationality and invertibility as above. The supplied
sources establish neither this fibre hypothesis nor the weaker uniform
multiplicity condition on just the conductor-supported fibres. No conclusion
about actual nonproperness is used to bridge them.

## 4. Primitive field and two-polar boundaries, reconstructed

The primitive-field step used in section2 can be checked independently of
the new finite derivative-list assertion. Put L0=C(f,g,H). The two target
derivations extend uniquely to this finite separable field, so H_f,H_g lie
in L0. The radial identities give E(f)=f+H_g, E(g)=-H_f and E(H)=fH_f.
Hence E preserves L0. Finite interpolation in E on homogeneous degrees
extracts f_1,g_1 into L0. Their determinant is the Jacobian at the origin,
equal to one, so they span x,y. Thus L0=C(x,y).

With BOTH memberships, both target derivations preserve B; alternatively
E already preserves its three generators f,g,H directly by these identities.
Degree-one projection then gives x,y in B, hence B=R. Monogenicity and
Omega_(R/A)=0 imply P_W is a whole-plane unit, therefore a nonzero complex
constant. The smaller-W-degree argument gives H in A and A=R. This verifies
the provisional two-polar implication without importing its pending FIRST
or confusing it with the one-polar condition. With only H_f in B, E(f)
still contains the uncontrolled H_g; the projection cannot be iterated in B.

For an automorphism A=R and both memberships hold automatically. The supplied
punctured-plane pair f=x^2,g=y/(2x),H=0 has one and both memberships but is
not a whole-plane polynomial pair: it only marks the global-polynomiality
boundary, not a refutation of the question asked. No genuine Keller
counterexample, blanket membership assertion, normality or JC2 conclusion
has been obtained.

## 5. Stopping point, quantity and custody

The exact unclosed arrow in the finite-source argument is

    H_f in B  ==>  c is a polynomial in g,

or any substitute that removes the surviving fibre-component unit data.
Only the weaker vertical-support implication was proved. Even a proof of
one-polar sufficiency would make membership equivalent to invertibility,
since the converse is immediate; it would not prove actual membership.
This report does not establish that equivalence or authorize a child search.

Cheapest discriminator of this argument is a manual comparison of the actual
conductor multiplicities across all components of one supported fibre, or a
source lemma forcing their uniformity; no actual such fibre/pair is supplied.
Five review minutes is an UNMEASURED planning allowance for checking this
precise gap, not an observed runtime or a selected new task. STOP here rather
than expand an ODE, curve, norm or relaxed-control family.

Own targets were absent before begin; no shared target or canonical OPEN.
Inputs: CLAIM3576962b, derivative reportb8374142, conductor report0b5aba8a,
finite-graph report77669329, COORD snapshot33cfa610, all exact full pins and
read modes in PINS. No linked or pending-review body consumed. Four scientific
texts read freshly WHOLE; COORD reuse traces to the completed same-agent
20:05-20:14UTC whole read, after the current snapshot pin. Only documentary
text/hash/date/apply_patch and the unchanged finalizer were used. Final own
WHOLE readback and unchanged input postpins precede the unique marker LAST;
custody is the last authored file and the terminal message gives actual IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9977`.
- Body SHA-256:
  `e91563c98b4b8b9d8e92938d9c922b7291ceaadf3d0d993220cc1675f6e703eb`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
