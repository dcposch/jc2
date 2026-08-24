# Hostile different-model review: `AS3-MIN-W2` / `W2-SURVIVOR`

**VERDICT: CONFIRMED.**

Every mathematical identity in the bounded claim was independently recomputed
by this reviewer with a third implementation (dense-array polynomial
arithmetic, own exterior-derivative conventions, three independent
Teichmueller definitions) and every one holds exactly.  Both documented
enumerators byte-reproduce their frozen artifacts from a fresh scratch
directory, `verify.py` passes in place and from a full scratch copy, all
hashes (manifest, provenance, embedded, canonical) are current, and the
preregistration's filesystem birthtime precedes the producer code itself.  No
sign error, bracket-convention error, restricted-correction-space mistake, de
Rham-quotient misuse, marked-point lift failure, or hidden support/cap change
was found.  No failing identity exists to report.

**Promotion guidance.**  Bank `W2-SURVIVOR` at exactly the stated tier:
one explicit polynomial Keller-collision lift over `Z/9` on the fixed
characteristic-three support, namely `(P2,Q2)=(x+8x^3, y+3x^2y)` with
`[P2,Q2]=1+27x^2+72x^4 == 1 (mod 9)` and the marked collision
`(0,0),(1,0) -> (0,0)` persisting with distinct sources modulo 9.  The only
licensed campaign-level update is that the promoted characteristic-two
Mondello-stratum first-Witt obstruction (`xmodel/sol-witt.md`, verdict SOUND
in `xmodel/grok-witt-review.md`) does **not** extrapolate as a blanket
first-Witt obstruction to all odd primes/supports.  Do not promote any `W_3`,
compatible all-Witt tower, bounded-support persistence (the correction already
grows the support by `x^2y`), `Z_3`/characteristic-zero, germ, or JC2
language; any `W_3` attempt is a new preregistered cap.  Caveats C1-C4 below
are non-blocking transparency notes, none touching a claim clause.

---

## 1. Reviewer identity, environment, perimeter

- Reviewer: Claude Fable 5 (model id `claude-fable-5`), Anthropic Claude
  Code CLI / Claude Agent SDK session, independent of the OpenAI Codex
  producer session.  Review executed 2026-08-24T03:02:06Z through
  2026-08-24T03:09:52Z.
- Host: macOS 14.6 (Darwin 23.6.0, build 23G80), zsh, Python 3.9.6
  (same interpreter class the artifacts document; `pow(x,-1,p)` requires
  3.8+, satisfied).  No network access used; no CAS used.
- Basis: `HEAD = 8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4` (branch `master`),
  identical to `provenance.json:base_commit`.
- Dirty perimeter at review time: tracked modifications
  `APPROACHES.md, AUDIT.md, COORDINATION.md, PROGRESS.md, pilot-local.log`;
  ~50 untracked round-1/round-2 paths including
  `cases/round2_witt_oddprime/` itself (0 tracked files in the case
  directory, so no git history exists for any case artifact — relevant to
  the timestamp audit in §5).
- Writes by this review: this file only.  Scratch work in
  `/tmp/w2rev.Y1o679` (ephemeral; its checklist output is transcribed in §4).
  No frozen artifact was overwritten; no shared ledger touched; no `W_3`
  computation performed; support never broadened.

## 2. Exact commands run

```text
python3 cases/round2_witt_oddprime/search.py --output $TMP/results.json
python3 cases/round2_witt_oddprime/replay.py --input cases/round2_witt_oddprime/results.json --output $TMP/replay.json
python3 cases/round2_witt_oddprime/replay.py --input $TMP/results.json --output $TMP/replay-fresh-input.json
python3 cases/round2_witt_oddprime/verify.py
# plus a full scratch copy (cases/ + the xmodel report) under $TMP/scratch,
# then: python3 $TMP/scratch/cases/round2_witt_oddprime/verify.py
python3 $TMP/reviewer_check.py        # reviewer's independent recomputation
shasum -a 256 -c cases/round2_witt_oddprime/MANIFEST.sha256
stat -f '%SB | %Sm | %N' cases/round2_witt_oddprime/* xmodel/round2-witt-oddprime-20260824.md
```

