VERDICT: STILL-BROKEN — Case C is repaired, but the claimed all-realizations kill is not: C3-V omits legal zero-cost neutral insertions before F1 (and on the terminal/trunk paths), so its fixed `i_F1 = 2`, `gap(F1) = 2/5`, and `i >= 170` window are not universal, and the checker never represents those realizations.

# Sol re-review of the `(9,15,7,3)@2` tower kill

Date: 2026-08-13

Reviewed read-only: `TOWER-9-15.md`, both
`cases/towers/t9_15_{direct,trunk}.json`, `cases/tower_check.py`, the relevant
coverage/schema sections of `xmodel/sol-gluing-design.md`, and the charged-path
sources cited by the submission. I independently replayed the Case-C
fractions, the `r`-parity argument, both raw-arrival representatives, and an
explicit neutral insertion outside C3-V's stated parameter window.

The repair closes my former finding 1. It also correctly handles the two
*displayed* `M_U` representatives and its algebra in `nu_X` does not use
`nu_X | 11305` or oddness. The fatal remaining issue is the quantifier over
realizations: a unique charged DAG does not fix where the zero-cost neutral
SCCs are inserted. Inserting one before `F1` changes the very `i_F1` and death
gap that the universal proof and checker hard-code. I found no completed tower
survivor—the missing family appears susceptible to a short additional joint
cap lemma—but that lemma is not in the submitted proof or executable checks.
Thus the repository does not yet prove the advertised cell-level kill.

## Ranked findings

### 1. CRITICAL — C3-V does not cover all neutral-depth realizations

The design requires zero-cost SCCs and neutral-padding families to remain
symbolic, and permits their insertion at any chain state
(`xmodel/sol-gluing-design.md:1064-1068,1083-1099,1130-1146`). The repaired
proof instead concludes from uniqueness of the **charged** DAG that

```text
F1 has i = 2 and F2 has i = 10 on every realization
```

at `TOWER-9-15.md:446-452`. It then uses `F1`'s fixed `i=2` for `k | 2` and
`gap(F1)=2/5`, while bounding padding only “once `i >= 170`”
(`TOWER-9-15.md:462-473`; `cases/tower_check.py:765-775`). That inference is
false: zero-cost neutral cells can occur before, between, or after the charged
vertices. The same omission applies to both completions because the direct and
trunk routes share this whole pole-to-merge subtree. Neutral insertions are
also possible rootward of `G` and on the trunk, although those are not needed
for the counterexample to coverage below.

#### An explicit legal realization outside the window

Start from the chain-2 pole frame

```text
P2: (rho,kbar,nu; w,M) = (1/2,5,3; 3/2,2),  deg p_f = 4.
```

Before the charged `(20,16)` vertex, insert the clean neutral cell with
`(l,nu)=(2,3)` and `(d_p,d_q)=(6,4)`. It has `M=2`, costs zero, and conserves
`w=3/2`. The exact BOOK/R1.2 rows are

```text
(1/2 + 13)/(5 + 13) = 6/(2*4),
kbar_Y = (5+13)/3 = 6,
rho_Y = 6 - 3*(3/2) = 3/2,

(3/2 + 6)/(6 + 6) = 20/(2*16),
kbar_F1 = (6+6)/3 = 4.
```

Thus this is not an arbitrary scaling or a state-only fiction. It is a legal
zero-cost predecessor realization of the same charged path. (Equivalently,
R1.2 gives `Delta=1`, `tau=9/2`, and edge `n=13` at the neutral.)

The full-degree ledger then gives

| vertex | `i` | `deg p_f` | death gap |
|---|---:|---:|---:|
| inserted neutral `Y=(6,4)` | 2 | 12 | `1/3` |
| `F1=(20,16)` | **6**, not 2 | 120 | **`2/15`**, not `2/5` |
| `F2=(119,35)` | **30**, not 10 | 3570 | `1/102` |

For the raw `M_U=4, nu3=7` realization the same insertion scales
`i_G=4420` to `13260` and the chain-1 product `2210` to `6630`. For the
displayed padded `M_U=2` realization it scales `i_G=22610` to `67830` and the
product to `33915`. Neither scaled realization occurs in either JSON, and
C3-V has no constructor or loop over insertion position.

This directly contradicts the assertions at `TOWER-9-15.md:449-450,465-468`
and the claimed escape perimeter at `:486-488`. The executable cap at
`tower_check.py:610-615` is the literal fixed test `2*l/k in N`; it is not
derived from a parametrically specialized `F1`. The `variants` loop
(`:710-764`) carries only `nu3`, a single aggregate `padding_factor`, and final
degree data. It never builds the intermediate vertices whose `i`, gaps, and
alive exponent caps are needed by the proof.

#### I found no mathematical escape, but the missing repair is not filed

