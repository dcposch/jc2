# Hostile review: order-two generic-square vertical `c=3,r>=2` thin gate

Date: 2026-08-26
Reviewer: grok-4.6 (read-only except this report; no Singular/Sage/msolve/Lean;
no live `.run` transcript; no worktree inventory).  Small rational identities
were recomputed by hand and by tiny textual/SHA checks.  Stored PASS strings
are evidence, never authority.

Target: `cases/max12_812_order2_square_owner_c3_vertical_thin_20260826/RESULT.md`

**Verdict: `CONFIRMED`.**

No load-bearing coefficient, identity, hypothesis, or scope statement failed.
On the reviewed generic-square first-normal chart `D(p*k0)`, a finite-order
arc with nonzero leading `A` normalized to order zero cannot have
`ord(C)=3` and `ord(R)>=2`.  The exact-Q run is the characteristic-zero
endpoint.  This is an arcwise/set-theoretic exclusion of those vertical
faces only.

## Firewall (enforced)

Licensed claim is at most vertical `a=0,c=3,r>=2` on `D(p*k0)`, conditional
on the already reviewed first-normal setup and the `c=1,2` / `c>=4,r>=2`
predecessors.  It does **not** cover `r=1`, horizontal `a>0`, `p=0`,
`k0=0`, ramified slopes, zero/infinity sections, scheme structure of the
obstruction ideal, fan exhaustion, the whole square stratum, exact order
two, maximum twelve, or JC2.  The producer states this and the evidence
does not overreach it.  The `F_65521` run is a software control, not a
characteristic-zero proof.

## Hashes actually verified

Advertised hashes, recomputed on disk with SHA-256:

| Object | SHA-256 | Status |
|---|---|---|
| producer `RESULT.md` | `c03ad20443cc24c1346e779d98172583bb9193beb89826d327e85f203d574557` | match |
| evidence `RESULTS.sha256` | `cb474217cfaef16773d296318973833edbbc133d4930bb74695f233719674551` | match |
| frozen source `FREEZE.sha256` | `a13d10fb845c1b5cafe249eb700af2e8dd49f3d847c9092478c7f121306fda24` | match |
| compiler `compile_c3_vertical.py` | `3f4d3ecb050090755bf39b9f2fc740495613dce9de4bb69afc77cb4e9d28da70` | match |
| design lemma | `dd4005a92440e8241807bbe3bea4f9305de06c2d08fd0e095dc5dddba4bc7707` | match |
| exact-Q compiled input | `ca1f0692893ba485e2407a6c3a49a397422abb075f97467da0923fdd4b682d29` | match |
| exact-Q stdout | `af96bae652206831e66737c63c490f036fdea962c22c618467a5d04096dac62c` | match |
| `F_65521` compiled input | `5b2a7a24ae0fea5fb016e603804779f985672f2556fdd40ec6ffa118d152cadf` | match |
| `F_65521` stdout | `feba24463e9443631b4d008cc6ed4819835457bc5b2d179ca1987b97ac529186` | match |

Every path inside `RESULTS.sha256` and inside `FREEZE.sha256` was rehashed
and matched.  Transitive compiler pins also matched on disk: cge3 base
compiler `352ad4f2…`, cge3 freeze `a5efc70c…`, `tails.json` `d72f774c…`,
load-ladder compiler `77f25216…`, Padé promotion `40790378…`, halfweight
results/review `eb2cd803…` / `49744ab9…`, low-contact promotion/review
`3447ce8c…` / `ca1a669d…`, ptangent `74551fe8…`.  Canonical all-tail digest
pin `6eed03d4…` is the string the cge3 emitter refuses to emit against.

Both lanes record `compiler_rc=0` and

```text
engine_rc=0
validator=PASS_SQUARE_C3_VERTICAL_THIN
```

