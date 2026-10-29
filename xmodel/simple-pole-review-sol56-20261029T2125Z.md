# Hostile review of SIMPLEPOLE2115

Status: COMPLETE / INDEPENDENT HOSTILE REVIEW. Requested adapter/model `gpt-5.6-sol`, ultra; actual hosted identity unverified. This is a first independent review of the new ROOT proof, not a retry.

Provisional partial written at measured UTC `2026-10-29T21:30:46Z`, before the `21:40` deadline. Manifest-first custody, all nine standing governors, the whole current STATE, and all 41 LF of the sealed candidate had then been read. Terminal postpins and the final seal were still pending.

## Verdict

`PASS_CONDITIONAL`, conditional only on the named standard surface foundations stated precisely below. The provisional verdict was unchanged at terminal review. I find no defect in the central point-blowup induction, the exceptional-divisor residue calculation, or the generic residue-transport argument.

## Independently checked argument

Let the ground field be `C`, let `K=C(x,y)`, and normalize divisorial valuations to value group `Z`. Assume the standard surface extraction/local-uniformization fact: a divisorial valuation of `K` is represented on a smooth model reached from `P2` by finitely many point blowups, and a valuation centred at a closed point over the line at infinity is extracted by its finite chain of infinitely-near point centres. Also use the standard fact that subsequent point blowups do not change the generic point or residue field of an already extracted divisor.

On `P2`, `div(dx wedge dy)=-3 L_infinity`, so the raw label `A=ord(Omega)+1` of `L_infinity` is `-2`. A prime already lying in `A2` has label `1`. If a divisorial valuation is centred at a closed affine point, its first exceptional divisor has label `2`; thereafter a smooth-centre blowup replaces `a` by a new adjacent label `a+1`, and a node blowup creates label `a+b`. Hence every divisor over an affine centre has positive label. This includes centres meeting non-boundary curves: those curves have coefficient zero in `div(Omega)`, and the same local calculation remains positive. Thus an `A=0` divisor is necessarily over infinity.

The total transform of `L_infinity` stays an SNC tree under the extracting sequence, so there is no omitted non-SNC centre. At a boundary smooth point,

`Omega=u^(a-1) b(u,z) du wedge dz`,

with `b` a unit, and the chart `u=t, z-z0=t s` gives the new label `a+1`. At a node,

`Omega=u^(a-1)v^(b-1)q(u,v) du wedge dv`,

with `q` a unit, and `u=t, v=t s` gives new label `a+b`. Starting from `-2`, induction proves both required edge invariants: no edge has labels of opposite strict sign, and no edge has two zero labels. A smooth blowup preserves them because the only zero birth is `-1 -> 0`; a node allowed by the two invariants is negative-negative, positive-positive, or zero-nonzero, and insertion of its sum preserves both. In particular no zero is born at a node: every zero divisor is born by blowing up a smooth point of an `A=-1` component.

At such a point the support of `div(Omega)` is exactly the SNC boundary, so the displayed coefficient is a unit at the point, not merely at the generic point. Write

`Omega=u^(-2)b(u,z) du wedge dz`, with `b(0,z0) != 0`.

On the exceptional chart `u=t, z=z0+t s`,

`Omega=t^(-1)b(t,z0+t s) dt wedge ds`,

and therefore `Res_D(Omega)=b(0,z0) ds` on the dense affine chart of the entire exceptional `P1`. Equality on that dense chart proves the global rational-form identity; it has one double pole at `s=infinity` and no zero. A later point blowup maps the strict transform of `D` isomorphically to `D`, so the rational residue form is unchanged under that identification.

For transport, let `H:K_t -> K_s` be the field embedding of a dominant generically finite rational map, suppose `H^*Omega_t=c Omega_s` with `c in C^*`, and let normalized divisorial valuations `v_s|v_t` satisfy `v_s(t)=e` and have `A(v_s)=A(v_t)=0`. At their generic DVRs choose uniformizers `t,u`; then `H^*t=u^e a` for a unit `a`. Writing a simple-pole form as `dt/t wedge eta` plus a term regular along the target divisor shows

`Res_v_s(H^*Omega_t)=e h^*Res_v_t(Omega_t)`.

Indeed `d(H^*t)/(H^*t)=e du/u+da/a`; the unit term and the pullback of the regular transverse term have no `du/u` residue. Thus transverse terms and units add nothing, while the normal term contributes exactly `e`. Comparing with `H^*Omega_t=c Omega_s` gives

`e h^*Res(Omega_t)=c Res(Omega_s)`.

More explicitly, write `Res(Omega_t)=gamma_t ds_t` and `Res(Omega_s)=gamma_s ds_s`, where `gamma_t,gamma_s` are nonzero constants and `s_t,s_s` are rational coordinates. Then

`e gamma_t d(s_t composed with h)=c gamma_s ds_s`.

In characteristic zero, a rational function with zero differential is constant, so

`e gamma_t (s_t composed with h)=c gamma_s s_s+constant`.

All three scalar factors are nonzero. Since `s_t` and `s_s` have rational-map degree one, degree multiplicativity gives `deg(s_t composed with h)=deg(h)=f=1`. Equivalently, in the distinguished residue coordinates `h` is affine linear with nonzero slope.

## Exact scope and remaining JC2 gap

