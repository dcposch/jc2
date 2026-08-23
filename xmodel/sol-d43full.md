# Fully reconstructed D43 residue-A family

**Date:** 2026-08-23

**Status:** **INTERNAL / UNREVIEWED / MOD-\(p\)**

**Scope:** residue A, representative fiber a00pp, fixed Sigray scale
\(B=84\), no-log, PIN42, \(W_1W_2\ne0\), at
\(p=105337,105673\). This is not a characteristic-zero lift, a formal germ,
or a polynomial Keller map.

## Verdict

The fully reconstructed family ideal is

\[
 I_{43}^{\rm full}=
 \langle 34\text{ parked},\ 95\text{ graph rows in bands }6\ldots24,
 \ 89\text{ graph rows in bands }26\ldots42\rangle
 \subset \mathbf F_p[184\text{ variables}].
\]

It is **NONEMPTY at both banked primes**. At each prime an exact-slice
linear basis decodes to an explicit \(184\)-coordinate point satisfying all
\(218\) generators. The same point passes the independent full survivor
gate: all \(184\) selected pristine residual coefficients are zero,
nu_window is null (the \(\nu\ge43\) gate), and all 18 executable floor checks
pass.

Thus D43 is **not** a first depth kill at fixed \(B=84\). This is the requested
live residue-A carrier / A-SCALE counterexample signal. It is only modular
and fixed-scale: it does not disprove A-SCALE and does not supply an
unbounded tower or a characteristic-zero realization.

The floor result is

\[
 \ell^+\ge37.
\]

The recorded value 37 is a certified window lower bound, while e_plus is
still tagged E_PLUS_CANDIDATE with certified = null; it is not an equality
claim. Since \(2\cdot37+1=75\), D75 is the first possible depth for the named
Newton certification. At D43 the threshold is 21 and the witness is above
it.

## Exact census and reconstruction

The omitted layer has the exact rung census

| band | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| old graph rows | 9 | 10 | 9 | 9 | 10 | 10 | 9 | 10 | 10 | 9 | **95** |

These are the \(76\) D21 window rows, 10 pristine Row-22 rows, and 9
band-24 frontier rows. The previous bad witnesses reported 94 nonzero old
coefficients because one of these 95 rows happened to vanish; 94 was a
witness failure count, not the generator census.

The late graph census is

| band | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 42 | total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| late graph rows | 10 | 10 | 9 | 10 | 10 | 10 | 10 | 10 | 10 | **89** |

The union ring remains exactly 184 variables: 28 parked coordinates and 156
graph coordinates. The 52 banked late compatibility rows are exact constant
left-kernel combinations of the 89 late graph rows. They are audit
redundancies. Retaining them gives a 270-row presentation; the
nonredundant tested presentation has 218 rows.

For both primes the reconstruction audit verifies:

- parked prefix: 34/34 rows and the banked parked-file SHA-256;
- restored old graph: 95/95 rows loaded from the ten byte-hashed reduced
  checkpoints for bands 6--24;
- late graph: 89/89, with the canonical expanded-row hash exactly equal to
  the prior graph emission;
- late compatibility: 52/52 rederived from the graph, with the canonical
  expanded-row hash exactly equal to the prior compatibility emission;
- corrected union variable census: 184/184.

The per-prime audit JSON files contain every checkpoint path/hash, row term
census, and the old/late/compatibility aggregate hashes.

## Exact-slice route

No full expanded D43 system was passed to msolve.

The reusable driver first specializes the certified parked component with
all 14 \(\mathbb A^{14}\) coordinates zero and the replay-certificate fourth
roots for \(W_1,W_2\). Exact evaluation of all 184 graph rows gives a
156-variable point bank with 107,665 terms and degree at most 6. This full
point bank is used only for direct replay.