The validator is the frozen `run_aws.sh`: it writes `engine_rc`, rejects
timeout/`FAIL_ENGINE`, requires a unique copy of each of twenty sentinels
(seven source/Faber extraction flags, three row-identity flags, the three
bridge/negative-control flags, both deck charts, D1–D4, `r>=3` symbolic,
wrong cubic, and the thin endpoint), rejects `=FAIL` and `^\? ` diagnostics,
and only then writes `PASS_SQUARE_C3_VERTICAL_THIN`.  Both stdouts contain
exactly one copy of each required sentinel and no diagnostic.  Exact-Q
`.meta` has `rc=0`, matching stdout SHA, and `/usr/bin/time` `Exit status: 0`.

The hardcoded print `SQUARE_CGE3_ROW_UNIT_DIAGONAL=1` is **not** a validator
requirement and is not used as authority below.

## 1. Seven source rows, first-normal substitutions, loads, targets, grades 13--15

**Verdict: pass.**

The thin compiler loads the frozen cge3 emitter, pins the shared Faber
tails, calls `emit`, then performs a unique ring-variable extension
(`rtx,aua,cvg,bvb`) and a unique replacement of the unspecialized
`L03`-separator block by the thin certificate.  The compiled exact-Q input
contains `Phi1`–`Phi7`, each built by `tail_text` of the pinned
`tails.json` row with `Lambda=sigma^2`.  Grade extraction is exact division
by `sigma^13` then two further `sigma` quotients, with `reduce` witnesses
and the fail-closed product `divisible*identities*forbidden`.  Stdout
prints seven polynomials at each of G13, G14, G15 (row 6 of G13 is the
zero polynomial, as the even `z^{-6}` moment of a degree-`<=2` proper
part must be).

Square first-normal substitutions in the compiled `Phi` rows:

- moving modulus `pp=p+2*sigma*ell1+2*sigma^2*ell2` (the factor `2` is the
  chart convention `L=z^2+p/2`);
- odd/even square defect `kc=sigma^3*bs1+...` and
  `kr=(pp^2+sigma^3*br1+...)/4`, so `c>=3` already at the K-coefficients;
- A-prolongation `n3=sigma^3*az`, `n2=sigma^3*ac`,
  `n1=sigma^3*(pp*az+cz)/2`, `n0=sigma^3*(pp*ac+cc)/2` with the frozen
  `/2` on `N` and `/4` on the even square load;
- C-jet `cz=sigma^3*e31+sigma^4*e41+sigma^5*e51` (and even counterpart),
  matching `E3z=(e31*z+e30)/2`;
- B-jet `Bz=sigma*(bs1*z+br1/4)+sigma^2*(bs2*z+br2/4)+sigma^3*(bs3*z+br3/4)`.

Loads: `k10=k0+sigma*k1+sigma^2*kk2`, plus `k6` and `k2load`.  The
forbidden-variable sentinels require `diff(g{13,14,15}_row,{k6,k2load,mu2,mu4,mu6,J})=0`
and printed `SQUARE_CGE3_FORBIDDEN=1`.  So `k6` and `k2` do not contribute
at absolute grades 13--15; they are not silently dropped from a grade
where they still live.  Target rows are subtracted at
`sigma^{2(12+row)}` and appear only as

```text
Phi2 ... -sigma^28*(mu2)
Phi4 ... -sigma^32*(mu4)
Phi6 ... -sigma^36*(mu6)
Phi7 ... -sigma^38*(J/4)
```

with odd rows untargeted.  Those powers are strictly above 15, so the
gauge rows do not pollute the extracted coefficients.  Denominator
convention is `L0=z^2+p/2`, `Ls=z^2+sp`, `Inv_k` the truncated binomial
expansion of `(1+sp t^2)^{-k}` (checked: `Inv1` geometric, `Inv2` with
coefficients `n+1`, `Inv3` with `C(n+2,2)`).  Truncation is through
`t^{10}`, which covers the Faber modes `t^2` through `t^8`.

No missing lower load, gauge row, or denominator convention was found.

## 2. Independent expansion of `H13,H14,H15` after `B1=0`

**Verdict: pass.  Every displayed rational coefficient and sign matches.**

The frozen common receiver in the compiled input is

