# AS109 one-sided target floor six — prime/4 theorem-interface composition

Date: 2026-08-27T07:28Z  
Producer: Sol / OpenAI subagent lane  
Repo HEAD at launch: `418e413593120d19e15e6546eb50c985f4b1f038`  
Verdict: **PASS-AS109-ONE-SIDED-TARGET-FLOOR-SIX**

## 1. Exact theorem

Let `R=Z_109`, `K=Q_109`, and let

```text
P = x-x^109+109A,        Q = y+109B                 (1.1)
```

belong to `R[x,y]`. If `det J(P,Q)=1`, then, conditionally on this being an
exact integral polynomial AS109 lift,

```text
deg_y(Q) = deg_y(B) >= 6.                            (1.2)
```

The equality in (1.2) is part of the conclusion: once the actual degree is at
least two, the seed term `y` cannot affect the top coefficient and `109` is
not a zero-divisor.

This strengthens the reviewed one-sided AS-TRI floor from `2` to `6`. It is
independent of any support rectangle and holds at arbitrary finite `x`-degree.

## 2. History and scope checksum

Before doing arithmetic, I read the active portions of `PROGRESS.md`,
`APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`, the newest `notes.md` LIVE
STATE (`2026-08-27 05:30Z`), the Opus5 source-gauge proposal and its
cross-reviews, and every pre-existing non-prompt `xmodel` report whose name
contains `as109`. The exact 40-report census is frozen in

```text
cases/as109_one_sided_prime4_20260827/HISTORY.sha256
SHA-256 569ee6510a581d89be3528681abeb48e890c005b52ad6b19c803a34b964fb986
```

The 15 load-bearing theorem/queue inputs are separately frozen in

```text
cases/as109_one_sided_prime4_20260827/INPUTS.sha256
SHA-256 41d155803dd1bae23f060be5719152352247afd41b4098183a7b00083681ceb6
```

The live top-level snapshot was:

```text
PROGRESS.md      edc584f495802325647c24ffa96333ebf7a06d8c45de89eb95df193cba0d507c
APPROACHES.md    e4235cdf73c02ac4da265d4bd413d48d3f8755a4b59db8023065144e657d2006
AUDIT.md         10f7bd3f45a295a09a1689aa9d678cab918a03387acaae6ccfd5cb459959ffea
COORDINATION.md  d5ca2421fdaaf7fac2f142e3fb0f96bf58c181047f092c3434a970d50dcde812
notes.md         5fc1858142ac889d55ab4035a5733f6de03533fc2d725ca14def54d56929c540
```

The newest LIVE STATE queued an AS109 `deg_y Q=2` arithmetic-Newton corner.
That rectangle is not open: the 2018 partial-`y` theorem already decides it
without a support or valuation cap. No prior report had composed that theorem
with AS109 Hensel noninjectivity to record the stronger one-sided floor (1.2).

## 3. Exact source interface and custody

The source is Vered Moskowicz, *A variation on Magnus' theorem and its
generalizations*, arXiv:1810.08202v2 (2018), Theorem 2.7. This is **not** the
separate 2024 prime field-extension-degree paper whose proposed proof is
quarantined elsewhere in the campaign.

For a characteristic-zero Keller pair

```text
p=a_n(x)y^n+... ,        q=c_r(x)y^r+... ,
A0=gcd(n,deg_x a_n),     C0=gcd(r,deg_x c_r),          (3.1)
```

Theorem 2.7 says that the pair is a polynomial automorphism if either `A0` or
`C0` belongs to `{1,4} union primes`. There are no auxiliary `uv != 0` or
unaligned-leading hypotheses in Theorem 2.7; those belong to earlier theorems
in the paper. The paper works over an arbitrary characteristic-zero field, so
`K=Q_109` is directly in scope.

The constant-leading case is explicit. If `c_r` is constant, then
`deg_x(c_r)=0` and the source uses `gcd(r,0)=r`; its proof treats the `u=0` or
`v=0` branch separately. The final display in that branch has a harmless
`gf(x)`/`gf(y)` typographical slip, but the preceding displayed degree formula
and the invoked coordinate are unambiguous and the theorem statement is
unchanged.

