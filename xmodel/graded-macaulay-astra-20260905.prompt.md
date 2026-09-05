# COMPUTE-STRUCTURE lane (turn "c^N ∈ I" into finite LINEAR ALGEBRA in one bidegree — no Gröbner basis): your round-2 graded report (frozen) proves the completed Moh chart ideal I ⊂ R = Q[z, c] is N²-homogeneous (deg z = (b, iK−a), deg c = (ℓ+1, D)), that V(I) is a cone, and that c ∉ I on the 77/111/129/136 fibres — so a (T)-kill needs c^N ∈ I for some N ≥ 2 (equivalently UNIT on I + (Tc−1), by the cone lemma). Every Gröbner attempt is time-bound. USE THE GRADING: c^N ∈ I ⟺ c^N lies in the degree-(N(ℓ+1), ND) piece I_δ of I, and I_δ is SPANNED by {m·g : g a generator of I of bidegree deg g, m a monomial of bidegree δ − deg g}. That is a finite sparse linear system (the Macaulay matrix M_δ of I in bidegree δ): c^N ∈ I ⟺ the vector of c^N lies in the row space of M_δ. TASK: (1) for the 77-parameter fibre (m12_m2_5/V1_1_6, s'=4 control; then 111/129/136) compute the bidegree δ_N = (N(ℓ+1), ND) for N = 2, 3 and COUNT the monomials of R in bidegree δ_N and the rows of M_{δ_N} (generators × monomials of the complementary bidegrees) — report sizes exactly; exploit the torus: the c = 1 section and the charge-zero eliminations (the 27/71 unit pivots of your triangular reduction) shrink the ring — do the count in the reduced ring too; (2) if the matrix is feasible (≲ 10^7 columns, sparse), compute its rank modulo a large prime with sparse linear algebra (python-flint nmod_mat for dense blocks; a sparse elimination in the style of F4's linear algebra — write it, or use msolve's `-P`/`-g` machinery only if it exposes a single-degree step; Singular's `kbase`/`jet` + `lift` in a truncated weighted ring is an alternative) and TEST whether c^N is in the row space: a modular YES is a signal ⇒ then produce the exact rational combination (lift with CRT over several primes, or solve the sparse system over Q on the identified support) and VERIFY the identity Σ m_j g_j = c^N in the original ring — that is a valid class kill under the h-support gate §8 rule with full custody; a modular NO at a given N is exact (rank cannot drop only over Q... careful: a modular NO for membership is not exact — membership over Q implies membership mod p for good primes, so NO mod p ⇒ NO over Q; state this correctly); (3) if infeasible at N = 2, 3 report the exact sizes and the minimal N-independent reduction (which bidegree pieces vanish, the Hilbert function of R/I in the relevant degrees from the truncation runs); (4) fleet: launch one r7i.16xlarge if RAM is needed (`bash ops/fleet/fleet.sh launch 1 r7i.16xlarge`; TERMINATE before sealing; never touch other workers). FALLACY-v2 (a modular membership is a signal; an exact rational identity in the ORIGINAL ring is the certificate; a truncated/specialized zero remainder proves nothing). ≤ 180 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/graded-macaulay-20260905/.
Report: xmodel/graded-macaulay-astra-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 180 min.
charged_input=xmodel/graded-moh-astra-r2-20260905.md
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=xmodel/source-support-closeout-opus5-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/graded-macaulay-astra-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
31b1a6a8a94a61968d88f4b92713b6a5eb15d6da1df041f37d055e933ba1deb6  {{LANE_INPUTS}}/graded-moh-astra-r2-20260905.md
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c  {{LANE_INPUTS}}/source-support-closeout-opus5-20260905.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d  {{LANE_INPUTS}}/fleet.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
