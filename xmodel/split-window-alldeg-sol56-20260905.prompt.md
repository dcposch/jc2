# THEOREM lane (OPEN[SPLIT-WINDOW-CLASSIFICATION] → a finite-window THEOREM for all degrees): the first-separation ledger (frozen) leaves the ES leaf (u_s≥2, early split ρ<v_s/u_s) as a typed obligation per (ρ, root partition), and 17(iiiiii) proved for the single (99,66) row that TWO exact necessary conditions on a split face, run over every (δ,partition) pair in the detector window, kill 54/66 charts and leave exactly the 12 triage survivors. TASK: make that screen an ALL-DEGREE theorem. (1) STATE the finite window precisely: for a Moh datum (n,m; M; d; V; s; u_s,v_s) with u_s≥2, which rational ρ<v_s/u_s and which partitions of the u_s minor roots can realize a first separation (cite Moh's contact/characteristic constraints pp.183–194 and Xu 1604.07683 §7 — Xu Cor 7.5 excludes the full u_s-distinct split below a strict cutoff; the PARTIAL partitions are the gap); prove the window is finite and give its size as a function of the skeleton; (2) STATE and PROVE the two split-face necessary conditions of 17(iiiiii) in general (not just (99,66)): what exact identities must the common leading form / the split face satisfy at radius ρ — write them as explicit polynomial conditions on the face coefficients, with the group element fixing any normalization (FALLACY-v2); (3) IMPLEMENT the general screen (box/lib/split_window.py: skeleton → the window → the surviving (ρ,partition) list with the killed ones' certificates) and RUN it on every u_s≥2 row of the frozen census n≤200 (box/moh_skeleton_full.py) — report the survivor counts per row and whether the survivor set has a uniform description (e.g. always the maximal-contact partitions); (4) VERDICT: the ES obligation reduced to an explicit finite list per row (THEOREM + tool), or exactly what remains. The 296 atlas complements should map onto this list — say how. ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/split-window-20260905/.
Report: xmodel/split-window-alldeg-sol56-20260905.md
Seal (<!-- BODY-END -->); 15-25KB; 150 min.
charged_input=xmodel/first-separation-lemma-sol56-20260905.md
charged_input=xmodel/g9966-n1-batch3-opus5-20260903.md
charged_input=xmodel/prop63-radius-gate-opus5-20260905.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/split-window-alldeg-sol56-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
43fe44eb8bebb46c23b612d586f266c73e4d632a22835a6324c4497e129aba1c  {{LANE_INPUTS}}/first-separation-lemma-sol56-20260905.md
c9f853dc490dba611d8b229aea43d293a7bcbfee151c6c1f16b4655bc676c545  {{LANE_INPUTS}}/g9966-n1-batch3-opus5-20260903.md
2fa1d334db58310aaa0e9471d6bc2ac955ffa3066e1bf571a9482f831aece1d7  {{LANE_INPUTS}}/prop63-radius-gate-opus5-20260905.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
