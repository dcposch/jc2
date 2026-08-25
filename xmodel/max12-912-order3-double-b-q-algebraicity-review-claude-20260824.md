# Hostile different-model review — max12 `(9,12)` order-three double-`B` exact characteristic-zero algebraicity

| Field | Value |
|---|---|
| Claim under review | Frozen producer: on the normalized order-three double-`B` leaf `k=mu=0`, `nu=r6=1`, `r1=r2=r3=r4=r5=r7=0`, `3*p+10*r8=0`, the nonzero-`p` locus `J=I+(p*ip-1)` has an exact reconstructed characteristic-zero DRL basis whose initial ideal contains a pure power of every variable (staircase `1188`); the `p=0` slice is exactly two reduced curves; hence `p` is algebraic over `Q` at every coefficient-field point, every actual Keller trajectory has constant `p` and constant `r8=-3p/10`, and the reviewed terminal row `9*r8'=j/u!=0` empties the double-root-off-`W` leaf |
| Overall verdict | **INCONCLUSIVE** |
| Smallest failing identity | **none** — no mathematical error found; every independently checkable identity was verified and passed |
| Smallest missing certificate | a characteristic-zero certificate, from a second engine or explicit cofactors, that msolve's printed basis elements lie in `J` (the nine elements with leading monomials `p^5,x0^5,...,x5^5,q^6,ip^6` suffice) |
| Nature of the block | engine-trust caveat on `msolve 0.10.1` multi-modular reconstruction, **not** a defect in the mathematics; compounded this session by a reviewer execution gap (below) |
| Evidence tier | full hand re-derivation of input rows 1–3 from first principles; exact hand evaluation of rows 6 and 8 at the independently reviewed parity fibre point; mod-3 character and weight homogeneity of all eight rows; term-by-term `p=0` cross-match of all eight rows against the Grok-reconstructed slice; line-by-line code audit of the frozen verifier, generator, parent compiler, runner, and both Singular scripts; hand proofs of the grevlex comparator, staircase BFS completeness, slice primality/radicality, and the algebraicity-to-constancy implication; frozen attestations for everything execution-dependent |
| Reviewer / model | Claude (Fable 5, Anthropic). Different model family from the producer lane (OpenAI Codex, GPT-5 family) and from the consumed Grok (xAI) reviews |
| Repo | `/Users/dc/code/math/jc2`, dirty worktree; named artifacts untracked on top of HEAD `2e6104a` |
| Date | 2026-08-24 |
| Execution constraint | **No shell.** `Monitor`/`Bash` were denied in this session. No hash was recomputed here, no script was executed here, `result.out.gz` (23 MB) could not be decompressed here, and Singular could not be invoked here. Every execution-dependent statement below is explicitly labelled as a frozen attestation or a code audit, and a complete re-execution battery is staged at `/tmp/jc2_doubleb_review_20260824/` |

Read in full before any verdict: the producer report; all fourteen files of
`cases/max12_912_order3_double_b_q_gb_20260824/`; the pinned generator
`cases/max12_912_order3_nu1_probe_20260824/generate_double_b_msolve.py`; the
pinned parent compiler `cases/max12_912_order3_fibre_20260824/order3_fibre.py`;
the pinned runner `ops/aws_doubleb_run.sh`; both consumed reviews
(`…critical-value-norm-review-grok…`, `…nu-belyi-collision-boundary-review-grok…`);
the predecessor `…double-b-p-algebraicity-grok…` (`INCONCLUSIVE`); the probe
README; and the live coordination entries in `notes.md` (22:41Z–23:10Z).
No producer, case, prompt, canonical, coordination, or run file was edited.
Scratch lives only in `/tmp/jc2_doubleb_review_20260824/`.

---

## Verdict in one paragraph

