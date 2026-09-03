# Instrument lane: a NATIVE preprocessing pipeline for the large two-point charts — Q*-pivot affine elimination, positive-grading LP, forced-nonzero torus slice, base-polynomial factorisation and field pass — executed inside Singular (or a compiled sparse exact solver), replacing the sympy parser that cannot digest the native emitter's 42–180 MB row files; then run it on the (25,15; 21; 2; 2) strata (135–137 unknowns) and report

Context (banked, AUDIT deltas 17(kkk), (bbbb)): the native emitter
(box/emitter-20260903/, charged) emits the corrected two-point strata systems
in seconds; on (25,15) the three strata have 517 saturated rows over 135–137
unknowns; direct modular standard bases time out at 20 min (2.4–4.6 GB) and the
charged sympy preprocessing (box/bigrows-20260903/preprocess.py; the K = 16
triangular_preprocess.py) times out parsing the row TSVs before any pivot;
the K = 16 experience (17(ww), (ddd), (www)) shows that Q*-pivot elimination +
grading + slice + field pass reduces such charts by an order of magnitude
before Gröbner (36 → 6 rows; 45 → 8; 54 → 10). Task: (1) implement
box/preprocess-native-20260903/prep.sing + prep.py: read the emitter's row
TSV directly into a Singular ideal (or generate it in-process from
emit_chart.sing — preferred: keep everything in one Singular session);
implement Q*-pivot elimination natively: repeatedly find rows that are affine-
linear in some variable with a constant (Q*) coefficient, substitute (Singular
`subst`/`reduce` with the pivot as a polynomial map), record the pivot and the
ring map; then the grading: extract the monomial exponent vectors of the
residual rows and solve the positive-weight LP (a small python LP over the
exponent matrix is fine — the data are small once rows are homogeneous;
export exponents from Singular); the forced-nonzero variable from a displayed
c-equation; the torus slice (set to 1; record the covering argument); the
univariate base row (factorise in Singular: `factorize`), the field pass over
each irreducible factor (Singular `minpoly` / ring over the algebraic
extension); final `std`; (2) VALIDATE on the K = 16 t = 3 and t = 4 charts (must
reproduce 36 → 23 → 6 rows → [1] and the Q(√15) eight-generator [1]) and on
(33,22; 30; 8; 1) [3] (28 unknowns, [1]); report timings; (3) run on the (25,15)
strata [3], [2,1], [1,1,1]: report per stratum the pivot count, residual size,
grading found or not, the base row, the field(s), and the final verdict
(SATURATED-EMPTY with the covering chain / COUNTING-BOUND with the exact
stuck system / a point and a direct J check, REPRESENTATIVE); ≤ 25 min per
stratum, 4 cores; (4) if time remains, (24,16; 17; 2; 5) smallest stratum;
(5) verdict + what the pipeline enables (the remaining large rows, the
(99,66) joint chart bands); FALLACY-v2 applies (every division by a
parameter-dependent pivot must be a proven unit or branch on zero). ≤ 150
min; no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane
reports. Drivers to box/preprocess-native-20260903/.
Report: xmodel/preprocess-native-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 150 minutes.
charged_input=xmodel/emitter-native-gpt55-20260903.md
charged_input=box/emitter-20260903/emit_chart.py
charged_input=box/emitter-20260903/emit_chart.sing
charged_input=box/emitter-20260903/validation.json
charged_input=xmodel/bigrows-preprocess-gpt55-20260903.md
charged_input=box/bigrows-20260903/preprocess.py
charged_input=xmodel/k16-t3-gate-gpt55-20260903.md
charged_input=xmodel/k16-t4-normalizer-gate-gpt55-20260903.md
charged_input=box/k16t3-20260903/preprocessed/triangular_preprocess.py
charged_input=box/k16t3-20260903/t3/t_order_system.py
charged_input=box/chartfix-20260903/shape.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/preprocess-native-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
455d42bb1002093427976f67d5c3351fd37b6995c0a4accb7b666b586e2711cd  {{LANE_INPUTS}}/emitter-native-gpt55-20260903.md
28cf67fd5386a9fef69094f3f00c4944a4930c79d4c464df170a9513a1224e66  {{LANE_INPUTS}}/emit_chart.py
3c8075b59d81ec996cfb553df2edd4f1fb55f92d33fb9cec5ee1e3e7dd999f2f  {{LANE_INPUTS}}/emit_chart.sing
ddc23e03e84e3462add743862bf5af459db7cd1d993d4c6f73b7a5f2799d3299  {{LANE_INPUTS}}/validation.json
3f994067f8149636fc81e57e98122261dc1435d4c0ac77f266893e58646c5273  {{LANE_INPUTS}}/bigrows-preprocess-gpt55-20260903.md
67b3735d27d8b92af2bf091566a14f9b2f49163577f51d54da751a76d22b2f2a  {{LANE_INPUTS}}/preprocess.py
5593aa5443dd755cadedca4b0d284a3dec4048f7cd5822da576587552f36aba6  {{LANE_INPUTS}}/k16-t3-gate-gpt55-20260903.md
e868a7f2df3814caf1847411918c17cbf8e71688779819fd4764d70e9d86ae83  {{LANE_INPUTS}}/k16-t4-normalizer-gate-gpt55-20260903.md
f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93  {{LANE_INPUTS}}/triangular_preprocess.py
e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28  {{LANE_INPUTS}}/t_order_system.py
ba25cd10fa5cc998017688db455094bcd3b7a8e870085dd2db64fb4f66b098de  {{LANE_INPUTS}}/shape.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
