# Hostile cross-review: `R30-SLICE-DESC` rows 31–34 through class row 34

Reviewer: Claude Fable 5 (Anthropic), different-model hostile referee
(producer lane is Sol Ultra)  
Pinned model ID: `claude-fable-5` (Claude Code CLI harness)  
Host: Python 3.9.6, Darwin 23.6.0  
Review date: 2026-08-28 (charged 2026-08-27 artifact)  
Charged source, byte-verified before any reading:

```text
e5a2c968e516a40509d136cfd57613c8be84e50041444ce8146916b976bdf24c
  xmodel/ggv-quarter-root-r30-slice-descendant-r0-sol-ultra-20260827.md
```

No raw determinant row, polynomial-`G` lift, endpoint decision, branch-P
family exclusion, Keller pair, landing, or JC2 theorem is decided by this
review.

## 0. Headline verdict

**All six charged atoms are CONFIRMED.  No REPAIRED, GAP, or REFUTED atom.
Every load-bearing identity was rederived independently, several by a
strictly stronger method than the producer's replay; the two receiver
nondegeneracy facts that the producer supported only by truncation
stability are proved exactly here by hand, upgrading the odd-row equation
content from replay-supported to unconditional.**

| # | Charged atom | Verdict |
|--:|---|---|
| 1 | Row-31 gauge `H^7p^-31`, quotient basis `[X],[X^2],[X^4]`, equations `6b1+b5=0`, `13b2+3b6=0`, `b4=0`, split surjectivity over the full nonreduced parent base | **CONFIRMED** |
| 2 | Every coefficient in gauged `q_10` (5.2)–(5.3), residue vector (5.6), ideal `(u^2v,u^5)`, containment in `(uv,u^4)` | **CONFIRMED** |
| 3 | Row-33 gauge `H^8p^-33`, both receiver-coordinate maps (6.2), affine equations (6.3), unit-pivot cancellation (6.4) with no localization at `u` | **CONFIRMED** |
| 4 | Every coefficient and cancellation in gauged `q_12` (7.2)–(7.3), all finite and infinity residues (7.5)–(7.6), ideal `(v^2,u^3v,u^6)`, "adds exactly `v^2`" (7.8) | **CONFIRMED** |
| 5 | Ring isomorphism (8.2), 24 free newest slots, length-five base `Q[u,v]/(uv,u^4,v^2)` with basis `1,u,u^2,u^3,v`, radical `(u,v)`, square-zero nonzero `v` tangent, socle `<u^3,v>` | **CONFIRMED** |
| 6 | Firewalls: licensed de Rham class equations on one symbolic slice only; not raw rows, not a polynomial `G`, not endpoint, not branch-P family exclusion, no Keller pair, no JC2 result | **CONFIRMED** |

## 1. Custody

Charged hash recomputed on live bytes; match exact.  All eight dependency
files named in the report's §1 were re-hashed before reading; every one
matches the producer's pin:

```text
e487bd6f54be9762dd551abe7bd25cabed4b9daa053b57a9a424441ef269848e
  xmodel/ggv-quarter-root-r28-nonlinear-class-test-r0-sol-ultra-20260827.md
ccf1d9778a50351c5ee0a8b919b7e917e1baa036e73062c7a64c45bedf9ba490
  xmodel/ggv-quarter-root-r30-symbolic-prefix-crossreview-grok46-20260827.md
6fac1961e85730b2909ce05ecbdee19c2b5b1f61831844cd409d97e88b4bff29
  xmodel/ggv-quarter-root-r30-symbolic-prefix-crossreview-grok46-prompt.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
60670d0a7066ab0a1d1f72ad05a0ff44a858fa39dbf4d18fd225913d26b6d114
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md
5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55
  xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
```

Only these files and the charged report were read.  No mutable canonical
ledger was reread, no path under `jc2-lean` was listed, opened, searched,
built, statused, or modified, no AWS resource was contacted, no heavy local
computation ran, and no unrelated ideation submission was opened.  Local
work is exact `fractions.Fraction` desk arithmetic in three staged `/tmp`
scripts plus a verbatim rerun of the producer's embedded replay.  This file
is the only write.

