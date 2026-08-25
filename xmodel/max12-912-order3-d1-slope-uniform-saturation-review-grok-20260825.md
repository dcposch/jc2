# Hostile review: D1 slope-uniform strict-boundary saturation

| Field | Value |
|---|---|
| Target | frozen slope-uniform D1 compiler / unit-ideal test |
| Reviewer / model | Grok 4.6 (xAI). Hostile source and logical audit |
| Overall verdict | **CONFIRMED** |
| Method | source reading and hand identities only; no local Bash, Python, Singular, Sage, msolve, or other CAS; no inference from still-running AWS jobs |
| Smallest failing identity | none |
| Missing hypothesis | none that affects the licensed unit-ideal test |

## Verdict

**CONFIRMED**

The consumed compiler implements the registered strict-slope Rees gate.  It
undoes exactly the three affine loads, homogenizes the raw descended tails
by the weight identity with `s` of weight zero, substitutes
`Lambda=q^3*rho`, saturates first by the interior product `q*rho`, and only
then cuts the boundary and saturates by the full irrelevant ideal.  The
emitted ring is `Q[q,rho,B,k,mu,nu]` (or the isomorphic normal coordinates),
not `Q(k,mu,nu)`.  The unit-ideal test has the exact logical meaning claimed
by the preregistration and the isotrivial design note.

No running, timeout, smoke, or dual-coordinate endpoint is a substitute for
this source review or for a later exact `SLOPE_UNIFORM_H_IS_UNIT` marker on
a `CONTROL_ONLY=0` characteristic-zero global harvest.

## Strongest exact claim that survives

Over a characteristic-zero field, write `R_l=D_l-delta_l` with
`delta_3=mu`, `delta_6=nu`, `delta_8=1`, and form

```text
Psi_l = D_l(1+q, B, q^18 rho^6 k) - q^{3(12+l)} rho^{12+l} delta_l,
I=(Psi_1,...,Psi_8),
K=I:(q rho)^infinity,
H=((K+(q,rho)):m_B^infinity),
```

in the polynomial ring `Q[q,rho,B_0,...,B_7,k,mu,nu]`, or in the isomorphic
normal coordinates `(p,c,X_0,...,X_5)` with `m_B=(p,c,X_0,...,X_5)`.  Then:

- `H=(1)` excludes every strict (slope `ord Lambda>3 ord q`)
  rational, formal, or Puiseux coefficient-infinity arc whose projective
  leading coefficient is nonzero, for every finite load `(k,mu,nu)`.
- `H!=1` is only a finite-type projective-boundary survivor, equivalently
  a Puiseux-accessibility condition after a finite constant-field
  extension.  It does not produce a rational section over `L(s)`, D1
  monodromy, Taylor polynomiality, a D1 solution, a counterexample, or
  JC2.

## Sharpest non-claim

This review confirms the source and the meaning of the unit test.  It does
not compute `H`, does not bound a jet, does not exclude slope `<=3` or
finite-coefficient D1, and does not close D1, `(8,12)`, maximum twelve, or
JC2.

---

## Charged targets

Read in full.  Byte identity is the charged digest below; this session did
not re-hash on disk.  Fail-closed AWS replay for custody is
`sha256sum -c` of `SOURCE_CLOSURE_SLOPE_UNIFORM.sha256` on a registered
host, which the licensed wrapper already performs before emission.