The mathematics is clean end to end: the input ideal is byte-traceable and
hand-verified against the pinned compiler, the logical implication from
zero-dimensionality to the terminal contradiction is watertight with no
constant-field, nilpotent, embedded-component, saturation, or
field-valued-point loophole, the `p=0` slice certificate is exact and correctly
corrected, and the consumed reviewed inputs are the right ones at the right
scopes. The single unfinished obligation is the one the producer itself
brackets: nothing in the frozen package proves over `Q` that the 1,246 printed
polynomials — in particular the nine whose leading monomials are pure variable
powers — actually lie in `J`. That is exactly the class of debt on which the
sibling elimination package's hostile review stopped `INCONCLUSIVE` hours
earlier, and the campaign's own live log (`notes.md` 23:10Z) says "no double-B
trajectory kill is promoted yet" while second-engine characteristic-zero lanes
(`lift(...,"slimgb")` membership on r6c; `modStd`/`slimgb` on Box01/Box02) run.
Given additionally that this review session could execute nothing, the verdict
must be `INCONCLUSIVE` pending that certificate. I stress the asymmetry: this
is an engine-trust caveat with every consistency probe passing, not a detected
error.

---

## Attack 1 — hash chain and the frozen verifier

**Execution gap, disclosed:** `shasum -a 256 -c` and
`verify_result.py` were not run here (no shell). What was done instead:

- *Internal consistency of the pin lattice (byte-level reads):* the verifier's
  `EXPECTED` table equals `MANIFEST.sha256` line-for-line on all eight case
  files; `metadata.txt`'s `input_sha256`/`result_sha256`/`stderr_sha256` equal
  the manifest entries for `input.ms`, the uncompressed result, and
  `stderr.log`; `FREEZE.txt` repeats the report/registration/readme/verifier/
  replay/compressed/uncompressed/manifest hashes consistently; the launch
  prompt's four pins (report `ea849b39…`, manifest `f705e7df…`, freeze
  `1f5f0432…`, uncompressed basis `6ce7d394…`) match the corresponding
  records. The generator hash `5c1c6e6d…` and parent hash `a4fdac5d…` agree
  across four independent sites: manifest, metadata `source_sha256`, the
  verifier's asserts, and the generator's own `PARENT_SHA256` pin.
- *Code audit of `verify_result.py`:* it hash-checks all eight files, asserts
  the nine-variable first line and `0` second line, asserts exactly eight
  `",\n"` row terminators plus the `p*ip-1` tail, **re-runs the generator with
  the recorded flags and byte-compares its stdout to `input.ms`**, asserts the
  metadata and stderr needles, decompresses and hash-checks the 23,172,493-byte
  output, asserts the output header (characteristic 0, variable order
  `p,x0,…,ip`, graded reverse lexicographical, 1,246 elements), parses all
  1,246 polynomials with a loud-failure tokenizer (any wrapped line, rational
  coefficient, or alien token raises), recomputes every leading monomial,
  extracts the minimal pure powers with a dict equality that fails unless all
  nine variables appear, enumerates the staircase, and byte-replays both
  Singular scripts against their frozen outputs.
