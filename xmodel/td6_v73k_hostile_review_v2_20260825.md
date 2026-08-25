# Hostile review V2: TD6 V73K plus custody repair

Inspection only of the four charged surfaces.  No producer, no
`verify.py` execution, and no `replay_v73.py` execution.  Stored `PASS`
strings were ignored as proof.  Frozen file bytes were hashed with
Python `hashlib` and compared by exact equality; the portable archive
was listed and read, not unpacked into the tree.

Charged surfaces:

- `cases/td6_c1_c2_c3_q2_cminus5_previous_x11_v73_aws_20260825/`
- `cases/td6_c1_c2_c3_q2_cminus5_v73_review_repair_20260825/`
- `xmodel/td6-c1-c2-c3-q2-cminus5-previous-x11-v73-aws-20260825.md`
- `xmodel/td6-c1-c2-c3-q2-cminus5-v73-review-repair-20260825.md`

The original eight load-bearing points are re-audited from source and
evidence.  The sole required V1 finding is then checked against the
nonmutating supplement: the q-prime omission bytes are predecessor
six-odd-row/per-edge support evidence, are not V73K-reproducible, and
are excluded from the V73K theorem/pass gate.

---

## Findings

**1. [Confirmed] Source typing is the raw line `V=0,C=-5U^2`, not the
parent `b3half` weighted center.**

The hash-pinned parent
`jc2/cases/td6_c1_c3_two_center_cover_20260824/c1_c2_c3_p3_quotient.py`
inside the portable archive hashes to `f8c46d2c…`, matching
`replay_v73.py`.  Mode `b3half` is a dummy `Q(U)` tower
(`Z^2=2`, `Y=1`, outer `V^2=U^3`, intended degree 1).  Parent `main()`
would install the birational `t=1/2` chart

`U=w^2/y`, `V=w^3/y`, `C=x w^4/y^2`

with `x=19/9`, `y=32/9`, hence `V≠0`.  V73K never calls parent `main()`.
`p.configure()` only retargets coefficient types.  `center_and_audit()`
then builds the raw point `(-5U^2,0,U)`, asserts `V=0`, `C+5U^2=0`, and
the raw sextic `100U^6-120U^6+20U^6=0`, and writes `r.fb.CENTER` before
transport.  Transport uses the frozen `t^15` / dead-stretch-0 / `F1_*` /
`POLE_*` data.  The `β t^2` term is the dual source `("g","X",0,2)`, not
a weighted rescaling of `q`.  Both theorem stdouts emit
`weighted_scaling_used=false`.

Parent `rational_constant_subfield` / `curve_base_subfield` audits live
only in parent `main()` and are not replayed on V73K identity
coefficients.  Residual/inverse TSV slots are the `Q(U)` components
`0,4,8,12,16,20`.  That is consistent with dummy-tower descent and does
not license a different center.

**2. [Confirmed] Hash-pinned outer `range(40)` intercept reconstructs
exactly `('X-1',0..11)`.**

`qd.compile_previous` is `jet_orbit_adjoint.compile_previous`, which
temporarily copies `qd.Q_PRIME` onto `qd.base.Q_PRIME` and calls
`base.compile_x_previous`.  The only `range(40)` in that function is the
outer degree loop; degrees are independent.  Inner loops are
`enumerate(f1)`, `enumerate(f2)`, and `range(1,len(f1))`.  Patching
`qd.base.range` therefore hits exactly the intended iterator;
non-`(40,)` calls go to `builtins.range`.  The wrapper asserts
`range_calls.count((40,))==1`.

Unintercepted packed `compile_previous` on the 94-chart, followed by
staged GE, yields `used_previous_indices=[0..11]` with keys
`('X-1',0)..('X-1',11)` in order, so `pack()` did not skip any of those
degrees (`pack` omits a degree only if both the linear part and the
constant vanish).  The intercepted compile is zipped against
`selected_degrees` from those keys, not against pack indices.  Both
theorem stdouts emit intercept count 1 and those twelve keys.  No pole
row enters the support.