Dependency-verdict accuracy: the producer's §0 quotation of the Grok46
review is faithful.  That review's §0 table marks the slice, the row-30
gauge, the residue vector, and the ideal `(uv,u^4)` **CONFIRMED**, its only
GAP being the non-load-bearing `F_7` rank-three citation; the rollback
trigger therefore did not fire, exactly as the descendant records.  The R8
crossreview's summary line "(3.7)/(0.2) transported coefficient is
`p^(-m_0)q_(b+4k)` — CONFIRMED — the real repair" endorses precisely the
fixed-receiver gauge the descendant uses; none of its four repairs touches
`nabla_m`, the dimension law, or the `H^k` gauge identity (3.6).

## 2. Licensing checks against the frozen sources

**Slot windows (2.1).**  Parsed the literal `chart_image` fields of the 141
frozen `F` slots in `RAW_INPUT.json`.  The positive-weight `X`-degree sets
are exactly

```text
n=8: {0..8}   n=9: {1..7}   n=10: {1..6}   n=11: {1..5}   n=12: {2..4}
```

with dimensions `9,7,6,5,3` — byte-level agreement with (2.1), including
both lower bounds `a>=1` and `a>=2`.  `F_13` (2 slots) and `F_14` (1 slot)
exist in the window but are correctly not adjoined: slot `F_n` enters at
row `n+22`, i.e. at rows 35–36, beyond scope; my brute-force composition
enumeration (Section 4) confirms neither can occur in any `q_n`, `n<=12`.

**Rank/receiver table (2.2).**  The licensed table is in the linear-vacuity
review (`5beb5550…`), P-licensed row: rows 23–34 read
`3,4,3,4,3,0,3,0,3,0,3,0`, so rows 30–34 are `0,3,0,3,0` — exact match.
Receivers: R8 (3.3) gives `dim V_m=r-1+k_m`, `k_m=1` iff `4 | m·e_i`; here
`H=A^2` (all `e_i=2`, `r=4`), so `k_m=1` iff `m` even, giving `4,3,4,3,4` —
exact match.  I additionally rederived these dimensions from scratch: `V_m`
for odd `m` is `H^1` of the rank-one regular-singular system `A^{-m/2}` on
`A^1` minus the four roots (monodromy `-1` at each root, `H^0=H^2=0`, so
`dim = -chi = 3`); for even gauged rows the receiver is ordinary
`H^1_dR(A^1 - {4 roots})`, dimension `5-1=4` (five `P^1` punctures, sum of
residues zero).  Independent agreement.

**Master formula and typing.**  The parent's (2.1)/(2.2) give
`q_n = (2/(n+2))[t^n]F^{(n+2)/8}` with `F=H^2+sum F_i t^i`, `p^4=H`; the
binomial expansion yields exactly the descendant's (3.1) with
`p^{n+2-8d}` powers.  R8 (3.1)–(3.7) licenses the class gate
`[p^{-m}q_{m-22}dX]=0` in `V_m=coker(nabla_m)`,
`nabla_m(f)=(f'+(m/4)(H'/H)f)dX`, and the gauge
`nabla_{m_0}(H^k f)=H^k nabla_{m_0+4k}(f)`.  With `H=A^2` this is
`nabla_j = d+(j/2)(B/A)dX`, the descendant's (3.3), **plus** sign.

## 3. Direct attack on the odd-row quotient typing (charge requirement)

This is the point where a wrong convention would silently corrupt (4.3)
and (6.3), so I attacked it three ways.

**(a) Sign of the connection.**  With the licensed sign, for any `d>=0`,

```text
nabla_j(X^d A) = ((d+4+2j) X^{d+3} - d X^{d-1}) dX,
```

a literal image element.  Had the receiver been the `p^{-j}`-twist
(`nabla = d-(j/2)(B/A)dX`), the recursion would be
`(d+4-2j)[X^{d+3}]=d[X^{d-1}]`, which for `j=3` at `d=2` forces `[X]=0`
and destroys (4.3).  The plus sign is pinned by R8 (3.1) (`+ (m/4)H'/H`),
by the parent's verified identity `d(H^7f)=H^7 nabla_28(f)`, and by R8
(3.2) `d(p^m f)=p^m nabla_m(f)`.  The producer used the correct receiver.

