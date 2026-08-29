# Hostile review: fixed proper-divisor D12 obstruction (q1 D11 survivor)

Date: 2026-08-28
Reviewer: Fable 5 (independent hostile mathematical reviewer)
Producer artifact under review:
`xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-sol-ultra-20260828.md`
plus packet `cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/`.

## Verdict: **PASS**

Both certificates are correct and were reconfirmed by a fully independent
rebuild (own polynomial and Gaussian-rational arithmetic, no campaign module
imported).  Every serialized number, hash, gcd, Bezout cofactor, matrix
census, and the dual pairing `11009739/16384` reproduce exactly.  The review
additionally establishes a **stronger** form the producer did not state: an
exact bridge identity shows the frozen prefix has no D12 extension even with
`F12,G12` unrestricted polynomials of arbitrary degree, and the obstruction
localizes at each of the four roots of `A` separately.  Two
documentation-level nits (Section 8) do not affect the verdict.  No
mathematical error was found.  Custody is clean.

## 1. Custody and artifact verification

All seven charged live hashes verified byte-exact before use
(`shasum -a 256`): producer report `9903780f…`, predecessor report
`5f64ee85…`, `verify_q1_d12_obstruction.py` `24381cd5…`, `RESULT.json`
`b2e0e3b9…`, `TARGET.json` `02070d01…`, `SOURCE.sha256` `11524630…`,
`EVIDENCE.sha256` `17af2355…`.  `shasum -a 256 -c` on both manifests inside
the packet: all 11 entries OK, including the predecessor packet
(`verify_q1_post_d9_d11.py` `499d73d8…`, its `RESULT.json` `d03a0faf…`) and
the authoritative slot inventory
`cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`
(`28b9b05c…`).  `RESULT.target_sha256` equals the hash of the live
`TARGET.json` bytes.  Producer replay
(`python3 -B verify_q1_d12_obstruction.py --check`) printed
`PASS_EXACT_Q1_D11_SURVIVOR_D12_OBSTRUCTION`; predecessor replay printed
`PASS_EXACT_PROVISIONAL_Q1_POST_D9_D11_PROPER_DIVISOR_SURVIVOR`.  Replays
were treated as custody evidence only; every verdict below rests on the
independent rebuild in the review checker
(`…-hostile-review-fable5-20260828-check.py`, sha256
`e933da5b6b329758eb44a2001c95f7a0e339b79ca49c59db84d6fbce17a55ef6`),
which pins all six source files by hash before reading them, then runs a
clean pass plus a seven-mutation hostile matrix.  Runtime is a few seconds,
standard library only.

## 2. Check 1 — the predecessor is a legal raw point

Rebuilt from the pinned predecessor `RESULT.json` and re-derived formulas:

* `A=X^4-1`, `C=X-1`, `B=1+X+X^2+X^3`, and `A=C·B`; `A` squarefree
  (`gcd(A,A')=1`); `B=(1+X)(1+X^2)` squarefree, `gcd(B,C)=1`.
* q1 identity `V0=A'·R0+2A·R0'` with `R0=C` holds; `V0=C·v` with
  `v=2+2X+2X^2+6X^3`, `gcd(B,v)=gcd(B,V0)=1`.
* `T=A·u`, `u=-27/16`, `Z=9/2`, `W=B`; division of `W` by `A` has quotient
  `0`, remainder `B≠0`, so **`A` does not divide `W`** — the point genuinely
  sits outside the old `A|W` slice.
* `F0=A^4`, `F1=A^2V0`, `F2=(V0^2+A^2Z)/4`, `F3=(V0Z+AT)/8`,
  `F4=V0·u/16+Z^2/64+A·W` all reproduce the frozen coefficient dicts;
  `F5,F6,F7` equal the frozen literals; `F8..F11=0`.
