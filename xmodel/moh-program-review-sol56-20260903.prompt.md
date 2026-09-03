# Hostile review + source lane: CENSUS-REBASE second reader — Moh's (8)–(13) transcription, the 4.1x correction, the p.202 erratum, and OPEN[MOH-PROGRAM]: find the elimination Moh's program applied beyond the printed list

The charged Opus report census-rebase-opus5-20260902.md (fb137b92;
AUDIT integration #17 delta (h)) claims: (1) Moh 1983 pp.200–202 search
conditions (1)–(13) transcribed VERBATIM from the page images (§1.1–1.2),
with the symbol dictionary (A_{r-1} = reduced denominator of L·δ_{r-1},
L = lcm of the reduced denominators of δ_s..δ_r; (9) the division
V_r d_{r-1}/d_r = △A_{r-1} + □; (10) V_{r-1} ≤ △ for a factor π − a,
a ≠ 0; (11) V_{r-1} = jA_{r-1} + □ for the factor π; (12)/(13) the A_1
alternatives at r = 2; p.188's identity A_1 | (n*+m*)V_2 − 1); (2) the
calibration lane's reconstructed (10) is exactly Moh's printed (10)
(521,190 level-pairs, 0 exceptions) and its (10)_1 is EQUIVALENT to
(12)∨(13) (242,099 assignments, 0 discrepancies); (3) branch (11) was
missing and costs 4.1x: the true (1)–(13) space at 48 ≤ D ≤ 120 is 1,692
V-assignments / 1,189 groups; (4) ERRATUM p.202: the n = 75 bracketed
δ_1 = 1/3 is attained by no (1)–(7)-admissible skeleton; Def 5.1(3)'s 2/3
is right; (5) DECISIVE NEGATIVE: (1)–(13) as printed leaves 658 rows in
63 (n,m) classes at n ≤ 100 against Moh's printed 6 rows in 4 classes
(p.202 l.1–3 claims the table is the complete program output); every
stricter reading tried kills printed rows; the automatic/non-separating
conditions listed in §5; OPEN[MOH-PROGRAM] (652 excess rows);
OPEN[PROP-5.6-SHADOW] (NOT-ALL-(11): 1,189 → 969, empties nothing);
(6) the rebased programme §6–§8 (670 alive at N ≥ 6; D = 48 emptied;
66, 78 no skeleton; no D > 100 empties; D = 105 → 3 groups; D ≤ 200:
14,016 groups; s ≤ 5 fails at D = 192).
The GPT-5.5 review of the sibling calibration lane
(tf-calibration-review-gpt55-20260902.md, 5f56d980, charged) corroborates
the (8)–(13) transcription but did NOT read pp.181–189 or Appendix II.
The Moh 1983 PDF IS available: refs/moh1983_jram340_configurations_of_roots.pdf
(sha256 6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51;
journal pp.140–212 = PDF pages 1–73; p.201 = PDF page 62). Render pages
with pdftoppm -r 300 -f P -l P -png and READ THE IMAGES; the pdftotext
layer drops every display formula. Read at least pp.179–189 (Def 5.1,
Props 5.3–5.6), 194 (Lemma/Cor 6.1), 198–202 (the search, the table),
and Appendix II in full (pp.203–212 or wherever it sits — locate it).
Your task, hostile and source-first:
(A) REVIEW. CONFIRMED / GAP / REFUTED per numbered claim (1)–(6), with
    page/line and repair. Mandatory: re-transcribe (8)–(13) yourself from
    the images BEFORE reading §1.2, then diff; re-derive p.188's identity;
    confirm or refute the erratum (4) by your own enumeration at (75,50);
    rerun box/censusrebase-drivers-20260902/run_all.py (charged) and
    confirm the 1,692/1,189 and 658/63 counts; spot-check ten of the 658
    rows against (1)–(13) by hand.
(B) OPEN[MOH-PROGRAM] — THE MAIN CHARGE. Find the restriction beyond
    printed (1)–(13) that Moh's program encoded. Discriminator: it must
    kill 652 of the 658 rows at n ≤ 100 (at (75,50): cut M_2 ∈
    {5,10,40,60}, keep (55,73)/V_2 ∈ {2,3}) and keep all six printed rows.
    Work through, in order, with page citations: (i) Prop 5.3's
    construction of p(π) pp.181–185 — does the multiplicity structure of
    the bottom polynomial impose a condition on V_{r-1} beyond orbit size;
    (ii) Prop 5.5 and the proof that yields (12)/(13) — is there a second
    clause at r = 2 the printed list omits; (iii) Prop 5.6 — is
    NOT-ALL-(11) its exact numerical content, and does the r = 2 step add
    a branch datum; (iv) Cor 6.1 / Props 6.1–6.4 (minor discs) — any
    numerical condition beyond (7); (v) Appendix II — READ IT: what
    eliminations does Moh actually perform on the six rows, and is any of
    them a general numerical condition he simply did not print in the
    list (e.g. on the u, v split, on H = L_1^u L_2^v, on the second point
    at infinity, on m | something, on the Def 5.1(1) root counts at every
    level, on the sign/ordering of the M_i); (vi) the Abhyankar–Moh
    semigroup: is a semigroup/conductor condition on {n, M_1, …, M_s}
    (e.g. that the M_i generate the semigroup of a one-place curve, or
    the approximate-root inequalities) implied by (3)–(5) and used
    implicitly. IMPLEMENT every candidate you find in a copy of
    box/moh_skeleton_full.py (write box/mohprog-drivers-20260903/), run it
    at n ≤ 100 and report survivors vs Moh's table (fail-closed: a
    candidate that kills a printed row is WRONG), then at 48 ≤ D ≤ 200
    (groups, alive at N ≥ 6 via the pinned-N knapsack, degrees emptied,
    D = 105/108/112/117/120 counts).
(C) READING. If you find the elimination: state it as a theorem with
    Moh's proof located, type PROVED-IN-SOURCE, and say whether it is
    uniform in D (a candidate all-degree kill) or case-by-case. If you do
    not: state the bounded residual precisely (which of (i)–(vi) are
    excluded and which remain), and rank the remaining candidates.
Typed verdict block; promotion recommendation per claim; bounded
quantity of every OPEN you raise (ops/open_collision.py contract).
Desk-scale CAS (< 30 min one core, < 4 GB); do not edit canonical
ledgers; do not inspect jc2-lean; do not read any ideation-20260903T*
file or the in-progress reports of other running lanes.
Report: xmodel/moh-program-review-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; the skeleton you
write first must NOT contain it); bounded writes; target 30-45KB;
150 minutes.
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=xmodel/tf-calibration-review-gpt55-20260902.md
charged_input=xmodel/time-function-calibration-d48-opus5-20260902.md
charged_input=xmodel/delta-denom-gpt55-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/censusrebase-drivers-20260902/run_all.py
charged_input=box/censusrebase-drivers-20260902/survivors-D48-120.txt
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
5f56d980ed8deea3a7996dd8954d3a9ff4fdd7b2c75802ddb93e51a0afb02ded  {{LANE_INPUTS}}/tf-calibration-review-gpt55-20260902.md
db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a  {{LANE_INPUTS}}/time-function-calibration-d48-opus5-20260902.md
7355259f17d13edd8e309231b8573ed4c1429093b84a72628c33730827fe59ea  {{LANE_INPUTS}}/delta-denom-gpt55-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
792eb15e74932a084f3d3ecac6ea914d3cff965634b2c19b02e6264c0947e3c7  {{LANE_INPUTS}}/run_all.py
47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1  {{LANE_INPUTS}}/survivors-D48-120.txt
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