The omitted realization does **not** itself enter the death window. In fact a
uniform bound is available. If a neutral cell of characteristic `nu` is
inserted above a poleward vertex of full `f`-degree `Dprev`, then H8 gives

```text
i = Dprev/l,
(d_p,d_q) = (l*nu, nu+1),
gap = d_q/(i*d_p) = (nu+1)/(Dprev*nu).
```

On chain 2, `Dprev >= 4`, hence for every `nu >= 2`

```text
gap <= 3/8 < 2/5 < gap(X).
```

All later charged gaps only shrink when earlier padding multiplies their full
degrees. I checked insertions at every state of both terminal paths; none
enters `(gap(X),5/2)`. There are also no `n>=2` clean zero-cost steps at the
seven relevant states: at `w=3/2` or `3/4`, the only possible `Delta=3`
would have `(n,nu,d_q)=(2,2,5)` and fails the denominator condition; the other
state numerators are below 3.

Likewise, the `k | 2` conclusion appears repairable, but not for the reason
submitted. If a pre-`F1` neutral stack has characteristic product `P`,
preserving `M=2` forces `P` odd. The first neutral has sole full factor
exponent 4, so it gives `k | 4`; `F1` has a simple reduced factor and
`i_F1=2P`, so it gives `k | 2P`. Both vertices are alive at X-death, and

```text
gcd(4,2P) = 2.
```

This joint cap restores `k | 2`. For example, in the `M_U=4` branch with a
pre-pad of characteristic 3, `nu_X=2` proposes X-death `(k,l)=(4,5)`: the
neutral accepts exponent `4*5/4=5`, but `F1` rejects its simple-factor
exponent `6*5/4=15/2`. For `nu_X=3`, `F1` accepts `(6,7)` but the neutral
rejects `4*7/6`.

That is a plausible one-lemma repair, not a result currently proved or tested
by the repository. The submitted claim is specifically that every neutral
padding realization is already machine-covered. It is not. Until insertion
positions are quantified and the general gap plus joint-cap argument is
added, finding 3 remains unresolved and the cell-level quantifier cannot be
promoted.

### 2. HIGH — the schema repair is mostly relabeling, not schema verification

The narrowing at `TOWER-9-15.md:490-496` is honest and useful: these are now
called tower-obstruction prefixes rather than byte-compatible design
`RouteCertificate`s. That scope correction does not make the advertised
fields genuine schema data.

What is genuinely derived:

- All filed `N_e`, `r_f`, and `r_g` values are arithmetically correct on all
  8 direct edges and all 9 trunk edges:

  ```text
  N_e = K(pi_U-pi_L),
  r_f = K(d_f,L-d_f,U) = deg(p_f,U)*N_e,
  r_g = K(d_g,L-d_g,U) = deg(p_g,U)*N_e.
  ```

  `tower_check.py:315-327` recomputes these exactly with `Fraction` (and
  `:265-273` has the bundled terminal-edge version).

What is only labeled, optional, or absent:

- Both validation blocks are guarded by `if "N_e" in e`. Deleting `N_e`
  skips `r_f`, `r_g`, `chartMode`, and authority validation too. Removing all
  five fields from every edge produced **zero failures** on both certificates.
- `chartMode: "PREFIX"` is a category error. The design uses `PREFIX` as a
  projection/completeness label (`sol-gluing-design.md:652-655`); actual chart
  modes require an elementary slot, expanded slots, or complete certified
  composite-chart data (`:177-182`). No slots or `C_e(z)` are present. The
  checker merely compares the string `"PREFIX"` at `tower_check.py:328-331`.
- `transport_authority` is also a string comparison, with no hypothesis or
  top-witness validation. Terminal edges return at `tower_check.py:258-274`
  before their authorities are checked. Corrupting either terminal authority
  to `BOGUS` produced zero failures.
- Every edge labels `g` as `ST8.3_LIVE_j0`, including `N->P1` and `F1->P2`,
  although the pole endpoints have `m=0`; `j=0` is a pole-death transition,
  not a common-live label there. The checker itself notes this distinction at
  `:298-300` but does not correct the authority record.
- Non-pole `m` values are prose strings saying no joint value is realizable;
  they are not integer `m_v` fields. The checker never reads `m` or
  `mu_k_note`. Deleting them all, or changing pole `m=0` to `99`, produced zero
  failures on both certificates.
- The `M_U=4` arrivals are compact `variants` rows, not separately
  specialized vertex/edge certificates, so none of their `N_e/r`, chart,
  authority, or `m_v` data exists.

Thus finding 2 is resolved only as an honest necessary-prefix/relabeling
disposition. It is not a completed implementation of the design schema, and
§8's statements that these fields are “FIXED” and verified on every edge are
too strong. This is not by itself a surviving tower—the obstruction can use a
smaller necessary prefix—but it makes the certificate-quality claim false.

### 3. CONFIRMED RESOLVED — my finding-1 table is implemented exactly, and Case C closes it

