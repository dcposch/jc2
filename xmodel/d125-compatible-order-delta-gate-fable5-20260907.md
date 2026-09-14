# Delta gate: appended W4/W5 rows expose 27 A-Hermite leaders (Fable 5.1, 2026-09-07)

Status: **GATE COMPLETE, verdict CONFIRMED** at exact leading-ideal scope, 2026-09-07 02:15 UTC.
Charged desk report `3a20ea61…`, its `check.py` `f139eb51…`, `witness.json` `86804185…`,
`baseline.py` `ec2fa2d1…`, Hermite producer `b6a81fc0…`, its gate `7e2594d5…`, my defect-order
gate `7fdb1098…`, FALLACY-v2 `e47fd16c…`: all eight frozen inputs rehashed (`input_pins.txt`) and
MATCH the charge. Frozen inputs only. No CAS, engine, AWS, solver, live file, ledger, J-row or lift-row
polynomial expansion. Every run under 30 s wall, 25 s CPU, 512 MiB AS; largest 3.8 s and 40 MB.
Consumed, not re-proved: the accepted three-row B theorem (192 leaders, kernel blocks at d=5,10,15,20),
the 105-row lift exponent law and the unimodular Hermite minors. This is a desk reserve review; the
running three-row code and its engineering test are untouched.

## Verdict table

| delta claim | verdict |
|---|---|
| Five-row order is a global monomial well-order; W1 positive on all 269 names despite negative W5; W4,W5 vanish off A; descriptor digest `97fc8241…` reproduced from names alone | **CONFIRMED** (§1) |
| Each A-lift layer `s=1..14`, after the constant unit Hermite row operations, yields `ceil(s/5)` polynomials leading at the selected free variables `A_(i,s-i)`, `i<ceil(s/5)`; 27 in total | **CONFIRMED** (§2) |
| The 192 accepted B leaders are retained: no B comparison reaches W4 or W5 | **CONFIRMED** (§3) |
| Same 269 names, 803 rows, faces, field, target; no localization or substitution; complement 50 is a name count | **CONFIRMED** (§4) |
| Producer six-run replay from the frozen inputs | not replayable here, custody note only (§5) |

## 1. Order

Rebuilding all five rows from the variable names (`15-i-j`, `25-i-j`, 3, 2; `25-i-j` on B; `i` on B; `15-i-j` on A; `-i` on A) reproduces the frozen witness rows byte for byte and the five-row descriptor digest. W1 ranges 1..24 and is positive on every name, so `1 < x` for each variable and the lexicographic weight comparison refined by dp is a multiplicative well-order; the negative W5 entries (down to −8) are consulted only after four ties and cannot break globality. Zeroing W1 on lambda3 is rejected by my control at that check.

## 2. A-Hermite leaders

Using the consumed exponent law `i+j = s+3b+2d`, `t+b+d <= j`, I enumerated every actual term of every A-lift row `(s,t)`, `1<=s<=14`, over the 83 lattice points of my own half-plane census (which reproduces the contract's 71 free and 12 fixed A slots, with nonzero fixed values only at the four top monomials and `A_(2,1)`). Every multinomial coefficient is nonzero, and the `b=d=0` part of the selected columns equals `(-1)^(s-i-t) C(s-i,t)` exactly. All 14 minors have determinant `(-1)^(rs+r(r-1)/2)` by integer Bareiss, with adjugate inverses verified as integer two-sided inverses. Left-multiplying by that constant inverse gives each selected variable coefficient one and kills the other selected variables; nothing else in the rows changes class. Against every selected pivot of its layer, every remaining term is strictly smaller:

| term class | comparisons | decided at |
|---|---|---|
| free `A_ij λ2^b λ3^d`, `b+d>0` | 1650 | W4 |
| same-layer unselected free `A_(h,s-h)`, `h>=r` | 255 | W5 |
| fixed top coefficient times λ monomial | 283 | W4 |
| fixed `A_(2,1)` times λ or constant | 2 | W1 |

The two comparisons the desk names decide at W4 (`A_g0_p1` against `λ3·A_g0_p3`) and W5 (`A_g0_p2` against `A_g1_p1`). Zero prescribed coefficients contribute nothing; the three `s=15` rows are the consumed identities. Hence the 27 reduced rows lead at 27 distinct single variables. No descending substitution is used, because a leading monomial is a property of one polynomial; the higher pivots inside the forcing terms are simply smaller monomials. **CONFIRMED.**

## 3. B inheritance

The accepted argument decides each B comparison at W1, W2 or W3. I replayed it with the five-row key: all 12,778 nonzero-determinant forcing pairs `(A_k, B_e)`, `k<15`, `k+e=d+15`, against every free `B_d` column give 1,125 decisions at W1 and 99,719 at W2; all 1,804 same-layer free B pairs decide at W3. No comparison reaches W4 or W5, so appending them cannot reverse any earlier strict decision, and the 192 leaders, including the kernel-block `b_i` over `b_0`, are unchanged. **CONFIRMED.**

## 4. Scope

Names equal the contract's 267 free coefficients plus the two lambdas; an order change touches no generator, so the 803 rows, both fixed faces, the coefficient field Q, the target gauge and the lift stay as they are. Leaders 27+192=219 are distinct variables, so a Groebner basis of a proper ideal must contain elements with exactly those leading monomials. The complement 50 = 44 retained A + 4 B kernel scalars + 2 lambdas is a count of names, not a dimension, properness, fill or discovery statement.

## 5. Controls and custody

Own `gate_own.py` (SHA `60525071…`, stdlib, zero Assert nodes, explicit `--baseline`/`--witness` paths): normal and `-O` pass with byte-identical output (`b460190f…`), 3.7 s / 3.8 s, 20 / 26 MB. Mutations reject in both modes: `no-w4` and `reverse-w5` at the named comparison directions, `bad-matrix` at the `s=6` unit minor, `w1-zero-lambda` at globality. One own bug fixed before citing: a same-layer counter that stored a flag instead of a count.

Custody note: the producer's `check.py` hardcodes repository-relative paths and pins a three-row `witnesses.json` (`6e8c0102…`) that is not among the frozen inputs, so its six-run result is not replayable from this lane; a rebuilt three-row file does not reproduce that digest. My control covers the same content independently. Out of scope and unclaimed: any installed-engine reading of five `a()` blocks, any checker, speedup, properness, unit or JC2 conclusion. Artifacts: `box/d125-compatible-order-delta-gate-fable5-20260907/` (`gate_own.py`, `out_*.json`, `err_*.txt`, `runs.txt`, `input_pins.txt`, `own_sha.txt`, `producer_*.err`). **STOP.**
<!-- BODY-END -->
