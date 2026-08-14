VERDICT: CONFIRMED-KILL — within §9's filed-route perimeter, N1–N4 remain valid for arbitrary finite legal neutral insertion stacks, preserve the joint `k | 2` cap through every Case-C prefix, and keep every new non-X gap below `2/5`; no insertion position, boundary M-drop, or multi-insertion compounding pattern escapes either completion.

# Final Sol re-review of the `(9,15,7,3)@2` tower kill

Date: 2026-08-14

Reviewed: `TOWER-9-15.md` §7b and §9, the C3-V/C3-N extension in
`cases/tower_check.py`, both tower certificates, the prior
`xmodel/sol-tower-rereview.md` counterexample, and the relevant P0/R1.2
neutral-transition rules. I replayed the repair algebra independently, tested
stacked insertions and boundary M-drops, traced the explicit `(6,4)` example,
and ran the advertised gate.

## Ranked findings

### 1. CONFIRMED — N1–N4 close the neutral-insertion family

The four lemmas at `TOWER-9-15.md:504-527` replay exactly.

- **N1.** For a clean zero-cost step,
  `Delta=(n-1)nu+1`, hence
  `Delta-n=(n-1)(nu-1)`. If `n,nu >= 2`, this is positive and
  `w' = w n/Delta < w`; an insertion stack that leaves a filed chain state
  unchanged therefore has `n=1` at every inserted vertex. It is a neutral
  cell `(d_p,d_q)=(l nu,nu+1)`. I also enumerated the exact R1.2 divisibility
  conditions at all seven/eight listed states. The only numerical candidate
  for `n>=2` is `Delta=3,n=2,nu=2` at `w=3/2` or `3/4`, but its `d_q=5`
  violates the required denominator divisibility in both cases. Thus there is
  no hidden zero-cost changing-`w` state between the listed states.
- **N2.** `gcd(l nu,nu+1)=gcd(l,nu+1)`. A viable pre-F1 insertion cannot
  drop `M=2`: neutral M-values divide the incoming M and cannot rise again,
  while the fixed F1 arrival needs multiplicity 2. Every member of a pre-F1
  stack therefore preserves M=2, forcing every inserted `nu` odd. Consequently
  `P_pre=prod(nu)` is odd at arbitrary depth.
- **N3.** If the pre-F1 stack is nonempty, its P2-adjacent neutral has one
  full f-factor of exponent `i*l=deg p_f(P2)=4`, so an alive ladder step
  imposes `k | 4`. F1 retains simple reduced factors with
  `i_F1=2 P_pre`, imposing `k | 2 P_pre`. Both witnesses have gaps below
  `gap(X)>1/2`, so both are alive throughout every non-killing Case-C prefix
  and at X-death. Since the ladder pair is coprime,
  `k | gcd(4,2 P_pre)=2`. For `P_pre=1`, F1's simple exponent 2 supplies the
  cap directly. This replaces the false fixed assertion `i_F1=2` without
  weakening the obstruction.
- **N4.** If the poleward full f-degree is `Dprev`, a neutral insertion has
  `i=Dprev/l`, sends the full degree to `Dprev*nu`, and has
  `gap=(nu+1)/(Dprev nu)`. Everywhere on chain 2, and after the first vertex
  on chain 1, `Dprev>=4`; hence
  `(nu+1)/(Dprev nu) <= 3/8 < 2/5` for every `nu>=2`. The first chain-1
  neutral is precisely X and retains
  `gap(X)=(nu_X+1)/(2nu_X)>1/2`. Repeated insertions only increase `Dprev`,
  while every downstream charged gap is divided by the accumulated
  characteristic product. Stacking therefore cannot compound a gap upward
  into `(gap(X),5/2)`.

The Case-C temporal interaction is consequently harmless. At every prefix
level the same two chain-2 witnesses remain alive and reimpose `k | 2`; route
insertions do not alter the fractional-part calculation
`alpha_m = 3/2 + r/2 (mod 1)`. X-death still requires either
`2nu_X | r nu_X+1` (`k_m=1`) or `nu_X | 1` (`k_m=2`), both impossible for
`nu_X>=2`. As a finite stress check, I tested `nu_X=2..500`, prefix counts
`r=0..29`, and 19,607 pre-F1 stacks of depth at most five; the proof itself is
the displayed identity and is not bounded by those ranges.

### 2. CONFIRMED — the 7/8 eligible states are exhaustive; the boundary M-drop does not escape

The direct certificate contains exactly the seven rows
`(3/2,2)`, `(3/4,4)`, `(2/7,7)`, `(1/2,2)`, `(1/2,4)`, `(2,1)`, and
`(2/3,3)`. The trunk adds exactly `(2/5,5)`. These are all chain segments of
the two filed charged routes; N1 excludes an intervening changing-w clean
state.

