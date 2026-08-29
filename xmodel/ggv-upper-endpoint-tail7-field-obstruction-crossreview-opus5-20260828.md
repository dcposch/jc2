# Opus 5 hostile crossreview — generalized tail-7 field obstruction

Date: 2026-08-28 UTC
Reviewer: Opus 5 (`claude-opus-5`), Claude Code CLI, working dir `/Users/dc/code/math/jc2`
Charge: promotion gate on
`xmodel/ggv-upper-endpoint-tail7-field-obstruction-r0-sol-ultra-20260828.md`

**Overall verdict: CONFIRMED.**
The obstruction is real, exact, and independently reproduced from the frozen
source by clean-room code. Atom 5 is `REPAIRED`: three statements in the
producer's scope prose are wrong *in the conservative direction* — one proof
step is redundant, the characteristic restriction is not sharp, and the
scheme disclaimer is stricter than the producer's own displayed data requires.
None of these weakens the obstruction; all are recorded rather than normalized.

---

## 0. Pin verification (fail-closed precondition)

```
$ sha256sum xmodel/ggv-upper-endpoint-tail7-field-obstruction-r0-sol-ultra-20260828.md \
            cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828/SOURCE.sha256
8eed5736afba781ce6bf522db7a8348c0f7ce0b1f4dbe885c9ba6eed95bdd882  xmodel/...-r0-sol-ultra-20260828.md
29ffa224682d8f424b1ff5f33fc8c1227e8805f1b67cec0610b74fcc14599955  cases/...projective_r14_20260828/SOURCE.sha256
```

Both match the charge exactly. Proceeding.

---

## Atom 1 — custody and source lineage: **CONFIRMED**

```
$ cd cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828 && sha256sum -c SOURCE.sha256
EVIDENCE_REFERENCE.md: OK          LOCAL_REPLAY/commands.txt: OK
LOCAL_REPLAY/compiler.stderr: OK   LOCAL_REPLAY/compiler.stdout: OK
LOCAL_REPLAY/direct_replay.stderr: OK   LOCAL_REPLAY/direct_replay.stdout: OK
LOCAL_REPLAY/identity.txt: OK      LOCAL_REPLAY/nullstellensatz.stderr: OK
LOCAL_REPLAY/nullstellensatz.stdout: OK LOCAL_REPLAY/stderr.sha256: OK
LOCAL_REPLAY/verifier.stderr: OK   LOCAL_REPLAY/verifier.stdout: OK
PREREGISTRATION.md: OK             R14/LOCALIZATION_CERTIFICATE.json: OK
R14/R14_HOMOGENEOUS.json: OK       R14/R14_P87_ONE.json: OK
R14/R14_P87_ONE_P86_ZERO.json: OK  R14/r14_nullstellensatz_q.sing: OK
R14/r14_nullstellensatz_replay_q.sing: OK  R14/r14_p87_one_p65521.sing: OK
R14/r14_p87_one_q.sing: OK         compile_projective_r14.py: OK
verify_projective_r14.py: OK
```

23/23 OK. Upstream manifests verified independently, not copied from the report:

```
$ sha256sum -c cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828/SOURCE.sha256   # 12/12 OK
$ sha256sum -c cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/SOURCE.sha256  # 14/14 OK
```

(Both use repo-root-relative paths and must be run from the repo root; running
them from inside the case directory produces spurious `FAILED open or read`.
This is a path convention, not a custody defect.)

Direct recomputation of the report's lineage pins:

| artifact | recomputed SHA-256 | report |
|---|---|---|
| `.../branch_p_20260827/RAW_DIRECT_SYSTEM.json` | `ead2fa40…e0a5a0` | match |
| `.../branch_p_20260827/tail_deformation.py` | `a411d661…23f626` | match |
| `.../tail7_reduced…/TAIL7_REDUCED/TAIL_DEFORMATION_SYSTEM.json` | `7edd5ccd…fba77a` | match |
| `.../BRANCHES/shared_block.json` | `3e586cc2…acabf9` | match |
| `.../BRANCHES/shared_block_q.sing` | `458dce83…1e707c` | match |

AWS custody. `AWS_R6D_SHARED_BLOCK_20260828T010806Z/EVIDENCE.sha256` uses
AWS-absolute paths; remapped to local basenames, **12/12 OK**. Manifest-of-manifest
hash `559c028e…b998ccc` matches the report. The frozen engine stdout
(`85d3aad6…9eb64c0`) literally reads:

```
BRANCH=shared_block variables=8 generators=16
START_SLIMGB
END_SLIMGB seconds=0
BASIS_SIZE=1
UNIT=1
J[1]=1
```

All three markers present. `METADATA.txt` confirms `singular_sha256=90ab699b…c7c46f4`,
`memory_cap_kb=8388608`, `wall_seconds=1800`, `exit_code=0`, 01:08:28Z→01:08:29Z.
`engine.rc`/`verify.rc`/`RUN_STATUS.txt` all `0`. `source_check.stdout` shows 14/14 OK.

