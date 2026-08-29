# History-checksum correction to ideation round `20260828T1707Z`

Date: 2026-08-28T18:22Z  
Coordinator: `/root`  
Status: **CANONICAL CORRECTION; SEALED SYNTHESIS LEFT IMMUTABLE**

## Corrected disposition

The frozen synthesis `xmodel/ideation-20260828T1707Z-synthesis.md`
(`0002169e...`) incorrectly promoted `SUBST-TRANSPORT` as a new first
residue-A attack.  The proposed attack class is already present, at greater
depth, in the coefficient-level Sheet-6 program:

- `SHEET6-TEMPLATE.md` E4--E6 derives the rigid pole/merge coefficients
  `b=2*sigma/3`, `a1*a2=sigma^2/6`, `b2=3*sigma/4`, the pole top
  cancellation, the fourth-power pole pin, and conjugate lead coherence;
- `cases/template_lift.py` checks those identities exactly over
  `Q(sqrt(3))`;
- `SHEET6-R1.md`, `SHEET6-R1-Q2E5.md`, `SHEET6-R1-25LOCUS.md`, and their
  engines already transport the coefficient-level Puiseux data through
  multiple cancellation depths and isolate the unresolved nonlinear core;
- `SHEET6-R6.md` and its review retain four live structure genomes, not one.

Accordingly, `SUBST-TRANSPORT` is reclassified
**DUPLICATE / KNOWN ATTACK CLASS**, not a new avenue.  The synthesis remains
frozen for provenance; this addendum supersedes only that disposition and
its immediate execution queue.

## Source correction: the merge tower is not forced to stop at `h_1`

For the row-1 pole pair, the first resonant exponents are indeed
`(k_0,l_0)=(2,3)`, and

```text
J(f,h_1)=2g,                 h_1=g^2-s_0 f^3.
```

But this full identity does **not** imply that Proposition 4.2 stops at
`j=1`.  Its stop test is the bracket of the leading patterns
`J(f_F^+,h_{1,F}^+)`.  That bracket can vanish because the leading part of
`h_1` is still a power of `f_F^+`, while lower cross-terms supply the
nonzero full Jacobian identity.  An implication such as
`delta_1(G_m)=0`, or an equivalent leading-part stop theorem, is missing.

The exact counter-scenarios are the authoritative R6 survivors:

| structure genome | terminal member carrying `q` |
|---|---|
| minimal `(3,4)`, `m_{G_m}=1` | `h_1` |
| staged `(1,2)`, `m_{G_m}=2` | `h_2` |
| echo `(2,3)->(6,17)`, `m_{G_m}=2` | `h_2` |
| echo `(2,5)->(6,23)`, `m_{G_m}=2` | `h_2` |

Thus any unconditional `m_{G_m}=1` promotion is rejected.  This is a
source-index error, not a contradiction in Sigray's printed theory.

## Exact conditional replay

The follow-up report
`xmodel/sigray-residue-a-subst-transport-gpt56-20260828.md`
(`87cfc52b...`) correctly makes the minimal-genome hypothesis explicit.  On
that branch it constructs an exact simultaneous two-parent Laurent seed over
a finite extension of `Q(sqrt(3))`.  Both pole patterns, the merge pattern,
and the ODE constants coexist.  The associated cross-parent eliminant is
compatible over `C`.

This is a useful explicit survivor, not a kill and not a descent obstruction
for JC2.  It does not distinguish the three `m_{G_m}=2` genomes.  Its rigid
coefficient pins substantially reproduce TEMPLATE E4--E6; its literal
two-correction certificate may be reused as a regression control for future
minimal-genome R1 work.

## Restored residue-A frontier

The deepest existing exact carrier is not a new first-edge seed.  It is the
fully reconstructed fixed-`B=84`, `a00pp` D43 family:

- 184 variables and 218 rows (`34+95+89`);
- explicit points at `p=105337,105673` satisfying all 218 rows and the full
  D43 survivor/floor gate;
- `ell^+>=37` at this window, with no characteristic-zero, inverse-limit,
  germ, globalization, or Keller-map conclusion;
- at `p=105337`, a pristine 184-row source-model lift through `p^2` and
  exact rank `rank J_218=131`, tangent dimension 53;
- modular source-to-D23-normal-form fidelity reviewed at the stated scope.

The exact missing implication is a **common integral 218-row presentation**:
the prime-specific 34 parked rows and 509 D23 reducers have not been emitted
over the source radical/number ring, and their integral membership traces are
absent.  Therefore the source `p^2` lift cannot yet be transferred to all 218
assembled rows, and neither flatness nor standard smoothness nor a
characteristic-zero point follows.

The next residue-A action is consequently:

1. reuse the D23/D25 source and reducer lineage to emit the smallest common
   integral parked model with reducer-to-parked membership traces;
2. replay the existing 184 source rows and all 218 assembled rows through
   `p^2` in that one model;
3. only after that succeeds, attack localized generation/flatness or move to
   a less-degenerate point of the 14-free parked cell;
4. keep the four per-genome R1 nonlinear cores available as an independent
   proof-side lane, without re-running already solved E4--E6 transport.

This queue is subject to the D43 duplication/feasibility audit now in
progress.  D75 and `B=168` remain held; this correction does not authorize
either.

## Evidence hashes

| artifact | SHA-256 |
|---|---|
| frozen synthesis | `0002169e1030b257d15c73b803d369787f661a57d70150f4bfc35296b2aee9b8` |
| conditional transport report | `87cfc52baa3e4b06f2c3a841ad6017c062ded45456586cb1854120f35f4304f6` |
| `SHEET6-TEMPLATE.md` | `850bc9687966e0f871753540532f803d8a69e84217d67d6ed4260be0c00c4273` |
| `SHEET6-R1.md` | `ad63701bc1614dfd53edf99ade0e5c1743ceada3c9a9cdac38ef29a5e9701fe9` |
| `SHEET6-R1-Q2E5.md` | `ea322dfffa4944a3cc8fc59dee3ff7fff02462a219b74e7d9a1f5a093c46f7bc` |
| `SHEET6-R1-25LOCUS.md` | `c8d2b03a25c33940609deb4b57e609e5ccd13ad044dff09f6b1243a6b98e053a` |
| `SHEET6-R6.md` | `a8bdba74bc68d2a8591f34c9ab9182e22d528d17a6c1f8544ab2d2963ff842ad` |
| `SHEET6-R6-REVIEW.md` | `769912195e9f0682b8e749cc646c5fdf4f8d53333b99a5c526e8a23e3f75374d` |
| `template_lift.py` | `7342a72e90dc6f3177ff61c6475b31f27cf9cf5b4ce51c183f9619904da285eb` |
| `r6_window.py` | `9cf8ca4b4685db1e8069420ddb11a3dca2654db57a3b2ef1445700abb220f17e` |
| D43 full producer | `bb1c979ca67545307c843a6c5ce7b16566ce5055b2ed807e91d818ce6704ce5f` |
| D43 full hostile review | `29c9c6eb860a33ba1ec8e53902ca73207010729155abc5cac48a65253950dfcb` |
| D43 source `p^2` screen | `a0db71acc5a808fcbeb8d3398ded7bc97b1dff48915dd4f6b03c75030ca12c14` |
| D43 integral-gate report | `5201d5c880fe237500ee6ac394dc65fa9a783b521c9a034762e9c4cf9730997a` |
| D43 NF-fidelity review | `85501e3c0f8b05b0a415b008d8041061d45b8517967c2ea0df76d236fca12f05` |

No heavy local computation was run.  `jc2-lean` was not entered, listed,
searched, read, built, modified, status-checked, or controlled.
