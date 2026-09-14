
## 0. Verdict

```text
REQUESTED  (1) exact factorisation of the Γ_t point polynomial over A_t at t = 4 (46 points) and t = 5 (265 points),
               with Frobenius cycle types;  (2) the all-or-nothing lemma with its Hensel/étale step;  (3) the
               one-evaluation instrument at t = 3, 4, 5, 6, 8;  (4) the uniform problem (I);  (5) the liaison
               colon (G):T_top at t = 3, 4;  (6) the verdict on (V0) for all t.
VERDICT    PARTIAL — fixed-t results PROVED, the uniform statement NOT closed and relocated, not removed.
PROVED     (1) f_t is IRREDUCIBLE over A_t for t = 3, 4, 5 AND 6 (Q(√3), Q(√15), Q(√2), Q(√21)): the affine
               points of Γ_t are ONE Galois orbit, by the degree-pattern criterion (Cor. 3.6) at 49 / 48 / 24 / 8
               prime ideals with the good-reduction hypotheses verified at each (Lemmas 3.3–3.5; exact chart
               vdim 7, 46, 265 over A_t; empty boundary at t = 4, 6), and exactly (factorize over A_3) at t = 3.
               Gal(f_t/A_t) = S_7, S_46, S_265, S_1548 (Jordan: prime cycles 41, 257, 1019 of length > n/2; odd types).
           (2) Lemma 3.1 (all-or-nothing), Lemma 3.7 (étale lift of a simple F_p-point on the flat model, the
               FALLACY-v2 lift statement), Lemmas 3.3–3.5 (flatness from the EN Hilbert function; freeness from
               n' = n; good reduction of the point polynomial) — written out, §3.
           (3) the instrument certifies clause (ii)_t at t = 3, 4, 5, 6 by ONE modular evaluation each (W ≠ 0 at a
               simple F_p-point, lifted; 28, 28, 17, 5 independent witnesses); boundary orbits handled EXACTLY at
               t = 3, 5 (b_3 = 1, b_5 = 2: six conjugate points with q_3 = 0 forming one orbit over Q(√2), plus the
               rational q_3-axis point) and empty at t = 4, 6.  Cost at t = 6: three modular jobs, ≤ 3 min, no
               number-field std, no radical.
           (5) (G):T_top = (G) exactly at t = 3 and mod p at t = 3, 4, 5, with positive/negative controls.
NOT CLOSED (4) problem (I) for t ≥ 7: no uniform mechanism; the determinantal structure fixes the degree, not the
               field of definition; the measured S_n groups are the generic (uniform-position) behaviour and
               any proof of (I) is a genericity statement of the same type as (V0)-tail itself (§7).  Moreover
               Prop. 7.1 shows (I) is NOT NECESSARY: clause (ii)_t over A_t follows from the modular cone statement
               V(I_2 + (W)) = {0} plus flatness, with no orbit count.  The binding uniform gap is (II): a t-indexed
               point of Γ_t with a closed-form T_top — unchanged by this lane.
           (3) at t = 8: the CI system (7 forms, 52140 points) mod 32003 was exported and msolve's F4 (4 threads,
               shared worker) was at degree 14 (45739 × 81237) at seal; the boundary of Γ_8 mod 32003 is six points
               in the stratum q_3 = 1 with W ≠ 0 at all of them (modular); the affine one-point test is typed
               OPEN[K16-ONE-POINT-T8] with the verify job ready (validated at t = 6 against Singular).
CONSEQUENCE (V0) ⇒ (8.1) ⇒ (T) on the whole K16 ray is NOT obtained (no MAJOR claim).  What changes: the fixed-t
           certificate of (V0)-tail is now  (i)_t  ∧  [one simple point per Galois orbit with W ≠ 0]  with
           k_t = 1 proved through t = 6, and the all-t problem is (i) ∀t  ∧  (II) — problem (I) is a structural
           fact (S_n) rather than a hypothesis.
NOTIFY     not warranted (no new (V0) index; fixed-t re-proofs by a cheaper route; irreducibility is new but
           closes no ledger item beyond OPEN[K16-GAMMA-IRREDUCIBLE] at t ≤ 6).
```
