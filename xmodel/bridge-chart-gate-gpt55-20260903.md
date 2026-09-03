# Bridge chart gate for the K=16 ray

Date: 2026-09-03.  Scope: frozen inputs from
`/tmp/jc2-lane.VZaWdW/inputs`; new drivers/results only in
`box/bridgegate-20260903/`.  No ledger files, `jc2-lean`, or prohibited
in-progress reports were edited or used as sources.

## 0. Custody

The lane receipt `xmodel/bridge-chart-gate-gpt55-20260903.run.v2` was parsed
mechanically with `awk`: `charged_input_<i>_sha256` was paired with
`charged_input_<i>_basename`, written to
`/tmp/bridge-chart-gate-gpt55-20260903.sha256.manifest`, and checked by
`sha256sum -c`.  All 14 frozen inputs returned `OK`; no digest was retyped into
the manifest.

Primary new artifacts:

```text
box/bridgegate-20260903/bridgegate_build.py
box/bridgegate-20260903/emit_runtime_bridge_sing.py
box/bridgegate-20260903/subset_audit_t1_2_3_4.json
box/bridgegate-20260903/run_summary.json
box/bridgegate-20260903/graded_terminal_pattern.json
box/bridgegate-20260903/moh-pages/moh-p209-pdf70-70.png
box/bridgegate-20260903/moh_p209_control.out
```

Claim labels are literal.  `PROVED-HERE` means a checked derivation in this lane
or in a charged frozen input.  `MEASURED` is reproducible output.  `MEASURED-
MODULAR` is not a characteristic-zero proof.  No exit-price assertion is made;
there is no `charge_basis` line.

## 1. BNF audit

Notation: on the ray

```text
n=12t+4=4e,  m=8t+4=4q,  e=3t+1,  q=2t+1.
```

**Definition of `etat`.**  The `etat` used in the BNF proof is the charged
reciprocal formal-root parameter

```text
etat = Q^(-1/m),     Q = etat^(-m),
P = etat^(-n) + sum_j p_j(gamma) etat^j.
```

This is the same reciprocal dictionary parameter used in
`k16-middle-spine-opus5-20260903.md:90-112`.  Since `m=4q`,

```text
etat^(-4)=Q^(4/m)=Q^(1/q)
```

exactly.  The Laurent series `Q^(1/q)` exists in characteristic zero because
on the bridge chart `Q=h^q(1+u)` with `u` supported in h-powers `<=-2`, so
`Q^(1/q)=h(1+u)^(1/q)` is the binomial Laurent series with leading h-term `h`.

**Tuple vanishings.**  In the reciprocal expansion of `P`, the charged
dictionary says the non-4-divisible coefficients below the first tuple index
vanish.  Hence the non-positive exponents are exactly

```text
-n, -n+4, ..., 0,
```

and the corresponding coefficients are

```text
a_k = p_(-n+4k),  0<=k<=e,  a_0=1.
```

Thus

```text
S := sum_(k=0)^e a_k Q^((e-k)/q)
   = sum_(k=0)^e a_k etat^(-n+4k)
```

is exactly the non-positive-exponent part of `P` in `etat`.

**h-negative terms.**  Every h-adic coefficient is reduced modulo the monic
quartic approximate root `h`, so its representative has `deg_pi < 4`.
This includes the beta coefficients: the basis elements are
`1`, `gamma`, `A`, `B`, `z=pi-gamma`, with `deg_pi` respectively
`0,0,3,2,1`; products in the bridge driver are Euclidean-reduced after every
h-adic multiplication.  Since `etat=pi^-1+O(pi^-2)` and `h` is monic of
pi-degree 4, a nonzero term `c h^i` with `deg_pi c=d<4` has

```text
ord_etat(c h^i) = -d - 4i >= -3 - 4i.
```

For `i<0`, this is `>=1`, so every h-negative term in `S` has positive
`etat`-order.

**Polynomial-degree argument.**  Let `S_{>=0}` be the truncation of `S` to
non-negative h-powers.  The preceding paragraph gives
`ord_etat(P-S_{>=0})>0`.  But `P-S_{>=0}` is an ordinary polynomial in `pi`:
`P` is polynomial, and `S_{>=0}` is a finite sum of h-powers with polynomial
coefficients.  A nonzero polynomial of pi-degree `d` has leading term
`lc*pi^d = lc*etat^(-d)+...`, hence `ord_etat=-d<=0`.  Therefore the difference
is zero:

```text
P = [ sum_(k=0)^e a_k Q^((e-k)/q) ]_(h>=0).        (BNF)
```