- *Hand proof that the verifier's order is right:* `grevlex_key(e) =
  (|e|, -e_n, …, -e_1)` compared lexicographically implements exactly DRL for
  `p > x0 > … > ip`: on equal degree, the first differing entry of the
  reversed-negated tuple is the rightmost differing exponent, and the monomial
  with the smaller exponent there wins — the textbook grevlex tie-break.
- *Hand proof that the staircase BFS is complete:* the standard monomials form
  an order ideal (closed under division), so every standard monomial `m≠1` has
  a standard predecessor `m/x_i`; induction gives reachability from `1`, and
  the `seen` set only prunes duplicates. Count `1188` is therefore correct *if*
  the parsed leading-monomial list is what the file contains — which the loud
  parser guarantees on a `PASS`.
- *Frozen attestation:* `replay.out` (manifest-pinned) records the expected
  `PASS` tail including `standard_monomials=1188`. That attests a producer-side
  execution, not one performed here.

The verifier deliberately does **not** check that the printed list generates
or is contained in `J`, and the README says so in so many words. That honesty
is correct and is the trust boundary of Attack 8.

## Attack 2 — the corrected input, traced to the pinned compiler

The shape assertions all hold on the read bytes: line 1 is exactly
`p, x0, x1, x2, x3, x4, x5, q, ip`, line 2 is `0`, rows 3–10 are the eight
double-`B` rows, row 11 is `p*ip-1`. The generator (audited) loads the
hash-pinned compiler, sets `k=0`, and emits
`tails[1..5]`, `tails[6]-1`, `tails[7]`, `10*tails[8]+3*p`, each cleared to a
primitive integer polynomial by a **positive** rational scalar (LCM of
denominators, then integer content) — ideal-preserving, sign-preserving. Since
the compiler's invariant-fibre constants are `r3=mu`, `r6=nu`, the equation set
is precisely the normalized leaf `k=mu=0`, `nu=r6=1`, `r1=…=r5=r7=0`,
`3p+10r8=0`. Nothing is missing and nothing extra is imposed (in particular
`W0!=0` is *not* imposed — see Attack 7 for why that is sound).

**Hand re-derivation, independent of the compiler.** With `K=z^3+pz+q`,
`f=K^3+φ`, `φ=Σ_{i≤5}x_i z^i` (so `a7=3p`, `a6=3q` exactly), the `k=0` tail is
`T = Σ_{q≥2} C(4/3,q) φ^q K^{4-3q}` (the `q=0,1` terms are polynomial), with
`C(4/3,2)=2/9`, `C(4/3,3)=-4/81`, `C(4/3,4)=5/243`; and
`r_ℓ = Σ_{j=1}^{ℓ} t_{-j}·[z(w)^{-j}]_{w^{-ℓ}}` with `z=w+c_1w^{-1}+…`,
`c_1=-a_7/9=-p/3`. Expanding `K^{-r}` at infinity and collecting:

- **Row 1** `= (27/4)·r_1`: all **10** printed terms match my derivation
  exactly, coefficients and signs (`3,3,3,-6,-6,-6,-3,-1,9,9`). This also
  equals Grok's independently reconstructed `27*r1` up to the content factor.
- **Row 2** `= (81/2)·r_2`: all **16** terms match exactly.
- **Row 3** `= (81/4)·r_3`, including the composition correction
  `r_3=t_{-3}+(p/3)t_{-1}`: all **20** terms match exactly (the `+48*x3*x5*p*q`
  term arises as `8/3 - 8/27 = 64/27` before clearing — a genuinely
  order-sensitive check).

**Structural checks on all eight rows.** Under the order-three character
`wt(x_i)=-i`, `wt(p)=2`, `wt(q)=0 (mod 3)`, every monomial of row `ℓ` has
weight `ℓ mod 3` (rows 6 and 8 including their constants `-243` and
`+19683p`, both of weight `0` and `2` respectively — consistent). Under the
`z`-scaling degree `deg(x_i)=9-i`, `deg(p)=2`, `deg(q)=3`, rows 1–5 and 7 are
homogeneous of degrees `13,14,15,16,17,19`; rows 6 and 8 are inhomogeneous
exactly by their normalization constants, with the self-consistent scales
`243=3^5` (so `-243 = 243·(r6-1)`'s constant) and `6561=3^8` (so
`+19683p = 6561·3p`).

**Exact numeric verification at an independently reviewed point.** The norm
review's parity fibre point (`x1=432, x3=36, x5=-36, x0=x2=x4=p=q=0`) carries
independently derived tails `nu=-(11/729)x3x5^3=25344` and
`r8=-x5^5/486=124416`. Evaluating the frozen rows by hand:

```text
rows 1,3,5,7: 0 trivially;  row 2: 18·432·36 - 6·36·1296 = 0;
row 4: 54·432² - 36·432·1296 + 36²·1296 + 5·36⁴ = 0;
row 6: -48·432·36·(-36) - 12·36³ + 12·36·(-36)³ - 243
     = 6,158,349 = 243·(25344-1)          [= 243·(nu-1)]  ✓
row 8: -3240·432²·(-36) - 3240·432·36² + 1080·432·(-36)³
       + 1620·36²·36² - 120·(-36)⁵
     = 8,162,933,760 = 6561·10·124416     [= 6561·(10·r8+3p)]  ✓
```

Rows 6 and 8 — the two rows carrying the leaf's only inhomogeneous
normalizations — are thereby confirmed at full coefficient normalization
against a point this producer never touched.

**`p=0` cross-match.** Setting `p=0` in the eight frozen rows reproduces,
term by term, the eight generators of the Grok-written `p0_primdec.sing`
(which Grok reconstructed by calling `compile_fibre()` itself in `/tmp`, before
this package existed) up to the unit scalars `4, 2/3, 4, 1, 4, 3` (with
`-243 = 3·(-81)` folding into `r6-81`), `4/3, 30`. Same ideal over `Q`.

Denominator, row-order, sign, normalization, and missing-equation attacks all
fail. The earlier malformed trials (an in-band comment misread as a
one-variable declaration) are quarantined per `notes.md` 22:41Z; this input
declares and parses nine variables (`stderr: #variables 9`).