Primary-source custody was rechecked during this lane. A fresh download from
`https://export.arxiv.org/e-print/1810.08202v2` had SHA-256

```text
ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419,
```

exactly matching the prior source audit. The load-bearing campaign custody is

```text
xmodel/as109-partial-y-history-stop-20260824.md
  6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe
xmodel/as109-partial-y-history-review-grok-20260824.md
  f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd
```

The review independently checked the arbitrary-characteristic-zero field
scope, descent where older total-degree inputs are stated over `C`, and the
constant-leading convention.

## 4. Proof of the one-sided floor

Let `n=deg_y Q` and write `q_n(x)` for the nonzero leading coefficient.
The seed congruence already forces `n>=1`; independently, reviewed AS-TRI
forces `n>=2`.

Suppose `n<=5`. For `n=1`, Moskowicz's invariant is
`C0=gcd(1,deg_x q_1)=1`. For each remaining degree the complete routing is:

| `n` | possible `C0=gcd(n,deg_x q_n)` | Theorem 2.7 route |
|---:|---|---|
| `2` | `1,2` | `1` or prime |
| `3` | `1,3` | `1` or prime |
| `4` | `1,2,4` | `1`, prime, or `4` |
| `5` | `1,5` | `1` or prime |

This includes `deg_x q_n=0`, because then `C0=n`. Thus Theorem 2.7 makes
`(P,Q)` a polynomial automorphism over `K` for every `1<=n<=5`.

The separately reviewed AS109 Hensel theorem says that an exact lift (1.1)
maps each of the 109 source residue balls above `(a,b)` bijectively onto the
same target ball above `(0,b)`. Hence every such exact lift is noninjective
over `K`. An automorphism is injective, a contradiction. Therefore `n>=6`,
which proves (1.2).

The Hensel custody consumed here is:

```text
xmodel/as109-support-gate-20260824.md
  b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5
xmodel/as109-support-review-grok-20260824.md
  1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8
xmodel/as109-support-gate-20260824-erratum.md
  ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb
xmodel/as109-carry-erratum-review-grok-20260824.md
  1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212
```

The carry erratum does not weaken the exact residue-ball conclusion.

## 5. The first honest residual corner is `n=6`

For `n=6`, the invariant `C0=gcd(6,deg_x q_6)` can be `1,2,3,6`.
Theorem 2.7 covers the first three, so a nonautomorphic exact AS109 lift must
satisfy

```text
6 | deg_x(q_6),                                      (5.1)
```

including the constant-leading case `deg_x(q_6)=0`.

Let `m=deg_y P`. The reviewed maximum-eleven theorem plus Hensel gives
`m>=12` when `n=6`. The reviewed partial-`y` source-shear theorem covers
`gcd(m,6)<=2`, hence a survivor must also have

```text
gcd(m,6) in {3,6},        equivalently 3 | m.         (5.2)
```

Write `d=gcd(m,6)` and use the standard leading common core

```text
p_m=alpha h^(m/d),        q_6=beta h^(6/d),
H=deg_x h.                                           (5.3)
```

Then (5.1) becomes the exact two-case residual:

```text
d=3  =>  3 | H,
d=6  =>  6 | H.                                     (5.4)
```

Consequently the smallest currently honest arithmetic-Newton target is not a
generic `n=2` row. It is the `n=6` stratum

```text
m>=12,  3|m,  6|deg_x(q_6),  and (5.4).              (5.5)
```

This is the maximal immediate one-sided floor supported by the charged
theorems. The exact determinant-one automorphism

```text
u=x+y,  v=y+u^6,  (P,Q)=(u+v^2,v)
```

has actual `y`-degrees `(12,6)` and constant top coefficients. It is not an
AS109 lift, but it is a useful scope control: the numerical residual
conditions themselves are compatible with the Keller equation, so no claim
`deg_y Q>=7` is available from this composition.

## 6. Source gauge audit

For `tau in R`, the exact source translation `(x,y)->(x+tau,y)` acts on the
AS109 lift set by

