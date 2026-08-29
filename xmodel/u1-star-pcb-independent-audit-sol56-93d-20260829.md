# Independent hostile audit: `U1*(r)`, PCB, and the enlarged td12 trunk closure

Date: 2026-08-29  
Researcher: Sol 5.6, independent desk lane  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `SEALED_READ_ONLY_RESEARCH_REPORT / NO_PROMOTION / FAIL_CLOSED`

## 0. Executive verdict

| claim | verdict | maximum safe reading |
|---|---|---|
| `U1*(r)` pole entry and star, odd `r>=3` | **CONFIRMED** | exact reduced arithmetic, `td=4r` |
| equal-join merge formulas and local `T1` | **CONFIRMED WITH REPAIR** | require merge index `n>=2`, hence here `n>=5`, `n=1,5 mod 6` |
| one-step P1 trunk closed forms | **CONFIRMED** | the report skipped a short divisibility argument; it is supplied below |
| displayed Corollary-7.1 budget fit | **LOWER-FLOOR NON-EXCLUSION ONLY** | pole and merge prices are exactly zero, but the dirty-cell prices need not equal their AF2 floors |
| `Sigma_cfg` interface no-go | **CONFIRMED AT ABSTRACT-INTERFACE SCOPE** | no axiom internal to the enumerated interface kills it; no actual realization follows |
| bare `PCB: d >= s + sum wt` | **UNSUPPORTED, NONDUPLICATE, LOGICALLY UNDECIDED** | no Keller counterexample is known; the proposed Section-7/Riemann--Hurwitz derivation is false |
| Fable `W1--W3` and pure-epsilon family | **EXACT REDUCED WITNESSES** | all displayed arithmetic and local `T1` checks pass; none is an actual source realization |
| B25 continuation | **EXACT BUT IRRELEVANT TO OCCURRENCE REFUTATION** | it shows B25 is not an absorbing terminal; the path already contains B25 |
| two-cell `{B25,S17}` terminal codomain | **REFUTED AT REDUCED TIER** | the actual-source occurrence theorem remains open |

The strongest conclusion is therefore two-level.  First, `U1*(r)` really is
an odd-arity family of reduced necessary-data survivors, so the present local
arithmetic is not `td`-selective; this confirms the charged no-go relative to
its explicitly enumerated `Sigma_cfg`.  Second, neither that abstract model
nor the new multi-step paths establishes actual occurrence or realizability.
The missing consumers are full-index/source transport, cross-vertex
coefficient gluing, and exact actual exit weights.

For `PCB`, the exact missing statement is not a “pole-cluster decomposition”
of the existing Euler proof.  It is the new excess inequality

```text
sum_i ( integral_(U_i) w_i dchi_c - wt_i(a) ) >= s(a)-1.       (PCB-EXCESS)
```

No reviewed result supplies it.  This is the cheapest precise prove-or-refute
target.

## 1. Scope and custody

This audit read the charged Opus occurrence/coverage report, the exact
equal-join producer and hostile review, the td12 trunk producer/review, the
reviewed pole-entry-zero producer/review, the exact weighted Section-7 repair
and hostile audit, the earlier sealed quartet/detour report, the new Fable
occurrence/coverage report, the convergent Grok hostile review of the charged
`U1*(r)`/PCB report, and the directly relevant Sigray/BOOK statements.
The current overlays and the coordinator source-interface audit supplied the
status perimeter.

This was desk reasoning only.  No web, AWS, CAS, git operation, canonical
edit, Lean action, repository-wide inventory, or external message was used.
The separately fenced formalization tree was not inspected, listed, read,
statused, built, or modified.  The only write is this requested sealed report.

One source-status correction is material.  The older U1 trunk hostile review
correctly reported pole price as unknown at its time, but the later
`POLE-EXIT-ZERO` producer and different-model `PASS` prove that every actual
pole vertex has empty literal and selected cv exit sets.  Thus the three
td12 pole prices are exactly zero.  The uncertainty belongs to interior
off-axis segment vertices, not to the pole vertices themselves.

## 2. Independent recomputation of `U1*(r)`