**(b) Gauge bookkeeping.**  `p^2=eps A` gives `H^7=A^14=(p^2)^14=p^28`
with `eps^14=1`, so `H^7p^-31=p^-3` with no `eps`; likewise
`H^8=p^32`, `H^8p^-33=p^-1`.  On even rows `A^16 p^-32=eps^-16=1` and
`A^17p^-34=eps^-17=eps`; each `p^{14-8d}` in `q_12` carries
`(eps)^{7-4d}=eps`, so `eps·q_12` is componentwise `eps`-free.  All four
gauges (3.2)/(3.4) verified; the row-31/33 gauged objects are exactly
`P_9/4` and `A^2P_11/4+(5u/8)BP_9` (from `c(11,2)=5/64` and
`F_2=4uA^2B`).  R8 (3.6) with `(m_0,k)=(3,7)` and `(1,8)` makes
multiplication by `H^7`, `H^8` a quotient isomorphism `V_31≅V_3`,
`V_33≅V_1`, so "in `V_3`"/"in `V_1`" is the licensed least-character
typing, not a shifted operator with a dropped `H`-power.

**(c) Receiver nondegeneracy — proved, not replayed.**  The producer's
replay derives the quotient rows from a single denominator level `s=M`
with an `M=4,6` stability check; that method is a priori one-sided (too
small an image can manufacture spurious equations).  I close this exactly.

*Lemma.*  For `j` odd and `A=X^4-1`: if
`(l_0+l_1X+l_2X^2)dX = nabla_j(g)` with `g in Q[X,1/A]`, then
`l_0=l_1=l_2=0`.

*Proof.*  Write `g=h/A^s`, `s>=0` minimal.  Then
`nabla_j(g)=[h'A+(j/2-s)A'h]A^{-s-1}dX`.  If `s>=1`, clearing gives
`A | (j/2-s)A'h`; `j/2-s != 0` (`j` odd) and `gcd(A,A')=1` (`A`
squarefree) force `A|h`, contradicting minimality.  So `s=0`, and
`A·(l_0+l_1X+l_2X^2)=h'A+(j/2)A'h` forces `A|h`; writing `h=Ak` gives
`l_0+l_1X+l_2X^2=(1+j/2)A'k+Ak'`, whose leading coefficient is
`(4+2j+deg k)·lc(k) != 0`, so the right side has degree `deg k+3 >= 3`
unless `k=0`.  Hence `k=h=0` and `l=0`.  ∎

Consequently `[1],[X],[X^2]` are `Q`-independent in both `V_1` and `V_3`;
since they are part of a `Q`-basis of a `Q`-vector space, they stay free
after base change to any `Q`-algebra, including the nonreduced parent ring
(coker commutes with the flat extension).  Combined with the explicit
image elements in (a), the recursions

```text
V_3 (j=3): (d+10)[X^{d+3}]=d[X^{d-1}]:
  [X^3]=[X^7]=0, [X^4]=[1]/11, [X^5]=[X]/6, [X^6]=(3/13)[X^2];
V_1 (j=1): (d+6)[X^{d+3}]=d[X^{d-1}]:
  [X^3]=[X^7]=[X^11]=0, [X^4]=[1]/7, [X^5]=[X]/4, [X^6]=[X^2]/3,
  [X^8]=5[1]/77, [X^9]=[X]/8, [X^10]=7[X^2]/39,
  [X^12]=3[1]/77, [X^13]=5[X]/64
```

are now *exact* statements in the true localized quotients, both
directions.  (4.2) is the `j=3` list verbatim.  A staged independent
script (different code and basis from the producer's; **all** denominator
levels `s=0..T-1` in the image, windows `(T,N)=(6,60)` and `(8,80)`)
reproduces every relation and the rank-3 independence.

## 4. Atom-by-atom rederivations

### Atom 1 — row 31 (CONFIRMED)

Brute-force enumeration of all ordered compositions of `9` on the slice
(no hand survivor list; `F_13,F_14` markers included) returns
`S_(9,d)=0` for every `d>=2` — parity: even parts cannot sum to 9, and
any odd part uses a dead slot — so `q_9=(1/4)p^3P_9`, `R_9=0`, and the
gauged class is `[P_9/4]` in `V_3`.  By the `V_3` ladder,

```text
[P_9/4] = (1/4)[(b_1+b_5/6)[X] + (b_2+3b_6/13)[X^2] + b_4[X^4]],
```

