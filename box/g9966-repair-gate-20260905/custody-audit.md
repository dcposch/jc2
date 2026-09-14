# Independent replay-custody audit, `(99,66)`, 2026-09-05

The replay-custody component **passes for both declared charts**. This does not
license the charts geometrically: the centre theorem and the availability of a
second source-translation gauge remain separate obligations for the root audit.
In particular, no computation below proves that the retained `Hc_11_0=0` pin is
valid for every source object after centring D2.

## 1. Byte custody and actual original endpoints

The root first verified all seven charged inputs from the frozen receipt. I
subsequently ran `sha256sum -c artifacts.sha256` with cwd
`box/g9966-d2-precise-20260905/`. All **230/230** artifact entries passed; the
230-line output is `custody-artifacts.check.log`, SHA-256
`9230f58338e2859c438c01a0a223c37f2d19e6694665518a179f5246dbcb4859`.
The original engine is pinned at
`3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9`,
the precise engine at
`76d8c7206f70ba190d1a21fff812c016cbde497cd64071c29c91cfe8089f3c06`.
The complete patch passes its artifact digest
`b8d638e4fe8a4ce4b12d5930c006203084631909235bd657dde9817639633ec9`.

This is not merely a comparison to newly labelled controls. I loaded the actual
earlier endpoints and compared their entire `joint_elimination` objects with the
precise lane's pristine controls: every comparison was exactly equal as parsed
JSON, including every pivot, residual expression, row hash and Singular result.

| actual earlier endpoint | SHA-256 |
|---|---|
| `box/g9966band-20260903/runs/delta2/stage4.json` | `5e9dd9516335ef5afa0bd956d014cf8058050601ea960e284b6e5b0a6effef51` |
| `box/g9966s8-20260903/runs/delta52/stage8.json` | `b88a08bd7a4ef323b53516adbf52b08289d0c958b5e0284e279ddb7bffe75006` |
| `box/g9966d52gate-20260903/runs/delta52/stage8.json` | `095c340d7729f97df9a1f1f4709c5afcde00be32fac15cb3ced540e4ae15ccb9` |

All three name the pinned original driver at line 35. The delta2 original
constant is at `g9966band-20260903/runs/delta2/stage4.json:270-271`; both earlier
delta52 records have the constant at `runs/delta52/stage8.json:456-457`.
`custody-original-run-comparison.json` records these comparisons, SHA-256
`360557961e0a3f3ff90d8acbcf9977aba533296cb8555dc6bf439a18d84717e0`.

| branch | pristine-control JSON SHA-256 | precise JSON SHA-256 |
|---|---|---|
| delta2, stage4 | `76c962a71ad088694d280bd5d398bdc8fa050ba81e8423e2260a92f1e99cc3f6` | `adfd00583ddb18a91051feb6b317e64fb6e5d943fdcdbc067ff3ccd8819cc2c8` |
| delta52, stage8 | `e32651392afe0cceb28668f0de2c84bd846bbdb29be4b1f1ec4d97f20e217495` | `77b41a93e4d6cb11e009ec389d270aeca409415a9273ae5d3a323f6cee9dc63f` |

The delta2 residual contains exactly `stage4_J_d159_k35=6264` in the precise
record (`runs/delta2/stage4.json:266-267`) and pristine control
(`control/delta2/stage4.json:270-271`). The delta52 residual is exactly the
single `stage8_G_local16_coord0=64`, precise at
`runs/delta52/stage8.json:450-454`, pristine at
`control/delta52/stage8.json:454-458`. Here and below omitted bundle prefixes
mean `box/g9966-d2-precise-20260905/`.

Even the complete residual hashes agree between control and precise runs:
delta2 `828864876f5068081c28aa1d2305ec124c96960000d714e0415f1a65effc25fe`,
delta52 `e356693da067de90565ae0275ecd5d6779737e962b9d01476fc46b355ce3ccb4`.
The cumulative raw-row hashes change as they should after release; they were
not copied from the controls. There are respectively 659 and 1285 labelled
input rows before joint elimination in both versions.

## 2. Exact specialization, including the maps rather than names alone

Define the coefficient-ring map over Q by

`sigma: Q[old named variables, jet0] -> Q[old named variables]`,
`sigma(jet0)=0`, `sigma(v)=v` for every old variable.