Results: fresh `results.json`, `replay.json`, and replay-on-fresh-results are
**byte-identical** to the frozen artifacts (`diff` empty three times);
`verify.py` prints `VERIFY PASS` both in place and from the scratch copy,
with producer/independent hashes equal to the report's quotes.

## 3. Artifact hashes (all verified current)

MANIFEST.sha256 verified 8/8 against on-disk bytes:

```text
af9917fe117c84a92ab9738c1d258d636354cec63cdc81e5e5bd1cbe4f6269e3  PREREGISTRATION.md
08493aa37d816612b0e051ca869ed59f6f414279bd59fb67a3a12ebe81b33da4  provenance.json
0620ecec6d49eec037292c57fb8f9e93983ae14f9888e573609a2bff0168ac3b  search.py
bb02c36fcd8356529b1d188fa61760bbfd6194fafcd050740752a795abd5201c  results.json
fd7eafad21e29f951baa107ab5fed9d134790a7f44d49b5e38e205fdf8cdaf32  replay.py
2285ade3f46eb9fb22cffb1af0c950776e8c1f9ee89e94a92e8a4495571d5341  replay.json
1ee9a5c764326e198316e429365c9d25c72d7e3bf87f29ef7605ce6c5e31d29a  verify.py
09b901f2a27f825a627da2ad0835d1875212716693769d505ab465b04bae6ff1  xmodel/round2-witt-oddprime-20260824.md
```

Reviewer-recomputed canonical digests (sorted-key compact JSON, SHA-256),
equal to the stored fields and to the report's verbatim quotes:

- producer canonical claim: `875682b644f367ee8b841d3e433b8706b3f95a25bb1200b6f20395faa8f7dff9`
- independent core: `9ee96b84ac81f36f921235987bcfcf33a71484a5e5a93aba4757f81efcdb834c`
- `replay.json:producer_result_sha256` equals sha256 of `results.json` bytes.
- Embedded `preregistration_sha256`/`provenance_sha256` in both JSONs equal
  the current files.  `provenance.json` sources verified 7/7 (including
  `cases/witt_check.py`, `xmodel/sol-pcurvature.md`, `xmodel/sol-witt.md`,
  `xmodel/grok-witt-review.md`, `xmodel/review-round1-proof-gates-claude.md`,
  both ideation files).  MANIFEST itself is the case's root of trust and is
  pinned nowhere else (expected; noted).

## 4. Independent derivations (reviewer's third implementation)

47/47 checks passed (`REVIEWER RECOMPUTATION: ALL CHECKS PASS`).  Fixed
conventions: `[F,G] = F_x G_y - F_y G_x`; `d(g dx) = -g_y dx^dy`,
`d(g dy) = g_x dx^dy`.  Highlights, clause by clause:

**Clause 1 (cap and census).**  The frozen text contains exactly `p=3`,
`P_a = x + a x^3`, `Q = y`, order `a=1,2`, supports `S_P={(1,0),(3,0)}`,
`S_Q={(0,1)}`, marked data `r0=(0,0)`, `r1=(1,0)`, `c=(0,0)`.  Exact-support
completeness: `a=0` kills the `x^3` monomial, so `{1,2}` is the whole
coefficient family (with the `x`-coefficient and `Q` normalized in the frozen
text; both are also canonically normalizable by target scaling).  Census:
`[P_a,y] = 1 + 3a x^2 == 1 (mod 3)` exactly as a polynomial, both values;
`F_1(1,0) = (2,0) != (0,0)` so `a=1` fails only the marked collision
(`rejected_at: marked-collision` accurate); `F_2(1,0) = (3,0) == (0,0)` so
`a=2` enters.  Matches frozen rows exactly.  **Holds.**

**Clause 2 (special fibre at `a=2`).**  Jacobian exactly the constant
polynomial 1 over `F_3` (not merely pointwise).  Generic degree: scaling
`2x^3+x-U` by `2^{-1}=2` gives the monic relation `x^3+2x+U=0` (verified
identically under `U = x+2x^3`), so `F_3[x,y]` is a free
`F_3[U,V]`-module on `1,x,x^2`.  Rank <= 3: the rewrite `x^3 -> x+2U` closes
(machine-verified by substitution for `x^3..x^8`).  Rank >= 3: `1,x,x^2` are
`F_3[U]`-independent — machine-verified exhaustively for all 19,682 nonzero
coefficient triples of `deg_U <= 2`, and in general because
`deg_x(U^d x^i) = 3d+i` determines `(d,i)`.  Hence generic degree exactly 3
with basis `1,x,x^2` — a module-rank computation, **not finite-point
counting**.  Separability: `dP/dx = 1+6x^2 == 1 (mod 3)` exactly (clause's
"separable derivative one"), equivalently the fibre cubic has unit derivative
`2`.  Marked points `(0,0) != (1,0)` collide onto `(0,0)`.  **Holds.**