```text
Hshift = (3/4) sigma^10 t AA EE Inv1
       - (3/8) sigma^12 t^2 BB AA^2 Inv2
       - (1/16) sigma^15 t^4 AA^3 Inv3
       + (5/16) sigma^10 kk BB^3 Inv1
       + (5/8) sigma^11 t kk BB EE Inv1
       - (5/32) sigma^13 t^2 kk BB^2 AA Inv2
       + (5/32) sigma^14 t kk AA^2 Inv1
```

with z-chart numerator `Num` the same seven summands times `Ls^{3-k}`.
Term-by-term, `Hshift = t*(Num/Ls^3)|_{z=1/t}` as compiled polynomials
(each of the seven pairs matches, including the `t`-power of the cubic
and of the three `kR*` summands).  After `B1=0`, `BB` starts at `sigma^2`,
so the three `kR*` summands start at `sigma^{16}` or later and cannot
reach grades 13--15.  Direct expansion of the remaining four summands in
`sigma`, using

```text
L(sigma)^{-1} = L^{-1}(1 - sigma ell1/L + sigma^2((ell1/L)^2 - ell2/L) + O(sigma^3))
```

and the parallel expansions of `L^{-2}` and `L^{-3}`, reproduces the
lemma displays exactly:

```text
H13 = (3/4) A0 E3 / L

H14 = (3/4)((A1 E3+A0 E4)/L - ell1 A0 E3 / L^2)
    - (3/8) B2 A0^2 / L^2
    + (5/32) k0 A0^2 / L

H15 = (3/4)((A2 E3+A1 E4+A0 E5)/L
           - ell1 (A1 E3+A0 E4)/L^2
           + (ell1^2/L^3 - ell2/L^2) A0 E3)
    - (3/8)((B3 A0^2 + 2 B2 A0 A1)/L^2 - 2 ell1 B2 A0^2 / L^3)
    - (1/16) A0^3 / L^3
    + (5/32)((k1 A0^2 + 2 k0 A0 A1)/L - k0 ell1 A0^2 / L^2).
```

The compiled numerators `C3h13,C3h14,C3h15` are these functions times
`L`, `L^2`, `L^3` respectively.  Every moving-`L` (`ell1,ell2`),
moving-`p` (inside `L0` and the row transform), moving-`k` (`k0,k1`),
`A0,A1,A2`, `E3,E4,E5`, `B2`, and `B3` correction that can reach grade
15 is present.  No extra sign flip and no omitted `2` in the
product-rule terms `2 B2 A0 A1` or `2 k0 A0 A1`.

Independent source-side check, not using `C3h`: after `bs1=br1=0`, the
printed exact-Q G13 row 1 is `(3/8)(a1 e30 + a0 e31)`.  That is
`[z^{-1}]` of `(3/4) A0 E3 / L` once `E3=(e31 z+e30)/2` is expanded
(the `/2` is why the source coefficient is `3/8` rather than `3/4`).
G15 row 6 contains the cubic `-1/16 a0^3` (and the cross term
`(3/32) p a0 a1^2`).  The same rationals reduce into the `F_65521`
print: `3/8 ≡ -24570`, `-1/16 ≡ 4095`, `3/32 ≡ 26618` (mod 65521).

## 3. Three common-numerator bridge identities

**Verdict: pass.  They are not two copies of one analytic guess.**

`SQUARE_C3_SOURCE_BRIDGE` checks, after `bs1=br1=0`,

```text
N13 = L^2 C3h13
N14 = L (C3h14 + 3 ell1 C3h13)
N15 = C3h15 + 3 ell1 C3h14 + (3 L ell2 + 3 ell1^2) C3h13
```

These are the coefficient-wise identities `N = H L(sigma)^3` with

```text
L(sigma)^3 = L^3 + 3 L^2 ell1 sigma + (3 L^2 ell2 + 3 L ell1^2) sigma^2 + O(sigma^3),
```

and with `H13=C3h13/L`, `H14=C3h14/L^2`, `H15=C3h15/L^3`.  `N13,N14,N15`
come from the z-chart polynomial `Num`, not from substituting `C3h` into
itself.

Glue to the actual source rows, not to a second analytic copy of `C3h`:

1. `g_i = T_{ij} h_j` is checked as a polynomial identity at each of
   grades 13, 14, 15 (`Check{grade}_{i}`, seven rows, remainder printed
   and `row{grade}` cleared on any nonzero).  The `h_j` are Taylor
   coefficients of `Hshift` in `t`.
2. `Hshift = t (Num/Ls^3)|_{z=1/t}` is the hand identification of the
   two compiled presentations of the same receiver (item 2).
3. The three identities then compare that `Num` to the claimed closed
   forms `C3h13,C3h14,C3h15`.

The fail-closed product is
`analyticDiv*row13*row14*row15*numDiv*C3all`.  A match of `Num` against
`C3h` with a broken source bridge would have already quit on a
`SQUARE_CGE3_G*_REMAINDER_*`.  The omitted-connection negative control
`C3bad14 = C3h14 + (3/4) ell1 A0 E3` (drop the first `AC` connection)
makes the grade-14 identity fail, so the bridge is not an `0=0` tautology.

## 4. Polynomiality from zero source tails and lower-unitriangular `T`

**Verdict: pass.  The hardcoded unit-diagonal print is ignored.**

The compiled checks, not the print, give the diagonal of `T`:

```text
Check13_1 = g13_1 - (1) h13_1
Check13_2 = g13_2 - (1) h13_2
Check13_3 = g13_3 - ((1/4)p h13_1 + (1) h13_3)
Check13_4 = g13_4 - ((1/2)p h13_2 + (1) h13_4)
Check13_5 = g13_5 - ((3/32)p^2 h13_1 + (3/4)p h13_3 + (1) h13_5)
Check13_6 = g13_6 - ((1/4)p^2 h13_2 + p h13_4 + (1) h13_6)
Check13_7 = g13_7 - ((5/128)p^3 h13_1 + (15/32)p^2 h13_3 + (5/4)p h13_5 + (1) h13_7)
```

These are exactly `transform_series(i,j)`: `T_{ij}` vanishes unless
`i-j` is even and nonnegative; the `n=0` term is `1`; the Pochhammer
`(j/2)_n / (n! 2^n) p^n` reproduces every displayed off-diagonal
(spot-checked `T_{31}=p/4`, `T_{51}=3p^2/32`, `T_{71}=5p^3/128`, and
the `ell1,ell2` companions at grades 14 and 15, including
`t2 = (3/8)ell2 p + (3/8)ell1^2` on `(i,j)=(5,1)`).  So `T` is lower
unitriangular over `Q[p,ell1,ell2]`, invertible on the same ring.
Vanishing of the seven source tails therefore vanishes all seven
Faber coefficients `h_1,...,h_7`.  Those are `[z^{-1}],...,[z^{-7}]`
of `H_z`, because `h_row = [t^{row+1}] Hshift = [z^{-row}] H_z`.

Proper-fraction degree bounds, charged explicitly:

- `H13 = C3h13/L` with `deg C3h13 <= 2 = deg L`.  Remainder has
  `deg <= 1`, so the proper part is spanned by `z^{-1},z^{-2}`.
  Seven vanished negative moments kill it, hence `L | C3h13`, hence
  `L | A0 E3`.
- `H14 = C3h14/L^2` with `deg C3h14 <= 4 = deg L^2`.  Remainder
  `deg <= 3`, poles `z^{-1}` through `z^{-4}`.
- `H15 = C3h15/L^3` with `deg C3h15 <= 6 = deg L^3`.  Remainder
  `deg <= 5`, poles `z^{-1}` through `z^{-6}`, still inside the seven
  moments.

Denominator recurrences: the three identities of item 3.  The thin
certificate drops the unspecialized Singular `L^3` division that the
universal cge3 emitter used as a separator; after the closed forms
`C3h` are identified with `N`, those recurrences are the same
statement (`N13 = L^2 C3h13` already encodes `H13 = N13/L^3`).
Polynomiality of a finite-order arc is therefore `L | A0 E3`,
`L^2 | N14`, and `L^3 | N15`, which is what D1–D4 consume.

