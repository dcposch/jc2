# Gate: exact low-row k-saturation and finite-arc consequences (Fable 5.1, 2026-09-07)

Bounded 12-minute hostile gate of `xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md` (frozen SHA `57d85da3…`, whole text read) with its `check.py` and `witness.json` (`37fc6434…`), read from `/tmp/jc2-lane.weMw0p/inputs` only, with the parity normalization, the zero-k classification and its gate, the preflight/`client.py`, the Hermite gate and the B-reconstruction gate as literal interfaces. Root's checker read, eight-run replay and transaction root `c004f483…` are taken as given. The promoted 14c moving-face theorem and 14f boundary classification/unramified obstruction are consumed, not re-reviewed; only the literal interface values used here were checked. Scope is total degrees 0 and 2 of the normalized odd source; no degree-15/25 pair, R³/R⁵, 803-row/full-source ideal, CAS, AWS, SSH, solver, live peer, ledger or adapter was touched. No frozen file was modified.

## Verdict table

| item | verdict |
|---|---|
| 1. Exact total-degree 0/2 rows from odd A₁,A₃,B₁,B₃ with d=5k²/9 and target −5k³g²/9; [A₁,B₃] terms retained before a01=0 | **CONFIRMED** |
| 2. I_low : k^∞ = (a01, 9e−5k·a12, a12²−3k·a03); k², k³, k⁴ certificates and reverse inclusion exact; contraction by k-saturation of a domain; equality after k-inversion survives arbitrary further quotients; no full-source saturation/properness/point claim | **CONFIRMED** |
| 3. The three raw eliminations are not three additional savings over the A-Hermite/B-reconstruction graphs; literal 7→5 term count only; no cost, source, cap or implementation change | **CONFIRMED** (one pre-existing double booking of e noted, §3) |
| 4. DVR arc interface: α(t+3)=γ(t+3)=0, a03=−(t+3)³+αt, ord(k)=2·ord(a12) when the a03 residue is nonzero, t=−3/α=0 exception persists, inverse need not extend, no degeneration guarantee, no ramified exclusion, nonreduced low boundary | **CONFIRMED**; the report's "PROVISIONAL" label on the classification is stale (§4) |
| 5. Scope, controls, stop clauses, actual unguarded countercontrol | **CONFIRMED** |

## 1. Literal low rows (item 1)

With [A,B]=A_gB_p−A_pB_g, the bracket of homogeneous parts of degrees i,j has total degree i+j−2. Odd parity leaves exactly (1,1) for degree 0 and (1,3),(3,1) for degree 2; degrees 1 and 3 are vacuous. Own control C5 adds generic degree-5 terms to A and B and finds the degree-0/2 parts unchanged while degree 4 moves. The prescribed values are the parity table's A_(2,1)=k, B_(1,0)=5k²/9 and scalar c₀k³ with c₀=−5/9. The rows are

```
r0   = -(5/9) k^2 a01
r_gp = 2 k e - (10/9) k^2 a12 - 2 a01 b21
r_p2 = a12 e - (5/3) k^2 a03 - a01 b12
g^2  : -(5/9) k^3 + (5/9) k^3 = 0
```

The a01·b21 and a01·b12 terms are genuine [A₁,B₃] contributions and are present before any use of a01=0; control C2 tests their literal coefficients, and the omission mutation fails there first. Nothing else of degree ≤2 exists. CONFIRMED.

## 2. Saturation (item 2)

Controls C6–C9 verify, as polynomial identities over Q with every other coefficient an indeterminate, the three certificates k²a01=−(9/5)r0, k³h1=(9/2)k²r_gp−(81/5)b21·r0, k⁴h2=(9/5)k³r_p2−(9/10)a12·k²r_gp+(81/25)(a12·b21−k·b12)r0, and the reverse identities r0=−(5/9)k²a01, r_gp=(2/9)k·h1−2a01·b21, r_p2=(1/9)a12·h1+(5/9)k·h2−a01·b12. Hence k⁴G ⊆ I_low ⊆ G. Contraction: a01 and e are eliminated by generators linear in them with unit coefficients, so S/G is a polynomial ring over Q[k,a12,a03]/(a12²−3k·a03); that generator is primitive and linear in a03 over Q[k,a12], hence irreducible, so the quotient is a domain in which k≠0. Thus k is a nonzerodivisor on S/G, G:k^∞=G, and G ⊆ I_low:k^∞ ⊆ G:k^∞=G. The argument uses only that the remaining coefficients are free; the report says so. Because both inclusions are polynomial identities, they persist under every ring map, and wherever k is a unit (the guarded ring and any of its quotients, nilpotents included) I_low and G generate the same ideal. The report correctly limits this to the low ideal: I_low≠G unguarded (C10: k=0, a01=a12=1 kills the rows, not a01 or h2), and nothing about the full-source saturation, properness or points is asserted. CONFIRMED.

