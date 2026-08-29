# Q+E5 equal-regime state-slot map and exact fixed-index existence consumer (R1)

Producer: GPT-5.6-Sol. Date: 2026-08-29. Lifecycle:
`PROVISIONAL_SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`. This is a bounded
merge-local desk-algebra report. It does not edit, run, or authorize an edit
to the legacy engine or any canonical file.

## Verdict

**The promoted Q+E5 fixed-pattern theorem passes at its reviewed scope, but
the advertised equal-regime consumer is not yet type-correct.** Four facts
must be separated.

1. For a fixed two-pole case-III state and fixed menu entry, R3's finite
   pattern-fibre theorem is sound at its stated `delta >= 1` scope.
2. At `delta = mu0-mu = 0`, a direct proof gives a finite integer
   `kbar_G` menu. With the target `M_G` and the forced target index `nu_G`
   supplied as slots, each menu value determines `(dp,dq,s,Sm)` uniquely,
   and R2.2-pattern existence is decided by one exact bounded-multiplicity
   inequality. No numerical cap and no partition search are needed.
3. The proposed call to legacy `cell_check(kbar,X,[mu],mu0,M_G)` is **not**
   this consumer. `cell_check` has no fixed-`nu_G` argument and searches all
   admissible indices, including `nu=1`; it also does not enforce N1
   `gcd(kbar_G,nu_G)=1`. An explicit profile below is accepted only through
   `nu=3` although Q+E5 forces `nu_G=2`.
4. Pattern existence is not edge or route realization. Full promotion still
   needs arrival provenance, `M_U`, the free incoming `nu_U` vertex,
   positive E5 offsets, and full-degree/i synchronization. These are record
   slots, not consequences of the pattern theorem.

The clean fix is a new pure, fixed-index consumer with the schema and exact
predicate in Sections 3--5. It should be reviewed and certified separately
before any engine migration. `NUCAP=500` and every legacy verdict remain
untouched.

## 1. Exact evidence and source boundary

Hashes are SHA-256 of the exact bytes read for this report.

| Source | SHA-256 | Exact use |
|---|---|---|
| `ladder/REDUCTION.md` | `b0b6c276b1fe28a9b94556e29a058264201267dfc496b3100c416f027bc7aa0f` | T7 gives entries, not configurations (`:520-534`); T8 lacks a typed configuration-to-record map and full downstream coverage (`:538-606`); T9(c) leaves off-axis `nu`, `kbar`, full-pattern and partner data unquotiented (`:661-694`); T10 is not established (`:698-727`); CRITICAL 4 requires typed provenance and fail-closed coverage (`:949-987`). |
| `ladder/BOOK-OFFAXIS.md` | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | Case typing and R2.1 handshakes (`:315-339`); R2.2 factor shapes, degree laws, S/NE/R and `M_G=gcd(dp,dq)` (`:341-368`); E5 distinguishes target `nu_G` from incoming `nu_U` and requires a priced arrival state with `mu0 | M_U` (`:739-766`). |
| `ladder/SHEET6-DEPTH.md` | `ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d` | `kbar_G` integrality at a `nu_G>=2` characteristic vertex (`:112-134`); the 0-edge is case III only for `nu_G>=2`, while `nu_G=1` is case I (`:278-302`). |
| `ladder/SHEET6-III.md` | `59a2fa489f7f999b24aabc4c707254b7e54f8db02d69690226754e3224f9bdda` | N1: `kbar_G in Z` and `gcd(kbar_G,nu_G)=1`; Q/max and E5 (`:123-150`). |
| `ladder/SHEET6-MULTIPOLE.md` | `93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb` | Tree/merge slot meanings (`:65-72`), merge localization (`:76-101`), and the full-degree common-quotient obligation. |
| `xmodel/sol-h5a.md` | `dd09069baeeaaa38644963571f929077af016cbbac664aaea9f3f50bee8f6d90` | Campaign/thesis orientation and distinct `nu_G,nu_U` (`:46-61`); Q/max (`:65-80`); E5 derivation (`:137-192`). |
| `xmodel/grok-h5a-review.md` | `3b8bd5c9e2a1f4132cff4353e0e7e0fd9b4426cbeea0b0c13d092161018f5d2f` | Different-model confirmation of Q+E5 and rejection of an implicit equal-index law (`:1-20,95-125`). |
| `xmodel/m2-caseiii-two-pole-e5-local-index-r3-repair-fable5-20260829.md` | `885e5cc261449890e23d54cb024f19f339424f6138938d2396c2e655244c7092` | Exact fixed-state hypotheses and Theorems A--D (`:70-129`); proposed migration interface (`:355-409`); explicit firewall (`:498-515`). |
| `xmodel/m2-caseiii-two-pole-e5-local-index-r3-hostile-review-opus5-20260829.md` | `9660ffe9302061c9daf7bc31c8eda57fb9412315283c868d8d072655d2033570` | `PASS_WITH_REPAIR`; case-I fractional-`kbar` countercontrol (`:355-393`); maximum safe consequence and exact exclusions (`:416-462`); proposed `delta=0` successor (`:464-483`). |
| `ladder/TOWER-UNIFORM.md` | `d996f57b8281d821753d773d88ebc5ee5d957fe2f6ffab5e0fe84e306842b872` | Arrival-vertex E5 offset `n_U=nu_U*kbar_G-nu_G*kbar_U>=1` and its equivalent form (`:147-162`). |
| `cases/book_offaxis.py` | `c22e3a1f977fef94022f34378232fcc78148fa506501f71ec6a57313d6042ebc` | Read-only interface audit: `cell_check` constructs degrees but loops over every `nu` (`:219-265`); `solve_arr`'s equal branch returns without a pattern solve (`:273-357`). It was not imported, run, or modified. |