**Clause 3 (Teichmueller, error, class, correction).**  Three independent
definitions agree that `[2]=8` in `Z/9`: unique `w == 2 (mod 3)` with
`w^3 == w (mod 9)` (brute force over all 9 residues: only 8); Frobenius
formula `2^3 mod 9 = 8`; multiplicativity `[2]^2 = 64 == 1 = [2*2 mod 3]`.
`[1]=1`.  Then `[x+8x^3, y] = 1+24x^2` exactly over `Z`; every coefficient of
`[P~,Q~]-1` is divisible by 3 both integrally and inside `Z/9`, and both
divisions give `E = 2x^2 (mod 3)`.  Top two-variable class: `E` has no
monomial with `i == j == 2 (mod 3)`; constructively,
`E dx^dy = d(x^2 y dx)` since `-d(x^2y)/dy = -x^2 == 2x^2 (mod 3)` — the
class vanishes by explicit primitive, independent of the basis theorem.
Correction equation derived independently: with `P2 = P~+3A`, `Q2 = Q~+3B`,
the exact `Z`-identity
`[P~+3A, Q~+3B] = [P~,Q~] + 3([A,Q~]+[P~,B]) + 9[A,B]`
(machine-verified on a four-pair test family) gives
`[P2,Q2] == 1 (mod 9)  <=>  E + [A,Q] + [P,B] == 0 (mod 3)`.
Verification of the witness: `A=0`, `B=x^2y` gives
`[A,Q]+[P,B] = B_y·P_x = x^2(1+6x^2) == x^2 = -E (mod 3)`, so
`E+[A,Q]+[P,B] = 3x^2 == 0`.  **Holds.**  (Forcing: within any correction,
the `x^2`-coefficient of `[A,Q]+[P,B]` can only come from the `x^2y` term of
`B` — the `A`-route needs `A ∋ x^3` whose derivative coefficient `3 == 0` —
so `B ⊇ x^2y` is structurally forced; producer and replay agreeing on
`(0, x^2y)` is necessity, not coordination.)

**Clause 4 (explicit lift).**  Dense integer arithmetic:
`[x+8x^3, y+3x^2y] = (1+24x^2)(1+3x^2) = 1 + 27x^2 + 72x^4` exactly over
`Z`, and `27 == 72 == 0 (mod 9)`, so the determinant is exactly 1 modulo 9.
`P2(1,0) = 1+8 = 9 == 0`, `Q2(1,0) = 0`, `F2(0,0) = (0,0)`: both distinct
marked points still map to `(0,0)` mod 9 and reduce to their residues mod 3.
Exhaustive lift banks (all nine lifts of each residue) confirm `(0,0)` is a
common image and the emitted witness is valid.  All frozen records
(`P2_mod9`, `Q2_mod9`, `determinant_exact_over_Z`, `determinant_mod9`,
`A_mod3`, `B_mod3`, `lifted_points_mod9`, `lifted_target_mod9`) match.
**Holds.**

**Clause 5 (separateness, hashes, fresh replay).**  `search.py` (sparse
dicts, de Rham primitive + unimodular-frame transport, lift-bank search) and
`replay.py` (term lists, independent census, own Teichmueller loop, 24-column
modular row reduction, direct witness verification) share no code and use
different algorithms for every load-bearing step; the shared bracket
convention and Teichmueller definition are the specification, not code reuse.
Reviewer's own elimination with **reversed** side and monomial orders
reproduces rank 10 (and the closed-form image span
`{y^j, xy^j : j<=2} ∪ {x^i, x^i y : i<=3}`, exactly 10 monomials) and the
same forced particular solution `B=x^2y`.  The replay's restricted 24-column
box is a witness-finder only — legitimate for an existence verdict; the
producer's construction is unrestricted.  Hashes/manifests current (§3);
byte-identical fresh replays and scratch-copy `VERIFY PASS` (§2).  **Holds**
(see caveat C2 on the generic-degree constants).

