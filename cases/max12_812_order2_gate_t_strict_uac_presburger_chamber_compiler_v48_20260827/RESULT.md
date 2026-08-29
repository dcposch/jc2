# V48: bounded strict unique-`AC` Presburger chamber compiler

Date: 2026-08-27

Status: **PRODUCER PASS / UNREVIEWED.  EXACTLY THE FROZEN V47R1 12
BASELINES PLUS 4 RAISED SUBTAILS AND ALL 8 V47 NEGATIVE CONTROLS ARE
REPRODUCED.  NO STRICT-FAN COVER IS CLAIMED.**

## 1. History check and deduplication

The construction began with a path-specific `git log --all`, `git
log --follow`, targeted `git blame`, and `rg` search for `Presburger`,
`strict chamber`, `chamber compiler`, and `12+4`.  At the observed repository
HEAD `418e413593120d19e15e6546eb50c985f4b1f038`:

- the V46/V47/V47R1 producer and review artifacts are not committed ancestors
  of this case; as their reviews already record, their custody is by frozen
  SHA256.  V48 pins and re-walks both the V47 and V47R1 inner freezes;
- V47 already has a contact-specific four-atom enumerator and derives 12+4 by
  bounded enumeration/scanning, but does not emit a Presburger formula;
- the pinned D23 support miner is an independent contact-specific census and
  local-pole tool, not a semilinear chamber compiler;
- `compile_chamber_split.py`, SHA256
  `431a204151ded8ef492658751855edb1b76dfec6ab31fb87677e8bb991c82982`,
  is an AWS-only `(a,d)=(8,3)` target-shadow Singular compiler.  It neither
  aggregates the strict unique-`AC` primitive universe nor compiles contact
  inequalities; and
- the only prior artifact specifying this exact task is the sealed ideation
  item (`xmodel/ideation-20260827T1104Z-actual_total_g20.md`, SHA256
  `e3bed5f49fefb6abe06f94e5b5764859a76f044b0719b0594b0d0a853537a7a2`)
  and its synthesis (`df8c920f019f1d99053af6d81f4eee52ad88c23d2c8e7bc513782ea06efe0eba`).

Thus V48 is additive software, not a rewrite or duplicate of an existing
compiler.  It preserves every V46/V47/V47R1 byte.

## 2. Independent affine primitive compilation

Before reading any V47 manifest, the compiler expands the four atoms

```text
id  fixed  L-denominator  (R,A,C)  scalar
R1    2          2        (1,0,0)     2
R2    4          4        (2,0,0)     1
A     5          3        (0,1,0)     1
C     5          4        (0,0,1)     1
```

inside the four binomial summands

```text
unloaded: alpha=3/2, delay=0
k10:      alpha=5/4, delay=4
k6:       alpha=3/4, delay=12
k2:       alpha=1/4, delay=20.
```

Routes are aggregated over `Q` by
`(summand,load,fixed,R,A,C,pole)`, where
`pole=L-denominator-4*alpha`.  A universal fixed-delay cap 34 is sufficient:
accepted contacts have `T_C2<32`, and the largest frozen negative has
`T_C2=34`; a primitive visible by either target must have fixed delay at most
34 because `a,c,r` and all powers are nonnegative.

Exact universal census:

```text
nonzero aggregated signatures     425
cancelled aggregated signatures    40
unique-AC inequalities             424
global-pole inequalities           417
```

The `+1` atom-bound pad produces the identical 425+40 tables.  In particular,
the compiler independently live-checks the three low load-bearing zero sums:

```text
unloaded R^4 :  3/8 - 3/4 + 3/8 = 0
unloaded R^2C:  3/4 - 3/4       = 0
unloaded R^2A:  3/4 - 3/4       = 0
```

The complete universal-table digest is
`9dfb45d24a6a0f3341f7d0ae14941ecd65fc3902b3c75092dc6883c6e1121863`.
All ten pinned V46 polar templates occur uniquely in this independently
generated table.

## 3. Presburger predicate and analytic tail threshold

For every nonzero primitive with affine first grade

```text
fixed + R*r + A*a + C*c,
```

the compiler imposes:

1. every primitive other than unloaded `AC/L` is strictly after
   `G=10+a+c`;
2. every pole-`>=2` primitive other than unloaded `C^2/L^2` is strictly after
   `T_C2=10+2*c`; and
3. `G<28` and `T_C2<32`.

For an inequality `fixed+R*r+A*a+C*c>H`, `R>0` gives its exact integer lower
bound

```text
r >= floor((H-fixed-A*a-C*c)/R)+1.
```