The conclusion concerns residue degree `f` only. It does not force normal ramification `e=1`, does not identify `e f` with the total field degree, and does not prove a weak local homeomorphism. Most importantly, the campaign's actual residual-fold obstruction has raw label `A=-1` and the specified inverse ends are infinitely singular rather than divisorial. This proof supplies neither a negative-label primitive theorem nor an infinitely-singular transport/no-fold theorem, so the global JC2 gap remains unchanged.

## Exact hypotheses and conditional foundations

The result proved here has the following exact hypotheses.

1. The ground field is `C` and each plane carries its standard affine coordinates and standard volume form. The conclusion is not asserted for an arbitrary exact rational two-form.
2. Divisorial valuations are normalized. I condition on the standard two-dimensional extraction/local-uniformization theorem and the usual factorization of extraction into finitely many point blowups from a smooth projective model. I also condition on the standard generic-point invariance of an extracted divisor under later blowups. These are the only unproved imported foundations in this review.
3. For transport, `H` is a dominant generically finite rational map of the two rational plane function fields, `H^*Omega_t=c Omega_s` for `c in C^*`, and `v_s` restricts to `e v_t` with both raw labels zero. The induced residue-field inclusion defines the nonconstant finite map `h` and `f=[kappa(v_s):kappa(v_t)]=deg(h)`.

No periodicity, invariant finite divisor set, properness, or extension of `H` to a morphism near a chosen closed point is used. The inclusion of the two generic DVRs is enough for the residue calculation.

## Custody and complete coverage

The first action was the required whole manifest read. Before any declared-input body was read, one metadata-only pass covered all eleven declared files. Every declared snapshot was a regular mode `0400` file, every tested ancestor and leaf was non-symlink, and bytes/LF/SHA matched the manifest. The manifest records original packet mode `0444`; original paths were treated only as provenance and were not inspected. Candidate pre-body verification passed with body bytes `5238`, body SHA-256 `41bab1de637f788cabe0bb7f6f46918a4b80e1abac93eff4b77690c99220a633`, and basis `26efb4f4ca452199c6d4bdab4210602071d6abcf`.

All ranges below were read contiguously and wholly, with no repeated body window and no clipped or cropped line. The postpass repeated metadata only. `pre SHA-256` and `post SHA-256` are independently measured values.

| declared input | whole range | bytes / LF | pre SHA-256 | post SHA-256 |
| --- | ---: | ---: | --- | --- |
| `HQ-AGENTS.md` | 1–23 | 1520 / 23 | `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f` | `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f` |
| `HQ-POLICY.md` | 1–112 | 6755 / 112 | `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634` | `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634` |
| `HQ-RESEARCH_POLICY.md` | 1–162 | 9551 / 162 | `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62` | `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62` |
| `HQ-RESTRICTIONS.md` | 1–259 | 18817 / 259 | `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed` | `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed` |
| `HQ-RUNBOOK.md` | 1–507 | 34745 / 507 | `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06` | `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06` |
| `HQ-STATE.md` | 1–211 | 54492 / 211 | `447d0a9ed9c6fb312ce2ba49702d24d48b2125c44023a38ee4af7c5950e4f518` | `447d0a9ed9c6fb312ce2ba49702d24d48b2125c44023a38ee4af7c5950e4f518` |
| `PUBLIC-AGENTS.md` | 1–22 | 1229 / 22 | `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f` | `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f` |
| `PUBLIC-README.md` | 1–102 | 5391 / 102 | `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf` | `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf` |
| `PUBLIC-COORDINATION.md` | 1–107 | 6042 / 107 | `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e` | `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e` |
| `PUBLIC-FALLACY-v2.md` | 1–36 | 1985 / 36 | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |
| `candidate.md` | 1–41 | 5570 / 41 | `da6ae54d7e490a9b35ed14c23c884237bc059d574f3e5ce4c7302e09be34440b` | `da6ae54d7e490a9b35ed14c23c884237bc059d574f3e5ce4c7302e09be34440b` |

The administrative `input-manifest.json` was read whole at lines 1–147 before metadata and had identical pre/post SHA-256 `120834af12c9083384c1e831c9ca5f057b18fa39fdbe45b707ee4b2106895540`, `4987` bytes, `147` LF, mode `0400`, and no symlink ancestor.

Actual body accounting: the ten declared non-STATE bodies were `1371` LF exactly; `HQ-STATE.md` was `211` LF separately. Counting the administrative manifest conservatively against the non-STATE cap gives `1518/2400` LF. Repeated body LF: `0`; clipped/cropped/unread requested LF: `0`. Source queries: `0`; history queries: `0`; primary-source body LF: `0`; unlisted-source body LF: `0`; CAS: `0`; control families: `0`; agents/jobs launched: `0`. No archive, whole `APPROACHES.md`, unlisted source, tool implementation, `jc2-lean`, `jc2-web`, or `max11` was inspected or enumerated.

Measured UTC events: first action `2026-10-29T21:25:52Z`; all nine non-STATE governors complete `2026-10-29T21:28:35Z`; whole STATE complete `2026-10-29T21:29:51Z`; substantive unsealed partial `2026-10-29T21:30:46Z`; terminal body writing stopped `2026-10-29T21:32:26Z`. The terminal legacy stamp and verification are performed only after the following body boundary; the appended seal records the frozen basis and body hash.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11060`.
- Body SHA-256:
  `250a85e98fe1476ce4cc8dfb0db266441162bf7621b20707d633366129285aed`.
- Frozen basis: `26efb4f4ca452199c6d4bdab4210602071d6abcf`.
