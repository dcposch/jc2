# ROOT proof lead, separately pinned task guidance

September11,2026. This is input3 added to the independent general-delta1
task, not a rewrite of TASK or a frozen mathematical premise. All steps
must be independently proved or marked GAP. Original reserve21:52 and
HARD21:55 remain unchanged. No affine report or review is an input.
Record this guidance's ROOT provenance if it influences the report.

Potential full-complex-G argument to audit:

1. Factor g(k,n)=G(r+k,n-k) over convergent Newton--Puiseux branches
   k=z_i(n) at n=+infinity, with polynomial leading coefficient a(n).
   Constant integer roots k=J>=0 give the already identified bounded-p
   truncation. G constant is a separate shear case.
2. Choose epsilon>0 below every positive real linear root slope. Thus
   only bounded or unbounded sublinear roots can approach integers in
   0<=k<=epsilon n. Non-real branches have an imaginary part with a fixed
   Puiseux leading power unless identically real. Bounded branches approach
   a fixed integer at a fixed Puiseux power unless identically that integer.
3. For each real positive sublinear root z(n)~c n^s, 0<s<1, exclude degrees
   with dist(z(n),Z)<n^-L, L>1-s and all relevant bounded-root exponents.
   On [N,2N] its derivative is asymptotic to cs n^(s-1), so each integer
   target contributes O(1) bad integer degrees for large L. There are
   O(N^s) targets. Finitely many branches give a density-zero exceptional set.
4. Outside this set, all factors in the first floor(epsilon n) recurrence
   terms have polynomial lower bounds. Only O(n^smax), smax<1, early k
   lie near sublinear roots; their total logarithmic loss is o(n log n).
   Later factors satisfy |g(k,n)|>=C n^gamma k^v with gamma>=0, and a
   positive fraction near k~epsilon n have genuine n-power growth unless
   G is constant. Verify all possible root positions, multiplicities,
   leading-coefficient zeros and signs; do not assert this lower bound
   from a generic leading term alone.
5. The recurrence product's nth root then grows off the density-zero set.
   Convergence of algebraic formal f would force those c_n to decay
   superexponentially. Their subseries is entire; the exceptional subseries
   is Fabry-lacunary. If it has finite radius, a natural boundary would
   contradict algebraicity of H. If entire, algebraic H is polynomial.

This is a proof idea, not an accepted theorem. Precise Puiseux root
separation, exceptional counting, product bounds, and the exact Fabry
version are the hard checks. New external theorem inputs must be named
as standard/conditional when not proved from the charged Bass source.
No automatic claim that this first-delta-order family exhausts U.
