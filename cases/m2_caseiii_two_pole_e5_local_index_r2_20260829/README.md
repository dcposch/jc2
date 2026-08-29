# M2 case-III two-pole E5 merge-local index — R2 repair packet

Primary repair (Fable 5, 2026-08-29) of
`cases/m2_caseiii_two_pole_nuh_bound_r1_20260829/` after the Fable 5
hostile review returned REPAIR_REQUIRED.  **R1 is byte-untouched**; this
packet supersedes its *reading*, not its arithmetic.

R1 bounded "the incoming zero-edge index `h = nu_H`" through the
case-III handshake `X = mu0*(kbar - h*w0)` — the printed
Prop 9.3(g),(h)/mixed pin, which the promoted H5a resolution
(`xmodel/sol-h5a.md` Props 1–2, `xmodel/grok-h5a-review.md` SOUND,
`ladder/BOOK-OFFAXIS.md` §11-PRE/§11a) refutes unless open CONJECTURE
`U_7C` holds.  Under the promoted Q+E5 pin the handshake is
`X = mu0*(kbar - nu_G*w_U)`: the eliminated index is the **merge-local
`nu_G`**, and the incoming `nu_U` is **free** (infinite neutral
congruence menus).  This packet re-founds everything on that pin:

* **Lemma A** (reading-independent): `dq/D <= 2*delta+3`,
  `kbar = mu*w*dq/D <= mu*w*(2*delta+3)`; equality forces `D = M = 1`
  (every sharpness witness is MP2-dead).
* **Theorem B** (new M-graded refinement): `dq/D <= 2 + (2*delta+1)/M`;
  equality iff `M | 2*delta+1` (M odd) on the `s=1, A=1, nu_G=delta+M`
  cell — attained by 12 of the 17 promoted §11a cells (the kbar=6
  family), which are MP2-alive.
* **Theorem C** (E5): `mu0*nu_G*w_U = delta*kbar + mu*w`; sharp `nu_G`
  bounds in all three regimes; proof-by-menu that **no incoming
  `nu_U`/`nu_H` bound follows or is required**.
* Counterfixtures: `r0=2` cells break the constant (`dq/D = 3*delta+4`);
  equal-`(mu,w)` joins have `kbar` affine-unbounded; at fixed
  `(kbar, nu_G)` with a `mu>=2` partner the pattern fibre can be
  infinite.

Run:

```sh
python3 test_caseiii_two_pole_e5_r2.py       # 1,264,851 checks
python3 -O test_caseiii_two_pole_e5_r2.py    # same count, -O parity
python3 caseiii_two_pole_e5_r2.py            # print sealed certificate
```

`certificate_r2.json` is the sealed output; the test requires it to
match a fresh regeneration byte-for-byte.  Six staged mutations
(MUT_A–MUT_F: Lemma-A constant, M-graded constant, elimination sign,
countercell ratio, charged-slice identity, firewall flip) are applied to
`/tmp` copies inside the ordinary test run and must each be detected;
the packet is never modified.

Firewall: this packet licenses **no** canonical-engine change (`NUCAP`
stays; its honest fate is removal-by-rebuild, and wholesale cap
replacement is UNSOUND on `r0>=2`/inner-arrival rows), no `U_7C`
adjudication, no equal-join `kbar` bound, no multipole or inner-merge
coverage, no realizability, no landing, no degree bound, no JC2, no AWS
or fleet action.  Status: source-ready for different-model hostile
review.  Report:
`xmodel/m2-caseiii-two-pole-e5-local-index-repair-fable5-20260829.md`.