---

## Atom 2 — clean-room rederivation: **CONFIRMED**

Written from scratch against the frozen `TAIL_DEFORMATION_SYSTEM.json` only.
Neither imports nor invokes `compile_projective_r14.py` or
`verify_projective_r14.py`. Exact `Fraction` arithmetic throughout; independent
polynomial type (monomial = sorted index tuple) and independent RREF with
polynomial remainders.

Helper SHA-256s (staged in `/tmp/hr`, removed at completion; core library
quoted verbatim in Appendix A):

```
7f88befba6b7df656833e9ced9d9840f33d1b4505fc91ef5cdbc73d8592bdfe3  cleanroom_r14.py   (library)
ed7c88406583597f74a8e22d3cebbe08104efa09636a2fe286c199086d30774f  step_row14.py
b4db1edc1ce20a14f68a8515edc951e5e62267533dceaee01c87149e64ca1c61  step_triangular.py
d6b3eccbef40a3b637c9d0428144a69102ea89a27026e0845a538d8f2d7305f7  step_controls.py
831071188e6a1625f156ae5dbe82a31e567a702f48489ca77b8882fe32d9a65a  step_block.py
bf7bda6e7e95398d359bfdf93539825a8704aaa2e4cef493d7fe09ae3455b937  step_hash.py
4b0bad38cb61628bfdbe0ad176a9b9b35cdc11fe1978bbeadd2d5c97c0484d22  step_artifacts.py
e38d14c72298caf0c27f5b7b48a30a60c84d0d43d95252aeb73e5b5ac40490ef  step_cofactor.py
c9d40b609fb81e5679c01080417929248a64d7a7e1959a05f1ffa4d1a4f948a9  step_mut2.py
ecdec1b445bc0a88d57b43ca2bc0bb7bcd6c6d259d17837aee49af4930e8effe  step_scope.py
df3af33a20542593529a8bf4e71e6e579a58f7dbc7c7cc68f7864dd9a3325aee  verify9.py
47c6ae33f0e208419a590c4b2bc529b792787cb8fe25cd05fbb409c43da255cd  step_final.py
```

### 2a. Triangular rows 14–21, withholding `p32,p87` from pivots

Frozen system: `cutoff 7`, `nullity 88`, 198 constraints, rows 14–22
(26,25,24,23,22,21,20,19,18 equations). Support census confirms the triangular
shape: linear supports `p33..p45`, `p24..p45`, `p17..p45`, `p11..p43`, `p6..p23`,
`p3..p16`, `p1..p10`, `p0..p5`, `p0..p2`.

```
p32 appears LINEARLY in rows: [15, 16, 17]
p87 appears LINEARLY in rows: NONE

row 14: eqs=26 cands=13 rank=10 free=3 zero-rows=16 nonzero-comps=16 maxdeg=2
        pivots: p33..p42                       frees: p43, p44, p45
row 15: eqs=25 cands= 9 rank= 8 free=1 zero-rows=17 nonzero-comps=17 maxdeg=2
        pivots: p24..p31                       frees: p43
row 16: eqs=24 cands= 7 rank= 7 free=0 zero-rows=17 nonzero-comps=17 maxdeg=2
row 17: eqs=23 cands= 6 rank= 6 free=0 zero-rows=17 nonzero-comps=17 maxdeg=2
row 18: eqs=22 cands= 5 rank= 5 free=0 zero-rows=17 nonzero-comps=17 maxdeg=2
row 19: eqs=21 cands= 3 rank= 3 free=0 zero-rows=18 nonzero-comps=18 maxdeg=2
row 20: eqs=20 cands= 2 rank= 2 free=0 zero-rows=18 nonzero-comps=18 maxdeg=2
row 21: eqs=19 cands= 1 rank= 1 free=0 zero-rows=18 nonzero-comps=18 maxdeg=3
```

Every rank / free / compatibility count agrees with the frozen
`LOCALIZATION_CERTIFICATE.json` `row_elimination` records
(26/[33..43]/10/[43]/16, 25/[24..31]/8/[]/17, 24/[17..23]/7/[]/17,
23/[11..16]/6/[]/17, 22/[6..10]/5/[]/17, 21/[3..5]/3/[]/18, 20/[1,2]/2/[]/18,
19/[0]/1/[]/18). `held_nonpivots = [32,87]` matches.

Note that withholding `p87` is **vacuous** — `p87` never occurs linearly anywhere
in the system. Withholding `p32` is a genuine choice: `p32` is a linear pivot
candidate in rows 15–17.

### 2b. Endpoint equation `-1 - p32*p87 = 0`

