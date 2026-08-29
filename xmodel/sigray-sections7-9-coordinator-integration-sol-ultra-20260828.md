# Coordinator integration: Sigray Sections 7--9 after the actual-weight repair

**Date:** 2026-08-28 15:50Z  
**Coordinator:** Sol Ultra / Codex  
**Status:** promoted at the campaign-internal tier, with the equality boundary below

## 0. Verdict

The amended actual-weight argument proves the inequality form of Sigray
Corollary 7.1 needed by the singleton characteristic-sequence exit budgets.
Together with the reviewed singleton first-separation ownership repair, this closes the last
conditional dependency in the campaign's repaired Section 9 derivation of

```text
normalized Keller counterexample  =>  td(f,g) >= 6.
```

This is an internal independent reconstruction of a conclusion already
available externally from Zoladek, Theorem 6.12.  It is not a proof that
`td != 6`, and it does not solve JC2.

The following stronger source claims remain quarantined:

- the literal per-puncture `delta_a` construction;
- printed Proposition 7.5 equation `(22)`;
- the fixed-baseline cluster equality `(22-cl)`;
- cross-fibre constancy of the repaired jump/max `kappa`;
- MP8's equality-based assertion that no refinement can assign positive
  global mass to the pure `M=1` forest.

## 1. Frozen evidence

The exact passed producer is

```text
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
```

The exact different-model hostile gate is

```text
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
```

The Section 9 source repair and hostile review are

```text
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md

0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad
  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
```

The last hash above is verified in its existing sidecar.  The Section 8
root-scope decision is separate: corrected Proposition 8.4 is nonroot only;
Statement 8.5 permits `M_root=1` and gives only divisibility.

## 2. Exact theorem now available

For each reference critical-value flag `F_i`, the passed quotient package
provides an abstract line `U_i`, a polynomial map
`phi_i=(P_i,Q_i):U_i -> A2`, and a cluster weight

```text
w_i(z) = sum_(P in C(i,z)) Lambda(P).
```

If `b_i^+=kappa_i^+(pi(F_i)-1)` is the generic nonzero-coefficient
baseline, then

```text
w_i(z)=b_i^+                         generically,
w_i(z)>=b_i^+                        at every exceptional point.
```

The special-point inequality is a **one-point** proper-tube comparison.  It
does not carry a multiplicity factor: nearby roots can have different moving
`Q_i`-values and cannot be summed into one local `g`-degree.  The hostile
review explicitly rejected the superseded multiplicity strengthening and
passed this amended one-point form.

Euler integration of the constructible actual weight gives

```text
d-1 = sum_i integral_(U_i) w_i d chi_c >= sum_i b_i^+.
```

For any prescribed reference fibre, its actual jump index is at most the
generic nonzero value.  Therefore, for the full set of its critical-value
flags, and hence for any subset of pairwise distinct such flags,

```text
td(f,g) >= 1 + sum_F kappa_F (pi(F)-1).             (C7.1*)
```

No equality or pointwise cross-fibre baseline is asserted.

## 3. Section 9 consequence

Literal `Y(F_i)` sets are nested and may double-count.  For a singleton-pole
characteristic path, assign each critical-value cluster to its unique first
separation edge.  The resulting exit sets `E_i` are disjoint.  Apply
`(C7.1*)` once to their union, together with the separate x-side `psi`
cluster.  This gives the repaired Statement 9.4 bounds used in the audited
row-4 graph.

The rest of the reviewed Section 9 assembly is local and unchanged:

- `td<=5` gives a singleton pole and table row in `{1,4,5,7,10}`;
- rows `1,5,7,10` have pinned `M=1` at a nonroot pole and die by corrected
  Proposition 8.4;
- row 4 dies by the repaired transition graph, finite-exit argument, and
  the restored first-separation/`psi` budgets;
- no root use of Proposition 8.4 occurs.

Thus the campaign-internal Section 9 reconstruction of `td>=6` is no longer
conditional on an open Section 7 lemma.  The printed thesis proof remains
incomplete and must not be cited as the proof.

## 4. Consumer boundary

The repair licenses these singleton-chain inequality consumers:

- Statement 9.4 / 9.5 exit budgets after first-separation ownership;
- H3q/`psi` budgets;
- the repaired row-4 and hence `td>=6` reconstruction.

For two or more pole chains, a separate global first-exit partition must
still prove cross-chain disjointness after shared suffixes are identified.
Corollary 7.1 applies to a distinct union once that is done; the singleton
ownership theorem does not do it automatically.  Thus the old shared
two-pole budget remains conditional on this multipole no-duplication lemma.

The repair also does **not** license equality consumers.  In particular, MP8's deduction
that identified `M=1` regions contribute exactly zero to every possible
global ledger used printed `(22)` as an equality.  Actual cluster weights
can jump upward at exceptional quotient points.  Local statements that a
specified exit set is empty or has `lambda_F=0` remain valid, but the global
"no refinement can charge" conclusion is not recovered by `(C7.1*)`.

Canonical files must therefore use two distinct labels:

```text
EXIT-BUDGET: AVAILABLE via actual weights + first-separation sets.
EQUALITY/MP8: QUARANTINED; (22) and (22-cl) are not restored.
```

## 5. Remaining campaign frontier

This integration removes one source-trust dependency but does not shrink the
main JC2 frontier by itself.  The live Sigray tasks are the reviewed
root-aware recensus and the multi-pole resonant-jump/landing problems.  Full
configuration landing, `RPMC(C)`, a cofinal degree or topological-degree
ceiling, and the possibility of a counterexample remain open.
