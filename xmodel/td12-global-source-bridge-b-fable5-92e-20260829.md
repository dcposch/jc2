# Fable 5 primary — TD12-GLOBAL-SOURCE-BRIDGE-B/v1: the nu=25 B route's global source bridge

Lane: Fable 5, equal independent primary researcher (not review). Date: 2026-08-29.
Git basis, verified at session start and re-verified immediately before sealing:

```text
92ebe92ad5986a47f01af9ed901260595dfed869
```

Task: own `TD12-GLOBAL-SOURCE-BRIDGE-B/v1`. Starting from an arbitrary
hypothetical minimal counterexample whose reduced tree realizes the named
type-`(2,3)` B state `(nu,kbar,X,M,w) = (25,17,25,3,2/3)`, seek a
source-backed bridge from the global polynomial pair / support / minimality /
approximate-root data to a finite local coefficient packet or to a genuine
nonabsorbable constraint at `s* = D_F + D_g - kbar_F`. The sibling `nu=17`
route is kept completely separate: no statement below concerns it, and no
object below is shared with it (route separation per the R1 erratum).

Worked only in `/Users/dc/code/math/jc2`. No access of any kind to
`jc2-lean`. No web, AWS, remote shell, CAS, or heavy computation; exact desk
algebra plus one small stdlib `Fraction` corroboration script in
`/tmp/b25bridge/` (§4.6). One repository file written: this report. No
commit, no push, no edit to any other file.

## 0. Custody

Recomputed with `shasum -a 256` before reading and again before sealing;
all matched the frozen manifest both times:

```text
7af80df724d880a47452de96a731ff1c4e17b8244fdbae8fc76eb1461e7bcc22  xmodel/post1224-next-wave-packet-20260829T1335Z.md
  (body 6730 bytes, body sha 7a6ce89e9858572b1a7e1cc3c06217145fb7f0e29f2d727b5959c8b0a0abce65, verified)
9677e2edf9848e81beac51cc9ed091c13cd934f912bc337b6ab8e25a5da86861  xmodel/roundview-20260829T1335Z-92ebe92a.md   (GENERATED_NON_AUTHORITATIVE; orientation only)
0f16187346628e881628d545f43eecdc26cecdd0cc908977a16f82902a91c8af  APPROACHES.md
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
79df783a0ed9e370621e750f4e6564dc9871b53e1481898e77dcdd037711ad1c  xmodel/td12-bchild-v1-minimal-source-packet-audit-r1-erratum-sol56-76c-20260829.md
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
4c3f2236a11f296f7eb194bb26e8cdc8ff0b91f10d8d7151e6314caa62629304  xmodel/g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md
f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1  xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md
29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b  ladder/REDUCTION.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
```

Also read for dedup only: the formal-cascade Opus review
`xmodel/td12-formal-cascade-rank-v1-hostile-review-opus5-ccb-20260829.md`
(body sha `66b15f5d...` per the coordinator integration).

Passages actually charged. Printed source (via the two independent prior
verifications, not fresh fraction reads; stacked-fraction hazard respected):
Notation 3.9 / Statement 3.7(5) / Notations 3.10–3.11 (pp. 13–15),
Proposition 4.1 with the chart identity `J(f^F,(g-b)^F)=xi^{-n/kappa}`
(p. 18), Proposition 4.2 with its repaired tower `h_0=g`,
`h_{j+1}=h_j^{k_j}-s_j f^{l_j}` and Proposition 4.4 prefix law (pp. 19–21),
Proposition 8.1(i),(iv) (pp. 39–41) — all exactly as charged and re-verified
by the TD12-BCHILD primary §0/§2 and the Sol disposition §0/§2. Campaign
results consumed at their promoted scopes: the exact recurrence `(E_s)` with
RHS `kappa_F * 1_(s=s*)` (bchild primary §2.3; disposition §2 PASS); order-0
factorization `G_0 = c_g p^r` (bchild §3.1; disposition §2); the type pin
`D_g/D_F = 3/2`, `r = 3i/2`, `i` even (disposition §1 repair 2, §8 of the
formal-cascade review); Theorem D weight law `e_k == 22k (mod 25)` (bchild
§2.2/§4); the trunk cell state, patterns `p=(t-A)^2(t-B)`, `q=eta(t-A)(t-B)`,
`t=eta^{25}`, normalized 8.1(iv) `rho p q' - p' q = C_iv p`, `rho=25/17`,
unique ratio `B/A=9/8`, `C_iv=(25/17)AB` (trunk consumer §3, review-passed
clauses); N1 `gcd(kbar,nu)=1` (trunk consumer §2.2, from SHEET6-III §3);
`P_0 = lambda_f p^i` (Prop 8.1(i) per the audit table); the promoted formal
envelope and its binding disposition (coordinator integration §§1–2);
T2/T4/T6/T7 of `ladder/REDUCTION.md`; interface Theorem 2.1 /
Proposition 3.1 / Theorem 4.1 (typed pair-to-tree constructor). The `i = 6n`
direct-entry rider is NOT consumed (nothing below needs it; only `i in 2N*`).

## 1. Verdict

```text
disposition:            SOURCE_BRIDGE_ESTABLISHED_AT_CONDITIONAL_SCOPE
  functorial bridge:    YES (Theorem A: every field of TD12LocalPairJet_B is a
                        well-defined functional of a hypothetical pair + occurrence)
  universal packet:     YES as a scheme (Theorem B), NOT finite-dimensional
                        (blocker CAP-B25)
  s* constraint:        YES, typed and exact (Theorem C): the J=0
                        fractional-power closure can never absorb the landing
                        row; the landing is forced to sit exactly at s*, and
                        its unique solution is gamma * q * p^(-i)
  route kill:           NONE AT THIS TIER: landing solvability is equivalent
                        to the already-promoted T1 ratio B/A = 9/8
  finite value emission: STILL_BLOCKED (CAP-B25, OCCURRENCE-B25, window
                        underdetermination per the bchild verdict)
charge_basis_status:    ABSENT (no new exit price asserted; correct per task)
```