Hostile finding on wording: this is **not** produced by elimination. It is a
*literal frozen generator* of the system, `constraints[180]`, `row=22`,
`x_degree=0`, per-constraint hash `8b3cc652…`, terms `[[[], "-1"], [[32,87], "-1"]]`
— the unique constant-carrying constraint in all 198. The report's phrase
"Replaying the triangular eliminations … gives the literal endpoint equation"
is loose; what withholding `p32` actually buys is *preservation*:

```
constraints[180]              : -1 - 1*p32*p87
after substituting row-14..21 : -1 - 1*p32*p87
unchanged                     : True     (p32 solved? False   p87 solved? False)
```

Because neither `p32` nor `p87` is ever solved, the generator survives the whole
triangular pass verbatim. Had `p32` been pivoted (see 2d), it would have been
rewritten. This is a wording repair only and is folded into Atom 5; the equation
itself is exactly as claimed.

### 2c. Row-21 compatibility `-(3/4)*p86*p87^2 = 0`

Reproduced with its **actual index and order**: of 18 nonzero row-21
compatibilities in RREF order it is number **2** (1-based); the frozen
certificate records `row21_simple_compatibility_index: 1` (0-based) — consistent.
It is a *single-monomial* relation, `term_count = 1`:

```
[2] (deg 3, 1 terms) -3/4*p86*p87*p87
frozen row21_simple_compatibility_terms: [[[86, 87, 87], "-3/4"]]
```

All 18 of my row-21 compatibility hashes equal the frozen
`row21_compatibility_sha256s` list, entry for entry, and equal the
`row_elimination` row-21 list.

The scalar `-3/4` is elimination-path dependent (compatibility rows are not
pivot-normalized by RREF); the invariant content is `p86*p87^2 = 0`. A
basis-free check confirms it is not a normalization artifact: the row-21
compatibility span has rank 18 and contains `p86*p87^2` (solved as a rational
combination, independent of my row ordering).

### 2d. Pivot-drift control

Rerunning the whole pass withholding only `{87}`, so `p32` may pivot:

```
row 15: withheld{32,87} rank=8 comps=17 | withheld{87} rank=9 comps=16  <-- DRIFT
(all other rows identical)
p32 became a pivot : True
p86*p87^2 still a row-21 compatibility when p32 is pivoted : True [index 2]
```

So the pivot convention does shift the row-15 rank, but the row-21 relation is
robust to it. Separately, restricting the row-14 candidate set from the 13
linearly-occurring variables `p33..p45` down to the producer's 11 "same-row"
variables `p33..p43` changes the free count (3 vs 1) but yields **the identical
16 compatibilities** — the `p44,p45` columns lie in the span of `p33..p42`.
Row-14 is therefore pivot-drift-free.

### 2e. Row-14 elimination

```
=== elimination on p33..p43 (11 same-row) ===
  rank            : 10
  pivot vars      : p33 p34 p35 p36 p37 p38 p39 p40 p41 p42
  free vars       : p43
  zero rows       : 16      nonzero comps : 16
  comp degrees    : [2]              (all monomials degree exactly 2)
  comp support    : p78 p79 p80 p81 p82 p83 p84 p85 p86 p87
  support == p78..p87 : True
```

All four sub-claims hold: rank 10, single free mode `p43`, exactly 16 nonzero
compatibilities, homogeneous of degree exactly 2, support exactly `p78..p87`.
My 16 polynomials equal the frozen `R14_HOMOGENEOUS.json` `compatibility`
records term-for-term, with matching `term_count`, `degree`, and all 16
per-polynomial SHA-256s (`de3faf21…`, …).

### 2f. Non-vacuity / mutation control

First attempt was a *dud* and is reported as such: perturbing the coefficient of
`p42` in row-14 equation 0 (`-8 → -7`) left the block bit-identical. Reason:
`p42` occurs in that equation alone among the 26, so its row is always consumed
as a pivot and never contributes to the left cokernel. Likewise mutations of
coefficients of monomials containing `p86` are structurally invisible after the
`p86=0` substitution. A live control needs a compatibility-feeding coefficient:

```
 eq1 coeff of p85*p87 : 12 -> 13 | rank 10 | comps 16 | block changed True
      frozen cofactors on mutated block -> 1 - 19/14*p81*p85 + 241/210*p85*p85 - …   (==1 ? False)
      mutated ordered-term sha : 24d4ba7c85713f13df65f5a45892de2a732697c432b01f521e9d690c0eca24ad
      (baseline                : 3af24b63f97df42e268f6d67bb8a19bb89ffd5d8d34928dec5e8441bf0f8912e)
```

The derivation and the certificate are therefore discriminating, not vacuous.

---

## Atom 3 — localization and byte-identity: **CONFIRMED**

Substituting `p87=1, p86=0` into my own 16 homogeneous quadrics:

