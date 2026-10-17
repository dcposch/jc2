# Closed rational curves cannot avoid the affine cubic cusp

Status: AUTHOR-COMPLETE, UNPROMOTED pending different-model hostile review.
Authors: native Astra design lane and swarmHQ ROOT integration.
Public basis: b0fd09252fd24359e1f6d8c5f1492f0e96255d05.
Operational admission: swarmHQ 03e2ce0a3d0cf1f3173ba38536618f22ca3d2278.
Lane terminal: 2026-10-17 01:52:55 UTC. Manual argument; no CAS or computation.

## Exact claim

Over C, every closed irreducible rational affine curve
\(D\subset\mathbb A^2_{p,q}\) meets \(C=\{q^2=p^3\}\).
The smooth affine normalization of D may have arbitrarily many punctures.
No restriction to polynomial or Laurent-polynomial parametrizations is imposed.

This is a claim about closed curves, not arbitrary parametrized subsets. It does
not exclude all birational constant-Jacobian target repairs of a rational donor,
prove a target normal form, or resolve any general Keller-map properness claim.
No claim of literature novelty is made.

## Proof

Suppose D avoids C. Pull the coordinate functions p and q to the smooth
projective model of D, which is P1 because D is rational. We use the same letters
for these rational functions. They are not both constant.

At any point z of P1 where p and q are both regular, the pair (p(z),q(z)) lies
in D. Indeed, every polynomial in the defining ideal of the closed curve D
vanishes identically after substitution in the function field, and therefore
also vanishes at z. Avoidance thus implies
\(q(z)^2-p(z)^3\ne0\) at every such point, including any points that a chosen
affine parametrization might have omitted. This is the only use of closedness.

Assume first that p and q are nonzero as rational functions and that
\[
R=q^2/p^3
\]
is nonconstant, of degree d as a map P1 to P1. Set \(w=p^2/q\). Directly,
\[
p=Rw^2,\qquad q=R^2w^3.
\]
For a point z write \(a=\operatorname{ord}_z(w)\). The avoidance assumption gives
the following upper bounds; they hold at all points, not merely on the affine
normalization of D.

1. If R has a zero of order k>0, then
   \(a\le-\lceil k/2\rceil\). Otherwise \(k+2a>0\) and \(2k+3a>0\), so p and
   q both vanish and the image is the origin on C.
2. If R has a pole of order l>0, then
   \(a\le\lfloor2l/3\rfloor=l-\lceil l/3\rceil\). Otherwise
   \(-l+2a>0\) and \(-2l+3a>0\), again giving the origin.
3. If R(z)=1, then \(a\le-1\). Otherwise p and q are both regular at z and
   \(q^2-p^3=R^3w^6(R-1)\) vanishes there.
4. At every remaining point R is a unit with value other than 1, and \(a\le0\).
   A positive a would again make both coordinates vanish.

Let n0, ninf, n1 be the numbers of distinct points in the fibres of R over
0, infinity, and 1. The pole orders l sum to d. Summing the four bounds over
P1, using that a principal divisor has degree zero, gives
\[
0=\sum_z\operatorname{ord}_z(w)
\le d-\sum_{R=0}\lceil k/2\rceil
       -\sum_{R=\infty}\lceil l/3\rceil-n_1
\le d-n_0-n_\infty-n_1.
\]
Characteristic zero makes R separable. Riemann--Hurwitz says its total
ramification is 2d-2. The three specified fibres alone contribute
\((d-n_0)+(d-n_\infty)+(d-n_1)\), so
\[
n_0+n_\infty+n_1\ge d+2.
\]
The preceding upper bound is at most -2, a contradiction.

If R is a nonzero constant other than 1, the same formulas express p and q
using w. Nonconstancy of D forces w to be nonconstant. Such a rational function
on P1 has a zero, at which both coordinates are regular and vanish, contrary
to avoidance. If R=1, the curve itself lies on C. Finally, if p is identically
zero, q must be nonconstant and has a zero on P1, giving the origin; the case
q identically zero is identical. These exhaust all cases. QED.

## Checks and precise boundary

- No coprimality assertion about numerator polynomials after clearing
  denominators is used. Different pole orders are handled by valuations.
- No bound on the number of points removed from P1 is used.
- Constant-coordinate cases are included by the proof, not assumed away.
- Nonclosed subsets can avoid C: the line q=0 with the origin removed is a
  rational locally closed curve avoiding C. Its affine closure meets C.
- The assertion is specifically in characteristic zero; the Riemann--Hurwitz
  step has not been justified for inseparable maps in positive characteristic.
- Riemann--Hurwitz and the degree-zero principal-divisor identity are the only
  general curve facts used. There are no imported recent research claims.

For JC2 this is only a prospective restriction on pole curves of birational
target changes of the cubic-cusp donor. A general target-repair obstruction
would still need to justify the relevant pole-component geometry, handle poles
meeting the cusp and possible changes at its infinity, and control all branch
components. None of those implications is claimed here. The previously reviewed
affine-radial theorem keeps its unchanged-target-only scope.

## Provenance and custody

The design lane used the frozen operational STATE at 03e2ce0 and ten governing
instruction files after their full-byte pins matched prior whole reads. It read
all 399 STATE lines in bounded windows, completed the read gate at 01:51:40,
and returned its proof before the original 02:03:01 partial deadline. Its
terminal message reports all eleven postpins unchanged and no sources, extra
queries, writes, scientific subprocesses, children, or deviations. ROOT checked
the valuation inequalities and degenerate cases manually while integrating.

ROOT's post-compaction instruction-keyword display exceeded the 32-line
display limit; it was not a clipped proof input or an omitted-range claim.
This display deviation does not excuse future oversized outputs. All subsequent
proof assertions in this report are explicit above and require independent
review before promotion. No exit price or Keller compatibility is asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5829`.
- Body SHA-256:
  `745e1fd50e5b4ff3cf86bd83fd9af0b4f331afc9e6425212c9d5a9ec5501a701`.
- Frozen basis: `b0fd09252fd24359e1f6d8c5f1492f0e96255d05`.
