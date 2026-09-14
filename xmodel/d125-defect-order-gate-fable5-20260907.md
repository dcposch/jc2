# Gate: D125 defect-weighted leading variables (Fable 5.1, 2026-09-07)

Status: **GATE COMPLETE**, 2026-09-07 01:56 UTC. Charged discriminator body SHA `222e48e9…` (frozen file `9b6f972b…`), `check.py` `5fb9827d…`, `witnesses.json` `6e8c0102…`, `baseline.py` `ec2fa2d1…`: all MATCH the charge. Frozen inputs only; no CAS, engine, AWS, live peer file, ledger, full J/lift expansion or stream read. Every command ran under 30 s wall, 25 s CPU, 512 MiB AS; largest observed 0.57 s and 40 MB.

## Verdict table

| claim | verdict |
|---|---|
| Leading-ideal theorem: the unchanged 269-variable, 803-row ideal contains 192 polynomials leading at the 192 nonkernel free B variables | **CONFIRMED** (§2) |
| Global order and descriptor: positive W1 on all 269 names, well-order, digests `64c212…` and `d894d6…`, complement 77 | **CONFIRMED**; original-dp digest `ccd93c…` is a **GAP** (§3) |
| Documented syntax: `a(...)` rows with zeros refined by `dp`, slimgb needs a global basering | **CONFIRMED** in content; both cited line ranges are wrong; three consecutive `a` blocks are not exemplified (§4) |
| Proposed order-aware checker requirements | **CONFIRMED** as stated, one requirement added; no checker or engine validated (§5) |

## 1. Inputs and method

Dependency accepted, not re-proved: the B kernel theorem and the exact block ranks from the reconstruction gate. Reviewed here: the new ordering argument only.

Own control `gate_own.py` in `box/d125-defect-order-gate-fable5-20260907/` differs from the producer's `check.py`. It builds every block matrix by explicit bracket differentiation of the fixed `H^3` against each free monomial and checks the `(pd-15i)h_p` formula as a consequence. It takes free columns, faces and fixed constants from `make_contract('unequal','rational')` loaded from an explicit relocated baseline path. It censuses every actual A-slot times B-slot forcing pair by weighted key against the actual pivot keys of its block, instead of the producer's degree census. It records the largest gamma row each block uses, computes kernels as exact nullspaces of the full free-column matrix, and replays the two tiny Groebner comparator controls of the charge with its own division routine. No J coefficient or lift row is ever formed.

## 2. Leading-ideal theorem

Setup confirmed from the contract: `A_15=H^3`, `B_25=H^5` with `H=pi^2(pi^3+gamma^3)`; the only lower fixed nonzero slots are `A_(2,1)=1`, `B_(1,0)=5/9`, `B_(8,5)=5/3`; origins fixed zero; free B columns at degree d are exactly `i=0..floor((7d+4)/12)`, 196 in total.

Layer argument. Coefficient extraction of `J=A_gamma B_pi-A_pi B_gamma` is bilinear: one A slot times one B slot with factor `il-jk`. Physical degree `d+13` receives exactly `[H^3,B_d]` plus pairs `(A_k,B_e)` with `k+e=d+15`, `k<15`, hence `e>d`. No B slot of degree below d, no B-times-B term and no lift variable enters. The 105 lift rows and the degree-2 target are untouched and unused.

Weights. A free `B_d` slot has `(W1,W2)=(25-d,25-d)`. Every actual forcing pair at layer d is strictly smaller: free-free gives `(25-d,25-e)` with `e>d`; fixed A with free B gives `W1=25-e<25-d`; free A with the degree-25 fixed B gives `(25-d,0)`; anything else is a constant, including `[H^3,K_d]`. I checked this on all 12,778 actual nonzero-determinant slot pairs, not on degree classes; the largest forcing prefix is `(24,23)` at d=1 from `A_(0,14)` times `B_(1,1)`, against the pivot's `(24,24)`. Constant rational row operations preserve the property: the pivot variable keeps coefficient one and no forcing monomial can rise.

Blocks. The explicit bracket matrix has nonzero rows only at gamma exponent `r<=q_d+8<=22`, so every row used is a literal row of the 660-row source envelope `0<=I<=23`, `I+J<=38`; the 780-versus-660 distinction is irrelevant, and rows with `I>23` are identically zero anyway. Descending-column RREF gives pivots `q_d..0` in the 20 nonkernel blocks and `q_d..1` in the four kernel blocks, ranks summing to 192 over 196 columns. The exact nullspace at `d=5,10,15,20` is one-dimensional and equals the coefficient vector of `H^(d/5)`, inside the free columns with `pi^d` coefficient 1. The graph complement is `71+4+2=77`.