```
nonzero after p87=1,p86=0 : 16
variables remaining       : [78, 79, 80, 81, 82, 83, 84, 85]
max degree                : 2
frozen remaining_parameters : [78, 79, 80, 81, 82, 83, 84, 85]
ordered list equality (exact Q) : True     (all 16, in order, term for term)
```

Recomputed hashes, from **my** polynomials under the documented canonical
encoding (terms sorted by plain monomial tuple; `json.dumps(sort_keys=True,
separators=(",",":"))` plus a trailing newline):

```
ordered-term sha256 (mine, clean-room) : 30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257
ordered-term sha256 (frozen block)     : 30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257
published pin                          : 30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257
shared block JSON sha256               : 3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab
published pin                          : 3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab
```

Both published hashes reproduce. The intermediate `R14_P87_ONE.json`
(`p87=1`, `p86` retained, 9 parameters) also matches my computation term-for-term.

### Why the normalization is licensed

The 16 compatibilities are **verified homogeneous of degree exactly 2** in
`p78,…,p87` (checked directly, not asserted). Given a field point of the
endpoint system, the frozen generator `-1-p32*p87=0` gives `p32*p87=-1`, so
`p87` is a unit. Put `q_j = p_j/p87`. Homogeneity gives
`f_i(q) = p87^{-2} f_i(p) = 0`, so `q` satisfies the same 16 equations with
`q87=1`. This rescales **only** the ten coordinates `p78..p87` inside the
row-14 necessary subsystem; it asserts nothing about `p0..p77` and does not
claim `q` satisfies the full residual system. `p86=0`, when used, is a property
of the original point and descends to `q86=p86/p87=0`. No torus symmetry of the
full system is invoked anywhere.

---

## Atom 4 — frozen verifier and direct cofactor identity: **CONFIRMED**

Run only after the clean-room derivation above.

```
$ cd cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828
$ python3 -B verify_projective_r14.py
{"endpoint_relation": "-1-p32*p87=0", "ordered_terms_sha256": "30607ce7…3d4257",
 "row21_relation": "-(3/4)*p86*p87^2=0", "scope": "all field-valued tail7 endpoint points",
 "shared_block_unit_literal": "J[1]=1", "status": "PASS"}                      RC=0

$ /opt/homebrew/bin/Singular -q R14/r14_nullstellensatz_replay_q.sing
DIRECT_REPLAY_LHS=1
DIRECT_REPLAY_OK=1                                                             RC=0
```

Literal `status: PASS`, `DIRECT_REPLAY_LHS=1`, `DIRECT_REPLAY_OK=1` all present.

Source and stdout hashes:

```
255aa3ac1db1594a84faa5fd178482ab6b002f0df9d18c2531dd85bdb51efbdc  R14/r14_nullstellensatz_replay_q.sing
3258a17ac3402c2db9f53423445a179846c78699ff22deec243b49e561841bca  R14/r14_nullstellensatz_q.sing
24250ce63900adca4899bf4c4d6e7b045e47e34c3c54d6efabec5b4d49addabf  LOCAL_REPLAY/direct_replay.stdout
cd946a2f1906a23978f8be97c766235e2a061030086ed4ab3ae7fa084ef7de1c  LOCAL_REPLAY/nullstellensatz.stdout
6ba0bb4f92337475070ea187d58b7abf2d9fbd82bab5fbd958ee9a8649b83a12  LOCAL_REPLAY/verifier.stdout
```

My live reruns initially hashed differently. Cause isolated by `od -c`: the
frozen captures carry **one extra trailing `\n`** added by the producer's capture
harness; content is otherwise byte-identical. Appending a newline reproduces
both frozen hashes exactly (`24250ce6…` and `6ba0bb4f…`). Benign, recorded.

### The identity, decided directly

The replay script is honest: it declares the 16 generators literally, declares
`h1..h16`, forms `lhs = h1*I[1]+…+h16*I[16]`, and prints it. **No standard-basis
routine is called.** I did not accept this at face value. I wrote an independent
parser for the script's Singular syntax and checked, in my own exact-`Q`
arithmetic:

```
generators parsed from replay script : 16
replay generators == clean-room 16   : True        <-- the identity is about the right ideal
nonzero cofactors                    : [1, 2, 3, 4, 13, 14, 15, 16]
cofactor degrees                     : [2, 2, 2, 2, 2, 2, 2, 2]
sum h_i * f_i (clean-room)           : 1
equals exactly 1                     : True        <-- expanded against MY generators
```

So `1 = Σ h_i f_i` is decided affirmatively by my own computation, against my own
independently derived `f_i`, with no reliance on Singular and no reliance on the
AWS `J[1]=1` line. The AWS marker was checked separately (Atom 1) and is
corroborative only. The frozen `liftstd` route (`UNIT_SCALAR=36036`, `J[1]=36036`,
`TRANSFORM_OK=1`, `DIRECT_IDENTITY_OK=1`) is consistent with it.

---