**Scalar `a_k`.**  The scalar claim uses the monomial-Jacobian version of
Lemma 2.1 in the reciprocal parameter, not the literal constant-J statement
alone.  The charged Newton/Lemma audit derives it at
`k16-ray-T-newton-sol56-v3-20260903.md:70-99`: for `J=c*gamma`, coefficients
`p_j` in the expansion anchored at `Q=etat^(-m)` are constants for `j<m-1`,
and the first allowed gamma-dependent anchor is `j=m-1=8t+3`.  Here
`j=-n+4k<=0<m-1`, so every `a_k=p_j` is scalar.

**BNF verdict.**  `BNF CONFIRMED` relative to the charged reciprocal dictionary
and the charged monomial Lemma 2.1 derivation.  Provenance note: Moh's printed
Lemma 2.1 is the constant-J theorem; the `c*gamma` variant is a charged
derived theorem, not a separate printed Moh statement.  I found no algebraic
gap in the BNF line after that dependency is accepted.

## 2. Subset audit

The bridge beta coefficients use exactly the order-chart spaces from the
frozen `t_order_system.py:chart_spaces(t,1,A,B,z)`.  I checked `t=1..4` in
`subset_audit_t1_2_3_4.json`:

```text
t  unknowns  alpha check                         beta check
1  11        direct BNF expressions: pass         direct: pass
2  17        direct BNF expressions: pass         direct: pass
3  23        BNF closure/nesting audit: pass      direct: pass
4  29        BNF closure/nesting audit: pass      direct: pass
```

For `t=3,4`, expanding every concrete alpha expression was the known Sympy
bottleneck, so the driver instead checked the exact closure property needed by
BNF: every product of basis elements in `S_i*S_j`, after monic h-reduction, has
each h-shifted coefficient in the required `S_{i+j-delta}`, and the spaces are
nested.  The closure failure count was zero for both `t=3` and `t=4`.

Therefore the bridge chart is a subset of the charged Theorem-1.2 order chart
at `t=1..4`.  Since BNF is forced by the tuple conditions, the tuple locus lies
inside the bridge chart, and the bridge chart remains a necessary superset of
the tuple locus.

## 3. Replayed kills at t=1,2

I replayed the fixed raw Singular inputs whose hashes are cited in the charged
spine (`k16-middle-spine-opus5-20260903.md:290-293`):

```text
t=1  nvars=12  ngens=24  sbsize=1  G[1]=1
     EMPTY <c,Tr*c-1> -> 0,  NONEMPTY <c-1,Tr*c-1> -> 1
     wall 0:00.03, max RSS 11448 KiB

t=2  nvars=18  ngens=59  sbsize=1  G[1]=1
     EMPTY <c,Tr*c-1> -> 0,  NONEMPTY <c-1,Tr*c-1> -> 1
     wall 0:03.54, max RSS 16444 KiB
```

Hashes:

```text
a99b483a0776e36580f50d2ab66ba9bfa3c4a7a42090709c831e79519fd51488  t1 fixed
6dd723bd5932c98fe17bccbe7db87518856546ae20347e8864c5cacf7b8467e7  t2 fixed
```

I also emitted and ran an h-adic normal-form presentation of the same bridge
Jacobian identities.  It has fewer coefficient generators because it equates
monic h-remainders rather than raw pi/gamma coefficients:

```text
t=1  unknowns=11  h-adic generators=16  exact Q  G[1]=1  wall 0:00.38
t=2  unknowns=17  h-adic generators=27  exact Q  G[1]=1  wall 0:07.10
```

The semantic actual-pair control is recorded in
`box/bridgegate-20260903/actual_pair_control.json`: `(pi,pi-gamma^2/2)` has
`J=gamma` but `deg_pi=(1,1)`, so it is not a point of the K=16 descended tuple
charts (`(16,12)` at `t=1`, `(28,20)` at `t=2`).  It is only a wrapper/Jacobian
sign control.

## 4. Runs at t=3..8

The frozen raw `bridge_chart.py` still has the known direct-expansion
bottleneck: `bridge_chart.py 2` entered the full
`sp.expand(diff(Q)*diff(P)-...)` step and I stopped it after it failed to
return promptly.  The new runtime Singular builder avoids that particular
Python expansion and constructs the h-adic BNF equations inside Singular.

Generator counts below are for the h-adic normal-form bridge presentation:
`11t+4` coefficient rows plus `Tr*c-1`.  This presentation is equivalent as a
polynomial identity test, but the raw fixed `t=1,2` counts above are kept
separate.

```text
t  unknowns  h-adic gens  modular / exact result
3  23        38           GF(32003): [1], 3:35.18, 41760 KiB
                         GF(32009): [1], 2:55.88, 41616 KiB
                         GF(32027): [1], 2:45.41, 42112 KiB
                         Q std: stopped at 4:59.29, no MAIN_DONE
                         Q slimgb: stopped at 3:35.64, no MAIN_DONE

4  29        49           GF(32003) std: stopped at 4:45.19, no MAIN_DONE
                         GF(32003) slimgb: stopped at 4:04.65, no MAIN_DONE
                         other primes and Q not launched after first-prime block

5  35        60           build-only completed, 0:13.47, 33696 KiB
6  41        71           build-only completed, 0:39.13, 63564 KiB
7  47        82           build-only completed, 1:06.63, 145724 KiB
8  53        93           build-only completed, 2:33.12, 318508 KiB
```