## 5. Etale split `L=uv` on `D(p*k0)`, opposite-root allocation, descent

**Verdict: pass.**

On `D(p)`, `L=z^2+p/2` is squarefree quadratic (discriminant `-2p`).
The chart `p=-2 rtx^2` is the degree-two cover
`Q[p,1/p] -> Q[rtx,1/rtx]`.  It is finite etale for `rtx != 0`, hence
faithfully flat.  `L=(z-rtx)(z+rtx)=u v` with coprime linear factors.

`A0` and `E3` are nonzero linear (nonzero leading `A` of order zero,
and `c=3` means the leading `C` coefficient `E3` is nonzero).  In the
UFD of linear polynomials, `L | A0 E3` forces the two prime factors of
`L` to split between `A0` and `E3`.  Same-root allocation
`A0 ~ E3 ~ u` fails to supply `v`.  Degree forbids `A0` or `E3` from
absorbing both factors.  The only possibilities are the two opposite
allocations, exchanged by the deck `rtx <-> -rtx`:

```text
A0 = aua (z - rtx),  E3 = cvg (z + rtx)
A0 = aua (z + rtx),  E3 = cvg (z - rtx)
```

The factor `2` in `e31=2 cvg` cancels the `/2` in `E3z`.  Compiled D1
checks `C3h13 = (3/4) aua cvg L` on both charts.  That is consistent
with the allocation, not a substitute for unique factorization; the
forcing is the hand UFD argument above.  Polynomiality and the later
unit-equals-zero contradiction are preserved by faithfully flat base
change, so emptiness descends from the splitting algebra to `D(p*k0)`.

`k0` is inverted because this cell lives on the nonzero-load square
component of the reviewed Padé support, not because D2/D4 themselves
need `k0` as a unit.

## 6. D2 and the `r=2` complementary factor of `B2`

**Verdict: pass.**

After D1, every summand of `C3h14` except `-(3/8) B2 A0^2` is visibly
divisible by `L` (`(A1 E3+A0 E4)L`, `ell1 A0 E3`, `k0 A0^2 L`).  Hence

```text
C3h14 ≡ -(3/8) B2 A0^2   (mod L),
```

which is `L^2 H14 ≡ -(3/8) B2 A0^2 (mod L)`.  The client reduces
`C3h14 + (3/8) B2 A0^2` modulo `L` on both deck charts, with `A1,E4,ell1,k0,B2`
still free.  Complementary root `v=0` is `z=-rtx`: `A0=-2 aua rtx`.  The
coefficient of `B2` is `-(3/8)( -2 aua rtx )^2 = -(3/2) aua^2 rtx^2`,
invertible on the stated chart (`char != 2,3`, `aua != 0` by nonzero
leading `A`, `rtx != 0` on `D(p)`).  Polynomiality of `H14` needs
`L | C3h14`, hence `L | B2 A0^2`, hence `v | B2`.  `B2` is linear, so
it is a scalar times `v`: `bs2=bvb`, `br2=4 bvb rtx`.  For `r>=3` one
has `B2=0` already.  D3 is this identity evaluated at the complementary
root; deck D2 plus the same unit coefficient gives the conjugate
factor `u | B2` (`br2=-4 bvb rtx`), which is what deck D4 consumes.
There is no separate `C3deckd3` flag; it is not a missing identity.

## 7. D4 after the factor constraint

**Verdict: pass, including the deck conjugate.**

Imposing `B2=bvb(z+rtx)` and reducing `C3h15` at `z=-rtx` (`L=0`,
`E3=0`, `B2=0`):

- every `AC` summand contains `L` or `A0 E3`;
- every `RA2` summand contains `L` or `B2` (the `B3 A0^2 L` term dies
  on `L`, independently of `B3`);
- every `k A^2` summand contains `L`;
- the cubic `-(1/16) A0^3` remains.

