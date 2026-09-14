# Active-variable ring variant

`active_ring_backend.py` implements the same normalized full characteristic block while performing its first four monic divisions in a smaller polynomial ring. It does not alter the running original backend or specialize a source coordinate.

The divisor and first dividend depend only on the actual variables occurring in h and B2, together with target_a and target_b. The implementation closes that dependency set through any named tower definitions. It checks every token against the declared polynomial generators and ordered definitions. The active ring is Q[z,t,active parameters], with z first and the same monic leading term. All four quotient/remainder identities are checked there.

After division, the code declares the complete original ambient ring, including every omitted source A3 coordinate, all five target coefficients, both leader coordinates, all separation/localization coordinates, and every otherwise unused free coordinate. It applies Singular imap to h,D,H,v and all eight quotient/remainder polynomials. An explicit ideal of the ordered active generators is mapped and each image is compared with the intended full-ring generator. This is an injective polynomial-ring extension, not an evaluation. Source h and D are then independently reconstructed in the full ring and compared with the mapped images; the shifted H and v identities are also checked. The active ring is released only after these checks.

Only then does the backend construct C,V,upper,digit,low and extract all the original characteristic and source rows. The emitted metadata records both ordered generator lists, the source-to-target index map, the generators omitted only during division, source-expression hashes, the original backend's full script hash, and the final variant script hash. The base generator order and full source ambient ring remain exact, regardless of whether a variable happened to occur in a division polynomial.

`active_ring_controls.py` compares the original and active-ring backends on an attained nonunit example, a version using a named tower definition, and the cone vertex unit control. The full-ring reduce-one, dimension and basis-size triples agree exactly in all three cases. Every generator and source-image check passes. A corrupted generator image triggers the intended explicit error. Production readers reject that diagnostic rather than interpreting any subsequent result marker.

The D108 stage0 first-division profile compares 654 full generators with 369 active generators on the same immutable emitted polynomial input. Each job had a 16GiB address-space cap and a 180-second limit. Neither completed the first division in that limit, and neither reported a mathematical result. Actual ps snapshots at 49 seconds showed full/active RSS 5,265,844/2,325,720 KiB; at 107 seconds they showed 7,599,056/3,329,708 KiB. These are snapshots, not maximum-RSS claims. Both owned process groups were stopped when the profile expired. Artifacts are `active-ring-profile.json` and the paired scripts/logs.

The coordinator then authorized a full active-ring run on the front-preprocessed `(99,66)` delta2 stage0 input. It ran on the already provisioned fleet worker, with a 48GiB address-space cap and a 1200-second timeout, under `front99-delta2-stage0-active/`. The active/full generator counts were 299/583. It ended as **COMPUTE_BOUND_OPEN** after 1200 seconds, still in its first division, with no parser/CAS error and no mathematical result. At elapsed 18m34s, ps recorded RSS 47,104,544KiB; this is a snapshot, not max RSS. The runner stopped its owned process group and the final artifacts were pulled. This run used the preserved backend snapshot under `run-code-front0/`; later revisions releasing division containers were not silently substituted into its receipt.

The front preprocessing was independently checked against `front-band-lemma.md`. Its B2 t<=27 and A3 t<=56 equations are radical consequences of the existing degree and source rows, not new gauges or assumed valuation bounds. It acts on actual source-position images and keeps the full original characteristic block. In particular the r27 argument uses the source equality coefficient at (27,27); without that printed source consequence the possible tau*z^27*(1+z)^5 term could not be removed.

No proper ideal, unit ideal, or necessary-chart point follows from memory reduction or from these bounded profiles. A complete controlled result still needs the full coefficient extraction and exact ideal computation after the active-to-full embedding.

The next version releases the Singular list/matrix/ideal containers immediately after extracting each quotient/remainder, and releases each old-ring polynomial immediately after its full-ring image is created. Re-running all three positive/negative backend comparisons and the deliberately corrupted generator-map test passed. These lifetime changes alter no mathematical equation. Its SHA-256 is recorded by `active-ring-controls.json`.

## Audited residual translation gauge experiment

The stage8 experiments under `../active-gauge/` compose the completed generic source input with the proved front consequences and then apply `jet0 -> 0` to every actual polynomial image and every residual row. This is the globally covering orbit slice proved in the frozen `translation-proof.md` and `minor_gauge-final-audit.md`, not an unexplained point specialization. The input metadata binds both proofs and their two independent PASS control receipts by SHA-256, and binds the original input through the front-parent hash and gauge-parent hash.

