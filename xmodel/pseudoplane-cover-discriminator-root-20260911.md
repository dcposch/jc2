# Double-cover boundary test: Euler cancellation, not an obstruction

ROOT / MANUAL STRATEGY DISCRIMINATOR / INTERNAL-UNREVIEWED.
Research began2026-09-11 12:20UTC; publication reserve12:36/HARD12:40 unchanged.
No scientific code, test, CAS, dummy, model adapter or AWS worker was run.
This is not an all-H classification, a promoted theorem or a JC2 resolution.

## 1. Exact cover and affine chart

Let S=Spec R, R=C[A,U,Z]/(U^2-A-A^2Z), and L={A=U=0}.
Put T={t^2-1=x^2Z} and q(x,t,Z)=(x^2,xt,Z). The involution
sigma(x,t,Z)=(-x,-t,Z) has no fixed point: x=t=0 violates the equation.
This is the classical cover of S(2,2,1), not a new construction; compare
[Dubouloz–Palka, Examples2.11–2.12 and equation5.2](https://arxiv.org/pdf/1701.01425v2).
The following elementary verification fixes its exact use here.

Write B=1+AZ; A and B generate the unit ideal. Over A!=0, q is obtained
by adjoining x with x^2=A and setting t=U/x. Over B!=0, it is obtained
by adjoining t with t^2=B and setting x=U/t. Both are finite etale of
degree2, since the adjoined root is invertible and characteristic is zero.
These two target opens cover S, proving the global finite-etale statement.

Let D_±={x=0,t=±1}, each an affine Z-line. There is an isomorphism

    A2 -> T minus D_-, (x,y) -> (x,1+x^2y,2y+x^2y^2).

The inverse y=(t-1)/x^2 on x!=0 equals Z/(t+1) on t+1!=0;
these opens cover T minus D_-. Thus q restricted to this chart is exactly
Phi(x,y)=(x^2,x+x^3y,2y+x^2y^2), not merely a birational resemblance.

## 2. What fibrewise Euler bookkeeping actually says

Use compactly-supported topological Euler characteristic chi, which is additive
for the algebraic strata used below and multiplicative for finite covers.
For ANY H in R with nonconstant restriction p(Z)=H(0,0,Z) of degree d,
write C_c=H^-1(c), E_c=(Hq)^-1(c), and F_c=(HPhi)^-1(c).
Let r_c be the number of distinct roots of p(Z)-c, without multiplicity.
Finite-etale base change and the exact affine chart give

    chi(E_c)=2 chi(C_c),
    F_c=E_c minus (D_- intersect E_c),
    chi(F_c)=2 chi(C_c)-r_c.                         (1)

There is no smoothness or generic-connectedness assumption hidden in (1).
All three assertions concern the full fibres. Over a common finite algebraic
stratification of the target, choose the generic values c0=chi(C_gen),
f0=chi(F_gen). Then f0=2c0-d. Additivity over those strata is the usual
constructible Euler integration formula, not an assumption that a smooth
nonproper map is a locally trivial fibration at every target value.

Directly, chi(S)=1: the A!=0 part is C* times A1 and the remaining reduced
line L has characteristic1. Also chi(A2)=1. Consequently

    sum_c (chi(C_c)-c0)=1-c0.

Each root of p of multiplicity e over c contributes e-1 to d-r_c.
The derivative p' has degree d-1, hence sum_c(d-r_c)=d-1. Substituting (1),

    sum_c (chi(F_c)-f0)
      =2(1-c0)+(d-1)=1-(2c0-d)=1-f0.               (2)

Thus the plane Euler identity is EXACTLY the surface identity plus the
one-variable derivative count. The apparent new boundary-degree cost cancels.
Even if one separately imports nonnegative fibre defects for H, the induced
plane defects are 2 delta_c+(d-r_c), automatically nonnegative. No upper
bound on d is obtained from this accounting alone. This is a statement about
the displayed identities, not about every topological or ramification method.

For constant p=c*, the removed locus is empty generically and the whole
D_- at c*. Replace r_c in (1) by its Euler value:1 at c*,0 elsewhere.
Then f0=2c0 and the extra sum is-1; cancellation again gives1-f0.
This includes U, whose boundary restriction is constant. Affine boundary
must include degree0 as well as degree1.

## 3. Primary-text applicability check and a countercontrol

A targeted search found [Hajra, arXiv2608.04214v1](https://arxiv.org/pdf/2608.04214v1),
submitted August4,2026. Its Theorem A assumes a finite surjective map from
C* times C*. No such map is supplied for S here, so that classification
does not discharge the arbitrary-submersion gap. Its Lemma2 on printed page4
asserts fibre irreducibility from Picard rank zero and a smooth affine
rational generic fibre. That auxiliary assertion is too broad as printed.

Elementary countercontrol: X=A2, B=A1, f(x,y)=xy. Pic(X)=0, the generic
fibre is C*, every fibre is connected, and f^-1(0) is the union of the two
coordinate axes. Thus even a connected-fibre convention does not repair
part2. If one instead adds the unstated condition that f be everywhere
submersive, f=x+x^2y has derivatives1+2xy and x^2 with no common zero,
generic fibre C*, and zero fibre A1 disjoint union C*. Neither example is
a scalar-bracket pair. The second example does not have connected special
fibre; it is not presented as satisfying both added conditions at once.

This is a scoped manual counterexample to an auxiliary lemma, not a refutation
of the paper's main classification and not a new JC2 result. No theorem from
that preprint is imported. PDF page4 was read first in exploratory primary
web text, then in local PDF extraction after its source hash was recorded. No contact,
publication or external issue was made. The exact PDFs retrieved12:26:34UTC:

- hajra-2608.04214v1.pdf SHA
  ff124a88e31585e81c9d0b21890570e34388e601cd1e450882cba74f6cdd14a4.
- dubouloz-palka-1701.01425v2.pdf SHA
  41150cfda4fdf477efefc7d2ce55bc5fb49941705620b567b3333df5fe84281e.

The latter's quoted surfaces/cover were checked in Examples2.11–2.12 and
equations5.1–5.2; its whole paper was NOT freshly read. Etale selfmaps in
that work remain distinct from an etale map S->A2. Search-only hits and the
failed Gurjar/IAS fulltext fetch are not proof dependencies. This targeted
intake does not count as a completed broad sweep.

## 4. History checksum, disposition and next discriminator

The old September2 notes around19438 already record a Suzuki ledger
cancellation for a Keller pencil, and around19702 record the unit-speed /
Riemann–Hurwitz wash. This cover attachment is at most a new instantiation
of a KNOWN mechanism, not a new global strategy. Those were selected-range
historical reads, not a fresh review of every old claim or its instruments.
The August31 one-cusp report's §§2,6.1,6.2 supplies related Picard and
smooth-fibration countercontrols; its degree-four ledger is not silently
generalized. Its historical hash was recorded after exploratory range reads.

The exact chart and identities in Sections1–2 are derived here from the
displayed equations, independently of those historical conclusions. No
generic fibre has been shown to be rational, no boundary degree bound has
been obtained, and no finite-jet algebraization or regular scalar pair is known.
The arbitrary-H affine-boundary assertion remains GAP. A finite etale
intermediate double cover is not the full Galois hypothesis for a Keller map.

STOP the Euler-only double-cover route as an additional discriminator. This
does not stop all pseudoplane work or promote an impossibility claim about
stronger invariants. Astra's separately owned bounded full-pair task tests
compactified-curve ramification, not this Euler calculation. Its live report
has not been consumed as an input; any terminal findings require their own
custody collection. No extra sparse-family, finite-degree, formal-jet,
runtime-engineering or assurance lane is selected by this report.

QUANTITY for any successor: a genuinely additional global restriction on
regular scalar pairs, not another derivation of the same numerical identities.
CHEAPEST TEST now active: Astra's one full-pair ramification discriminator,
planning15minutes UNMEASURED, original12:36 reserve/12:40 hard stop. If its
constraints also duplicate Riemann–Hurwitz without contradiction, stop that
numeric proposal and retain the global surface/algebraization GAP. No result
here changes mathematical dispositions1–46 or licenses source computation.

## COLLISIONS and resources

Own final/manifest absent at begin; no duplicate live owner for the H-only
test. Related historical Suzuki and rational-deck mechanisms were found and
explicitly reconciled above. No exhaustive novelty claim or new canonical OPEN.
One native Astra task is active; no Fable lane or AWS worker allocated for
this micro-round. Cumulative terminal Fable70653seconds unchanged, not billing.
System-level observation12:26:34: MemAvailable125195788KiB, swap0 and no swap
page-in/page-out counters. Protected workload was not inspected.

The preceding goal turn completed actual retirement/custody and changed
authoritative state: PROGRESS operationally, not mathematically. This turn's
banked discriminator changes the next mathematical allocation, not the JC2
truth status. Next FULL23:38:28.440200222 and BROAD22:01:02.811468974UTC,
all inherited debts unchanged. The goal remains active and unresolved.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8854`.
- Body SHA-256:
  `83603ae1a3561e89c82afc522f781a54b1a650f8bef15294ba6c5253cd772502`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
