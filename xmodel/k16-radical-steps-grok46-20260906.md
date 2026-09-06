# K16 two-step radical certificate at finite t: u³ ∈ J+(r) is not t-uniform

Lane `k16-radical-steps-grok46-20260906`, 2026-09-06. Basis `cf45b6b4`.
Drivers/transcripts: `box/k16-radical-20260906/`. Singular 4.3.2, exact
`Q(d)/(3d²-N)` and `GF(p)` at declared roots. No fleet, ledger, `jc2-lean`,
or uncharged `ideation-*`. FALLACY-v2 applies; no exit-price assertion, so no
`charge_basis` line.

```text
REQUESTED  at t=3,4,5 (and 6 if it fits), from frozen controls_t{3,4,5}_raw.sing
           (identity map on (c_i,b); minpoly 3d²-N): (1) u²+4T₂ ∈ J_t;
           (2) min e1,e2 with u^{e1}∈J_t+(r), r^{e2}∈J_t+(u), cofactor weights;
           (3) tabulate; t-uniform pattern for a universal-recursion proof?;
           (4) VERDICT: pattern found / exponents grow. L-tail first via unit Toeplitz.
ANSWER     (1) YES as a polynomial identity, all t checked: u²+4T₂+24 E₂=0, so
               u²+4T₂=-24 E₂ ∈ J_t with constant cofactor -24 (weight 0).
           (2) e1(t)=3,3,3,4 and e2(t)=1,2,2,2 for t=3,4,5,6. Original-generator
               lift cofactors are weighted-homogeneous of the expected degree
               wt(target)-wt(generator); those degrees grow linearly in t.
           (3) No constant-exponent non-vacuous pattern. The sol56/astra pair
               u³∈J+(r), r²∈J+(u) holds at t=3,4,5 (mostly socle-forced) and
               FAILS at t=6: u³∉J+(r) is a nonzero normal form of weight 36≤39.
           (4) EXPONENTS GROW. e1 rises from 3 to 4 at t=6. A symbolic proof
               cannot target constant e1=3. The only t-uniform identity seen is (1).
CUSTODY    5/5 charged hashes OK (awk pairing of charged_input_<i>_sha256=_basename=
           into box/k16-radical-20260906/manifest.sha256; sha256sum -c). Frozen
           t=3,4,5 rows/B/η/target reproduced by imap. t=6 has no frozen exact
           file; it is the same UF/Theorem-H emitter, modular only.
NOTIFY     not warranted (no new index, no exit claim).
```

## 1. Custody and ring map

Receipt `xmodel/k16-radical-steps-grok46-20260906.run.v2` was parsed with `awk -F=`;
`sha256sum -c` on the resulting manifest returned **5/5 OK** before any
mathematical read. Inputs were the frozen copies in `/tmp/jc2-lane.ltoqmP/inputs`.
Charged: astra #3 / sol56 Q3.A (same two-step certificate), the tacnode report
(identity `Lpivot²=-4T₂-24E₂`), the universal-series (UF) recursion, FALLACY-v2.

**Declared map.** Big ring `r=(K,(x,Y,c1..c_{t-1},b,B,eta,w1..w_{2t+1}),dp)` with
`K=Q(d)` and `minpoly=3*d^2-N` (`N=t+1`), or `K=GF(p)` at a printed root of
`3d²=N`. `y=(d+N)/(2(2t+1))`, `L=x²C/y-b`, `P=xW-b²/4`. Theorem H eliminates
`(w_{2t},…,w1,B)` from rows `x^{4N-1}..x^{2N+1}` (unit scalar pivots). Small ring

```text
rsmall=(K,(c1..c_{t-1},b),wp(1,2,…,t-1,N)),   J_t=(E_2..E_{2t}),
u=4η+3b·c_{t-1}/y   (wt 2t),   r=Bη (wt 4t+1),   T₂=3b²w₃+18 B w₂-10η² (wt 4t).
```

Frozen `box/k16xempty-20260905/controls_t{3,4,5}_raw.sing` is imported as `rfro`
(identifiers renamed only) and compared by `imap` on `(c_i,b)`: **rows, B, η,
target equal** at t=3,4,5 over `Q(d)`. Matching names were not used as evidence.
The tilde in the charged `L̃` is a label; `u,r,T₂` here are polynomials, not
derivatives.

## 2. L-tail Toeplitz (unreduced high rows)

On the unreduced (UF) (P-jets free), `D=∂_Y Q_P(x,L)`, `deg_x D=3N`, and
`d_{3N}=[x^{3N}]D=(3/(4y³))(1-4p)` lies in the coefficient field and is nonzero
(`p=1/(4(2d+1))≠1/4`). For `2≤m≤N-1` and `k` in `{3N+2,…,4N-1}`,

```text
y · ∂[x^k]UF / ∂c_{N-m}  =  -[x^{k-m}] D     (= ∂ row_k / ∂ l_m,  l_m=c_{N-m}/y).
```