Answer to the packet's central question ("does the campaign's reduction
actually map that pair to this route with enough functorial data to define
the required local coefficients?"): **YES at definition level.** A
hypothetical minimal counterexample is an exact pair; T2/T4 select and
normalize it; interface Theorem 2.1 constructs its decorated tree and
completions functorially; Notation 3.9 / Statement 3.7 then define every
graded piece `P_k, G_k` as an exact functional of the pair and the
occurrence witness. What the reduction does **not** supply is (a) any
occurrence theorem, (b) any support cap making the packet
finite-dimensional over all candidate pairs, and (c) any value of a `k>=1`
piece from route data alone (the promoted bchild underdetermination).

The centerpiece is Theorem C: over the graded completion at the trunk
vertex, the g-side of an actual pair deviates from the fractional-power
algebra of `f^F` along a finite ledger whose orders are forced into
`25 Z` until they land **exactly** at `s* = 25(i+r) - 17 ≡ 8 (mod 25)`;
N1 (`gcd(kbar,nu)=1`) is exactly the statement that the landing order is
never absorbable. The landing row is an explicit first-order inhomogeneous
ODE whose solvability in the on-weight ring is **equivalent** to the
Proposition 8.1(iv) cell identity — i.e. to the promoted `B/A = 9/8` T1
solve — and whose solution is then unique with pinned scale

```text
T = gamma * q * p^(-i),   gamma = kbar-side scale = kappa_F / (25 i lambda_f A B)
                                = kappa_F / (1800 i lambda_f u^2)  at (A,B)=(8u,9u).
```

Consequences: the "distant inhomogeneous row" target is, at leading order,
**already spent** — it re-derives exactly the surviving T1 content, so no
naive `s*`-attack can kill the route with route-local data; the genuinely
unspent Keller content starts at the row `s*+1`, is forward-rigid except at
the resonant rows `j ≡ 17 (mod 25)` below the landing, and at the first
resonant row `s* + 17` reduces to exactly **two residue conditions** (one
per root orbit) coupling the window pieces `P_1..P_17` — the first-child
data — to the landed rigid tail. That is the correct future kill/emission
lane and the smallest nonduplicate descendant (§10).

Nothing here is a germ, a Keller pair, an occurrence proof, a gate verdict,
a landing/coverage theorem, a `td` bound, or any JC2 consequence.

## 2. Q1 — the functorial bridge (Theorem A)

### 2.1 Statement

> **Theorem A.** For every pair `(f,g) in C[x,y]^2` with `J(f,g)=1` that is
> not a polynomial automorphism (T1 hypothesis of `ladder/REDUCTION.md`),
> Sigray-normalized of type `(2,3)` (T4), and for every occurrence witness
> `(a, S, F)` — a fibre value `a`, a y-side boundary branch `S`, and an
> interior vertex `F in T_a^+ ∩ V_{1,a}` of the decorated tree `DPT_a(f,g)`
> whose reduced state equals `(nu_F,kbar_F,X,M,w) = (25,17,25,3,2/3)` with
> full top `P_0 = lambda_f p^i`, `p = (t-A)^2(t-B)`, `t = eta^{25}` — every
> field of the audit's `TD12LocalPairJet_B` is a well-defined function of
> `((f,g), a, S, F)` up to the recorded deck/gauge orbit:
>
> 1. `PairRef_B := (f,g)` itself, with `J=1` certificate by hypothesis;
> 2. the completion `iota_S` and the Notation 3.9 chart: interface
>    Theorem 2.1 (exact pair constructor) and Proposition 3.1 (local flagged
>    transport) — the completion is not an extra datum, it is constructed;
> 3. the pieces `P_k := p_{f, n_f - Qk}`, `G_k := p_{g, n_g - Qk}` for all
>    `k >= 0` (Statement 3.7(5) + the reviewed Theorem D re-indexing), each
>    an exact polynomial functional of the coefficients of `f` (resp. `g`)
>    and the finite Puiseux prefix of `S` below `F`; finitely many are
>    nonzero, with the closed support bound of §2.2;
> 4. the tower `(m_F; h_j,k_j,l_j,s_j)` by repaired Proposition 4.2 with
>    `h_0 = g`, first step `(k_0,l_0) = (2,3)` and `s_0 = c_g^2` (order-0
>    factorization + type pin), shared along the branch by Proposition 4.4;
> 5. the residues `e_k ≡ 22k (mod 25)`, floors (V), extraction law (C), and
>    leading value `v_{B,0} = (25 u^2 c^{24})^i` (all already promoted);
> 6. the deviation ledger `(C_k, rho_k)` and landing datum
>    `T = gamma q p^{-i}` of Theorem C, with
>    `gamma = kappa_F/(25 i lambda_f A B)`.
>
> Moreover B-route packet construction shares nothing with the sibling
> route (R1 erratum): every field above is a functional of this route's
> witness only.

