# Audit: selected-Q8 positive-genus specialization bypass

Date: 2026-08-25  
Reviewer: cube owner, independent hand audit  
Verdict: **SOUND AS A CONDITIONAL CURVE-THEORETIC COMPOSITION**

## Audited implication

Assume all four charged inputs at their exact scopes:

1. a geometrically integral mod-127 plane curve `H` and an `H`-supported
   selected-source component `C`;
2. the reviewed rational-contact theorem, so one of the full contacts
   `v=26,58,67` lies on such a `C`;
3. the arithmetic full-contact bridge, giving the same integral source over
   a common DVR and completed local ring `R[[w]]` at that marked point;
4. geometric genus `g(H)>0`.

Then the normalization of `C` maps finitely and separably to the normalization
of `H`.  Finiteness follows from the nonconstant map of projective integral
curves.  Separability is certified locally: the completed map at the marked
point preserves `w` with a unit linear term, so the pullback of `dw` is
nonzero.  Riemann--Hurwitz therefore gives `g(C)>0` (also in the `g(H)=1`
case).

The arithmetic completion `R[[w]]` has one total component and one special
branch.  Hence the closure of the attached characteristic-zero selected
component specializes dominantly to `C`; it cannot switch to a different
special component through the same full point.

If that characteristic-zero component were dominated nontrivially by
`P1`, its smooth projective function field would be a subfield of `K(t)` and
therefore rational by Lüroth.  Resolve a proper model of this rational curve
over the DVR and its map to the selected-source closure.  Every geometric
vertical component of a regular proper model birational to `P1_R` has
rational normalization (equivalently, use the ruled-residue theorem for a
residually transcendental divisorial valuation of `K(t)`).  A vertical
component mapping dominantly to `C` would then put `k(C)` inside a rational
function field, forcing `C` rational by Lüroth, contradiction.  This argument
does not require the special map to be separable.

Finally, the reviewed primitive eight-contact action permits only one
all-eight component or eight singleton conjugates.  In the first case the
attached component is the common one.  In the second, all eight singleton
components have conjugate projective normalizations and the same genus.
Thus one positive-genus attachment excludes a nonconstant `P1` trajectory
on every selected contact component in either partition.

## Necessary cautions

- An affine closure or pointwise reduction is insufficient; properization
  and the divisorial special component are load-bearing.
- `R[[w]]`, not merely the plane identity `H(0,v)=0`, supplies local
  uniqueness and the generic-to-special attachment.
- The positive-genus conclusion remains conditional until an exact genus
  certificate is frozen and reviewed.
- The cross-characteristic contact bridge is producer-exact and still needs
  its independent review before this composition can be promoted.
- The argument covers selected components meeting corrected-Q8 contacts
  only.  Components disjoint from those contacts and all other maximum-twelve
  strata remain outside scope.

No all-contact, degree-one, Taylor, terminal, full maximum-twelve, or JC2
conclusion is asserted here.
