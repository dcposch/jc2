# Hostile different-model review — round-1 proof-side gates (P1 boundary passport, P2 TRACE-REG)

- **Reviewer/model:** Claude (Anthropic), interactive session. Different model
  family from both producers: P1 producer Averroes and P2 producer Nash are
  OpenAI Codex sessions on the `/root` coordinator host (Nash self-identifies
  as "OpenAI Codex research subagent",
  `xmodel/ideation-20260824T0035Z-nash.md:3`; Averroes is the sibling
  `strategy_audit` session in the same roster,
  `notes.md:3488-3490`). COORDINATION.md promotion rule 1
  (different-model hostile review) is satisfied by this review.
- **Review window (UTC):** 2026-08-24T02:02:29Z – 2026-08-24T02:19:52Z.
- **Host:** `dc-mbp-m2.local`, macOS 14.6 / Darwin 23.6.0 arm64.
- **Engines:** `uv 0.6.9`; uv-managed CPython 3.11.11; `sympy==1.14.0`
  (exact pin, resolved **offline** from the local uv cache — no network call
  was made at any point). Producers ran on Linux; byte-identity across
  OS/CPU/python-minor (below) independently demonstrates the determinism the
  reports rely on.
- **Basis:** commit `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`. Working tree
  dirty in `AUDIT.md` (the pre-drafted P1 COSTUME entry, see §6) and
  `pilot-local.log`; both gate directories untracked. The current dirty
  `AUDIT.md` (SHA-256 `1e8403ed…`) is byte-identical to the copy hashed in the
  frozen P2 input manifest, so the replay snapshot is coherent.
- **Reviewer discipline:** code inspected line-by-line before execution; exact
  arithmetic only; all scratch output in a fresh `mktemp -d`
  (`/tmp/jc2-review-7jZ4kx`, outside the repository); no author contact, no
  shared-ledger edits, no repository writes except this file. Verdicts are
  restricted to the registered scopes; nothing here is an inference for or
  against JC2 itself.

## Verdicts (summary)

| Gate | Registered scope | Verdict |
|---|---|---|
| P1 `xmodel/round1-boundary-passport-20260824.md` + `cases/round1_boundary_probe/` | equivalent-map boundary covariance / non-tautology kill test (`CANDIDATE`/`COSTUME`) | **CONFIRMED** |
| P2 `xmodel/round1-trace-regularity-20260824.md` + `cases/round1_trace_probe/` | TRACE-REG `m=1,2` residue/underdetermination audit, not an engine | **CONFIRMED** |
| **Overall** | | **CONFIRMED** |

All minor remarks below are non-blocking (labeling, citation-offset, and
replay-hygiene notes); none changes a number, a scope, or a verdict.

## 1. Registered scopes adjudicated

From `xmodel/ideation-20260824T0035Z-synthesis.md` and the
2026-08-24 01:05Z `LIVE STATE` (`notes.md:3517-3558`):

- **P1** (root P, owner Averroes): "Test equivalent-map covariance and
  non-tautology once before any positivity, capacity, or cofinal-bound
  program" (synthesis lines 75-77, 154); harvest trigger "boundary verdict
  `CANDIDATE` or `COSTUME`".
- **P2** (queued item 2, owner Nash): "TRACE-REG `m=1,2`
  residue/underdetermination audit after P1 stops"; card 4: "do not build a
  general engine until `m=1,2` yields a separating residue identity or
  demonstrates exactly which global branch-pairing datum is absent"
  (synthesis lines 78-84, 182-183).

Both reports executed exactly these scopes: P1 returned `COSTUME` and opened
no theorem lane; P2 fired its registered `INSUFFICIENT-DATA` stop, launched no
engine, and named the absent datum (target-affine-divisor-tagged completed
branch pairing with the coefficient convolutions).

## 2. Artifact hashes verified (SHA-256)

