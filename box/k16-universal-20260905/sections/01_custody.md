## 1. Custody

The receipt `xmodel/k16-universal-series-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing each
`charged_input_<i>_sha256=` with its `_basename=` into `box/k16-universal-20260905/manifest.sha256`; `sha256sum -c`
returned **4/4 OK** before any input was opened (re-run at sealing: `input-verification-final.log`). No digest was
retyped. Basis `e00b2002`. All four charged inputs were read from `/tmp/jc2-lane.S7hyqB/inputs`; (UF), (UJ), (UL) and
the identities (I1)–(I4), Theorem H and the x = 0 pivot law are consumed from the charged abel-polysol report; the
boundary identity `R_boundary = y·eta/3` from the charged Astra §8. The frozen certificates replayed are
`box/k16xempty-20260905/controls_t{3,4,5}_raw.sing` (byte-unchanged, identifiers renamed on import), compared under
the identity map on `(c_i, b)` by `imap`, exactly as in the charged `uf_emit.py`. No ledger, `jc2-lean` or
`ideation-*` file was read or written. All drivers and transcripts are in `box/k16-universal-20260905/`.

Notation (charged §7.1): `N = t+1`, `q = 2N−1`, `theta = x d/dx`, `G = (3/2)L(L+b) − Bx`,
`R = Rfree = (3/16)L²(L(L+2b) − 4Bx) − eta·x²(bL/2 + Bx)`, so (UF) reads `(theta−3)(P²) + G·P = R`.
Write `L = −b + Σ_{j≥2} l_j x^j` (`l_1 = 0` is `L'(0) = 0`; on the ray `l_j = c_{N−j}/y` for `2 ≤ j ≤ N−1`,
`l_N = 1/y`, `l_j = 0` for `j > N`) and `P = Σ_k P_k x^k` with the jets `P_0 = −b²/4`, `P_1 = −B`, `P_2 = eta`,
`P_3 = w_2` (`= [x²]W`). `G_i`, `R_k` are x-coefficients; the tilde in `L̃` below is a label, not a derivative.