## Atom 5 — logic and scope audit: **REPAIRED**

### 5a. Endpoint ⟹ `p87 ≠ 0` — correct, and stronger than stated

`p32*p87 = -1` makes `p87` a **unit**, in any field of any characteristic (and in
fact in any nonzero commutative ring, since `p87` divides `-1`). Sound.

### 5b. Row-21 ⟹ `p86 = 0` — correct but **REDUNDANT** (the substantive repair)

From `-(3/4)p86 p87^2 = 0` with `p87` a unit one gets `p86 = 0` provided `3/4`
is invertible, i.e. char ∉ {2,3}. In char 0 this is sound.

**But this step is not needed at all.** I tested the nine-variable system
(`p87=1`, `p86` left free):

```
$ Singular -q /tmp/hr/ctl_p86free.sing
P86FREE BASIS_SIZE=1     P86FREE UNIT=1     P86FREE DIM=-1
```

and then, refusing to trust `std`, extracted `liftstd` cofactors and expanded them
in my own exact-`Q` code:

```
liftstd scalar G1 = 36036
sum H_i * f_i (independent exact-Q expansion) : 36036
equals 36036 : True
=> 1 = sum (H_i/36036) * f_i holds with p87=1 and p86 STILL FREE
nonzero cofactors : [1, 2, 3, 4, 13, 14, 15, 16]   degrees : [2]
```

So the row-14 block alone, after the licensed `p87=1` dehomogenization, is
already the unit ideal. The row-21 compatibility `(C21)` — and with it the entire
triangular pass over rows 15–21 — is **not load-bearing**. The producer's proof
presents `(E) + (C21) ⟹ p86=0` as a link in the chain; it is a true statement
about a redundant hypothesis. This changes the proof's structure and its
characteristic bookkeeping but not the obstruction, hence `REPAIRED`, not
silently normalized.

Consequence: the char ≠ 2,3 sensitivity introduced by the `-3/4` disappears from
the argument entirely.

### 5c. Characteristics actually covered — **sharper than "characteristic zero"**

The report claims only characteristic zero, which is correct but not sharp. I
computed the exact denominators of every rational quantity in the displayed
chain:

```
primes in denominators of T (elimination transform f_i = sum_j T_ij eq_j) : [2, 3, 5, 7]
non-integer coefficients among the 16 quadrics                            : NONE (all integral)
primes in cofactor denominators h_i                                       : [2, 3, 7, 11, 13]
36036 = 2^2 * 3^2 * 7 * 11 * 13                                           : [2, 3, 7, 11, 13]
primes in the assembled certificate's denominators                        : [2, 3, 5, 7, 11, 13]
```

The displayed rational proof therefore **does** cover characteristic 0 and every
characteristic `p ∉ {2,3,5,7,11,13}`, by reducing the same certificate mod `p`.
It **does not** cover `p ∈ {2,3,5,7,11,13}`: there the elimination transform
and/or the cofactors lose `p`-integrality, and the frozen data decides nothing.
(Absence of a certificate is not a counterexample; those characteristics are
simply open on this evidence.)

### 5d. Field-valued vs scheme — the disclaimer is **conservative**

The report states it makes "no claim about … scheme emptiness/nonreduced points".
That is safe, but the producer's own displayed data proves more. Every step is
ring-valid, so I assembled a single explicit Nullstellensatz certificate against
the **frozen constraints themselves**:

```
p87^4 = sum_i Homog(h_i) * f_i                    [verified exactly; Homog = degree-2 homogenization in p87]
X^4 - 1 = E * [-(X-1)(X^2+1)],  X = p32*p87,  E = constraints[180]     [verified exactly]
1 = p32^4 * p87^4 - (X^4 - 1)

=== SINGLE EXPLICIT NULLSTELLENSATZ CERTIFICATE OVER Q ===
  constraints used : [0..25, 180]      (26 row-14 generators + the row-22 endpoint generator)
  sum_j cof_j * constraint_j = 1
  equals exactly 1 : True
```

Hence `1 ∈ J`, where `J` is the ideal generated by the frozen tail-7 constraints
in `Q[p0,…,p87]`. The tail-7 endpoint locus is therefore **empty as a scheme over
`Q`**, not merely devoid of field-valued points — no nonreduced or non-field-valued
points either, since a nonzero `Q`-algebra point would force `1 = 0`. Note again
that only **rows 14 and 22** appear in the certificate.

This is an under-claim in the report, not an error. I flag it because the charge
requires distinguishing the two, and because the ledger should not record a
weaker theorem than the frozen evidence supports.

### 5e. Scaling firewall — **CONFIRMED**, and not relied upon

I reproduced the producer's grading census exactly:

```
monomial-weight relations: 4018 (terms 4216 - constraints 198 = 4018)
rank: 86  nullity: 2
free gradings (nullspace coords): ['p46', 'p77']
  basis vector free=p46 : support ['p46=1']
  basis vector free=p77 : support ['p77=1']
```

