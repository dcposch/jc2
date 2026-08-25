# Hostile referee report — repaired frozen-`d4` finite-`c` landing unit

**Object.** Nonmutating successor
`xmodel/max12-912-order3-nu-q8-w0-rankdrop-b1-frozen-d4-finite-c-unit-repaired-v2-20260825.md`
together with
`PARAM_SCOPE_ERRATUM.md`, every `PARAM_*` file, and
`aws_box02_param_q_std_dp_v1/*`
in
`cases/max12_912_order3_nu_q8_w0_rankdrop_b1_loaded_saturation_aws_20260825/`.

**Mode.** Read-only. No Bash, CAS, solver, network, or Python. The frozen Box02 endpoint is the computation. Hashes were checked for internal consistency among V2, the freeze, the manifest, `source.sha256`, and the generator pins; they were not independently recomputed.

**Parents.** Pinned compiler
`quotient_compiler.py` / order-three
`order3_fibre.py`; reviewed generic-`c` localizer unit and its Grok review; reviewed slope-two next-order control and its Grok review; ramified-arc audit (filename stale: Grok, not Claude, by the provenance erratum) and both immutable errata.

---

## 1. Six rows, map, ring, load, saturation

**Holds.**

The compiler’s `compile_quotient("approx")` imposes exactly `(1,3,5,7,2,4)` on names `["w","c","d2","d4","x1","x3","x5"]`. `generate_param.py` fail-closes unless `tuple(imposed)==(1,3,5,7,2,4)`. Frozen `input.sing` writes eight approximate-cubic tails and then

```text
ideal SI=se1,se3,se5,se7,se2,se4;
```

`se6` and `se8` never enter `SI`. No terminal, Taylor, or localizer equation is hidden. The six imposed polynomials agree with the ramified-audit quotations and with the already-reviewed generic-`c` tails (same compiler pin `22b0cdc4…`).

The map is exactly

```text
map phi=S,w,c,2+u,1,x1,x3,x5;
```

so `d2 → 2+u`, `d4 → 1`. This is the rank-one point of the doubled drop line `d2-d4=1`, with normal displacement `u=d2-2` and `d4` frozen.

The working ring is

```text
ring R=0,(w,u,x1,x3,x5,c),dp;
```

Characteristic zero, `c` a polynomial variable, not a coefficient-field parameter. This is `Q[w,u,x1,x3,x5,c]`, not `Q(c)[…]`. Contrast the generic-`c` lane `ring R=(0,c),(inv,…)`.

Load and saturation:

```text
poly A=x3-2*x5; ideal Load=w*x5*A;
list LS=sat(I,Load); ideal C=LS[1];
```

`Load` is principal, so this is `I:(w*x5*(x3-2*x5))^∞`. Selected factors appear only as the saturator.

Then `GC=std(C)`, `Landing=GC,w,u,x1,x3,x5`, `GL=std(Landing)`, with `option(redSB)`.

---

## 2. Does `Landing=(1)` exclude every finite `c` at that centre?

**Yes, in this ring, with no hidden `c` denominator.**

Stdout is

```text
landing_empty=1
C_PARAMETER_BASIS_BEGIN
GL[1]=1
C_PARAMETER_BASIS_END
Q8_W0_RANKDROP_B1_PARAMETER_SATURATION_PASS
```

`landing_empty=1` is `reduce(1,GL)==0`. With reduced standard bases, `GL[1]=1` is the unit ideal. Hence `Landing=(1)` in `Q[w,u,x1,x3,x5,c]`.

The centre does not set `c`. A unit ideal in a polynomial ring over `Q` in which `c` is a variable has empty fibre over every closed point of the `c`-line. No polynomial in `c` is inverted in the source, the map, or the saturator. Integer denominators such as `4/9` are constants in `Q`, not content in `c`.

The unit is not automatic from adding the centre: on the raw overlap the six rows vanish, so `I+(w,u,x1,x3,x5)` is nonunit. `Landing=(1)` is a genuine saturation-then-landing statement.

This is weaker than `GC=(1)` and does not empty the selected open. The centre lies in `V(Load)`; the test is whether the closure of `V(I)\V(Load)` meets that centre.

Coefficient infinity (`c=∞`) is a different chart and remains open.

---

## 3. Refused inferences; V2 repairs; `C_PARAMETER_BASIS`

**V2 no longer makes the forbidden inferences.**

| Inference | V2 |
|---|---|
| `GC=(1)` | Explicitly refused; `GC` is never printed |
| Global selected-open emptiness for every finite `c` | Explicitly refused |
| Moving `d4` | Named as successor, not claimed |
| Arbitrary ramification at `b=1` | Main preregistration phrase superseded |

The marker is historical. The generator prints