Fix odd `r>=3`, type `(alpha,beta)=(2,3)`, and `r` identical pole rows

```text
(a,b,nu)=(1,2,3).
```

### 2.1 Entry and star

At each pole,

```text
Lambda = a*b*alpha*beta/nu = 4,
M      = b = 2,
w      = a*(b*(alpha+beta)-1)/(b*nu) = 3/2.
```

The two arithmetic guards are literal:

```text
3 | beta,                 3 | (b*alpha-1)=3,
gcd(a*(alpha+beta),nu)=gcd(5,3)=1.
```

Hence the mass identity gives `d=4r`.  Take one arity-`r` star merge, with
all arrivals nonzero and of multiplicity `mu=2`; at reduced-interface scope
the arms may be length zero, while a typed source packet may insert
clean-neutral interpolations.  Then

```text
sum_merges (R_G-1)=r-1=s-1,
mu=2 | M_pole=2,
gcd(nu_pole,mu)=gcd(3,2)=1.
```

The repaired arrival-subtree floor is saturated:

```text
d >= r*max(beta,2*alpha)=4r=d.
```

Thus entry, mass, tree Euler, arrival divisibility, P2 entry coprimality,
and `ASM'/NM'` are mutually consistent for every `r`.

### 2.2 Merge closed forms

Let `n` be the U1 merge characteristic index.  With
`(mu,epsilon,k,lex,w)=(2,0,0,0,3/2)`, direct substitution gives

```text
dp       = 2*r*n,
dq       = r*n+1,
E        = 2,
kbar     = 3*(r*n+1)/2,
X        = 3*r*n,
w_trunk  = 3*r/2,
M        = gcd(2,r*n+1),
lambda_G = 0.
```

`M>=2` and `kbar in Z` both require `rn` odd, hence `n` odd.  Moreover

```text
gcd(kbar,n)=gcd(3,n),
```

because `gcd((rn+1)/2,n)=1`.  N1 therefore requires `3 not| n`.
The U1 theorem is a `nu_G>=2` theorem; `n=1` belongs to the separate
case-I/U2 regime.  The correct progression is consequently

```text
n>=5,        n == 1 or 5 (mod 6),
```

not the charged report's unqualified `n=+/-1 mod 6`, which accidentally
admits `n=1` in its prose.

The merge-local Proposition 8.1(iv) equation also has an exact solution for
every `r`.  Put

```text
R(t)=t^r-A_*,       p=R(t)^2,       q=eta*R(t),
t=eta^n,            rho=2rn/(rn+1),       A_*!=0.
```

Then the normalized left side is

```text
rho*R + n*t*(rho-2)*R'.
```

Its `t^r` coefficient is
`rho+nr(rho-2)=0`, and its constant is `-rho*A_*!=0`.
Thus local `T1` is genuinely solved.  What is not solved is gluing the `r`
roots of `t^r-A_*` to the actual leading coefficients of `r` source pole
chains in one polynomial pair.

### 2.3 Full-index laws outside `Sigma_cfg`

The exact trunk-edge Statement 3.9 consumer, which the charged interface
deliberately does not include, is

```text
i_F*2=i_G*(2rn)       =>       i_F=rn*i_G.                 (St 3.9)
```

This is the first exact consumer of the unbounded merge index.  It is not a
contradiction: normalization indices are unbounded.  It is, however,
mandatory typed data at actual-source scope.  Any later continuation must
transport these indices at every shear; a reduced `(w,M)` path does not do
so.

One must not silently identify a literal zero-length pole chart with the
merge chart and infer `deg p_pole=4=i_G*mu`, hence `i_G=2`.  The convergent
Grok review notes that this naive MP6(b)/chart identification would equally
kill the already reviewed td12 U1 object.  At abstract-interface scope one
may retain clean-neutral pole-arm interpolations, which preserve
`(w,M)=(3/2,2)` and price zero.  At actual-source scope the arm charts and
their indices must be supplied and transported; `i_G=2` is not banked here.

## 3. One-step trunk theorem, with the missing derivation supplied

Start from `(w_G,M_G)=(3r/2,2)`.  For a dirty epsilon-zero step, arrival
`l=2`, `k>=1` extra non-chain orbits, all `m_j=1`, and `lex=0`, the exact
formulas are