The localizers map identically (`rho -> rho`, `c -> c`), so sigma extends to
their localizations. The inverse-image chart inclusion is the closed section
`jet0=0`; this is a section of the declared parameterized systems, independently
of whether their geometric normalization is legitimate.

I checked symbolic images, not just labels. In both branches all assigned Hc
expressions specialize to the pristine formulas (18 images in delta2, 21 in
delta52); the new branch free-variable set is exactly the old set plus jet0.
The precise map is displayed at `band_engine.py:254-300`. In delta52 it still
assigns `(11,0):0` at line 293 and excludes Hc_11_0 from the free list at line
295. Thus this patch releases the minor constant and retains the polynomial
constant pin. It does not release both pins, and it supplies no independent
proof of the retained pin's geometric availability.

The earlier patch validator checks this at `validate_patch.py:45-56`; it also
reconstructs the face equations and their rational pivots at lines 58-83. I
reran it under local SymPy **1.12**, obtaining byte-identical output to the
stored SymPy 1.14.0 validation certificate:
`custody-patch-validation.json`, SHA-256
`ffdb09b7f20f33767cd5e828a170f7fe243665ce46b6e9a1909b5df7a3957bab`.

Independently, I checked **all serialized endpoint pivot maps and residual
images**, beyond the earlier validator's toy polynomial test:

| branch | corresponding pivot RHS whose sigma-images equal pristine | corresponding residual images checked | extra unresolved quotient generators |
|---|---:|---:|---|
| delta2 | 35/35 | 118/118 | exactly `jet0` |
| delta52 | 66/66 | 1/1 | exactly `jet0` |

For each pivot I additionally checked the same labelled row, same pivot
variable, and same nonzero rational pivot coefficient. Entire row-accounting
objects are equal. The symbolic coefficient images are checked by exact
expansion in Q, not by finite-field or rational-point samples.

The new audit driver `custody_check.py` also compares source code for
`h3_template`, `outer_state`, `raw_minor_support`, `stage_spec`, `qstar_reduce`,
`cumulative_rows`, `build_FG`, `jacobian_band`, `outer_effective_tz`, `tz_mul`,
and `z_band_to_w`; each is identical between engines. `OUTER_SPECS` is also
identical. The only mathematical expansion changes are the branch maps and
constant-jet substitution. The changed minimum-order prefilters are safe:
in delta2, `w=jet0*t+u*t^2+zeta*t^3` has t-order at least 1, so `t^r*w^j` has
order at least `r+j`; in delta52, `t=s^2` and
`w=jet0*s^2+u*s^4+v*s^6+pi*s^7`, so the lower order is `2r+2j`
(`band_engine.py:568-598`). After jet0=0 these expand exactly to the original
substitutions. All subsequent constructions use additions, multiplications,
derivatives, coefficient extraction and division by fixed nonzero rationals,
which commute with sigma. Hence the parameterized raw systems specialize too;
this is stronger than the vacuous statement that two empty terminal solution
sets embed.

There is also a direct support-set proof. The source lower support is the full
triangle `i+j<D` for each D=99,66. Choosing d constant factors in
`(jet0+u*t+zeta*t^2)^j` changes the remaining power to `j'=j-d`; its local
exponent is the old formula `pole-i+j'+k`. Since `i+j'<D`, that tag is already
in the old raw set. In delta52 the same replacement gives the old doubled
formula `pole-2i+2j'+2b+3k`. Conversely `d=0` recovers every old tag. Thus the
complete inventories coincide, not merely their sizes. The engine's old
enumerator is at `band_engine.py:601-628`; sizes remain delta2 F/G=1134/513 and
delta52 F/G=1316/594. The untouched cumulative stage schedule selects the same
tags (`band_engine.py:787-825`).

## 3. Ring, quotient, localizers, and exact unit checks

The coefficient field is Q throughout; no modular inference is involved. The
K2c coordinates are not identified with old C2/C3 merely by matching names.
They are defined as coefficient images of
`K3^3+(t^22*C2)*K3+t^33*C3`; see `band_engine.py:918-927`. The full inverse map
is not serialized, as the engine explicitly admits at line 926. The structural
proof available in `legacy/inputs/major_tower_structure.py:129-152` orders
coefficient positions by increasing r and decreasing q. C3 enters with
coefficient 1 in its own row; C2 first enters via the monic q=11 top coefficient
of K3, also with coefficient 1. Lower q and positive-r terms occur later.
Adding jet0 only changes positive-r coefficients; it preserves these unit
leaders and the coordinate isomorphism over the enlarged coefficient ring.
The seven h2-D1 pivots are checked directly in `band_engine.py:351-384`.