| File | Hash | Matches |
|---|---|---|
| `cases/round1_boundary_probe/boundary_probe.py` | `a923e0f9303833e8926492a11270e2652809a6bbe12d37f7c5bc196b0a84e5ef` | (recorded here; no prior pin) |
| `cases/round1_boundary_probe/results.json` | `f049f0315e635b792e0927281a34d8a71cef779a0d79cb5f5b01dded361e2e83` | P2 manifest entry ✓ |
| `cases/round1_trace_probe/trace_probe.py` | `faadfaf26c7184c24fc3e55a3de90c881e38b0bf12293cb245bcaa9ab5ad0372` | P2 report + embedded `tool_sha256` ✓ |
| `cases/round1_trace_probe/results.json` | `51f5a6e200327dd343c1c06ed2e9529ef807428531d21535caef63c655f00706` | P2 report ✓ |
| boundary full-audit stdout (default mode, replayed) | `a7168b569fe07c622125b68cb9bb14775687af3bbefe777ffa62cb980b0a9a9b` | P1 report + `full_audit_json_sha256` field ✓ |
| P2 input manifest (recomputed in replay) | `b9028b003acccabea5299d02960bac0f276c86ad00c3ea8ac62ebcd477e39c85` | P2 report ✓ |

Every file named in the P2 input manifest (`AUDIT.md`, `PROGRESS.md`,
`ladder/TRANSPORT.md`, `ladder/SHEET6-CLASSICAL.md`,
`ladder/GROK-MONODROMY.md`, `xmodel/round1-boundary-passport-20260824.md`,
`cases/round1_boundary_probe/results.json`) was re-hashed; all seven match the
frozen manifest byte-for-byte.

## 3. Replays (pinned commands, byte-identity required and achieved)

Deviations from the pinned invocations, both content-neutral, both forced by
review discipline: (i) `--offline` added (network prohibition; the version pin
`sympy==1.14.0` is unchanged and resolved from cache); (ii) outputs directed
into the fresh scratch directory instead of the pinned `/tmp` filename (P1)
and instead of **overwriting the frozen artifact** (P2 — see remark T3).
Byte-identity was tested with `cmp` (stricter than `diff`).

```sh
# P1, pinned summary replay (README contract)
uv run --offline --no-project --with sympy==1.14.0 \
  python3 cases/round1_boundary_probe/boundary_probe.py --summary \
  > /tmp/jc2-review-7jZ4kx/round1-boundary-results.json
cmp cases/round1_boundary_probe/results.json \
  /tmp/jc2-review-7jZ4kx/round1-boundary-results.json   # -> BYTE-IDENTICAL

# P1, default full-audit mode (binds the compact file to the rich object)
uv run --offline --no-project --with sympy==1.14.0 \
  python3 cases/round1_boundary_probe/boundary_probe.py \
  > /tmp/jc2-review-7jZ4kx/boundary-full.json
# sha256 = a7168b56… = report quote = embedded full_audit_json_sha256  ✓

# P2, pinned replay with --out redirected to scratch
uv run --offline --no-project --with sympy==1.14.0 \
  python3 cases/round1_trace_probe/trace_probe.py \
  --out /tmp/jc2-review-7jZ4kx/trace-results.json
cmp cases/round1_trace_probe/results.json \
  /tmp/jc2-review-7jZ4kx/trace-results.json              # -> BYTE-IDENTICAL
# stdout: VERDICT: INSUFFICIENT-DATA / COLLISION RESIDUES: ['84', '168']
```

All three runs exited 0 with empty stderr. Every producer `assert` (the
per-map pure-boundary determinant identity, the curl identities, the zero
residues, the covariance separations, the collision residues `84`/`168`, the
manifest `COSTUME` cross-link) therefore re-executed and passed on this
reviewer's machine. Byte-identity held across a different OS (macOS vs Linux),
CPU (arm64), and CPython minor version.

## 4. Gate P1 — boundary passport (`COSTUME`)

### 4.1 Code inspection

`boundary_probe.py` read in full before execution: pure stdlib + sympy, no
network, no filesystem writes (it prints one JSON document); exact `QQ`
domains throughout; the `--summary` output is the frozen `results.json` and
carries the full-audit hash binding. The generic-DVR valuation
(`ord_var`) is the u-adic valuation over `QQ(v)[u]_(u)` (min degree of
numerator minus min degree of denominator after `cancel`) — correct because a
nonzero coefficient in the transverse variable is a unit at the generic point.