**3. [Confirmed] Direct `q'` is retained in the theorem run.  The
q-prime-omission bytes are predecessor six-odd-row/per-edge support
evidence, are not V73K-reproducible, and are excluded from the V73K
theorem/pass gate.**

Parent formula of `compile_x_previous` at degree 11, after
`configure_qd` has set `Q_PRIME[1]=2β`:

- `2·Q_PRIME[0]·f2[11] = 2 f2[11]`
- `2·Q_PRIME[1]·f2[10] = 2·(2β)·f2[10] = 4β f2[10]`
- `Q_PRIME[24]` needs `f2[-13]`, absent

The printed string `4*beta*f2[10]` is not extracted from the compiled
polynomial; it is true by that formula together with the post-compile
assert `qd.Q_PRIME[1]==BetaPoly([0,2])`.  Intercepting the outer loop
still enumerates all of `f2`, so `f2[10]` is not dropped.  Theorem
Box02/Box03: `direct_qprime_retained=true`, dependents
`[('X-1',11),('X-1',13)]`, twelve previous keys `0..11`, aggregate
convolution, `V73C_PREREGISTRATION.md` in the source list, tag
`…_k_single_positive_…T2107Z`.

The frozen control is a different producer:

| | Theorem (V73K) | `evidence/control/box03-qprime` |
|---|---|---|
| tag | `…_k_single_positive_…T2107Z` | `…_b_qprime_…T1927Z` |
| source list | includes `V73C_PREREGISTRATION.md` | omits it |
| dependency | 12 rows, `0..11` | 6 odd rows `1,3,5,7,9,11` |
| lift | one aggregate convolution | per-edge `previous_edge_*` DAG |
| `Q_PRIME[1]` | asserted `2β` | `direct_qprime_retained=false` |
| DAG extras | `aggregate_*_sha256` | absent |
| stderr command | `./run_v73.sh main` | `./run_v73.sh omit-direct-qprime` |
| identity digest | `be5b6bc8…` | `c7b45865…` |
| DAG digest | `27a26a20…` | `e2a19087…` |
| leaf ledger | `112776f2…` | `71552fdc…` |

V73K as written cannot emit that control: `assert qd.Q_PRIME[1]==BetaPoly([0,2])`
and `assert used_previous_keys==[('X-1',d) for d in range(12)]` are
unconditional inside `previous_x11_certificate`.  The tarball
`run_v73.sh` still advertises an `omit-direct-qprime` mode; that mode
cannot pass those asserts.  Residual digest and residual-factor TSV
still match the theorem (`3884ec0c…`, `8763f53f…`), and `('X-1',13)` is
absent.  That much is usable support, from a different binary.

The nonmutating supplement completes the required classification:

- repair README / repair xmodel label the bytes as predecessor
  `td6_v73_cminus5_x11_b_qprime_box03_20260825T1927Z` six-odd-row
  per-edge support;
- repair `verify.py` asserts the six-odd-row keys and does not treat
  the predecessor `PASS` string as a V73K theorem gate;
- predecessor stdout/stderr in the supplement are byte-identical to
  the original control copies (`c698dca9…` / `12994f40…`);
- the predecessor directory still has no `rc`, `launch.meta`, or
  timestamps, and the supplement infers none (GNU `time` in stderr
  prints `Exit status: 0`; that is not a frozen return-code file);
- theorem runs never read the control directory.

The frozen original `verify.py` still *reads* those bytes as a package
marker.  Stored `PASS` strings are non-authoritative under this charge,
and the overlay pass gate excludes them.  Because the original package
is immutable, that leftover marker clause is not a remaining required
repair.

**4. [Confirmed] `('X-1',11)` residual is β-independent, U-supported,
unit on `D(U)` after inverse.**

GE records `residual.degree==0` with digest `3884ec0c…` on both theorem
hosts and in the predecessor omit run.  TSV (byte-identical on all three
copies):

- numerators: `Q`-multiples of `x` (`U`), empty denominator factors,
  U-order 1
- inverse: constant numerators, denominator `x`, U-order 1

