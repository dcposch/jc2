# ANCHOR-AUDIT GATE -- GPT-5.5 -- 2026-09-03

Lane target: `OPEN[DESCENT-ANCHOR]` hostile gate against
`xmodel/descent-anchor-audit-grok46-20260903.md` sections 0-5.  No ledger
edits.  `jc2-lean` was not inspected.  I used only the frozen inputs in
`/tmp/jc2-lane.gg5Ofk/inputs` for the replay, plus the charged Opus
submission H1/section 13.

## 0. Mechanical Input Gate

The checksum manifest was generated mechanically from
`xmodel/anchor-audit-gate-gpt55-20260903.run.v2` with `awk` over the
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines, then
checked with `sha256sum -c`.

Result: **11/11 OK**.  The generated manifest is
`box/anchor-gate-20260903/input-manifest.sha256`.

Frozen drivers copied for local replay:

```text
box/anchor-gate-20260903/measure_anchor.py
box/anchor-gate-20260903/phi_delta.py
box/anchor-gate-20260903/moh_skeleton_full.py
box/anchor-gate-20260903/full_tree_partition.py
box/anchor-gate-20260903/anchor_zero_rows.txt
```

Replay artifacts:

```text
box/anchor-gate-20260903/measure_anchor.stdout
box/anchor-gate-20260903/measure_anchor.json
```

The generated `measure_anchor.json` is byte-identical to the frozen
`/tmp/jc2-lane.gg5Ofk/inputs/measure_anchor.json`.

## 1. Moh Page Images Opened

The PDF has 74 pages.  The first attempted offset was wrong; opening that
image showed PDF page 15 is printed p.154.  The corrected mapping is:
printed page = PDF page + 139.

Required page images opened from the charged PDF, rendered with
`pdftoppm -r 200 -png`:

```text
p.173  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-34.png
p.174  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-35.png
p.175  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-36.png
p.176  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-37.png
p.177  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-38.png
p.178  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-39.png
p.179  box/anchor-gate-20260903/corrected-pages/moh-printed-p173-179-40.png
p.196  box/anchor-gate-20260903/corrected-pages/moh-printed-p196-198-57.png
p.197  box/anchor-gate-20260903/corrected-pages/moh-printed-p196-198-58.png
p.198  box/anchor-gate-20260903/corrected-pages/moh-printed-p196-198-59.png
```

Supporting images opened because the claims depend on them:

```text
p.151  box/anchor-gate-20260903/corrected-pages/moh-printed-p151-12.png
p.199  box/anchor-gate-20260903/corrected-pages/moh-printed-p199-60.png
p.207  box/anchor-gate-20260903/corrected-pages/moh-printed-p207-68.png
```

## 2. Source Check

**Def. 5.1(3), p.179: CONFIRMED.**  The printed denominator contains the
factor `n - M_s - 1`.  In ASCII transcription:

```text
delta_i = 1 - (n - M_i) prod_{j=i+1..s}(V_j(n-M_j)-d_j)
              / ((n - M_s - 1)
                 prod_{j=i+1..s}(V_j(n-M_{j-1})-d_j)).
```

The same page, Def. 5.1(2), also prints `V_{s+1}=d_{s+1}` for a tower
`D_s superset ... superset D_r`.  Thus `V_{top+1}=d_{top+1}` is Moh's
convention for a Def. 5.1 tower.  Applying it after truncating a dictionary
is the lane's reconstruction of that Moh convention on the effective tuple;
Moh does not print a separate "truncated dictionary" algorithm.

**p.174 drop: CONFIRMED as Moh's effective-pair convention; GAP for a
separate monomial-Jacobian theorem.**  The p.174 Definition-Remark says
that if `M_h = n - 1`, it is dropped from consideration, and the effective
characteristic pairs exclude that `M_h`; the last effective characteristic
pair is denoted `M_s`.  The proposition statement around it is phrased for
the root configuration of `g` and the approximate-root factors, not as a
special Appendix-II child algorithm.