```text
dp   = nu*(k+2),
dq   = nu*(k+1)+1,
E    = k*nu+2,
kbar = 3r*dq/E,
X    = 3r*dp/E,
w_F  = 3r*(k+1)/E,
M_F  = gcd(dp,dq)=gcd(k+2,nu-1).
```

The shape claims are sound: `m_j<dp/dq<2` forces `m_j=1`, and `dq<dp`
removes q-only extra orbits.

Now impose P1: `w_F<1`, `M_F>=2`, and
`j=M_F(1-w_F)` a positive integer.  Since `M_F` divides both `dp,dq`, it
divides `E`; write `E=M_F e`.  In reduced coordinates
`gcd(dq/M_F,e)=1`.  Integrality of

```text
kbar=3r*(dq/M_F)/e
```

therefore gives `e|3r`.  Put `t=3r/e`.  Then

```text
w_F=t*(k+1)/M_F,       j=M_F-t*(k+1)>0.
```

But `M_F<=k+2`.  Hence necessarily `t=1`, `M_F=k+2`, and `j=1`.
It follows that

```text
E=3r*(k+2),       nu=3r+2*(3r-1)/k.
```

Finally `M_F=k+2 | nu-1` forces `2(3r-1)/k` to be even, equivalently
`k | 3r-1`.  Conversely every such divisor satisfies all these equations.
With

```text
A=3r-1,       q=A/k,
```

the closed forms are

```text
nu       = 3r+2q,
kbar     = 3r+q,
X        = nu,
M_F      = k+2,
w_F      = (k+1)/(k+2),
j        = 1,
psi      = k+1,
gap/orbit= q,
floor    = k*q = 3r-1,
budget   = 4r-k-2,
slack    = r-k-1.
```

N1 is automatic:

```text
gcd(kbar,nu)=gcd(3r+q,3r+2q)=gcd(3r,q)=1,
```

because `q | 3r-1`.  Also `gcd(M_F,nu)=1`, `dq==1 (mod nu)`, and the
`(S)`, `(NE)`, `(R)` and divisor guards hold.  Thus the P1-fitting
one-step terminals are precisely

```text
k | 3r-1,       1<=k<=r-1.
```

In particular `k=1` works for every odd `r>=3` and gives

```text
nu=9r-2,       kbar=6r-1,       X=9r-2,
w=(2/3),       M=3,             floor=3r-1,
psi=2,         budget=4r-3,     optimistic slack=r-2.
```

### 3.1 Trunk-local `T1`

For `k=1`, put

```text
p=(t-A)^2(t-B),       q=eta*(t-A)(t-B),
t=eta^nu,             rho=3nu/(2nu+1).
```

The quadratic term cancels identically.  The remaining condition is

```text
B/A=(nu+2)/(nu-1)=3r/(3r-1),
```

and the constant is `rho*A*B!=0` for `A!=0`.  This confirms the claimed
local solution for all odd `r`; it does not glue it to the merge scale
`A_*` or to an actual source coefficient.

### 3.2 Exact status of the budget

The reviewed `POLE-EXIT-ZERO` theorem gives exact zero at all `r` pole
vertices, and U1 gives exact zero at the merge.  The dirty-step number
`3r-1`, however, is an AF2 lower floor.  The actual cluster weight may be
larger unless a separate exact-price theorem is proved.  Therefore

```text
3r-1 <= 4r-k-2
```

means only “not excluded by the current lower floor.”  It does not construct
an actual exit set whose weight equals `3r-1`.  This distinction is already
load-bearing at `r=3`: B25 has one unit of apparent slack, while S17 is
floor-tight.

## 4. What `U1*(r)` does and does not prove

The following statement is rigorous:

> For every odd `r>=3`, the entry, star, U1 merge, one-step `k=1` trunk,
> local merge/trunk `T1` equations, pole-zero theorem, and all displayed
> numerical lower-floor tests admit a mutually consistent reduced packet
> of degree `4r`.