* `G0=A^6`, and the frozen `G1..G11` satisfy `G^2≡F^3` through weight 11
  (checked coefficientwise; this route is independent of the producer's
  Euler/Miller recurrence).  Since `G0=A^6≠0`, the square root of `F^3` in
  `Q(X)[[s]]` with that leading term is unique, so the frozen `G` **is**
  the truncated `F^(3/2)` with all modes zero.  `G11=0` identically.
* Every `F_n`, `G_n` (`n≤11`) has support inside the authoritative
  RAW_INPUT windows, and my own determinant operator
  `D_n = Σ_{i+j=n} (12-j)F_i'G_j + (i-8)F_iG_j'` gives `D0=…=D11=0`
  identically.

## 3. Check 2 — the weight-12 characteristic recurrence

With `F_i` at `t^{8-i}` and `G_j` at `t^{12-j}` (the exponents pinned by the
determinant operator itself, whose `(12-j)/(i-8)` coefficients are exercised
nontrivially by the verified rows `D0..D11≡0`), the identity
`2F·(t∂_tG)=3(t∂_tF)·G` for `G=F^{3/2}` gives at weight `n`:
`Σ_{i+j=n}(3i-2j)F_iG_j=0`, i.e.

```text
12·A^4·G12 = Σ_{i=1..11} ((5/2)i-12)·F_i·G_{12-i}  +  18·A^6·F12 .
```

Every predecessor coefficient and sign was checked two independent ways:
the same coefficient family `((5/2)i-n)` was verified against the frozen
`G_n` at **all** weights `n=1..11` (66 `(i,n)` pairs), and at weight 12 the
Euler-route numerator `N12` satisfies `N12·A^2 = 6·[(F^3)_12 - Σ_{i=1..11}
G_iG_{12-i}]`, the completely independent quadratic route from `G^2=F^3`.
Fixture degeneracy note: at weight 12 itself the `i=1` term is silenced by
`G11=0` and `i=8..11` by `F8..F11=0`, so the numerically load-bearing
weight-12 coefficients are `i=2..7`; the full family is pinned by the
lower-weight sweep plus the symbolic derivation.

The legal `F12` term is `18·A^6·F12/(12A^4)=(3/2)A^2F12` — a polynomial for
*every* polynomial `F12`, windowed or not.  The mode born at weight 12 is
`c12·F^0=c12` per the frozen compiler's own schedule (predecessor
`all_modes_retained["12"]="0"`; schedule = even weights 2..20), a constant
lying inside the `G12` window, whose D12 column is identically zero.
**Neither can change the polar class.**  Confirmed.

## 4. Check 3 — numerator reduction, gcd data, Bezout

Independent recomputation (degrees: `deg N12=18`):

* `N12 mod A^4 ≠ 0`; `gcd(N12,A^4)=A·B=C·B^2`; `Nred=N12/(AB)` exact,
  `deg Nred=11`; `A^4/(AB)=C^3B^2`.  So `g12_char = N12/(12A^4) =
  Nred/(12·C^3·B^2)` exactly.  **Verified.**
* `gcd(Nred,A)=1` — no further cancellation; the four `A`-root poles are
  genuine.  **Verified.**
* `Nred(1)=-12`.  **Verified** (sum of coefficients).
* The serialized Bezout cofactors in `RESULT.json` satisfy
  `s·Nred+t·B=1` when re-multiplied with my own arithmetic, and my own
  extended-Euclid run reproduces the identical cofactors.  Hence `Nred` is
  a unit modulo `B`.  **Verified.**

Naming nit (no verdict impact): `Nred/(12C^3B^2)` is the **entire**
characteristic `g12`, not only its polar part — `deg Nred=11 > 8`, and the
division quotient (the polynomial part, degree 2) is nonzero and is
honestly serialized in `RESULT.json`.  The strict polar part is
`remainder/(12A^4)`.  Since `gcd(Nred,A)=1`, all pole-order claims are
unaffected.  See Section 8.

## 5. Check 4 — root-by-root adjudication, and an exact bridge

