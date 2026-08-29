# Hostile review: exact origin-residue exclusion on the symmetric deep slice

Date: 2026-08-28
Reviewer: Fable 5 (independent hostile audit)
Verdict: **PASS — theorem CONFIRMED on its stated slice; generalization
refusal CONFIRMED by exact `Q=X` counterexample replay**

## 0. Frozen target and custody

All hashes verified byte-identical at audit start and end:

```text
xmodel/ggv-upper-endpoint-origin-residue-slice-sol-ultra-20260828.md
  7202f70380c8379d85dab82e4ef06f47b1312ba840775d8581eaa629ed328e30
cases/ggv_8_28_upper_endpoint_origin_residue_slice_20260828/
  verify_origin_residue_slice.py
  de371953d4bc22da7cfc39c4e94221097eac7612b7b4a8b44afe0fd14ecb76e0
xmodel/ggv-upper-endpoint-deep-q1-lambda0-even-subbranch-origin-coupling-
  independent-sol-ultra-20260828.md
  c940ba048f5edf60b3018670c8914acc469f55f30101f211a6aedb5d591b6714
```

Formula sources pinned (bytes hashed, producer code neither trusted nor
imported): odd-gate tail packet `b649e082...`, q15 packet `18831713...`,
origin-coupling lemma `3e4a0f03...` with its checker `f23a6d95...`, and the
authoritative window source `RAW_INPUT.json` `28b9b05c...`.

Fresh standalone checker (standard library only, exact rationals, run with
`PYTHONDONTWRITEBYTECODE=1 python3 -B`):

```text
xmodel/ggv-upper-endpoint-origin-residue-slice-hostile-review-fable5-
  20260828-check.py
```

Final marker: `PASS_HOSTILE_ORIGIN_RESIDUE_SLICE_FABLE5`.  The frozen
producer checker was also replayed read-only and printed its own marker;
no verdict rests on it.

## 1. T5 exactness theorem and completeness of the q parameterization

Independently re-proved and machine-checked:

- `T5(d)=(5A'd+2Ad')/2` satisfies `deg T5(d)=deg d+3` with leading
  coefficient `(k+10)·lc(d)`, hence **zero kernel** in characteristic zero,
  and `d(p^5 d)=p^3 T5(d) dX` (sufficiency verified as the polynomial
  identity `2A(A^2d)'+A'(A^2d)=2A^2·T5(d)`).  Necessity uses: pole
  multiplier `1-2m` never vanishes, and `A'=4X^3` is a unit mod `A=X^4-1`
  with explicit inverse `X/4` (both machine-checked).
- On the slice the reviewed odd coefficients collapse to `h5=0`,
  `h7=f/4`, `h9=F9/4`, `h11=A·F11/4`, `h13=A^2·F13/4`, `h15=0` (verified by
  transcribing the complete frozen `h5..h15` formulas and specializing
  `Q=e=F8=r=0`; the `F10` term of `h15` is killed by `r=0`, so `F10` need
  not be constrained).  Hence **q5 and q15 are automatic** (primitives
  `d5=d15=0`), and q7/q9/q11/q13 are exactly the four `T5` equations.
- Completeness of the displayed primitives, derived rather than assumed:
  - q7: `deg f<=5` forces `deg d7<=2`; no floor on `f`; `f=4T5(a0+a1X+a2X^2)`
    with support `{0,1,3,4,5}` inside window `0..9` of `F7=Af`.
  - q9: `deg F9<=7` forces `deg d9<=4`; the authoritative constant floor
    (weight-9 F window is `X^1..X^7`, no `X^0` slot) forces the primitive
    X coefficient: `F9[X0]=-4·d9[X1]`, so `b1=0`.  Support `{1,2,3,5,6,7}`.
  - q11: `A·F11=4T5(d11)`; `A|T5(d11)` iff `A|d11` because
    `X·(X^3 d mod A)=d mod A` (X^3 invertible mod A); `deg F11<=5` forces
    `d11=A·k`, `deg k<=2`; the weight-11 constant floor gives
    `F11[X0]=-4·k[X1]`, so `k1=0`.  Support `{1,3,5}`.
  - q13: `A^2·F13=4T5(d13)`; two successive reductions mod squarefree `A`
    (second uses `A'` a unit mod `A`) force `d13=A^2·ell13`, and
    `deg d13<=8` makes `ell13` a scalar; `F13=72·ell13·X^3`, inside the
    `{X^2,X^3}` window.
  No legal raw or primitive mode is omitted: the degree bounds are exact
  (`T5` strictly raises degree by 3) and every floor used is a literal slot
  absence in the pinned `RAW_INPUT.json`.