**Proof.** 1 is a tautology of the conditional quantifier. 2 is interface
Theorem 2.1 (proved EXACT there: `(K,P,Q,c,m,n,a)` determines `DPT_a(f,g)`
up to deck-equivariant decorated isomorphism, including at every vertex the
data (2.11)–(2.12): `u, kappa_F, nu_F, D_{f,F}, D_{g,F}, p_{f,F}, p_{g,F}`,
tower, deck action) together with Proposition 3.1 for the flag segment;
T4 supplies the normalized representative and preserves `td`. 3 is
Statement 3.7(5) applied to the constructed chart: `h^F(x,eta)` is a finite
sum of graded pieces, and substitution `h(x, phi(x) + eta x^{-u})` exhibits
each piece as a polynomial in the coefficients of `h` and the prefix
coefficients of `phi`. 4: order-0 of `(E_s)` forces `G_0 = c_g p^r` with
`r = i D_g/D_F` (bchild §3.1, disposition-confirmed); the type pin gives
`r = 3i/2`, hence `l_0/k_0 = r/i = 3/2` in lowest terms, `(k_0,l_0)=(2,3)`,
`s_0 = c_g^{k_0} = c_g^2` (Prop 4.2(iii)); Prop 4.4 shares the step along
the branch. 5 is the promoted bchild/discriminator layer, consumed. 6 is
Theorem C below. Route separation: every constructor input is the B
witness. QED.