Canonical origin-Jacobian prefix slices solve linearly through band 34. The
band-34 point already replays every graph row through band 38 (164/164). At
band 40 exactly nine rows are nonzero. The continuation construction keeps
all 174 prefix rows through band 40, fixes the 43 nonpivot graph coordinates
to the band-38 center, and retains the canonical 101 pivot coordinates:

| prime | stored rows | nonzero solver rows | variables | terms | degree | input SHA-256 |
|---:|---:|---:|---:|---:|---:|---|
| 105337 | 174 | 165 | 101 | 55,947 | 6 | 1e67d9f9d457db2a9b789966545404e45d8c16d78a1c724434dba2d6829e0ee1 |
| 105673 | 174 | 165 | 101 | 55,947 | 6 | 10b07f407588f17aab00208c6334486f85f34c67c8cc4fe29c9f2460b1cf7c6e |

msolve 0.10.1 was used only on these small exact slices
(-g 2 -t 16 --random-seed 843). The runs took 281.56 s and 297.81 s.
Each reduced basis has 101 completely linear elements and 123 terms. The
decoded points replay all 174 unsliced prefix rows; without adding another
equation they also make all ten band-42 rows zero. Direct replay therefore
gives 184/184 graph rows, not merely slice-row vanishing.

## Certificate and gate replay

The two certificates give the same exact profile:

| gate | 105337 | 105673 |
|---|---:|---:|
| parked equations | 34/34 | 34/34 |
| old graph, bands 6--24 | 95/95 | 95/95 |
| late graph, bands 26--42 | 89/89 | 89/89 |
| full ideal | 218/218 | 218/218 |
| selected pristine residuals | 184/184 | 184/184 |
| executable survivor/floor checks | 18/18 | 18/18 |
| s9_d43_residual_184_zero | PASS | PASS |
| s9_nu_ge_43 | PASS | PASS |
| floor eligible | yes | yes |
| \(\ell^+\) lower bound | 37 | 37 |

At each point the parked Jacobian rank is 14 and the graph Jacobian rank in
the 156 graph coordinates is 111. These are exact subranks; no global
dimension claim is made for the full ideal. The negative control
tf1_57 += 1 breaks 18 graph rows at each prime.

The independent floor replay additionally records, at both primes,
alpha=beta=0, window rank \(125\), \(M_2\)-rank \(17\), and
\((\delta^+_{N_1},\delta^+_{N_2})=(26,43)\). All D21/D23/D25 reconstruction
residuals and all rung residuals are zero before the floor is accepted.

## Artifacts and replay

- cases/d43_full_family.py: assembler, census/hash audit, point and pivot
  slices, continuation, linear-basis decoder, full replay, and floor gate.
- cases/d43_full_audit_p{105337,105673}.json: exact source census and hash
  regressions.
- cases/d43_full_slice_p*.{ms,out,err,json}: the only solver inputs and their
  completely linear bases.
- cases/d43_full_pointbank_p*.pkl: all 184 point-specialized graph rows used
  for independent unsliced replay.
- cases/d43_full_certificate_p*.json: explicit full 184-coordinate points,
  218-row replay counts, Jacobian subranks, and negative controls.
- cases/d43_full_floor_p*.json: all 18 survivor/floor checks and the
  \(\ell^+\ge37\) record.

The decisive replay command is the driver's --final-certificate mode; it
parses the linear basis, evaluates every point-bank graph row and every raw
parked row, runs a coefficient perturbation, reconstructs the operator point,
and invokes the independent D43 survivor/floor gate. Any mismatch is a hard
assertion failure.

## Honest interpretation

**MOD-\(p\) decision:** the fully reconstructed representative residue-A D43
family is NONEMPTY at both banked primes, with explicit full-gate witnesses.

**A-SCALE signal:** anti-A-SCALE / live carrier signal. The fixed \(B=84\)
residue-A carrier survives through D43; there is no D43 first-depth kill.

**Not proved:** characteristic-zero nonemptiness, inverse-limit survival,
algebraization, globalization, polynomial Keller realization, or unbounded
Sigray scale. The artifacts support none of those promotions.