An `R=0` failure is persistent.  Taking the maximum of all finite lower
bounds and the registered endpoint floor produces the ray base directly;
there is no search over `r`.  Since every `R` coefficient is nonnegative,
each accepted base certifies the entire closed tail.  The replay additionally
tests two later sentinels for every ray.

Inside exactly the registered V47 box, the 16 expanded rays compress to three
Presburger families:

```text
(2<=a<=6 and d=1 and c=a+1 and r>=a)
OR (1<=a<=6 and d=2 and c=a+2 and r>=a and r>=3)
OR (2<=a<=6 and d=3 and c=a+3 and r>=a and r>=5).
```

Compressed-formula SHA256:
`1827f42b4517a547e84c70db72c690a19a68432d40d8027d16bc87f75f3ced5c`.
The equivalent 16-clause expanded-formula SHA256 is
`e0d55bbc0415dedfc448134b56ce94b3bef64756d8989f8e2e3589d743b4ee73`.

## 4. Exact 12+4 result

Baselines:

```text
A2D1 A3D1 A4D1 A5D1 A6D1
A2D2 A3D2 A4D2 A5D2 A6D2
A5D3 A6D3
```

Raised subtails:

```text
A1D2_R3 A2D3_R5 A3D3_R5 A4D3_R5
```

For every representative, `COMPILED.json` stores the complete aggregated
inventory through `T_C2`, its canonical digest, every active affine facet,
the predecessor witness for a raised ray, and the inherited endpoint ID and
authority/review hashes.  The 16 inventory digests equal V47 byte-for-byte;
their primitive counts sum to 71.  Their compiled chamber-record digest is
`ecd642fe8360d95a38e5c33e564fd21541087ef4624b2c9dd482d2b8617eeb43`.

Only after deriving the regions does the compiler read V47 for comparison.
It then attaches the reviewed V47R1 coefficient digest

```text
ad0c9b15ce394e554c178521fadb32b3c71318cf3a8d700a2311aceb9d12a850
```

to every ray.  Endpoint localizations and theorem types remain inherited;
V48 creates none.

## 5. Eight negatives and eight live mutations

The independently compiled reasons exactly equal the frozen V47 reason lists:

```text
A1D2_R2_RA2       RA2
A2D3_R3_RA2       RA2
A2D3_R4_RA2       RA2
A3D3_R4_RA2       RA2
A4D3_R4_RA2       RA2
E_A1D3_R20_A3     A3 (persistent R-free wall)
A7D1_K6_TIE       NONUNIQUE_G
A9D3_K2_TARGET    NONUNIQUE_G, OTHER_GLOBAL_POLE,
                   G_TARGET_WALL, T_TARGET_WALL
```

Each record includes the exact offending affine primitive.  As a live-fire
control, disabling exactly that record's reason set makes that negative
accepted; all eight such mutations fire.  These mutations demonstrate that
the constraints are operative.  They are forbidden relaxations, not new
mathematical permissions.

An independently imported, pinned support miner matches the V48 inventories
and its own `+1` pad on all 16 positive bases plus all 8 negatives: 24/24
comparison cells.

## 6. Custody and replay

Producer artifacts before this report/freeze:

```text
29d206524de1eb2faadaa3d25a261376c7be380f5b669ed9cf5fa436b263cafe
  SCHEMA.json
1a7dfe1c852e5ac655ed12e4efc80a9a1c8fd3ca2aa0ae0b98f3c17ebd04b575
  compile_presburger_chambers.py
43ff29257e917b4ae5e264866a5159861a5439477b31d74e1a9c0afa6baf285a
  COMPILED.json
```

Replay from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/max12_812_order2_gate_t_strict_uac_presburger_chamber_compiler_v48_20260827/compile_presburger_chambers.py
```

The replay is standard-library-only, takes well under one second locally,
rehashes all ten source pins and both inner freezes, recompiles the universe
and all affine thresholds, compares the 24 independent miner cells, and
requires exact equality with `COMPILED.json`.  No AWS capacity is used.

## 7. Narrow status

This producer establishes only a machine-checked semilinear restatement of
the already reviewed V47/V47R1 strict predicate on its registered 16-contact
domain, plus the eight frozen negative controls.  It is valuable because the
contact list is now derived by an auditable affine compiler rather than
curated/scanned.

It does **not** establish that the registered box covers a strict fan, that
other boxes have no strict chambers, that all normalized boundary data enter
this box, or that Gate T/order two/maximum twelve/JC2 follows.  Different-model
hostile review is required before any canonical integration of V48 itself.