The force of Theorem A against the audit's absent-fields table: every row
the audit classifies `GENUINELY ABSENT` is absent **as a serialized
instance**, and is nevertheless a **well-defined functional** of the
hypothetical pair — including the two rows the audit flags beyond data:
the "gauge/free-side choice" (resolved canonically by Theorem C: the free
side is fixed by maximal fractional-power subtraction, i.e. the binomial
response is the canonical g-side normalization, and the residual freedom is
exactly the ledger constants), and the g-side initialization (pinned to
`(2,3,c_g^2)` conditionally on the route, per the disposition's repair 2).
So the correct campaign statement is not `PairRef absent ⇒ no bridge`; it
is: the bridge is a proven functor, and only instances, caps, and
occurrence are missing.

### 2.2 Finite support, exactly

For any polynomial `h` with `deg_x h = d_x`, `deg_y h = d_y`, the chart
substitution `y = phi(x) + eta x^{-u}` (finite prefix, exponents `> -u`)
puts the x-support of `h^F` inside `[-u d_y, d_x]`. Hence on the
`kappa_F`-lattice the nonzero pieces of `f^F` have index `k` from the top
bounded by

```text
K_f = kappa_F (d_F + u * deg_y f) = D_F + (kappa_F - kbar_F) * deg_y f
    = 25 i + (kappa_F - 17) * deg_y f,
```

and symmetrically `K_g = D_g + (kappa_F - 17) * deg_y g`. The packet is
finite for every actual pair; its size is controlled by the global degree
data and the unpinned `kappa_F` — this is where the missing cap (§8,
CAP-B25) enters and is the exact reason no uniform finite packet exists on
the frozen basis.

## 3. Q2 — the universal coefficient scheme (Theorem B) and the cap blocker

The packet explicitly invites "coefficient variables modulo the exact
Keller/support ideal, together with a proven completion map and route
incidence ideal," while forbidding formal independent jets. That object
exists at the following exact scope.

> **Theorem B (universal-parameter form; standard-machinery tier, proof
> outline below).** Fix a support-cap vector
> `Delta = (d_x^f, d_y^f, d_x^g, d_y^g)`. On the affine coefficient space
> `A_Delta` of pairs with those support bounds times the fibre line
> (coordinate `a`), the locus
>
> ```text
> Occ_Delta = { (f,g,a) : J(f,g) = 1, and DPT_a(f,g) has a y-side interior
>               vertex realizing the B state (25,17,25,3,2/3) }
> ```
>
> is a constructible set, and admits a finite constructible partition on
> each piece of which every Theorem-A field (in particular each `P_k`,
> `k <= K_f`, and each ledger entry of Theorem C) is given by an algebraic
> function of the coefficients (regular after a finite etale base change
> absorbing the Puiseux/Kummer root choices, quotiented by deck). Every
> hypothetical counterexample realizing the route lies in `Occ_Delta` for
> some `Delta`.

**Proof outline (not promoted beyond outline tier).** The Keller condition
is a finite set of polynomial equations on `A_Delta`. The Newton–Puiseux
algorithm of interface Theorem 2.1 run with coefficient parameters branches
at each step on vanishing/nonvanishing of finitely many polynomials in the
parameters (face selection, residual-root multiplicities, discriminants);
tree depth and the number of branches are bounded by intersection-number
bounds polynomial in `Delta`; therefore the algorithm terminates uniformly
on a finite constructible partition, on each piece of which all Puiseux
prefix coefficients are algebraic functions. State equality
`(nu,kbar,X,M,w) = (25,17,25,3,2/3)` and interiority are finite boolean
combinations of equalities/inequalities of those functions (Q/jump/max
labels included, since all presentations through the vertex are emitted by
the constructor). Chevalley preserves constructibility under the final
projection/quotient. The field formulas are those of Theorem A. QED
(routine but long; recorded as an outline, fail-closed: no promotion of
Theorem B is requested until a write-out is reviewed).

**What Theorem B does not give.** The union over `Delta` is strictly
increasing and no theorem on the frozen basis bounds `Delta` at fixed
`td = 12` plus B-occurrence (`ladder/REDUCTION.md` T10: no upper bound on
degree-type complexity is anywhere in the chain; the Bezout identity
`td = deg f deg g - sum i_p` allows unbounded degrees at fixed `td`).
So there is no finite-dimensional universal packet and no licensed finite
elimination/enumeration. That is blocker CAP-B25 (§8), the first missing
source lemma of the emission problem — not `PairRef` absence.

## 4. Q3 — the deviation ledger and the forced landing at `s*` (Theorem C)

Throughout: the fixed occurrence of Theorem A; `' = d/d eta`;
`D_F = 25 i`, `D_g = 25 r`, `r = 3i/2`, `i` even; `kbar_F = 17`;
`s* = D_F + D_g - kbar_F = 25(i+r) - 17`; `(E_s)` as promoted, RHS
`kappa_F * 1_(s = s*)`. Route patterns `p = (t-A)^2(t-B)`,
`q = eta (t-A)(t-B)`, `B/A = 9/8`, `A = 8u`, `B = 9u`, `u != 0`,
`P_0 = lambda_f p^i`, `G_0 = c_g p^r`.

### 4.1 The fractional-power algebra

Work in the x-graded completion of the chart ring at `F` (formal sums of
graded pieces with x-orders descending to `-infinity`; each piece a finite
object of the on-lattice weight class; `J_{x,eta}` extends continuously).
For `rho in (1/i) Z` define `(f^F)^rho := lambda_f^rho x^{rho d_F} p^{i rho}
(1+V)^rho` with `V := sum_{k>=1} (P_k/P_0) x^{-k/kappa_F}` and the formal
binomial series; this is well defined whenever `i rho in Z` (then
`p^{i rho}` is an honest rational function). Let

```text
Phi_F := { finite sums  sum_k C_k (f^F)^{rho_k} :  C_k in C,
           rho_k in (1/i)Z,  i rho_k in Z,  rho_k distinct }.
```

Every element of the closure of `Phi_F` is annihilated by `J(f^F, . )`
(chain rule for formal powers in a Q-algebra: `J(f^F,(f^F)^rho) =
rho (f^F)^{rho-1} J(f^F,f^F) = 0`; continuity extends this to graded
limits). All graded pieces of all elements of `Phi_F` lie in
`C[eta][1/p]` (integer powers of `p` only) and are on-lattice with weight
`≡ 22 * (drop-from-top) (mod 25)` — the same Theorem D law as for `f^F`,
`g^F`, because pieces are sums of products of `P_a/P_0`'s times `p`-powers,
`p` has weight `0`, and drops add.

### 4.2 Theorem C1 (ledger rigidity)

> **Theorem C1.** There are finitely many constants `C_1, ..., C_m in C^*`
> and exponents `3/2 = rho_1 > rho_2 > ... > rho_m` with `i rho_k in Z`,
> such that, setting `Dev^{(0)} := g^F - c_g (f^F)^{3/2}` (top root of
> `p^{i}` chosen so the leading piece cancels; `c_g` from `G_0`) and
> `Dev^{(k)} := Dev^{(k-1)} - C_{k+1}(f^F)^{rho_{k+1}}` greedily whenever
> the top row stays homogeneous, the successive deviation orders
> `delta_1 < delta_2 < ... < delta_m` (drop of `ord_top Dev^{(k)}` from
> `D_g`) satisfy:
>
> 1. `delta_k ≡ 0 (mod 25)` for every `delta_k < s*`;
> 2. each absorbed top piece is a pure power: `C_k p^{r - delta_k/25}`;
> 3. `m <= i + r - 1 = 5i/2 - 1`;
> 4. the process never exhausts `g^F` (no `Dev^{(k)} = 0`).

**Proof.** Let `Dev` be any of the `Dev^{(k)}` with top drop
`delta < s*` and top piece `T_delta != 0`. All rows of
`J(f^F, Dev) = x^{-u}` above the landing vanish, and the topmost row
involves only `P_0` and `T_delta`:
`D_F P_0 T_delta' - (D_g - delta) P_0' T_delta = 0`, i.e. `T_delta` solves
a first-order linear ODE over `C(eta)` whose solution line is
`C * p^{(D_g - delta)/25} = C * p^{r - delta/25}` (solutions of `LT=0`
form a one-dimensional space over the constants: two nonzero solutions
have constant ratio). Rationality: `p = P_1^2 P_2` with
`P_1 = t - A, P_2 = t - B` squarefree and coprime as eta-polynomials
(`A != B`, both nonzero — route data), so `p^c = P_1^{2c} P_2^c in C(eta)`
iff `c in Z`, i.e. iff `25 | delta` (since `25 | 25r`). But `T_delta` lies
in `C[eta][1/p] ⊂ C(eta)` (pieces of `g^F` are polynomials; pieces of
`Phi_F` elements are in `C[eta][1/p]`). Hence `25 | delta` and item 2
holds; the weight law gives an independent second proof: the required
weight `≡ 22 delta` of `T_delta` matches the weight `0` of a `p`-power iff
`25 | delta` (`22` is invertible mod `25`). The greedy subtraction
`C (f^F)^{(25r - delta)/(25i)}` has matching top order and piece, and
`i * (25r-delta)/(25i) = r - delta/25 in Z`, so it stays in `Phi_F`;
the drop strictly increases. Item 3: the `delta_k` are distinct multiples
of `25` in `(0, s*)`, and `floor((s*-1)/25) = i + r - 1`. Item 4: if some
`Dev^{(k)} = 0`, then `g^F in Phi_F`, so `J(f^F, g^F) = 0 != x^{-u}` —
contradiction. Termination (no infinite ledger): if the subtraction never
reached the landing, the partial sums would converge in the graded topology
to an element of the closure of `Phi_F` equal to `g^F`, again contradicting
`J(f^F,g^F) = x^{-u}` (concretely: `J(f^F, g^F - S_m) = x^{-u}` for every
partial sum while `ord_top(g^F - S_m) -> -infinity`, so eventually every
row of the left side at the landing order is empty). QED

Dictionary to the printed tower: `Dev^{(0)} = h_1^F / (g^F + c_g(f^F)^{3/2})`
with `h_1 = g^2 - c_g^2 f^3 = g^2 - s_0 f^3` the first Proposition 4.2
resolvent, so `delta_1 = 2 D_g - D_{h_1,F}` and item 1 at `k=1` is exactly
the divisibility `nu_F | D_{h_1,F}` of Prop 4.2(iii). Theorem C1 is the
chart-completion sharpening of that mechanism, not a rival to it.

### 4.3 Theorem C2 (forced landing at exactly `s*`)

> **Theorem C2.** Let `Dev^red := g^F - sum_{k=1}^m C_k (f^F)^{rho_k}` be
> the terminal reduced deviation of Theorem C1. Then its top drop is
> **exactly** `s*`: `ord_top(Dev^red) = D_g - s* = kbar_F - D_F`, and its
> top piece `T != 0` satisfies the landing row
>
> ```text
> D_F P_0 T' - (kbar_F - D_F) P_0' T = kappa_F .      (LANDING)
> ```
>
> Moreover `s* ≡ 8 (mod 25)`; more generally, on this state the
> nonabsorbability of the landing is exactly N1: `gcd(kbar_F, nu_F) = 1`
> implies `s* ≡ -kbar_F not≡ 0 (mod nu_F)`, so the landing order can never
> satisfy the C1 rigidity condition and no `J=0` response — the binomial
> lift or any element of `Phi_F` — can absorb it.

**Proof.** By C1 the greedy process strictly deepens the top while the top
row is homogeneous; a top drop `delta < s*` with `25 ∤ delta` is
impossible, and one with `25 | delta` is absorbed. The top drop cannot
exceed `s*`: if `ord_top(Dev^red) < kbar_F - D_F`, then every product of a
piece of `f^F` (order `<= n_f`) with a piece of `Dev^red` has total order
`< Q kbar_F`, so `J(f^F, Dev^red)` — which equals `x^{-u}` exactly, since
`J(f^F, Phi_F) = 0` — has no term at the landing order: contradiction.
Hence the top drop is exactly `s*`, and the landing row of the graded
identity, which involves only `P_0` and `T`, reads (LANDING) in the
promoted `(E_s)` normalization with `D_g - s* = kbar_F - D_F`. `T != 0`
because it is a top piece; nonvanishing is also forced by (LANDING) itself
(`kappa_F != 0`). Arithmetic: `s* = 25(i+r) - 17 ≡ -17 ≡ 8 (mod 25)`; with
general state data `s* ≡ -kbar_F (mod nu_F)` and `gcd(kbar_F,nu_F)=1`,
`nu_F >= 2` give `s* not≡ 0`. QED

This is the packet's desideratum 3 in exact form: a nonzero compatibility
at `s*` that the `J=0` binomial response — indeed the whole fractional-power
closure — provably cannot absorb, with the route-datum N1 identified as the
precise nonabsorbability mechanism.

### 4.4 Theorem C3 (the landing row is exactly Proposition 8.1(iv); scale pin)

> **Theorem C3.** Substituting `P_0 = lambda_f p^i` and clearing
> `i lambda_f p^{i-1}`, (LANDING) is equivalent to
>
> ```text
> 25 p T' + (25 i - 17) p' T = (kappa_F / (i lambda_f)) p^{1-i} .    (*)
> ```
>
> (i) In the on-weight ring `C[eta][1/p]`, `(*)` is solvable **iff**
> `8B = 9A` — the promoted T1 ratio — and then the solution is **unique**:
>
> ```text
> T = gamma * q * p^{-i},
> gamma = kappa_F / (17 i lambda_f C_iv) = kappa_F / (25 i lambda_f A B)
>       = kappa_F / (1800 i lambda_f u^2)   at (A,B) = (8u, 9u).
> ```
>
> (ii) The mechanism of the coincidence is the state datum `X = nu_F`:
> the reduced landing operator is `nu_F p ( . )' - kbar_F p' ( . )` on the
> `q`-line, which is the 8.1(iv) operator `rho p q' - p' q` (times
> `kbar_F`) precisely because `rho = dp/dq = nu_F / kbar_F`, i.e.
> `X := kbar_F * dp/dq = nu_F` (here `75/51 = 25/17`, `X = 25`).
> (iii) The exact quadratic behind both: for every `(A,B)` of the shape,
>
> ```text
> 25 p q' - 17 p' q = 25 p * ( A B + (8B - 9A) t )        (identically),
> ```
>
> so the cell identity `= 25 A B p  [= 17 C_iv p]` holds iff `8B = 9A`,
> with constant term `A B` for every `(A,B)` — machine-corroborated (§4.6).

**Proof.** The reduction to `(*)` is the displayed division. Uniqueness:
two solutions differ by the kernel `C p^{(17-25i)/25}`, irrational since
`25 ∤ 17` (C1 rationality lemma), so at most one solution in `C(eta)`.
Existence and the ratio: seek `T = N p^{-i}`, `N in C[eta]`. Indicial
analysis of `(*)` at the eta-roots of `p` (leading coefficients
`25 sigma + 2(25i-17)` at A-orbit roots and `25 sigma + (25i-17)` at
B-orbit roots are never zero mod 25) forces `ord T = 1 - 2i` at each
A-root and `1 - i` at each B-root, so `N = T p^i` is a polynomial with
simple zeros exactly on the fifty roots of `W(eta^{25})`, and the weight
class `e_{s*} ≡ 22*8 ≡ 1 (mod 25)` gives `N = eta (t-A)(t-B) Ntilde(t)
= q * Ntilde(t)`. Substituting and using
`(q Ntilde p^{-i})' = (q' Ntilde + q Ntilde') p^{-i} - i q Ntilde p' p^{-i-1}`,
`(*)` becomes the t-level equation

```text
25 (A B + (8B - 9A) t) Ntilde + 625 t W Ntilde_t = kappa_F/(25 i lambda_f) * 25 ...
```

precisely: `(25 p q' - 17 p' q) Ntilde + 25 p q Ntilde' = (kappa_F/(i lambda_f)) p`,
and with (iii) and `q Ntilde' = 25 t W Ntilde_t * eta`-reduction:
`25 (A B + (8B-9A) t) Ntilde + 625 t W Ntilde_t = kappa_F/(i lambda_f)`.
If `deg_t Ntilde = d >= 1`, the term `625 t W Ntilde_t` contributes an
uncancelled top of degree `d + 2` (coefficient `625 d Ntilde_d != 0`), so
no solution; hence `Ntilde = Ntilde_0` constant, and the equation forces
`(8B - 9A) Ntilde_0 = 0` and `25 A B Ntilde_0 = kappa_F/(i lambda_f)`.
Since `Ntilde_0 = 0` is impossible (`kappa_F != 0`), solvability holds iff
`8B = 9A`, and then `Ntilde_0 = gamma` as displayed
(`17 C_iv = 17 * (25/17) A B = 25 A B`). Identity (iii): with `q = eta W`
one has `q' = W + 25 t W_t` and `p' q = 25 t p_t W`, so
`25 p q' - 17 p' q = 25 [ p W + 25 t p W_t - 17 t p_t W ]`; polynomial
division of the bracket by `p` is exact for every `(A,B)` of the shape and
the quotient is `A B + (8B - 9A) t` (top coefficient cancellation is the
`rho = dp/dq` top law; the closed forms were verified exactly, §4.6, and
match the trunk consumer's linear condition `(225/17)A - (200/17)B = 0`
up to the overall factor `-17/25`). (ii) is read off: the reduced landing
operator on the `N = q Ntilde` line is `25 p ( . )' - 17 p' ( . )` after
clearing, i.e. `nu_F, kbar_F` in the 8.1(iv) slots, because
`dp/dq = 75/51 = nu_F/kbar_F`, which is the state datum `X = 25 = nu_F`.
QED

**Reading.** The route's only genuinely inhomogeneous Keller equation, at
its leading order, is *exactly* the equation the campaign already solved as
T1 (`TRUNK_T1_SURVIVES`, unique `B/A = 9/8`, `C_iv != 0`). Two corollaries:

- **No kill at this tier.** Any lane hoping to kill the B route by
  evaluating "the distant inhomogeneous row" with route-local data will
  re-derive `B/A = 9/8` and stop. The row is satisfiable, uniquely, on the
  promoted cell.
- **New exact invariant.** The landing scale
  `gamma = kappa_F/(25 i lambda_f A B)` binds the chart denominator
  `kappa_F`, the full index `i`, the f-top scale `lambda_f`, and the
  T1-solved pattern scale `A B = 72 u^2` to the deviation-top scale of any
  realizing pair — a genuine invariant of the Theorem-A packet determined
  by the completion algebra plus the approximate-root data (packet
  desideratum 2). It consumes no value of any `P_k`, `k >= 1`.

### 4.5 Theorem C4 (below the landing: forward rigidity and residue rows)

Index the pieces of `Dev^red` from the landing: `T_0 := T`,
`T_j := ` piece at drop `s* + j`. Row `s* + j` (`j >= 1`) of
`J(f^F, Dev^red) = x^{-u}` reads

```text
sum_{a=0}^{j} [ (D_F - a) P_a T_{j-a}' - (kbar_F - D_F - j + a) P_a' T_{j-a} ] = 0,
```

whose fresh-term operator, after clearing `i lambda_f p^{i-1}`, is

```text
L_j[T_j] = 25 p T_j' + (25 i + j - 17) p' T_j .
```

> **Theorem C4.** (i) `L_j` has a nonzero kernel in `C(eta)` iff
> `j ≡ 17 (mod 25)`; at `j = 17 + 25 m` the kernel is `C p^{-(i+m)}` and
> `L_j = 25 p^{1-I} ∘ (d/d eta) ∘ p^{I}` with `I = i + m` (Leibniz).
> (ii) At every non-resonant `j`, `T_j` is uniquely determined by
> `(P_1..P_j, T_0..T_{j-1})`: the below-landing tail of the deviation is
> forward-rigid.
> (iii) At each resonant `j = 17 + 25m`, solvability for `T_j` is
> equivalent to the vanishing of the residues of the rational 1-form
> `p^{I-1} * RHS_j / (25 i lambda_f) d eta` at the roots of `p`; the row's
> weight is `≡ -1 (mod 25)`, so the form is deck-invariant and the fifty
> point conditions collapse to exactly **two** orbit conditions (A-orbit,
> B-orbit); one new gauge constant (`C p^{-I}`) enters per resonant row.

**Proof.** (i) kernel exponent `(17 - 25 i - j)/25 in Z` iff
`j ≡ 17 (mod 25)` (C1 rationality lemma); the conjugation identity is
`25 p^{1-I}(p^I R)' = 25 p R' + 25 I p' R` with `25 I = 25 i + j - 17`.
(ii) unique solvability against an irrational kernel as in C3 (existence:
the rows are identities of the actual pair, so a solution exists — the
actual piece; uniqueness is the content). (iii) With
`RHS_j := - sum_{a=1}^{j} [(D_F - a) P_a T_{j-a}' - (kbar_F - D_F - j + a)
P_a' T_{j-a}]`, the row becomes `(p^I T_j)' = p^{I-1} RHS_j /(25 i lambda_f)`;
an element of `C[eta][1/p]` is a derivative within `C[eta][1/p]` iff all
its residues at the roots of `p` vanish (partial fractions: log terms are
exactly the residues; the polynomial part and higher-order poles integrate
termwise; the residue at infinity is then zero by the residue theorem).
Weight bookkeeping: each product `P_a T_{j-a}` term has weight
`≡ 22a + (1 + 22(j-a)) - 1 ≡ 22 j (mod 25)`; at `j ≡ 17`,
`22 * 17 ≡ -1`, and an `h` of weight `-1` makes `h d eta` invariant under
the deck `eta -> zeta eta`, so residues along a deck orbit are equal. QED

The count "two conditions per resonant row" echoes the promoted intrinsic
cokernel `q = 2` (two distinct t-roots) of the window operator — same
distinct-root mechanism, different operator and regime; the two results are
not identified, merely consistent.

### 4.6 Machine corroboration

Exact `Fraction` t-polynomial checks, stdlib only, scratch
`/tmp/b25bridge/landing_check.py`
(sha256 `ce4ed6252911b39d3bf61f1b7fbd5be4490c379c9c6d8e50fc3d294888c6123e`):

```text
cell A=8 B=9 and A=24 B=27:  25pq'-17p'q - 25AB*p == 0          (identity (iii) at the T1 ratio, two gauges)
six random (A,B):            p | (pW + 25tpW_t - 17tp_tW); quotient = AB + (8B-9A)t exactly
                             (c2 == 0 always; c1 == 8B-9A closed form; c1 = 0 iff B/A = 9/8; c0 == AB)
mutations kbar->16, nu->24, B->7, drop-25tpW_t: all detected (nonzero residuals)
landing conjugation at i=2:  25p(qp^-i)' + (25i-17)p'(qp^-i) == (25pq'-17p'q)p^-i   residual {}
L_17 Leibniz conjugation:    residual {} remainder {}
arithmetic: s* ≡ 8 (25); e_{s*} ≡ 1 (25); resonant rows j ≡ 17 (25)   all True
ALL_LANDING_CHECKS_PASS
```

Every checked statement is also proved in-text; the run is corroboration,
not proof-of-record.

## 5. First consequence attacked — RES-ROW(s*+17)

Theorem C's first genuinely unspent consequence is the first resonant row
`j = 17`, i.e. absolute order `s* + 17 = 25(i + r)`:

```text
(p^i T_17)' = p^{i-1} * RHS_17 / (25 i lambda_f),
RHS_17 = - sum_{a=1}^{17} [ (D_F - a) P_a T_{17-a}' - (kbar_F - D_F - 17 + a) P_a' T_{17-a} ],
```

with `T_0 = gamma q p^{-i}` pinned (C3) and `T_1..T_16` forward-rigid
functionals of `(P_1..P_16, T_0)` (C4(ii)). Solvability is exactly two
residue conditions (C4(iii)) — the first place where the **window pieces**
`P_1..P_17` (the first-child coefficient data of the depth-24 B gate) meet
landed inhomogeneous rigidity. Status of the attack:

- **Typed completely** here: the condition is a finite bilinear residue
  functional in `(P_1..P_17)` and the rigid tail; the two functionals are
  computable from `p` alone once the `T_j` recursions are expanded.
- **Not evaluable on the frozen basis**: by the promoted bchild
  underdetermination (level-1 two-choice exhibits and own-order
  absorption), the window pieces carry genuine freedom on the (V)/(W)
  class; and the `T_j` recursion also consumes `(kappa_F, lambda_f, c_g,
  C_k)` — Theorem-A functionals with no serialized instance. Blockers:
  CAP-B25 and OCCURRENCE-B25 (§8), exactly as the packet anticipates.
- **Correctly scoped**: because the window rows `s <= 24` are all
  homogeneous and `J=0`-solvable (promoted envelope), while `s* + 17` is
  pinned inhomogeneously, RES-ROW is the *earliest* row where a
  contradiction against the reduced route data could in principle be
  manufactured by a value-bearing packet — the typed candidate kill lane
  replacing the structurally dead window-cascade lane.

## 6. Attacks and countermodels considered

- **Kill via the landing row with route data only: fails, provably.** C3
  shows the row is uniquely solvable on the promoted cell; the only way it
  kills is if `B/A != 9/8`, which T1 already excludes. (Conversely this
  gives an independent rederivation of the T1 ratio from the global
  Jacobian, with two extra outputs: uniqueness of the landing top and the
  scale `gamma`.)
- **Kill via ledger parity/counting: fails at this tier.** The ledger
  orders are only constrained to `25 Z ∩ (0, s*)` with multiplicity-free
  occupancy; both occupied and unoccupied patterns are consistent with all
  frozen data (the formal envelope realizes maximal transparency; the
  level-1 exhibits realize freedom). No contradiction is available without
  values.
- **Global residue reciprocity (`sum_S Res_S = 0` over boundary places):
  not consumed.** The action-form version is promoted `COSTUME`
  (Avenue 33); the honest versions (`Res_S(g^k dx)` etc.) couple all
  boundary places of the fibre, i.e. re-import the unpinned contact ledger
  and caps — strictly weaker per new information than the local landing
  analysis above, and not route-local. Recorded as considered and set
  aside, not as a result.
- **Support duality / Newton-polygon duality on the pair:** subsumed at
  this vertex by the finite-support bound §2.2; the polygon data enter
  only through `K_f, K_g` and the type pin already consumed. Nothing
  sharper was found that does not need CAP-B25 first.
- **Minimal-degree normalization as a value source: nothing found.**
  T2/T4 minimality is consumed in fixing the type and excluding elementary
  reductions; neither the GGV `B_GGV` minimum nor lexicographic
  `(deg f, deg g)` minimality descends to a constraint on any window value
  at this vertex on the frozen basis. Stated as a nonclaim, not a proof of
  impossibility.

## 7. Novelty and history ledger

Searched: `xmodel/` and ladder files for fractional-power/deviation/landing
mechanisms and for any development of the `s*` row. Findings: the formal
cascade lane (producer, Opus review, coordinator integration) proves the
window-side `J=0` transparency and *names* the `s*` row as the correct
future target ("A future purely formal successor, if any, must target the
inhomogeneous row `s*`"), but develops nothing below the window; the bchild
primary's Theorem B is own-order absorption *in the window*; no file
constructs the fractional-power closure, the ledger rigidity, the forced
landing, the `X = nu_F` identification with 8.1(iv), the scale `gamma`, the
below-landing forward rigidity, or the resonant residue rows. Honest
classification of the underlying mechanism: Theorems C1–C2 are the
chart-completion sharpening of Sigray's Proposition 4.2 tower mechanism
(dictionary in §4.2) — equivalent in spirit, new in form and in the exact
`mod nu_F` / N1 statements; Theorem C3's equivalence and scale pin and
Theorem C4's resonance/residue structure are new statements about this
route; identity (iii) of C3 is a new exact closed form consistent with (and
refining) the trunk consumer's coefficient solve. The universal-parameter
Theorem B is the construction the wave packet itself sanctions, executed at
outline tier. No numbered avenue is reopened; nothing here overlaps the
finite-pole scope task or TWIN-ORDER.

## 8. Exact blockers — the first missing source lemmas

1. **CAP-B25 (first missing lemma for a finite packet).** Statement
   needed: *there is `N` such that every Sigray-normalized type-`(2,3)`
   `td=12` counterexample realizing the B state has
   `deg_y f <= N` (equivalently `K_f, K_g, kappa_F` bounded).* On the
   frozen basis nothing bounds `deg` or `kappa_F` at fixed `td` plus
   occurrence (`ladder/REDUCTION.md` T10; Bezout ceiling note). Without it
   Theorem B's union over caps is not finite-dimensional and no finite
   elimination, enumeration, or emitter is licensed. This — not
   `PAIRREF_ABSENT` — is the exact frontier of the emission problem.
2. **SUBTOP-TRANSPORT-B25.** Printed Statement 3.9 transports pattern
   *leads* only; nothing printed pins sub-leading pattern coefficients
   across the trunk edge (trunk consumer §4, "explicitly not printed").
   Consequence: the landing data `(T, gamma)` at `F` cannot yet be
   transported to the merge vertex to test cross-vertex consistency of the
   `gamma`-scales along the branch. A proved sub-leading transport law (or
   a proof that none is needed) is the second missing lemma.
3. **OCCURRENCE-B25.** No theorem forces any minimal counterexample into
   the B state; the route is one open case of the td=12 off-axis panel
   (`BOOK-OFFAXIS.md` §4 open; REDUCTION T9(c) no completeness
   certificate). All theorems here are conditional on the occurrence
   witness, as tasked; none manufactures it.

Strongest theorems immediately below the missing lemmas: Theorems A, B
(outline tier), C — none of which needs any of 1–3.

## 9. Nonclaims

Not claimed: any value of `v_{B,k}` or `P_k` (`k >= 1`); any occurrence,
realizability, gluing, or landing/coverage result; any gate verdict or
level advance; any new exit price (`charge_basis` absent by design); any
`td` bound, panel closure, `G2-PSC`/`G2-BD` progress, degree cap, kill of
the B route, counterexample, or JC2 consequence. Theorem B is outline-tier
and not proposed for promotion without a written-out review. The sibling
route is untouched; no object here may be reused for it. The `i = 6n`
rider is not consumed. `jc2-lean` untouched; no AWS or heavy CAS; no
canonical file edited; exactly one repository file written (this report);
scratch confined to `/tmp/b25bridge/`.

## 10. Smallest nonduplicate descendant

**`TD12-B25-RESROW/v1`** (desk, finite, source-bearing, reviewable; no AWS):
expand Theorem C4's recursion symbolically through `j = 17` on the reduced
cell; emit (a) the two residue functionals of RES-ROW(s*+17) as explicit
finite bilinear forms in `(P_1..P_17)` and the rigid tail, with all
`(kappa_F, lambda_f, c_g, gamma, C_k)` dependence typed; (b) a
vacuity/nonvacuity verdict on the (V)/(W)-admissible class (does some
admissible window choice violate the residue conditions, or are they
identities on the class?); (c) fail-closed states
`RESROW_VACUOUS_ON_CLASS`, `RESROW_NONVACUOUS` (typed kill lane input),
`EXPANSION_BLOCKED(missing datum)`. Inputs: frozen basis only. Stop rule:
symbolic expansion only; no caps, no invented jets, no value emission.
Nonduplicate: no existing lane develops any row below the window
(§7 search); the window-cascade lane is stopped by the coordinator and is
not reopened by this (different rows, inhomogeneous side).

Secondary (not claimed as smallest): a SUBTOP-TRANSPORT-B25 source hunt in
printed §§3, 6 for any sub-leading transport germ, strictly scoped to the
trunk edge.

## Seal

Git basis `92ebe92ad5986a47f01af9ed901260595dfed869`, HEAD re-verified
unchanged immediately before sealing. Body = all bytes of this file before
the literal `## Seal` heading.

report_body_bytes = 39510
report_body_sha256 = 539ecec1d4255067a7819bb7577e69809a1b4f0800ab8e8313d1ad026fa58278