## 3. Presentation (item 3)

Literal term counts are 1+3+3=7 for the rows and 1+2+2=5 for G; no timing exists and none is claimed. The Hermite gate's pivots c_{i,s−i} with i<⌈s/5⌉ put a01 at level 1 and a03 at level 3 (a12=c_{1,2} is retained), and the B-reconstruction gate's free B₁ columns are i≤⌊(7+4)/12⌋=0, so e=b_{0,1} is the unique free B₁ column, eliminated in the d=1 descent step. All three raw eliminations therefore land on coordinates already graphed, and the sparse relations become constraints on reconstructed values, exactly as stated. Note, uncharged: e is also the level-1 B-Hermite pivot (i<⌈1/5⌉), so e is booked by two reviewed presentations; that pre-existing overlap only strengthens the no-additive-saving conclusion. No source, cap or implementation change follows. CONFIRMED.

## 4. Finite DVR arc interface (item 4)

Interface fit against the promoted classification: own C12 multiplies R_t=p⁵+g³p²+(t+3)gp²+tp³−(t+3)p with products truncated at receiver degree 3 (never R³ or R⁵) and finds in A₀=R_t³+αR_t and B₀=R_t⁵+βR_t³+γR_t exactly

```
a01 = -alpha (t+3)      a12 = alpha (t+3)      a03 = -(t+3)^3 + alpha t
e   = -gamma (t+3)      [g]B0 = 0 = d at k=0    no constants
```

The report's displayed values are correct; it omits a12, which equals −a01 on every centre. Logic, replayed: a DVR O⊇Q is a domain; the guarded rows are polynomial in k and the coefficients, so they hold in O; the certificates give k²a01=k³h1=k⁴h2=0 with k≠0, hence a01=h1=h2=0 in O; at the special point this reads α(t+3)=0, e=−γ(t+3)=0 and a12²=3k·a03. The special point satisfies every unguarded k=0 row without the inverse, so 14f classifies it over the residue field; k⁻¹ need not lie in O. If the a03 residue is nonzero, a03 is a unit and 2·ord(a12)=ord(k), so ord(k) is even. C13 confirms a03 vanishes on the classified centre iff t=−3 and α=0 (a03|α=0=−(t+3)³, a03|t=−3=−3α), where only ord(k)+ord(a03)=2·ord(a12) survives; the report keeps that locus open. C11 confirms the literal even-ramified low-row solution k=s², a12=s, a03=1/3, e=5s³/9, a01=b21=b12=0. Three limits are stated correctly: no guarded point is shown to degenerate to k=0, ramified arcs are not excluded (the low rows admit ord(k)=2), and the saturated low fibre at k=0 contains a12²=0, so the boundary may be nonreduced. Stale label: the report calls the classification PROVISIONAL and consumes the sealed `129947ee…` copy; the field classification (§§1–3 of 14f) is now PROMOTED, and only that part is used here, not the order-two obstruction. CONFIRMED with that relabel.

## 5. Scope, controls, stop (item 5)

Own `gate_controls.py` (SHA `2ce673dd…`, stdlib, zero Assert nodes, ordered named gates) runs a 17-name exact polynomial ring with degree-capped products. Runner: eight runs, normal and −O, positive witnesses byte-identical (`cc2f5336…`), and each mutation recorded by its FIRST failing gate: wrong sign in the k⁴ certificate → `cert-k4-h2`, omitted [A₁,B₃] → `A1B3-terms` (the constant row still passes, so the branch is reached), false unguarded equivalence → its own gate after all prior gates pass. Total 0.9 s wall, 23 MB, under the 30 s/25 CPU/512 MiB caps; `replay.json` and `input_pins.txt` are in the box. The frozen `check.py` was run once read-only in plain mode: stdout hashes to `37fc6434…`, matching the charged witness; its three mutation branches are independently reachable by the same argument. The report's stop clauses are all present and accurate: low-row equivalence and conditional valuation restrictions only; no full-ideal unit, properness, generic fibre, runtime, source-coverage or JC2 claim; the unguarded point is a low-row countercontrol, not a full-source point; no code-generation or baseline authority.

Typed gaps, uncharged: **GAP-TRANSACTION** (root `c004f483…` is not among the frozen inputs); **GAP-HISTORY** (the "no earlier explicit formula" checksum is unverifiable from the frozen set). No exit-price claim is made, so no charge basis is declared. **STOP:** review only; no promotion authority beyond the five verdicts above.

<!-- BODY-END -->