For this gate I read the print as follows: once a descended tuple is accepted
as characteristic data, p.174 supplies the normalization `drop M_h=n-1`.
What is **not** supplied by p.174 or Lemma 2.1 is a fresh theorem that every
monomial-Jacobian pair `J=c gamma^k` must have that terminal entry.

**Lemma 2.1, p.151: GAP for `J=c gamma^k`.**  The printed lemma states an
iff for `J_{x,y}(f,g)=c`, a nonzero constant.  Its note says that, if the
Jacobian condition is satisfied, the `M_i` terminate at `n-1`.  The print
does not state the same lemma for `J=c gamma^k`.  Therefore the sentence
"Lemma 2.1 forces every Jacobian pair to have `M_h=n-1`" is confirmed only
when "Jacobian pair" means the constant-J condition used in Lemma 2.1.  It
is a gap if extended to the descended monomial-Jacobian child.

**Prop. 5.1(1), pp.173-174: CONFIRMED, with the same scope caution.**  When
`M_h=n-1`, the printed radius is finite:
`delta_h=delta_{h-1}=-1/(n-M_{h-1}-1)`.  The construction uses the
`h-1` disc containing all roots and applies Prop. 4.6 at `r=h-1`.  The
naive expression `-1/(n-M_h-1)` is not the applicable formula at
`M_h=n-1`.

**Prop. 6.3/6.4, pp.197-199: CONFIRMED.**  The stated Prop. 6.3 hypotheses
are `g` monic in `y`, `deg g = deg_y g = n > 1`, `delta_s=-1`, and the
minor-disc bound `delta^*_{s-1} >= v_s/u_s`.  Prop. 6.4 assumes the same
degree/monicity and `delta_s=-1, u_s=1`, then supplies that bound.  Neither
proposition states a hypothesis involving the child's anchor
`n' - M'_{s'} - 1`.

## 3. Replay Results

Command run:

```text
python3 box/anchor-gate-20260903/measure_anchor.py
```

The replay reproduces the p.207 control and the negative control:

```text
10/10 p.207 rationals MATCH: True
(15,10), V2=3: Def51 delta_2 = -1/3
drop-factor control: delta_2 = -3
drop-factor BREAKS the match: True
```

p.207 itself has the five `u_s=1` transformed rows:
`(16,12)`, two `(21,14)` rows, and two `(15,10)` rows.  The replay reports
`drop=0` on all five, so `Phi_eff` is a no-op on that printed control set.

Counts:

```text
n <= 100:
  (1)-(13) rows                         658
  C_FULL_TREE_ODE survivors              58
  u_s=1 descendable                      57
  u_s>1 residue                           1  = (99,66)
  anchor-zero before p.174 drop          38
  evaluable as charged before drop       19
  still undefined after p.174 drop        0
  evaluable after Phi_eff                57

n = 108:
  (1)-(13) rows                         217
  C_FULL_TREE survivors                  21
  C_FULL_TREE_ODE survivors              20
  u_s=1 descendable                      19
  u_s>1 residue                           1  = (108,72), M=[-72,81,106]
  anchor-zero before p.174 drop          12
  evaluable as charged before drop        7
  still undefined after p.174 drop        0
  evaluable after Phi_eff                19
```

Height distribution needs one qualification.  For all descendable rows in
this replay:

```text
n <= 100, after drop: s_eff counts {2: 29, 3: 27, 4: 1}
n = 108, after drop: s_eff counts {2: 12, 3: 7}
```

The charged report's `29/57` for `s_eff=2` is confirmed.  The `14/57` line
is confirmed only as the anchor-zero parent-`s=5` block: among the 38
anchor-zero rows, the post-drop split is `{2:24, 3:14}`.  If read as the
complete all-descendable `s_eff=3` count, it is refuted by the replay:
there are 27 such rows, plus one `s_eff=4` row
`(96,64), M=[-64,-48,-8,20,94], V={2:1,3:1,4:6,5:3}`.

## 4. Item Verdicts

**(a) CONFIRMED.**  Def. 5.1(3) as printed at p.179 carries
`1/(n-M_s-1)`.

