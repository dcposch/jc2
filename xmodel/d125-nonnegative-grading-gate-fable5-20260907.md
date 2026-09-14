# Fable gate: D125 straight-grading one-row no-go (producer 13e19b39)

2026-09-07 22:41–22:50 UTC. Independent mathematical gate of the producer
report `d125-nonnegative-grading-discriminator-astra-20260907.md` from the
frozen lane inputs only. **Verdict: every exact claim CONFIRMED; one cosmetic
correction; no failed line.** Own evidence in
`box/d125-nonnegative-grading-gate-fable5-20260907/` (literals.py,
reconstruct.py/.out, replay-runs.tsv, witness-replay*.json, custody.json).

## 1. Per-claim verdicts

1. **Ring and row are literal (CONFIRMED).** client.py fixes, for the
   `unequal` A polygon, the outer face `i+j==15` with zeros, the inner face
   `5i-7j==top` with `top=3`, and the constant (lines 136–144). 14c's N ring
   sets the lift parameter to 1 and A_(2,1)=k; 14t's S/I is unguarded with no
   z. The v-exponent −3 is negative, so `[u^0 v^-3]phi(A)` is a required
   negative row, whatever its Hermite status.
2. **Polygon, 33 free slots (CONFIRMED, one correction).** Convex hull of
   (0,0),(0,15),(9,6),(2,1) equals the FOUR half-planes i≥0, i+j≤15,
   5i−7j≤3, i≤2j on a wide box. The producer's three displayed half-planes
   omit i≥0: (−1,1) satisfies them but lies outside the hull. Harmless for
   monomial exponents and for the checker's box range(10)×range(16); count
   unchanged. Odd slots 44, fixed odd 11 (nine on the total face, (2,1),
   with (9,6) on both faces), free 33, (2,1) excluded on the inner face.
3. **Coefficient formula, 32 of 33 (CONFIRMED).** Closed form
   c_ij=(−1)^j C(j,(j−i+3)/2) agrees with a direct trinomial expansion of the
   single monomial image v^−i(v⁴u−v−v^−1)^j on all 44 odd slots. Only (0,1)
   gives zero. The row has 34 terms and equals the witness literal_row
   dict exactly; the free-slot list equals the witness list.
4. **Constant −2484 (CONFIRMED, two routes).** Binomial-theorem top face
   C(3,m) at (3m,15−3m) gives −5005, 2772, −252, 1. Independently
   H|_{u=0}=−v⁵−5v³−10v−9v^−1−3v^−3 cubed at v^−3 gives −135−1620−729.
5. **k coefficient −1 (CONFIRMED).** phi(g²p)=v²u−v^−1−v^−3 by full
   expansion.
6. **Infeasibility (CONFIRMED, slightly stronger).** For any integer weights
   with Q in degree 0, homogeneity of this one generator forces its degree to
   be 0 (constant) and wt(k) (k term); hence wt(k)=0. Negative wt(k) dies
   too; no other weight enters.
7. **Unspecialized three-row version (CONFIRMED).** With all 44 odd slots
   as variables the row has 43 terms including a_(9,6) with coefficient 1
   and a_(2,1) with coefficient −1. Pins a_(9,6)−1 and a_(2,1)−k then force
   wt(a_(9,6))=0=wt(a_(2,1))=wt(k).
8. **Abstract bridge (CONFIRMED as a conditional).** If I and k are
   homogeneous then J=I:k^∞ is homogeneous: k^N f∈I splits into homogeneous
   parts k^N f_e∈I. If S/J≠0 with all variable weights ≥0 and wt(k)>0, then
   kx=1 is impossible since every k·x_e has degree ≥wt(k)>0 while 1 has
   nonzero degree-0 part. So J+(k) is proper and, by the Nullstellensatz over
   Q, a geometric k=0 point of X exists, feeding 14t. Note the hypothesis
   S/J≠0 is exactly U≠∅, the open question; the bridge converts a k≠0 point
   into a boundary point and never creates one.
9. **Scope statements (CONFIRMED).** An inhomogeneous generator does not
   show that I lacks a homogeneous generating set, nor anything about
   recentered origins, abstract quotient gradings or filtrations. No guarded
   emptiness, boundary existence or all-degree consequence follows. The
   producer's (k,a−1) example is correct.