Ordering rows `F_{4N-1},…,F_{3N+2}` and columns `l_{N-1},…,l_2` from the tail
gives a triangular block with constant diagonal `-d_{3N}` and
`det=(-d_{3N})^{N-2}`. Checked at t=3,4,5,6 (`TOEPLITZ_* =1`; `N-2=2,3,4,5`).
The frozen `J_t` is the complementary Theorem-H chart (P-jets spent, L-jets
remaining); memberships below are in that frozen presentation.

## 3. Task (1): `u²+4T₂ ∈ J_t`

The tacnode identity is an equality of polynomials, not a Gröbner membership:

```text
u² + 4 T₂ + 24 E₂  =  0     in  K[c,b]
```

(`IDENTITY_u2_plus_4T2_plus_24E2=1`). Hence `u²+4T₂=-24 E₂∈J_t`. Lift against
the original rows: cofactor of `E₂` is the constant `-24` (weight 0); all other
row cofactors are 0 (`M0_1_equals_-24=1`, `COF0_LIFT_OK=1`). Verified exact at
t=3,4,5 (frozen custody) and as the same polynomial identity at reconstructed
t=6. `T₂,u,r` themselves lie outside `J_t` at every t checked.

## 4. Task (2): min exponents and cofactors

`reduce` against `std(J)`, `std(J+(r))`, `std(J+(u))` in the weighted ring;
socle = max weighted degree of `kbase`. Vacuous means `wt(power)>socle` (any
homogeneous of weight `>socle` lies in a 0-dimensional homogeneous ideal).
Negative controls: `u^{e1-1}∉J+(r)` and `r^{e2-1}∉J+(u)` when `e>1`. Cofactors
are `lift` against the **original** generators `(E_2..E_{2t}, r)` and
`(E_2..E_{2t}, u)`; `I·M=f` was checked (`LIFT_OK=1`) except t=4 original-lift
over `Q(d)` (product too heavy; exact membership by `reduce` plus `division`
remainder 0 against the GB, original cofactors from `p=31991`).

| t | field | socle | vdim J | e1 | wt(u^{e1}) | vac? | e2 | wt(r^{e2}) | vac? |
|--:|---|--:|--:|--:|--:|---|--:|--:|---|
| 3 | `Q(d)`, `3d²=4`, exact | 14 | 66 | 3 | 18 | Y | 1 | 13 | N |
| 4 | `Q(d)`, `3d²=5`, exact | 21 | 338 | 3 | 24 | Y | 2 | 34 | Y |
| 5 | identity exact; GB `p=31991,d=6434` and `p=10007,d=2641` | 30 | 1709 | 3 | 30 | N (=socle) | 2 | 42 | Y |
| 6 | reconstructed; `p=32003,d=13969` and `p=32009,d=1756` | 39 | 8621 | 4 | 48 | Y | 2 | 50 | Y |

vdim `J+(r)` / `J+(u)`: t=3: 64/41; t=4: 327/215; t=5: 1651/1099; t=6: 8284/5557.
t=5 two primes agree on `(e1,e2,socle,vdim)` and on all COF1 weights/term-counts;
COF2 term-counts differ by 3 (lift cofactors are not unique; **weights agree**).

**Non-vacuous normal forms (FALLACY-v2 raw remainder).** t=6, both primes:
`reduce(u³, J+(r))` has 307 terms, weighted degree 36 `≤` socle 39, not zero;
`reduce(r, J+(u))` has 66 terms, degree 25, not zero. t=3,4,5: `u²∉J+(r)`
(weights 12,16,20 all `≤` socle); `r∉J+(u)` at t=4,5 (weights 17,21 `≤` socle);
at t=3, `r∈J+(u)` is the one non-vacuous ideal-level implication.

**Original-generator cofactor weights** for `u^{e1}=∑ a_i E_{i+1}+λ r`
(always `wt(a_i)=2t·e1-wt(E_{i+1})`, `wt(λ)=2t·e1-(4t+1)`):

```text
t  e1  a_1..a_{2t-1} weights     λ wt  λ terms   max |a_i| terms
3   3  6,7,8,9,10                 5     3         12     exact Q(d)
4   3  8,9,10,11,12,13,14         7    10         40     p=31991; exact membership
5   3  10..18                     9    21        128     two primes
6   4  24..34                    23   417       1753     two primes
```

For `r^{e2}=∑ b_i E_{i+1}+μ u`, `wt(μ)=(4t+1)e2-2t`: t=3 e2=1, `μ` wt 7 (6 terms);
t=4,5,6 with e2=2, `μ` wt 26,32,38 (171, 714, 2695 terms). All grow with t.

## 5. Task (3): is there a t-uniform pattern?