Both nullspace basis vectors are supported on a single silent coordinate, so
`w32 = w87 = 0` in every admissible diagonal grading — there is indeed no
licensed global diagonal torus normalizing `p87`. Confirmed.

The conclusion does **not** rely on any such action. As set out in Atom 3, the
only rescaling used is `q_j = p_j/p87` on the ten coordinates `p78..p87`,
justified solely by the *verified* degree-2 homogeneity of the 16 row-14
compatibilities. The forbidden global argument is nowhere in the chain.

### 5f. Scope boundaries preserved

- **Fixed square-tail / tail-7 specialization.** The frozen source is explicit:
  `specialization: "all raw parameters of weight below 7 are zero"`, `cutoff: 7`,
  `D23_imposed: false`, `G22_present: false`, and the source itself carries
  `negative_result_scope: "specialization_only_non_evidence"`. The result is
  confined to this stratum.
- **Unrestricted branch P.** Untouched. Nothing here constrains branch-P endpoint
  points with any weight-`<7` parameter nonzero.
- **Other GGV branches.** Untouched.
- **JC2.** No consequence whatsoever. This is a negative result on one
  specialization of one branch; it removes a search rung, it does not bear on the
  conjecture.
- **Tail-6.** Explicitly not addressed, consistent with the report.

### 5g. Corroborative material (not charged, checked anyway)

The four sparse equations in `a=p68, b=p60, c=p54` do have exactly the two
characteristic-zero solutions `(3/4,0,0)` and `(3/2,0,0)`; both verify with zero
residuals, and `(32/9)(a-3/4)(a-3/2) = 4-8a+(32/9)a^2` checks. The case split as
written is correct. This material is corroborative only and the main proof does
not depend on it.

---

## Verdicts

| # | Charged atom | Verdict |
|---|---|---|
| 1 | Custody: `SOURCE.sha256`, upstream tail-7 source, shared-block + AWS pins | **CONFIRMED** |
| 2 | Clean-room rederivation: triangular 14–21, endpoint eq, row-21 relation, row-14 rank/free/16 quadrics | **CONFIRMED** |
| 3 | `p87=1,p86=0` substitution, byte-identity with frozen block, both hashes, licensing | **CONFIRMED** |
| 4 | Frozen verifier PASS, `DIRECT_REPLAY_LHS/OK=1`, cofactor identity decided directly, AWS markers | **CONFIRMED** |
| 5 | Logic and scope audit | **REPAIRED** |

Atom 5 repairs, all in the conservative direction:
1. `(C21) ⟹ p86=0` is redundant; the `p87=1` block alone is already the unit
   ideal (independently certified). Rows 15–21 are not load-bearing.
2. The characteristic scope is not merely 0 — the same certificate holds for all
   `p ∉ {2,3,5,7,11,13}`.
3. The result is scheme emptiness over `Q` (`1 ∈ J`, explicit certificate), not
   only absence of field-valued points.
4. Wording: the endpoint equation is a literal frozen generator
   (`constraints[180]`), not an elimination output; withholding `p32` preserves
   rather than produces it.

**Overall: CONFIRMED.**

---

## Narrowest licensed promotion

> On the frozen tail-7 square-tail specialization of the GGV 8_28 raw branch-P
> endpoint system (`TAIL_DEFORMATION_SYSTEM.json`, `7edd5ccd…fba77a`; all raw
> parameters of weight below 7 set to zero, `D23` not imposed, `G22` absent),
> there is **no characteristic-zero field-valued point**.

That is the producer's claim and it is fully licensed. The same frozen evidence
additionally licenses, at the reviewer's recommendation and with certificates
recorded above:

> `1` lies in the ideal generated by the frozen tail-7 constraints over `Q`
> (explicit cofactors on `constraints[0..25]` and `constraints[180]`), so the
> tail-7 endpoint scheme over `Q` is empty; and the same certificate reduces mod
> `p` for every prime `p ∉ {2,3,5,7,11,13}`.

Not licensed, and must not be recorded: any statement about the unrestricted
branch-P endpoint family, any other GGV branch, the tail-6 rung, characteristics
`2,3,5,7,11,13`, or any Jacobian Conjecture consequence. No raw endpoint witness
is banked; this is a negative result on a specialization.

## Stop rule

Retire the tail-7 rung. Do not spend further compute on tail-7 endpoint search,
normalization variants, or the two normalized affine subbranches — the
obstruction is now certificate-level and pivot-convention independent.

Advance to the tail-6 rung. Given finding 5b, the efficient attack there is
narrow: compile only the tail-6 analogue of the **row-14 block plus the row-22
endpoint generator**, check whether the lowest row's compatibilities are again
homogeneous in the top coordinates, and test that block for the unit ideal. The
intervening triangular rows were dead weight at tail 7 and should not be
launched at tail 6 before that reduction is exhausted. Do not launch the full
tail-6 residual.