The campaign-level boundary is important. `REDUCTION` proves no universal
`B(td,entry)` and no total off-axis configuration compiler. The result below
is therefore a typed local consumer for a record already known to satisfy
its input contract. It is not a new landing theorem.

## 2. What is promoted, what is new, and what is broken

### 2.1 Preserved promoted layer

Fix the reviewed Q/max reading and E5. A two-pole case-III target `G` has:

- exactly one nonzero pole-chain arrival of multiplicity `mu` and invariant
  `w>0`;
- one pole-chain 0-arrival of multiplicity `mu0`, invariant `w_U>0`, and
  priced state divisor `M_U`;
- no inner arrivals;
- target index `nu=nu_G>=2`;
- reduced target degrees

  ```text
  dp = mu0 + nu*(mu + Sm),
  dq = 1 + nu*(1 + s),
  s  = k + lex,
  Sm = sum(m_j),
  ```

  with S, strict NE, R, `M_G=gcd(dp,dq)`, and N1.

Writing `delta=mu0-mu`, `D=mu*dq-dp`, `A=mu*s-Sm`, the case-II
nonzero handshake and E5 0-handshake give

```text
X_G = mu*(kbar_G-w),
X_G/kbar_G = dp/dq,
mu0*nu_G*w_U = delta*kbar_G + mu*w.
```

At `delta=0`, the last equation forces the **target** index

```text
nu_G = w/w_U.
```

It does not force or enumerate the incoming zero-edge vertex index `nu_U`.

### 2.2 Two interface defects in the advertised consumer

The R3 migration sketch correctly observes that the equal branch has no
pattern solve, but it does not yet bind all of the slots it uses:

- its input destructures `zero` as `(mu0,w_U,nu_i)` and later calls
  `arrival_state_legal(mu0,M_U)`, although `M_U` is not in that tuple;
- the suggested successor invokes `cell_check`, whose signature contains no
  `nu_G`. The function reconstructs `(dp,dq)` from `M_G*red(X/kbar)` and
  then loops over every divisor index, explicitly including `nu=1`.

The second defect is mathematical, not cosmetic: Q+E5 fixes `nu_G`, and a
pattern at another index is a different target vertex. Section 6.2 gives an
exact false-positive profile. In addition, `cell_check` enforces integer
`kbar` for a tested `nu>=2` but never enforces N1
`gcd(kbar_G,nu_G)=1`.

### 2.3 Theorem D is not silently extended

R3 Theorem D is stated for `delta>=1`. Its proof algebra extends to
`delta=0`, but this report does not cite the statement outside its domain.
Sections 4--5 give a separate direct `delta=0` proof. With fixed `M_G`, the
result is stronger and simpler: a candidate `kbar_G` determines one degree
pair, so no fibre search is needed for the existence verdict.

## 3. Explicit state-slot map

### 3.1 Input record

The minimal fail-closed input is the following. “Fixed” means fixed before
the local existential search.

