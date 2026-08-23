VERDICT: BROKEN

# Adversarial review of the direct `(9,15)@2` tower obstruction

Date: 2026-08-13  
Reviewed: `TOWER-9-15.md`, `cases/towers/t9_15_direct.json`,
`cases/tower_check.py`, `xmodel/sol-gluing-design.md` §1, and the printed
statements in `refs/sigray_full.pdf`.

The submitted construction does not prove that the direct route family dies.
Its two displayed clash calculations are correct **conditional on X or F1
being the level-1 death vertex**, and its use of (H8) on the represented
full-`f` edges is legitimate. The fatal error is that those are not the only
two possibilities: level 1 may be alive at both X and F1. Exactly three
coprime level-1 pairs survive the submitted arithmetic. The checker has no
branch for them and therefore manufactures “exhaustion” by omission.

Independently, the JSON is not the `RouteCertificate` defined by the design,
and the fixed `M_U=2`, `nu_F3=5` representative cannot remove the direct
completion record, which also contains the unexamined `M_U=4` arrival and a
free-characteristic predecessor family.

## Ranked findings

### 1. CRITICAL — the level-1 case split is not exhaustive

`TOWER-9-15.md:221-239` and `tower_check.py:488-521` consider only:

1. X dies at level 1; or
2. F1 dies at level 1.

Printed Prop. 4.2 does not give this dichotomy. It defines a finite tower at
each vertex, with `m_F` the first index at which `delta_m=0`; before that,
`delta_j>0` and the member is alive. Notation 4.1 and Cor. 6.1 give strict
prefix growth, not `m_parent=m_child+1`. Thus levels may be skipped by the
death vertices recorded in the route. The repository already uses this
printed distinction in `SHEET6-R6.md:123-140`.

Here `alpha_1=3/2`, so an alive level 1 has

```
g_1 = l_1/k_1 + 1 - alpha_1 = l_1/k_1 - 1/2.
```

At X the full `f` pattern has one orbit of multiplicity 2. At F1 its orbit
multiplicities are `(4,2,2)`. Prop. 4.2(iii), together with
`gcd(k_1,l_1)=1`, therefore gives `k_1 | 2` whenever level 1 is alive at both.
Strict descent at the shared prefix requires

```
5/2 = g_0 > g_1 > gap(X),       gap(X) <= 3/5,
```

and hence leaves exactly:

| `(k_1,l_1)` | `g_1` | exponent at X, `2l_1/k_1` | F1 exponents `(4l_1/k_1,2l_1/k_1)` | `delta_1(F1)=10g_1-4` |
|---|---:|---:|---:|---:|
| `(1,2)` | `3/2` | `4` | `(8,4)` | `11` |
| `(2,3)` | `1` | `3` | `(6,3)` | `6` |
| `(2,5)` | `2` | `5` | `(10,5)` | `16` |

All entries are integral and positive. The deltas at `(G,H2,F3,F2,F1)`
are respectively

```
(1,2): (101740,33911,4842,250,11)
(2,3): ( 67825,22606,3227,165, 6)
(2,5): (135655,45216,6457,335,16).
```

At every chain-1 neutral stack vertex they are likewise positive integral:
`D_f` is a multiple of 4 and its death gap is at most `gap(X)`. These three
branches are not claimed here to complete the whole tower; they show that the
submitted level-1 obstruction has not killed it. Each must be continued to
the later level at which X and then F1 die.

The program cannot detect this omission because its only obstruction loops
are the two assumed-death cases. Passing all of those assertions proves the
conditional calculations, not the claimed disjunction.

### 2. CRITICAL — the claimed object is not the design's `RouteCertificate`

The design's definition at `xmodel/sol-gluing-design.md:126-182` requires,
among other things:

- instantiated `m_v`, `mu_v`, `k_v`, exact/lower-bound lambda authorities,
  and complete local shape data at every non-pole vertex;
- an edge `chartMode`, elementary slots or a certified composite chart,
  zero/nonzero and arrival labels, a per-label `TransportAuthority`, and
  derived `N_e,r_eh`;
- common tower-label records, `(k_j,l_j,tower_s[j])`, `d_{h_j,v}`, top-pattern
  certificates, chart/jet windows, terminal data, and root-of-unity choices.

The JSON instead declares the separate schema `td7-tower-certificate/v1`
(`t9_15_direct.json:2`). The non-pole records at `:16-54` have no `m_v`,
`mu_v`, or `k_v`; the edges at `:56-74` have no chart mode, slots, transport
authority, or derived chart data; and the ladder ends in the string
`OBSTRUCTED` at `:140-149`. Tower constants and pole scale relations are
prose strings rather than owned algebraic data. It is therefore an
obstruction **prefix**, not a complete tower certificate and still less a
full route certificate.

