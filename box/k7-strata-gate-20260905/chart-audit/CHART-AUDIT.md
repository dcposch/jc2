# K=7 chart audit (chart requirement only)

## Outcome

The ten `K=7`, `b=9..13`, `q0/q1` light charts reconstruct from the charged
`pinned_chart.py` coefficient boxes and identities plus the charged beta-strata
LEVEL-4 formulas.  The independent reconstruction agrees byte-for-byte with the
production Singular preludes, and its independently re-aliased integral rows
agree byte-for-byte with the fresh `.ms` files.  Fresh hashes agree with the
producer's exact-Q custody records for all ten files.

There is one wording correction.  It is literally false that
`theorem_cut=False` and `theorem_cut=True` have identical unknown rings: the
latter adds the auxiliary scalar `lam`.  No *geometric* `h/B/q` unknown is
dropped.  The valid inclusion is over

```text
S = Q[h_ij,B_ij,q(active),q_pin_inv],  T = S[lam]:
I_light * T  subset  I_full.
```

Therefore `I_light=S` implies `I_light*T=T` and hence `I_full=T`.  This repair
does not weaken any unit conclusion, but the promotion report should say
`CONFIRMED-WITH-FIX`, not repeat the literal same-ring claim.

## Custody and source reconstruction

The receipt-derived manifest was made with `awk`; `sha256sum -c` returned 7/7
OK.  Evidence: `charged-inputs.sha256` and `charged-inputs.check.log` here.

Charged source citations:

- `inputs/pinned_chart.py:79-104`: `mons`, `h_mons`, `lower_beta_mons`, and
  coefficient naming; `:148-175`: parameter weights and `h,B,Al,Rh`;
  `:180-215`: rho and ID6 Jacobian rows; `:217-245`: MASTER rows and `RR->SS`
  map.
- `inputs/k4ray-beta-strata-grok46-20260905.md:43-58`: exact LEVEL-4 top and
  two-chart cover; `:64-73`: exact `h/B` boxes and definition of `I_light`;
  `:159-164`: FALLACY checks on row versus unknown deletion and ring maps.
- `inputs/k4ray-degree-tower-opus5-20260903.md:120-123`: E-CUBIC identity;
  `:167-186`: MASTER theorem and its `K+6` cutoff.

The beta-strata `strata_chart.py` and producer `strata_chart.py` differ in
exactly one line, their output-root `HERE`.  The audit does not rely on that
fact alone.  `chart_structure_audit.py` loads the charged pinned file, uses its
`QUOY`, full coefficient boxes, names and joins, and independently constructs
each chart's names, weights, `Q`, `Btop`, forced rho top, rho rows, ID6 Jacobian
rows, target row, localizer, and optional MASTER rows.  All twenty light/full
preludes equal the producer prelude strings byte-for-byte.  For each completed
chart it also reconstructs the Singular dump script, parses the dumped rows,
independently applies the declared longest-name-first `v_i` alias map, and
compares the resulting msolve input byte-for-byte.  The dump script explicitly
uses `cleardenom(ROWS[i])`; all fresh `.ms` files are characteristic zero and
contain no `/`.

## Exact unknown sets and cover

For `K=7`, `H=y^6(y-x)`, so `H^2 | P^3` gives
`P=y^4(y-x)Q`.  The exact normal-form cap `deg_y P<=6` gives `deg_y Q<=1`.
For `d=b-5`, therefore

```text
Q = q0*x^d + q1*x^(d-1)*y.
```

The `q0` chart retains both scalars and adds `q0*q0_inv-1`.  The `q1` chart is
the locus `q0=0`, retains `q1`, and adds `q1*q1_inv-1`.  These cover every
nonzero pair `(q0,q1)`, hence every exact-degree-`b` top form.  Omitting `q0`
on the second chart is the defining chart equation, not a floor.

The `h` set is all `(i,j)` with `i+j<=6` except `(0,6)`: 27 coefficients.  The
exception is the charged monic/leading-form gauge, not a floor.  The lower `B`
set is exactly

```text
{ B_i_j : 0<=j<=6 and 0<=i<=b-1-j },  count = 7b-21.
```

There is no weight-floor test in the construction.  The cap `j<=6` is the
charged `deg_y beta<K` normal-form box.  Top/geometric/localized counts are:

```text
b   lower-B   q0 geom/GB   q1 geom/GB   rho cutoff (degree >=)
9      42       71/72        70/71             13
10     49       78/79        77/78             16
11     56       85/86        84/85             19
12     63       92/93        91/92             22
13     70       99/100       98/99             25
```

Each light ideal consists only of the simplified rho/J row ideal, `CSTP-1`,
and the chart localizer.  Fresh markers on every chart say
`TARGET_FOUND 1`, `PRE__CST_ZERO 0`, `PRE__HOMOG_I 1`, and
`PRE__THEOREM_SKIPPED disabled`.

## Generator comparison

The frozen values below are extracted from exact-Q `EXACTQ_UNIT` records in
`box/k4ray-strata-solve-20260905/all-msjob.jsonl` (file SHA-256
`75799f0f9dea54a43d13bdfd230e4eac9ac78a7f9cda204e0a6200ae2770119c`).