10. **ℓ control (CONFIRMED).** Restoring phi(p)=v⁴u−ℓv−v^−1 multiplies the
    (i,j) contribution by ℓ^((i+j−3)/2); constant ℓ⁶, k term ℓ⁰. Weights
    wt(ℓ)=1, wt(k)=6, wt(a_ij)=(15−i−j)/2 give a single row degree 6; the
    pin ℓ−1 is inhomogeneous. This matches the symmetry report's character
    (i+j−15) up to sign and shows the obstruction is created by the ℓ=1 pin.
11. **Controls (CONFIRMED, one custody caveat).** The checker's metadata
    path is repo-relative (`ROOT=HERE.parents[1]`); the flat charged path
    fails with FileNotFoundError, as recorded. I made two byte-identical
    scratch copies at the required layout (hashes in scratch-copies.sha256)
    and ran ten runs, normal and −O, each under 30 s wall, 25 s CPU, 512 MiB,
    `python3 -I -B`. All ten return codes and stdout hashes match replay.json;
    both plain witnesses are byte-identical to the frozen witness. A scratch
    `--record` reproduced the same witness; its replay.json differs from the
    frozen one in exactly the 8 mutation stderr hashes (16 diff lines, all
    stderr_sha256) because tracebacks print the absolute script path. Those
    stderr hashes are therefore not portable custody values. Zero Assert
    nodes by independent AST count. The four mutations change real objects
    (top pin value, lift sign, deletion of constant, deletion of k).
12. **Hashes (CONFIRMED).** All ten frozen inputs match the producer custody
    pins where pinned; witness-O.json (not in my inputs) is pinned equal to
    witness.json and my −O run reproduces that byte string.

**First failed line:** none.

## 2. Replay commands

```
S=/tmp/jc2-gate-fable5-scratch   # copies of frozen check.py/client.py at box/<name>/
(ulimit -v 524288; ulimit -t 25; timeout 30 python3 -I -B [-O] \
  $S/box/d125-nonnegative-grading-discriminator-20260907/check.py [--mutate-*])
python3 -I -B box/d125-nonnegative-grading-gate-fable5-20260907/reconstruct.py
```

Normal and −O stdout: `e6efd2c671f9c4ef8a1588d8a27b81b9fbaf993e5a7cc52a34af6357d50d2e2d`.
Mutation exits 1 with messages `actual fixed-face coefficient projection`,
`actual k monomial lift sign`, `actual constant-and-k infeasibility witness` (×2).

## 3. Current input hashes (sha256sum output)

    7ff4ca5dd3e38bdf8ef6623624774223f9f8594324d97c34db381e16492671de  check.py
    ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53  client.py
    6682fc5b0587cb407102480e41e855f37a8ea62fcd83bbefd515c25e80abf639  custody.json
    c454d950b7f7e81440c2999328840f38ad3e54df32b82acb1791e863f892ea6d  replay.json
    e6efd2c671f9c4ef8a1588d8a27b81b9fbaf993e5a7cc52a34af6357d50d2e2d  witness.json
    13e19b39ccc70cea0dd5fb71b307292f0469937b62b4b1a75bdf6d119c194b0f  d125-nonnegative-grading-discriminator-astra-20260907.md
    1fe149db1b5e8fd74598c948c681885451d8e86ce89d29964517da76c3df833b  d125-nonnegative-grading-discriminator-astra-20260907.md.artifact.json
    19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc  d125-parity-unit-normalization-astra-20260907.md
    6f9e63a8162af7c6d212363b62c368f9029b282fa8acbb65bcdc5d9cf81b72d3  d125-arc-closure-interface-astra-20260907.md
    9bed554644b1bd3c881ba4e289ea0950601ed6141677a45152577442fd477b12  d125-symmetry-discriminator-astra-20260907.md

## 4. Corrections and unreviewed scope

Corrections (frozen reports not edited): §1 "equivalently" needs i≥0 as a
fourth half-plane; replay.json stderr hashes are path-dependent.

Unreviewed: `ideation-20260907T2200Z-sol56.md` (Sol Card1) was not in my
inputs, so the exact wording of the proposal being refuted and the §4
history/novelty search are GAP (unverified, not disputed). The 14c unit
lemma, 14t arc argument and symmetry-report Hermite counts were consumed as
accepted, not re-proved. No B row, Jacobian row or other negative row was
examined. Whether I admits some homogeneous generating set, or whether a
recentered grading exists, remains open and is not claimed either way. No
full source, H³/A/B powers, CAS, LP, AWS or live peer material was used.
STOP/IDLE.

<!-- BODY-END -->
