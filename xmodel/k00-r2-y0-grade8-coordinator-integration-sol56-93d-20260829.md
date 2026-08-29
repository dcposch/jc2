# K00 old-plane valuation-two zero-odd-correction exclusion — binding integration

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PROMOTED_EXACT_SUBLANE_EXCLUSION / PREFLIGHT_REJECTED`

## 0. Binding disposition

Opus 5 independently rebuilt all seven V20R2 rows from the frozen 569 tails
and returned `PASS_WITH_INDEXING_REPAIRS` on the producer's grade-eight
exclusion.  The promoted statement is:

> In the normalized V20R2 source over a characteristic-zero field, no
> old-plane valuation-two jet
> `d=Lambda^2 ell(s,t)+Lambda^4 z+O(Lambda^5)` with
> `ell=(2s,t/8,s,t,s,2t)`, `(s,t)!=(0,0)`, `C6=1`, the five frozen
> boundary zeros (in particular `k6[0]=0`), and `k10[0]!=0` extends through
> grade 8.  The determinant unit is not used at this grade.

Equivalently, any old-plane valuation-two jet compatible through grade eight
in this source must have a nonzero `Lambda^3` correction `y`.  This is a
necessary condition, not existence of such a correction; compatible
seven-jets with `y=0` are not excluded.

The producer's proposed grade-seven nonzero-`y` rank/Fitting preflight is
rejected.  On the actual grade-six locus `DQ(y)` has rank at most two rather
than the assumed ambient-generic rank four (generic rank two, with rank-one
and rank-zero substrata), and the grade-seven equations are unconditionally
soluble.  Do not run that packet locally or on AWS.

Reviewer-derived stronger grade-eight exclusions remain provisional and are
not promoted by this integration.

## 1. Exact grade-eight proof

Put

```text
d = Lambda^2 ell(s,t) + Lambda^4 z + O(Lambda^5),
ell=(2s,t/8,s,t,s,2t),
a=(s^2,st/8,16t^2,0,0,0),
w=z-a.
```

Define

```text
A=16w1-4w3+w5,
B=w0-4w2+2w4,
kappa=k10[0].
```

Grades four through seven vanish identically on this sublane.  At grade eight
the only variables are `kappa,s,t,z`; no later `d` coefficient, nonconstant
`k10` coefficient, other load, or target can cancel the rows.  Exact
translation gives

```text
E_i = Q_i(w) + kappa L_i.
```

The raw quadrics and loads satisfy

```text
Q1+8Q3 = (3/2048) A B,
Q4     = (3/524288)(B^2-64A^2),
L1+8L3 = 0,
L4     = 0.
```

Hence the corresponding row combinations force `A=B=0` in characteristic
zero.  Every `Q_i(w)` then vanishes, and the two independent remaining rows
are

```text
E1 = (5 kappa/4096)  t(3s^2-64t^2),
E2 = (5 kappa/65536) s(s^2-192t^2).
```

They have no common zero on
`D(kappa) intersect (D(s) union D(t))`: if `t=0`, the second forces `s=0`;
if `t!=0`, the first gives `s^2=(64/3)t^2` while the second gives
`s^2=192t^2`.

The indexing repair is material but harmless to the proof: `Q6=0`, row 6 is
vacuous throughout this window, the seven quadrics span dimension four, and
there are only two independent grade-eight loads.  Row 7 remains the
Jacobian-target row but its target begins at grade 19.

## 2. Rejected grade-seven successor

For general

```text
d=Lambda^2 ell(s,t)+Lambda^3 y+Lambda^4 z+...,
```

grade six imposes all seven equations `Q_i(y)=0`; set-theoretically on the
reduced characteristic-zero locus this is `A(y)=B(y)=0`.  On this locus
`DQ(y)` has generic rank two and four-dimensional right kernel, not the
ambient rank four and two-dimensional kernel used by the proposed preflight.
The omitted cokernel conditions nevertheless vanish, and grade seven has the
universal solution

```text
A(z)=2st,
B(z)=s^2-64t^2.
```

Thus the proposed Fitting/chart split has zero exclusion power.  A concrete
compatible 7-jet with unnormalized `kappa=5` supplies a positive control in
the review.  Stop this packet rather than reparameterizing it.

The review additionally derives, but does not independently review, a
grade-eight rank-two-stratum kill, invariance of the zero-odd calculation
along the old plane, and an over-`Q` closure of the whole old-plane lane.  Over
an algebraic closure it isolates the rank-one stratum
`u=+-8 i v`, `v!=0`, as the smallest possible survivor.  These statements are
`REVIEW_DERIVED_UNREVIEWED`; they require a fresh different-model packet
before canonical promotion.

## 3. Scope and execution disclosure

This is a finite grade-eight exclusion in the named old-plane sublane.  It
does not exclude other components of the valuation-two leading cone,
valuations three through five, another normalization/support, a polynomial
map, K00 as a whole, a counterexample, or JC2.  A same-source formal arc in
this excluded sublane would truncate and is therefore impossible; a
compatible finite jet in an open sublane would not produce an arc or map.

The reviewer disclosed an operational scope violation: a repo-wide
`grep -rl` traversed the fenced `jc2-lean` path, and later path-pruning/status
commands statted it.  No modification or build was reported, and no Lean
object enters the mathematical reconstruction or evidence ledger.  The
mathematical review is accepted on its independently hashed V20R2 inputs;
the execution is not considered a clean precedent.  Future broad search and
status commands must exclude the fenced path before traversal.

## 4. Custody

```text
e4ec4431d679f44b27d35cbdc3c195c2383f21a57adc63e879be632c13af8a31
  xmodel/k00-higher-valuation-contraction-and-r2-preflight-sol56-93d-20260829.md
efec8e4e94315afee74dc47f2658fccd9be1d99c078dadbc61f3f88b25235cf3
  producer body through its first BODY-END marker
5d9cd05c5d14ad69259e084148c5d605fe01c90fa52cb466889005c57c9f7eef
  xmodel/k00-r2-y0-grade8-hostile-review-opus5-93d-20260829.md
4a60e84331eaf363990b4438956493274c359ec4f504a028a0544ba7bca7e677
  hostile-review body through BODY-END
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

No exit price, occurrence, attainment, or map is asserted.  No canonical
file, case source, AWS resource, or `jc2-lean` object was touched while
preparing this binding integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6146`.
- Body SHA-256: `3e8f271f5957cc26733de38a58c15f6709ecb1acd4ccf6f5375f6214f16b95c8`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
