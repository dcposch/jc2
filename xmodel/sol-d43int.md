# D43 recovered-checkpoint integral/smoothness gate

**Date:** 2026-08-23

**Prime:** (p=105337), residue-A fiber `a00pp`; recovery regression also at
(p=105673)

**Status:** **MODULAR SOURCE/NF FIDELITY PASSES; STAGE 2 OPEN**

## Verdict

The recovered `cases/d43red/` files close the missing **modular polynomial**
audit.  Fresh replay at both primes certifies the exact 184-variable,
218-row census

\[
34\text{ parked}+95\text{ old graph}+89\text{ late graph},
\]

including every checkpoint hash and the old/late canonical row hashes.  At
(p=105337), the pristine symbolic source bank was independently rebuilt and
all reductions were rerun with traces retained.  The result is

\[
\boxed{184/184\quad R_{\rm raw}
=R_{\rm NF}+\sum_j Q_jG_j\quad\text{over }\mathbf F_{105337}},
\]

with dictionary-exact agreement against every recovered checkpoint.  The
replay covers 24,882,668 grouped raw terms, 38,871,970 NF terms, and
102,883,725 quotient-trace terms.  Its aggregate trace hash is

```text
59f795b6489b3ecafa316bbf75a6d4bce318812fac868da479e047f7314170ed
```

This does **not** produce the requested common integral 218-row model.  Every
recovered checkpoint has exactly the payload keys

```text
band fiber gbvars prime rows
```

and contains no trace or integral coefficient data.  The regenerated identity
above stops at the 509-element D23 basis over (mathbf F_p).  The repository
still has no common integral/(mathbf Z_p) 34-row parked presentation derived
from the source radical algebra, no membership of those 509 reducers in such
integral parked generators, and hence no integral or (p)-adic
source-to-parked NF identity.  Lifting the displayed prime-specific
coefficients as least residues would define an unverified model.

The local smoothness gate also remains open.  The exact linear data are
unchanged:

\[
\operatorname{rank}J_{218}(\bar x)=131,\qquad
\dim T_{\bar x}=53,\qquad \det M=810\ne0\pmod {105337}.
\]

A new bandwise local-normal-form engine avoids `std` and proves localized
generation on the fixed 156-variable parked graph fiber through band 32.  It
uses nested pivot rows, normalizes their distinct linear leading monomials,
and invokes the product criterion; dependent rows in bands 6--32 all reduce
exactly to zero.  At band 34 the two dependent rows with global indices 142
and 143 did not return a normal form within 300 seconds.  This is a timeout,
not a nonzero remainder.  More importantly, this calculation fixes all 14
parked-cell coordinates, so even a completed 156-variable fiber certificate
would not by itself prove local dimension 53, generation by 131 equations in
the total 184-variable local ring, or (p)-flatness.

Therefore there is no standard-smooth certificate, Stacks 02H6 cannot be
invoked, and no (mathbf Z_p)-point or characteristic-zero point is certified.

\[
\boxed{\textbf{FIRST CERTIFIED CHAR-0 D43 POINT: NOT OBTAINED; STAGE 2 OPEN.}}
\]

## 1. Recovered 218-row modular model

Fresh recovery audits pass at both primes:

| gate | (105337) | (105673) |
|---|---:|---:|
| parked rows | 34/34 | 34/34 |
| old graph rows, bands 6--24 | 95/95 | 95/95 |
| late graph rows, bands 26--42 | 89/89 | 89/89 |
| variables | 184 | 184 |
| full rows | 218 | 218 |

Canonical hashes are:

| object | (105337) | (105673) |
|---|---|---|
| parked file | `ef6db7e9ad36666537475fabf8238887de0c7e6d8f02c9381eaa7c810cbe4fe2` | `43b81c4ea5f77a5d0d32f433a23e867e9ef4c7228f5d6e7624f43561aa976175` |
| old graph rows | `3cbb13d166529c043502ccc070692e610357c4dcab99ccf337b2296b41803651` | `d681bc8f36372cecadcb5cee6ffc95e8d4ef3657e0baf9c60196daa95da7c85f` |
| late graph rows | `43dc1d54e121e25fe03a6f95ab4666fc6d117c3835dc971c050af9209af15807` | `1f72d049b1ec50c64ffa22b1a15d47f7f9c664cb0e7c8bf52a67ee8654f94d3e` |
| late compatibility rows | `536e2c3fe5516ae51adeb456477d4546d4820eeb369db1e32290d9191f9af59a` | `60b20bee7fa418d22eb598638d91ae3446790470fd4bc3e2745c3efaf22c1205` |

The checkpoint rows are therefore recovered and internally consistent.  This
is an exact modular presentation, not a common characteristic-zero emission.

## 2. Full modular source-to-NF trace replay

`build_tails_modp.py` rebuilt the 189-variable pristine symbolic source bank
at (p=105337): 184 Euler cells, with the odd-band, surplus-(eta), and
congruence gates all passing.  The raw-bank SHA-256 is

```text
19a4f73ce8dd271406610fc2e716eea583e259ce6478abf8580b895a9ed4588a
```

`d43_nf_trace_replay.py` then parsed the shipped 509-element D23 basis,
regrouped each raw row exactly as the checkpoint producer did, and for every
base coefficient:

1. recomputed the normal form and quotient trace;
2. reconstructed (R_{\rm NF}+\sum Q_jG_j) coefficient-by-coefficient;
3. compared the reconstruction with the raw coefficient dictionary;
4. compared the NF dictionary with the recovered checkpoint.

All 184 rows pass both identities.  This fixes the principal ambiguity left
by `sol-clift.md`: the recovered graph polynomials really are the tested
source reductions modulo the D23 ideal.

The remaining ambiguity is one level earlier.  (G_1,\ldots,G_{509}) and the
34 parked rows are prime-specific modular objects here.  No artifact writes
them over the Hensel-selected radical ring or expresses the (G_j) through
integral parked generators.  Consequently the modular trace cannot be lifted
by choosing integer representatives.

## 3. Integral and (p^2) boundary

The positive source-model result from `sol-clift.md` remains exact.  The
coefficient radicals are simple-root Hensel lifts in the selected
(mathbf Z_p) embedding:

\[
r_3^2=3,\quad \zeta_{42}^{42}=1,\quad
A_1^3=3+r_3,\quad A_2^3=3-r_3,\quad 2h^2=3.
\]

The 184 pristine source equations have rank profile (129=129) in the
first correction system, and the explicit 24-coordinate correction replays
184/184 rows modulo (p^2).  This is a source-model (p^2) point.

What is still absent is an all-218 computation in one integral 184-coordinate
ring retaining the (W_i), their inverse/radical laws, and the integral
right sides of (W_i^4=\mathcal A_i).  In particular, the following were not
computed and are not implied by the modular trace:

- \(F_{218}(x_1)/p\) in a common integral presentation;
- the parked-coordinate columns of its integral correction matrix;
- an all-218 corrected replay modulo (p^2);
- integral syzygies identifying the NF presentation with the source model.

Thus Step 1 of the algebraization gate remains **not certified**, although
its full modular source/NF subgate now passes.

## 4. Dimension, generation, and flatness

The unit (131\times131) minor proves only the rank statement.  To test the
origin without another blind standard-basis run, `d43_local_fiber.py` works
bandwise on the 184 point-specialized graph equations.  At each prefix it:

- retains a nested set of original independent rows;
- selects a unit Jacobian minor;
- uses constant row operations to give distinct pivot-variable leading
  monomials in a local degree order;
- applies the product criterion, so no `std` call is needed;
- reduces only the newly dependent rows.

The exact transcript is:

| band | prefix rank | increment | dependent rows | result |
|---:|---:|---:|---:|---|
| 6 | 1 | 1 | 8 | PASS |
| 8 | 3 | 2 | 8 | PASS |
| 10 | 3 | 0 | 9 | PASS |
| 12 | 6 | 3 | 6 | PASS |
| 14 | 10 | 4 | 6 | PASS |
| 16 | 14 | 4 | 6 | PASS |
| 18 | 18 | 4 | 5 | PASS |
| 20 | 22 | 4 | 6 | PASS |
| 22 | 28 | 6 | 4 | PASS |
| 24 | 32 | 4 | 5 | PASS |
| 26 | 38 | 6 | 4 | PASS |
| 28 | 46 | 8 | 2 | PASS |
| 30 | 54 | 8 | 1 | PASS |
| 32 | 64 | 10 | 0 | PASS |
| 34 | 72 | 8 | 2 | **TIMEOUT (no remainder)** |

The nine band-10 identities are therefore not, by themselves, a hidden
quadratic cut on this fixed fiber: all nine are locally generated by the
earlier nested pivots.  The calculation does not complete band 34 and does
not include the 14 parked directions.  Hence none of

\[
\dim\mathcal O_{X,\bar x}=53,\qquad
I_{\bar x}=\langle f_1,\ldots,f_{131}\rangle_{\bar x},\qquad
p\text{-flatness}
\]

is certified.

No claim is made that the component is everywhere singular.  The timeout is
computationally inconclusive.  A less degenerate point on the same modular
component remains a valid route, but it must be searched in the full
14-free parked cell and replayed against all 218 rows.

## 5. Artifacts and replay

- `cases/d43_integral_recovery_audit_p{105337,105673}.json`: fresh recovered
  checkpoint audits.
- `cases/d43modp_p105337_a00pp_rebuilt.pkl`: rebuilt pristine symbolic source
  bank.
- `cases/d43_nf_trace_replay.py` and `cases/d43_nf_trace_p105337.json`: exact
  184-row modular membership replay and trace digests.
- `cases/d43_local_fiber.py` and `cases/d43_local_fiber_p105337.json`: bounded
  bandwise fixed-fiber local-generation attempt.
- `cases/d43_integral_gate.py` and `cases/d43_integral_gate_p105337.json`:
  fail-closed consolidated verdict.

Recovery audits:

```bash
python3 cases/d43_full_family.py --audit \
  --ckdir cases/d43red --root cases --prime 105337 \
  --out cases/d43_integral_recovery_audit_p105337.json
python3 cases/d43_full_family.py --audit \
  --ckdir cases/d43red --root cases --prime 105673 \
  --out cases/d43_integral_recovery_audit_p105673.json
```

Raw source rebuild and full trace replay:

```bash
python3 cases/build_tails_modp.py \
  --prime 105337 --fiber a00pp --depth 43 --validate-points 0 \
  --out cases/d43modp_p105337_a00pp_rebuilt.pkl
python3 cases/d43_nf_trace_replay.py \
  --raw cases/d43modp_p105337_a00pp_rebuilt.pkl \
  --gb cases/directionb_det23_gb_p105337.out.txt \
  --ckdir cases/d43red --workers 3 \
  --out cases/d43_nf_trace_p105337.json
```

Bounded local attempt and consolidated gate:

```bash
python3 cases/d43_local_fiber.py \
  --timeout 300 --out cases/d43_local_fiber_p105337.json
python3 cases/d43_integral_gate.py \
  --out cases/d43_integral_gate_p105337.json
```

Expected final line:

```text
D43 integral gate: modular fidelity PASS; integral/local smooth gates OPEN
```

## Final tier

**New exact result:** the complete recovered 218-row modular presentation is
audited at both primes, and at (p=105337) every pristine graph row has a
replayed source-to-D23-NF membership trace matching the recovered checkpoint.

**Still not obtained:** a common integral 34+184 presentation, an all-218
(p^2) replay, local dimension 53, localized generation by 131 equations,
(p)-flatness, standard smoothness, a (mathbf Z_p)-point, or a
characteristic-zero D43 point.

The next bounded algebraization move is to re-emit the D23/D25 parked system
over the source radical number ring (or (mathbf Z_p)) with
reducer-to-parked traces.  Then rerun bandwise local membership in the full
14-free cell; if band 34 remains the bottleneck, move to a non-origin point
of that same modular component before attempting any family-wide singular
deformation analysis.