I specifically attacked neutral M-drops, which are not self-loops. Before
F1, F2, F3, or the trunk step, dropping M destroys the next required arrival
multiplicity `2`, `4`, `7`, or `3`, and M cannot recover through another
neutral. A terminal drop from M=3 or 5 lands at M=1 and is outside the fixed
completion. The sole viable boundary transition is post-pure-b `M=4 -> 2`.
For example, after the `nu3=7` pure-b cell, insert `(l,nu)=(2,3)`:

```text
Dprev = 170*52 = 8840,
i_Y = 8840/2 = 4420,
deg p_f,Y = 26520,
gap(Y) = 4/26520 = 1/6630,
i_G = 13260,  chain-1 product = 6630.
```

It lands in the listed `(1/2,2)` state, is downstream of F1 and the N3
witnesses, and satisfies N4. Arbitrary M=4 self-loops before it and M=2
self-loops after it only enlarge `Dprev` and shrink gaps. Thus this legitimate
cross-state padding is not an eighth/ninth escaping state and cannot weaken
the clash.

### 3. CONFIRMED — the prior explicit `(6,4)` example is covered end-to-end

From the P2 frame `(rho,kbar,nu;w,M)=(1/2,5,3;3/2,2)`, inserting
`Y=(6,4)` with `(l,nu)=(2,3)` gives

```text
Delta = 1, tau = 9/2, n_e = 13,
kbar_Y = 6, rho_Y = 3/2, w_Y = 3/2, M_Y = 2.
```

Both BOOK rows are exact:

```text
(1/2+13)/(5+13) = 6/(2*4),
(3/2+6)/(6+6) = 20/(2*16),  kbar_F1 = 4.
```

The degree ledger is `i_Y=2`, `deg(Y)=12`, `i_F1=6`, `deg(F1)=120`,
`i_F2=30`, `deg(F2)=3570`; the corresponding gaps are `1/3`, `2/15`, and
`1/102`. Here `P_pre=3`, so N3 is the concrete cap
`gcd(4,2P_pre)=gcd(4,6)=2`. Every later full degree scales by 3: the M=2
representative changes `i_G/product` from `22610/11305` to
`67830/33915`, and the M=4 representative changes `4420/2210` to
`13260/6630`. The universal `nu_X>=2` A/B/C argument covers every resulting
chain-1 factorization. The direct and trunk completions share this entire
pole-to-merge subtree; on the trunk, `i_T=3i_G`, so the same trace reaches the
second terminal without a new opening.

### 4. MEDIUM, nonfatal — C3-N does not machine-bind the claimed state-set completeness

`cases/tower_check.py:875-893` loops over whatever rows happen to occur in
`insertions.states`; it does not assert the expected seven/eight names,
positions, count, or route-derived `Dprev_min` values. In an in-memory
negative test, replacing the list by `[]` produced zero checker failures.
C3-V likewise does not explicitly instantiate the legal post-pure-b
`M=4 -> 2` transition above.

This is an executable-certification weakness, not a mathematical survivor in
the current submission: the actual JSON lists are correct, the chain-segment
enumeration above is complete, and N4 is position-, M-, and l-independent once
`Dprev>=4`. It should nevertheless be hardened if the checker is intended to
certify completeness rather than regress the present certificate.

### 5. LOW — the explicit-example replay is partly hard-coded

The computations at `cases/tower_check.py:797-827` are correct, but only some
record fields are compared back to the certificate. Corrupting `cell`, `l`,
`nu`, `position`, `M`, `i_Y`, `deg_p_f_Y`, `i_F2`, and `i_G_scale` together in
an in-memory copy caused zero failures. This does not affect the end-to-end
arithmetic just replayed, but those fields are presently descriptive rather
than checker-bound.

### 6. CONFIRMED — the 696-gate suite and all 14 perturbations pass

I ran exactly:

```text
python3 cases/tower_check.py
```

It exited 0. Independent transcript counts were:

```text
direct certificate: 338 PASS, 0 FAIL
trunk certificate:  344 PASS, 0 FAIL
perturbations:        14 PASS, 0 missed
total:               696 PASS, 0 FAIL
```

All fourteen named perturbations were caught, including the stale
`i_F1=2` pre-F1 insertion and removal of the insertion-closure section. The
final runtime verdict was `OBSTRUCTED` for both certificates.

## Final scope disposition

The `(9,15,7,3)@2` cell is dead at the tower tier for both filed completions,
both raw arrivals `M_U=2,4`, every admissible free pure-b characteristic,
every padding/chain-1 factorization, and every finite legal neutral-insertion
realization, including arbitrary stacks and the legal `M=4 -> 2` boundary
drop. This confirms exactly the §9 perimeter: it does not purport to exclude a
new charged route outside the filed §11a closure or make a claim about the
other sixteen cells.