So `L^3 H15 ≡ -(1/16) A0^3 (mod v)`.  The client checks the polynomial
identity `C3d4root + (1/16)(-2 aua rtx)^3 = 0` in the remaining jet
variables (`A1,A2,E4,E5,B3,ell1,ell2,k0,k1,bvb,...`).  If any
connection or load term survived, the equality would fail.  The
right-hand side is `-(1/16)(-8) aua^3 rtx^3 = (1/2) aua^3 rtx^3`,
nonzero on the chart.  Deck conjugate: `z=+rtx`, `A0=2 aua rtx`,
`C3d4broot + (1/16)(2 aua rtx)^3 = 0`, same cubic with the opposite
sign of `A0`.  Polynomiality would require `v | C3h15`, contradiction.

## 8. Independence from `B3` and exhaustion of `r>=2`

**Verdict: pass.**

`C3rge3` checks `diff(C3d4root,{bs3,br3})=0` and that the same cubic
identity survives `bvb=0`.  `B3` enters `H15` only as
`-(3/8) B3 A0^2 / L^2`, which after multiplication by `L^3` is
`-(3/8) B3 A0^2 L`, already `0` modulo `v`.  No higher `R`-jet can
reach grades 13--15: for `r>=4`, `RA^2` starts at `sigma^{16}`.  The
registered `kR3`, `kRC`, `kR2A` terms start at `sigma^{16}` once
`B1=0` (item 2).  Completeness of the four surviving summands against
the seven source rows is the row identities of item 3.  Thus `r=2`
(with the D3 factor of `B2`) and `r>=3` (with `B2=0` and free `B3`)
exhaust the advertised vertical family `a=0,c=3,r>=2`.  They do not
touch `r=1` (`B1` present; the `kR*` terms re-enter grade 13).

## 9. Negative controls; exact Q carries characteristic zero

**Verdict: pass.**

Omitted first `AC` connection: `C3negative` is the boolean that the
grade-14 bridge fails for `C3bad14`.  Printed `=1`.  Wrong cubic:
`C3d4root + (1/15)(-2 aua rtx)^3 != 0`, so the identity is sharp at
`-1/16` rather than an accidental vanishing.  Printed `=1`.

Exact Q is the producer: rational coefficients in stdout, ring
characteristic `0`, input SHA `ca1f0692…`.  `F_65521` is the independent
software control (characteristic `65521` in `result.json`, good prime:
`2,3,5,16` invertible).  The modular G13/G15 prints are the exact-Q
rationals reduced into `F_65521` (item 2), not a second characteristic-zero
argument.  The producer firewall states this.

## 10. Scope

**Verdict: pass; no overclaim in the producer theorem or the endpoint.**

The theorem is the emptiness of vertical `a=0,c=3,r>=2` finite-order
faces on `D(p*k0)` with nonzero leading `A`.  The contradiction is a
unit equal to zero on the etale charts, hence set-theoretic/arcwise.
It does not produce a saturated ideal membership, a scheme structure
on the obstruction, a statement at `p=0` or `k0=0`, a horizontal
`a>0` contact, `r=1`, ramified/zero/infinity sections, fan
exhaustion, the whole square stratum, exact order two, maximum
twelve, or JC2.  Compiled `result.json` scope is
`A_ZERO_C3_RGE2_ON_DPK_ONLY_NO_SQUARE_OR_ORDER2_VERDICT`.  The
endpoint token is `PASS_VERTICAL_C3_RGE2_THIN_DIVISIBILITY`.  Both
match the firewall.

## Residual observations (not load-bearing)

- `SQUARE_CGE3_ROW_UNIT_DIAGONAL=1` is hardcoded.  Unit-diagonality is
  proved from the `Check*` identities (item 4), not from that print.
- There is no `C3deckd3` flag.  Deck D2 plus invertibility of
  `-(3/8)A0^2` at `u=0` supplies the conjugate linear factor; deck D4
  uses it.
- The thin certificate deliberately drops the universal cge3
  `C15+A0^3` separator and the unspecialized `L^3` division
  recurrence.  Those belong to the failed `c>=3,r>=1` global gate.
  The closed-form recurrences of item 3 replace them on this cell.

No smaller failing coefficient, identity, hypothesis, or scope
statement was found.

ORDER2_SQUARE_C3_VERTICAL_CONFIRMED