```text
b  chart  vars gens bytes     frozen/fresh SHA-256
9   q0     72   241 12675213  15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275
9   q1     71   235 11511528  09002c7229da517ca0d809f925873aeb94d44650467bd6addf71268aacbb7934
10  q0     79   261 19173893  273a1a0f65308af6019c3b8986fa921c76d4e27da30d0b675afc532bc3f3d434
10  q1     78   255 17715692  a49433e9834c4fa7a76a89aef50e7f3852ee0e26ff1d665bc1c8516dc390f97d
11  q0     86   281 27133266  e8e57139c2292f0535226e7fb8fc2fac90b459685e939b825abec31531b2367e
11  q1     85   275 25367692  42f96a5f916e94457887e933cb8cb3f8656537e1547e719e30851075990fd4f1
12  q0     93   301 36605124  3a3821db1511fa96096f627d5d5ed23b1b60a2c95022f33dfb90791a4c60561d
12  q1     92   295 34517061  875573726b784dc4700de3835f0130617279eb5bab451f712f77088c26cae4e2
13  q0    100   325 47622625  970026efbf5ffd1150def477d64de057b8212455527a15f6abbf18807d5cce2c
13  q1     99   317 45201213  570e241e4e2515d1c97c77f9b7696e5d519fb97697543da93410ca5eb2797a8b
```

## Precisely which rows I_light drops

With `B=2 beta`, `Al=4 alpha`, and `Rh=4 rho`, the charged E-CUBIC identity
shows that

```text
E64 = 8*B^3 - 48*Rh*h^2 - 72*B*Rh + 9*Al^2 = 64*(g^2-f^3).
```

For every chart the omitted rows are exactly

```text
coeff_(x^i*y^j)(E64 - lam*(h^2+B))
for every nonzero x,y coefficient with i+j > 13.
```

This predicate is the complete list; substitute the per-chart `Q` values
`q0*x^d+q1*x^(d-1)*y` or `q1*x^(d-1)*y` for `d=4,5,6,7,8` respectively.
No J, rho, target, localizer, `h`, lower-`B`, or active-top coordinate is
removed.

`theorem_row_support_audit.py` gives an explicit, independently reconstructed
list in `theorem-row-support.json` and a compact list in
`theorem-row-support.tsv`.  Write `D=i+j`; every range below means all rows
`coeff_(x^(D-j)y^j)(ELAM)` for every integer `j` in the range.  On every chart
the common bulk is

```text
D=14..20:       j=0..D
D=21..2b+10:    j=0..20.
```

The exact tails and raw/simplified row counts are

```text
b   chart  D=2b+11  D=2b+12  D=2b+13  raw=simplified
9    q0      2..20     8..20    14..20       333
9    q1      4..20    10..20    16..20       327
10   q0      2..20     8..20    14..20       375
10   q1      4..20    10..20    16..20       369
11   q0      2..20     8..20    14..20       417
11   q1      4..20    10..20    16..20       411
12   q0      2..20     8..20    14..20       459
12   q1      4..20    10..20    16..20       453
13   q0      2..20     4..20    12..20       507
13   q1      4..20     8..20    15..20       498
```

The support proof does not infer generic nonvanishing from probability.  Monic
division in `y` gives exact support upper bounds: `deg_y Al<=5`,
`deg Al<=2b-7`, with its top band divisible by `y^2` (`q0`) or `y^4` (`q1`);
and `deg_y Rh<=6`, `deg Rh<=2b-1`, with the same respective divisibilities in
its top band.  (The degree-`2b` remainder cancels because
`B_b^2/H=4y^2(y-x)Q^2`.)  Exact integer specializations then witness a nonzero
coefficient for every support point allowed by those bounds, for `Al`, `Rh`,
and finally `ELAM`.  Thus a witness proves each universal coefficient is
nonzero, while the support bounds exclude all other positions.  Singular's
own exact-Z arithmetic rechecked `Al`, `Rh`, `ELAM`, and the extracted support
for all 100 specializations.  Singular's `simplify(EROWS,2)` only removes zero
entries here, so the raw and printed row counts agree.

The machine-side licence in the full prelude is
`PRE__THEOREM_CUTOFF 13`, followed by `PRE__THEOREM_ROWS <count>`.  Its
mathematical licence is MASTER: for `K>=7` there is unique lambda with
`deg(g^2-f^3-lambda*f)=K+6`; at `K=7`, `K+6=13`.  Scaling by 64 merely rescales
lambda.  The fresh light files instead print `PRE__THEOREM_SKIPPED disabled`.

`emit_theorem_rows.py` is also an independent E-only exact-Q symbolic
enumerator.  Its large-expression runs were preempted on the fleet to protect
the certificate/lift jobs after the fleet reached 146 GiB used.  At preemption
the initial jobs had run roughly 20 minutes and used about
3.1/5.1/4.8/8.2 GiB for `b9q0/b10q0/b10q1/b11q0`; a local `b9q1` attempt had
used about 2.7 GiB.  The exact support audit above replaces those incomplete
runs without claiming they completed.

## Chart verdict

Every chart: generator agreement **CONFIRMED**.  The chart family,
cover, and absence of geometric floor deletion: **CONFIRMED**.  The literal
same-ring phrase “never unknowns; `I_light subset I_full`”:
**CONFIRMED-WITH-FIX** via `S -> S[lam]` as stated above.  No chart is refuted.

No exit-price assertion is made, so no `charge_basis=` line is emitted.
