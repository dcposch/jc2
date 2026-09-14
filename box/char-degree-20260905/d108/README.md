# D108 characteristic-degree implementation

Coverage correction discovered during this lane: the frozen chart's mean-zero
quadratic `pi²-c` is not a proved complete gauge. The original schedules
remain exact reproductions of that frozen chart, and any kill there would be
conditional on this extra restriction. `meanfree_stage.py` and
`run_meanfree_schedule.sh` additionally run stages0–8 with the arbitrary
quadratic `(pi-minor_mean)²-c`, retaining `minor_mean` as a scalar variable
and leaving the arc unchanged. These supplementary runs repair that coverage
gap; `c!=0` means distinct roots. The h3 incidence rows add `-2*minor_mean`
at local coefficient `(8,1)` and `minor_mean²` at `(8,0)`, and the complete
leading F/G targets become this quadratic's powers12 and8. Their necessity
and the failure of the old mean gauge are audited in the parent lane's
`d108-mean-coverage-control` artifacts. No existing engine or ledger file is
edited. The supplementary metadata names the free mean explicitly.

This directory augments an immutable copy of
`box/d108-rekill-20260905/work/rekill_engine.py`. Its source degree pair is
108,72; the auxiliary h2 has degree36 and the characteristic T2 has actual
y-degree63. The characteristic constants are **all five** `target_a` through
`target_e`. `leader63` is a scalar variable, localized by `Z63*leader63-1`.
The source minor localization `Zc*c-1` remains present. `jet0` is free.

No ledger, original engine, Lean file, or ideation file is edited. The inherited
gauge ledger is embedded in every source-state JSON. The engine's corrected
leading-pole subtraction is copied verbatim and used by all scheduled rows.

`char_degree_driver.py` retains every original stage row and every source
coordinate through rational pivots. It also imposes the proved characteristic
consequences B1=-b/3 and A2=(3B2+a)/2. Its `backend_script` and `emit_maps`
functions expose a reusable physical-coordinate exact-Q implementation.
Physical source polynomials are completed at their full finite degrees; a
stage-8 t-jet is never padded with zeros to manufacture a characteristic row.

`normalized_backend.py` is the primary complete implementation. It makes the
same divisions in the original t,z coordinates, avoiding expansion of
z=y/x-1. It additionally imposes the printed total-degree and top-form
conditions from Moh Proposition4.5, audited in the parent lane's source
notes. Every leader/face is emitted as **coefficient minus target**, with the
target scalar retained and inverted by its own variable.

Write the depressed variables

```
H=h-b/6, v=D+a/3+b^2/18,
V=C-bD/4+ab/12+b^3/54-c/2,
A=a+b^2/4, d0=d+bc/2,
p=d0-A^2/3, q=e+c^2/4-A*d0/3+2*A^3/27.
```

Perform exact monic-y divisions

```
v^2=UH+R, vU=PH+R1, vR=Q1H+R2, U^2=WH+R3.
```

All remainders have y-degree below36. The complete characteristic conditions
are equivalent to the coefficient rows

```
V=3U/8,
upper=3R/4+p-P/8=0,
digit=Q1-R1/8-9W/64,
low=R2-9R3/64+pv+q,
T2=digit*H+low.
```

For the total-degree/top-form version, digit has degree at most27 and top
form `leader63*y^6*(y-x)^21`; low has degree at most62. Thus T2 has degree63
and top form `leader63*y^14*(y-x)^49`. This includes its constant nonzero
y63 coefficient. The lower target coefficient e remains a free constant:
an upper-degree condition does not silently set the constant term to zero.

The normalized degrees are H36, v71, V107, U106, R142, P141, R1/Q1177,
R2213, W176, R3212. Accordingly the normalized digit's depth150 coefficients
subtract `leader63*z^21*(1+z)^6`, all depths below150 vanish, and the
normalized low polynomial vanishes below depth151. These depths are shifted
normalizers after proved cancellations; the original degree216 normalizer
places the actual y63 scalar coefficient at depth153.

`backend_controls.py` and `normalized_controls.py` run the actual emitted CAS
backend on both a forbidden cone point (UNIT) and an attained-degree control
(NONUNIT), and require wrapper outputs `(0,1)`. The attained control is
F=s^6+3s^3/2+3/8, G=s^4+s, with T2=-s^3/8-9/64. These are control polynomials,
not D108 branch witnesses. The parent lane also independently audited the
normalized map, wrong-face rejection, and low-term cutoffs.

The initial physical diagnostic serializer was rejected by these controls:
Singular interprets `x^2/3` ambiguously. It was replaced by a recursive
serializer with rational factors in parentheses and all literal formulas
were repaired. The reserved identifier `QQ` was also replaced. No output
with a parser diagnostic is accepted as a decision. The rejected startup
attempts are quarantined and are not primary schedule evidence.

`run_normalized_schedule.sh` runs stages0–8 with12GiB per process;
`run_normalized_m24_schedule.sh` repeats with24GiB and distinct `_m24` tags.
Each Singular call is capped at1200 seconds. A halt before `BEGIN_RESULT` is
recorded as compute/memory bounded OPEN; it is neither a unit nor a survivor.

`native_flint_stage.py` is a further bounded exact-Q attempt, using a smaller
active polynomial ring and native FLINT monic division before emitting every
coefficient row into the full declared Singular ring. With `--early-D` it
uses the separately proved leading-band radical consequences: D coefficients
at r<=30 vanish, D31=tau*z31*(1+z)^4, C at r<=62 vanishes, and
C63=3*tau^2*z34/8. Tau is its actual existing leading coefficient and may be
zero; no component or nonzero branch is discarded. All original source rows
and full characteristic rows are still retained. The parent lane's
`front-band-lemma.md` and controls justify these extra equations.