| Slot | Type | Status | Source/use |
|---|---|---|---|
| `reading` | enum | fixed, must be `Q_MAX_E5` | Prevents mixing E5 with printed `(g)/(h)` or the open `U_7C` equality. |
| `target_id` | opaque vertex/provenance id | fixed | Required by `REDUCTION`'s typed-map/provenance obligation. |
| `target_case` | enum | fixed, must be `III` | A structural two-arrival shape does not distinguish case I. |
| `target_case_certificate` | source pointer/hash | fixed | Must establish interior 0-direction and `nu_G>=2`; absence means fallback, not `DEAD`. |
| `r0` | positive integer | fixed, must be `1` | Exactly one nonzero pole-chain arrival. |
| `inner_arrivals` | list | fixed, must be empty | The reviewed Q+E5 theorem excludes inner arrivals. |
| `mu,w` | `N* x Q_{>0}` | fixed | Nonzero-arrival multiplicity and reduced invariant. |
| `M_H` | `N*` plus provenance | fixed | Check `mu | M_H`; omitted in the compressed theorem state but needed by a route record. |
| `mu0,w_U,M_U` | `N* x Q_{>0} x N*` | fixed | 0-arrival reduced state; check `mu0 | M_U`. This binds the missing R3 pseudocode slot. |
| `arrival_vertex_set_U` | finite/provenanced set or an explicit witness | fixed | Contains legal incoming `(nu_U,kbar_U,rho_U,degp_U,edge_id)` records. Under E5, `nu_U` is free relative to `nu_G`, not absent. |
| `M_G` | `N*` | fixed | Target gcd slot. It is not derivable from `(mu,w,mu0,w_U)` and is required to reconstruct exact degrees. |
| `unused_branches` | typed list | fixed, empty at this local scope | Prevents a two-pole theorem from silently dropping additional arrivals. |
| `downstream_context` | opaque pointer | fixed | Preserves the consumer/route context; this theorem does not inspect it. |

The equal-regime preconditions and derived target slot are

```text
mu0 = mu,
delta = 0,
nu_G = w/w_U in Z,  nu_G >= 2,
mu | M_H,  mu | M_U.
```

Failure of the first equation routes to another Q+E5 regime. Failure to
establish `target_case=III` routes to the legacy/open branch. If case III is
already certified, a nonintegral or `<2` value of `w/w_U` is a local death.

### 3.2 Enumerated and derived pattern slots

For each integer menu candidate `K=kbar_G`, derive, rather than search:

| Slot | Formula/domain |
|---|---|
| `kbar_G` | enumerated `K in Z`, `K>w`, `gcd(K,nu_G)=1` |
| `X_G` | `mu*(K-w)>0` |
| `(a,b)` | positive coprime numerator/denominator of `X_G/K` |
| `(dp,dq)` | `(M_G*a,M_G*b)`; hence `gcd(dp,dq)=M_G` exactly |
| `D` | `mu*dq-dp` |
| `s` | `(dq-1)/nu_G - 1` |
| `Sm` | `(dp-mu)/nu_G - mu` |
| `mmax` | `floor((dp-1)/dq)`, the exact strict-NE multiplicity cap |
| `kmin` | `ceil(Sm/mmax)` when `Sm>0` |
| `(k,lex,mults)` | canonical witness described in Section 5, or a finite list if a downstream consumer needs every pattern |

Output status must be typed:

```text
PATTERN_DEAD
PATTERN_EXISTS_REALIZATION_UNCHECKED
EDGE_REALIZED_FOR_EXPLICIT_ARRIVAL_WITNESS
```

The local predicate may return only the first two. The third requires the
additional slots in Section 3.3.

### 3.3 Edge/route realization slots deliberately outside the pattern solve

For every explicit arrival witness retained by a route record, check:

1. nonzero-edge full offset
   `n_H = nu_H*kbar_G-kbar_H in N*` (BOOK R2.1 orientation);
2. zero-edge E5 offset
   `n_U = nu_U*kbar_G-nu_G*kbar_U in N*`, equivalently the reviewed E5F
   identity in `TOWER-UNIFORM`;
3. the common full-degree quotient/i-sync, including the exact source-backed
   equality `deg(p_H)=i_G*mu` and the corresponding 0-edge/full-product
   synchronization;
4. the priced-path, arrival-class, budget, downstream and unused-branch
   provenance carried by the enclosing route record.

The compressed state `(mu,w,mu0,w_U)` has none of these full fields. A
successful pattern solve cannot manufacture them.

## 4. Equal-regime finite-menu theorem

### Proposition 4.1 (cap, fixed-index form)

Under the Section 3.1 contract, every R2.2-admissible equal-regime pattern
satisfies

```text
D = nu_G*A,
A = mu*s-Sm >= s >= 1,
dq/D <= 2 + 1/(M_G*nu_G),
kbar_G <= mu*w*(2 + 1/(M_G*nu_G)).
```

Consequently the exact candidate menu is finite:

```text
Kset = { K in Z : w < K <= mu*w*(2 + 1/(M_G*nu_G)),
                  gcd(K,nu_G)=1 }.
```