### 4.2 Formula suite (hand-recomputed by the reviewer)

- **Homogenization/gradient.** `homogeneous_chart` restricts
  `F=Σ c_{ij}X^iY^jZ^{d-i-j}` to `X=1` (resp. `Y=1`) correctly;
  `homogeneous_gradient_matrix` recovers `F_X` via the Euler relation
  `F_X = dF - vF_Y - uF_Z` at `X=1`. I re-derived and confirmed
  `T_n=(x,y+x^n)`: `A_standard=[[1,n],[0,u^{n-1}]]`, Smith `(0,n-1)`, blow-up
  identical; identity `(0,0)`.
- **Pure-boundary identity.** `F_XG_Y-F_YG_X = u^{d+e-2}·J(f,g)(1/u,v/u)`
  re-derived from the chain rule (matches the promoted identity,
  committed `AUDIT.md:984-994`); the checker asserts it per map, and my
  independent script verified it for all seven maps plus one out-of-suite map.
- **Log coframe.** Columns `df,dg` in `(du/u,dv)`: reviewer re-derivation
  gives `L_standard=[[-u^{-1},-vu^{-1}-nu^{-n}],[0,u^{-1}]]` for `T_n`, Smith
  `(-n,n-2)`, blow-up `(-n,n-1)`, identity `(-1,-1)→(-1,0)` — all as reported.
- **Inverse composition.** `(x,(y+x^4)-x^4)` expands to the identity pair;
  frozen metrics equal the identity row, and the `map_pair_sha256` of the
  composed pair equals the identity's (`6a92e22c…`). Word history is erased at
  the polynomial-pair level, as claimed.
- **Hénon tower.** `henon_tower(r)` is exactly the promoted construction
  (`xmodel/sol-k2c.md:119-150`, eqs (2.4)–(2.8)): `q=(7,3,2,…,2)`, `s=r+4`,
  `(f_r,g_r)=(P_s,P_{s+1})`, each step `H_q(u,v)=(v,v^q-u)` with explicit
  polynomial inverse `(u,v)→(u^q-v,u)`; hence every suite member is a
  certified polynomial automorphism with `J=1` (I verified `J=1` symbolically
  for all six). Degrees `(42,84)`, `(84,168)` match `κ_r=42·2^r`
  (committed `AUDIT.md:1103-1124`, dual-confirmed entry "UNRESTRICTED K2C
  REFUTED"; in the current dirty tree the same entry sits at
  `AUDIT.md:1130-1151`). The independently recorded Grok verification
  "`Z^124` at r=0 by direct expansion" corroborates the probe's gradient
  determinant order `124`.
- **Negative control.** `f=x⁴+y, g=x⁶+y⁵`:
  `J=20x³y⁴-6x⁵=-2x³(3x²-10y⁴)` (hand-checked), non-constant, hence
  non-Keller; the standard-chart gradient determinant
  `-2r³z(3r²z²-10)` re-derived by hand (`z^8·J(r/z,1/z)`) — the residual
  Jacobian curve is exposed exactly as claimed, and the curls
  `±(J-1)` are retained instead of primitives. The decoy is used only as a
  schema/negative control, and no residue-A truncation appears anywhere in
  the suite — confirmed by inspection.

### 4.3 DVR Smith/Fitting and the `J=1` survivors

- The Smith recovery `(a, b)` with `a=ord Fitt₁=min entry order`,
  `a+b=ord Fitt₀=ord det` is the classical determinantal-divisor fact
  (`D₁=gcd of entries`, `D₂=det`) over the DVR at the generic boundary point;
  it extends verbatim to Laurent-entry matrices by clearing `t^N`
  (both sides shift equally). Correct as coded for nonzero 2×2 matrices;
  zero entries are correctly excluded from the entry-ideal minimum.