The four historical gauge files also passed a mechanical `sha256sum -c` against the entries extracted from the historical `artifacts.sha256`. That full manifest hashes to `7cc2be6ab6556558cda34caba76a79dc46242d96f34b9d45d8cbdadc29f1064f`, exactly the hash printed at line192 of the frozen charged99 report. `gauge-source-binding.json`, the extracted manifest and the check log record this chain; current filenames alone were not used as historical authentication.

The source action is simultaneous diagonal translation `Q_q(x,y)=Q(x+q,y+q)`. Its inverse and centre transport are those in the frozen proof: jet0 becomes jet0-q; u remains u; minor_a2 or v becomes that coordinate minus q*u; rho/c and Hc_11_0 are unchanged. Only jet0 is removed from the free-generator list. No other centre, target scalar, separation parameter or source constant is pinned.

The new characteristic block respects this old gauge. For fixed scalar a,b,c,d,e, the target polynomial in translated F/G is the translated target polynomial. Hence an exact total-degree bound and its homogeneous leading form are invariant; the leader lambda remains the same scalar. The full five-target family is retained. The source action increases normalized t order and preserves z degree, so the already proved front cut is preserved as well. It follows that the augmented source/characteristic locus is the jet0=0 locus times the free translation line. Its properness or emptiness can be decided on this slice, with the stated dimension adjustment.

`../active-gauge/gauge_extension_control.py/.json` verifies target-family covariance symbolically with all five scalars free, homogeneous-top invariance and the inverse. Its separate exact identity control verifies the coordinator's proposed lifted remainder formula: after V=3U/8, the difference between the depressed characteristic polynomial and `(3R/4+p)H^2-vUH/8+vR-9U^2/64+pv+q` is exactly `(v^2-UH-R)(3H^2/4+v)`. This controls a possible no-division backend; the stage8 active jobs still use the audited four monic divisions.

Both gauged stage8 inputs retained the complete characteristic block. Front reduction used 23 rational pivots and had zero residual rows in each branch. The gauge changed 23/25 mapped coefficient images and removed exactly one free generator. The resulting active/full generator counts are 268/494 for delta2 and 266/492 for delta52. Both ran on the existing fleet worker with separate48GiB address-space caps and1800-second time limits. Both ended **COMPUTE_BOUND_OPEN** at1800.004/1800.003seconds, still in their first division, with no parser/CAS error. At elapsed27m57s the RSS snapshots were37,967,908/27,255,540KiB; these are not maximum-RSS measurements. The final receipts were pulled and all six owned runner/process-group/Singular PIDs were confirmed absent. No unit, properness result, or point follows from these attempts.

## Stronger derived front inputs, kept separate from those running jobs

The cubic argument in `../cubic-front-improvement.md` proves H0^2 divides
the cube of the first D band. It safely improves99 to D<=28,C<=58 and
108 to D<=32,C<=66. Independent audit found no missing cross term: every
lower R band vanishes first, and the scalar terms enter strictly later.

`quartic-front-improvement.md` then derives H0^3 dividing the fourth power
of that band, using the first low H-adic coefficient. Its exact scalar is
5/192. This independently checked proof improves99 to D<=29,C<=60.
The controls explicitly retain the next99r30 and108r33 leading shapes;
they are leading-band controls, not full-chart points.

The source agent's `../stage-specific-front-audit.md` and
`../d108-stage-front-audit.md` add the actual offset-one D1 moment rows.
At W190 the99 face is pi*S(pi^3), deg S<=10, and the required order13
forces it to vanish. At W277 the108 face is pi*S(pi^4), deg S<=8, and
required order12 does the same. Both actual frozen source maps and ranks
were checked. This justifies99 D<=30,C<=62 and108 D<=33,C<=68 for
stages1–8. Stage0 does not acquire these extra source moments. The next
W193/W281 coefficient images are nonzero, so no further cutoff follows.

New99 stage8 inputs are `../active-gauge/inputs/{branch}_stage8.strongest.json`.
Their parent chains include the original stage8 state, old proved front,
audited gauge, quartic cut, and stage-specific cut. The last two reductions
use28 and19 rational pivots, respectively, with zero residual rows; final
free-coordinate counts are444/442. They retain all original characteristic
rows and all surviving source images. The independent
`verify_stronger_front_inputs.py/.json` checks every rational leader, every
raw row after the graph map, every source coefficient image, declared-ring
closure, and the asserted t cutoffs. Both inputs were pushed to the existing
worker with matching SHA-256 hashes for the coordinator's later backend.
They do not overwrite the old input hashes used by the active-division jobs.