and `[X^4]=(1/11)[1] != 0`, so vanishing is exactly
`6b_1+b_5=0`, `13b_2+3b_6=0`, `b_4=0` — (4.3) verbatim, with basis
`[X],[X^2],[X^4]` legitimate.  The `3x7` matrix has the `3x3` minor
`diag(1,3,1)` on columns `(b_5,b_6,b_4)` with determinant `3 in Q^x`, so
the map is split surjective over **every** `Q`-algebra, in particular over
the full nonreduced parent base `Q[u,v]/(uv,u^4)` tensored with the slot
ring — no generic-point argument used, no `(u,v)`-equation added.  Free
coordinates `b_1,b_2,b_3,b_7` (7−3=4).  Rank 3 = licensed table entry.

### Atom 2 — row 32 / `q_10` (CONFIRMED)

Every coefficient re-obtained twice: (i) hand Pochhammer,
`c(10,d)=(1/6)binom(3/2,d) = 1/4, 1/16, -1/96, 1/256, -1/512`; (ii) a full
multivariate polynomial expansion over `Q` in `(X,u,v)` with linear slot
markers, computing `sum_d c(10,d)A^{20-4d}S_(10,d)` from brute-force
compositions and matching it to the cleared right side of (5.3)
**as an exact polynomial identity** (not coefficient bookkeeping):

```text
q_10 = A^2P_10/4 + (u/2)BP_8 - (u^2v/4)B^2/A^2 - (u^5/2)B^5/A^4.
```