- **The "follows from `J=1`" claim is an identity, not an observation.**
  Reviewer derivation: with `x=1/u, y=v/u`, `dx∧dy=-u^{-3}du∧dv`, and in the
  basis `(du/u,dv)` the matrix determinant satisfies
  `det L = -J(f,g)∘chart · u^{-2}`; after the blow-up `x=1/s, y=w`,
  `det L = -J∘chart · s^{-1}`. So every `J=1` pair — automorphic or not —
  has log-determinant orders exactly `(-2,-1)`, and my independent script
  verified the *exact identities* `det L_std=-u^{-2}`, `det L_blw=-s^{-1}`
  for all six suite maps and for one out-of-suite `J=1` map
  (`(x+(y+x²)³, y+x²)`) the producer never ran. The decoy's orders
  `(-9,-5)` decompose as `ord_z(J∘chart)-2 = -7-2` and
  `ord_s(J∘chart)-1 = -4-1` — the log determinant sees exactly `J` and
  nothing else. This fully substantiates "coordinate-volume form of `J=1`".
- **Zero residues are automatic.** `ω_P=f dg-x dy`, `ω_Q=g df-y dx` have
  curls `J-1` and `1-J` (re-derived); for `J=1` both are closed, and closed
  polynomial 1-forms on `A²` are exact with polynomial primitives (the
  checker constructs and verifies them; my script reconstructed them by the
  opposite integration order). The divisorial differential residue of an
  exact form vanishes identically (`d/du` of a Laurent series has no `u^{-1}`
  term), so the zero residues carry no information beyond exactness — as the
  report itself states.

### 4.4 Independent recomputation (different code paths)

Reviewer script (scratch, `indep_boundary.py`, SHA-256 `ba54843d…`):
true 3-variable homogenization with direct partials (no Euler shortcut),
y-first primitive integration, independent tower reconstruction from the
sol-k2c spec, hash-binding via the frozen `map_pair_sha256`. Result: **every
frozen number reproduced** — degrees, gradient Smith standard/blow-up,
gradient determinant orders (`124/124`, `250/250`), log Smith
(`(-84,82)→(-12,11)`, `(-168,166)→(-24,23)`, etc.), log determinant orders
`(-2,-1)` on all Keller rows and `(-9,-5)` on the decoy, action pole orders
(`3,3 / 5,5 / 126,18 / 252,36`), zero residues, decoy curl strings. Zero
failures. The dash rows are genuinely the zero primitive: the frozen hash
`6c6cd015…` is the canonical payload `[[0,0,"0"]]` of the zero polynomial
(verified), and `ω_P=ω_Q=0` for the identity by direct cancellation.

### 4.5 `COSTUME` scope adjudication

- The kill is valid at its registered scope: all six Keller controls are
  presentations of the *same* trivial automorphism class, yet the raw
  gradient Smith/Fitting data, raw log Smith splits, and action-primitive
  pole orders differ across them (`(0,0)` vs `(0,1)` vs `(0,3)` vs `(0,124)`;
  `(-1,-1)` vs `(-2,0)` vs `(-4,2)` vs `(-84,82)`; `-,3,5,126`) and change
  again under the explicit blow-up (`(0,124)→(36,88)`, `126→18`). Any
  quantity invariant under equivalent presentation and compactification
  refinement must therefore take its identity value on the whole suite. The
  only stable outputs are the log-determinant orders `(-2,-1)` (an identity
  consequence of `J=1`, §4.3) and the zero residues (automatic from
  exactness). "No measured quantity is both stable and stronger than the
  determinant/volume identity" is exactly right for the measured set; I
  checked that no combination of the recorded scalars (differences of splits,
  blow-up deltas) is stable either.
- **Precisely-tested kills.** The five "variants killed" all reference
  measured quantities with the demonstrated failure mode; none over-reaches.
- **Correctly left open.** The report and the drafted AUDIT entry keep open:
  a checksum attached to one fixed certified choice-independent minimal
  compactification; boundary-twisted forms; signed invariants from complete
  polynomial data; and everything about nonautomorphic Keller maps (no
  positive control can exist short of resolving JC2). It also states the kill
  does not weaken the pure-boundary identity itself. All as required.
- The suite tests one standard chart per family plus one explicit blow-up;
  demonstrated variation suffices for a kill (more charts could only add
  variation). The negative control shows the schema is not vacuous.

### 4.6 Minor remarks (non-blocking)

