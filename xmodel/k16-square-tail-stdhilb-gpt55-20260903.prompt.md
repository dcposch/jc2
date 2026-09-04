# Compute lane (Card A of the Opus round submission, coordinator-adopted): move the K = 16 ray past t = 7 with a Hilbert-driven Gröbner computation — test "the t tail rows T_{t,t..2t−1} form a homogeneous system of parameters (hsop) of S_t = A_t[b₄, q_{2,0..t−1,0}, b₃] with weights wp(1, 2, …, t−1, t+1)" at t = 7 and t = 8, using the PREDICTED complete-intersection Hilbert series Π_{d=2t+2}^{3t+1}(1 − s^d) / Π_j(1 − s^{w_j}) to guide Singular's std (std(I, hilb, weights)); predicted lengths L_t = 2·binom(3t+1, t−1): 90, 572, 3640, 23256 at t = 3..6 (measured by Sol, 17(vvvv)), 149226 at t = 7, 961400 at t = 8

OPERATIONAL: skeleton first; every job in the FOREGROUND with `timeout
3000`; never end the turn with a job running; ≤ 4 cores, ≤ 24 GB. Inputs: the
banked terminal driver (charged: box/k16terminal-*/ and box/k16hilb-20260903/;
the terminal rows T_{t,k} are generated there — reuse the generator, do not
re-derive), the properness instrument 17(kkkk) (a modular dim = 0 of the
homogeneous ideal is a char-0 certificate; the LENGTH may differ mod p).
MANDATORY CONTROLS (a guided std with a WRONG series returns a wrong basis
silently — no result is reported without all five): (i) positive control at
t = 5, 6 reproducing lengths 3640 and 23256 (mod a good prime, both fibres at
split t); (ii) after every guided run, NF(T_{t,k}, G) = 0 for every tail row
k = t..2t−1; (iii) vdim(lead(G)) = predicted L_t (report the actual number);
(iv) negative control at t = 2, y = 1/5 where dim I_{2,+} = 1 — the guided run
must NOT return dim 0; (v) a deliberately perturbed series must produce a
detectable failure in (ii) or (iii). Task: (1) build S_t and the tail ideal at
t = 7 (mod a good split prime, a root of H_t as in the charged drivers; both
fibres), run the guided std with the predicted series, then dim, vdim,
controls (ii)–(iii); (2) same at t = 8 if t = 7 completes within budget;
(3) ALSO run the FULL cone ideal I_{t,+} = ⟨T_{t,1..2t−1}⟩ at t = 7 with the tail
Gröbner basis as a starting point (the tail is an hsop ⇒ dim I_{t,+} = 0 for
free, since I_{t,+} ⊇ tail — state this implication explicitly: an hsop
subideal of dimension 0 forces the big ideal to dimension 0, so (V0) at t = 7,
8 follows from (1)–(2) alone; then (8.1) and (T) at t = 8 via the banked CONE
chain — say what is promoted at each index); (4) record wall/RSS per index;
(5) interpretation per the card: dim 0 + vdim = L_t at t = 7 and 8 ⇒ SQUARE-TAIL
is the right uniform statement (the tail is a complete intersection with
degrees 2t+2..3t+1); dim > 0 or a control failure ⇒ (V0) refuted as a uniform
statement at that t — report exactly. Verdict: PROVED-HERE at t = 7 / t = 8
(modular, promoted to char 0 by properness for dim = 0) / TIMEOUT / REFUTED;
FALLACY-v2 applies. ≤ 170 min; no ledger edits; no jc2-lean; no ideation-*
files; no in-progress lane reports. Drivers to box/k16stdhilb-20260903/.
Report: xmodel/k16-square-tail-stdhilb-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-20KB; 170 minutes.
charged_input=xmodel/k16-hilbert-regseq-sol56-20260903.md
charged_input=xmodel/k16-properness-gate-opus5-20260903.md
charged_input=xmodel/k16-t11-cone-gpt55-20260903.md
charged_input=xmodel/k16-terminal-proof-fable5-20260903.md
charged_input=FALLACY-v2.md
charged_input=box/k16hilb-20260903/extract_initial_ideal.py
charged_input=box/k16hilb-20260903/t5_mod_p1009_b1_full.sing
charged_input=box/k16hilb-20260903/t6_mod_p1009_b0_tail_t.sing
charged_input=box/k16hilb-20260903/emit_preexpanded_cone_job.py
charged_input=box/k16hilb-20260903/legacy_t7_hilb.sing
charged_input=box/k16hilb-20260903/t3_exact_stated_tplus2.sing
charged_input=box/k16t11-20260903/top_tail_fast_recurrence.py
charged_input=box/k16cone-20260903/terminal_laurent_model.py
charged_input=box/k16cone-20260903/terminal_array_recurrence.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/k16-square-tail-stdhilb-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
69ea2475c0471ff2254d39d177f35029068d31fea53b29ba7bd35565ec9c29e7  {{LANE_INPUTS}}/k16-hilbert-regseq-sol56-20260903.md
f4d071a18cff25c4bdade4508f53c58bc39d20a26907fa619410622bfb91ccf6  {{LANE_INPUTS}}/k16-properness-gate-opus5-20260903.md
6e0dcef2d78c1956f471b4f37bbe42952edd94194ae5e36258f4df5ad8d77e6e  {{LANE_INPUTS}}/k16-t11-cone-gpt55-20260903.md
16d5112ae6ed9a6de0c504b11df2e19c97ed031a1715a3916fd8d207cdf0d961  {{LANE_INPUTS}}/k16-terminal-proof-fable5-20260903.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
fff2edc38c459ef6d93af06dca64627f5c1904a6e33e94256e9a8dd771f283c4  {{LANE_INPUTS}}/extract_initial_ideal.py
32948deb16752304d3587e2c2f99b87675cbc42eba7bfc3e95f803f6286214a4  {{LANE_INPUTS}}/t5_mod_p1009_b1_full.sing
d57c1bda23ad6ce16daaa69c7dc02a9ea22894b8f583b551e26ea698f2edc9e5  {{LANE_INPUTS}}/t6_mod_p1009_b0_tail_t.sing
28e53f84eb470e6556aca430c2bce32530e71dbf245810e431ec75125095bcfb  {{LANE_INPUTS}}/emit_preexpanded_cone_job.py
deca4771c5fab8dda6b84daada05ee3e7b71329f7ffc7391a7a79190904889c1  {{LANE_INPUTS}}/legacy_t7_hilb.sing
0cb8bdffb12f48da02483cae28b44efa2382e257b5593284d98d2610d9701864  {{LANE_INPUTS}}/t3_exact_stated_tplus2.sing
ecda7caa7d5def840ca9190baf294249ea33efb65c57f3b6ef0f88cb6d4e0d61  {{LANE_INPUTS}}/top_tail_fast_recurrence.py
53b9b3b43eaa067f4636df75dc6092fa74a1b3ee381ddac9abb53dcd0530c42e  {{LANE_INPUTS}}/terminal_laurent_model.py
8a935838ac01731110efd5f36652cae3d66bd00ffa23ae4450cdadaa41438001  {{LANE_INPUTS}}/terminal_array_recurrence.py
```