The decisive new step of this review: eliminating `F12` from the D12 row
via the exact identity `12F12'G0+4F12G0' = 12A^4·(A^2F12)'` (verified on
monomials `X^0..X^13`), the row reads
`D12 = base + 12A^4(A^2F12)' - 8A^4G12'`.  I then verified the **exact
polynomial bridge identity**

```text
3·A·base = 2·A·N12' - 8·A'·N12 ,     equivalently   base = 8A^4·(g12_char)' ,
```

which is forced structurally because `J(F,F^{3/2})=0` holds identically at
weight 12 with the rational coefficient `g12_char`.  Consequences:

* `D12=0` for candidate polynomials is **equivalent** to
  `G12 = g12_char + (3/2)A^2F12 + c12` for a constant `c12`.  In particular
  the antiderivative of `base/(8A^4)` is rational (zero residues, no log
  terms) — a fact the producer used implicitly and this review certifies.
* Pole orders of `g12_char=Nred/(12C^3B^2)` are exact: order **3** at the
  `C`-root `X=1` (`Nred(1)=-12`, `B(1)=4`), and order **2** at each of the
  three simple `B`-roots: `Nred(-1)=-3969/4096`,
  `Nred(±i)=2511/4096 ∓ 1377/4096·i`, with `C(-1)=-2`, `C(±i)=±i-1` all
  nonzero (Gaussian-rational arithmetic, exact).
* **Root-local form.**  Fix any single root `β ∈ {1,-1,i,-i}` and work over
  any characteristic-zero field containing `β`.  For any `F12` and any
  `G12` merely *regular at `β`* (poles allowed everywhere else), `D12=0` is
  impossible: the forced right side has a pole at `β`.  So each `B`-root
  obstructs **independently** of the `C`-root, and conversely.  The
  producer's single-root claim is confirmed and sharpened.

Semantic firewall, as charged: these root statements are field-point
valuation statements at closed points over `Q` (roots `±1`) and `Q(i)`
(roots `±i`).  What *is* scheme-theoretic is only this: the windowed
16-variable D12 extension system of this one fixture generates the unit
ideal over `Q` (Section 6), hence is empty over every `Q`-algebra.  No
scheme-unit, stratum-wide, or non-fixture conclusion is licensed.

## 6. Checks 5–6 — literal raw D12 equation and the 28×16 system

Slot inventory rebuilt directly from `RAW_INPUT.json` (442 records, kinds
`F` and `G` only, all slot names unique; the weight law `w=3x-y+8` for `F`
and `w=3x-y+12` for `G` re-verified on every record).  At weight 12 the
legal new slots are exactly `f_2_2,f_3_5,f_4_8` (`F12: X^2,X^3,X^4`) and
`g_0_0,g_1_3,…,g_12_36` (`G12: X^0..X^12`) — 16 slots, no omission, no
extra kind, and no bound mode outside them (`c12` is the `X^0` slot
direction).  The affine row from the determinant operator is exactly
`D12_base + 12F12'G0 + 4F12G0' - 8F0G12'` (the `(12-12)F0'G12` term has
coefficient zero).

Independent linear algebra over exact fractions (`deg base=17`; the 28 rows
are coefficient degrees `0..27`, the maximum realized by the `G12_X12`
column of degree 27):

* matrix rank **12**, augmented rank **13** — infeasible;
* homogeneous nullity 4 realized by four explicit, verified null vectors:
  `(F12=X^d, G12=(3/2)A^2X^d)` for `d=2,3,4` — note `deg A^2X^d ≤ 12`, so
  these live inside the legal window — plus `(G12=X^0)`;
* the dual functional `Φ=20[X^0]+10[X^4]+4[X^8]+[X^12]` annihilates all 16
  legal columns and `Φ(base)=11009739/16384 ≠ 0`.  Structure: 13 of 16
  columns have support disjoint from exponents `≡0 (mod 4)`; the three that
  touch it are `G12_X1,G12_X5,G12_X9 = -8d·A^4X^{d-1}`, and `Φ` kills
  `A^4`, `A^4X^4`, `A^4X^8` while `Φ(A^4X^12)=1`.  So `Φ` is an explicit
  Fredholm/unit-ideal certificate for the windowed system, and the
  degree-12 window cap is load-bearing *for this certificate*: a would-be
  illicit `G12_X13` column pairs to `-104≠0`.  Infeasibility itself does
  **not** depend on the cap — the Section 5 bridge kills unbounded-degree
  extensions outright.