## 2. Complete characteristic reconstruction of G11 and G15

An independent fractional-power recurrence (`w F0 S_w = sum ((e+1)i-w)
F_i S_{w-i}`, sheet convention `S_0=A^(4e)`, i.e. the reviewed literal
`A^(6-k)` branch factors) rebuilt all ten modes
`G=F^(3/2)+sum_{k=1..10} c_{2k} t^{2k} F^((6-k)/4)` through weight 15 in
the canonical ring `K[X,1/A]` (numerators reduced to minimal A-power).
Self-tests `(F^(1/2))^2=F` and `F^(1/2)·F^(-1/2)=1` pass through weight 15.
Crucially, the even slots `F10,F12,F14` — which the slice does **not** fix —
were kept fully symbolic on their literal windows, and all ten `c` modes
symbolic.  Result:

```text
G11 = (3/2)A^2 F11 + (5/4)c2·A·F9 + c4·F7                (exact match)
G15 = (5/4)c2·A·F13 + c4·F11 + (1/A)((3/4)c6·F9 + (1/2)c8·f)
```

with `F10,F12,F14,c10,...,c20` provably absent from both weights:
`c10,c12,c14` enter through `[t^5]F^(1/4)`, `[t^3]F^0`, `[t^1]F^(-1/4)`,
all zero because `F5=F3=F1=0` (machine-checked), and `c16..c20` are unborn
at weight 15 since `2k>15`.  No born or predecessor mode was dropped.

## 3. Residue division and the endpoint identity

Exact monic division of the pole numerator `(3/4)c6·F9+(1/2)c8·f` by `A`
gives the **full** remainder (independently derived, all four
coefficients):

```text
R = 20c8·a1 + 10(3c6·b2+2c8·a2)·X + 30c6·b3·X^2
    + (30c6·(b0+b4)+20c8·a0)·X^3,
```

so `R[X1]=10(3c6·b2+2c8·a2)` as claimed.  The endpoint slot law
`D22[X0]=F11[X1]·G11[X0]-F7[X0]·G15[X1]` was re-derived from the literal
pinned windows: term `F_i'·G_j` needs an `F_i` `X^1` slot (`i<=11`) and a
`G_j` `X^0` slot (`j<=12`), leaving `(10,12)` killed by `12-j=0` and
`(11,11)` with `+1`; term `F_i·G_j'` needs an `F_i` `X^0` slot (`i<=8`) and
a `G_j` `X^1` slot (`j<=15`), leaving `(8,14)` killed by `i-8=0` and
`(7,15)` with `-1`.  The `+1` target is the Keller normalization
`J(P,Q)(0)=1` via the slot dictionary
`(f_1_0,f_0_1,g_1_0,g_0_1)=(P_x,P_y,Q_x,Q_y)(0)` (checksum verified).
With the independently derived slot values

```text
F11[X1]=-8k2,  G11[X0]=4a1·c4,  F7[X0]=4a1,
G15[X1]=-8k2·c4+36c6·b2+24c8·a2   (legal quotient),
```

the `c4` terms cancel exactly and

```text
D22[X0] = -48·a1·(3c6·b2+2c8·a2),
5·D22[X0] + 6·F7[X0]·R[X1] = 0        (exact polynomial identity).
```

Polynomiality of `G15` is coefficientwise vanishing of all four
coefficients of `R`; in particular `R[X1]=0`, hence `D22[X0]=0`,
contradicting the required target `+1` (and equally `-1`).  Every
normalization, derivative coefficient, and sign in this chain was
recomputed from scratch.  **Theorem (2) of the frozen report is CONFIRMED**
on the strict slice `A=X^4-1, lambda=0, exact D=0, Q=e=F8=r=0`.

## 4. Field/scheme scope

- Coefficient domain: the identities are polynomial identities over
  `Z[1/2,1/3,1/5]`; the exclusion holds for solution points valued in any
  field of characteristic zero (as claimed).  The parameterization
  completeness (pole-order argument, unit reductions mod squarefree `A`)
  is a field-level argument; the residue identity itself is ring-level, so
  the conclusion also holds coefficientwise over any characteristic-zero
  algebra when "G15 polynomial" is read as `R=0` coefficientwise.
