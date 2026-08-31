# Hostile review: conductor-10/16 genus-ladder S4 obstruction (fresh)

**Referee:** Grok 4.6 (independent, hostile).
**Date:** 2026-08-31.
**Charge:** one-place `S4` obstruction packet for conductors 10 and 16.
**Mode:** frozen read-only inputs; no promotion; no ledger edit; no `jc2-lean` inspection; no CAS.

## 0. Hash verification

Frozen copies were hashed with SHA-256 in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.lxZ2k3/inputs`.
All six charged files match the assignment:

| file | sha256 |
|---|---|
| `block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md` | `e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863` |
| `...sol56-20260831.md.artifact.json` | `373aa3b1790084848710291d09b5b4af7840818242833a6faf94f71b44c1b33f` |
| `block_descent_a1_genus_ladder_s4_replay.py` | `a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a` |
| `block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md` | `03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa` |
| `block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md` | `03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4` |
| `block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md` | `070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5` |

Hash check: **pass**. The independently fetched arXiv `1407.0490v1` PDF hashes to
`05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9`, matching the
packet. Review proceeds.

## 1. Overall verdict

**CONFIRMED** at the packet's exact charged scope. Under the already charged
one-place interfaces (1.1) and the quartic transposition monodromy, no reduced
irreducible `A1`-normalized affine plane curve can have `Delta_aff` equal to 5
or 8. The four infinity knots are the complete reduced delta-sequence census
at conductors 10 and 16, and every sign/mirror version has zero labelled
full-`S4` meridian-transposition colourings.

No claim is REFUTED. No load-bearing GAP was found in the census, the
cabling dictionary, the signed satellite braid, the full-image filter, or the
stated scope. The theorem remains strictly conditional on the charged
meridian-preserving surjection and does not assert existence or non-existence
of the curves themselves. This is not an exit-price assertion.

## 2. Reduced delta-sequence axioms and recursion

**Attack.** Mis-transcribe Assi--Garcia-Sanchez so that either (i) the
reducedness inequality is too strong and a sequence is dropped, (ii) it is too
weak and a non-reduced or multi-place sequence is admitted, or (iii) the
Section 5 recursion misses a length-four row at conductor 16.

**Primary source.** Before Proposition 13, a sequence `(a0,...,as)` is a
delta-sequence when:

1. `Gamma=<a0,...,as>` is free in that order (`e_k a_k` lies in the preceding
   semigroup, with `e_k` minimal);
2. `a_k D_k > a_{k+1} D_{k+1}` for `1<=k<=s-1`, where `D1=a0` and
   `D_{k}=gcd(D_{k-1},a_{k-1})`;
3. `a0 > a1 > D2 > D3 > ... > D_{h+1}=1`.

Proposition 2(iii)--(iv) is the same Newton inequality in the `r,d` labels,
together with conductor `C=sum_k (e_k-1)r_k - r0 + 1`. The packet's (1.2) is
clause 3 verbatim. The replay's `is_delta_sequence` checks `r0>r1>d2`, strict
decrease of the gcd tower to 1, freeness by semigroup membership of
`e_k r_k`, and `r_k d_k > r_{k+1} d_{k+1}` for `1<=k<h`. Indexing matches:
packet `d1=r0`, so the first Newton comparison is `r1 r0 > r2 d2`, which is
the paper's `k=1` instance. First-step freeness is automatic (`e1 r1` is a
multiple of `r0`); later steps are not. Minimality of `e_k` follows from
`gcd(r_k/d_{k+1}, d_k/d_{k+1})=1` together with `d_k` dividing the preceding
semigroup, so membership of `e_k r_k` is the exact free-semigroup test.

The stronger Opus wording `r_k/d_{k+1}>=2` at every stage is not in the paper.
The paper's reduced chain forces it at `k=1` (`r1>d2` and integrality), not
later. Replacing the stronger wording by (1.2) is the correct interface. Desk
enumeration below shows it does not change the conductor-6/8/10/16 lists.

**Recursion.** Section 5 of the paper is exactly the packet's (2.1)--(2.3):

- `h=1`: `C=(r0-1)(r1-1)`;
- `h>1`: `C=d_h C_prefix + (d_h-1)(r_h-1)` from Proposition 4(ii) at `k=h`;
- `2<=r_h<=C-2` (Frobenius is not a generator; the paper excludes only
  `<3,2>`, which is one-stage);
- `2<=d_h<=C/(r_h-1)+1`;
- `gcd(d_h,r_h)=1`;
- prefixes are themselves reduced delta-sequences of conductor `C_prefix`.

The last point is not an extra hypothesis: if `(r0,...,rh)` is reduced then
so is `(r0/d_h,...,r_{h-1}/d_h)`. Every reduced sequence of length `>2` arises
this way, so the recursion is finite and complete. The `h<=log2(g+1)` bound
is used only as a finiteness remark; the implementation does not cap length
and will emit a four-term sequence if one satisfies the axioms.

**Conductor-14 control.** Example 18 prints, for Frobenius number 13
(conductor 14), the ten sequences

```text
(6,4,11), (8,3), (8,6,3), (9,6,5), (10,4,7),
(12,8,3), (12,8,6,3), (15,2), (15,6,2), (15,10,2).
```

Desk recursion from (2.1)--(2.3) plus the exact axioms reproduces this list
with nothing extra: one-stage `(15,2)`, `(8,3)`; then
`(6,4,11)`, `(10,4,7)`, `(8,6,3)`, `(9,6,5)`, `(15,6,2)`, `(12,8,3)`,
`(15,10,2)`, and the unique length-four row `(12,8,6,3)` obtained by scaling
`(6,4,3)` by `d_h=2` and appending `3`. The ordering test is sharp on
`(6,4,11)`: `4*6=24>11*2=22`. Dropping freeness or dropping the product
ordering therefore cannot leave Example 18 intact.

**Verdict.** Axioms, recursion completeness, and the published control:
`CONFIRMED`.

## 3. Conductors 10 and 16, and the four knots

**Attack.** A missing delta-sequence, a wrong reducedness cut, or a swapped
cable parameter.

**Conductor 10, desk.** One-stage: `(r0-1)(r1-1)=10` with `r0>r1>1` and
`gcd=1` yields only `(11,2)` (`(6,3)` is imprimitive). Two-stage with
`d=2`: `r2=11-2 C_prefix`. The only surviving prefix is conductor 2, namely
`(3,2)`, giving `(6,4,7)`. Freeness `14 in <6,4>` and Newton `24>14` hold.
Prefix conductor 4 gives `(10,4,3)`, which fails freeness (`6` not in
`<10,4>`). Larger `d` produce either a gcd failure or a non-integral
`r_h`. No length-four row exists (`g=5` allows `h<=2` anyway). Census:
`(11,2)`, `(6,4,7)`.

**Conductor 16, desk.** One-stage yields only `(17,2)`. Two-stage `d=2`:
`(6,4,13)` fails Newton (`24>26` is false); `(10,4,9)` survives (freeness
`18=10+2*4`, Newton `40>18`). Scaling the three conductor-6 prefixes by 2
and appending 5 kills all three by freeness, including the length-four
candidate `(12,8,6,5)` (`5` is the Frobenius of `<6,4,3>`). All `d>=3`
fail gcd or integrality. The genus bound `h<=log2(9)` permits a four-term
row; none exists. Census: `(17,2)`, `(10,4,9)`.

Both lists match (0.2) and the charged conductor-6/8 lists
`(4,3),(6,4,3),(7,2)` and `(5,3),(6,4,5),(9,2),(9,6,2)`.

**Cabling dictionary.** For a three-term sequence, `d=gcd(r0,r1)`, the
normalised prefix is the companion torus knot `T(r1/d,r0/d)`, and the last
stage is a winding-`d`, meridional-`r_h` cable. Thus

```text
(11,2)   -> T(2,11),
(6,4,7)  -> C_(2,7)(T(2,3)),
(17,2)   -> T(2,17),
(10,4,9) -> C_(2,9)(T(2,5)).
```

Schubert's formula independently matches conductors: `g(T(2,11))=5`,
`g(C_(2,7)(T(2,3)))=2*1+6/2=5`, `g(T(2,17))=8`,
`g(C_(2,9)(T(2,5)))=2*2+8/2=8`. The swapped winding `C_(7,2)(T(2,3))` has
genus 10 and is not a candidate. The companion `T(3,2)` is the same knot as
`T(2,3)`. The dictionary is the same one used for the charged `(6,4,3)` and
`(6,4,5)` rows.

**Embedding versus abstract semigroup.** Example 18 records that several
delta-sequences can generate one Abhyankar semigroup. The obstruction must
kill sequences, not semigroups: different characteristic data can give
different iterated cables. The replay enumerates sequences. Assi's converse
(Section 4) realises every delta-sequence by a one-place polynomial, so the
census is exactly the set of reduced plane embeddings of conductor `C`, not
an abstract-coordinate-ring list. Unreduced presentations are stripped by
the reducedness clause and, by the paper's Theorem 14, do not produce a new
equivalence class of embeddings. This is the right object. There is no
embedding-versus-abstract overclaim.

**Verdict.** Censuses and (0.3): `CONFIRMED`.

## 4. Signed satellite braid, closure, and Alexander

**Attack.** Wrong block switch, wrong blackboard-framing correction
`q-2n`, or a left/right Artin convention that computes colourings of a
different knot.

The permutation braid of the block swap `[0,1,2,3] |-> [2,3,0,1]` bubble-sorts
to the word `(2,3,1,2)`, i.e. `X=sigma2 sigma3 sigma1 sigma2`, matching (3.1)
and the charged genus-three formula `X_2=s2 s3 s1 s2`. The zero-framed
winding-two cable of the two-braid companion `sigma1^n` is then
`X^n sigma1^(q-2n)`: the blackboard 2-parallel of writhe `n` contributes
`2n` to the meridional parameter, and `sigma1` supplies the remaining twists
inside one block. Negative letters invert the word. This is the `p=2` case
of the charged genus-three convention
`W_(p,q,epsilon)=X_p^(3 epsilon) (s1...s_(p-1))^(q-3 epsilon p)`.

The Artin action `sigma_i:(A,B)|->(A B A^{-1},A)` and its inverse
`(A,B)|->(B, B^{-1} A B)` are the standard Hurwitz generators; the replay
implements them literally. Closure of `T(2,q)` is a 2-cycle for odd `q`;
closure of each charged four-strand satellite word is a 4-cycle. Both are
knots, as required.

The reduced-Burau numerator is checked, up to Laurent units, against
`Delta_T(2,q)(t) Delta_T(2,n)(t^2) * (1-t^4)`, which is Schubert/Seifert's
cable formula times the four-strand `(1-t^n)` factor. The torus factor
`(t^q+1)/(t+1)` for odd positive `q` is the alternating `1,-1,...,1`
polynomial used in the replay. Palindromicity means Alexander does not
separate a braid from its inverse, so the sign sweep is essential; it is
present (both companion signs and both meridional signs). Alexander does
separate a swapped dictionary: `C_(2,7)(T(2,3))` and `C_(2,3)(T(2,7))` have
unequal Alexander degrees `(6+4)` versus `(2+12)`. A wrong framing
`q-n` or a `sigma3` twist in the opposite block would not match the cable
polynomial. The eight charged sign/mirror words all pass.

**Verdict.** Convention, closure, and Alexander control: `CONFIRMED`.

## 5. Full-S4 counts and the winding-two residue theorem

**Attack.** A full-image filter that discards a genuine `S4` colouring; an
inexact `*6` conjugacy multiplier; a residue reduction that is not an
identity on the state space; or a determinant-only inference that cannot
kill `C_(2,9)(T(2,5))`.

Two transpositions in `S4` generate a subgroup of order at most 6 (`C2`,
`C2xC2`, or `S3`). Desk, not enumeration. A two-bridge knot therefore admits
no transitive transposition image on four letters. This kills `T(2,+/-11)`
and `T(2,+/-17)` without counting, and the two-strand enumeration returns
zero as a control. The graph-floor (a connected transposition graph on `d`
vertices needs at least `d-1` edges, hence meridional rank at least 3 in
degree 4) is the same observation and is not used for the satellites.

For a four-strand closed braid, Wirtinger meridians are the strand colours.
Fixing the first colour at `(12)` and multiplying by 6 is exact on the
full-`S4` locus: simultaneous conjugation acts freely (centre of `S4` is
trivial once the colours generate `S4`) and transitively on the six
transpositions, so each 24-element conjugacy orbit contributes exactly four
`(12)`-normalised colourings and the labelled total is `6` times the
normalised count. The filter `|G|=24` is equivalent, for transposition
generators, to transitivity on four letters: a transposition-generated
proper subgroup of `S4` is intransitive or of order at most 6.

The replay reports labelled counts

```text
T(2,+/-11), T(2,+/-17):                 0
C_(2,+/-7)(T(2,+/-3)), four versions:   0,0,0,0
C_(2,+/-9)(T(2,+/-5)), four versions:   0,0,0,0
```

Determinant is not a substitute. The parent double-cover lemma only forces
`3 | det`. One has `det T(2,q)=q` and `det C_(2,q)(T(2,n))=|q|`, so
`T(2,11)`, `T(2,17)`, and `C_(2,7)(T(2,3))` die by determinant, but
`C_(2,9)(T(2,5))` has determinant 9 and is a genuine determinant survivor.
The load-bearing zero is that cable. The packet's refusal of
determinant-only inference is necessary.

**Residue theorem.** On all `6^4` transposition four-tuples the action of `X`
has order 12 and the action of `sigma1` has order 6 (replay). Therefore the
colouring count of `X^n sigma1^(q-2n)` depends only on `n mod 12` and
`(q-2n) mod 6`. Restricting to odd residues (the knot case) gives an exact
`6 x 3` table. The replay's table is

```text
(n mod 12, q mod 6) | 1  3  5
                 1  | 0  0  0
                 3  | 0 72  0
                 5  | 0  0  0
                 7  | 0  0  0
                 9  | 0 72  0
                11  | 0  0  0