This sharpens the review's safe `2+1/M_G` cap.

**Proof.** In the equal regime,

```text
D = mu[1+nu(1+s)] - [mu+nu(mu+Sm)]
  = nu(mu*s-Sm) = nu*A.
```

Strict NE gives every nonchain multiplicity `m_j<=mu-1`. Hence

```text
A = mu(k+lex)-Sm >= k+mu*lex >= k+lex=s.
```

Since `D>0`, `s=0` is impossible, so `s>=1`. Therefore

```text
dq = 1+nu(1+s) <= 1+nu+D <= 1+2D,
```

because `D=nu*A>=nu`. Also `M_G=gcd(dp,dq)` divides
`D=mu*dq-dp`; R2.2 gives `dq=1 mod nu`, so
`gcd(M_G,nu)=1`. Thus `M_G*nu | D`, and

```text
dq/D <= 2+1/D <= 2+1/(M_G*nu).
```

Finally the nonzero-edge handshake and ratio identity give

```text
mu*(K-w)/K = dp/dq
=> K = mu*w*dq/(mu*dq-dp) = mu*w*dq/D.
```

N1 supplies integer `K` and `gcd(K,nu)=1`. This proves the menu. The ratio
bound is attained at the pattern-law tier when `s=A=1`, where `D=nu` and
`M_G=1`; attainment of an integer/N1 menu value depends on `w`. QED.

## 5. Exact fixed-index existence predicate

### Proposition 5.1 (no partition search)

Fix a Section 3.1 record and `K in Kset`. Put

```text
X = mu*(K-w),
(a,b) = reduced positive fraction X/K,
dp = M_G*a,  dq = M_G*b.
```

There exists an R2.2 factor-pattern witness at the **forced** target index
`nu=nu_G` if and only if all of the following exact checks pass:

1. `dq == 1 (mod nu)` and `dp == mu (mod nu)`;
2. `s=(dq-1)/nu-1` and `Sm=(dp-mu)/nu-mu` are integers with
   `s>=1`, `Sm>=0`;
3. `D=mu*dq-dp=nu*(mu*s-Sm)>0` and
   `K*D=mu*w*dq` exactly;
4. if `Sm=0`, take `k=0`, `lex=s`;
5. if `Sm>0`, require `dq<dp`, put
   `mmax=floor((dp-1)/dq)>=1` and
   `kmin=ceil(Sm/mmax)`, and require `kmin<=s`. Then take
   `k=kmin`, `lex=s-k`, and any positive `k`-part partition of `Sm`
   with every part at most `mmax`.

The partition in item 5 always exists once its inequality passes: by the
definition of `kmin`, `Sm<=kmin*mmax`, while `mmax>=1` gives
`kmin<=Sm`; distribute `Sm-kmin` extra units among `kmin` initial ones,
never exceeding `mmax`.

**Proof of equivalence.** R2.2 gives exactly the two congruences and the
formulas for `s,Sm`. If `Sm>0`, at least one nonchain orbit exists. Strict
NE is precisely `m_j*dq<dp`, hence
`1<=m_j<=floor((dp-1)/dq)=mmax`; `k<=s` is precisely the availability of
`lex=s-k` q-only orbits. A bounded positive partition exists exactly when
`ceil(Sm/mmax)<=s`. Conversely the constructed multiplicities, one
nonzero arrival orbit, the zero factor of multiplicity `mu`, and `lex`
simple q-only orbits realize the R2.2 factor degrees. S holds because
`D>0`; R holds for the arrival multiplicity by `D>0` and for each
nonchain multiplicity by strict NE. `M_G=gcd(dp,dq)` holds by construction.
QED.

This is an equivalence for the promoted **R2.2 factor-pattern grammar**.
It is not an existence theorem for a solution of the full Proposition
8.1(iv) ODE, an actual Puiseux edge, a polynomial Keller pair, or a route.

### Corollary 5.2 (finite exact consumer)

Loop over the finite `Kset`, apply Proposition 5.1 at the single forced
`nu_G`, and return all witnesses or `PATTERN_DEAD`. This proves the desired
equal-regime pattern-level decidability without importing or modifying the
legacy engine.

## 6. Controls

### 6.1 Positive boundary control

Take

```text
mu=mu0=2, w=1, w_U=1/2, nu_G=2, M_G=1,
K=5, X=8, (dp,dq,D)=(8,5,2).
```

The cap is attained:
`K=mu*w*(2+1/(M_G*nu_G))=5`; N1 is `gcd(5,2)=1`.
The predicate gives `s=1`, `Sm=1`, `mmax=1`, `k=1`, `lex=0`, with formal
shape

