# D3 sectioned one-support: clean-infinity classification and AWS HB-jet packet

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, sectioned one-support family lane  
Frozen basis: `f91e751041a0f926b6981c9bfe33aa1665c2c226`  
Lifecycle: **EXACT CONDITIONAL CLEAN-INFINITY REDUCTION / UNLAUNCHED AWS SCREEN / REVIEW REQUIRED**

## 0. Maximum-safe result

Inside the fixed sectioned two-`(1,1)` CFS chart `P18` of

```text
xmodel/bd-a2-d3-sectioned-one-support-universal-ramification-strata-sol56-20260830.md,
```

the clean-infinity part of an actual proper cubic block is much more rigid
than the earlier length-27 condition alone records.

1. The infinity curve is the union of exactly three smooth `(1,1)` sections.
   They meet at the unique source point over the unique target-infinity point,
   and every pair has intersection multiplicity exactly two there.
2. If that point lies on the distinguished line `D={y=0}`, the `P18` cubic
   has a whole target line of triple-root fibres.  This violates the charged
   actual-block condition `S0=empty`.  Hence the point lies off `D`.
3. Residual coordinate changes preserving the chart put the point at
   `[x:y:z]=[1:1:0]`.  The common coefficient root is finite.  After scaling
   and permuting the three sections, their boundary polynomial is

   ```text
   P=product_delta ((t-tau)x+(kappa+delta(t-tau))(y-x)),
   delta in {d1,d2,1},                                  (0.1)
   kappa(d1-d2)(d1-1)(d2-1) != 0.
   ```

   It satisfies the exact identity

   ```text
   Disc_t(P)=kappa^6(d1-d2)^2(d1-1)^2(d2-1)^2(x-y)^12. (0.2)
   ```

4. The restriction map from `P18` has a four-dimensional kernel, and the
   lifts of (0.1) form its corresponding affine fibre.  Thus the normalized
   clean-boundary slice has eight affine parameters

   ```text
   tau,kappa,d1,d2,h,pv,qv,rv.                          (0.3)
   ```

5. At the clean point, the three pulled-back twisted-cubic minors localize to
   a two-equation Hilbert--Burch complete intersection `(U,V)`.  On the open
   chart `U_Z != 0`, the condition that the entire universal length 27 be at
   this point is an explicit finite formal-jet ideal.  The packet below emits
   that ideal for prefixes `N=2,...,27` and runs it fail-closed on AWS.

No computation was launched for this report.  A unit result at a prefix would
close only this normalized `U_Z != 0` clean-infinity shard, after exact
certificate and different-engine review.  It would not close the full P18
chart, other CFS charts, the non-transverse `U_Z=0` shard, a degenerate
infinity row, or the sectioned one-support row.

## 1. Why clean infinity has only one normalization type

Let `C_inf -> L_inf=P1` be the degree-three infinity cover.  In the clean row
it is generically reduced.  Its normalization components are rational by the
actual first-leg boundary-forest theorem.  All branching is over the single
target point at infinity: away from it, two coefficient roots cannot meet.

If a normalization component had target degree `f>=2`, Riemann--Hurwitz would
give total ramification `2f-2`.  A single fibre can contribute at most
`f-1`, a contradiction.  Every component therefore has target degree one,
so there are exactly three sections.  Connectedness and the unique branch
value force all three to pass through one physical point: a degree-one
section has only one point above that target value.

Write their coefficient-root degrees as `d_i`.  Since `C_inf` has class
`(3,3)`,

```text
d_1+d_2+d_3=3,
C_i.C_j=d_i+d_j.                                      (1.1)
```

No two `d_i` can vanish because the sections meet.  The only unordered
possibilities are `(1,1,1)` and `(0,1,2)`.  The second is impossible.  Send
the degree-zero section to root coordinate zero.  The degree-one and
degree-two sections then vanish to orders one and two at the common point,
because all their intersections with the constant section are concentrated
there.  Their difference has order one, contradicting the required mutual
intersection `1+2=3`.  Hence

```text
(d_1,d_2,d_3)=(1,1,1),       C_i.C_j=2.               (1.2)
```

This is a topology-to-equations reduction; it uses the already charged
actual-block boundary forest and one-target-point inputs.  It is not a new
standalone proof of either input.

## 2. Normalized boundary slice in P18

