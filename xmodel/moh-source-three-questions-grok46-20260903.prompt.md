# Source lane (fast, decisive): three questions on Moh 1983 page images — does Moh's Def 5.1 / p.200 Theorem require V_j >= 2 at major discs (MAJOR-MULT)? is (12)/(13) an exclusive disjunction forcing A_1 >= 2 (MOH-INCREMENT)? what datum does Appendix II use per row?

Context (charged; blind-round submission ideation-20260903T1015Z-opus5.md
§0–§1, measured on box/moh_skeleton_full.py): the conjunction
  MOH-INCREMENT  A_j >= 2 for every j = 1..s-1   (A_j = Moh's "increment"; when
                 A_j = 1 the automorphism t -> ω t of (8) is the identity and
                 (10)/(11) are vacuous)
  NOT-ALL-(11)   some j in {2..s-1} satisfies (10) (Prop 5.6 numerical shadow)
  MAJOR-MULT     V_j >= 2 for every j = 2..s      (the factor of p(π) selecting
                 a major disc is not simple) — SOURCE-UNVERIFIED
keeps all six p.202 rows, reduces the (1)–(13) survivors at n <= 100 from
658 to 51 rows / 13 classes, reproduces exactly the printed (75,50) residue
{M = (55,73), V_2 in {2,3}} and kills M_2 in {5,10,40,60} there, and EMPTIES
D = 105 (all three true D = 105 groups have V_2 = 1). The Moh PDF is at
refs/moh1983_jram340_configurations_of_roots.pdf (sha256 6c8847a8…; journal
page N = PDF page N−139). Render with pdftoppm -r 300 -f P -l P -png and READ
THE IMAGES (pdftotext drops display formulas).
Answer exactly these, with page/line quotes transcribed from the images:
Q1 (decides OPEN[MAJOR-MULT]). p.179 Theorem/Definition 5.1 (and Prop 5.2,
   5.3 pp.180–185; the Theorem on p.200 clauses (4)–(7); Cor 6.1 p.194): in
   the definition of a MAJOR disc and of the assigned integers V_i, is there
   any requirement that V_i >= 2, that the selected factor of p(π) be
   non-simple, or that a disc containing a single root be MINOR? Quote the
   defining sentence. State plainly: is MAJOR-MULT Moh's (PROVED-IN-SOURCE,
   with citation), a consequence of his definitions (derive it), or NOT in
   Moh (then it is a campaign CONJECTURE).
Q2 (decides MOH-INCREMENT at j = 1). p.188 l.1–13 and p.201 (12)/(13):
   is Moh's derived condition the EXCLUSIVE disjunction "A | n*V_2 and
   A ∤ m*V_2, or A ∤ n*V_2 and A | m*V_2" (so A_1 = 1 is inadmissible), and
   does the same sentence structure at (8)–(11) imply A_{r-1} >= 2 at every
   level (or is A_{r-1} = 1 simply a level that is not a characteristic
   exponent, i.e. excluded by the definition of the tower)? Quote.
Q3 (the shape of a uniform theorem). Appendix II (locate it; pp.203–212):
   for EACH of the six p.202 rows, in one line: what datum does the case
   analysis use that is not in {n, m, M_*, V_*} (e.g. approximate roots,
   the second point at infinity, a coefficient identity, a degree count of
   a remainder, a monomial-Jacobian transform via Prop 6.3/6.4)? Also: does
   Appendix II or §6 impose conditions at the SECOND point at infinity
   (the L_2 tower with v roots) — is there a second tower analysis anywhere?
Then REPRODUCE (fail-closed): run the three predicates on
box/moh_skeleton_full.py's census (drivers charged in
box/mohsieve-drivers-20260903/) and confirm or refute: 6/6 rows kept; the
(75,50) residue; 658 → 391 → 247 → 86 → 51; D = 105 empties; the emptied-degree
list {48,60,63,81,88,104,105,110,152,154} at 48 <= D <= 200; group counts
14,016 → 2,652 → 1,908. Report any discrepancy to the unit.
Typed block: per question PROVED-IN-SOURCE / DERIVED / NOT-IN-SOURCE with
citations; per measured number CONFIRMED / REFUTED. Bounded quantity of any
OPEN. Desk-scale (< 10 min CAS); do not edit canonical ledgers; do not
inspect jc2-lean; do not read other ideation-20260903T1015Z-* submissions
except the charged Opus one, and do not read other running lanes' reports.
Report: xmodel/moh-source-three-questions-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 60 minutes.
charged_input=xmodel/ideation-20260903T1015Z-opus5.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohsieve-drivers-20260903/moh4.py
charged_input=box/mohsieve-drivers-20260903/battery.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  {{LANE_INPUTS}}/ideation-20260903T1015Z-opus5.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
cdf5eeb7d9e40021642837805bf97c307fcfe8b2900ce50ec4a510e712d083d2  {{LANE_INPUTS}}/moh4.py
d6e40234299f21ba7c7c08433f5bc219f7f139003756ad90cebd05f29f251685  {{LANE_INPUTS}}/battery.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