This confirms Theorem NG at its exact stated scope: the enumerated abstract
interface `Sigma_cfg` has a model of degree `4r` for every odd `r`, hence
`Sigma_cfg` alone entails neither `td=12` nor any finite `td` ceiling.  The
independent Grok hostile review reached the same verdict and found no omitted
promoted configuration-level axiom internal to that interface that kills the
family.

`Sigma_cfg` is nevertheless not an actual-source realizability theory.  Work
outside its declared perimeter still has to instantiate:

1. the typed P2/MP6 pole-arm handshakes without conflating pole and merge
   charts;
2. Statement 3.9 sheet transport on the trunk and on every later shear;
3. the U1 domain restriction `n>=2` (repaired here by `n>=5`);
4. actual coefficient/Puiseux-prefix and deck-orbit gluing of all incoming
   chains to one merge polynomial;
5. exact actual cluster weights above the AF2 floors; and
6. a total, provenance-preserving map from an actual source tree to the
   reduced record.

Items 1--3 are compatible with the abstract packet when charts and neutral
arms are kept typed; they do not kill the interface family.  Items 4--6 are
the missing actual-source premises.  Thus the safe verdict is the confirmed
`ABSTRACT-INTERFACE NO-GO`, not occurrence, realizability, or a claim that no
future source theorem can select `td=12`.

## 5. Hostile audit of `PCB`

The proposal is

```text
d >= s + sum_(F in T_cv(a)) wt(F),       wt(F)=kappa_F*(pi(F)-1).
```

Using `d=sum_poles Lambda(P)`, it is equivalently

```text
sum_(F in T_cv(a)) wt(F) <= sum_poles (Lambda(P)-1).       (5.1)
```

So PCB is a new comparison of finite-value critical-direction weight with
the total pole ramification deficit.  No existing theorem in the frozen
corpus states (5.1); exact-expression search finds only the charged proposal.
It is not a duplicate of Corollary 7.1, landing, MFE, or a source bridge.

### 5.1 The exact Section-7 identity and the fatal proof error

For the reviewed quotient lines `U_i ~= A1`, let

```text
I_i = integral_(U_i) w_i dchi_c,
b_i^+ = kappa_i^+*(u_i-1),
wt_i(a)=kappa_i(a)*(u_i-1).
```

The promoted weighted repair proves

```text
d-N = sum_i (phi_i)_! w_i,
d-1 = sum_i I_i,
I_i >= b_i^+ >= wt_i(a).                                  (5.2)
```

The global `1` in (5.2) is not the Euler characteristic of one pole cluster
or of a collection of pole clusters.  It is

```text
integral_(A2) N dchi_c = chi_c(A2_source)=1.
```

Each `U_i` already contributes its own baseline through `I_i>=b_i^+`.
The maps `phi_i` parameterize finite target values `(a,b) in A2`; pole
places have `g=infinity` and do not occur in this pushforward.  Sidedness
proves that exclusion.  It does not turn the excluded pole places into `s`
additional compactly supported components of the same integral.

From (5.2), PCB is **exactly equivalent** to

```text
sum_i (I_i-wt_i(a)) >= s(a)-1.                             (PCB-EXCESS)
```

or, after splitting the known nonnegative terms,

```text
sum_i (I_i-b_i^+) + sum_i (b_i^+-wt_i(a)) >= s(a)-1.
```

Current Section 7 proves only that the left side is nonnegative.  It gives no
unit per pole.  The local specialization proof deliberately transports one
nearby simple direction, not every nearby root: the other roots may have
different `Q_i`-values.  The hostile-reviewed failure of the multiplicity
enhancement is therefore directly adverse to the proposed “one independent
unit per pole cluster” argument.

### 5.2 Riemann--Hurwitz does not repair the sign or the typing

Let the projective normalization of `f=a` have `c` connected components,
total genus `G`, total degree `d`, and `s` pole places.  Since the affine
restriction of `g` is unramified, componentwise Riemann--Hurwitz gives

```text
R_pole    = sum_poles (e_P-1)    = d-s,
R_nonpole = sum_nonpole (e_P-1)  = 2G-2c+d+s.              (5.3)
```