The `u^2v` coefficient is the cancellation `1/4-1/2=-1/4` between
`S_(10,2)` and `3F_2^2F_6`; the `u^5` coefficient is `-1/2+2-2=-1/2`
across `d=3,4,5`.  Survivor list (5.1) confirmed by enumeration.  The two
polynomial terms are exact, so the class is (5.4).  Residues were computed
by the **derivative formula** `Res_a = (1/(l-1)!) d^{l-1}[f·(X-a)^l]|_a`
with exact Gaussian-rational arithmetic separately at all four roots (not
the producer's series method, no scaling assumption):
`Res_a(B^2/A^2 dX)=3a^3`, `Res_a(B^5/A^4 dX)=256`, and
`Res_inf(B^5/A^4 dX)=-1024` from the `1/X` expansion (only exponent
`3k-4l=-1` case; sum over `P^1` is `4·256-1024=0`).  Vector (5.6) verbatim,
including `+512u^5` at infinity.  Ideal: `(r_1-r_2)/2` and `(r_1+r_2)/2`
give `u^2v` and `u^5` up to units, and every entry lies in `(u^2v,u^5)`;
the two class directions `(3a^3)_a` and `(256)_a` are linearly
independent, so the ideal does not collapse to a single combination.
`u^2v=u·(uv)`, `u^5=u·u^4`, hence `J_32 ⊂ I_30` in the full nonreduced
quotient — row 32 cuts nothing.  Both replays agree.

### Atom 3 — row 33 (CONFIRMED)

`S_(11,2)=2F_2P_9` and `S_(11,d)=0` for `d>=3` confirmed by enumeration;
`c(11,2)=5/64` by hand; `p^{-1}q_11 = A^2P_11/4 + (5u/8)BP_9` re-verified
by full polynomial expansion after clearing `A^2`.  The nonlinear carry
`(5u/8)BP_9` is correctly retained: `V_1` classes of polynomials need not
vanish.  From the exact `V_1` ladder,

```text
[A^2 P_11] = (5/8)(d_1+d_5/8)[X] + (20/39)d_2[X^2] + (4/77)d_4[1],
[B P_9]    = (b_2+b_6/2)[X] + (4b_3/3+28b_7/39)[X^2]
             + (4b_1/7+20b_5/77)[1],
```

so in the coordinates rescaled by `(8/5, 39/20, 77/4)` the two maps are
exactly (6.2), including `(8b_2+4b_6)/5`, `(13b_3+7b_7)/5`, and
`11b_1+5b_5`.  Setting `(1/4)(d-part)+(5u/8)(b-part)=0` and clearing gives
(6.3) verbatim.  Pivots `8,2,2 in Q^x`: the solve (6.4) — including
`(14/3)u b_2` after `b_6=-13b_2/3` and `(95/2)u b_1` after `b_5=-6b_1` —
is a split affine cancellation valid over the entire nonreduced base; `u`
appears only in the non-pivot columns, so **no localization at `u` occurs
anywhere**, and the contraction to `Q[u,v]` is unchanged.  Free: `d_3,d_5`.
The producer's `row33` fixture matrix equals my hand-derived joint
`phi`-matrix column for column.  Rank 3 = licensed entry.

### Atom 4 — row 34 / `q_12` (CONFIRMED)

`c(12,d)=(1/7)binom(7/4,d) = 1/4, 3/32, -1/128, 5/2048, -9/8192, 39/65536`
by hand.  Survivor list (7.1) confirmed by enumeration; the parity
argument for odd slots is airtight (`P_9,P_11` need an odd partner; all
other odd slots vanish; `9+9,9+11,11+11 > 12`).  Full expansion of
`sum_d c(12,d)A^{24-4d}S_(12,d)` equals the cleared (7.3) exactly, with
the two load-bearing cancellations independently recomputed:

* `P_8`: `+(3/32)·4 = 3/8` from `2F_4P_8` against
  `-(1/128)·48 = -3/8` from `3F_2^2P_8` — identically zero (my expansion
  asserts no `P_8` marker survives anywhere in `q_12`);
* `u^3v`: `-3/8+5/8=1/4`;  `u^6`: `(-1+15-45+39)/16=1/2`;  `v^2`: `3/32`;
  `uABP_10`: `3/4`.

Residues by the derivative formula at each root:
`Res_a(dX/A)=a/4`, `Res_a(B^3/A^3dX)=6a^2`,
`Res_a(B^6/A^5dX)=(1155/2)a^3`; all three infinity residues vanish
(`1/X` exponents `-4-4t`, `-3-4t`, `-2-4t` never hit `-1`), and each
finite quadruple sums to zero.  Vector (7.6) verbatim, entry by entry,
including the `i`-entries `3iv^2/128-(3/2)u^3v-(1155i/4)u^6`.  The three
class directions `(a)_a`, `(a^2)_a`, `(a^3)_a` are independent, so the
imposed ideal is exactly `J_34=(v^2,u^3v,u^6)`.  Modulo the parent,
`u^3v=u^2(uv)` and `u^6=u^2·u^4` die; `v^2` is not divisible by `uv` or
`u^4` (monomial ideal), so `v^2 notin (uv,u^4)` and (7.8)
`I_30+J_32+J_34=(uv,u^4,v^2)` is exact: **row 34 adds exactly `v^2`.**
The `J_32`/`J_34` generators are slot-free polynomials in `Q[u,v]` before
any reduction, so imposing them over the row-33 ring adds precisely these
ideals.

### Atom 5 — coefficient ring (CONFIRMED)

`I_31` eliminates `b_4,b_5,b_6` and `I_33` eliminates `d_1,d_2,d_4` by
unit-pivot triangular substitution — genuine ring isomorphisms, not
dimension counts.  The base ideal collapses:
`(uv,u^4,u^2v,u^5,v^2,u^3v,u^6)=(uv,u^4,v^2)`.  Hence (8.2) is an actual
isomorphism onto

```text
Q[a_0..a_8, b_1,b_2,b_3,b_7, c_1..c_6, d_3,d_5, e_2,e_3,e_4, u,v]
  /(uv, u^4, v^2),
```

with `9+4+6+2+3 = 24` free newest slots — exact count.  Base algebra:
monomials outside the ideal are `1,u,u^2,u^3,v` — length five;
`rad=(u,v)` (both nilpotent, residue field `Q`);
`m^2=(u^2)`, `m^3=(u^3)`, `m^4=0`; annihilator of `m` is spanned by
`u^3` and `v` (a general element `c_0+c_1u+c_2u^2+c_3u^3+c_4v` killed by
`u` and `v` forces `c_0=c_1=c_2=0`), so socle `= <u^3,v>` — (8.3)
verbatim.  `v notin (uv,u^4,v^2)` (monomial divisibility), so `v` is a
**nonzero** square-zero element; `m/m^2` is spanned by `u,v`, dimension 2.
Since (8.2) is free over `Q[u,v]/(uv,u^4,v^2)`, the contraction of the
total ideal to `Q[u,v]` is exactly `(uv,u^4,v^2)`: rows 31–33 add no
`(u,v)`-equation (row 31 constant-coefficient in `b` only; row 32
contained in `I_30`; row 33 a pivot solve), and the first smaller base
scheme is at row 34, where the reduced `v`-axis dies but `v` survives as a
square-zero tangent — the zero-ring/`u=v=0` over-reading in (0.2) is
correctly avoided.

### Atom 6 — firewalls (CONFIRMED)

Every ideal in (8.1) is an ideal of de Rham class coordinates on the one
frozen symbolic slice; the report claims nothing else.  Specifically
checked: class exactness is asserted only as necessary (matching R7R1's
one-directional `w_{n+22}'=-(n+2)q_n/16` licensing); `qbar_10`, `qbar_12`
are explicitly not raw `D_32`, `D_34` and the dropped polynomial exact
terms are correctly said to remain in the raw coefficients; the row-31/33
surjectivity is not converted into raw-row solvability or `G`-uniqueness;
the support collapse (8.3) is confined to the two-parameter slice and no
branch-P family exclusion or endpoint decision is drawn; no Keller-pair
statement appears anywhere in the file; the descendant self-reports as
unreviewed and non-promotable alone.  Nothing in the mathematics smuggles
a wider claim.  My session likewise touched no AWS, no `jc2-lean`, no
canonical ledger, and no unrelated submission.

## 5. Replays and staged scripts

Independent scripts (staged, not committed), exact `Fraction` arithmetic
only:

```text
45f5405ac47a72e42666c8f2a3dbf61d95ae16ea24711663e85b66ee8b7dbcc4
  /tmp/fable5_r30desc/indep_check.py
    brute-force compositions; full (X,u,v)+slot-marker expansions of
    q_9,q_10,p^-1 q_11,eps q_12; derivative-formula residues at all four
    roots over Q(i); infinity residues; F_13/F_14 leak guard.
    Output ends: ALL INDEPENDENT CHECKS PASS
efe94da8652c4faf447162cab1db1f190f91c46d822e2fe8fb94c37208675887
  /tmp/fable5_r30desc/vj_quotient.py
    all-level image V_1/V_3 quotients at windows (6,60) and (8,80);
    ladder relations and rank-3 independence.
    Output ends: VJ QUOTIENT CHECKS PASS
```

The producer's §9 replay was rerun verbatim: output is byte-identical to
the report's §9 block (`diff` exit 0; output hash
`53c34e1675e7f6d27fb5e59d4584ced7b1b4f19ae0f082e7685f81c577e4e909`).

