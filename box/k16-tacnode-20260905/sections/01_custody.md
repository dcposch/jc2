## 1. Custody

The receipt `xmodel/k16-tacnode-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing each `charged_input_<i>_sha256=`
with its `_basename=` into `box/k16-tacnode-20260905/manifest.sha256`; `sha256sum -c` returned **4/4 OK** before any input
was opened (re-run at sealing: `input-verification-final.log`). No digest was retyped. Basis `57ba54fa`. The four charged
inputs were read from `/tmp/jc2-lane.WnfxfS/inputs`. Consumed: from the charged universal-series report (UF) in Euler form, `Φ_k`, Props. 2.2, 4.1, 4.2, 4.3 and the frozen
`universal_recursion / tacnode_checks / degenerate_pivot` drivers and JSONs in `box/k16-universal-20260905/`; from the charged
abel-polysol report (I1)-(I4), Theorem H and the pivot laws; from the charged Astra report (UF), (UJ), (UL), (UT), the t = 2
family and the `b = 0` chart (§7.3). The frozen certificates replayed are
`box/k16xempty-20260905/controls_t{3,4,5}_raw.sing` (byte-unchanged, identifiers renamed on import), compared under the
identity map on `(c_i, b)` by `imap`, exactly as in the charged `custody_bu.py`. No ledger, `jc2-lean` or `ideation-*` file
was read or written. All drivers and transcripts are in `box/k16-tacnode-20260905/`.

Notation (charged §7.1): `N = t+1`, `theta = x d/dx`, `G = (3/2)L(L+b) - Bx`, `R = (3/16)L²(L(L+2b) - 4Bx) - eta*x²(bL/2 + Bx)`,
(UF) `(theta-3)(P²) + G*P = R`; `L = -b + Σ_{j>=2} l_j x^j` (ray: `l_j = c_{N-j}/y`, `l_N = 1/y`, `l_j = 0` for `j > N`);
`P = Σ P_k x^k`, `P_0 = -b²/4`, `P_1 = -B`, `P_2 = eta = w_1`, `P_3 = w_2`, `P_4 = w_3`; `p = omega*y² = 1/(4(2d+1))`, `3d² = N`.
`Q_P(x, Y) = R(x,Y) - G(x,Y)P - (theta-3)(P²)` (quartic in Y, leading coefficient 3/16). The tilde in `L̃` is a label, never
a derivative; `Lpivot := 4eta + 3bl_2`; `piv_2 := 2Bl_2 + b²l_3 + 2bw_2`. Throughout `b != 0` (§5 end for b = 0).