## Attack 3 — is the msolve output a real characteristic-zero basis?

Audited from the pinned runner and the frozen log/metadata/output header
(**attestation-level**, since I could not execute):

- Invocation (runner branch `msolve-sat-elim-p-first`, `elim=0`):
  `msolve -f input.ms -o result.out -t 32 -v 2 -g 2 -P 1 --random-seed 0` — a
  **full 9-variable reduced-GB computation** (`-g 2`), no `-e` elimination
  block, plain DRL in the declared order. The metadata label `command=msolve
  saturated full solve order=p-first` matches; the `elim` in the backend name
  is a family label only (cosmetic; noted, not an error). `-P 1` is not
  documented in-repo; harmless given the header and log pin the mode.
- `stderr.log` is a genuine F4 + tracer trace: 9 variables / 9 equations /
  characteristic 0 / DRL; 31 F4 rounds with sane matrix shapes; `size of basis
  1246`; lift batches `[1][2][576][667]` summing to `1246`; `#primes 126`,
  `#bad primes 0`, `Max coeff. bitsize 1368`; CRT and rational-reconstruction
  phases explicitly timed. Reconstruction arithmetic is plausible:
  `126 × ~30.2-bit ≈ 3800` modulus bits against the `2·1368=2736` bits a
  balanced reconstruction needs, with margin. Start/end timestamps (27 s),
  memory deltas, `exit_code=0`, `final_status=DONE` are coherent.
- The output header (asserted by the verifier, attested by `replay.out`)
  declares characteristic 0, the nine-variable order, grevlex, and 1,246
  elements; the parse count matches.
- This is **not** the quarantined failure class: the hazardous earlier runs
  were solve-mode (printing `[-1]` after a single prime) and a finite-char
  staircase failure `[1,9,-1,[]]`, both documented in the Grok predecessor;
  a non-unit 1,246-element rational basis with a logged 126-prime CRT/ratrecon
  phase is categorically different, and `[1]`/`[-1]` short circuits are
  excluded by the header length, the parse count, and the pure-power staircase.
- Independent modular corroboration (from the predecessor, not msolve): Singular
  `slimgb` found `dim 0, deg 1188` for the same saturated system at eight
  primes, and the sibling elimination package's degree-630, 71-term `P(p)`
  satisfies the exact staircase arithmetic `630 + 558 = 1188` (minpoly block
  plus `q`-times-block in the product order).

What none of this proves: that the 1,246 *rational* polynomials printed after
reconstruction lie in `J`. That is Attack 8.

## Attack 4 — leading monomials and the 1,188 staircase

**Execution gap, disclosed:** without a shell I could not decompress the
23 MB output, so I performed no independent recount here. What stands
instead: the hand proofs (Attack 1) that the frozen verifier's grevlex
comparator and BFS are correct and its parser fails loudly; the frozen
`replay.out` attesting `zero_dimensional_initial_ideal=YES` /
`standard_monomials=1188`; and the two external consistency identities
(`1188 = 630+558`; eight-prime modular degree `1188`). The producer's reading
is also the right one: `p^5,…,ip^6` are **leading monomials witnessing
zero-dimensionality of the initial ideal**, not univariate equations — the
report says exactly this and never claims a univariate in `p`.

A fresh, independently written recount (different tokenizer, different DRL
formulation, minimal-generator prefilter, plus a reduced-basis check the
frozen verifier lacks — pairwise indivisibility of all 1,246 leading
monomials, content `1`, positive leading coefficients, no duplicate
polynomials) is staged at
`/tmp/jc2_doubleb_review_20260824/independent_recount.py`. It was **not run**.

## Attack 5 — the exact `p=0` slice

Both Singular scripts audited; both frozen outputs read; **not re-run here**
(the frozen verifier byte-replays both, attested by `replay.out`).