`BetaPoly.inverse` requires degree 0; `residual*inverse==1` is asserted
in the coefficient field.  Normalized target `{(): -1}` has canonical
digest `d8bcc0ed…` on both theorem identities *and* the predecessor
identity, so the unit polynomial is the same object.  Vanishing locus of
the residual is only `U=0`.  Endpoint `U=0` is not consumed.

**5. [Confirmed] Ancestry is original previous-plus-first, not echelon
rows; signs check.**

- Staged left-null on packed `compile_previous(bands94)` plus poles:
  combination replay equals `{(): -residual}`.
- Same scalar weights on raw intercepted `compile_previous(bands132)`
  give `aggregate_raw`.
- One exact batch division through first-stage pivots (normalized
  singleton leading 1, no other pivot in the tail, reconstructed-input
  replay).
- Remainder remapped 132→94 equals the target; lift of quotients through
  GE combinations, then **negated**, so `aggregate_raw − lift = remainder`.
- `first_rows` are `qd.pack('X-2', first_band_polynomials(bands132))`,
  the original first-band polynomials on the 132-chart, not the stored
  echelon forms (`solve_stage` copies rows).  Thirteen nonzero first
  multipliers.
- One convolution `raw_previous + first_relation` is asserted equal to
  `{(): -residual}`.  Normalization is scalar multiplication of that
  replay by `residual^{-1}`, not a second convolution.

Dead V72 current/N13 body after `return` is unreachable.

**6. [Confirmed] Lex exponent-vector leading-monomial argument is a
valid integral-domain certificate.**

`Quad.inverse` and `Curve.inverse` check the product against `1`.
Dummy `b3half` tower (`Z^2=2`, `V^2=U^3`) is constructed as a field.
Thus `ECurve[β]` is a domain, and the source polynomials sit in a
polynomial ring over a domain.

Lex on exponent vectors, with a fixed variable order (`sorted` of
variables appearing in the two factors), is a monomial order, so
`lm(fg)=lm(f)lm(g)` and the product of leading coefficients is the
leading coefficient.  `nonzero_product_witness` asserts that product is
a nonzero `BetaPoly` and checks exponent additivity.  It does not need
to form the omitted convolution.

- Omission of `('X-1',0)`: multiplier is a source-constant `{(): weight}`;
  delta `-m·r`; witness `lm=(0,30)`, digest `89ffc253…`.
- Plus-one: delta is the selected original row; `max(selected_row)` uses
  Python tuple order, not lex, but only nonzeroness is required.  Valid,
  weaker.
- Wrong-row `('X-1',1)`: `r_wrong≠r` by polynomial inequality;
  `m·(r_wrong-r)` witnessed nonzero with a different leading-coefficient
  digest `4741f098…`.

Stdout domain tag `Q(U)_exact_field_polynomial_beta` is slightly
narrower than the true ring `Q(U)(algebraic constants)[β]`; that does
not break the domain property.

**7. [Confirmed] Numerator/denominator and leaf-denominator ledgers
charge only `U`.**

Residual TSV factors every `Q[U]` coordinate of residual and inverse.
Leaf ledger enumerates coordinate denominators of transport-chart
inverse, residual, inverse, dependency weights, first/previous pivot
leads, raw previous multipliers and selected original previous rows,
first multipliers and selected original first rows, and the two
normalized multiplier families.  Emitted denominators: `1` and `x^k`
for `k=1..8`.  `leaf_denominator` and `transport_chart` share summary
`(8,1,7f4f8056…)`; `leaf_denominator.factor()=(1,[(x,8)])`; monic
product is `x^{16}`.  `certificate_chart_factor_set=['x']`.  No other
prime is localized.

The predecessor leaf ledger charges the same primes with smaller
multiplicities, as expected from a six-row per-edge combination.

**8. [Confirmed] Dual-host theorem outputs agree after the registered
provenance cut; no positive identity byte changed; freeze design is
custody, not algebra.**

Box02/Box03 start together at `2026-08-25T21:07:22Z`, end `21:38:37Z` /
`21:39:02Z`, wall ~31m, RSS ~1.69GB, distinct hostnames
`ip-172-30-0-186` / `ip-172-30-0-249` — independent runs, not a copy.
After dropping exactly