```text
2824cca5d49a3992f65ea34a1c55884ea1a0e132eaf4a919a9f5153879181f6f  cases/max12_912_order3_d1_weighted_infinity_20260825/FREEZE_SLOPE_UNIFORM.sha256
39f43b1a078a1e07c18a3bd369a7d8f1b63a7d35a3e5015016d798b7743fd885  cases/max12_912_order3_d1_weighted_infinity_20260825/SOURCE_CLOSURE_SLOPE_UNIFORM.sha256
1acb149bc997d4dae1e29b97b0683b99ca38e9d8dd7543b0da03cf64cc152cb7  cases/max12_912_order3_d1_weighted_infinity_20260825/compile_slope_uniform.py
4aa066bad83407eae9383597aba1fc7e3a7e828be28fd77610d4076cef02b1b7  cases/max12_912_order3_d1_weighted_infinity_20260825/PREREGISTRATION_SLOPE_UNIFORM.md
d77bd3ae91113e09b90109842a93e18b84fd129e47b951d45b1d0e953473d809  cases/max12_912_order3_d1_weighted_infinity_20260825/run_slope_uniform_aws.sh
c25092a17cc8db8d70019018e97120776ca374c8c00d20f981bc7cde7436b9b5  cases/max12_912_order3_d1_weighted_infinity_20260825/SLOPE_UNIFORM_SMOKE_V2_CUSTODY.md
b9df8e900f4f07017a8d04bb30888356a4dbf0fc68ec0ad966a0bd7985f2080c  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
de7dd223d472508e057db72a5ec466c6362b762b4ba9a50f4ff823f585e774c7  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-20260825.md
a274c8d8e0883ce7606f31f69803a293afb15ad48fe9d401191cac1cdbe1daee  xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md
bdb369f187284df82935488288d3752c4781e527eec1c38da80b757a26f50c38  xmodel/max12-912-order3-d1-isotrivial-strict-rees-saturation-20260825.md
```

The exceptional-support producer `de7dd223...` is a fixed review target.
Later slope-uniform compilers pin it and do not rewrite it.  Ancillary
freeze members (`README_SLOPE_UNIFORM.md`, the V1 quarantine note, the
general Mason pair) were read for custody and chart language; they are not
a second theorem.

---

## Charge 1 — raw versus shifted rows

**CONFIRMED**

Parent `compile_all` descends ordinary Faber tails into `D_l` on the ring
`(A_0,...,A_7,s,k,mu,nu)`, then forms the compiled rows

```text
R_3=D_3-mu,    R_6=D_6-nu,    R_8=D_8-1,
R_l=D_l otherwise.
```

`Ring.var` / `Ring.one` place `mu` at index `10`, `nu` at index `11`, and
`1` at the twelve-zero monomial.  The slope compiler’s `raw_tail_rows`
deletes exactly those three monomials after demanding coefficient `-1`, and
then forbids any remaining `mu` or `nu` in every row.

`transform_rows` homogenizes the stripped dictionaries and only afterwards
adds the scaled targets

```text
-q^{3(12+l)} rho^{12+l} mu     (l=3, slot 11),
-q^{3(12+l)} rho^{12+l} nu     (l=6, slot 12),
-q^{60} rho^{20}               (l=8).
```

That is formula (4) of the isotrivial note, with `T_l` meaning unshifted
`D_l`.  The catastrophic double-count (unscaled `-1` or `-mu` surviving
into `Psi_l`) is exactly what the strip prevents: an unscaled `-1` in
`Psi_8` would be a unit at `q=rho=0` and would force a spurious `H=(1)`.

No k-load is scaled twice.  The substitution is
`k |-> q^{18} rho^6 k = Lambda^6 k` with `Lambda=q^3 rho`, once.

---

## Charge 2 — every monomial weight

**CONFIRMED**

The runtime test is

```text
sum_{i=0}^{7} (9-i) e_i + 6 e_k = 12+l,
```

with `e_k` read from index `9` and with index `8` (`s`) omitted.  This is
the needed and sufficient identity for the substitution
`A_i |-> B_i`, `k |-> Lambda^6 k` to be the Rees homogenization rather than
a leftover power of `Lambda`.  Character descent only rearranges powers of
`s`; `wt(s)=0` is correct.  Target exponents after the substitution are
`Lambda^{12+l} delta_l = q^{3(12+l)} rho^{12+l} delta_l`, matching the
slots above.

The weight test is not a substitute for character descent.  Character
descent is a separate eight-row rebuild (Charge 3).

---

## Charge 3 — isotrivial twist

**CONFIRMED**

Independently: `sigma(z)=zeta z` gives `wt(a_i)≡-i (mod 3)`.  The descent
`a_i=t^{i mod 3} A_i` with `wt(t)≡2` matches that character.
`wt(r_l)≡l (mod 3)` and `2l·wt(t)≡l (mod 3)` give