**(b) CONFIRMED/GAP.**  Confirmed: p.174 drops a terminal `M_h=n-1` from
the effective characteristic sequence; Prop. 5.1(1) gives a finite radius
using `M_{h-1}`.  Gap: Lemma 2.1's printed terminal statement is for
`J=c` nonzero constant, not for the descended `J=c gamma^k` child.  Do not
fill that extension by analogy.

**(c) CONFIRMED.**  Prop. 6.3/6.4 hypotheses never mention the child's
anchor.  Therefore the 38 and 12 anchor-zero rows are not killed by those
proposition headers.  Their obstruction is only the later attempt to feed an
untruncated child with `M'_{s'}=n'-1` into Def. 5.1(3).

**(d) CONFIRMED, with source split.**  `Phi_eff` is:
after the Prop. 6.3 image, drop a terminal `M'_{s'}=n'-1`, set the new
`V_{s*+1}=d_{s*+1}`, then evaluate `(k+1)*Def. 5.1(3)` on the effective
tuple.  The drop and `V_{top+1}=d_{top+1}` are Moh conventions for effective
Def. 5.1 data; the multiplication by `k+1` is the p.207-controlled
monomial-Jacobian radii conversion from the charged descent-radii driver.
All ten p.207 rationals match, and dropping the printed factor breaks the
`(15,10)` control.

**(e) CONFIRMED except the literal all-row height wording.**  The headline
counts reproduce exactly: `658 -> 58`, `57` descendable, `38` anchor-zero,
`0` undefined after drop, residue `1/58=(99,66)`; and `217 -> 21 -> 20`,
`19` descendable, `12` anchor-zero, `0` undefined after drop, residue
`1/20`.  `s_eff=2` on `29/57` and `12/19` is confirmed.  Exact all-row
`s_eff=3` at `n<=100` is `27/57`, not `14/57`; `14` is the anchor-zero
subblock with parent height 5.

## 5. Promotion Scope

Verdict: **PROMOTE-QUALIFIED** for `OPEN[DESCENT-ANCHOR]` as the descent
radii rule on the reviewed finite descent gate.  Do not promote it as a
standalone theorem for arbitrary monomial-Jacobian pairs.

Producer scope:

```text
rule:          delta_i' = (k+1) * Def5.1(3) on descended data
producer:      descent-radii-grok46 phi_delta.py / p.207 controls
printed scope: p.207 rows with raw s' = 2
printed k:     k = 1 for Jacobian X, k = 2 for Jacobian X^2
controls:      10/10 printed rationals; (15,10) drop-factor negative control
```

Reviewed scope in this gate:

```text
rule:          Phi_eff after p.174 terminal-drop normalization
datasets:      C_FULL_TREE_ODE n<=100 and n=108 frozen drivers
rows:          57 + 19 descendable u_s=1 rows
raw height:    s' <= 4
effective ht:  s_eff <= 4
k observed:    k in {1,2,3,4,5,6}, hence k >= 1 in this reviewed descent set
defined:       76/76 after the drop
anchor repair: 50/50 anchor-zero rows repaired, 0 still undefined
```

So the safe campaign statement is: `Phi_eff` is promoted for Prop. 6.3/6.4
`u_s=1` descendants in the reviewed finite driver universe, with raw
`s'<=4`, effective `s_eff<=4`, and `k>=1` as observed.  The formal extension
"Lemma 2.1 also forces monomial-Jacobian children to terminate at `n-1`" is
not sourced by the opened print and remains a typed gap.

## 6. FALLACY-v2 Check

No exit-price assertion is made, so no `charge_basis` line is emitted.  No
cv flag/place/series identification is used.  No floor is promoted to
attainment: the counts are exact finite enumerations from the frozen driver,
and the p.207 rationals are direct controls.  The prime marks in `delta_i'`,
`n'`, and `M_i'` are labels; Lemma 2.1's `f_i'(x)` is the derivative in the
printed proof.  The monomial-Jacobian extension is left as a GAP rather than
filled by analogy.

<!-- BODY-END -->