The charged proposals (sol56 Q3.A; astra #3) ask for **constant** exponents
`u³∈J_t+(r)` and `r²∈J_t+(u)`, cofactors of bounded weight, as a certificate
of `√(J+(T₂))=√(J+(u))=√(J+(r))` and hence “`T₂=0` on `V(J_t)` iff (R)”.

What is actually uniform:

- **Identity (1)** `u²+4T₂+24E₂=0`, cofactor `-24`, every t. Already Theorem 5.1
  of the charged tacnode report; re-checked on the frozen bases.
- Toeplitz unit `d_{3N}` and triangular det `(-d_{3N})^{N-2}`, every t checked.

What is **not** uniform, and is mostly socle-forced:

- `e1=3` at t=3,4 is implied by `u³∈J_t` itself (min power of `u` in `J` is 3,
  weight `>socle`). It is not a relation with `r`.
- `e2=2` at t=4,5,6 is implied by `wt(r²)>socle`. The only non-vacuous
  `r∈J+(u)` is t=3 (weight 13`≤`14), matching the charged tacnode table.
- The one genuine `u³∈J+(r)` not already in `J` is t=5, at the socle degree 30
  (`u³∉J`, `u²∉J+(r)`). It does **not** persist: at t=6, `u³∉J+(r)`
  non-vacuously (307-term remainder, two split primes).
- Cofactor weights are the tautological homogeneous degrees `wt(f)-wt(g)`,
  linear in t, not bounded independently of t.

A universal-recursion proof can target identity (1) (already written). It
cannot target constant `e1=3`. An `e1(t)` that tracks the first weight above
the socle is not a syzygy.

## 6. Task (4): VERDICT

**Exponents grow.** `e1(3)=e1(4)=e1(5)=3` and `e1(6)=4`; `e2(3)=1` and
`e2(t)=2` for `t=4,5,6`. The conjectured uniform identities of sol56 Q3.A /
astra #3,

```text
u³ ∈ J_t+(r),     r² ∈ J_t+(u)        for all terminal t≥3
```

are not a t-uniform non-vacuous certificate: `u³∈J+(r)` is false at t=6 as a
nonzero normal form of weight `≤` socle (two primes; reconstructed `J_6`, not
frozen-custody). `r²∈J+(u)` is weight-vacuous for all t≥4. Finite-t identities
are not a theorem (FALLACY-v2). `(R)` and the tacnode statement remain OPEN.
No new index; theorem (T) is not promoted.

t=6 is optional evidence: same emitter that reproduced frozen t=3,4,5, no
`controls_t6_raw.sing` to imap. The t=6 nonmembership is therefore a modular
obstruction to the *pattern*, not a char-0 theorem. Exact `std(J_5)` over `Q(d)`
was not completed (charged tacnode already left it unfinished at 32 min); t=5
memberships are two-prime modular, with exact confirmation of (1) and frozen
custody only.

## 7. FALLACY-v2

- **Finite-t / floor.** Min powers are search minima. Memberships with
  `wt>socle` are labelled vacuous and are not structure. t=5 `u³` sits *at* the
  socle, not above it; t=6 `u³` remainder degree 36 is below the socle.
- **Modular → char 0.** Nothing modular is promoted. Two primes at t=5 and t=6;
  t=3,4 exact over `Q(d)` for `(e1,e2)` and (1). t=6 `u³∉J+(r)` is a nonzero
  remainder, not a reconstructed char-0 cofactor.
- **`sat()`.** Unused. Membership is `reduce` against a reduced standard basis;
  cofactors are `lift`/`division`.
- **Raw remainder.** Branch on zero: printed `terms`, `deg`, `zero=` for the t=6
  `u³` and `r` remainders; zero remainders for the claimed memberships.
- **Variable/ring map.** §1: generator order, weights, `minpoly` or `(p,droot)`,
  identity `imap` image check. t=6 reconstruction is declared, not frozen.
- **Prime label.** `u,r,T₂,L̃` are labels; `θ=x d/dx` and `∂_Y` are derivatives.
- Flag/place/series, exit sets, poles, 8.5, arrival index: not touched.

OPENS RETAINED: `OPEN[K16-UF-DEGENERATE-TACNODE]` (charged tacnode), sharpened
only as “the bounded pair `(u³,r²)` is not a uniform certificate”. QUANTITY:
indices with non-vacuous `u³∈J+(r)` among {3,4,5,6} = 1 (t=5); indices with
non-vacuous `u³∉J+(r)` = 1 (t=6, modular); indices with non-vacuous `r∈J+(u)` = 1
(t=3, exact).

## 8. Computation record

```text
box/k16-radical-20260906/
  manifest.sha256                         5/5 OK
  emit_radical.py                         UF replay + Toeplitz + lift
  radical_t{3,4}.sing/.out                exact Q(d); t=4 original-lift skipped
  radical_t4_div.sing/.out                exact division rem 0; GB cofactors
  radical_t4_p31991_d4933.sing/.out       original cofactors
  radical_t5_identity.sing/.out           exact (1)+frozen custody, then quit
  radical_t5_p{31991,10007}_d*.sing/.out  two-prime (e1,e2,lift)
  radical_t6_p{32003,32009}_d*.sing/.out  two-prime; NF of u³,r printed at 32009
```

Local `--cpus=1`. Driver dir 760 KiB. No artefact tree.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11514`.
- Body SHA-256:
  `3db1fa0776de82d040f842e92480efd594a28f165f33fd664c5e3b2f26b5261a`.
- Frozen basis: `cf45b6b4f80196d8bc2236c603ffc62cb0eddaa7`.
