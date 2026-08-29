# Hostile review assignment: fixed-`p=0` residual `A`-Cech grade-14/15 replay

You are the independent hostile reviewer.  Work read-only except for the one
required report named below.  Do not edit any top-level ledger, case package,
other `xmodel` artifact, or `jc2-lean`.

Write exactly:

`xmodel/max12-812-order2-p0-a-cech-g14-g15-hostile-review-grok-20260826.md`

The producer claim is PROVISIONAL.  Audit it from the complete frozen source,
not from printed PASS tokens.  Pin and verify these custody hashes first:

- `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/FREEZE.sha256`
  SHA-256 `9b162c2dff50a6ca51d0eb0e7bb352379a5e0cd5f33acb7ce9c020ab7128b8a5`;
- `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/RESULTS.sha256`
  SHA-256 `bf9d044082ad94e5a46d7b4b8c32638bd6381cfef7964409aa91d06bd805799c`;
- `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/RESULT.md`
  SHA-256 `0db373023a1431e3d8e266faa9b52f90a886627fa77aae1c6738f860b86853dd`;
- `cases/max12_812_order2_p0_a_cech_g14_g15_20260826/compile_p0_a_cech.py`
  SHA-256 `3c2f6829d17794979f5e18381d859408a9f96d7c06060d334d10b1ef41b705cb`;
- `xmodel/max12-812-order2-p0-dk0-support-exhaustion-ramified-closure-design-20260826.md`
  SHA-256 `3518ac6c1505098a7b9e19c7b7ca2610dce42ff741e3f39065d0618b926ddb10`.

Audit, with exact source-level evidence, all of the following.

1. The compiler really starts from the frozen complete seven-row source and
   specializes `p=0` before any localization or division by `p`.
2. All lower loads and targets are retained.  In particular, independently
   census/check `k6`, `k2`, `mu2`, `mu4`, `mu6`, `J`, and targets at
   `sigma^28,sigma^32,sigma^36,sigma^38`; determine rather than assume that
   they do not contribute at absolute grades fourteen/fifteen.
3. The Laurent/Faber coefficient convention and target indexing are correct;
   no reversed-index, missing-tail, truncated-jet, or off-by-one error can
   manufacture the displayed rows.
4. Recompute the raw identities
   `g15[6]=-(1/16)a0^3`,
   `g14[2]=-(3/32)a1^2 br0`,
   `g14[1]=(3/8)a1(e0-a1 bs0)`, and, only after the two stated raw pivots,
   `g15[3]=-(1/16)a1^3`.
5. Check that the deductions on `D(a0)` and
   `V(a0) intersect D(a1)` are raw triangular/unit deductions over Q, with no
   hidden radical, saturation, unsafe denominator, or modular inference.
6. Verify the exact-Q lane is logically independent of the `F_65521` control,
   the relevant constants remain nonzero mod 65521, and the two evidence
   collections match their frozen inputs.
7. Audit whether `R=C=0` is used only after legitimate fixed-fibre routing,
   and whether any omitted coefficient direction or nilpotent thickening
   invalidates the stated *fixed-p0 high-contact residual-chart* scope.
8. Explicitly quarantine all generic V12/unbounded `d=1` and eight-form fan
   claims.  They are known to omit lower-load `k6/k2` terms at larger `a` and
   must not be used here.  Decide whether this fixed-p0 source replay is in fact
   independent of that defect.
9. Enforce the scope firewall: this cannot by itself prove one total
   Kummer/Rees family, positive-valuation moving-`p` exclusion, the all-zero
   higher-contact receiver, `k0=0`, terminal/Taylor closure, all of order two,
   maximum twelve, or JC2.

End with exactly one verdict token on its own line:

- `CONFIRMED`
- `REPAIR`
- `QUARANTINE`

If not confirmed, give the smallest exact correction and identify every
downstream statement that must remain quarantined.  If confirmed, state the
maximal theorem scope in one precise paragraph and list remaining composition
debts separately.