The charged formula `2g-2+d+s` is the special case `c=1`.  A generic fibre
may be connected, but PCB is stated for an arbitrary fibre satisfying the
every-fibre rider; connectedness of that fibre is an omitted premise.

Even in the connected case, (5.3) supplies no PCB arrow.  Indeed

```text
R_nonpole-R_pole = 2*(G+s-c) >= 0,
```

because every component has at least one pole.  Riemann--Hurwitz naturally
makes the physical nonpole ramification at least the pole ramification; PCB
would need the separately typed cv-flag weight to be at most the latter.
In the charged connected counterexample regime `s>=2`, one even has

```text
R_nonpole >= d+s-2 >= d > d-1 >= sum wt,
```

so identifying the RH sum with the Section-7 flag sum would contradict the
promoted bound rather than strengthen it.
FALLACY-v2 forbids identifying a physical place, a cv flag, and a cover
series.  No map from the terms of (5.3) to the excess terms in PCB-EXCESS is
present.

A curve-level negative control makes the logical point.  On `P1`,
`g(t)=t+t^(-1)` has degree two, two simple poles, and two finite ramification
points `t=+/-1`.  Remove all four points: the affine restriction is
unramified, and (5.3) is exact, but there is no inequality forcing finite
ramification below `d-s=0`.  This is not a Keller polynomial-pair
counterexample and does not refute PCB; it refutes the claim that
Riemann--Hurwitz plus affine unramifiedness and pole mass has the required
direction.

### 5.3 Classification and cheapest source audit

The exact classification, matching the independent Grok review, is:

```text
bare PCB on actual Keller maps:               UNSUPPORTED / UNPROVED / NOT REFUTED;
duplicate of a frozen theorem:                NO;
proposed Section-7/pole-cluster proof:         FALSE;
proposed Riemann--Hurwitz transfer:            NOT TYPED;
PCB as a consequence of promoted Section 7:   FALSE;
“PLAUSIBLE_OPEN” campaign label:               NOT LICENSED;
actual Keller counterexample to PCB:           NONE KNOWN.
```

In ordinary logical language the bare inequality remains undecided because
no nonautomorphic Keller map is available to test it.  `UNSUPPORTED` is the
correct campaign status; it must be kept distinct from the **false proposed
derivation**.

The cheapest audit is not a broad pole-cluster reread.  It is a direct audit
of PCB-EXCESS on the already constructed common-resolution quotient package:

1. keep (5.2) unchanged and define each exact excess `I_i-wt_i(a)`;
2. ask whether the resolved boundary graph supplies an injection of `s-1`
   independent pole relations into positive excess events;
3. use as the first negative control the locally allowed situation
   `P_i` linear/unramified and `w_i` constant at its baseline, where every
   excess is zero;
4. if a compactification is invoked, compute its boundary pushforward
   explicitly: the target point at infinity contributes deficit `d-s`, not
   `s` independent affine components; and
5. retain component-aware Riemann--Hurwitz and the flag/place/series firewall.

Proving PCB-EXCESS proves PCB.  Producing source-compatible quotient data
with `s>1` and total excess `<s-1` refutes it.  A merely reduced U1 packet is
only an interface countermodel, not an actual refutation.

## 6. Reconciliation with the quartet, Fable witnesses, and A7/C5 detours

### 6.1 What the quartet still says

The sealed theorem `TD12-U1-FIRST-NONNEUTRAL-QUARTET` remains exact at its
stated conditional reduced tier.  After a provenance-preserving neutral
prefix, every first budget-surviving nonneutral row is one of

```text
A7, C5, B25, S17.
```

The Fable report does not refute it.  Its B/S-free paths begin with A7 or C5,
exactly as the theorem predicts.  What the new report refutes is a different
claim: that the complete multi-step terminal codomain is the two cells
`{B25,S17}`.

### 6.2 Previously banked A7/C5 fixtures

The two exact reduced tails are

```text
A7: (9/2,2) --(21,15; nu=7;  lambda=6)--> (2,3)
              --(63,28; nu=9; lambda=2)--> (6/7,7)
              --(247,39;nu=19;lambda=1)--> (6/13,13),

C5: (9/2,2) --(20,16; nu=5;  lambda=6)--> (9/4,4)
              --(119,35;nu=17;lambda=2)--> (6/7,7)
              --(247,39;nu=19;lambda=1)--> (6/13,13).
```