The P18 conditions are invariant under `y -> alpha*y` and
`X=x+tz -> X+beta*y`.  These transformations preserve `D={y=0}`, the moving
section, and the two equal-weight drops, and act transitively on
`L_inf\D`.  Thus an allowed clean point off `D` may be placed at
`[1:1:0]`.

If the clean point were on `D`, the missing `t^3x^3` P18 coefficient forces
the common coefficient root to be `t=infinity`.  The three contact-two
bilinear factors then have boundary form

```text
product_i (x+(kappa*t+delta_i)y).
```

Matching the P18 restriction sets the two other pure-`x` coefficients to
zero.  On the whole target line `y=0`, the full cubic becomes a scalar
multiple of `(x+tz)^3`.  That is a divisorial triple-root locus meeting the
affine target, contrary to `S0=empty`.  Therefore the clean point is off `D`.
A common root at `t=infinity` off `D` is also impossible: the leading
`t^3` coefficient would be the cube of the line vanishing at the clean
point, while every P18 leading coefficient is divisible by `y`.

For a finite common root, three degree-one root maps with common value and
first derivative have, after individual factor scaling, the form (0.1).
The missing `t^3x^3` coefficient says

```text
product_i(1-delta_i)=0.
```

The deltas are distinct by (1.2), so precisely one equals one.  This proves
the normal form after relabelling.  Taking pairwise resultants of the three
linear-in-`t` factors gives (0.2).

Let `[m]P` denote the coefficient of monomial `m` in (0.1), and let
`a0,...,a18` be coefficients in the frozen P18 basis.  The lift is

```text
a0 =[y^3]P       a1 =[xy^2]P       a2 =[t y^3]P
a3 =[txy^2]P     a4 =[x^2y]P       a5 =pv
a6 =[t^2y^3]P    a7 =h              a8 =[t^2xy^2]P
a9 =[t^2x^2y]P   a10=[x^3]P         a11=h-[tx^2y]P
a12=qv           a13=[t^3y^3]P     a14=[tx^3]P
a15=rv           a16=[t^3xy^2]P    a17=[t^2x^3]P
a18=[t^3x^2y]P.                                      (2.1)
```

The four kernel directions are `B5`, `B12`, `B15`, and `B7+B11`.  The
generator checks both `F|z=0=P` and `F(t;-t,0,1)=0` with explicit exceptions,
not Python assertions.

## 3. Local Hilbert--Burch equations

At `x=1,y=1+Y,z=Z`, write the raw binary cubic as

```text
F=c0+c1*t+c2*t^2+c3*t^3.
```

The three scaled minors of the twisted-cubic Hilbert--Burch matrix are

```text
H0=c1^2-3c0c2,
H1=c1c2-9c0c3,
H2=c2^2-3c1c3,                                       (3.1)
```

with exact syzygies

```text
3c0 H2-c1 H1+c2 H0=0,
c1 H2-c2 H1+3c3 H0=0.                                (3.2)
```

At `(Y,Z)=(0,0)`, equation (0.1) gives `F=(t-tau)^3` and `c3=1`.  Hence
`3c3` is a unit, and by (3.2) all three minors generate the same completed
local ideal as

```text
U=-H2=3c1c3-c2^2,
V=-3c3 H1+2c2 H2
 =27c0c3^2-9c1c2c3+2c2^3.                            (3.3)
```

Along `Z=0`, one has `U in (Y^4)` and `V in (Y^6)`; generically the orders
are four and six.  Special equianharmonic parameter values can raise one of
these two orders, so the computation does not invert their leading
coefficients.  It inverts only

```text
Omega=kappa(d1-d2)(d1-1)(d2-1) U_Z(0,0).             (3.4)
```

## 4. Tractable length-N target

On `Omega != 0`, formal implicit function gives a unique series `Z(Y)` with
`U(Y,Z(Y))=0`.  For `2<=N<=27`, introduce

```text
Z_<N(Y)=z1 Y+...+z_(N-1)Y^(N-1).                      (4.1)
```

The emitted ideal is

```text
J_N=( [Y^j]U(Y,Z_<N), [Y^j]V(Y,Z_<N) : 1<=j<N,
      oinv*Omega-1 ).                                 (4.2)
```

There are `8+(N-1)+1` variables and `2(N-1)+1` displayed generators.  The
`U` equations are Hensel-triangular: their new coefficient is always
`U_Z(0,0) z_j`.  Consequently (4.2) is equivalent to local intersection
length at least `N`, not merely a necessary Taylor shadow.

