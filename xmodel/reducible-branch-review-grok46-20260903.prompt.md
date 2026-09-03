# Hostile review lane: REDUCIBLE-BRANCH REPRICE — is the exact machinery H2-free; does N_min = 6 hold on the reducible branch; the NONPROPER theorems; the measured recovery of the H2 kill

The charged Opus report (`reducible-branch-reprice-opus5-20260902.md`,
fd1f383a; AUDIT integration #17 delta (g), PROVED-HERE/UNREVIEWED +
MEASURED) claims: (1) SCOPE AUDIT — no item of JAC-FIBRE, FRONTIER-EXACT,
DETECTOR-NULL, D1-PIN, D1-STAR, PIN-NOT-CEILING, the integrality filter,
Moh condition (15), HARMONIC-BOUND or N-CEILING uses H2 (A_F irreducible);
H2 enters the charged reports only as the clip of the integrality window
to [4,16]; load-bearing instead are (GEN), (MIN) and Moh's tower with
M_s = n − 2 (checked by perturbation: off M_s = n − 2 the r = 1 gap is
(1−δ₁)(1 − (n − M_s − 1)) ≠ 0 and N is only bracketed); (2) the N ≤ 5
closure is H2-FREE (its dependency chain quoted), so the reducible branch
has the same frontier N_min = 6; (3) REDUCIBILITY: the branches of a
generic fibre partition into PROPER (e·Σ_B V₂(B) roots of bottom-major
discs) and NON-PROPER (all in minor discs, each contributing 0 to N);
every datum distinguishing A_F reducible from irreducible (limit points
(a₀, c₂), their monodromy orbits, component degrees) is carried by the
non-proper block, so the pinned N is blind to reducibility by
construction; (4) NEW THEOREMS: NONPROPER-COUNT (# non-proper branches
= D − eΣ_B V₂(B) = e(K − ΣV₂), skeleton-determined); NONPROPER-RATE
(ord_t(f(τ) − a₀) = δ⁰ − 1 + ord_t J at every branch); STRICT-FRONTIER
(δ⁰ = 1 impossible for Keller); NONPROPER-CAP (n_A^Y ≤ e(K − Σ_B V₂(B)));
113 exact checks on 19 non-Keller rows; (5) MEASURED (D ≤ 120, (UNI),
N ≥ 6, no upper window): 98.94% of assignments / 59.79% of groups die
vs the H2-clipped 98.98% / 60.04%; on the calibration lane's proved
(10)₁ gate 63.40% H2-free vs 63.69% H2; on its RECONSTRUCTED full gate
the unconditional integrality filter kills nothing beyond the frontier
(9.41% vs 13.94%); no degree emptied; (6) VERDICT (c), partially
subsumed: the census + pinned-N filter is ONE program for both
branches; the reducible residual OPEN[COMPANION-R0-REALISATION]
concerns the non-proper block.
Context you must hold: the census those measurements ran on is the
(1)–(7) SUPERSET (integration #17 delta (h): the true (1)–(13) space at
48 ≤ D ≤ 120 is 1,189 groups, 670 alive at N ≥ 6; box/moh_skeleton_full.py
implements it). The report's PERCENTAGES are therefore about the
superset; say explicitly which of its claims survive unchanged on the
true space and which must be re-measured. The Moh 1983 page images are
NOT available on this machine; use the verbatim transcription of Moh
(1)–(13) and Def 5.1 in census-rebase §1 (charged) and the OCR text
box/depth-drivers-20260902/moh.txt (display formulas dropped) only.
Your task, hostile: CONFIRMED / GAP / REFUTED per numbered item with
line and repair. Mandatory: (a) redo the scope audit yourself — for each
of the ten named theorems quote the line in integration17 / d1-subtree /
its review where the hypothesis set is stated and say whether H2 is
consumed anywhere in the proof (not only in the window clip); (b)
reprove NONPROPER-COUNT and NONPROPER-RATE from JAC-FIBRE and Moh's disc
structure; find the exact hypothesis under which "non-proper branches
lie in minor discs" holds and whether a non-proper branch can sit in a
bottom-MAJOR disc (which would break the partition); (c) STRICT-FRONTIER:
prove or refute δ⁰ = 1 impossible for a Keller pair; (d) NONPROPER-CAP:
is n_A^Y correctly identified with the number of non-proper branches
at generic c₂ (the horizontal degree of A_F), and does the cap consume
irreducibility of A_F anywhere; (e) rerun nmin_reprice.py,
nonproper_count.py, nonproper_rate.py (charged), then REPEAT the
N_min = 6 (UNI) measurement on the true (1)–(13) space with
box/moh_skeleton_full.py (D ≤ 120; report groups / killed / alive and
whether any degree empties) and compare with census-rebase §6; (f) the
perturbation check of M_s = n − 2: reproduce the r = 1 gap formula;
(g) say whether verdict (c) is the right typing or whether (a)/(b)
["fully subsumed" / "not subsumed"] is forced by your findings. Typed
verdict block; promotion recommendation per item; bounded quantity of
every OPEN you raise (ops/open_collision.py contract). Desk-scale CAS
(< 20 min one core, < 4 GB); do not edit canonical ledgers; do not
inspect jc2-lean; do not read any ideation-20260903T* file.
Report: xmodel/reducible-branch-review-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; the skeleton you
write first must NOT contain it); bounded writes; target 20-30KB;
90 minutes.
charged_input=xmodel/reducible-branch-reprice-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/moh_skeleton_N.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/reducible-reprice-20260902/nmin_reprice.py
charged_input=box/reducible-reprice-20260902/nonproper_count.py
charged_input=box/reducible-reprice-20260902/nonproper_rate.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
fd1f383a2882712ad2a288b2b023b464529570652cbd889778cd665c187c96be  {{LANE_INPUTS}}/reducible-branch-reprice-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
b6349f5a76fd56425b47efa009fbbb216f50498a94356cc1ffd62449c54519a5  {{LANE_INPUTS}}/nmin_reprice.py
c76f5b8e6bd16aca86c50b12259eb3066a25ba71aee8bbe55f6e0e39105d885f  {{LANE_INPUTS}}/nonproper_count.py
92ded32b61ac5d0fc5902a1982dd792822f8ec1c7fda268b334dbe8946746485  {{LANE_INPUTS}}/nonproper_rate.py
```