Both have total lower floor `9`, terminal `j=7`, `psi=1`, and current
ceiling `10`.  Their local `T1` solutions are exact:

```text
A7:       B/A=3/2,                   constant=21*A^2/10;
C5:       B+D=3A, BD=3A^2,           constant=-15*A^3/4;
A-middle: B+D=3A, BD=3A^2,           constant=-27*A^3/4;
C-middle: B/A=3/2,                   constant=51*A^2/10;
H:        B/A=2,                     constant=38*A^2/3.
```

These remain reduced/local fixtures, not glued source paths.

### 6.3 Independent check of the new Fable paths

The three new A7 paths are arithmetically exact:

```text
W1: A7 --(135,55;nu=27;kbar=11;lambda_floor=3)--> (2/5,5),
    total=9, j=3, psi=1, current ceiling=10, T1 ratio B/A=6/5.

W2: A7 --(35,15;nu=7;kbar=9;lambda_floor=2)--> (6/5,5)
        --(117,27;nu=13;kbar=9;lambda_floor=1)--> (2/3,9),
    total=9, j=3, psi=2, current ceiling=9, both T1 ratios B/A=2.

W3: A7 --(35,15;nu=7;kbar=9;lambda_floor=2)--> (6/5,5)
        --(441,99;nu=49;kbar=11;lambda_floor=2)--> (2/9,9),
    total=10, j=7, psi=1, current ceiling=10; final T1 ratio B/A=6/5.
```

The B25 continuation is also exact:

```text
(2/3,3)@25 --(35,15;nu=7;kbar=3;lambda_floor=1)--> (2/5,5),
total=9, psi=1.
```

But it cannot refute “the path contains B25 or S17”: the path contains
B25 at its first row.  It only proves that a P1-legal state is not an
absorbing grammar state unless it is chosen as the last vertex above the
root.

The C5 pure-epsilon route also checks exactly:

```text
C5 -> (9/10,10) on (dp,dq,nu)=(130,40,13), kbar=12, floor=2
   -> (6/19,19) on (893,95,47), kbar=15, floor=1
   -> (1/2,12) by l=19, epsilon=7, nu==11 (mod 12), floor=1.
```

For the final family,

```text
E=12, kbar=(nu+1)/2, M=gcd(12,nu+1)=12,
w=1/2, j=6, psi=1, total floor=10.
```

Its local T1 equation is uniform.  With

```text
p=eta^7*(t-A)^19, q=eta*(t-A), t=eta^nu,
rho=(19nu+7)/(nu+1),
```

the `t` coefficient cancels and the constant is
`-(rho-7)A=-12nu*A/(nu+1)!=0`.  The preceding three-root cell has
`B+D=3A`, `BD=3A^2`, and the two-root cell has `B/A=3/2`.

Thus the individual Fable witnesses are exact reduced/local solutions.
Their prices are still floors, their full Statement-3.9 index transports
and cross-row coefficients are not instantiated, and no source Puiseux
prefix or actual tree is constructed.  The scratch counts `83` states and
approximately `517` cells remain unreviewed superset diagnostics, not a
theorem.

### 6.4 PCB against every displayed td12 fixture

If PCB were proved and if the displayed floors were attached to pairwise
distinct actual first-separation flags, its ceiling would be `12-3-psi`:

| route | floor | `psi` | current ceiling | PCB ceiling | result under PCB |
|---|---:|---:|---:|---:|---|
| direct B25 | 8 | 2 | 9 | 7 | killed |
| direct S17 | 8 | 3 | 8 | 6 | killed |
| either banked A7/C5 tail | 9 | 1 | 10 | 8 | killed |
| W1 | 9 | 1 | 10 | 8 | killed |
| W2 | 9 | 2 | 9 | 7 | killed |
| W3 | 10 | 1 | 10 | 8 | killed |
| C5 pure-epsilon family | 10 | 1 | 10 | 8 | killed |
| B25 continuation | 9 | 1 | 10 | 8 | killed after already meeting B25 |