For an actual clean proper-block occurrence, there is no affine triple-root
point and the clean boundary is not mapped into the twisted cubic.  The
global refined pullback degree is 27.  Thus an actual occurrence must solve
`J_27`; its local length is then exactly 27 and no residual triple-root point
remains.  Solutions of `J_27` in the raw P18 slice can be extraneous because
finite flatness, exact level, additive terminal type, normality, actual
morphicity, and the separate genus-28 gate have intentionally not yet been
imposed.

## 5. Frozen packet and desk replay

Files:

```text
ops/d3_one_support_clean_hb_generate.py
ops/aws_d3_one_support_clean_hb_run.sh
```

Frozen pre-seal file facts:

```text
generator bytes                         15265
generator SHA-256                       7ef8d1d048c72d2ab7f91821b906fdbd2633d1749142ada5a6307e49801b2f48
AWS runner bytes                         9554
AWS runner SHA-256                       e4fad695687a3b7743436292481f873e4f0eb3404381bd97d5523726d07b51f8
```

The bounded replay is

```bash
python3 -m py_compile ops/d3_one_support_clean_hb_generate.py
bash -n ops/aws_d3_one_support_clean_hb_run.sh
python3 ops/d3_one_support_clean_hb_generate.py --self-test
python3 -O ops/d3_one_support_clean_hb_generate.py --self-test
python3 -OO ops/d3_one_support_clean_hb_generate.py --self-test
```

All three self-test stdout streams are byte-identical, with SHA-256

```text
fc80bb406ce8755af035adf86bd7100e14c74f541db27764aaa924ef01412061.
```

The exact JSON payload records the boundary, coefficient-lift and
discriminant hashes, both Hilbert--Burch syzygies, the length-27 positive
control `Y^27`, and rejection of the off-by-one mutation `Y^26`.

The source mutation

```bash
python3 ops/d3_one_support_clean_hb_generate.py \
  --self-test --mutate-boundary-lift
```

reverses the unique `B7-B11` cancellation.  Ordinary, `-O`, and `-OO` all
exit one, emit empty stdout (SHA-256 `e3b0c442...b855`), and emit identical
stderr with SHA-256

```text
415e271805890a904f6f9cf84ec0afd7862a2b417a15ffa8725e02d89d7e76be.
```

A local invocation of the AWS runner with otherwise valid arguments exits
`125` before allocating its job root.  Its stdout is empty and its stderr has
SHA-256

```text
0022ea2e819d5cce6f8bb655aad7d62bde344e1f0238af4b8c280a55ea38f6c4.
```

No full jet input is generated by `--self-test`.  In accordance with
`ops/FLEET.md`, even uncertain generator expansion and every Singular run
belong on AWS.

## 6. AWS launch ladder

The hardened runner refuses non-Linux and non-EC2 hosts, checks the exact
instance id and frozen generator hash, requires a registered tag and a fresh
job root, runs the self-test first, caps virtual memory, limits generator
time to two hours and Singular time to at most twelve hours, and records
versions, input/result hashes, `/usr/bin/time -v`, verdict markers, and a
complete evidence manifest.  Its output is screening evidence; it never
labels a modular unit as a characteristic-zero theorem.

Before using any listed node, audit its live processes and output custody.
Do not stop or repurpose a node merely to run this packet.  On an SSH timeout,
run `ops/sg_autoupdate.sh` once before further diagnosis.

Recommended ladder:

| stage | hosts | lanes | cap per lane | decision |
|---|---|---|---:|---|
| 1 | audited-idle `r6a,r6b,r6c` | `N=8`, primes `32003,32009,32027`, `slimgb` | `110000000` KiB, 6 h | syntax/performance and low-prefix screen |
| 2 | same 128-GiB nodes | surviving primes at `N=12,16` | `110000000` KiB, 12 h | stop a prime after certified unit or resource failure |
| 3 | audited-idle `r6d` | `N=20`, one modular and then `p=0` if warranted | `220000000` KiB, 12 h | distinguish persistent component from delayed obstruction |
| 4 | audited-idle `Box03` only if needed | `N=24,27`, modular then exact | `450000000` KiB, 12 h | final transverse-shard screen |

Example stage command after copying both packet files to a fresh remote stage
directory and independently checking their hashes:

```bash
nohup bash aws_d3_one_support_clean_hb_run.sh \
  /home/ubuntu/jobs/d3_one_support_clean_hb_p32003_n8_20260830 \
  d3_clean_hb_p32003_n8_20260830 \
  i-02cb2b4a379ffcc64 32003 8 slimgb 110000000 21600 \
  7ef8d1d048c72d2ab7f91821b906fdbd2633d1749142ada5a6307e49801b2f48 \
  > launch.stdout 2> launch.stderr &
```

The instance id above is `r6a`; resolve its current IP from the AWS control
plane rather than trusting the historical address in `FLEET.md`.  Give every
lane a distinct stage directory, job root, and tag.  Ship files with `scp`,
not a long inline SSH payload.

## 7. Pre-registered interpretation and stop certificates

Every run must preserve `EVIDENCE.sha256`, `run/run.meta`, `input.sing`, both
generator streams, both Singular streams, the self-test streams, and the two
copied payload files.

- `FAILED_CLOSED_SELFTEST` or `FAILED_CLOSED_GENERATOR`: stop.  This is a
  source/environment failure, not mathematical evidence.
- Timeout, OOM, missing marker, nonzero Singular exit, or
  `FAILED_CLOSED_OR_INCONCLUSIVE`: stop that lane.  Do not infer survival or
  emptiness.
- `D3_CLEAN_HB_SCREEN=UNIT` in positive characteristic (metadata state
  `MODULAR_SCREEN_UNIT`): useful prime-specific screening only.  It is not a
  `Q` verdict because affine inverse variables can escape reduction and no
  effective good-prime bound has been proved.
- `D3_CLEAN_HB_SCREEN=NONUNIT` in positive characteristic (metadata state
  `MODULAR_SCREEN_NONUNIT`): a special-fibre survivor only.  It neither
  produces a characteristic-zero occurrence nor licenses a higher prefix by
  itself.
- Exact `p=0`, `N<27`, `SCREEN=UNIT`: freeze the run, reproduce with the
  other engine, export and independently replay an exact identity
  `1=sum h_i f_i`.  Once certified, this closes the full `N=27` transverse
  shard because length at least 27 implies length at least `N`.
- Exact `p=0`, `SCREEN=UNIT` at `N=27`: same certificate requirement.  Do not
  promote the runner's `EXACT_SCREEN_UNIT_CERTIFICATE_REQUIRED` marker by
  itself.
- Exact `p=0`, `SCREEN=NONUNIT`: freeze the basis and extract a component or
  geometric point.  Then impose the omitted finite-flat, exact-level,
  additive, normality, no-affine-triple, actual-morphic and genus-28 gates.
  A raw jet survivor is not an occurrence.
- If all tractable prefixes survive but the job grows beyond the registered
  caps, stop and exploit the triangular `U` equations symbolically before
  adding RAM.  Do not launch a blind larger ansatz.

The complementary `U_Z=0` locus is intentionally excluded by (3.4).  Its
next target is the first nonzero `Z`-jet of `(U,V)`, split by the rank of
their linear and quadratic normal parts.  No verdict from this packet applies
to that higher-embedding-dimension branch.

## 8. Firewalls

- This packet is conditional on the charged rational-forest, unique
  attachment and one-target-point theorems.
- The clean `(1,1)^3` classification is family-wide for actual clean cubic
  blocks; the eight-parameter equations are only the fixed P18 chart after
  its residual normalization.
- The boundary polynomial and length-27 TC gate are necessary conditions,
  not sufficient incidence surfaces and not proper first-leg morphisms.
- A Singular unit without a serialized exact cofactor identity is screening
  evidence, not theorem-tier emptiness.
- No result here addresses the three degenerate infinity rows, other CFS
  sequences, the primitive/no-proper-block horn, or JC2 as a whole.
- No heavy computation ran locally or remotely in producing this artifact.

The maximum-safe advance is therefore an exact clean-boundary classification,
an explicit eight-parameter P18 lift, a localized Hilbert--Burch length-27
ideal with honest non-transverse firewall, and a frozen fail-closed AWS launch
packet.  The row remains open pending the actual AWS screen and review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15966`.
- Body SHA-256:
  `bbdbb101132fc6d09452bf43e67520c5354c5fbff3a13aae5b7f8d5c29cdc168`.
- Frozen basis: `f91e751041a0f926b6981c9bfe33aa1665c2c226`.
