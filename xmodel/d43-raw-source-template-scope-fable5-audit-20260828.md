# D43 raw-source/template scope — Fable 5 hostile audit

UTC: 2026-08-28T19:55Z  
Role: independent read-only audit through the authenticated Fable 5 CLI  
Verdict: **REPAIR**

## Scope verdict

The 184 pristine Euler/J rows through bands 6--42, together with the
coefficient radical frame, define the complete **finite raw-J truncation** on
the selected source coordinates.  They do not by themselves define the full
residue-A/template locus: `W1,W2` remain free and the E5/nonvanishing bridge
is absent.  This is a meaningful necessary-condition system, but its points
must not be called template-branch survivors without a separate gate.

The pristine presentation itself already enforces the low raw-J bands.
D21/D23/D25 reconstruction rows are not required for raw source existence;
they are required for NF-presentation equivalence, selection of the banked
normal-form section, and reuse of banked geometry.

## Minimal exact E5 bridge

Write `a1=3+r3`, `a2=3-r3`, `S_M=7^12/2^6`.  The literal corrected E5 pair
is

```text
4*(a_i-4)*HM
 + 243*S_M^3*(2*r3)^4*a_i^2*A_i*W_i^4 = 0,    i=1,2.
```

Eliminating the linearly occurring `HM` gives exactly

```text
E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4 = 0.
```

All relevant coefficients are units in characteristic zero and at the two
registered primes.  Therefore:

1. the E5 pair with existential `HM` is scheme-isomorphic to `E=0`;
2. given E5, `W1 != 0`, `W2 != 0`, and `HM != 0` are equivalent, so one unit
   row suffices;
3. `E=0` plus a W-unit condition is equivalent to the existence of a unit
   `HM` satisfying both E5 rows; and
4. E6 introduces `s1F` but no further W equation.  On an ambient carrying
   `s1F`, the explicit choice `s1F=(2^8/7^16)HM` satisfies
   `2^24 HM^3-7^48 s1F^3=0` and is a unit.

These statements hold over `C` and over the registered `Z/p^N` frames.  They
bridge only the displayed E5/E6/unit equations; they do not certify other
upstream or all-depth template conditions.

The clean localized finite template contract is consequently the 184 raw-J
rows plus `E=0` and one unit row, followed by literal reconstruction/replay of
E5/E6.  The inverse-chart extension with only two W-unit rows is still raw
and is not an E5 bridge.

## High-Hensel interpretation

A lift that solves only the 184 raw rows certifies one finite raw congruence
modulo `p^N` along its deterministic correction choices.  It does not certify
template membership beyond the last separately checked template gate.  A
failure of the raw Newton step or the E gate kills only that deterministic
branch unless the whole correction tree is covered; a pass is not
formal-smoothness, a `Z_p` point, or branch survival.

During this audit the concurrent producer revised
`cases/d43_source_high_hensel.py` to add a per-state E/W-unit gate.  Fable
independently checked the registered `p^2` point:

```text
p       = 105337
W1      = 10092159227 mod p^2
W2      =  4041263462 mod p^2
E       = 0 mod p^2
HM(E5)  =  5143408652 mod p^2, pole-consistent and a unit.
```

This is a genuine necessary template check through two digits.  Because the
Newton correction is still selected from the raw 184-row system, later E-gate
failure is possible and would be branch-local information only.  The v2
runner, preregistration, p2 reference, AWS harness, and report still require a
fresh coherent seal and independent review.

## Canonical ledger corrections

- Replace “complete finite-D43 source system” by “complete finite raw-J
  truncation”; the intended localized E5 source locus adds `E=0` and one unit
  condition.
- Do not call high-Hensel success “branch evidence” or “survival.”  It is a
  finite raw congruence with a separately replayed necessary E gate.
- Any local-generation/smoothness calculation intended for the template
  locus must use the E-extended Jacobian, not only the raw rank-129 Jacobian.
- The exact-sparse promotion contract must include nonvanishing; rows plus
  homogeneous E5 equations admit the degenerate W/HM-zero locus otherwise.
- Keep D21/D23/D25 reconstruction and the 509/184 traces in the separate
  NF-equivalence lane.

## Ranking

Keep D43 active, but rank the exact 22-support characteristic-zero route above
the high-Hensel probe.  Its decisive object is exact emission and solution of
the 184 raw rows together with the elimination-equivalent E/unit bridge,
followed by all-row and literal E5/E6 replay.  The high-Hensel lane is a
secondary fail-closed diagnostic.  NF equivalence remains parallel and lower
priority for existence.
