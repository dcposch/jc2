# Hostile source/certificate review — corrected control-2 A

Act as a hostile tropical/commutative-algebra and CAS-custody referee.  This
is a text-only review on the local Mac: do not run Python, Singular, Sage,
msolve, Lean, Gfan, or any substantive symbolic computation.  Read frozen
sources and already-emitted AWS artifacts; lightweight text search and
SHA-256 verification are allowed.  State explicitly that no local
substantive computation was run.

Audit the complete package

```text
cases/max12_912_order3_d1_double_root_control2_rees_corrected_A_20260826/
```

whose result-freeze file has SHA-256

```text
49c745ae0e1b48b80a5d2b017e0311fe2fbb3ddc0252c0da0b5b24ac23bfb1d6
```

Read every source/custody/result file at the package root and every artifact
under `aws_box03_LPDP/` and `aws_r6d_DP/`.  Also read in full:

```text
cases/max12_912_order3_d1_double_root_control2_rees_source_identity_20260826/
cases/max12_912_order3_d1_double_root_control2_rees_v2_20260826/
cases/max12_912_order3_d1_double_root_control2_rees_certificate_20260826/
cases/max12_912_order3_d1_double_root_control2_rees_Afast_20260826/
cases/max12_912_order3_d1_double_root_control2_rees_20260826/SOFTWARE_CONTROL.md
xmodel/max12-912-order3-d1-double-root-control2-rees-v2-source-review-grok-20260826.md
xmodel/max12-912-order3-d1-double-root-control2-rees-certificate-review-grok-20260826.md
```

Charge every point below and fail closed on any ambiguity.

1. **E8 correction and provenance.** Verify from the frozen exact AWS
   identity control that old factored A and expanded B agree on
   `E1,...,E7,LT` and that
   `A_E8-B_E8=-25134148616192/43046721`.  Locate the bad emitted A `poly E8`
   and its renderer call.  Verify that the corrected compiler does not hand
   repair/refactor E8: it hash-pins B and extracts `E1,...,E8,LT`
   byte-for-byte.  Decide whether this is the cleanest sound correction.

2. **35-generator equality.** Verify that expected B stdout is pinned at
   SHA-256 `d5317aac...`, parses exactly 35 consecutive `GH[i]` entries with
   final `la^20,s`, and that both corrected A sources construct an `EXPECTED`
   ideal from all 35.  Audit the two mutual-reduction loops in both
   directions.  Explain why the different printed reduced-basis order in
   global `dp` (with `s` first and `la^20` last) is compatible with equality
   of ideals; do not require textual basis identity where term orders differ.

3. **Contraction and saturation order.** Check that the full nine-generator
   Rees ideal is first contracted from `s!=0` using direct `sat(I,<s>)`, only
   then specialized with `s=0`, and only then standardized.  Compare this
   against B's independent `u*s-1` contraction.  Charge the distinction
   between `sat` and `sat_with_exp`, the fleet return-type control, the later
   torus saturation, and why specializing before contraction would be wrong.

4. **Certificate semantics.** Verify direct membership of `la^20` and of the
   torus product in the full special-fibre ideal, exponent-one torus
   saturation, unit localization, and residue unit.  Decide whether these
   support exactly the claimed no-torus-leading-coefficient theorem.  Make
   clear that `la^20` is an S-polynomial/full-initial-ideal consequence, not
   merely an initial form of a submitted generator.

5. **AWS custody.** Verify both registered tags, complete pre-GO source
   custody, compiler/Singular rc zero, empty compiler and CAS stderr,
   separated timing, expected PASS and absence of FAIL markers, input and
   stdout hashes, and the two different orders/caps.  Treat the two A runs as
   separate AWS executions of one compiler/source strategy; do not call them
   independent derivations of the charged equations.

6. **Impact enumeration.** Audit `IMPACT_MATRIX.md` against repository text.
   Enumerate every historical control-2 A-only artifact consuming the bad
   renderer: V1 A, V2 A, A-fast, and the deliberate identity negative
   control.  Identify any top-level or xmodel statement that actually relied
   on a bad A endpoint.  Explicitly decide whether the old v2 source review's
   A-equivalence discussion is superseded while its B-only computation
   remains valid.  Do not contaminate tied-toric or other compilers merely
   because they used the harmless list-wrapped `sat` idiom.

7. **B theorem and firewall.** State whether the B-only theorem and focused
   B certificate review remain valid.  The strongest permitted promotion is
   only the exact fixed
   `a=1,h=q2=k=nu=0,mu=2/3`, support and weight
   `(4,1,1,22,22,30,30,30)`, with all eight displayed coordinates nonzero.
   It is not a moving-axis, moving-load, nonzero-`q2`, other-support,
   other-weight, whole-cone/fan, D1, or JC2 theorem.

Write exactly one report and make no other repository edits:

```text
xmodel/max12-912-order3-d1-double-root-control2-rees-corrected-a-review-grok-20260826.md
```

End with one token on its own line:
`CORRECTED_A_CONFIRMED`, `CORRECTED_A_REPAIRED`, or
`CORRECTED_A_REJECTED`.