Joint elimination permits a pivot only when its derivative with respect to the
candidate variable is a nonzero rational and the remainder is independent of
that variable (`band_engine.py:188-236`). Cycles in the reconstructed map are
rejected (`band_engine.py:159-177`). The localizer is expressly excluded from
eligible variables, and residual symbols are checked to lie in the remaining
ring (`band_engine.py:850-856`). This establishes quotient-preserving affine
elimination; no disappeared coefficient leader is silently divided by.

There is **no `sat()` wrapper** in this implementation. Localization is the
Rabinowitsch presentation in characteristic zero with a new variable Zp and
equation `Zp*p-1`. I independently reconstructed each emitted ring declaration
from exactly the residual free-symbol set plus p, sorted lexicographically,
then appended Zp. Every first script line matched
`ring R=0,(...),dp;`. I reconstructed the entire `ideal I=` line from every
serialized residual polynomial and the localizer equation; all four scripts
(two pristine and two repaired endpoints) matched exactly.

I then actually reran **all four emitted Singular scripts locally**, with a
30-second timeout per script. Every run completed, no stderr, producing the
same exact output: dimension -1, standard basis `1`, and controls `0,1,0`.
The positive control is `<p,Zp*p-1>`; the negative control is
`<p-1,Zp*p-1>`; the third check shows the raw residual ideal is already unit
before localization. The delta52 precise script is particularly transparent:
`runs/delta52/stage8.sing:1-9` declares `Q[c,Zc]`, sets
`I=<64,Zc*c-1>`, and separately tests `RawControl=<64>`.

The direct identities, in the quotient after the recorded rational pivots, are
`1=(1/6264)*stage4_J_d159_k35` and
`1=(1/64)*stage8_G_local16_coord0`. The row labels refer to their **reduced
images**, not to uneliminated source rows; when lifted to the full ideal, the
recorded pivot equations supply the additional summands. The constant rows
alone prove the residual ideals are unit without depending on a CAS dimension
convention or the localizer's nonvanishing.

The independent checks are reproducible by
`PYTHONDONTWRITEBYTECODE=1 python3 box/g9966-repair-gate-20260905/custody_check.py`.
Driver SHA-256:
`336d38604908b179a0ceb2c4b9d51cb00d9e2b0c8cdec857883df93d20972809`.
Output `custody-independent-checks.json` SHA-256:
`67aa16b7b58c6f78e154b4fa3bf9f5a478db80be17e220750812b94446a36726`.
All four local Singular stdout files have SHA-256
`236517b4a8e5567c586d39194059d49207001416a1d922efaec1fc3d2b9c7b73`.

## 4. Final-stage feasibility and bounded conclusion

The root was sent the delta2 stage4 invocation and has independently launched
the full final-stage reconstruction. The original precise run took 4:40.99,
169 MB, versus delta52's 44:10.10 and 673 MB; delta2 is the sensible branch for
the requested less-than-one-hour independent rerun. I did not duplicate that
expensive job. This note independently reruns only the cheap emitted final
Singular systems and validators. The root should add the fresh full-stage
result and timing to the final report.

`validate_controls.py` was rerun and reproduced its stored certificate exactly
(SHA-256 `cc5a81ad3028dc101db1792cd5e94acceccb530abd435e0d9450806613bce48c`).
`analyze_results.py` was rerun successfully across all 14 repaired stages;
output SHA-256 `bc72a8483ab0c88e5fa4c283876b909a769cb04cd1b2b1ed94929d63735c83da`.
Its promotion wording is its own chart-conditional conclusion and cannot pay
the missing geometric gauge debt. The custody verdict is:

* delta2: exact original unit recovered on the displayed one-parameter enlarged
  chart; numerical and specialization claims confirmed.
* delta52: exact original unit recovered on the displayed enlarged chart
  **with Hc_11_0 still zero**; numerical and specialization claims confirmed.
  This audit supplies no normalization parameter for that retained equation.

No new exit-price assertion is made. No ledger, `jc2-lean`, or `ideation-*`
material was edited or needed for these checks.