```text
r_l = t^{2l mod 3} D_l.
```

The affine D1 target `(r_1,...,r_8)=(0,0,mu,0,0,nu,0,t)` therefore descends
to `(D_3,D_6,D_8)=(mu,nu,1)`, because

```text
(2·3 mod 3)=0,    (2·6 mod 3)=0,    (2·8 mod 3)=1,
```

so `r_8=t·D_8` converts `r_8=t` into `D_8=1`.  In the étale chart
`tau=t-1`,

```text
q=t^3-1=tau(3+3 tau+tau^2),    u(0)=3,
```

which is étale at `tau=0` in characteristic zero (`dq/dt=3t^2`, value `3`).
Putting `rho_t=u^3 rho` yields `Lambda=tau^3 rho_t` and
`gamma_8=t=1+tau`, with no extra `t` factor on rows 3 and 6.

The runtime rebuild uses `(2l mod 3)` directly, not the parent lookup
table `(0,2,1)`, reconstructs every `D_l` from `independent.build()["tails"]`,
and raises on any of the eight rows.  It compares unshifted tails, which is
the correct identity (5).  The ordinary-chart polynomials (7) are an étale
accelerator and are not the emitted ideal; the registered computation is
(4).

---

## Charge 4 — strict-slope bridge

**CONFIRMED**

In this affine chart `rho` is regular.  Valuations of a one-parameter arc
with `ord q>0` satisfy

```text
ord Lambda = 3 ord q + ord rho.
```

Hence `ord rho>0` if and only if `ord Lambda>3 ord q`.  Slope `=3` is the
locus `rho` a unit, which the slope-three control keeps off `rho=0`.  Slope
`<3` makes `rho` polar and leaves the chart.  The registered boundary
`q=rho=0` is therefore exactly the strict sector in this chart.

For a rational slope `m/n>3` in lowest terms set `q=eps^n`,
`rho=eps^{m-3n}`, `Lambda=eps^m`.  Then `Lambda=q^3 rho` holds as monomials,
`kbar=q^{18} rho^6 k=eps^{6m} k`, and
`q^{3w} rho^w=eps^{m w}`.  These are exponent identities, not samples.

Coefficient normalization: `alpha=max_i pole(A_i)/(9-i)=m/n` produces

```text
B_i = eps^{m(9-i)} A_i(1+eps^n)
```

regular, and maximality of `alpha` forces some `B_i(0)!=0`.  If every
leading coefficient vanished, the true slope would be larger, or `A≡0`
(the irrelevant origin `f=z^9`).  Projective saturation removes that origin.
Cyclic D1 keeps `k` finite, so `k` is a polynomial coordinate, not a second
infinity.

---

## Charge 5 — exact ideals and saturation order

**CONFIRMED**

The emitted program computes, in order,

```text
K = sat(I, (q*rho)),          # I:(q rho)^infinity
boundary = K + (q, rho)       # plus Rabinowitsch v*chart-1 only in a chart
                              # and only after K
H = sat(boundary, irrelevant) # full ideal (p,c,X_0,...,X_5) or (B_0,...,B_7)
```

Adding `(q,rho)` before interior saturation would keep components already
supported on `q rho=0` that are not limits of the interior.  The compiler
does not do that.  Charts impose `p!=0` or `c!=0` only after `K`.

Saturation is by the irrelevant *ideal*, not by the coordinate product.
The product is retained only as the negative axis control.

Product versus sequential: in any commutative ring
`I:(ab)^infinity=(I:a^infinity):b^infinity` (equalize exponents by
multiplying by the missing factor, which stays in the ideal).  The program
compares `std(I:(q rho)^infinity)` with `std((I:(q)^infinity):(rho)^infinity)`
by two-sided reduction.  Algebraically this is the registered control.
The two-containment is executed on whatever `I` is: the D1 source when
`CONTROL_ONLY=0`, the synthetic arc when `CONTROL_ONLY=1`.

