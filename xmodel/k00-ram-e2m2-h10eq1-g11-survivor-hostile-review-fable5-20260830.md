# Hostile review: K00 `e=2,m=2,h10=1` boundary child through G11 (survivor claim)

Date: 2026-08-30 UTC
Reviewer: Fable 5 (different-model hostile reviewer)
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c` (verified = HEAD)

Reviewed in full:

```text
05e416fccb20b42a187f254995c021608e9060444660628d52a848d17f19b8e1
  xmodel/k00-ram-e2m2-h10eq1-g11-survivor-producer-sol56-20260830.md   (verified)
  body 9996 bytes / a0104064a049911d4bc732245b53d653a093acffa9019116dca58092abdd9865 (verified)
d5e458d2c430cc85be86b711e37355671090057881474458055dbf7f593609c3
  xmodel/k00-ram-e2m2-h10eq1-g11-survivor-replay-sol56-20260830.py     (verified)
```

## Verdict

**CONFIRM_WITH_CORRECTIONS.** Every displayed mathematical object — the
arrival census, formula (2.3), the seven literal G11 rows and their term
counts, the inherited-tree survival audit, the complete fresh-`n=5` rank fan
(4.1)–(4.8), the two-sign `n=4` rank-one G11 survivors, all three fixtures and
all three algebraic mutations — was independently rebuilt from the frozen 569
tails with my own parser, series engine, and formula implementations
(producer helpers not used), and every claim reproduced exactly. The
corrections are ledger-level, not mathematical: the certificate's `CUSTODY`
mutation entry is not backed by an executed control, and two symbolic charts
assert fewer low-grade zeros than they rely on (the gaps are mathematically
automatic and I verified them mechanically). The producer's endpoint (6.1) is
exactly the maximum safe conclusion; nothing stronger, nothing weaker.

| mandate item | finding |
|---|---|
| 1. hashes, seals, pins, replay, `-O`, mutations | CONFIRMED; two ledger corrections (C1, C2) |
| 2. arrival census; `S4,T4,N8,k10[2]` absence | CONFIRMED and upgraded to machine proof |
| 3. seven literal G11 rows, (2.3), term counts, `alpha,beta` | CONFIRMED exactly; row-6 nuance (C5) |
| 4. G10 tree with `k10[0]` deleted | CONFIRMED; no unit-face terminal imported |
| 5. fresh-`n=5` rank fan (4.3)–(4.8) | CONFIRMED, incl. independent cone-support proof |
| 6. old-`n=4` rank-one branch, both signs | CONFIRMED; forcing (3.1) re-derived symbolically |
| 7. fixtures + mutations, evidence levels | CONFIRMED; mutations fail exactly at G11 |
| 8. maximum safe conclusion, G12 retention | exactly `POINT_SET_NONEMPTY_THROUGH_G11`; no cheaper obstruction exists |

## 1. Custody, replay, determinism

- Producer full-file, body-byte (9996), and body-SHA256 seals verified against
  the standalone `<!-- BODY-END -->` definition; exactly one standalone marker
  line.
- All six charged dependency hashes verified on disk: tails.json
  (`d72f774c…`), exact engine (`2c918d5b…`), e2m2 G10 replay (`efd2f4fe…`),
  G10 report (`fa5a4ef6…`), my G10 hostile confirmation (`4710349b…`), and
  the ramified calendar gate (`9a94cd3b…`).
- Replay run twice, `python3 -B` and `python3 -B -O`: exit 0, byte-identical
  output, matching §7 line-for-line, ≈2.2 s, no files written. All assertion
  paths use explicit raises, so `-O` is a meaningful control.
- `CERTIFICATE_BYTES=2656` and
  `CERTIFICATE_SHA256=d83eeb1db7e7d092eaa5cb23016e73ebcf72835024300d679316121a9518d817`
  reproduced; the expected-digest gate is armed (not `PENDING`).
- Mutation controls: `WALL_SIGN`, `N5_B (-5/12→-5/13)`, `N4_Y1 (5/72→0)` all
  executed and all visible. See C1 for the `CUSTODY` entry.

## 2. Exact arrival census through G11 (upgraded to machine proof)

I rebuilt the literal source `R(d) + tau^4(kappa tau + k2 tau^2)A10(d)` on an
**enlarged** `n=4` chart that retains, as live symbols, everything the
producer's census excludes: `S4,T4` (grade-4 surface), all six `N8` slots,
and `k10[2]`, alongside `S2,T2,S3,T3,N4(cone),N5,N6,N7,k10[1]`. Truncation 13
(through G12). Results:

- G0–G7 identically zero; `G8=Q(N4)`; `G9=DQ(N4)[N5]`;
  `G10=DQ(N4)[N6]+Q(N5)+(1/2)D^2R3(ell2)[N4,N4]` with **no load** (the
  `k10[0]` slot is gone and `kappa`'s earliest load grade is 11).
- **`S4`, `T4`, all `N8` slots, and `k10[2]` appear in no grade G0–G11** —
  proven by retention, not by omission. All of `s,t,alpha,beta,p,q,kappa,
  N5,N6,N7` genuinely appear at G11 (positive census side verified too).
- At G12 the same chart picks up `k2, s4, t4, n8_*` — so `k10[2]` (and
  `S4,T4,N8`) first reach exactly G12, as claimed.
- K6/K2 load rows exist in the tails and are excluded below G12 by the
  charged calendar (K6 at 15/17, K2 at 23, targets 29+, Jdet 38); those
  grades contain no `k10` factor, so zeroing `k10[0]` cannot lower them.
  The producer's replay retains `k10[2]` computationally and argues
  `S4,T4,N8` by census; the census argument is sound (gradient lemma +
  grade count) and is now also machine-verified (C4).

## 3. The seven literal G11 rows and formula (2.3)

Re-extracted from the 569 tails with an independent implementation of every
ingredient (`DQ`, full bilinear Hessian, `second-half` Hessian, `M4`,
`A10^[3]`, `mu`, `ell`). Row by row, exactly:

```text
G11_r = DQ_r(N4)[N7] + DQ_r(N5)[N6] + D^2R3_r(ell2)[N4,N5]
      + (1/2)D^2R3_r(ell3)[N4,N4] + kappa*(DM4_r(ell2)[N4] + W_r(s,t)),
