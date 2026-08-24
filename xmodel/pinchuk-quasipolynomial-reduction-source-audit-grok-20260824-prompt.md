# Hostile primary-source audit — Pinchuk quasi-polynomial reduction

Act as an independent hostile mathematical source reviewer. Work in
`/Users/dc/code/math/jc2` at basis
`7832fb73ac887041968f9cec2dc6cba7aa0d0bcf`. The newly found source is:

S. I. Pinchuk, *Quasi-polynomial mappings with constant Jacobian*,
Izvestiya: Mathematics 85:3 (2021), 506--517, DOI `10.1070/IM9017`.

Primary landing page:
`https://www.mathnet.ru/eng/im9017`

Primary English PDF:
`https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=9017&what=fullteng`

Read the whole primary paper, not search snippets. Also inspect the exact local
campaign context in `xmodel/ideation-20260824T1820Z-packet.md`, but do not read
any ideation submission or synthesis from that round. Read primary sources
cited by Pinchuk where a load-bearing arrow is imported, especially the exact
scope of Pakovich--Zvonkin 2014 (`arXiv:1306.4141`) and any source actually
needed for Theorem 1.3. Secondary summaries are navigation only.

Audit these claims independently:

1. **Definitions and fidelity.** Reconstruct polynomial equivalence,
   q-equivalence, and “a polynomial map is equivalent to a q-map.” State
   exactly which properties are preserved in each direction: constant
   Jacobian, polynomiality, rational/fractional powers, invertibility,
   noninvertibility, and recovery of a polynomial inverse. Find the smallest
   countermodel to any overreading.
2. **Imported polynomial normal form.** Identify the precise provenance and
   hypotheses of Theorem 1.3. Decide which pieces are proved in the paper,
   which are cited/assumed, and whether they cover an arbitrary hypothetical
   noninvertible plane Keller map after legitimate polynomial changes.
3. **Theorem 3.4.** Line-audit the complete reduction to a q-polynomial reduced
   form. Reconstruct a well-founded termination measure through Lemma 3.6 and
   the sentence “the rest ... is similar.” Check all six cases, rational
   exponent denominators, changes of Newton polygon, preservation of the
   selected adjacent sides, and the assertion that some leading weighted
   Jacobian becomes a nonzero constant. Attempt explicit small polygon
   countermodels to every monotonicity or termination step. Give
   `CONFIRMED`, `GAP`, or `REFUTED` at the strongest exact scope.
4. **Theorem 4.1.** Independently derive the identity for coprime positive
   `k,r`, degrees `kd,rd`, and `m=k+r+1`:

   ```text
   r*p'*q-k*p*q' in C*;
   deg(p^r-q^k)=d*(k*r-k-r)+1;
   J(x^-k p(x^m y),x^-r q(x^m y)) in C*.
   ```

   Check all nonzero/coprime/leading-coefficient hypotheses, signs, and both
   implication directions. Decide whether it remains valid over the
   differential coefficient field `C(x)` when degree is in a separate
   variable `z`, and what specialization/discriminant exceptions arise.
5. **Classification citation.** Check the paper's sentence that
   Pakovich--Zvonkin 2014 gives a “complete classification” of minimizing
   pairs. Distinguish: all complex equality pairs, weighted plane-tree
   correspondence, unitrees, and rational-coefficient examples. State exactly
   what finite enumeration is licensed for exponent pair `(4,3)`, `d=3`.
6. **Maximum-12 client.** Independently verify the campaign's elimination
   identity

   ```text
   W=g^3-f^4-3*k*f^2*g-k^3*f^2
    =Norm_(t^3=f)(g-f*t-k*t^2),
   J(f,W)=3*(g^2-k*f^2)*J(f,g).
   ```

   At `k=mu=nu=0`, verify that coprime monic degrees `(9,12)` and
   `deg_z W=16` exactly attain the polynomial-abc bound for exponents `(4,3)`.
   Decide whether the cited source supplies rigidity, merely a combinatorial
   parameterization, or no shortcut for a coefficient trajectory over
   `C(x)`. Specify the cheapest honest next test.
7. **Campaign impact.** Separate valid local identities from a global JC2
   reduction. Map any usable result to numbered avenues without confusing
   S. I. Pinchuk's q-polynomial work with the real Pinchuk-map avenue. Give
   exact promotion and quarantine language.

Use exact algebra and primary text. Do not edit canonical, packet, producer,
reviewer, prompt, run, log, or case files. Keep scratch outside tracked paths.
Write exactly one report:

`xmodel/pinchuk-quasipolynomial-reduction-source-audit-grok-20260824.md`

Give an overall verdict and per-claim verdicts, source URLs/pages/lines,
explicit derivations or smallest countermodels, and a bounded successor. Do
not claim novelty, priority, or JC2 resolution.