V1 read `KS[2]`/`HS[2]` on a one-entry `sat` list and is quarantined.  The
successor uses `KS[1]`/`HS[1]` only and prints `K_SATURATION_API=LIST_IDEAL_ONLY`.
The wrapper sets `rc=104` on any nonempty Singular stderr.

---

## Charge 6 — constant field and load strata

**CONFIRMED**

```text
ring R=0,(q,rho,<eight projective>,k,mu,nu), (dp(2),dp(8),dp(*));
```

Characteristic zero, polynomial ring over `Q`, with `k,mu,nu` among the
variables.  This is not `R=(0,k,mu,nu),(...)`.  No load stratum is inverted.
The parent V2 generic path over `Q(s,k,mu,nu)` is a different emitter and
is not consumed.  The printed marker is
`COEFFICIENT_RING=POLYNOMIAL_Q_K_MU_NU_NO_LOCALIZATION`.

---

## Charge 7 — common-cubic coordinates and coverage

**CONFIRMED**

The map

```text
B_7=3p,  B_6=3c,  B_i=C_i(p,c)+X_i  (i<=5),
```

with `C_i` the coefficients of `(z^3+p z+c)^3`, is a polynomial
automorphism of `A^8` over `Q`: inverse `p=B_7/3`, `c=B_6/3`,
`X_i=B_i-C_i(p,c)` is polynomial over `Q` because `3` is a unit in
characteristic zero, and the Jacobian is triangular with diagonal
`(3,3,1,...,1)`.  Pullback of `(B_0,...,B_7)` equals `(p,c,X_0,...,X_5)`
as ideals over `Q`, not merely up to radical, because
`B_i ≡ X_i (mod (p,c))`.

Hand expansion of `(z^3+p z+c)^3` reproduces the frozen `CUBE_PC` /
`CUBE_STRING` dictionaries.  They match the independently reviewed graph
(2) of `de7dd223...` / `a274c8d8...` (`r` there is `c` here; `rho` is the
new slope coordinate and does not clash).

The reviewed reduced exceptional divisor is weighted `P(2,3)`.  Every
projective point has `(p,c)!=(0,0)`, hence `B_7!=0` or `B_6!=0`.  The
registered `p` and `c` charts therefore cover that radical if the global
job is inconclusive.  They are not a cover of a hypothetical extra
component with `p=c=0` and some `X_i!=0`; the global characteristic-zero
job remains the arbiter for any such extra support.

The `p`-chart is `v p-1=0` with `c` free; the `c`-chart is symmetric.
Neither substitutes a numerical value of `c^2/p^3`.  The discriminant

```text
Delta=-4p^3-27c^2
```

is not a pivot: it does not appear in the emitted program.  On the axes,
`Delta=0` forces the origin in characteristic zero, so `Delta=0` with
`p c!=0` is a nonempty non-axis locus and is retained by the symbolic
charts.  A separate `Delta=0` stratum would be required only if some later
normal-form step inverted `Delta`; this compiler does not.

`verify_common_cubic` specializes the *unshifted* tails at `s=1`, `k=0`,
`X=0`.  That is the associated-graded vanishing `D_l(1,C(p,c),0)=0`, not
the affine equations `R_l=0` (which still carry `-mu`, `-nu`, `-1`).  At
`q=rho=0` the scaled targets vanish, so the boundary equations are the
unshifted ones.  Correct.

---

## Charge 8 — controls and custody

**CONFIRMED**

| Control | Implementation | Required outcome |
|---|---|---|
| Synthetic strict arc | `p=1`, `c=q`, `X_0=rho`, other `X_i=0` (or the `B`-analogue) as `I` under `CONTROL_ONLY=1`; also as a toy before source operations | `H` nonunit |
| Pure boundary | `sat((q,rho),(q rho))` | unit |
| `rho`-unit slope three | `rho-1`, leading coordinate `1`, others `0` | unit after cutting `rho=0` |
| Irrelevant ideal vs product | axis point with first coordinate `1`; `sat` by the full irrelevant ideal versus `sat` by the coordinate product | nonunit vs unit |