```text
p_red = eta^2 (eta^2-c^2)^2 (eta^2-d^2),
q     = eta   (eta^2-c^2)   (eta^2-d^2).
```

This is a pattern-positive control only. In an interior-trunk context,
`M_G=1` is separately MP2-dead.

### 6.2 Fixed-`nu_G` leakage control (new)

Take the equal-state profile

```text
mu=mu0=2, w=3/2, w_U=3/4, forced nu_G=2, M_G=1,
K=7, X=11, (dp,dq)=(11,7).
```

It lies inside the cap and passes target N1. At the forced index `nu_G=2`,
`(dp-mu)/nu = 9/2` is not integral, so no target pattern exists. But at
`nu=3` the same degrees have `s=1`, `Sm=1` and the valid R2.2 shape

```text
p_red = eta^2 (eta^3-c^3)^2 (eta^3-d^3),
q     = eta   (eta^3-c^3)   (eta^3-d^3).
```

Thus an unrestricted predicate that loops over `nu` returns a false
positive for the Q+E5 target. This proves that adding a finite `K` loop
around legacy `cell_check` is not a clean fix; `nu_G` must be a typed input.

### 6.3 Required typed case-I fractional-`kbar` negative control

Use the reviewed fixture

```text
target_case=I, nu_G=1,
mu=2, mu0=3, w=1, w_U=3/2, M_G=1,
kbar_G=5/2, X_G=3, (dp,dq)=(6,5).
```

It satisfies the case-I/R2.2 arithmetic with, for distinct nonzero roots,

```text
p_red = eta^3 (eta-a)^2 (eta-b),
q     = eta   (eta-a)   (eta-b)(eta-c)(eta-d).
```

S and strict NE read `2*5>6`, `3*5>6`, `1*5<6`; R and
`gcd(dp,dq)=1` also pass. This is not claimed to solve the ODE or realize a
Keller edge. It is the fail-closed routing control: `nu_G=1` is case I,
fractional `kbar_G` is legal at this tier, and the Q+E5 integer-menu consumer
must return `NOT_APPLICABLE/FALLBACK`, never `DEAD`.

## 7. Stop conditions and maximum consequence

Stop or fall back, without a local kill, if any of the following occurs:

1. `target_case=III` and `nu_G>=2` are not source-certified;
2. the reading is not explicitly Q/max+E5;
3. the target has another nonzero arrival, an inner arrival, or an untyped
   unused branch;
4. `M_G`, `M_U`, arrival provenance, or the distinction `nu_G != nu_U`
   is absent;
5. `mu0!=mu` (route to another regime);
6. a caller asks a pattern verdict to certify i-sync, positive offsets,
   budget, source landing, or coefficient realization.

Inside the certified contract, a nonintegral or `<2` forced `w/w_U`, an
empty `Kset`, or failure of Proposition 5.1 for every `K` proves
`PATTERN_DEAD` at this local grammar. A success proves only
`PATTERN_EXISTS_REALIZATION_UNCHECKED` until Section 3.3 is discharged.

Nothing here proves a total off-axis book, a full configuration compiler,
arrival/route completeness, the Proposition 8.1(iv) ODE, source landing,
polynomial realizability, a topological-degree bound, a Keller
counterexample, or JC2. It does not remove or alter `NUCAP=500`.

## 8. Cheapest next exact solve

The cheapest next step is a standalone, exact-rational certificate for the
Section 5 predicate, not an engine edit:

1. accept only declared Section 3.1 records;
2. enumerate the proved finite `Kset` at the forced `nu_G`;
3. emit `(K,X,dp,dq,D,s,Sm,k,lex,mmax)` plus a canonical multiplicity
   witness and every failed gate;
4. permanently include the three controls in Section 6, especially the
   wrong-index and fractional-case-I controls;
5. compare against the legacy predicate only as a regression diagnostic,
   never as the proof oracle.

Once differently reviewed, this closes the equal-regime **pattern-existence**
slot. The next mathematical datum is then explicit arrival realization:
apply the E5 offset and i-sync checks to the finite surviving cells using
full arrival-vertex records. If those full records are unavailable, that is
the precise stop datum; reduced `(w,M)` states alone cannot answer it.

*End of sealed report body.*

## Seal

- Body definition: all bytes before the literal `## Seal` heading.
- Body byte count: `18948`.
- Body SHA-256: `b27e7436eab58c75fbf5949626214c50942ff9ec6316b65a6069e765e7cecd91`.