The claimed `K` is also not certified under design (J0). With no elementary
slots, no `d_h` ledger, and no Prop. 3.1 suitability witnesses, taking the lcm
of vertex kappas is only a denominator-clearing candidate. The checker tests
only `K*pi` and `K*d_f` (`tower_check.py:357-361`).

There is a source-level correction to my design as well. Printed Prop. 4.2
constructs `K_F,L_F,S_F,h_{j,F}` **per vertex**. A label becomes common along
a route only through a proved prefix comparison (Notation 4.1, Prop. 4.4,
St. 8.3(i)/Cor. 6.1). The blanket wording at
`sol-gluing-design.md:659-703` should be understood as “the same global
polynomial on a certified common prefix,” not as authority to identify the
same index on arbitrary incomparable branches. X and F1 can acquire a common
prefix through the shared rootward G, but the JSON must record the depths and
comparison authority; it currently does neither.

The design does permit emptiness of a correctly generated necessary prefix
to kill a route (`sol-gluing-design.md:1647-1649`). That rule does not help
here because the necessary-prefix obstruction itself omits the alive/alive
case.

### 3. HIGH — even a repaired fixed-path kill would not cover the direct book record

The §11a census retains four raw equality completion records for this cell:

| chain-2 arrival | terminal |
|---|---|
| `M_U=2` | direct `(w,M,psi)=(2/3,3,2)` |
| `M_U=4` | direct `(2/3,3,2)` |
| `M_U=2` | one-step `(35,15,7,5)` trunk to `(2/5,5,1)` |
| `M_U=4` | the same trunk terminal |

The census dedup drops `M_U`, leaving two summaries, direct and trunk
(`BOOK-OFFAXIS.md:755-758`; `sol-gluing-design.md:961-972,1003-1008`). The
design expressly says these collapses are not coefficient-system dedups.

The JSON fixes `H2.M=2` and `F3.nu=5` (`t9_15_direct.json:34-42`) and merely
lists `M_U_raw=[2,4]` in arrival prose/data (`:81-84`). The checker never reads
that list; its arrival gate reads the fixed H2 only (`tower_check.py:327-337`).
Moreover, `sol-gluing-design.md:1130-1154` records `nu_F3=5` as one
representative of a free-characteristic family and explicitly forbids using
one specialization to kill that family without an invariance theorem.

Consequently, no §11a completion record may be removed:

- both trunk raw records are wholly untouched;
- the direct `M_U=4` raw record is not represented;
- the direct `M_U=2` raw record still suppresses predecessor/free-`nu`
  provenance; and
- even the displayed `M_U=2,nu_F3=5` specialization is not killed because of
  Finding 1.

Thus **all four raw records and both deduplicated summaries remain**.

### 4. CONFIRMED — (H8) itself is applied within its hypotheses; the M-fold hazard is not the failure

Printed St. 3.17(i) (p. 18) gives full-pattern equality on a vertex edge:

```
deg p_{f,U} = mult(p_{f,L},c).
```

Prop. 8.1(i) (pp. 39-40) gives
`p^{full}_{f,L}=S p_L^{i_L}`. If the reduced continuation multiplicity is
`mu_e`, their combination is exactly

```
deg p^{full}_{f,U} = i_L mu_e.                 (H8)
```

This is an `f` statement; it does not use the overextended dead-member form
of St. 8.3(ii). On the represented route it correctly gives, for example,
`22610*2=45220` on `G->H2`, and `i_N=2` from the `N->P1` degree 2 and
`mu_e=1`.

The design's M-fold warning concerns recovering the chain parameter by
reducing a nonprimitive `(d_p,d_q)`. Here the chain-1 state has `M=1`.
St. 8.4 forces every arriving thickness to divide that M, hence it is 1;
the clean neutral pairs are `(nu,nu+1)` and are primitive. In addition, BOOK
R1.2 uses the repaired cross-multiplied proportion and cancels the thickness
before reduction (`BOOK-OFFAXIS.md:239-256`). No M is silently lost in the
chain-1 synchronization calculation.

For the fixed chain-2 representative, (H8) therefore legitimately forces
the product of the chain-1 neutral characteristics to be
`22610/2=11305`. It does **not** make `22610` universal over the unrepresented
`M_U=4` and free-characteristic chain-2 families.

### 5. CONFIRMED CONDITIONALLY — the displayed gap arithmetic is correct

The arithmetic requested in the construction can be rederived directly from
the printed statements.