---

## Replay transcript

```sh
sha256sum xmodel/ggv-upper-endpoint-tail7-field-obstruction-r0-sol-ultra-20260828.md \
          cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828/SOURCE.sha256
( cd cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828 && sha256sum -c SOURCE.sha256 )
sha256sum -c cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828/SOURCE.sha256
sha256sum -c cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/SOURCE.sha256
sed 's#/home/ubuntu/jobs/.*/output_shared_block/#./#' \
    cases/.../AWS_R6D_SHARED_BLOCK_20260828T010806Z/EVIDENCE.sha256 > /tmp/aws.sha256
( cd cases/.../AWS_R6D_SHARED_BLOCK_20260828T010806Z && sha256sum -c /tmp/aws.sha256 )
python3 -B /tmp/hr/step_row14.py        # rank 10, free p43, 16 deg-2 quadrics on p78..p87
python3 -B /tmp/hr/step_triangular.py   # rows 14-21 ranks/frees/comps; row-21 index 2
python3 -B /tmp/hr/step_controls.py     # endpoint invariance; pivot drift; span membership
python3 -B /tmp/hr/step_block.py        # ordered byte equality with frozen shared block
python3 -B /tmp/hr/step_hash.py         # 30607ce7…, 3e586cc2…
python3 -B /tmp/hr/step_artifacts.py    # all frozen R14 artifacts vs clean-room
python3 -B /tmp/hr/step_cofactor.py     # 1 = sum h_i f_i in own exact-Q arithmetic
python3 -B /tmp/hr/step_mut2.py         # live mutation control (eq1 p85*p87: 12 -> 13)
python3 -B /tmp/hr/step_scope.py        # denominators; 4018/86/2 grading census
Singular -q /tmp/hr/ctl_p86free.sing    # P86FREE UNIT=1  (row-21 redundant)
Singular -q /tmp/hr/ctl_p87zero.sing    # P87ZERO UNIT=0 DIM=5 (p87!=0 is load-bearing)
python3 -B /tmp/hr/verify9.py           # 9-variable identity checked in exact Q
python3 -B /tmp/hr/step_final.py        # single certificate: 1 in J over Q
( cd cases/ggv_8_28_upper_endpoint_tail7_projective_r14_20260828 \
  && python3 -B verify_projective_r14.py \
  && /opt/homebrew/bin/Singular -q R14/r14_nullstellensatz_replay_q.sing )
```

Control that the `p87 ≠ 0` premise is itself load-bearing (so the obstruction is
not vacuous): on the `p87=0` slice the homogeneous block is **not** the unit
ideal — `P87ZERO BASIS_SIZE=22, UNIT=0, DIM=5`. The endpoint generator is doing
real work.

## Pinned identity

```
model                : claude-opus-5 (Opus 5), Claude Code CLI
platform             : darwin 23.6.0, arm64
python3              : 3.9.6 (Clang 15.0.0), exact `fractions.Fraction` only
Singular             : /opt/homebrew/bin/Singular -> Cellar/singular/4.4.1p5_3
                       arm64-Darwin 4.4.1 (44105, 64 bit), GMP 6.3.0, NTL 11.6.0, FLINT 3.6.0
Singular binary      : d31b5138a4ed6fdc1be66d77df99758772fa36d1c7173b10065b7dbdb17089ca
                       (matches the producer's local-replay pin)
AWS engine (frozen)  : 90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4
```

Local work was desk-scale: exact-`Q` Python plus four 8–9 variable Singular runs,
each sub-second. No AWS interaction, no running lane touched, no `jc2-lean`
access, no canonical ledger edited. Ephemeral helpers under `/tmp/hr` were
removed at completion.

### Execution gaps, stated plainly

- The upstream compilation from `RAW_DIRECT_SYSTEM.json` to the 88-dimensional
  nullspace coordinates (`tail_deformation.py`) was **not** re-executed; the
  charge licenses `TAIL_DEFORMATION_SYSTEM.json` as the starting point. That link
  rests on hash custody (`ead2fa40…`, `a411d661…`, `7edd5ccd…`, all verified)
  rather than on recomputation.
- The report's history claims (tail-11/tail-10 unit sections; the same `-1`
  obstruction at tail 9 and tail 8) were not re-derived. They are not charged and
  are not load-bearing for this verdict.
- The two normalized 41-variable branch descents were checked only at the level
  of the four displayed sparse equations (§5g), not recompiled.

## Appendix A — clean-room library, exact bytes

The following is the **verbatim** content of the helper `cleanroom_r14.py`.
The bytes of this code block hash to `7f88befba6b7df656833e9ced9d9840f33d1b4505fc91ef5cdbc73d8592bdfe3`,
the value listed in Atom 2. Every driver script imported this module; none of
them imported or invoked the producer's compiler or verifier.