- **B1.** "Exact orbit minimization" is certification **by construction**
  (every suite member is an explicit composition of automorphisms with
  explicit inverses; composition with the inverse reaches the identity), not
  a computed minimizer run; the JSON flag `orbit_minimization.available` is a
  producer input. The report's wording "certified, not heuristic" is
  accurate, and this review independently verified the automorphism property
  (tower reconstruction + `J=1` + explicit inverses + hash match). Future
  schemas might name the field `by_construction` to prevent misreading.
- **B2.** The report's `AUDIT.md:979-1015` and `AUDIT.md:1103-1124` anchors
  are line-exact against the **committed** `AUDIT.md`; the uncommitted
  COSTUME insert shifts the second entry to `1130-1151` in the working tree.
- **B3.** The README replay writes to a fixed `/tmp` filename; this review
  used a fresh `mktemp -d` target instead (byte-identity unaffected). Prefer
  scratch-unique targets in future replay contracts.

### 4.7 Verdict P1: **CONFIRMED**

`COSTUME` at exactly the tested raw-passport scope, with the stable outputs
correctly identified as `J=1`/exactness consequences, the negative control
meaningful, the replay byte-identical, and every number independently
recomputed.

## 5. Gate P2 — TRACE-REG residue audit (`INSUFFICIENT-DATA`)

### 5.1 Code inspection

`trace_probe.py` read in full before execution: reads only the seven manifest
files, writes only `--out`, exact symbolic arithmetic, deterministic output
(`sort_keys`, canonical term ordering); `laurent_terms`/`principal_part`/
`residue` are exact finite-Laurent operations; `cyclic_trace_power` is the
roots-of-unity filter `Σ_{ζ^e=1} ζ^n = e·[e|n]` with weight `e`. The manifest
gate asserts P1's frozen verdict is `COSTUME` (consistency link only — no P1
invariant is consumed as a proposition, confirmed by inspection).

### 5.2 Conditional algebra (every hypothesis checked)

Proposition (`k=C`, `A=C[P,Q]⊆B=C[x,y]`, `d=[L:K]`, `J(P,Q)=c∈C*`; if
`Tr_{L/K}(x^m),Tr_{L/K}(y^m)∈A` for `1≤m≤d` then `(P,Q)` is an automorphism):

1. `J≠0 ⇒ P,Q` algebraically independent (char 0) `⇒ A≅C[U,V]`; `d` finite
   by equal transcendence degrees. ✓
2. Field trace = trace of the multiplication operator; `p_m=tr(M_z^m)` are
   the power sums of the char-poly roots; Newton recursion
   `re_r=Σ(-1)^{i-1}e_{r-i}p_i` — verified symbolically at degree 4 by the
   producer gate (replayed) and at degree 5 by this reviewer. Char 0 permits
   division by every `r≤d`; induction puts all `e_r∈A`; Cayley–Hamilton gives
   `χ_z(z)=0`, so `x,y` integral; `B=A[x,y]` module-finite. ✓ (The report's
   insistence on the *field* trace — an `A`-module trace does not exist
   before finiteness — is correct and important.)
3. Presentation `B≅A[X,Y]/(U-P,V-Q)` (eliminate `U,V`) with relation-Jacobian
   determinant the unit `c` ⇒ standard-smooth of relative dimension 0 ⇒
   étale; with finiteness, finite étale. ✓
4. `Spec B=A²` connected, `C²` simply connected ⇒ degree 1 ⇒ `L=K`; `A`
   normal + `B` integral ⇒ `A=B` ⇒ automorphism. ✓ Non-closed char-0 fields
   handled by geometric connectedness after base change, as stated. ✓
5. **Converse and equivalence** (`A` normal, traces of integral elements are
   integral and in `K`, hence in `A`): first-`d` trace regularity of `x,y`
   ⟺ integrality ⟺ finiteness ⟺ (given `J∈C*`) automorphism. ✓ So full
   TRACE-REG is an equivalent reformulation of properness/finiteness — the
   report's own headline, honestly stated.
6. **Char-p warning verified:** `(x^p-x, y)` has `J=-1∈k*`, is finite étale
   of degree `p` (Artin–Schreier; `T^p-T-P` has derivative `-1`), and is not
   an automorphism. The literal arbitrary-characteristic statement is false,
   exactly as warned. Newton division and the simply-connectedness step both
   fail at `p`. ✓
