# AS F-only affine-output normalization lemma

## Exact statement

Let `R` be either `Z_3` or `Z/3^n Z`, and let

\[
F=(P,Q)\in R[x,y]^2,
\qquad \det JF=1\in R[x,y].
\]

Assume that the reduction of `F` modulo 3 is the AS seed

\[
(x-x^3,y).
\]

Put `c=F(0)` and `A=JF(0)`.  Then `det A=1`, so `A` is in `SL_2(R)`, and

\[
G=A^{-1}(F-c)
\]

satisfies

\[
G(0)=0,\qquad JG(0)=I,\qquad \det JG=1.
\]

Moreover `A` reduces to `I` modulo 3, hence `G` has the same AS special fibre.  Thus all constant coefficients and every higher 3-adic digit of the degree-one coefficients can be removed simultaneously, without changing the determinant equation.

## Proof

Evaluation at the origin commutes with the determinant, so

\[
\det A=(\det JF)(0)=1.
\]

Therefore `A` is invertible over `R`.  Translation in the target does not change a Jacobian matrix, and left multiplication by `A^{-1}` gives

\[
JG=A^{-1}JF,
\qquad
\det JG=(\det A)^{-1}\det JF=1.
\]

The identities at the origin follow immediately.  The seed has value zero and Jacobian `I` at the origin in characteristic three, so `c=0` and `A=I` after reduction modulo 3.  This proves preservation of the special fibre.

The same proof applies to a finite congruence map: reducing integer coefficients modulo `3^n` turns `det JF congruent to 1 mod 3^n` into the exact equality `det JF=1` over `Z/3^n Z`.

## Support condition

Postcomposition takes `R`-linear combinations of the two components.  It preserves a common total-degree cap, and more generally any common monomial support set allowed for both components.  It need not preserve two different lacunary support sets assigned separately to `P` and `Q`.  The F-only `D=7` gate uses the same total-degree cap for both components, so this support condition is met.

## Campaign use and firewall

This lemma licenses a **normalized complete-map chart**: to exclude genuine determinant-one maps, or complete maps modulo `3^n`, it is enough to exclude the chart with zero constant term and identity linear part, provided the remaining compiler contains every degree-at-least-two coefficient allowed by the common support cap.

It does not turn an incomplete filtered state into a normalized determinant-one map.  In particular, the displayed Q5/Q4/Q3 states still have unresolved lower determinant rows and cannot themselves be postcomposed under the lemma as though they already solved the complete equation.  The valid implication is conditional: any complete continuation of such a state has an affine-output-normalized representative, and a source-complete normalized successor must contain that representative.  Therefore the Q2/Q1 exclusion promotes beyond its explicit digit family only after the compiler is audited to contain all transformed degree-at-least-two coefficients and to reimpose every determinant/terminal row.

No all-depth, algebraization, collision, counterexample, or JC2 conclusion follows from normalization alone.