Leading monomials. In a nonkernel block the reduced row is `b_i` plus forcing, so it leads at `b_i`. In a kernel block it is `b_i+c*b_0` plus forcing, and `W3(b_i)=i>0=W3(b_0)` decides for `b_i`; under dp alone `B_g0_p5` precedes `B_g3_p2` in the displayed order and would lead, which my reversed-W3 mutation reproduces at `d=5`, column 3. Hence rational combinations of literal rows give 192 ideal elements leading at the 192 nonkernel free B variables. **CONFIRMED.** The corollary that any Groebner basis of a proper ideal contains elements with exactly those leading monomials is correct, since a divisor of a variable is the variable or 1. Nothing about dimension, properness, discovery time or fill follows, as the charge says.

## 2. Leading-ideal theorem

## 3. Global order and descriptor

W1 is 1..24 on all 269 names (A `15-i-j`, B `25-i-j`, lambda 3 and 2), so `1<x` for every variable, and the lexicographic combination of three weight rows with dp is a multiplicative well-order. Rebuilding the three rows from the name strings alone reproduces the witness vectors, the descriptor digest `64c212c2…` and the ring-declaration digest `d894d642…` exactly, and the witness ring string byte for byte. **CONFIRMED.**

GAP: the statement that the same names with the original dp descriptor reproduce the first-attempt ring digest `ccd93ccf…` is unverifiable here. The original declaration string is not among the frozen inputs, and four natural spellings of `ring R=0,(names),dp;` do not hash to it. Unverified, not refuted.

## 4. Documented syntax

I fetched both linked Release-4-3-2 files (copies in the owned box). The "Extra weight vector" node defines `a(w_1,...,w_n)` for "any integers (including 0)", compares weighted degree first, and says it "can only be used in combination with other orderings to insert an extra line of weights into the ordering matrix", with `(a(1,2,3),dp)` as an example. The matrix display for `(a(1,2,3,4,5),Dp(3),ds(3))` shows the `a` row spanning all variables with zero padding, so an `a` block consumes no variables. The slimgb node says the basering ordering "has to be global" and that `option(redSB)` returns a reduced basis. The general definition says global orderings are well-orderings with `1<x_i`. Zero entries, refinement by dp and the global requirement are therefore documented. **CONFIRMED in content.**

Citation defects: pdata.doc lines 1181-1290 cover matrix and product orderings; the `a(...)` node starts at line 1302 of the fetched file. reference.doc lines 7037-7057 are the `simplify` node; slimgb is at lines 7163-7185. Three consecutive `a(...)` blocks are nowhere exemplified in the fetched text, only implied by "insert an extra line"; the pending installed-engine control is the only possible evidence for that form, and I claim no engine validation.

## 5. Proposed order-aware checker requirements

The properness logic is sound. If G passes Buchberger's criterion under the weighted order, has nonzero normal form of 1, and reduces every one of the 803 original rows to zero, then the original ideal lies inside the proper ideal generated by G; no `G subset I` proof is needed. The unit branch is order-independent as stated. Own replay of the two comparator controls: `{x-y^2, z-y^3}` with first weights `(3,1,4)` leads at `x,z`, is a Groebner basis with nonzero normal form of 1, and is not a dp basis, the dp S-remainder being `x*y-z` up to sign; `(x*y-1,x^2)` fails Buchberger under both orders. **CONFIRMED.**

Requirement to add: the checker's Buchberger and normal-form routines must use the same three rows and the same dp tie-break as the engine declaration, with the bound descriptor digest recomputed from the rows the checker actually used, never copied from the driver. My `tiebreak` mutation shows the digest changes when only the tie-break token changes. No checker exists yet; nothing here validates one.

## 6. Controls and custody

Producer `check.py`, replayed from a relocated temp tree with the frozen baseline: normal and `-O` output is byte-identical to the frozen `witnesses.json`; the three mutations reject in both modes at the intended messages (`W2 forcing separation`, `W3 kernel marking`, `restricted exact pivot/kernel mismatch`).

Own `gate_own.py` (SHA `827d543c…`, output `out_own.json` `4eaaf703…`), normal and `-O`: pass, 0.30 s and 0.47 s, 21 and 27 MB. Mutations, both modes: `w2` (zero second row) rejects at the slot-pair census, block d=1, pair `A_(0,1)` times `B_(1,14)`, which the producer's degree census also catches; `w3` (negated third row) rejects at the kernel-block leading test, d=5 column 3; `envelope` (cap `I<=21`) rejects at d=24, row 22; `tiebreak` (`lp` token) rejects at the descriptor digest. Two earlier own bugs, a comprehension precedence slip and a hard-coded pivot prefix that let `w2` pass, were fixed before these results; the fixed script is the only one cited.

Owned files, all in `box/d125-defect-order-gate-fable5-20260907/`: `gate_own.py`, `out_*.json`, `*.out`, `*.err`, `input_pins.txt`, `pdata.doc`, `reference.doc`. No process retained, no live file, ledger, lane or protected project touched. **STOP.** The order proposal is confirmed as a leading-ideal statement; the installed-engine control, any checker and any solve remain outside this gate.

<!-- BODY-END -->