7. **No universal cutoff:** for `α^d=u^{-1}`, `T^d-u^{-1}` is irreducible
   over `K` for a prime element `u` (valuation `-1` is coprime to every
   `p|d`, and the `-4·(4th power)` case is excluded the same way), all
   `Tr(α^m)=0∈A` for `m<d` while `α` is not integral, `Tr(α^d)=d/u`.
   Reviewer verified the power sums via the Newton recursion at `d=5`
   (`p_1..p_4=0`, `p_5=5/U`). So `m=1,2` is a data discriminator for `d>2`,
   never an integrality test; and `d` is unbounded over the universal problem
   (only per-pair Bezout bounds exist). The refusal to import the sheet-6
   `td=6` (`ladder/SHEET6-CLASSICAL.md:51,205,334`) without a transport
   theorem is correct. ✓

### 5.3 Local principal-part/residue formula

For a target DVR `K_C=κ_v((t))` with `L⊗_K K_C=∏_w L_w` (char 0 ⇒ étale
decomposition, trace additive over factors ✓): in split form `t=u_w^{e_w}`
with `μ_{e_w}⊆κ_w` (function fields over `C` contain all roots of unity ✓),
the conjugation filter retains `e_w|n` with weight `e_w` and residue-field
trace `Tr_{κ_w/κ_v}` applied coefficient-wise on the unramified layer;
`e_w f_w c` when coefficients lie in `κ_v` (`Tr_{κ_w/κ_v}(c)=f_w c`) ✓;
residue slot `n=-e_w` ✓; **all places above the same target divisor must be
summed** (not merely conjugates of one source place) ✓; `A=∩_{ht 1}A_p` for
the normal `A` makes "trace in `A` ⟺ all affine principal parts vanish"
correct, while poles along a compactification's divisor at infinity are
ordinary polynomial growth ✓ (demonstrated by the tame control's
`P=t^{-1}` chart); an ordinary residue sees only `t^{-1}`, so full principal
parts are required absent a proved simple-pole bound ✓. The quadratic
convolution `Σ_{q+r=-ℓ}a_{j,q}a_{j,r}` is exactly what a contact-only
passport discards ✓.

### 5.4 Controls (independently cross-checked)

- **Tame automorphism `(x,y+x²)`:** `d=1`, inverse `(P,Q-P²)`; affine-DVR
  traces `t, t², q-t², (q-t²)²` all regular; the infinity-chart poles are the
  allowed kind. ✓ (trivial hand check; frozen table matches).
- **Nonproper `(x²,xy)`:** `J=2x²`, `d=2`; no affine preimage of `(0,q≠0)` ✓;
  reviewer cross-checked the *completed* computation against **global
  minimal polynomials**: `x` has `T²-P` (so `Tr x=0`, `Tr x²=2P`) and `y=Q/x`
  satisfies `y²=Q²/P∈K` (so `Tr y=0`, `Tr y²=2Q²/P`) — identical to the
  frozen `0, 2t, 0, 2q²/t`, residue `2q²`. The first moment cancels by
  conjugacy while `m=2` detects nonproperness; correctly framed as a residue
  validation, not a Keller statement. ✓

### 5.5 Denominator-42 completion collision

Reviewer recomputed everything by an independent support-convolution path
(no reuse of the producer helpers), plus a from-first-principles validation
of the filter mechanism by explicit summation over all six exact sixth roots
of unity at `e=6` (both `m=1,2`):

- `Tr(z_b)=42(t^{-2}+at^{-1}+bt)` and
  `Tr(z_b²)=42(t^{-4}+2at^{-3}+a²t^{-2}+2bt^{-1}+2ab+b²t²)` — exact match
  (also re-derived by hand: the only exponent pairs summing to multiples of
  42 are the six displayed; `-30,-10,-5` generate nothing divisible by 42
  in single or pairwise sums except through the invariant slots).
- Residues `Res(Tr(z)dt)=42a`, `Res(Tr(z²)dt)=84b`; at `a=1`:
  `b=1→84`, `b=2→168`; the full `m=1` principal parts `42/t+42/t²` are
  identical for both completions. ✓