Method note (no verdict impact): the producer's `quotient_rows` uses a
single denominator level `s=M` and infers exactness of the quotient from
`M=4,6` stability; that inference is one-sided in principle.  The Section 3
lemma plus explicit image recursions now prove the same quotient data
exactly, so successors may cite the odd-row equations as proved rather
than truncation-stable.  A second minor observation: the "reviewed
licensed new-slot table" (2.2) lives in a hostile-review artifact
(`5beb5550…`) rather than a producer report; its rows 30–34 entries are in
any case independently reproved here (even rows rank 0 universally, odd
rows rank exactly 3).

## 6. Promotion recommendation

**PROMOTE**, at desk-class slice scope, as now carrying an independent
different-model review leg (Sol Ultra producer, Fable 5 reviewer),
conditional only on the already twice-confirmed parent ideal
`I_30=(uv,u^4)`:

1. Rows 31/33: the licensed odd-slot class maps are split surjective onto
   their three-dimensional receivers with the exact equations (4.3)/(6.3)
   and unit-pivot solves (6.4); no `(u,v)`-equation is added at rows
   31–33.
2. Row 32: gauged class `-(u^2v/4)B^2/A^2-(u^5/2)B^5/A^4`, residue vector
   (5.6), ideal `(u^2v,u^5) ⊂ (uv,u^4)` — no new cut in the full
   nonreduced quotient.
3. Row 34: gauged class (7.4), residue vector (7.6), ideal
   `(v^2,u^3v,u^6)`, adding exactly `v^2`; through row 34 the descendant
   is the scheme (8.2) with 24 free newest slots over the length-five
   local base `Q[u,v]/(uv,u^4,v^2)`, basis `1,u,u^2,u^3,v`, radical
   `(u,v)`, socle `<u^3,v>`, and `v` a nonzero square-zero tangent.

**DO NOT PROMOTE**: any raw determinant statement `D_23..D_34`; any
polynomial-`G` construction or window descent; any endpoint decision; any
branch-P family exclusion or generic-prefix theorem beyond the
two-parameter slice; any Keller pair; any landing; any JC2 conclusion.
The class equations remain necessary-only for polynomial solutions.

**Review verdict: atoms 1–6 CONFIRMED; zero repairs; zero gaps; nothing
refuted.  The provisional descendant is exact as written and is now
independently reviewed at full slice scope.**