```

The unique odd residue of `q` divisible by 3 is `q≡3 mod 6`; the unique odd
residues of `n` divisible by 3 are `n≡3,9 mod 12`. Thus there is a full-`S4`
transposition colouring if and only if `3|n` and `3|q`, and the labelled
count is then exactly 72. This is (4.2)--(4.3). The charged conductor-6
survivor `C_(2,3)(trefoil)` is the cell `(n,q)≡(3,3)`, count 72, matching
the charged genus-three table under the same Artin/`X_2` convention. The
two new rows miss for different reasons: `7` is not divisible by 3, while
`5` is not. Desk check of the reduction for the load-bearing cable:
`C_(2,9)(T(2,5))` is `X^5 sigma1^(9-10)=X^5 sigma1^{-1}`, and
`(9-2*5) mod 6 = 5`, which is the action of `sigma1^5` since `sigma1` has
order 6, i.e. the cell `(n,q)≡(5,3)`.

The theorem is only about winding-two cables of two-braid companions. It is
not an all-genus obstruction. Conductor 6 and 8 already show the boundary
sieve is sporadic: `C_(2,3)(trefoil)` and `C_(3,2)(trefoil)` survive it.

**Verdict.** Every charged colouring count, the `*6` multiplier, the
full-image filter, and (4.2)--(4.3): `CONFIRMED`.

## 6. Meridian surjection and maximum-safe scope

**Attack.** Promote a knot-group vanishing to an affine-complement vanishing
without the charged surjection, or silently enlarge the statement to
existence of curves, reducible branches, or JC2.

The charged total-delta packet supplies, for any reduced irreducible
one-place `A1` curve, not merely for small genus,

```text
g_3(K_infinity)=Delta_aff(B),
K_infinity is an iterated cable and is prime or trivial,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians.
```

Zariski--van Kampen imposes each finite braid relation; the boundary only
imposes their product. Individual relations imply the total one, so a
transitive transposition representation of the affine complement pulls back
to one of the infinity-knot group. Contrapositive: zero knot colourings
forbid the charged quartic boundary representation. The present packet
does not re-prove (1.1). It consumes it honestly.

**Weakest exact hypotheses.** Let `B` be a reduced irreducible complex
affine plane curve with `normalization(B)=A1`. Assume the three charged
interfaces (1.1). Assume `pi1(A2-B)` admits a transitive representation to
`S4` sending every positive generic meridian to a transposition. Then
`Delta_aff(B) != 5` and `Delta_aff(B) != 8`.

No `b1(B)=1` hypothesis is used (unlike the charged genus-three and
genus-four packets). That is a genuine strengthening at these two
conductors: the group-theoretic screen already kills every one-place row.

**Maximum-safe non-claims**, all of which the packet states:

- One-place curves with affine delta 5 or 8 may exist; they cannot carry
  this monodromy.
- Reducible branches, several places at infinity, non-`A1` normalisation,
  nonminimal rank-four packets, higher-rank blocks, and JC2 are untouched.
- Winding-three and deeper iterated rows at other conductors are not
  governed by (4.2).
- No finite algebraic cover, polynomial map, or Keller map is constructed.

There is no flag/place/series identification, no floor-as-attainment, and no
exit-price assertion.

**Verdict.** Implication and scope: `CONFIRMED`. The theorem is not a new
proof of (1.1); blast radius if (1.1) is withdrawn is the entire (0.1).

## 7. Replay, optimisations, and mutations

The frozen script was run as

```text
python3  .../block_descent_a1_genus_ladder_s4_replay.py
python3 -O  ...
python3 -OO ...
```

All three exited 0 with byte-identical stdout SHA-256

```text
b2a4418172aab4834fef9b1e09cffa2e921132770e4029d6f532e8c6b3ee437c
```

matching the packet. Checks use `require()`, not `assert`, so `-O`/`-OO` do
not strip the gates. Recomputed payload hash before inserting the hash field
is `1061ea3423bd77c208419f39beb3ad0a597b4ee85865f539ed67b90228fe50ba`,
matching both the stdout field and the packet. Status string
`PASS-A1-GENUS-LADDER-CONDUCTOR-10-16-S4-OBSTRUCTION`. Runtime was a few
seconds; no CAS was invoked.

Mutations, each exiting 1 at the intended gate:

| flag | exit | gate |
|---|---:|---|
| `--mutate-drop-freeness` | 1 | `exact recursive delta-sequence censuses` |
| `--mutate-drop-ordering` | 1 | `exact recursive delta-sequence censuses` |
| `--mutate-promote-cable-coloring` | 1 | `all conductor-10/16 cable sign rows have zero full-S4 colorings` |

The third mutation writes the conductor-6 count 72 onto `C(2,+7)(T(2,+3))`
after the genuine zeros are computed, so it tests the zero-gate rather than
the enumerator. That is the advertised gate.

**Verdict.** Replay claims: `CONFIRMED`.

## 8. Attacks that did not land

- *Missing length-four sequence at conductor 16.* The only candidate
  `(12,8,6,5)` fails last-step freeness. None other arises from the finite
  `(r_h,d_h)` box.
- *Wrong Newton inequality `r_k d_{k+1}` versus `r_k d_k`.* Packet indexing
  `d1=r0` matches the paper.
- *Swapped cable parameters `C_(q,2)` or companion/cable swap.* Genus and
  Alexander both reject the swaps.
- *Blackboard framing `q-n` or opposite-block twists.* Cable Alexander would
  fail.
- *Full-image filter discarding a transitive transposition colouring.* No
  proper transposition-generated transitive subgroup of `S4` exists.
- *`*6` overcount from a nontrivial colouring centraliser.* Full `S4` has
  trivial centre.
- *Determinant-only kill of `C_(2,9)(T(2,5))`.* Determinant 9; the residue
  cell `(n,q)≡(5,3)` is the actual kill.
- *Abstract-semigroup overclaim.* Sequences, not semigroups, are listed;
  Assi Example 18 is precisely the warning that these differ.
- *Promotion to non-existence of the curves, or to JC2.* Explicitly refused.

The residual methodological limit is that the four-strand labelled counts
were reproduced by running the charged enumerator, not by a second
independent permutation library. Computation rules forbade writing one.
Mitigations: the two-bridge zeros are desk; the 72-cell agrees with the
charged genus-three table under the same convention; Alexander pins the
satellite; the residue reduction for `(5,9)` was checked by hand.

## 9. Correction, blast radius, next falsification

**Correction.** None. The Opus-to-paper reducedness correction is already in
the packet and is right.

**Blast radius.** If the charged meridian-surjection (1.1) is withdrawn,
(0.1) falls in full and the colouring table remains only a knot-group
statement. If the winding-two residue theorem were false, the load-bearing
loss would be the conductor-16 cable (the other three rows still die by the
two-bridge or determinant arguments). A missed delta-sequence at conductor
10 or 16 would open a hole in (0.1) of size one row; none was found.

**Best next falsification test.** Independently enumerate labelled full-`S4`
transposition colourings of the single four-braid `X^5 sigma1^{-1}` (the
zero-framed word for `C_(2,9)(T(2,5))`) with a different realisation of the
Hurwitz action (opposite composition convention, or `S4` as a permutation
matrix group). One colouring refutes the load-bearing zero. A cheaper
positive-control variant is the cell `(n,q)≡(3,3)`, which must remain 72
under the same change. Do not extend (4.2) by analogy to winding three.

## 10. Per-claim verdicts

| claim | verdict | attack shown |
|---|---|---|
| Reduced axioms (1.2) equal Assi before Prop. 13 | CONFIRMED | compared to `a0>a1>D2>...>1`, freeness, Newton |
| Recursion (2.1)--(2.3) complete | CONFIRMED | transcription of Section 5 plus Prop. 4(ii); prefix reducedness |
| Conductor-14 Example 18 | CONFIRMED | desk recursion equals the printed ten-row GAP list |
| Conductor-6/8 charged lists | CONFIRMED | desk |
| Conductor-10 census `(11,2),(6,4,7)` | CONFIRMED | desk; `(10,4,3)` fails freeness |
| Conductor-16 census `(17,2),(10,4,9)` | CONFIRMED | desk; `(6,4,13)` fails Newton; `(12,8,6,5)` fails freeness |
| Knot dictionary (0.3) | CONFIRMED | prefix torus plus winding-`d` cable; Schubert genus matches `C/2` |
| Braid (3.1) and framing `q-2n` | CONFIRMED | block-switch bubble-sort; Alexander equals the cable formula |
| Closure is a knot on all eight sign rows | CONFIRMED | 2-cycle / 4-cycle |
| Two transpositions generate order `<=6` | CONFIRMED | desk `C2`/`V4`/`S3` |
| Torus rows have zero full-`S4` colourings | CONFIRMED | two-bridge floor, plus 2-strand count 0 |
| All four cable sign/mirror rows have count 0 | CONFIRMED | charged replay; residue cells `(3,1)` and `(5,3)` |
| `*6` first-colour multiplier | CONFIRMED | free `S4`-action, 24/6=4 normalised colourings per orbit |
| Full-image filter `|G|=24` | CONFIRMED | no proper transitive transposition subgroup of `S4` |
| Action orders of `X`, `sigma1` are 12, 6 | CONFIRMED | replay on all `6^4` states |
| (4.2)--(4.3): colourable iff `3\|n` and `3\|q`, then 72 | CONFIRMED | exact `6x3` odd-residue table; cells `(3,3)` and `(9,3)` |
| Determinant is not used, and cannot kill the `(10,4,9)` row | CONFIRMED | `det=9` |
| Meridian-surjection implies (0.1) from knot vanishing | CONFIRMED | charged (1.1); packet does not re-prove it |
| Maximum-safe scope / non-claims | CONFIRMED | no existence, no reducible, no JC2, not all-genus |
| Embedding versus abstract semigroup | CONFIRMED | sequences not semigroups; Assi Theorem 14 / Example 18 |
| Normal/`-O`/`-OO` stdout hash | CONFIRMED | `b2a44181...437c`, byte-identical |
| Payload pre-insert hash | CONFIRMED | `1061ea34...50ba` |
| Three mutations exit nonzero at named gates | CONFIRMED | census gate; census gate; zero-colouring gate |
| (0.1) as a theorem under the weakest hypotheses of §6 | CONFIRMED | census complete and every row has zero colourings |

<!-- BODY-END -->