- **Decoration invariance:** the non-invariant exponents are exactly
  `{-30,-10,-5}` (offsets `54,74,79` from the leading `-84`); gcd chain
  `42→6→2→1`; characteristic indices `(7,3,2)` — matching the residue-A
  ladder `1→7→21→42` recorded at `AUDIT.md:1049-1052`; orbit size 42 since
  `gcd(support∪{42})=1`; both `a`- and `b`-slots sit at exponents divisible
  by 42, hence are fixed by every `u→ζu` and cancel from every conjugate
  difference — so support, every contact, every gcd drop, orbit size, and
  the leading coefficient are all unchanged while the varying slot (offset
  `126 > 79`, strictly beyond the last retained characteristic/contact
  level) changes the `m=2` residue. All verified. ✓
- Correctly labeled a **completion collision**, not a polynomial map, not a
  formal Keller countermodel. ✓

### 5.6 Why `INSUFFICIENT-DATA` follows for the current packet

The four §5 document claims were verified against the frozen inputs at
specific lines:

1. `ladder/SHEET6-CLASSICAL.md:35,43` — denominator-42 Newton pairs
   `(7,2)(3,10)(2,5)`, characteristic exponents `12/42<32/42<37/42`, pinned
   contact table; `:40` "partition below F_s NOT pinned"; `:46` "same B-dir
   pairs: > 12, unpinned"; `:13,18,148` B/x resolution tails unpinned. ✓
2. `ladder/GROK-MONODROMY.md:54` — "place partition unpinned (degrees in
   7Z)"; `:195-200` — x-side finite values through the unpinned degree-63
   polynomial `L(a_3)`. ✓
3. `ladder/TRANSPORT.md:697` — "CONJECTURE T (corner-to-tree functor). A
   fiber-tagged, paired…" is exactly a conjecture; `:459-462` — the GGV
   polygon transport "does not… determine pole status, fiber tags, residual
   g-cancellations". ✓
4. D25 artifacts exist as source-chart jets (`AUDIT.md:937-974`); no proved
   source-to-target-completion dictionary exists anywhere in the cited
   corpus (consistent with Conjecture T being open). ✓

Given the collision, the retained decoration type (valuations, contacts,
gcd/characteristic data, support, leading data) provably does not determine
even the `m=2` residue; inserting either completion would be an extra
assumption; and assuming complete branch pairing or integrality would assume
the very objects TRACE-REG is meant to prove. `INSUFFICIENT-DATA` for the
**currently retained packet** follows. The report explicitly does **not**
claim any augmented packet is insufficient, does not refute TRACE-REG, and
closes no residue-A-completion questions — the perimeter is exactly right.

### 5.7 Minor remarks (non-blocking)

- **T1.** §2's "after tame geometric splitting, choose `t=u_w^{e_w}`"
  presumes the split normalization; over a non-algebraically-closed residue
  field a unit twist (`u^e=c₀t`, `c₀∈κ_w^*` without an `e`-th root in
  `κ_w`) can obstruct the literal normalization and must be carried as
  bookkeeping. The report itself lists "a common target uniformizer with
  conjugation twists fixed" among the missing data, and everywhere the
  formula is *used* the normalization holds by construction — so this is a
  packaging remark only.
- **T2.** The results record the sympy version but not the Python version
  (P1 records `"python": "3"`); cross-platform byte-identity observed here
  mitigates, but pinning the interpreter in the engine record would be
  cleaner.
- **T3.** The pinned replay command's `--out` targets the frozen
  `results.json` itself; run verbatim it overwrites the artifact (harmlessly
  when healthy, destructively on any divergence). This review redirected to
  scratch and compared with `cmp`. Future replay contracts should target a
  scratch path, as P1's README does.

### 5.8 Verdict P2: **CONFIRMED**

The conditional algebra is correct with all hypotheses explicit; the
char-p warning, converse, and no-cutoff examples are correct; the local
formula is correct as packaged; both controls validate; the collision is
exact and its decoration-invariance claims are fully verified; and
`INSUFFICIENT-DATA` follows for the current packet at exactly the registered
scope.

