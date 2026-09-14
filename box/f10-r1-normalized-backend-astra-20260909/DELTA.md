# Literal source delta inventory (static, unexecuted)

The accepted retained transformer/checker/helper were copied unchanged as
retained_transformer.py, retained_checker.py, execution_gate.py. Their hashes
are exactly the charged originals; no old source was edited. These are not
an edited old representation artifact or a live caller adaptation.

NEW algebra.py: selected dense-Q[v] coefficient operations and rational-string
sparse wire conventions from the old transformer architecture, now with the
axes x,y,z,s,S,t,v. Only fixed-modulus reduction, certified unit inverse and
column-ideal Bezout operations. Adds fixed3-by3 adjugates; no generic solver.

NEW generator.py: complete normalized Euler recurrence, completed first and
second matrices, literal third series left inverse, and fourth column-ideal
Bezout. It does not consume a precomputed normalized artifact or the newer
univariate theorem. Every basis probe is only a coefficient/matrix definition;
setting z=0 there does not specialize the final source. The final construction
keeps z polynomial and s unchosen.

NEW checker.py: separate canonical parser, flat monomial modulus construction,
long reduction and repeated multiplication. Does not import generator.py,
evaluate its Euler recurrence or use its B inversions. The frozen original
coefficient/row wires independently bind all completed matrices, affine forcing,
maps, full A/B, upper/low target, zero slots and guard after z=s^2. This injection
does not set s=1. Full bracket and inverse poles are also calculated directly.
Simple linear utilities remain shared and must be included in static review.

Fourth-band choice: let h=(Acol,Bcol), and let lambda be the accepted Gram
left inverse. The new pair-Bezout algorithm returns lambda' with the literal
identity lambda' h=1 checked before use. If d=lambda'-lambda, then

    d=t*(Bcol,-Acol), t=d_A*lambda_B-d_B*lambda_A.

Thus E'-E=-t*(Bcol*P-Acol*Q)=-t*Phi4. The two whole substituted presentations
are identical modulo the retained compatibility; individual lower G/H
polynomials need not be byte-identical to the Gram choice. All lower equations
are regenerated with the chosen E, and all original equations are checked with
the same back-map. This is not localization at Acol or Bcol, and does not
discard any leading component. No other triangular-map recipe is changed.

No API was added to the old checker or helper. No caller/authority/supervisor
was created. DISABLED.json has no active host, caps, argv or deadline. The
external CAPRUN hash is a future registration requirement only.