```text
A^tau = A(x+tau,y) + (tau-tau^109)/109
        - sum_{i=1}^{108} [binom(109,i)/109] tau^(109-i) x^i,
B^tau = B(x+tau,y).                                  (6.1)
```

It is integral, additive, free, determinant-preserving, and seed-preserving.
It preserves both actual `y`-degrees and the `x`-degree of each nonzero top
`y`-coefficient. In particular, it cannot move a residual satisfying (5.1)
out of that residual.

If `deg_x A<=108`, then for `phi(A)=[x^108 y^0]A`,

```text
phi(A^tau)=phi(A)-tau,
```

so the unique section is `tau=phi(A)` and has normalized equation
`[x^108 y^0]A=0`. No automatic section is claimed for `deg_x A>108`; there
the gauge equation receives terms from higher `x`-coefficients. The proof of
(1.2) does not consume the gauge or its degree cap. It is only a safe
preprocessor for a future bounded enumeration on the residual (5.5).

## 7. Disposition of the queued `n=2` job

The smallest determinate exact claim for that lane is

```text
No exact integral polynomial AS109 lift has deg_y Q=2. (7.1)
```

Section 4 proves (7.1) at arbitrary support. Therefore both advertised
outcomes of a bounded Newton calculation are already interpreted:

- an empty bounded system would be a strict subset of (7.1), hence a history
  duplicate;
- a survivor would not be an exact lift unless it exposed an error in a
  charged theorem interface; ordinarily it would diagnose missing equations,
  truncation, or insufficient saturation in the bounded model.

Stop rule: **STOP-AS-HISTORY-DUPLICATE**. Do not enumerate an `n=2`, `n=3`,
`n=4`, or `n=5` support rectangle. Start future arithmetic only at (5.5), and
stop there too unless the model is exact enough that either emptiness or a
survivor changes the unrestricted AS109 state.

## 8. Fail-closed replay

Run:

```text
python3 cases/as109_one_sided_prime4_20260827/replay.py
```

Replay SHA-256:

```text
4413482ee6d518d85abaa85c609f1f3421c168496c2d40b6b9a9340a2d4ff73d
```

It fails on any missing or hash-changed frozen report, checks the exact gauge
formula/group law/section and degree invariance, exhausts the small invariant
routing, translates the `n=6` common-core conditions, and verifies the sparse
determinant-one `(12,6)` control. Its terminal payload is:

```text
verdict = PASS-AS109-ONE-SIDED-TARGET-FLOOR-SIX
history_reports_pinned = 40
excluded_actual_target_y_degrees = [1,2,3,4,5]
first_not_excluded = 6
newton_n2_job = STOP-AS-HISTORY-DUPLICATE
next_arithmetic_corner = n=6 on the residual invariant stratum
```

No Singular process, support enumeration, heavy local algebra, or AWS instance
was needed. This was a theorem-interface and exact sparse-arithmetic lane.

## 9. Scope firewall and review request

This report does **not** prove that an AS109 lift exists or does not exist. It
does not bound `x`-support, route every `n=6` pair, construct a marked
collision, decide any other characteristic-`109` seed, prove a
characteristic-zero counterexample, or decide JC2. The conclusion is
conditional on an exact integral polynomial lift in the displayed AS109
coordinates and uses partial degree, which is not invariant under arbitrary
source automorphisms.

Rank impact: the one-sided target correction floor is now `deg_y B>=6`, while
the separately reviewed two-sided floor remains
`max(deg_y A,deg_y B)>=12`. Thus all target branches `deg_y B<=5` are removed
even when `deg_y A` is unbounded, and the first residual target degree six
automatically has `deg_y A=deg_y P>=12` plus (5.1)--(5.4).

A hostile reviewer should recheck only these load-bearing interfaces:

1. Moskowicz Theorem 2.7's exact `{1,4} union primes` invariant and its
   constant-leading branch;
2. arbitrary-characteristic-zero applicability to `Q_109`;
3. the reviewed 109-ball noninjectivity implication;
4. the finite routing for `n=2,3,4,5` and the residual classification at
   `n=6`.

