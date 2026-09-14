# source-support-closeout-20260905

Closes the three gate-§4 residuals of `xmodel/first-separation-gate-opus5-20260905.md`.
Report: `xmodel/source-support-closeout-opus5-20260905.md` (sealed, body 16386 B).

## Artifacts

- `inputs.sha256`, `inputs.check.log` — 5/5 charged inputs OK (manifest built from the
  `.run.v2` receipt with awk, checked with `sha256sum -c`).
- `alpha_beta_regression.py|.json|.out` — OPEN[OLD-CAP-REGRESSION-alpha/beta].
  72 blocks x 12 fibres. Control: `G_i \ uncapped-D1` == frozen `*_added_beyond_raw`
  of `support-completion.json`, 72/72. Gate sec 3.d h-block replicated exactly.
  VERDICT: cap-refuted = 4 fibres / 22 blocks (V1_1, V1_3, V4_3 of the (16,12;6,13;ell=3)
  class in every block; V4_9 at h only). The other 11 fibres / 66 blocks fail only against
  the uncapped D1 floor -> NORMALISATION-GAP, not refutation.
- `q_is_t1_witness.py|.json|.out` — OPEN[Q-IS-T1]. M_1'=-m' 12/12, ell=v_s-u_s-1 12/12,
  M_s'<=n'-2 12/12.
- `prop51_ell_validate.py|.out` — OPEN[PROP51-ELL-EXTENSION]. Appendix II p.207: ell-form
  4/4, ell=0 form 0/4 (the printed table REFUTES the unshifted Prop 4.4 condition (3)).
  12 frozen fibres 12/12.
- `p{29,34,35,36,46,58,59,60,61}.txt`, `pg{26,29,30,31,32,34,35,36,58,59}-*.png` — page
  extracts/renders. PDF page = printed page - 139.

## Key printed lines found this lane (not in the gate)

- **p.169 Remark**: a SECOND ell-Remark, for Proposition 4.4, condition (6) -> (6)*
  `ord T_r^psi(sigma) = (-mu_r+M_r-n)lambda - 1 + delta - l`. Only two such Remarks exist
  in the paper (p.169 for 4.4, p.171 for 4.6) — exactly the two tools p.173 names for Prop 5.1.
- **p.165** (Prop 4.2 proof): `lambda < (-1+delta)/(n-M_{r+1})` <=> "the LHS of equation (1)
  of Prop 4.1 with h = T^psi_{r+1} has a smaller formal order" — so that `-1` is the Jacobian
  order, and it must become `-1-l`. Moh does NOT print this; p.207 forces it.
- **p.198** (Prop 6.3 proof, conclusion (3)):
  `J_{gamma,pi}(gbar(sigma), Tbar_1^psi(sigma)) = J_{gamma,pi}(x,y) J_{x,y}(g, T_1^psi(f,g))`
  — the descended pair IS (g, T_1^psi), so Q' is the image of T_1^psi by construction.
- **p.185**: `deg T_1^psi(f,g) = deg_y T_1^psi = -M_1`.

## New typed OPEN

`OPEN[PROP42-ELL-CONDITION3]` — printed/complete justification for Prop 4.2's condition (3)
under J = x^l. Everything downstream already needs it.