All producer serializations match my rebuild exactly: `N12`, quotient,
remainder, gcd, `Nred`, denominator `C^3B^2`, Bezout cofactors, base row,
the three canonical-JSON sha256 fields, matrix census `(28,16,12,13)`,
variable order, nullity 4, `Φ(base)`, the zero `g_0_0` column flag, and the
recorded 20→19 mutation table (nonzero pairing only on `G12_X1`, value 8).

## 7. Check 7 — hostile mutation matrix

Independent-checker mutations, each caught by the named check (clean run
has zero failures; every mutation aborts):

| mutation | caught by |
|---|---|
| `G12` operator sign `-8→+8` | `null_vectors_annihilate` |
| `F12` column coefficient `12→11` | `null_vectors_annihilate` |
| base-row coefficient `(12-j)→(13-j)` | `bridge_base_equals_8A4_d_g12char` |
| recurrence sign `((5i-24)/2)→((5i+24)/2)` | `euler_equals_quadratic_route` |
| omit legal slot `G12_X12` | `column_count_16` / slot census |
| illicit extra slot `G12_X13` | `column_count_16` / slot census |
| dual coefficient `20→19` | `dual_kills_all_columns` |

Global operator mutations are additionally excluded because `D0..D11≡0`
pins `(12-j)/(i-8)` on the frozen data.  The two *legal* moves —
`F12=X^2+2X^3+3X^4` and `c12=5` — were confirmed to leave the polar
remainder and the row untouched (null mutations, not flagged), matching the
producer's recorded live mutations.

## 8. Findings that do not change the verdict

1. **Polar naming (documentation).**  `g12_polar=Nred/(12C^3B^2)` in the
   report/TARGET is the full characteristic coefficient, which includes a
   nonzero degree-2 polynomial part; the strict polar class is the
   serialized `remainder/(12A^4)`.  All pole claims survive because
   `gcd(Nred,A)=1`.  Suggested wording: "g12_char", or "polar class of".
2. **Execute-before-pin (custody hardening).**  The producer checker
   `exec`s the predecessor module at import time (`P = load_predecessor()`
   at module scope) *before* `calculate()` asserts the SOURCE pins; the
   predecessor does the same with the prefix compiler.  A tampered
   dependency would execute before failing the hash gate.  No exposure
   here (this review verified all hashes independently from the shell
   first), but verify-bytes-then-exec would be sounder.  Same pattern class
   as the known `shared_faber_probe` unpinned-import gap.
3. Minor robustness nit: `assert not columns[3]` addresses `g_0_0` by
   position; a name-keyed assert would survive window renumbering.

None of these is a mathematical error; 1 is documentation, 2–3 custody or
style.

## 9. Check 8 — bearing on single-root transport / two-scale local model

The proposal (Sol Ultra, `ggv-upper-endpoint-unit-root-transport-…`,
itself **awaiting hostile review** and not adjudicated here) is that at a
simple root `α` of `A` with `V0(α)≠0`, the entire fixed characteristic
cascade and its obstructions transport to the local DVR at `α` via the
two-scale substitution `X=α+ε`, `t=ε^2·s`, so that death is decided
root-locally with no cross-root coupling.  What this packet actually
contributes, on this review's independent verification:

* All three `B`-roots of this fixture are simple `V0`-unit roots
  (`V0(-1)=8`, `V0(±i)=4±4i`), and each obstructs D12 **by itself**, with
  an order-exactly-2 pole, even if `G12` is allowed poles at every other
  root; the `C`-root obstructs separately at order 3.  That is precisely
  the decoupled, root-local failure mode the two-scale model predicts, at
  the earliest row where this proper-divisor prefix can die — one honest
  data point of the mechanism, with no hidden global coupling detected
  (the Bezout unit-mod-`B` certificate is exactly the statement that the
  `C`-side cancellation `gcd(N12,A^4)=A·B` never eats a `B`-root).