## 6. What may enter `AUDIT.md`, and what must remain open

**May enter (promotion gate now satisfied by this different-model review):**

1. **P1.** The working-tree draft entry "RAW BOUNDARY PASSPORT/CAPACITY PROBE
   RETURNS COSTUME (2026-08-24)" (`AUDIT.md:1017-1042` in the dirty tree) is
   accurate as written — its KILLED-AT-THIS-SCOPE and NOT-KILLED bullets
   coincide with what was verified here — and may be committed/promoted at
   tier EXACT (computational; scope = the tested raw passports on the
   registered suite, one standard chart per family plus one explicit
   blow-up), citing this review. Note the entry was drafted before this
   review completed; with this review the different-model rule is met.
2. **P2.** A new entry may record, at the stated scopes: (i) the EXACT
   char-0 conditional equivalence — first-`d` field-trace regularity of
   `x,y` ⟺ integrality ⟺ finiteness ⟺ (given `J∈C*`) automorphism — with
   the explicit char-p falsity `(x^p-x,y)`, the no-universal-cutoff Kummer
   family, and the label that this is an equivalent reformulation of
   finiteness, not a shortcut past it; (ii) the EXACT denominator-42
   completion collision: the currently retained valuation/contact/gcd/
   support decoration does not determine the `m=2` Newton-sum residue
   (`84` vs `168` with identical retained decoration and identical full
   `m=1` principal parts), hence verdict `INSUFFICIENT-DATA` for deriving
   TRACE-REG from the currently retained boundary packet; (iii) the
   identified smallest missing datum: a target-affine-divisor-tagged
   completed branch pairing, including the coefficient convolutions
   `Σ_{r+s=-e_w}a_{w,r}a_{w,s}` with residue-field traces and grouping of
   all places above one target divisor.

**Must remain open (not promotable from these artifacts):**

- P1: any coordinate-free capacity claim for canonical-minimized checksum,
  boundary-twisted, signed, or complete-data invariants (untested here);
  any behavior claim on nonautomorphic Keller maps (no positive control
  exists short of resolving JC2); any chart/compactification beyond the two
  tested; any reading of `COSTUME` as weakening the pure-boundary identity.
- P2: TRACE-REG itself (trace regularity for any actual Keller family);
  whether some augmented packet (e.g. D25 jets plus a proved Conjecture-T
  dictionary) suffices; any Keller-specific separating identity; any
  universal trace cutoff below `d`; any statement about all residue-A
  coefficient completions.
- Neither gate bears on the truth of JC2 in either direction; neither opens
  a theorem lane (both registered stops honored).

## 7. Evidence scope of this review

Checked: both scripts in full; byte-identical replays of both pinned
commands plus the P1 full-audit mode; every hash quoted in either report;
every number in the P1 covariance table and P2 tables (independent
recomputation via different code paths — reviewer scripts
`indep_boundary.py` SHA-256 `ba54843d29c0ba03d9de1c4a84558a292c441fc67bbda700e47c1c42ed8cae23`,
`indep_trace_fast.py` SHA-256 `029a7a9a38d4dbb95654ebaed99038f244e14e36348daf744a6390d6f8e60704`,
kept in scratch; their checks are fully described above and reproducible
from this text); the mathematical derivations behind every headline claim;
the four cited campaign documents at the specific cited claims; the AUDIT
anchors against both committed and working-tree versions; and the lane
registrations. One reviewer-side check initially failed (explicit
roots-of-unity summation at `e=6`) and was diagnosed as the reviewer's own
radical-normalization artifact; after reducing exponents mod 6 it passes for
`m=1,2` — recorded here for completeness.

Not re-adjudicated: the promoted parents (pure-boundary identity, Hénon
tower, class-kill family) beyond the parts these gates actually consume
(those parts were incidentally re-verified: the identity per map, the tower
reconstruction with `J=1` and explicit inverses, the decoy Jacobian); the
cited campaign documents beyond the specific claims quoted; the wider claim
DAG and the other round-1 gates (separate reviews exist or are owed).

— Claude (Anthropic), hostile different-model reviewer, 2026-08-24T02:19Z