```

with `W_r = DM4_r(ell2)[mu(s,t)] + A10_r^[3](ell2)` — formula (2.2)/(2.3)
verified as exact polynomial equality. Raw sparse term counts:
**36, 39, 41, 33, 39, 12, 34** — matching the producer's list exactly.
`alpha,beta` are genuinely retained (they enter through the
`(1/2)D^2R3(ell3)[N4,N4]` term); per-row dependence is
rows 1–5, 7 yes, **row 6 no** (see C5). `k10[2]` is absent from every row.

## 4. Inherited tree: what survives when `k10[0]` is deleted

Audited against the charged G10 replay code and my own pinned G10 review:

- `n=2` deaths at G6 and `n=3` deaths at G8/G9 are `k10`-free: the load
  cannot reach grade ≤9 on this face (`M4(ell2)=0`, plane/cone polar
  identities kill load grades 4 and 5), and the `n=3` reduced chart was
  verified in the G10 round with all six `k`-slots symbolic. Valid verbatim
  on `k10[0]=0`.
- `n=4` rank two: the G10 `C,E` death identities hold with symbolic `k0`
  and `k10`-free right sides — valid verbatim.
- `n=4` rank one: I rebuilt the chart (`p=eps*8i*q`, `B(N5)=eps*8i*A(N5)`)
  with `kseries=(0,kappa,k2)` and verified symbolically, both signs:
  G0–G9 vanish; **G10 is entirely `kappa,k2`-free** (the old terminal
  `-eps*(5i/16)k10[0]t^3` has no `k10[0]`-free part, so it vanishes
  identically here, and no new load term replaces it); the wall combo
  `(3 eps i/64)q^2(s-eps*8i*t)` forces `s=eps*8i*t`; row 4 then forces
  `A(N5)=B(N5)=0` — that is (3.1), re-derived as necessity; after the
  forcing, all seven G10 rows reduce to the single solvable equation
  `(3/1024)q(eps*8i*U-V) + (Hessian residual) = 0` in `(U,V)=(A,B)(N6)`
  (rows 4,6 vanish; 3,5,7 and 2 are fixed multiples of row 1). The branch
  survives G10 structurally, not by fixture accident.
- `n=4` rank zero: G10 becomes `Q(N5)`, forcing the fresh `n=5` cone.
  No unit-face terminal was imported anywhere; §3's table is the exact
  `k10[0]`-deleted restriction of the confirmed tree.

## 5. Fresh-`n=5` fan, with an independent reduced-support proof

**Cone support.** The recentering uses `Q(w)=0 ⟹ w ∈ image(cone_vector)`
set-theoretically. Beyond consuming the charged G10 confirmation, I proved
`V(Q1..Q7)_red = V(A,B)` outright by four elementary certificates computed
today from the tails:

1. each `Q_r = A*L_r + B*M_r` (linear `L_r,M_r`; so `V(A,B) ⊆ V(Q)`);
2. `A*B = (2048/3)Q_1 + (16384/3)Q_3` (so `V(Q) ⊆ V(A) ∪ V(B)`);
3. `B ∈ span(A, M_1..M_7)` (so `V(Q) ∩ {A=0} ⊆ {A=B=0}`);
4. `A ∈ span(B, L_1..L_7)` (so `V(Q) ∩ {B=0} ⊆ {A=B=0}`).

Hence every `G10=0` solution is a cone vector; its plane part absorbs into
`S5,T5`, which I verified (retained symbols) touch nothing through G11, so
the reduced chart `w=(2p,0,0,q,-p,4q)` loses no G11 point-set generality.
The rank trichotomy `Delta≠0 / p=eps*8i*q, q≠0 / p=q=0` is exhaustive over
the declared algebraically closed characteristic-zero field.

**Fan identities.** On the enlarged `n=5` chart (retaining
`alpha,beta,S4,T4,S5,T5,N7,N8,k10[2],y1..y4`): G0–G9 vanish identically;
G10 `= Q(w) = 0` on the chart; G11 `= DQ(w)[v] + kappa*W` exactly, free of
every retained extra symbol including `y1..y4`. Equations (4.3), (4.4)
(rows 3,5,7 = `-(1/8),-(1/128),-(1/1024)` of row 1; rows 4,6 ≡ 0), and the
`W1,W2` cubics (4.5) verified literally.

- **Rank two:** the cross-multiplied inverse identities for (4.6) hold, and
  substituting (4.6) back kills `Delta*G11_1` and `Delta*G11_2`
  identically — every `Delta≠0` cone point extends through G11 with
  `(A,B)` uniquely determined and four free `v`-slots. Symbolic, complete.
- **Rank one:** the full-row identity
  `G11_2+(eps i/2)G11_1|_(p=eps 8i q) = kappa*(5/65536)(s+eps*8i*t)^3`
  verified for both signs (and the wrong-sign wall differs, so the sign is
  pinned). On reduced field-valued support this forces `s = -eps*8i*t`
  (4.8) — the wall **opposite** to the `n=4` branch's `s=+eps*8i*t`, as
  claimed; `d[2]≠0` then forces `t≠0`; the residual equation is
  `(3/1024)q(eps*8iA-B) + kappa*W1 = 0` with `q≠0` and
  `W1 = -(5/16)t^3 ≠ 0` — one inhomogeneous linear condition on `(A,B)`,
  always solvable. Both signs survive.
- **Rank zero:** all seven G11 rows equal `kappa*W_r`; `kappa` is a unit;
  `t=0 ⟹ W2=(5/65536)s^3`, `s=0 ⟹ W1=-(5/64)t^3`, and on `st≠0`,
  `s^2=192t^2` forces `3s^2-64t^2=512t^2≠0` — dead in characteristic zero
  on `(s,t)≠(0,0)`, including every deeper recentering `ord(N)>5` (the
  load term `kappa*W` at G11 is independent of all normal data beyond
  grade 5).

## 6. Old-`n=4` rank-one G11 branch and fixtures

All three fixtures re-evaluated numerically in my independent pipeline,
all seven rows, all twelve grades G0–G11: identically zero for
`n5_rank2` (rational), `n4_rank1_plus`, `n4_rank1_minus`. Sharper than the
replay's own check, each of the two algebraic fixture mutations still
passes G0–G10 and fails **exactly at G11** (`-5/13`: row 2;
`y1→0`: rows 1,2,3,5,7), so both controls certify G11-sensitivity
specifically, on two different transition-tree branches. The rational
fixture's `(A,B)=(0,-5/12)` is exactly the (4.6) rank-two specialization at
`s=1,t=0,p=1,q=0,kappa=1` (hand-checked and machine-checked). Denominator
audit: (4.6) divides only by `Delta` (rank-two open), the rank-one solve
only by `q` (rank-one open) and uses `t≠0` from `d[2]≠0`; `kappa≠0` is the
declared face open; all other constants are fixed rationals. The fixtures
satisfy every declared open (`k10[1]=1≠0`, `d[2]≠0`, `Jdet` free through
G11 since its calendar grade is 38).

**Evidence levels, distinguished as mandated:** the fresh-`n=5` fan is a
complete symbolic classification (identities above), not fixture-inferred.
The `n=4` rank-one branch is: survival-at-G10 symbolic (section 4 above) +
G11 nonemptiness by explicit two-sign fixtures; the producer claims no
complete G11 solution variety there, and none is certified. Nonemptiness
(0.2) needs only one fixture and has three.

## 7. Maximum safe conclusion, G12 retention, no cheaper obstruction

Because explicit points pass G0–G11 and the charged, `k10`-monotone
calendar puts every non-K10 sector strictly beyond G11, **no obstruction to
this child exists at any grade ≤ 11** — the proposed one-grade closure is
refuted constructively, and no cheaper obstruction was omitted. The
maximum exact statement safe to promote:

```text
On the normalized generic K00 support with Lambda=tau^2, C6=1, ord(d)=2,
k10[0]=0, k10[1]!=0, Jdet[0]!=0, d[2]!=0:
  V(G0,...,G11) is nonempty, with a rational witness (0.3) valid over
  every characteristic-zero field, and Gaussian witnesses on both n=4
  rank-one sign charts;
  survivor strata at G11: n=4 rank-one (both signs, on s=eps*8i*t),
  fresh n=5 rank-two (all Delta!=0 cone points), fresh n=5 rank-one
  (both signs, exactly on the opposite wall s=-eps*8i*t);
  the fresh n=5 rank-zero stratum (hence every ord(N)>5 branch) is empty;
  POINT_SET_NONEMPTY_THROUGH_G11; FORMAL_ARC_STATUS_OPEN;
  NEXT_LITERAL_GATE=G12.
