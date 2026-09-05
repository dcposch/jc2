# first-separation-gate-opus5-20260905 — working notes

Report: `xmodel/first-separation-gate-opus5-20260905.md` (sealed,
body_sha256=6144f7cc3688d1fe3a997d05f8b6046e91b4bb858be35d8a307d4182c106ddb3).

- `inputs.sha256` — manifest built with awk from the run receipt; `sha256sum -c` = 5/5 OK.
- `verify_gate.py` / `verify_gate.json` — Appendix II terminal radii (4/4 match), Appendix II
  coefficient counts vs total-degree counts, per-class `d` and `|G_1|`, negative control
  `h = y(y-x^2)^3`.
- Page evidence (PDF page = printed - 139):
  `pg44-44.png` p.183 Prop 5.4 + `delta_i = -1/(n-M_i-1)`
  `pg46-46.png` p.185 degree-drop automorphism, `deg T_1^psi = deg_y T_1^psi`, Lemma 5.3
  `pg55-55.png` p.194 the (FS) top form, Lemma 6.1, eqs (8)(9)(10)
  `pg35-35.png` p.174 Prop 5.1(2) + the effective-characteristic Definition-Remark
  `pg32-32.png` p.171 the `J = x^l` Remark, condition (3)*
  `pg40-40.png` p.179 Definition 5.1 + "minimal disc D_s ... contains all roots"
  `pg-61.png` / `pg-62.png` pp.200-201 Theorem (1)-(7) then bounded search (1)-(13)
  `pg68-68.png` p.207 Appendix II table and coefficient counts
- `pdfNN.txt` — pdftotext scrapes used only for navigation; the OCR mangles formulas, every
  quoted line in the report came from the rendered image.

Cross-check that mattered: `d` and `|G_1|` recomputed from `(n',m',M_s',ell)` alone agree with
`box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/support-completion.json` on
12/12 fibres.