## 5. Late hostile check: valid internal division does not license the H3 face

The centre/radius reviewer identified an additional geometric defect. I
independently checked the theorem-hypothesis chain and agree with the defect.
This supersedes any reading of the custody pass as a promotion recommendation.

First, the apparent triangular algebra objection by itself fails. At t-order
4 one can realize the K2 face contribution `-8*z^21` internally by

```
C2_4 = -8*z^10 +24*z^9 -48*z^8 +80*z^7 -120*z^6 +168*z^5
       -224*z^4 +288*z^3 -360*z^2 +440*z -528,
C3_4 = 624*z^10 +1144*z^9 +528*z^8,
z^8*(1+z)^3*C2_4 + C3_4 = -8*z^21.
```

I verified this identity exactly in SymPy. Both coefficient polynomials have
degree 10, so the engine's algebraic division is possible. More generally K3
is monic in z of degree 11 and total degree at most 11; Euclidean division of
a polynomial of z-degree at most 21 and total degree at most 33 produces a
quotient of z-degree at most 10 and total degree at most 22, and a remainder
of z-degree at most 10 and total degree at most 33. Positive t-order is
preserved. This establishes the internal coordinate change completely; it
does not impose the additional source coefficient floor.

That additional floor follows from an actual coherent complete system, not
from one major-disc order alone. Let P be the degree-99 polynomial (Moh's g,
the engine's F). At D2 its order is `72*(1/3)+27*(-1)=-3`. For each of the 27
minor roots, the generic-disc order profile is

`nu_tau(delta)=sum_alpha min(delta,ord(tau-alpha))`.

It is continuous, piecewise linear with positive integer slope on discs
containing tau, and tends to infinity. It therefore has a unique rational
radius where its value is -3. Distinct discs obtained at the same level are
either equal or disjoint: nesting of distinct root-containing discs strictly
increases this profile. Choose distinct representatives, together with D2.
These are disjoint and cover all 99 roots, all at accuracy -3, exactly the
requirements of Moh Def. 1.4 (`moh-layout.txt:445-461`). They lie strictly
inside the principal minor direction because the outer radius -1 has order
-99, below -3.

Prop. 6.1 with r=3 applies to the principal minor multiplicity 3, since
`3 <= 11/(99-97)=11/2`. Its detector conclusion applies at every selected
minor generic point: it is a pi-root of the product because it is a pi-root
of P, it has proximity greater than -1 to the minor direction, and its
P-order is negative. See printed p.191, especially
`moh-layout.txt:2754-2762` and `moh-p191.png`. The distribution-detector
degree ratios for `P,T1^psi,T2^psi` are `99:66:55=9:6:5`, so each selected
minor P multiplicity is divisible by 9; D2 has multiplicity 72, also
divisible by 9. This verifies every divisibility hypothesis of Thm.1.1,
including the roots outside the major disc.

Apply Thm.1.1 to the cubic approximate root H2 of P, then to the cubic
approximate root H3 of H2. The complete system is inherited with accuracies
-1 and -1/3. H3 is consequently a cubic quasi-approximate root of H2 in the
sense of Def.1.5. Thm.1.2 now legitimately applies to
`H2=H3^3+C2*H3+C3` and gives

`ord_D2(C2)>=-2/3`, `ord_D2(C3)>=-1`.

I inspected printed p.149 directly (`moh-p149.png`); its inequality is
`ord h_j(sigma_i) >= (lambda/d)*j`, with the complete, coherent, divisibility
and degree hypotheses stated there. Thus normalized C2 has weight at least
64, whereas the explicit internal C2_4 above has terms far below 64. The
engine's freedom in C2 does not satisfy the source theorem merely because
division succeeds.

At weight 32 the allowed normalized H3 face is
`A(pi)=pi^8+a*pi^5+b*pi^2`. Its cubic has pi^21 coefficient `3a`.
The correct K2 face `(pi^3-beta)^8` has pi^21 coefficient `-8*beta`, beta
nonzero. At weight 96 a source-legal C2 contribution has local pi-degree at
most `10+8=18`, and C3 at most 10. Therefore neither can change pi^21:
`3a=-8*beta`. The replay's strict H3 cutoff fixes `a=0`, contradicting this
necessary equation. Source-valid objects cannot be represented on that
strict H3-face slice. The exact old constants are therefore certificates
about an invalid geometric chart even though all custody, specialization,
quotient and Singular checks pass.

## 6. Independent evaluation of the corrected-face delta2 witness

The root's separate corrected-face diagnostic rerun produced a nonunit stage4
system with zero residual and a rational point. I independently evaluated the
point with `validate_corrected_point.py`, SHA-256
`17c3e96017e73c6efaa3c27f8efdb6a65a2183f92c62614dae5d10c006f52737`.
It imports the corrected engine and reconstructs the 952 variables before
joint elimination using `build_major_h2(delta2,8)` and `outer_state(4)`. It
assigns jet0=rho=1 and every other variable zero, checks the full assignment
digest, then specializes K2 and the outer blocks **before** multiplying out
F and G. Only after numeric construction are the local-series coordinates
substituted in the cumulative rows. No joint elimination or claimed point
result is used to establish their vanishing.

All 659 raw cumulative rows vanish, including `stage4_J_d159_k35`, whose value
is now zero. The localizer rho=1 and wrapper value 1 satisfy their equation.
The zero-image digest matches the root's symbolic run:
`9454c440cbcec9447a609880dd89e1910e690d13f014958531934dd4e58dcf33`.
The input endpoint JSON SHA-256 is
`5eb2ef39d18784eb923b00028584c04a1e91035882e27815227a87f2e7fd2c96`;
the point-assignment SHA-256 is
`47213af3e9a6a4229d0675deecc66dda53665121656602aefecd8406854bcb63`.

The meaningful negative control changes the pre-joint free variable
B1c_0_32 from 0 to 1 while retaining every other assignment. It makes 515 raw
rows nonzero, including `stage1_J_d162_k35=-864` and
`stage1_J_d162_k43=-1158059148444000`. Independently differentiating the fixed
top forms gives the perturbation `864*(w-1)^127*w^35`; its w^43 coefficient
is exactly `-864*binomial(127,8)`, which the validator asserts. Setting the
localizer to zero also makes its Rabinowitsch equation -1.

Output `corrected-point-delta2-validation.json` SHA-256:
`938983e565aa3541cfdea0823e5946ac964b223384ea9707a8ec120c25be0ac9`.
This is a point of the displayed corrected-face **diagnostic truncation**.
It is neither a Keller pair nor proof that all remaining source conditions
can be imposed consistently. It is decisive evidence that the old constant
is not stable under the forced equality-face correction.

## 7. Independent delta52 stage8 point, without a solver endpoint

While the root's full corrected-face delta52 symbolic job was still running,
I tested the explicit assignment `jet0=c=1`, every other pre-joint free
variable zero, without reading any stage8 solver endpoint. The independent
script `trial_corrected_delta52_point.py` constructs
`build_major_h2(delta52,8)` and `outer_state(7)`, with 105 inner and 826 outer
variables. It specializes all these coefficient blocks before building F/G,
then computes and evaluates the full cumulative stage8 raw rows.

The result is **PASS_EXACT_RATIONAL_POINT**: all **1285/1285** rows vanish;
`stage8_G_local16_coord0=0`; `c=Zc=1` satisfies the localizer equation. The
calculation took 16.996 seconds and establishes nonunit of this diagnostic
coefficient ideal independently of any Groebner computation. It does not
establish its dimension or construct a Keller pair.

The same active negative control, B1c_0_32 changed from 0 to 1, makes 1039 raw
rows nonzero, including J162,k35=-864 and J162,k43=-1158059148444000, the
independently expected coefficient of `864*(w-1)^127*w^35`.

| artifact or certificate | SHA-256 |
|---|---|
| `trial_corrected_delta52_point.py` | `3c414755bf3a347e41af877bfc6556ab84bbf1a819bdeeceda3d42dc9451a93b` |
| `corrected-point-delta52-trial.json` | `f4d7e823eae8ec915d30b549cc32f77a43ca56e93b6cf2b3cd67d250b6b75305` |
| full 931-variable assignment | `f864014faa0667a39776ca3e2fe367acc96417df5b131960fb2271f2e1f58257` |
| all 1285 labelled zero images | `8a87b12edac714b1302c47ccdf6c8995c3e752c1b5a9bc6cda93d426f069ef5c` |

Both corrected diagnostic branch truncations therefore have independently
verified exact rational points. Their old unit generators disappear after
the forced face repair; neither original branch-kill certificate survives
this test.