* It is **only** a data point.  One fixture, one prefix, one row: it does
  not prove the transport theorem, does not show every proper-divisor
  prefix dies at D12 (a different prefix changes `N12` and could in
  principle make `A^4 | base`), and does not constrain the deep `C=A`
  (`A|V0`) stratum, where no root is a `V0`-unit.  Any promotion of the
  transport mechanism must come from its own packet's review, not from
  this fixture.

## 10. Strongest promotable statement

Under exactly these hypotheses — the byte-pinned predecessor prefix
(`F0..F11`, `G0..G11` as frozen, all characteristic modes zero), the
determinant operator `D_n=Σ_{i+j=n}(12-j)F_i'G_j+(i-8)F_iG_j'`, and the
RAW_INPUT weight-12 windows `F12⊆{X^2,X^3,X^4}`, `G12⊆{X^0..X^12}`:

1. **(Windowed, scheme-level for this fixture only.)**  The 28
   affine-linear coefficient equations of `D12=0` in the 16 legal slot
   variables generate the unit ideal of `Q[16 slots]`; explicitly,
   `(16384/11009739)·Σ_{d∈{0,4,8,12}} Φ_d·(coefficient-d equation) = 1`.
   Hence there is no legal D12 extension over any field extension, indeed
   over any `Q`-algebra.
2. **(Unbounded strengthening.)**  There is no extension even with
   `F12,G12` arbitrary polynomials of arbitrary degree: `D12=0` forces
   `G12 = Nred/(12C^3B^2) + (3/2)A^2F12 + c12`, whose right side has poles
   of exact orders `3,2,2,2` at `1,-1,i,-i`.
3. **(Root-local.)**  At each individual root of `A`, over any
   characteristic-zero field containing it, no `G12` regular at that root
   alone can satisfy `D12=0`, for any `F12` and any `c12`.

Scope firewalls: this kills only the one frozen rational D11 prefix.  The
q1 locus itself still rests on the provisionally reviewed D23 licensing
theorem upstream.  Nothing here is a proper-divisor-stratum theorem, a
universal single-root transport theorem, a branch-P exclusion, an endpoint
or GGV-landing statement, a scheme-unit statement about any stratum, or a
JC2 result.

## 11. Review log

Files read: the two charged xmodel reports; the packet's
`verify_q1_d12_obstruction.py`, `RESULT.json`, `TARGET.json`,
`SOURCE.sha256`, `EVIDENCE.sha256`, `README.md`; predecessor
`verify_q1_post_d9_d11.py` and `RESULT.json`; `RAW_INPUT.json` (D3 case);
prefix compiler `verify_q1_prefix_target.py` (helper-semantics audit
only); `ggv-upper-endpoint-unit-root-transport-sol-ultra-20260828.md`
(context for check 8).  No canonical file was modified; the `jc2-lean`
tree was not touched; no network, CAS, or AWS was used.

Commands (all read-only or `/tmp`/xmodel-report writes): the two
`shasum -a 256` verifications of charged hashes and manifests; three
`python3 -c` inspection one-liners over `RAW_INPUT.json` and the
predecessor `RESULT.json`; `grep`/`sed` reads of the prefix helpers; the
two `--check` replays (outputs quoted in Section 1); development runs of
the review checker in `/tmp`; final run
`python3 -B xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-hostile-review-fable5-20260828-check.py`
→ `ALL CHECKS PASSED` with the mutation matrix of Section 7.

Review checker hash:

```text
e933da5b6b329758eb44a2001c95f7a0e339b79ca49c59db84d6fbce17a55ef6  xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-hostile-review-fable5-20260828-check.py
```

Final report hash command:

```bash
shasum -a 256 xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-hostile-review-fable5-20260828.md
```