The repaired table at `TOWER-9-15.md:360-371` and the executable Sol-table
block at `tower_check.py:637-658` agree row-for-row on both certificates:

| `(k_1,l_1)` | `g_1` | X exponent | F1 exponents | deltas `(G,H2,F3,F2,F1)` |
|---|---:|---:|---:|---|
| `(1,2)` | `3/2` | 4 | `(8,4)` | `(101740,33911,4842,250,11)` |
| `(2,3)` | `1` | 3 | `(6,3)` | `(67825,22606,3227,165,6)` |
| `(2,5)` | `2` | 5 | `(10,5)` | `(135655,45216,6457,335,16)` |

In particular, `delta_1(F1)=(11,6,16)` exactly. The checker also verifies
positive-integral deltas at every recorded non-pole vertex before comparing
the hard-coded rows (`tower_check.py:626-632`). The finite menu enumeration is
exhaustive: `k | 2` and `gap(X)<l/k-1/2<5/2` leave exactly those three pairs.

I replayed the arbitrary-prefix argument independently. Let `S` be the sum of
the odd `l_j` over prefix steps with `k_j=2`; `k_j=1` adds nothing to `alpha`,
and `S` has the same parity as the number `r` of `k=2` steps. Then

```text
alpha_m = 3/2 + S/2,
gap(X) = 1/2 + 1/(2*nu_X),
l_m/k_m = 1 + S/2 + 1/(2*nu_X).
```

While `F1` and the relevant chain vertices remain alive, the fixed-family cap
is `k_m | 2`. For `k_m=1`, integrality requires

```text
2*nu_X | S*nu_X + 1.
```

If `S` is even the residue is 1; if odd it is `nu_X+1`, strictly between 0
and `2*nu_X` for `nu_X>=2`. For `k_m=2`, integrality requires `nu_X | 1`.
Both are impossible. This handles every continuation of each of the three
rows, not only `r=0..5`. Strict descent of the positive integer delta prevents
an infinite non-killing prefix.

The runtime's detailed X-death loop still enumerates only the 15 divisors of
`11305` (`tower_check.py:666-693`), and the separately named universal tests
sample `nu_X=2..300` (`:568-587`). Universality beyond those samples comes
from the displayed divisibility identities, which are valid; it is not an
exhaustive runtime enumeration.

### 4. CONFIRMED WITH THE SCOPE LIMIT ABOVE — both displayed raw arrivals and both terminals replay

The two representative calculations are correct:

- `M_U=2`: `nu3=5` gives `(d_p,d_q)=(38,6)`, `M=2`; the displayed neutral
  pad has `nu=7`, giving full degree `6460*7=45220`, `i_G=22610`, and
  chain-1 product `11305`.
- `M_U=4`: `nu3=7` gives `(52,8)`, `M=4`, `n=63`, and `kbar=4`; with no
  pad, full degree is `170*52=8840`, hence `i_G=4420` and the even chain-1
  product is **2210**. Direct terminal data become
  `(k_f,l_f)=(39780,13260)`; trunk data become
  `i_T=13260`, `(k_f,l_f)=(464100,278460)`.

For arbitrary admissible pure-b characteristic, the filed bound

```text
gap(F3'(nu)) = (nu+1)/(170*(3+7*nu)) < 2/5
```

is correct, and the universal `nu_X>=2` parity refutation itself works just as
well for divisors of 2210 as for divisors of 11305. The direct/trunk distinction
does not affect the shared clash; the trunk's additional recorded gap is far
below the window. What fails is the assertion that these two representatives
plus a post-`F3` aggregate padding bound exhaust all neutral insertion
positions.

### 5. CONFIRMED — the advertised gate and perturbation transcript pass, but do not test the gaps above

I ran

```text
python3 cases/tower_check.py
```

It exited 0. Counting the emitted transcript independently gave

```text
PASS=647
FAIL=0
PERTURB=12
```

All twelve named perturbations are caught, including removal of Case C and
the two `M_U=4` fixture perturbations. None inserts a neutral before `F1`,
moves padding to another chain/trunk state, removes the optional schema
fields, corrupts terminal transport authority, or changes `m_v`. Therefore
the green gate is consistent with—and does not answer—Findings 1 and 2 above.

## Required disposition

Do not promote the `(9,15,7,3)@2` cell kill yet. The next repair can be small,
but it must quantify the symbolic neutral SCCs at **every** eligible state for
both terminal families, derive the general `Dprev` gap bound, and encode the
joint `gcd(4,2P)=2` cap (or another valid uniform replacement) instead of
asserting `i_F1=2`. The checker also needs a perturbation placing a neutral
before `F1` and should reject missing schema fields; `PREFIX`, chart mode, and
transport authority must be separated according to the design's own types.

No repository file other than this review was modified; no git command was
run.