**Clause 6 (interpretation boundary).**  Report §5 asserts exactly one
bounded statement and explicitly excludes: bounded-support compatible tower
through all Witt levels, `W_3`, `Z_3`/integral lift, characteristic-zero
descent/algebraization, polynomial germ, JC2 counterexample — and flags that
the correction itself grows the support (`x^2y`), killing any
bounded-support-persistence reading.  The licensed update (char-2
Mondello-stratum obstruction does not extrapolate blanketly to odd
primes/supports) is correctly scoped against a real promoted object:
`xmodel/sol-witt.md` proves NEVER-VANISHES on its registered char-2 stratum
(`W_2(F_2)=Z/4`), verdict SOUND in `xmodel/grok-witt-review.md`; a char-3
`W_2` survivor refutes only the blanket extrapolation, not that theorem.
Producer report and `PROGRESS.md` row both use the bounded language;
prereg's forbidden list (no `F_5` after survivor, no `W_3`, no support
enlargement, no char-0 inference, no network) is respected by the artifacts:
`values_screened=[1,2]`, stop `first-W2-survivor` at the last cap value,
nothing modulo 27 anywhere, stdlib-only imports.  **Holds.**

## 5. Preregistration timestamp audit

APFS birthtimes (PDT = UTC-7, converted):

```text
PREREGISTRATION.md  born 2026-08-24T02:47:27Z   mtime 02:52:12Z
provenance.json     born 2026-08-24T02:47:27Z   mtime 02:52:12Z
search.py           born 02:49:19Z              unmodified
replay.py           born 02:50:59Z              unmodified
results.json        born 02:51:10Z              mtime 02:52:26Z
replay.json         born 02:51:22Z              mtime 02:52:26Z
verify.py           born 02:52:49Z              unmodified
report (xmodel)     born 02:53:35Z              unmodified
MANIFEST.sha256     born 02:53:52Z              unmodified
```

Findings: the corrected header value `02:47:27Z` equals the filesystem
birthtime **exactly**, and the preregistration predates not only both result
files (+3m43s to `results.json` — the report's "about four minutes" is
accurate) but the producer code itself.  The admitted erroneous first header
(`03:18:00Z`) would have *postdated* the results — i.e. the error was
self-undermining, and the correction moved the header to the verifiable
truth.  The 02:52:12Z edit is disclosed in the header; the 02:52:26Z
regeneration of `results.json`/`replay.json` is exactly what refreshing the
embedded `preregistration_sha256` requires, and the canonical-claim hash is
structurally independent of the prereg text (recomputed: unchanged), so the
correction could not have altered the banked mathematics.  Determinism was
verified by byte-identical reruns.  Residual limit (C1): the case directory
is untracked, so content-freeze between 02:47:27Z and 02:52:12Z beyond the
disclosed header line rests on the birthtime evidence, the disclosure, and
the fact that the two-value cap's *complete* census is independently
recomputed — even a hostile reading leaves no room for cherry-picking within
this cap.  Non-blocking.

## 6. Provenance / dedup audit (typed control, not an invented family)

- `xmodel/sol-pcurvature.md:142-148` records `F_AS = (x - x^p, y)` as the
  campaign's decisive negative control: Jacobian one, finite etale of degree
  `p`, not an automorphism.  At `p=3`, `x - x^3 = x + 2x^3`: the `a=2`
  survivor **is** the typed control; the cap is its exact-support coefficient
  family.
- `xmodel/review-round1-proof-gates-claude.md:301-304` independently verified
  the control's Keller/finite-etale/degree-`p`/nonautomorphism properties
  (Artin–Schreier `T^p - T - P` with unit derivative).
- `xmodel/sol-witt.md` + `cases/witt_check.py` are characteristic-two only
  (`W_2(F_2)=Z/4`, Mondello hull-plus-shell, collision `(0,1),(1,0),(1,1) ->
  (0,1)`); the odd-prime `W_2` question was genuinely open in-repo.
- Hostile repo-wide grep for `W_2(F_3)`, `Z/9`, `mod 9`, `Teichm*` outside
  this case: only `PROGRESS.md:115` (a coordination row about this very run,
  correctly bounded) and `xmodel/grok-census11a-review.md:21` (an unrelated
  `25 ≡ 7 (mod 9)` residue check in another lane).  No prior char-3 Witt
  computation exists.  Dedup claim **holds**.