The V2 smoke (`c25092a1...`) ran `D1_SLOPE_CONTROL_ONLY=1` on Box02, printed
`CONTROL_ONLY=1`, `SLOPE_UNIFORM_H_IS_UNIT=0`, empty Singular stderr
(`e3b0c442...` is SHA-256 of the empty string), and
`PASS_D1_SLOPE_UNIFORM_SOURCE_AND_CONTROLS`.  That `H!=1` is the synthetic
arc, not the D1 source.  It is syntax/source/control evidence only.

V1 (`SLOPE_UNIFORM_SMOKE_V1_NEGATIVE.md`, freeze member `5d1051c1...`) is
quarantined: nonempty `sat` diagnostics, invalid `KS[2]`/`HS[2]`, wrapper
that admitted process exit `0`.  The successor does not read those list
slots.  The wrapper refuses nonempty `singular.stderr` even when the
process exit is `0`.

A theorem harvest must also show `CONTROL_ONLY=0`.  The wrapper permits
either value; the printed marker is the fail-closed discriminator, not an
implicit default.

---

## Charge 9 — exact theorem firewall

**CONFIRMED** (exclusion); **CONFIRMED** (non-existence reading of `H!=1`
is refused); **CONFIRMED** (running/timeout/two-presentation substitution
is refused).

### `H=(1)` excludes strict arcs

Let `phi` be a homomorphism from the polynomial Rees ring to an integral
domain of formal or Puiseux series such that `phi` kills `I`,
`phi(q rho)!=0`, and the special fibre has `B(0)` not the origin.  If
`F∈K=I:(q rho)^infinity`, then `(q rho)^N F∈I` for some `N`, so
`phi(F)=0` by cancellation in a domain.  Setting `q=rho=0` therefore
yields a nonirrelevant zero of `H`.  Contrapositively, `H=(1)` admits no
such arc.

This argument does not require the arc to be rational, algebraic, or of
bounded slope.  Curve selection after a finite extension is the converse
direction (a nonunit `H` produces some Puiseux arc) and is not used for
the exclusion.  Nullstellensatz over an algebraic closure upgrades
`H=(1)` in `Q[...]` to emptiness over `C`.

Hypotheses that remain in force, and are not bugs: the arc lives in this
chart (`rho` regular), loads `(k,mu,nu)` are regular (cyclic D1: finite
`k`), and the leading projective point is nonzero.

### `H!=1` is only accessibility

A nonunit `H` is a closed projective-boundary point in the Zariski closure
of `D(q rho)∩V(I)`.  Curve selection supplies a Puiseux arc after a finite
extension.  That is not a rational map over `L(s)`, not the monodromy
filter `n=1` (overlap) / `n|2` (`c=0`) / `n|3` (`p=0`), not Taylor
polynomiality, not a D1 solution, and not JC2.  The common-cubic reduced
support can survive order zero for unbounded numerator `m`; survival of
`H` does not lift a cubic along `tau`.

### Endpoints that are not theorems

A still-running job, a timeout, a resource-inconclusive chart, agreement
of the `normal` and `B` presentations, or a `CONTROL_ONLY=1` smoke cannot
replace source review and the exact pair of markers

```text
CONTROL_ONLY=0
SLOPE_UNIFORM_H_IS_UNIT=0|1
```

together with `PASS_D1_SLOPE_UNIFORM_SOURCE_AND_CONTROLS` and empty
Singular stderr.  This review infers nothing from unfinished AWS work.

---

## Defects

### Mathematical

None.  The identities `R_l=D_l-delta_l`, the weight test, the character
`r_l=t^{2l mod 3} D_l`, `gamma_8=1+tau`, `Lambda=q^3 rho` as the strict
chart, interior-then-boundary saturation, and the unit-ideal exclusion
are correct.

### Source

None in the consumed compiler.  The three-load strip, the scaled
re-insertion, the eight-row ordinary rebuild, the common-cubic
automorphism, the polynomial coefficient ring, and the `sat` list API
repair are present as written.

### Deployment

None that falsify the licensed test.  Residual operational notes, not
repairs:

1. Two-containment uses `size(reduce(K,KSEQ))` rather than a generator-wise
   `reduce(f,G)==0` loop.  On the registered Box02 Singular 4.3.2 this
   branch printed `PASS_PRODUCT_SEQUENTIAL_SATURATION_AGREEMENT` in the
   V2 smoke.  A false disagreement would be fail-closed (no `H` harvest).
   A false agreement is not indicated by the API and is not a licensed
   substitute for the algebraic identity, which holds in any commutative
   ring.
2. The wrapper does not itself refuse `CONTROL_ONLY=1` as a theorem run.
   The printed `CONTROL_ONLY=` marker is mandatory at harvest.

### Scope

None that the artifacts overclaim.  The following are correctly fenced
and must not be collapsed into the unit test:

1. Slope `<=3`, finite-coefficient D1, and `q≡0` identically are outside
   this chart.
2. `p`/`c` charts cover the reviewed common-cubic projective radical, not
   an extra `p=c=0`, `X!=0` component, should one appear in a nonunit `H`.
3. Mason / exceptional support identifies reduced order-zero support only.
   It does not bound scheme thickness, normal deformations, or the
   numerator `m`.  The `k!=0` pivot is unavailable on this boundary
   because `q^{18} rho^6 k` vanishes there.
4. Dual-coordinate emission and ordinary-chart polynomials (7) are not
   required by the slope-uniform preregistration and cannot replace `H`.

---

## Strongest exact implication if a later source run reports `H=(1)`

Provided the harvest is global, `CONTROL_ONLY=0`, characteristic zero,
empty Singular stderr, and the registered pass markers, `H=(1)` excludes
every strict rational, formal, or Puiseux coefficient-infinity arc of
cyclic D1 with nonzero projective leading `B` and finite loads `(k,mu,nu)`,
uniformly on load space.  It does not exclude slope-three or bounded
sectors, does not prove polynomiality of a putative solution in the
finite-coefficient chart, and is not JC2.

## Strongest exact implication if a later source run reports `H!=1`

The projective strict-slope boundary of the interior closure is nonempty.
After a finite extension, some Puiseux arc of slope `>3` with nonzero
leading `B` is Zariski-accessible.  That is not a rational constant-field
section, not a D1 monodromy certificate, not Taylor polynomiality, not a
polynomial automorphism, and not JC2.  If the global job is instead
resource-inconclusive, the `p` and `c` charts cover only the reviewed
common-cubic radical, retain `c^2/p^3` and `Delta=0`, and still do not
promote a nonunit chart ideal to existence.

A timeout or a still-running job licenses neither implication.

---

## Fail-closed AWS replay (not executed here)

Anything that would require expanding tails, saturating, or re-hashing on
disk is already the licensed wrapper on a registered EC2 host:

```text
export JC2_AWS_TAG=max12_912_order3_d1_slope_uniform_<UTC>_<HOST>_global
export D1_SLOPE_RUN_DIR=/home/ubuntu/jobs/$JC2_AWS_TAG
export D1_SLOPE_COORDINATES=normal
export D1_SLOPE_CHART=global
export D1_SLOPE_CONTROL_ONLY=0
bash cases/max12_912_order3_d1_weighted_infinity_20260825/run_slope_uniform_aws.sh
```

Refuse any endpoint that lacks `PASS-D1-SLOPE-UNIFORM-COMPILER`,
`PASS_D1_SLOPE_UNIFORM_SOURCE_AND_CONTROLS`,
`COEFFICIENT_RING=POLYNOMIAL_Q_K_MU_NU_NO_LOCALIZATION`,
`CONTROL_ONLY=0`, a line `SLOPE_UNIFORM_H_IS_UNIT=[01]`, empty
`singular.stderr`, and a matching `SOURCE_CLOSURE_SLOPE_UNIFORM.sha256`
check.  Do not interpret `CONTROL_ONLY=1` or a timeout as `H`.

---

## Output report SHA-256

Digest of lines 1--501 inclusive (every byte above this section):

```text
67db045635b60ac77c5d7abef20a2d66e0aef7a5b73d68b1acbd6247508ac3d4
```

On-disk digest of this complete file is the `sha256sum` of the path after the trailer was written.