`translation_backend.py` implements an additional **invertible coefficient
map**, not a gauge slice. It keeps `jet0` and every old h/minor parameter,
keeps the old source pole/J rows, and computes the characteristic identity
using h'=T(h), D'=T(D), C'=T(C), where
`T(P)(x,y)=P(x+jet0,y+jet0)`. In normalized coordinates a degree-N monomial
`t^r*z^q` maps to `t^r*z^q*(1+jet0*t)^(N-r-q)`.

The D/C source spaces are invariant: D2 weight increases by4l; a new D1
moment `(W,k)` uses old weight `W-4l` and q-moments of degree at most k+l,
where the old threshold supplies moments through k+8l. The inverse uses
`-jet0`. The leading-band graph is invariant as well. Because every retained
stage≤8 pole/J row depends only on the old h, the D'/C' coefficients may be
renamed as independent coordinates in these same spaces while the old
source equations remain in place. The JSON records explicit old-generator
images in the new ring and mechanically checks both full polynomial images
and every basis roundtrip. It does not transform or silently pin the minor
at-level mean. The h t1 band disappears, but jet0 remains free.

The generic source stage8 emitter and the optimized pullback emitter were
also compared mechanically: all1429 raw rows have the same SHA-256
`91d0ac274ae21ba8f70c921fc43b29084afbed08fdd38716e97bc2a09e9fb82b`.
After the first two characteristic consequences every outer coefficient is
absent through t12, so F=h^3 and G=h^2 in those bands. Computing the minor
pullback before its square/cube and retaining each J label with value0
reduces source emission from593.569s to63.553s without changing a row.

The stronger field consequences are enabled by `strong_front=True` and are
recorded in a separate radical ledger, with no coordinate normalization:
stage0 has D_r=0 for r<=32 and C_r=0 for r<=66; stages1–8 have D_r=0 for
r<=33 and C_r=0 for r<=68. The proofs and actual frozen-source checks are in
`../cubic-front-improvement.md` and `../d108-stage-front-audit.md`. Original
source rows and complete characteristic rows are retained after these
consequences are solved by rational pivots.

The primary monic-division schedules encountered memory/time bounds before
the first quotient. A native FLINT variant also encountered explicit
allocation failures. Singular can restart after such an allocation failure
and continue on an incomplete ideal. `finalize_native.py` records the
D108 restart as `CAS_AFTER_FAILURE_REJECTED`; the later row count/GB marker
is never accepted as evidence for the full characteristic ideal.

`coefficient_circuit_backend_v2.py` is a self-contained production alternative
that emits the complete ideal without expanding products in all parameter
variables. It introduces a fresh scalar coefficient for every nonconstant
coefficient of H, v, U, the low-z remainder R, H², and vU, retaining a monic
polynomial graph equation for each. Every coefficient of v²-UH above the
remainder's z-degree bound is imposed. The exact characteristic identity is
then emitted coefficientwise through depth151, with the full target
`leader63*t^151*z^49*(1+z)^14` subtracted. The graph variables add no choice:
projection and evaluation are inverse polynomial maps. The five original
target constants and both nonzero localizers remain in the declared ring.

The stage0–8 circuit schedule uses the proved stronger front rows and the
invertible translation map, retaining jet0 as a free old coordinate. Stage8
runs at48GiB/1800s; stages0–7 run two parallel16GiB processes/900s each.
The preceding `coefficient_circuit_backend_v1.py` snapshot is the exact
version used for those runs; v2 additionally asserts generator distinctness
and handles an identically zero remainder in the generic cutoff. Both use
the same polynomial identities, inclusive target depth, and strict result
acceptance. An accepted result requires process return0, all rows parsed,
complete result markers, wrapper controls exactly0 and1, no parser/CAS
diagnostics, and an unchanged script hash. `NONUNIT_NOT_POINT` is never a
claimed branch survivor. A point or a validated full unit certificate is
required for the stronger campaign gate.

A further **selected** variant, kept outside both complete schedules, uses
`meanfree_stage_v2.py` with `jet0free=False` only after the free-mean repair.
The polynomial affine translation q=old jet0 transports
`jet2'=jet2-q*jet1`, `minor_mean'=minor_mean+q²*jet1-2q*jet2`, with c fixed;
the new jet0 is zero. The inverse from the slice plus an arbitrary scalar s
restores `jet0=s`, `jet2=jet2'+s*jet1'`, and
`minor_mean=minor_mean'+s²*jet1'+2s*jet2'`. The parent lane's
`d108-meanfree-translation-theorem.md` and exact source controls establish
coverage, major and outer graph transport, and the complete finite pole
prefix. This gauge is valid for the repaired chart; it does not justify a
jet0 pin in the old even-face chart.

Two isolated selected cases use SLIMGB at32GiB/1200s: the full mean-free
stage8 chart, and its proved jet0 slice. The variant changes only
`std(I)` to `slimgb(I)` in the main ideal computation, with all ring,
equation, target, and control text unchanged. Their guarded runners and
source adapters are copied into each case directory, and `result.json`
binds the exact script and input hashes. The slice's relative proof-control
path is relative to its actual selected case directory, three levels below
the lane; that path resolves to the parent source control.