- The slice ideal is source-honest: the eight `p0_primdec.sing` generators are
  unit multiples of the frozen input rows at `p=0` (Attack 2), in the correct
  7-variable ring `Q[x0..x5,q]` — dropping `p` and row 9 is legitimate because
  `I+(p)` in nine variables maps isomorphically onto `I|_{p=0}` (and `J+(p)`
  would be the unit ideal; the report correctly slices `I`, not `J`).
- The two-way check is a genuine ideal-equality certificate:
  `reduce(G,H)=0` with `H=std(intersect(C1,C2))` proves `I+(p) ⊆ C1∩C2`;
  `reduce(H,G)=0` proves the reverse. Normal form against a standard basis is
  a complete membership test, so `I+(p) = C1 ∩ C2` exactly — this "rules out
  hidden embedded structure" as claimed.
- Primality over `Q`, by hand: `2x0^2-9` is irreducible (`9/2` is not a
  rational square), so `C1`'s quotient is `Q(√(9/2))[q]`, a domain; `4x3^3+81`
  is irreducible (`4a^3=-81` has no integer solution, so no rational root of
  the cubic), so `C2`'s quotient is `(Q[x3]/(4x3^3+81))[q]` with `x0=x3q`, a
  domain. Both prime, hence radical; their intersection is radical; they are
  incomparable (`x3∈C1∖C2`, `x0-x3q∈C2∖C1`), so both are minimal primes, the
  decomposition is irredundant, dimensions/degrees `(1,2)` and `(1,3)`, slice
  degree `5=2+3` matching `mult(std(I))=5`.
- The raw diagnostic is correctly corrected: `p0_primdec.out`'s `c_dim=2` for
  component 2 is Singular's documented behaviour when `dim` is called on a
  non-standard basis (the raw leading ideal `(x3^3, x3q, x5,x4,x2,x1)` has a
  two-dimensional `x3=0` plane); `p0_dims.sing` recomputes `std` first and
  gets `(1,3)`; the extra `G2` elements `4x0x3^2+81q, 4x0^2x3+81q^2,
  4x0^3+81q^3` are immediate consequences of `x0=x3q`, `4x3^3=-81` (checked).
- **Altitude note:** the slice is *not load-bearing* for the kill. If `p=0`
  in the trajectory field, `p` is already constant and the contradiction fires
  with no CAS input at all. The slice is corroboration plus a strong
  cross-check of the input rows at `p=0`.

## Attack 6 — the implication, hunted for loopholes

The producer's argument, tightened and checked step by step:

1. *Field dichotomy, not time-pointwise:* an actual normalized trajectory
   yields elements `(x0..x5,p,q)` of the trajectory field `K ⊇ L=C(x)(u)`
   satisfying the eight equations identically. In the **field** `K`, either
   `p=0` or `p` is invertible; isolated time zeros do not exist at this level.
   No loophole.
2. *If `p≠0`:* `ip=p^{-1}∈K` and the tuple is a `K`-point of `J`. Because the
   Rabinowitsch variable is adjoined explicitly, `K`-points of `J` are exactly
   `K`-points of `I` with `p≠0`; **no saturation black box** and no lost or
   gained points. No loophole.
3. *Finite dimension ⇒ algebraic:* if `dim_Q Q[9 vars]/J < ∞`, the powers of
   `p̄` are linearly dependent, giving `0 ≠ g ∈ Q[T]` with `g(p̄)=0`; applying
   the point's evaluation homomorphism gives `g(p)=0` in `K`. This argument
   runs inside the possibly non-reduced quotient — **nilpotents and embedded
   components are irrelevant** to it, and a `K`-point kills them anyway. No
   loophole. (If `J` were the unit ideal, step 2's case would be vacuous and
   `p=0` in `K` — the conclusion only strengthens.)
4. *Algebraic over `Q` ⇒ constant:* the minimal polynomial of `p` over `Q` has
   constant coefficients (`Q` lies in the constants of any characteristic-zero
   differential field); differentiating gives `f'(p)·p'=0` with `f'(p)≠0` by
   minimality in characteristic zero, so `p'=0`. This step does not even need
   `C` algebraically closed; algebraic closure is needed only upstream, where
   the reviewed `nu=1` normalization chooses `λ` with `λ^18=1/nu` in `C*`.