```

No formal arc, lifting, source reachability, algebraization, map, or JC2
statement is available or claimed; a finite jet is not an arc. The
producer's non-claims list is correct and complete.

**G12 retention (verified by truncation-13 census on both mechanisms):**
- `n=4` mechanism: G12 depends on `s,t,alpha,beta,S4,T4,p,q,N5,N6,N7,N8,`
  `kappa,k10[2]` — i.e. exactly the four G11-absent slots arrive, plus the
  unloaded quartic sector (`D^2R4` base) and `D^3R3` cubic-in-normal terms.
- fresh `n=5` mechanism: G12 depends on `s,t,alpha,beta,p,q,A,B,y1..y4,`
  `N7,kappa,k10[2]` (full `N6`, not just `(A,B)`; no `S4,T4,N8` yet).
A G12 successor dropping any of these is defective; the producer's §6 list
is accurate. The section-5 fixtures' zero-continuations are correctly
flagged as non-evidence for G12.

## 8. Corrections (none affecting the verdict's substance)

- **C1 (ledger).** `MUTATIONS=CUSTODY,...` and the certificate's
  `"custody"` entry are not backed by an executed mutation control in this
  replay: the custody gate is a plain digest comparison, and the base
  replay's vacuous-custody negative control does not run on import. The
  honest count is three executed algebraic mutations plus digest gates.
- **C2 (provenance).** The V20R2 compiler hash is pinned only inside the
  imported engine/base-replay constants, whose `main()` gates never run
  here, so it is unchecked at runtime. No mathematical exposure (the
  coordinate map is hard-coded in the hash-pinned engine), but a G12
  successor should pin it directly.
- **C3 (robustness).** `fresh_n5_g11_fan` does not assert G0–G9 ≡ 0 on the
  symbolic chart, and `literal_general_g11` does not assert G8–G10; both
  are mathematically automatic (gradient lemma + load calendar) and I
  verified both mechanically, but a successor replay should assert them.
- **C4 (evidence level, resolved).** `S4,T4,N8` absence at G11 was
  census-argued, not machine-retained, in the producer replay (`k10[2]`
  was retained). Upgraded to machine proof here; the census is exact.
- **C5 (precision).** "The `alpha,beta` terms are genuinely retained" is
  true of the G11 system, but row 6 (12 terms) contains no `alpha,beta`
  monomials; rows 1–5 and 7 do.

Verdict: **CONFIRM_WITH_CORRECTIONS**; safe to promote exactly (6.1) as
quoted in section 7 above, with C1–C5 attached.

<!-- BODY-END -->