PCB would therefore bypass, not prove, B25/S17 occurrence: it would
contradict every listed U1 continuation once actual attachment is available.
That strategic power is exactly why PCB-EXCESS needs a source proof rather
than a reinterpretation of the existing Euler constant.

## 7. The canonical route that survives

Do not promote a two-cell terminal-closure theorem.  Retain the quartet as
the exact first-event theorem and refine the previously named actual-source
packet to

### `TD12-U1-FAMILY-AWARE-DETOUR-EXCLUSION/v2`

Inputs:

1. one exact normalized td12 pair, fibre, U1 merge, all pole places, and the
   complete source Puiseux prefixes;
2. merge index `n`, the exact relation `i_F=3n*i_G` on the first trunk edge,
   separately typed pole-arm indices/charts, and full indices through every
   later shear;
3. every neutral prefix retained with provenance;
4. the banked A7/C5 tails, Fable `W1--W3`, the C5 pure-epsilon family, and
   their local `T1` witnesses as adversarial fixtures; and
5. B25/S17 as occurrence states, not assumed absorbing terminals.

Required proof obligations:

1. prove a fail-closed, actual-to-reduced, family-aware trunk map; the Fable
   `MERGE-FREE-TRUNK-TERMINAL-CLOSURE` is a plausible infrastructure lemma,
   but its grammar-totality and single-chain terminal-typing riders remain
   open;
2. instantiate Statements 3.7/3.9/3.18 and the full index ledger on every
   fixture rather than merely checking `(w,M,nu)`;
3. glue the displayed local `T1` ratios across source coefficients, deck
   actions, root choices, and the U1 `t^3-A_*` merge;
4. compute exact actual cluster prices whenever a floor-tight path is used;
5. serialize pairwise-distinct first-separation flags before applying either
   Corollary 7.1 or a future PCB; and
6. classify every family-record fibre, with the pure-epsilon congruence
   retained rather than truncated to literal cells.

Verdicts:

```text
PROVED_FAMILY_AWARE_EXCLUSION:
  every actual B/S-free A7 or C5 continuation contradicts;

REFUTED_BY_ACTUAL_SOURCE_TAIL:
  one exact source-compatible B/S-free tail reaches the root;

SOURCE_TRANSPORT_OPEN:
  only reduced/local closure is obtained;

PCB_BYPASS:
  PCB-EXCESS is independently proved and kills the actual U1 route.
```

Under `SOURCE_TRANSPORT_OPEN`, do not emit a B/S occurrence, route kill,
degree ceiling, `PairRef`, or JC2 conclusion.  The new reduced witnesses
make source typing more important; they do not make the actual-source lemma
false.

## 8. Final disposition and firewall

Bank as exact:

- the corrected `U1*(r)` entry, merge, local `T1`, trunk, and lower-floor
  closed forms, with `n>=5`;
- the no-`td`-ceiling conclusion relative exactly to the enumerated abstract
  interface `Sigma_cfg`;
- universal exact pole-zero;
- the quartet first-event theorem;
- the banked A7/C5 and individually checked Fable reduced fixtures.

Do not bank as theorem:

- any extension of the interface no-go to actual occurrence or realizability;
- equality of actual dirty-cell prices with AF2 floors;
- a two-cell multi-step terminal codomain;
- PCB or any `s`-unit Euler decomposition;
- a flag/place/cover-series identification;
- actual occurrence, source gluing, td selection, or a JC2 conclusion.

The cheapest global discriminator is `PCB-EXCESS`.  The cheapest local
discriminator is the family-aware actual-source detour packet above.  They
are complementary: the former would bypass occurrence; the latter is the
minimal route if PCB fails or remains open.

<!-- END-SEALED-BODY::u1-star-pcb-independent-audit-sol56-93d-20260829 -->

## Seal

- Body definition: every byte from the first byte through the unique body-end
  marker line, including its terminating newline.
- Body byte count: `25131`.
- Body SHA-256:
  `4073cc92bf44057018a42440de72b8865105a4c9f3d8825a20ec4de300013d09`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