`aws_hostname=`, `aws_run_tag=`, and the four `*_path=` lines,

every remaining stdout line agrees (149 lines, including
`aws_platform=Linux` and all mathematical lines).  Both `rc` files are
the single byte `0` and hash to `9a271f2a…`.  The four theorem artifacts
are byte-identical across hosts.  Independent SHA-256 of those artifacts,
both theorem stdouts, both `rc` files, `replay_v73.py`, the portable
archive, `V73_SOURCE.sha256`, original `MANIFEST.sha256`, original
`FREEZE.sha256`, and the producer report all match the freeze table.
Walking every original `MANIFEST.sha256` entry gives zero mismatches.

Positive identity bytes (DAG `27a26a20…`, identity `be5b6bc8…`, leaf
ledger `112776f2…`, residual factors `8763f53f…`) are unchanged by the
supplement: the repair directory contains none of those files, and the
original copies still match the freeze.  The predecessor residual-factor
TSV is the same object as the theorem TSV; the predecessor identity,
DAG, and leaf ledger are different objects, as required for a different
combination.

Repair `MANIFEST.sha256` / `FREEZE.sha256` walk with zero mismatches.
Repair freeze pins the original `MANIFEST` / `FREEZE` / producer-report
digests `1282f908…` / `d50d8844…` / `716717ab…`.

Scope firewall holds on both theorem stdouts
(`whole_B3_killed=false` and sibling flags) and on both xmodel reports.
Nothing in the DAG, identity, or repair overlay claims whole B3, whole
A3, TD6, SP-2, landing, or JC2.  The exact theorem scope remains
`V=0,C=-5U^2,D(U)` for all beta in the fixed source-typed A3 q2-beta
section.

---

## Strongest exact claim that survives

In the already fixed, source-typed normalized A3 section with
`q_β=t+β t^2+t^{25}` and direct `q_β'=1+2β t+25 t^{24}`,
on the raw open line `V=0`, `C=-5U^2`, `D(U)`:

the previous-stage row `('X-1',11)` is dependent, with β-degree 0 and
residual digest `3884ec0c…`.  Its exact `Q[U]` numerators are supported
only at `U`, it has no residual denominator, and its inverse
denominator is only `U`.  There is an exact left-null combination of
the twelve original parent-compiler rows `('X-1',0),…,('X-1',11)`
which, after one exact first-stage division and lift to thirteen
original first-band rows, convolves to that residual; scalar
normalization yields `-1` on `D(U)`.  Therefore those licensed
original source rows cannot vanish simultaneously on this line, for
every β.  The degree-11 contribution of the `t^1` term of `q'` is
`4β f2[10]` by the pinned parent formula.

The frozen `evidence/control/box03-qprime` bytes are predecessor
six-odd-row/per-edge support evidence from
`td6_v73_cminus5_x11_b_qprime_box03_20260825T1927Z`.  They are not
reproducible by frozen V73K `replay_v73.py`, and they are not a V73K
pass gate, theorem premise, independent theorem run, or custody proof.

This does not consume `U=0`, does not kill whole `B3` or whole A3,
and is not a TD6 / SP-2 / landing / JC2 theorem.

---

## Remaining required repairs

None.

The V1 required provenance finding is discharged by the nonmutating
supplement.  No algebraic change to the positive original-row identity,
the residual, or the LM controls is required.  No positive identity
byte changed.  The strict `V=0,C=-5U^2,D(U)` fixed-section scope is
preserved.

Recommended, not required:

1. Assert parent `b3half` rational/curve descent on identity
   multipliers, or dump their `flat_ratu` support, so the "`Q(U)`
   adapter" claim is audited on the combination and not only on the
   residual TSV.
2. Extract `4β f2[10]` from the compiled degree-11 polynomial;
   parent-formula inspection already certifies it.
3. The frozen original `verify.py` still reads predecessor `PASS`
   markers.  That script is a non-authoritative custody checker and is
   not the V73K theorem gate; mutating it would break the original
   freeze.

---

CONFIRMED
