**Finite certificate computations: all four first-power tests are settled.** Over Q, **c∉I on each of the 77,111,129,136 completed fibres**. Thus every possible c-power certificate has N≥2. This is a negative ideal-membership result, not radical nonmembership, a c≠0 point, or a class kill.

The certificates give explicit homomorphisms from each FULL quotient R/I to a smaller rational algebra where c survives. For 111/136, send charge-zero coordinates and declared omitted positive-charge coordinates to zero, fixing the retained coordinates and c; use positive degree B and cutoff3. For 77/129, send every charge-zero coordinate z to t^w(z), with deg(t)=(0,1), retain the declared positive-charge coordinates and c, and send omitted positive-charge coordinates to zero. Use H=w+(D+1)B, with cutoffs119/125. These total polynomial maps preserve both gradings; t remains an indeterminate.

Let G be the saved rational polynomial list and M the ideal of all monomials beyond the stated positive-degree cutoff. Every full source row maps into (G)+M: all eligible images divide exactly to zero by G, and every omitted row has larger degree. For the curve receivers the smallest omitted source degrees are123/139, strictly beyond119/125. Verify every required S-pair through the cutoff. The bounded Buchberger criterion proves that the saved nonzero NF(c) survives in A=Q[receiver variables]/(G+M), hence c∉I. No reverse assertion G⊆image(I) is needed for this negative proof. Membership in I would persist under the map, contradicting its nonzero image.

| Fibre | Full rows / terms audited | Eligible rows / nonzero images | Saved basis | Exact required S-pairs | NF(c) |
|---|---:|---:|---:|---:|---|
| 77 | 150 / 33,030 | 77 / 77 | 382 | 775 | c |
| 111 | 167 / 74,878 | 78 / 67 | 60 | 466 | c |
| 129 | 177 / 239,501 | 70 / 70 | 67 | 256 | 21 nonzero terms |
| 136 | 348 / 371,224 | 87 / 76 | 68 | 574 | c |

Independent Python Fraction verifiers reproduce source images and polynomial division; a second independent audit starts from ALL original direct rows and verifies the total maps, both gradings, 2,071 required S-pairs and saved remainders. A basis row reduces to zero; adding c produces the nonzero remainder; 1 stays nonzero. Complete rational bases, source hashes, ordered rings, maps and controls are under `resume-r2/{triangular,truncation}/`; `resume-r2/nonmembership-second-audit.{md,json}` and `audit_nonmembership.py` unify the four proofs.

In all four witness algebras c²=0 automatically because of the degree overflow. Therefore these certificates cannot prove radical nonmembership or supply a geometric point with c≠0. A UNIT or zero c² remainder after these parameter maps would not prove a positive statement in the original chart. This direction distinction is essential to FALLACY-v2.

The triangular computations are also complete as algebraic reductions. Rational DAGs eliminate27/71 unit pivots from the full77/136 presentations, leaving50/65 coordinates. A compact recursive circuit replay checks every pivot identity and rejects each +1 perturbation, without expanding millions of terms. In the N=1 component the136 chart has49 eligible pivots and60 remaining coordinates, with5,209,906 ambient monomials;77 has18,574,576. Corrected exact replay confirms42/37 substitutions for111/129. The original replay's declaration and ideal-comparison errors were rejected. The early curve checker with an undefined lcm routine was likewise rejected; independent rational arithmetic and a clean Singular check replace it. No success marker from an erroneous script is consumed.

The 77/136 strict-low subsystems contain147/338 rows; the111/129 counts are157/168. Every one admits z=0,c=1. All four expensive direct/pivot-order N=1 attempts on .67 were explicitly stopped after the exact nonmembership proofs; their actual rc1 and cancellation reasons are retained, not renamed timeouts.

Bounded N=2 probes also ran on all four fibres, retaining every source row eligible by first charge. Zero remainders were returned by the 77 curve,111 zero-charge,129 selected-curve and136 zero-charge probes. The fuller136 curve probe timed out at600s. These specialized/truncated zero outputs are unpromoted solver dispositions; they establish neither c²∈I nor c²∉I in the original charts. The further full77 test retains all150 original rows, uses the reversed pivot order with positive weights w, and targets c² at(4,78) through weight78. It timed out rc124 after1200.03s under128GiB, without a completed basis or rational identity; original c² membership remains OPEN.

**Adopted fleet and full saturation attempts.** Ownership is established by round-1 `ops/owned-worker*.json`, launch records, status host fields and EC2 launch times: `.67`=`i-05bbedf0197e8eee3` launched13:50:31Z, `.86`=`i-02aaa996f54d2c004` launched13:56:42Z, both r7i.16xlarge. Both were adopted; no additional worker was launched. The requested `sh fleet.sh ips` rejected Bash's pipefail option, so the same fleet script was run with Bash. Other instances were neither used nor terminated, including .7/.18/.28.

The two inherited msolve slices were already FINISHED rc124 when reached:77 took1,201.84s and peaked71,234,288KiB RSS;111 took1,200.86s and peaked32,639,412KiB. These were time limits, not fresh memory-allocation failures. Each had a420GiB address-space limit. The inherited exact-Q Singular full slices timed out at600s, and all three77 second-torus Q branches timed out at900s.

| Full chart / section | msolve modular full | Singular Q full | Additional exact-Q sections |
|---|---|---|---|
| 77 | rc124,1200s | std rc124,600s | 3/3 torus branches: std900s and slimgb1800s, all rc124 |
| 111 | rc124,1200s | std rc124,600s | full slimgb rc124,1800s |
| 129 | rc124,1800s | std rc124,1800s | none |
| 136 | rc124,1800s | std rc124,1800s | none |

All entries are TIMEOUT/OPEN, with no basis verdict. Round-2 msolve peaks were23,260,020KiB for129 and98,170,236KiB for136, below their180GiB limits. The observed obstruction was bounded computation time; these runs did not report allocation failure.

All full c=1 jobs preserve the declared complete direct generator lists and all remaining coordinates. Singular runs use Q and dp; msolve0.10.1 runs use p=1073741827, grevlex,16 threads, -g2, linear-algebra44, and a2,000-pair batch in round2. Modular output is only a signal; the msolve first-prime output is never relabelled exact Q. The three77 torus branches are the complete proved cover, but timeouts on them establish no cover emptiness. The slimgb variants change only std(I) to slimgb(I); exact rational unit/nonunit and lifted-identity controls pass.

Final custody is in `resume-r2/execution-custody.json`, `run-summary.json`, and the two subtask disposition records. They retain exact commands, variable and generator orders, fields, input and executable hashes, actual return codes, time/RSS, output hashes and cancellation causes. The final `resume-r2/final-custody.sha256` manifest binds the lane artifacts and is mechanically checked. Positive UNIT promotion requires a valid exact-Q computation or a rational original-ring identity; no such result occurred. This lane certifies zero class kills. The four first-power obstructions are complete; higher-power membership and all saturation claims remain OPEN.

Both owned workers were terminated with `bash ops/fleet/fleet.sh term <ID>` after harvesting: `.67` first, then `.86`. The final EC2 record `resume-r2/owned-instances-final.json` confirms TERMINATED for both exact IDs. All33 status-recorded invocations are finished and all their declared input/output hashes match. Operational cutoff: 15:14:00Z (54m30s in round2), within150min. No ledger, jc2-lean, ideation, or other-lane worker was changed. The frozen draft remains byte-identical to its charged hash.