5. *Terminal contradiction:* on the leaf `r8=-3p/10`, so `r8'=0`. The reviewed
   terminal row transports through the constant normalization with the factor
   `λ^20 ∈ C*`: `9·r8' = λ^20·j/u ≠ 0` since `j≠0` and `u≠0` in `K`.
   Contradiction. The Grok collision review's warning (its non-blocking remark
   3) about inferring `r8` constancy from `λ^18∈C*` does not apply here: `p`
   itself is proved constant and `r8` follows through the leaf equation, with
   no `λ`-weight bookkeeping at all.

The **only** computational input the whole chain needs is
`dim_Q Q[9]/J < ∞`, and for that it suffices that the **nine specific
polynomials** whose leading monomials are `p^5,x0^5,…,x5^5,q^6,ip^6` lie in
`J` (then `in(J)` contains those pure powers regardless of everything else in
the file). Neither the exact staircase count `1188`, nor reducedness, nor the
GB property, nor the `p=0` decomposition is load-bearing. This is the sharpest
honest statement of the trust surface, and it is smaller than the producer's
own framing.

## Attack 7 — consumed reviewed inputs and leaf identity

Both consumed reviews were read in full; both are `CONFIRMED`; their pinned
hashes (`b6ae9516…`, `6d34908c…`) match the manifest and the producer's
citations.

- The norm review confirms: `nu=1` is a legal constant scaling
  (`λ^18=1/nu`, `λ∈C*`, equivalently the chart `r6=1`); on the seven-row leaf
  `p=a7/3` and `B=54(z^2-s)` with `s=-(a7+10·r8)/9`, so the **double root of
  `B` is exactly `s=0 ⟺ 3p+10r8=0`** — the producer's row 8; the `s=0`
  stratum is retained and split by `W0` into double-root-in-`W` versus
  double-root-off-`W`.
- The collision review confirms: on the `k=mu=0, nu≠0` landing the constants
  are exactly `r1=r2=r4=r5=r7=0, r3=mu, r6=nu`; the terminal row
  `9*r8'=j/u≠0`; and the **full-absorption** double-root-in-`W` passport
  `(18,3,1^15)` is already empty of actual trajectories, while "a double `B`
  root off `W`" is explicitly retained as a four-point family.
- Scope fit: the producer's eight equations cut out the whole `s=0` stratum —
  the **union** of the retained off-`W` leaf and the already-killed in-`W`
  leaf, without imposing `W0≠0`. Killing the union is logically valid and
  strictly contains the retained leaf, so the headline "the
  double-root-off-`W` four-point leaf is empty" is a correct consequence, not
  a scope slip. It is not a broader generic fibre: the seven fibre rows,
  `nu=1`, and `s=0` are all imposed. The already-killed full-absorption leaf
  contributes nothing here and is not double-counted as evidence.

## Attack 8 — the exact trust boundary, and the decision

**What the frozen evidence proves** (modulo the attested hashes and replay):
the input is byte-identical to the corrected nine-variable, characteristic-zero
system regenerated from the pinned compiler — and independently hand-verified
here; the preserved output is a well-formed 1,246-element characteristic-zero
DRL list whose printed first terms are genuine DRL leading terms and whose
leading monomials generate an initial ideal with pure powers of all nine
variables and a 1,188-element staircase.

**What it does not prove:** that the printed list — after CRT and rational
reconstruction — lies in `J` over `Q`. msolve's multi-modular GB is
Monte-Carlo-verified (126 primes, zero flagged bad primes), not certified; the
reconstruction step is precisely where a silent error would live; and this
campaign has already caught two distinct msolve misbehaviours **on this very
system** (the char-0 solve-mode `[-1]` after one prime; the finite-char
`[1,9,-1,[]]` staircase failure). The producer, README, REGISTRATION, and
FREEZE all bracket this equality as the trust boundary; the sibling
elimination package's hostile review (`notes.md` 23:10Z) stopped
`INCONCLUSIVE` on the same debt with no false identity found; and the
campaign's own promotion bar keeps the double-`B` kill provisional while the
second-engine lanes run.