- `c2!=0` is **not load-bearing**: the checker verifies `c2` occurs in
  neither `R` nor the endpoint identity (it multiplies only the polynomial
  `(5/4)A·F13` and `G11` terms).  Its presence in the hypothesis is
  harmless scope narrowing inherited from the branch definition — correctly
  so reported, not silently used.
- The slice does not need to fix `F10,F12,F14`; the theorem is insensitive
  to them (Section 2), which slightly strengthens the frozen statement.

## 5. Arbitrary-Q negative control (frozen `Q=X` mutation)

Independently replayed with `A=X^4-1, Q=X, e=F8=r=0, c2=c6=1`:

- All five primitives verified exactly against the complete frozen
  `h7..h15` formulas: `h_n=T5(d_n)` for
  `d7=(2^27/75)X`, `d9=-(2^21/15)X^2`, `d11=(2^14/3)X^3`,
  `d13=-(7·2^8/15)X^4`, `d15=X^5`; `h5=0`.  A denominator mutation
  (`2^15 -> 2^14` in the `Q^2 f` term of `h11`) is detected.
- The complete ten-mode characteristic recurrence reproduces the frozen
  closed forms `G11=A·P11` and `G15=-(2^21/5)X+(2^10/3)X^3` exactly;
  `G15` is **polynomial** (no A-pole), `G11` support lies in `X^1..X^13`,
  `G15` support in the literal `X^1..X^9` window.
- Origin pairing: `F11[X1]=G11[X0]=0`, `F7[X0]=2^29/75`,
  `G15[X1]=-2^21/5`, so `D22[X0]=2^50/375 != 0`; with all odd slots scaled
  by `th` the pairing is exactly `(2^50/375)·th^2` (linearity through
  weight 15 machine-verified), and substituting `th^2=375/2^50` gives
  exactly `+1`.

So legal q7–q15 primitives, legal G11/G15 windows, G15 polynomiality, and
nonzero (indeed unit) origin pairing coexist at `Q=X`: the fixed-slice
residue identity **cannot be promoted to arbitrary `Q`**, confirming the
frozen refusal.  No claim is made (or supported) that this mutation is a
full endpoint survivor: other G windows, the four-root endpoint system,
and remaining raw rows were not imposed.

## 6. Hostile mutation battery (all detected)

1. Restoring the forbidden primitive X coefficient: `F9[X0]=-4b1` and
   `F11[X0]=-4k1` collide with the literal absence of the weight-9/11
   `X^0` slots in pinned `RAW_INPUT.json`.
2. Dropping a characteristic mode (`c8` term of `G15`): mutated closed
   form no longer matches the independent recurrence reconstruction.
   (Note: mode-dropping is invisible to the internal 5/6-identity alone —
   the identity re-balances; the recurrence comparison is the load-bearing
   detector, which is why the audit rebuilt the full schedule.)
3. Changing one fractional coefficient (`(3/4)c6 -> (3/8)c6` in `G15`;
   `(5/4)c2 -> (3/4)c2` in `G11`): recurrence mismatch.
4. Changing a residue coefficient/sign (`+2c8a2 -> -2c8a2`; `10 -> -10`;
   `+6 -> -6` in the identity): all break exact equalities.
5. Replacing target `+1` by `-1`: the exclusion itself is sign-robust
   (`D22[X0]=0` contradicts both); the `+1` normalization is pinned by the
   `J(P,Q)(0)` checksum, and flipping a pair-law sign breaks it.
6. Substituting `Q=X` into the fixed-slice conclusion: refuted by the
   Section 5 replay (`D22[X0]=2^50/375`, scalable to `+1`).

## 7. Defects

None.  No first defect to name.  Two harmless observations: (a) the frozen
report's `c2!=0` hypothesis is unused by the proof (Section 4); (b) the
even-subbranch packet describes the G11 window as `X^1..X^13` while the
pinned window table includes an `X^0` slot (`g_0_1`) — the narrower claim
is a subset statement about the mutation's `G11=A·P11` and is not relied
on here.

## 8. Scope firewall

Confirmed strictly for `A=X^4-1, lambda=0, exact D=0, Q=e=F8=r=0`, in
characteristic zero.  Nothing here promotes the result to arbitrary `Q`
(explicitly refuted), another `A`, another branch or D-valuation, the full
endpoint, Keller, or JC2.