```python
#!/usr/bin/env python3
"""Clean-room hostile re-derivation of the tail-7 projective-r14 claims.

Reads ONLY the frozen TAIL_DEFORMATION_SYSTEM.json.  Does not import, exec, or
invoke compile_projective_r14.py or verify_projective_r14.py.  Exact Q only.
"""
import json, hashlib, sys
from fractions import Fraction as F

SYS = ('cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828/'
       'TAIL7_REDUCED/TAIL_DEFORMATION_SYSTEM.json')

# ---------- exact multivariate polynomials over Q -------------------------
# monomial = sorted tuple of variable indices (repeats allowed => powers)
def padd(a, b):
    r = dict(a)
    for m, c in b.items():
        v = r.get(m, F(0)) + c
        if v:
            r[m] = v
        else:
            r.pop(m, None)
    return r

def pscale(a, s):
    if s == 0:
        return {}
    return {m: c * s for m, c in a.items()}

def pmul(a, b):
    r = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = tuple(sorted(m1 + m2))
            v = r.get(m, F(0)) + c1 * c2
            if v:
                r[m] = v
            else:
                r.pop(m, None)
    return r

def pvar(i):
    return {(i,): F(1)}

def pconst(c):
    return {(): F(c)} if c else {}

def deg(p):
    return max((len(m) for m in p), default=-1)

def support(p):
    s = set()
    for m in p:
        s |= set(m)
    return s

def pstr(p):
    if not p:
        return "0"
    out = []
    for m in sorted(p, key=lambda t: (len(t), t)):
        c = p[m]
        cs = str(c)
        if not m:
            out.append(cs)
        else:
            mono = "*".join("p%d" % v for v in m)
            out.append(("%s*%s" % (cs, mono)) if c != 1 else mono)
    return " + ".join(out).replace("+ -", "- ")

# ---------- load frozen system -------------------------------------------
def load():
    d = json.load(open(SYS))
    cons = []
    for c in d['constraints']:
        p = {}
        for mono, coef in c['terms']:
            m = tuple(sorted(mono))
            p[m] = p.get(m, F(0)) + F(coef)
        p = {m: v for m, v in p.items() if v}
        cons.append({'row': c['row'], 'x_degree': c['x_degree'],
                     'poly': p, 'sha256': c['sha256']})
    return d, cons

# ---------- substitution --------------------------------------------------
def subst(p, sol):
    out = {}
    for m, c in p.items():
        term = pconst(c)
        for v in m:
            term = pmul(term, sol.get(v, pvar(v)))
        out = padd(out, term)
    return out

# ---------- RREF elimination with exact polynomial remainders -------------
def eliminate(polys, cands):
    """RREF over Q on the linear columns `cands`.  Returns
    (pivots, frees, solution dict, compatibility polys, rank)."""
    n = len(cands)
    idx = {v: j for j, v in enumerate(cands)}
    rows = []
    for p in polys:
        vec = [F(0)] * n
        rem = dict(p)
        for v in cands:
            c = rem.pop((v,), F(0))
            vec[idx[v]] = c
        rows.append([vec, rem])
    # forward elimination
    pivots = []
    r = 0
    for j in range(n):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][0][j] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][0][j]
        rows[r][0] = [x / pv for x in rows[r][0]]
        rows[r][1] = pscale(rows[r][1], F(1) / pv)
        for i in range(len(rows)):
            if i != r and rows[i][0][j] != 0:
                f = rows[i][0][j]
                rows[i][0] = [a - f * b for a, b in zip(rows[i][0], rows[r][0])]
                rows[i][1] = padd(rows[i][1], pscale(rows[r][1], -f))
        pivots.append(j)
        r += 1
        if r == len(rows):
            break
    rank = len(pivots)
    frees = [cands[j] for j in range(n) if j not in set(pivots)]
    sol = {}
    for i, j in enumerate(pivots):
        # row: p_j + sum_{free} a*p_free + rem = 0
        e = pscale(rows[i][1], F(-1))
        for jj in range(n):
            if jj != j and rows[i][0][jj] != 0:
                e = padd(e, pscale(pvar(cands[jj]), -rows[i][0][jj]))
        sol[cands[j]] = e
    comps = []
    for i in range(rank, len(rows)):
        assert all(x == 0 for x in rows[i][0]), "nonzero pivot part in tail row"
        if rows[i][1]:
            comps.append(rows[i][1])
    return pivots, frees, sol, comps, rank

def canon(p):
    """canonical ordered term encoding of one polynomial"""
    return ";".join("%s|%s" % (",".join(map(str, m)), str(p[m]))
                    for m in sorted(p, key=lambda t: (len(t), t)))

def blockhash(polys):
    payload = "\n".join(canon(p) for p in polys).encode()
    return hashlib.sha256(payload).hexdigest()
```