**Decision:** exact `msolve 0.10.1` plus source-replay is **not sufficient**
for canonical confirmation under this campaign's standard, and I decline to
lower that bar — particularly in a session where I could not even re-execute
the frozen verifier. The verdict is `INCONCLUSIVE` **as an engine-trust
caveat, explicitly not a mathematical error**: every consistency probe that
could be run by hand passed, including three full symbolic row derivations,
two exact high-magnitude numeric evaluations at an independently reviewed
point, the `630+558=1188` cross-package staircase identity, and the
eight-prime independent modular degree agreement.

**Smallest sufficient discharge (any one):**

1. exact characteristic-zero cofactor representations of the nine
   pure-power-LM basis elements in terms of the nine input generators,
   verified by exact arithmetic (the `lift(...,"slimgb")` lane started
   22:57:41Z on r6c is of exactly this shape); or
2. any second-engine characteristic-zero Gröbner basis of `J` (Singular
   `modStd`/`slimgb`, Magma, Macaulay2) reaching `dim 0` — the degree value
   `1188` is corroborative, not load-bearing; or
3. a characteristic-zero elimination certificate producing a nonzero
   univariate in `p` inside `J` together with a membership witness (the
   sibling package's `P(p)` route).

## Execution gaps and staged re-execution battery

This session had no shell (`Monitor`/`Bash` denied). Therefore, performed
here: **zero** hash recomputations, **zero** script executions, **zero**
decompressions. Everything execution-flavoured above is code audit plus
frozen, manifest-pinned attestation. Staged for the operator, not run:

- `/tmp/jc2_doubleb_review_20260824/replay_all.sh` — manifest hash chain,
  launch-prompt pins, uncompressed-result hash, frozen verifier, then the two
  scripts below;
- `/tmp/jc2_doubleb_review_20260824/independent_recount.py` — reviewer-written
  revalidation (independent parser, independent DRL comparator, reduced-basis
  minimality/content/duplicate checks the frozen verifier lacks, independent
  staircase BFS expecting `1188`), which also emits
  `mod_check_1000000007.sing` and `mod_check_998244353.sing`: two-way modular
  inclusion `(basis) ⊆ J` and `J ⊆ (basis)` at fresh primes msolve never used,
  on a second engine;
- `/tmp/jc2_doubleb_review_20260824/exact_char0_modstd_J_generated.sing`
  (emitted by the recount script directly from the frozen `input.ms` bytes;
  a hand-transcribed twin `exact_char0_modstd_J.sing` also exists, but the
  generated file is authoritative) — the optional local certificate-bearing
  run (`modStd` over `Q`; `dim=0` would discharge the boundary). msolve was
  not and must not be run locally.

## Smallest failing identity

None. No identity, sign, scalar, row, order, hash, scope, or logical step
tested here failed.

## Exact promotable sentence

**Promotable now:** nothing new. (The `p=0` sub-kill — both reduced `p=0`
families die on `r8'=0` — is already registered inside the predecessor Grok
report at its own scope; this package correctly reproduces and strengthens it.)

**Promotable verbatim once any Attack-8 certificate lands and replays:**

> On the normalized maximum-12 `(9,12)` order-three double-`B` leaf
> `k=mu=0`, `nu=r6=1`, `r1=r2=r3=r4=r5=r7=0`, `3*p+10*r8=0`, the nonzero-`p`
> locus `J=I+(p*ip-1)` is zero-dimensional over `Q`; hence `p` is algebraic
> over `Q` at every coefficient-field point, every actual Keller trajectory on
> this leaf has constant `p` and constant `r8=-3*p/10`, and the reviewed
> terminal row `9*r8'=j/u!=0` makes the double-root-off-`W` four-point leaf
> empty of actual Keller trajectories.

## Scope firewall

This review licenses nothing beyond the sentence above at its stated
condition. It does not license: any other pair-norm leaf (no-`B`-root,
one-root-collision, and equal-non-`1`-value leaves remain open); `nu=0` or
`mu!=0` or `k!=0` strata; any Taylor boundary; other invariant loads; the
order-one core; `(8,12)`; all `(9,12)`; maximum-twelve automorphy; a
counterexample; or JC2. No result here may be promoted to all `(9,12)`,
maximum twelve, a counterexample, or JC2.

---

**Verdict: `INCONCLUSIVE`** — no mathematical error found; blocked solely on
the independent characteristic-zero membership certificate for the msolve
basis (nine pure-power-LM elements suffice), which the already-running
second-engine lanes are expected to supply.