- `xmodel/ideation-20260824T0156Z-dedup.md:94,203,279` types the lane as
  existing avenue 19 with exactly this scope ("new support choice, W2
  obstruction computation ... a finite-field survivor or scoped negative
  census only"); `xmodel/ideation-20260824T0156Z-synthesis.md` (§3 and the
  W-root row) licenses "one fixed odd-prime/other-support W2 cap,
  different-model replay of any survivor, first survivor or cap exhaustion;
  no W3/support expansion" — all respected.

## 7. Attack log (all negative)

1. **Sign/bracket-convention error** — recomputed everything under my own
   conventions, including the exterior-derivative signs and the
   `A dQ - B dP` frame transport (`A = -P_y U + P_x V`, `B = -Q_y U + Q_x V`,
   valid because the frame determinant is `[P,Q]=1`); the end-to-end exact
   integer determinant `1+27x^2+72x^4` leaves no convention slack.  Negative.
2. **Restricted-correction-space mistake** — producer's primitive-transport
   is total on exact forms (unrestricted); replay's box is a witness-finder;
   `B ⊇ x^2y` is forced (§4, clause 3); rank 10 confirmed under reversed
   elimination order.  Negative.
3. **De Rham quotient misuse** — image of the linearization equals exact
   2-forms exactly (both inclusions via the unimodular frame); the survivor
   direction uses only constructive exactness, exhibited as
   `E dx^dy = d(x^2 y dx)`; the Cartier `i==j==2 (mod 3)` support is used
   only as the basis screen and is the standard `H^2_dR(A^2)` basis (Kunneth
   from `H^1_dR(A^1)`).  Negative.
4. **Marked-point lift failure** — direct evaluation, distinctness,
   residue-reduction, and exhaustive 9x9 lift banks all pass; notably the
   Teichmueller lift alone already sends `(1,0)` to `(9,0) == (0,0)`.
   Negative.
5. **Hidden support/cap change** — enumerator literally iterates `(1,2)`
   over fixed monomial dicts with an exact-support predicate; no `F_5`, no
   `W_3`, no enlarged special-fibre support in any artifact; the lift's
   `x^2y` growth is the disclosed correction, permitted by the frozen text
   and flagged in the boundary.  Negative.
6. **Post-hoc preregistration** — §5: birthtime precedes producer code and
   results; correction disclosed and equals verifiable truth; canonical hash
   invariant.  Negative (with non-blocking limit C1).

## 8. Caveats (non-blocking)

- **C1** Freeze-verifiability limit inherent to untracked files: see §5.
  Recommend committing preregistrations (or hashing them into a tracked
  ledger) before running future caps.
- **C2** The generic-fibre facts (`degree 3`, basis, separable derivative)
  are encoded as constants in *both* scripts; the report's "replay.py ...
  proves the triangular generic-fibre basis" overstates code that asserts a
  hand-proved certificate after checking `2^{-1}=2`.  The certificate itself
  (monic division after unit scaling) is valid and is now machine-verified by
  this review (rewrite closure + exhaustive independence).  Recommend future
  caps compute such certificates in code.
- **C3** A `PROGRESS.md` coordination row describes this result as under
  review with correct boundary language; noted for perimeter completeness
  (not a case-artifact defect; this reviewer did not touch it).
- **C4** `MANIFEST.sha256` is the case's unpinned trust root (standard for
  this campaign's layout); its contents were verified against disk here.

## 9. Scope restated

Confirmed exactly and only: within the frozen two-value cap on the inherited
Artin–Schreier support over `F_3`, `a=1` fails the marked collision; the
`a=2` datum `(x+2x^3, y)` is Keller with generic degree exactly three
(basis `1,x,x^2`, separable), its two distinct marked points collide, its
unrestricted first Witt obstruction vanishes (`E = 2x^2`, class zero with
explicit primitive), and `(x+8x^3, y+3x^2y)` is an explicit determinant-one
lift over `Z/9 = W_2(F_3)` retaining the marked collision with distinct
sources.  Nothing beyond the finite-field/`W_2(F_3)` tier is asserted or
licensed.