At a death level, Prop. 4.2's `delta_m=0`, Cor. 6.1's degree law, and
Prop. 8.1(ii) give the equivalent formula

```
gap(v) = kbar_v/D_f,v = d_q,v/(i_v d_p,v).
```

For the pole-adjacent clean neutral X, R1.2 from P1's
`(rho,kbar,nu)=(1,5,2)` gives `tau=4`, hence

```
rho_X=2,   kbar_X=2(nu_X+1).
```

(H8) gives `i_X=2`, so `deg p_f,X=2nu_X` and
`D_f,X=rho_X deg p_f,X=4nu_X`. Therefore

```
gap(X) = kbar_X/D_f,X = (nu_X+1)/(2nu_X).
```

At F1, the printed St. 9.6(C) reduced pair `(d_p,d_q)=(20,16)` together
with `i_F1=2` gives, equivalently to the certified frame,

```
gap(F1) = 16/(2*20) = kbar_F1/D_f,F1 = 4/10 = 2/5.
```

If X really dies at level 1, then

```
l_1/k_1 = gap(X)+alpha_1-1 = (2nu_X+1)/(2nu_X),
```

so coprimality gives `(k_1,l_1)=(2nu_X,2nu_X+1)`. At F1,
`delta_1=10gap(X)-4=1+5/nu_X`; among the admissible divisors only `nu_X=5`
makes it integral, and then the F1 exponents are `22/5,11/5`. If F1 really
dies at level 1, `l_1/k_1=2/5+1/2=9/10`, hence `(10,9)`, while X would need
the nonintegral alive exponent `2l_1/k_1=9/5`. These conditional
contradictions are sound. The error is promoting them to an exhaustive
case split.

### 6. HIGH — `tower_check.py` verifies a hard-coded calculation, not its claimed certificate/family semantics

I ran the requested command:

```
python3 cases/tower_check.py
```

It exited 0 with 258 printed `PASS` checks and the final text
`tower tier verdict: OBSTRUCTED`. There is no `Fraction`, sign, or denominator
bug in Cases A/B. The obstruction logic nevertheless cannot support its
conclusion:

- `NN=11305`, the X gap, and the F1 exponent multiplicities are hard-coded at
  `tower_check.py:472-501`;
- the only final comparison with the obstruction record checks `status` and
  `checked_stacks` (`:522-523`);
- the advertised universal `n/Delta<1` test samples only
  `2<=n<=11, 2<=nu<=23` (`:482-487`). The universal fact is true because
  `Delta-n=(n-1)(nu-1)>0`, but the checker does not prove it;
- the 15 loop values are the 15 possible nontrivial **pole-adjacent divisor
  classes**, not 15 stacks. There are 75 ordered factorizations of the four
  distinct prime factors (length counts `1,14,36,24`). A proved
  shape-invariance lemma could compress them, but that proof is not encoded;
- in-memory changes to `M_U_raw`, the prose obstruction statement/scope, and
  the recorded obstructed ladder leave `run_all(...,quiet=True)` green; and
- the LEAD-PILOT “regeneration” appends the JSON's stored local, separation,
  scale, and guard row lists (`:579-603`), so equality with the design block is
  substantially a copied-fixture regression, not RouteCertificate IR/schema
  validation.

The negative perturbation suite does not exercise the missing alive/alive
branch, the absent certificate fields, or the omitted route families.

## What survives and where the LEAD-PILOT point lies

The surviving §11a book for `(9,15,7,3)@2` is unchanged: four raw equality
completion records, deduplicated to the direct and trunk summaries described
in Finding 3. “Survives” here means not excluded at the proved tiers; it is
not an existence claim for a Keller pair.

The 83/74 LEAD-PILOT SAT anchor is on the challenged **direct**
`M_U=2,nu_F3=5,nu_N=11305` specialization
(`sol-gluing-design.md:1243-1322`; `t9_15_direct.json:197-287`). It is not on
the untouched trunk route. Since the tower kill is broken, that specialization
remains unexcluded: the SAT point is on a surviving direct necessary-prefix
route, not on a certified-dead family.

## Required disposition

Do not promote `TOWER-9-15.md`'s family kill or remove the direct endpoint
from §11a. Relabel the JSON/checker result as a fixed-data
`tower-obstruction-prefix` regression. A renewed proof must at minimum:

1. carry instantiated `m_v` and prefix authorities;
2. continue the `(1,2)`, `(2,3)`, and `(2,5)` alive/alive branches to their
   later deaths;
3. encode rather than assert the neutral-stack compression; and
4. separately cover `M_U=2/4`, all predecessor paths, and the free
   characteristic family before making an endpoint-family claim.