```text
print("C_PARAMETER_BASIS_BEGIN");GL;print("C_PARAMETER_BASIS_END");
```

so the enclosed basis is `GL`, not `GC` or `C`. V2 and the scope erratum both say this.

The original frozen unit
(SHA-256 `c8e295f0…`, bytes unchanged) claimed that the run “upgrades the reviewed generic-`c` result by removing the finite exceptional-`c` debt in that slice.” That sentence, unscoped, would discharge `D(c)` for the selected open. V2 relicenses it only with “at this landing centre” appended, after refusing `GC=(1)`. That is the correct remaining reading: exceptional finite `c` are excluded at this centre, not off it.

The ramified audit’s original Shard B1 unit-claim (“empties every selected formal/Puiseux/ramified arc through `(2,1)`”) is the claim the scope erratum retracts. V2 does not reinherit it.

---

## 4. Box02 custody and trust tier

**Holds, as a one-engine Singular standard-basis theorem.**

| Item | Record |
|---|---|
| `runner.rc` / `run.meta` | `0` / `rc=0` |
| Host | `ip-172-30-0-186`, tag `q8_w0_rankdrop_b1_param_Q_std_dp_box02_v1` |
| Engine / order | `std` / `dp` only |
| Wall / user / RSS / swaps | `1:07:11` / `4026.60s` / `41820` KiB / `0` |
| Generator stderr | empty (`e3b0c442…` = SHA-256 of empty) |
| Diagnostics | none in stdout; stderr is `/usr/bin/time -v` only; exit status 0 |
| Input SHA-256 | `58c2fa57…` (V2, manifest, `source.sha256`) |
| Stdout SHA-256 | `98950fa2…` (V2, manifest) |
| Manifest SHA-256 | `5c3fa2d4…` (freeze ↔ V2) |
| Compiler / order3 pins | `22b0cdc4…` / `a4fdac5d…` (generator, manifest, `source.sha256`) |

Regeneration: `run_param_remote.sh` emits `input.sing` from `generate_param.py --engine std --order dp`, fail-closes on nonempty generator stderr, requires exactly one `PARAMETER_SATURATION_PASS`, and bans the listed diagnostic patterns. Frozen `input.sing` matches that generator for `std/dp` (map, ring, load, `sat`, `std`, printed `GL`).

No cofactor / `lift` / `modStd` file exists. No in-run `Singular --version` exists. `AWS_R6D_SINGULAR_VERSION.txt` is a different host (`ip-172-30-0-45`) and is not a Box02 pin; V2 does not cite it.

There is no `aws_box03_param_*` tree. Independent Box03 and polynomial-`c` `modStd` endpoints are absent and are not counted.

Custody residual, not a V2 defect: the compiler’s transitive descent-replay pin is enforced on import and is not listed in `PARAM_BOX02_RESULT.manifest.sha256` (same qualification as the generic-`c` review). Erratum and freeze-file hashes in V2 are singly attested; freeze cross-pins the original unit and the result manifest.

---

## 5. Firewall

**Enforced in V2 and in the scope erratum.**

Still open: moving `d4`; the rest of the rank-drop line and full selected horizontal closure `Hsrc`; coefficient and other projective infinity; terminal/Taylor realization; trajectories; all `(9,12)`; maximum twelve; JC2.

This does not contradict the surviving slope-two leading cone `(X1, 3 X3-5 X5, 9 W+4 X5^2)`: an initial cone need not continue, and a frozen-`d4` landing unit does not kill `d4`-drift. The ramified audit remains `NOT_CONFIRMED` for arbitrary ramification. The generic-`c` theorem remains a `Q(c)` statement about the selected open; its exceptional-`c` debt off this centre is not discharged here.

---

## Verdict

Source identity, polynomial-`c` ring, principal selected saturation, and the printed unit of `Landing` survive. Granting the one-host `std/dp` standard basis, `Landing=(1)` excludes every finite `c` at `(w,u,x1,x3,x5)=0` in the slice `d4=1`, `d2=2+u`, with no hidden `c` denominator. V2 correctly refuses `GC=(1)`, global selected-open emptiness, moving `d4`, and arbitrary ramification, and correctly identifies `GL` under `C_PARAMETER_BASIS`. Trust is one engine, no cofactor, no Box02 version capture.

**CONFIRMED**

**Repairs:** none.

**Smallest exact geometric successor:**

```text
d4=1+v,  d2=2+v+u,
C = I : (w*x5*(x3-2*x5))^infinity,
Landing = C + (v,w,u,x1,x3,x5)
```

over `Q[c,v,w,u,x1,x3,x5]` (the pointed moving-coefficient shard already named by the ramified-audit scope erratum and the slope-two review). Box03 / `modStd` remain pending custody, not that successor.