`T` verdict from these runs:

```text
t=3: MEASURED-MODULAR on the bridge chart over three primes; not proved over Q here.
t=4: no modular verdict; first prime did not finish in the bounded attempts.
t=5..8: no modular or exact verdict; only BNF construction/count data.
```

Thus `(T)` at `t=5..8` is **not PROVED-HERE** on the bridge chart and is not
even `MEASURED-MODULAR` in this lane.  The honest type is `OPEN[COMPUTATION]`
for those fixed `t`.

## 5. Terminal data

No full post-normalisation bridge terminal system was obtained for `t=4..8`.
The requested canonical band-descending terminal rows over `A_t` therefore
cannot be printed without filling a computation gap by analogy, which
FALLACY-v2 forbids.

The graded normalizer was replayed from the frozen scripts and is recorded only
as `GRADED_NORMALIZER_ONLY_NOT_FULL_BRIDGE_TERMINAL` in
`graded_terminal_pattern.json`.  The universal rows are:

```text
H_t(y)=12(2t+1)^2 y^2 - 12(2t+1)(t+1)y + (t+1)(3t+2),
c_t(y)=t(3t+1)y((t+1)-6(2t+1)y)/(6(2t+1)^3).
```

The `phi_5` residual modulo `H_t` has numerator associate

```text
-t(t+1)(20t*y - 3t + 10y - 2)/2,
Res_y(H_t,num phi_5)=12*t^2*(t+1)^2*(2t+1)^4*(3t+2)*(4t+1).
```

Specialized primitive `H_t` data:

```text
t=3  H=147y^2-84y+11       disc=588
t=4  H=486y^2-270y+35      disc=4860
t=5  H=242y^2-132y+17      disc=968
t=6  H=507y^2-273y+35      disc=3549
t=7  H=675y^2-360y+46      disc=5400
t=8  H=578y^2-306y+39      disc=3468
```

This is the measured graded pattern only.  It is not a substitute for the
requested full bridge terminal systems.

## 6. Moh p.209 discrepancy

`pdftoppm -r 200 -f 70 -l 70 -png` rendered printed Moh p.209 as PDF page 70:

```text
box/bridgegate-20260903/moh-pages/moh-p209-pdf70-70.png
sha256=19bbfa56fd017c545219fadc51fcc1e515a7faedc3ec059913eccacf133928a9
```

The page visibly has the same gauges
`(f,g)->(f-(3/4)a_3, g-a_1 f-a_4)`, then displays

```text
f = h^3 + beta_2 h + beta_3
g = h^4 + (4/3)(beta_2 h^2 + beta_3 h)
    + (2/9)(beta_2^2+2 gamma) - (4/81)delta + a_2 h^2.
```

The isolated frozen control `moh_p209_control.py` returned

```text
uniform-bridge P == Moh p.209 formula : False
residual: 2*a2*(b1*c3*p**2 + b2*c3*p + b3*c3
                - c3*g*p**2 + c3*p**3 + c4)/3
```

The parenthesized expression is exactly `beta_2`.  Therefore the discrepancy is

```text
(2/3) a_2 beta_2.
```

This is not a different normalization: the page and the control use the same
displayed gauges and the same definitions of `beta_2`, `gamma`, and `delta`.
The missing term is the h-nonnegative part of
`a_2 f^(2/3)=a_2 h^2(1+beta_2 h^-2+beta_3 h^-3)^(2/3)`.  Verdict: Moh p.209
has an omitted truncation term/misprint; the coefficient count remains 10.

## 7. Final verdict

```text
BNF: CONFIRMED, conditional only on accepting the charged reciprocal dictionary
     and charged monomial Lemma 2.1 derivation.

bridge subset order chart: CONFIRMED at t=1..4.

t=1,2 bridge kills: CONFIRMED by fixed raw Singular replays with controls.

t=3 bridge chart: MEASURED-MODULAR [1] over three primes; exact Q not completed.

t=4..8 bridge chart: NOT PROVED-HERE.  t=4 did not finish even over the first
prime in the bounded attempts; t=5..8 have construction/count data only.

terminal systems t=3..8: full bridge terminal pattern OPEN/NOT PRODUCED.
graded H_t/c_t pattern: MEASURED, not promoted to a full terminal certificate.
```

FALLACY-v2 check: the chart direction is kept as `tuple locus subset bridge
chart subset order chart`; modular results are not promoted to characteristic
zero; raw and h-adic generator presentations are not conflated; no denominator
or pivot-unit branch is asserted without a completed normalization; no graded
pattern is treated as full terminal attainment.

<!-- BODY-END -->
