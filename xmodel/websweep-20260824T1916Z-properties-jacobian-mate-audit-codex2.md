# Primary-source audit: Makar-Limanov--Trakhtenberg, *Properties of a Jacobian mate*

**Verdict: MIXED.**  The paper gives a useful new necessary-condition engine for one
Newton-resolved, shaped component of a hypothetical plane Keller counterexample.  Its
integrality, sub-expansion, polynomiality, and decreasing-denominator constraints are
actionable as a small independent checker.  They do **not** exclude `(72,108)`, TD6,
the residue-A two-pole template, or maximum partial `y`-degree 12.  The printed
`D <= 100` census is an implemented enumeration reported by the authors, but the
implementation is not supplied, the paper does not give a completeness proof at code
level, and several structural inputs are imported from `[ML2]`.  Nothing here proves
JC2.

This audit used the complete official 27-page MPIM submitted PDF, not the canceled
Claude log.  Scratch downloads and checks were confined to `/tmp/jc2-jmate-audit`.
Repository state was read at `a04affb7247fb5e87cad4e87f5926ab440254b24`; no existing
artifact was edited.

## 1. Sources, version, and reproducibility

Primary source consumed: L. Makar-Limanov and L. Trakhtenberg, [*Properties of a
Jacobian mate*, MPIM Preprint 2024 (33)](https://archive.mpim-bonn.mpg.de/id/eprint/5148/1/mpim-preprint_2024-33.pdf), submitted 2024-12-06.  The MPIM item page labels its sole
403 kB deposit “Submitted Version,” deposited and last modified 2024-12-16.  The PDF
is 27 physical pages (25 numbered article pages).

Primary publisher metadata for DOI
[10.1007/s40863-025-00520-4](https://doi.org/10.1007/s40863-025-00520-4) gives the
same title, authors, abstract, reference list, and 25-page article, *São Paulo Journal
of Mathematical Sciences* 20, article 16, online 2026-04-30 (cover date 2026-06-01).
The publisher full text was paywalled here.  Therefore: **no material version change
is visible in the accessible primary metadata, but textual identity has not been
established**.  In particular, the published metadata still describes `[ML2]` as an
MPIM preprint “to appear,” just as the submitted version does, which is evidence that
the bibliography was not substantially refreshed.

The title-page footnote says Trakhtenberg “implemented the algorithm described in the
paper.”  Searches of the MPIM item and author listings, the publisher article page,
and the authors' institutional publication records found no supplement, repository,
code archive, or executable attachment.  The MPIM record contains only the PDF.
Accordingly the census is **not publicly reproducible from an author-supplied
implementation found in this audit**.

Other primary technical sources actually implicated are Makar-Limanov,
[*A Jacobian mate defines the Jacobian pair*, MPIM 2022 (48)](https://archive.mpim-bonn.mpg.de/4771/1/mpim-preprint_2022-48.pdf) (`[ML2]`), Cassou-Noguès' 2011 Newton-tree paper, the
published GGV paper (J. Algebra 471 (2017), DOI
[10.1016/j.jalgebra.2016.08.039](https://doi.org/10.1016/j.jalgebra.2016.08.039)),
and Dixmier/ML1 for the homogeneous Jacobian equation and principal-edge form.

## 2. Exact scope and theorem inventory

The standing scope, sometimes left implicit after the introduction, is crucial:
work over `C`; assume a **nonautomorphic** Keller pair exists; after a polynomial
automorphism choose one component `f` with Newton polygon contained in the standard
trapezoid, leading vertex

\[
v_0=(m,n),\qquad n>m>0,
\]

and no edge parallel to the diagonal.  Choose the decreasing-power Newton solution
whose finite nonhorizontal chain has

\[
v_i=(\mu_i,\nu_i),\quad v_0=(m,n),\quad
v_{s+1}=(\mu_{s+1},1),
\]

with `mu_i < nu_i`, both coordinates strictly decreasing through `i=s`, positive
`x`-intercepts `rho_i`, and principal last edge of slope greater than one.  The
existence of a solution with precisely these properties is imported from `[ML2]`.
Cassou-Noguès (with ML1 as the stated route) supplies the no-diagonal-edge shaping
input.  GGV is only one citation among many for the older trapezoidal shaping; this
paper neither proves nor uses a GGV admissible-chain-to-book transport theorem.

The genuinely new restrictions in the paper are as follows.

1. **Newton-resolution data and first integrality condition (proved in-paper after
   imported setup).**  At stage `i`, substitute a finite fractional-power prefix
   `y_i=y+sum c_j x^(epsilon_j/delta_j)` and put
   `f_i=f(x,y_i) in C_i=C[x^(+-1/Delta_i),y]`, with `Delta_i` minimal.  Let `e'_i`
   be the pre-modification edge producing chain edge `e_i`; normalize its weight by
   `w_i(x)=1`.  Expanding the mate and stopping at the first term with bracket one
   gives `h_i=f_i(e'_i) g_{i,t_i}(e'_i)` with
   `J(f_i(e'_i),h_i)=f_i(e'_i)`.  If
   `dv(h_i)=c_i(\mu_i,\nu_i)` and `k_i=c_i nu_i`, then
   `k_i in Z`, and `c_i mu_i=k_i mu_i/nu_i in (1/Delta_i)Z`.

2. **Vertex reconstruction and remaining integrality/inequality conditions
   (proved algebraically in-paper).**

   \[
   \rho_i={\nu_i-\mu_i\over k_i-1},\qquad
   \alpha_i={k_i\mu_i-\nu_i\over\nu_i(k_i-1)},
   \]
   \[
   \mu'_{i+1}=\nu'_{i+1}-
   { (\nu_i-\mu_i)(k_i\nu'_{i+1}-\nu_i)\over\nu_i(k_i-1)},
   \]
   and the identical formula with unprimed `v_{i+1}`.  Required are
   `mu'_{i+1} in (1/Delta_i)Z`, `mu_{i+1} in (1/Delta_{i+1})Z`,
   `k_i>1`, `k_i mu_i-nu_i>0`, and `k_i nu_{i+1}-nu_i>0`.

3. **Divisibility lemma (claimed proof in-paper).**  From
   `J(f_i(e'_i),h_i)=f_i(e'_i)`, the paper concludes
   `w_i(f_i)` does not divide `w_i(h_i)`; in ordinate form `nu_i` does not divide
   `k_i`.  This drives `gcd(delta,l_0)<delta` initially and
   `gcd(l_i d_i,d_{i-1})<d_{i-1}` later.  The proof is terse: it subtracts a
   suitable power to lower the degree vertex and then asserts the remainder must be
   `c_0 x(y+c_1x^tau)`, contradicting noncollapse.  That classification step is not
   independently established in this paper and should be treated as a load-bearing
   lemma requiring source-level reproof, not as a machine gate already earned.

4. **Sub-expansion lemma and polynomiality (new claimed theorem).**  If
   `g_i=sum_{j<t_i} a_{i,j} f_i^(lambda_{i,j})+g_{i,t_i}`, the expansion at
   `e'_i` is a strict sub-expansion of that at `e'_{i-1}`:
   `t_{i-1}>t_i` and the earlier coefficients and exponents agree for `j<t_i`.
   Consequently, for `j>i`, the displayed paper condition is
   `f_i(e_i)^(k_j/nu_j) in B_{i+1}` (where `B_i=C[x^(1/Delta_i),y]`).
   The proof uses the auxiliary algebra `C[f_s,f_sg_s]`, a maximal power
   `f_s(e_i)=psi^d`, and an asserted homothetic propagation of Newton-edge chains.
   This is a theorem claim, not an enumeration heuristic, but the homothety and
   cancellation/completeness steps are sketched rather than isolated as lemmas.

5. **Denominator/divisor descent (conditional consequence of the sub-expansion and
   divisibility claims plus `[ML2]`).**  Write the initial form maximally as
   `f(e'_0)=phi_0^d0`, with `phi_0` not itself a power.  The edge exponents lie in
   `(1/d0)Z`.  `[ML2]` is cited for `lambda_0` being neither an integer nor the
   reciprocal of an integer.  If a nonprincipal next edge has maximal power `d'_i`,
   set `d_i=gcd(d_{i-1},d'_i)`; then `d_i` is a proper divisor of `d_{i-1}` and the
   new exponents lie in `(1/d_i)Z`.  If `d_{i-1}` is prime, the next edge must be
   principal.  This gives termination of the **nonprincipal denominator descent**,
   not by itself completeness of every Newton-chain enumeration.

6. **Leading total-degree complexity restriction (conditional theorem, with an
   important reading).**  Maximality gives `d0>1`; the divisibility lemma rules out
   a primitive degree vertex for `phi_0`.  Thus

   \[
   dv(\phi_0)=\delta(a_0,b_0),\quad \delta>1,\quad
   \gcd(a_0,b_0)=1,\quad b_0>a_0\ge1,
   \]
   \[
   D:=m+n=d_0\delta(a_0+b_0).
   \]

   “Product of at least three primes” unambiguously means **prime factors counted
   with multiplicity**, i.e. `Omega(D)>=3`: each of the three integers `d0`,
   `delta`, and `a0+b0` is at least two.  It cannot mean three distinct primes,
   because the paper itself retains `D=64=2^6`.  It applies to the leading total
   degree of this shaped `f`, not to topological degree, not to partial `y`-degree,
   and not simultaneously to both components of the map.

7. **Finite enumeration algorithm (implemented claim, not a proved software
   theorem).**  Starting from `D=d0 delta(a0+b0)`, it enumerates `l_i`, primitive
   edge directions `(beta_i,gamma_i)`, pre/post-modification vertices, denominator
   grids `Gamma_i`, proper divisors `d_i`, and principal-edge tests.  At the first
   edge,
   `1 <= l0 <= ((b0-a0)nu0+d0)/(d0 b0)`, with
   `epsilon0=gcd(l0a0-1,l0b0-1)`,
   `(beta0,gamma0)=((l0a0-1)/epsilon0,(l0b0-1)/epsilon0)`, and
   `v'_1=v0-t_1d0(beta0,gamma0)`.  The recursive formulas replace the `x` lattice
   by `1/Gamma_{i-1}`, impose
   `1 <= l_i <= [Gamma_{i-1}(nu_{i,1}-mu_{i,1})nu_i+d_i]/(d_i nu_{i,1})`,
   the gcd restriction above, and update `Gamma_i` by the printed lcm/denominator
   formula.  Principal candidates have ordinate zero or one and must cross `y=1`
   with abscissa in `(0,1)`; their admissible `l_i` is recovered from the displayed
   integer `z` formulas, with `lambda_0=l_i/d_{i-1}-1`.

The Newton-binomial “radical lemma” is elementary and correctly shows that if
`f_i(e'_i)^r in C_i`, then `f_i^r` belongs to the formal weight-completed algebra
`A_i`.  The assertions that the final bracket-one term satisfies
`h_i in B_i`, that `g` is recoverable from `f`, that the principal ratio is
`lambda_0=w_s(g_s)/w_s(f_s)`, and that a suitable resolved solution exists are
not new proofs here: they are assigned respectively to Dixmier/ML1 and `[ML2]`.

## 3. Independent identity and row checks

The vertex identities rederive directly.  Parallelism of
`v_i-(rho_i,0)` and `c_iv_i-(1,1)`, with `c_i=k_i/nu_i`, gives
`rho_i=(nu_i-mu_i)/(k_i-1)`.  Since the supporting line has
`w_i(x)=1`, its substitution exponent is
`alpha_i=(k_i mu_i-nu_i)/(nu_i(k_i-1))`.  Writing
`v'_{i+1}=(rho_i,0)+nu'_{i+1}(alpha_i,1)` and subtracting coordinates gives
the paper's reconstruction formula.  These calculations are independent of
the paper's prose and check exactly.

A scratch exact-rational program checked representative printed leading forms:

| printed case | top vertex of `phi_0` | after power `d0` | check |
|---|---:|---:|---|
| `D=42`, `d0=2`, `phi0=c x(xy^3-r1)^4(xy^3-r2)` | `(6,15)` | `(12,30)` | sum `42`, matching `2*3*(2,5)` |
| `D=48`, `d0=3`, `phi0=c x(xy^4-r1)^3` | `(4,12)` | `(12,36)` | sum `48`, matching `3*4*(1,3)` |
| `D=50`, `d0=2`, first row | `(5,20)` | `(10,40)` | sum `50`, matching `2*5*(1,4)` |
| `D=63`, `d0=3`, `phi0=c x(xy^3-r1)^5` | `(6,15)` | `(18,45)` | sum `63`, matching `3*3*(2,5)` |
| `D=64`, `d0=4`, `phi0=c x(xy^4-r1)^3` | `(4,12)` | `(16,48)` | sum `64`; explicit counterexample to “three distinct primes” |

The same scratch check factored all 19 reported values and confirmed
`Omega(D)>=3`.  These checks validate transcription and necessary arithmetic,
not the search's exhaustiveness.

## 4. Complete bounded output

The exact bound is the shaped component's **leading total degree `D<=100`**.  The
paper reports exactly these 19 surviving degree values:

```text
42, 48, 50, 56, 60, 63, 64, 66, 70, 72, 75, 80, 84,
88, 90, 96, 98, 99, 100.
```

The complete leading-vertex groups printed beneath those values are:

```text
42:  2*3*(2,5)
48:  3*4*(1,3); 6*2*(1,3)
50:  2*5*(1,4)
56:  2*7*(1,3)
60:  2*3*(3,7); 6*2*(1,4)
63:  3*3*(2,5)
64:  4*4*(1,3)
66:  2*3*(3,8)
70:  2*5*(2,5)
72:  2*4*(2,7); 6*2*(1,5); 6*3*(1,3); 9*2*(1,3)
75:  3*5*(1,4)
80:  2*4*(3,7); 5*4*(1,3); 8*2*(1,4); 10*2*(1,3)
84:  2*6*(2,5); 2*7*(1,5); 3*7*(1,3); 4*3*(2,5); 6*2*(1,6)
88:  2*11*(1,3)
90:  2*3*(4,11); 2*9*(1,4); 3*3*(3,7); 6*3*(1,4); 9*2*(1,4)
96:  3*8*(1,3); 6*2*(1,7); 6*2*(3,5); 6*4*(1,3)
     [two separately printed continuation blocks]; 8*2*(1,5);
     8*3*(1,3); 12*2*(1,3)
98:  2*7*(1,6); 2*7*(2,5)
99:  3*3*(3,8)
100: 2*5*(3,7); 2*10*(1,4); 4*5*(1,4); 10*2*(1,4)
```

This is the complete degree/leading-group output.  Pages 16--24 further split
these groups into all reported vertex-chain/form alternatives and mark three
families (`D=56`, `70`, `98`) and one `D=80` plus one `D=100` subgroup as
contradictory because `deg_x f(x,0)<2`.  The text nevertheless includes those
alternatives in the case display, so a faithful client must retain a status flag
rather than silently drop brace-marked rows.  There are visible typographical
hazards: at `D=64` one line misses punctuation before `phi0`; at `D=72` a repeated
factor is printed with the same `r1` although the global convention says distinct
indices; at `D=90`, `deg(g0)=5` almost certainly means `deg(q0)=5`; and at `D=64`
`phi1` is typeset in Latin letters once.  These prevent safe OCR-as-spec use.

## 5. Mapping to this campaign

There is no type-safe direct identification with the Sigray books.

| paper | meaning | campaign relation |
|---|---|---|
| `(mu_i,nu_i)` | rational Newton vertices along one decreasing Puiseux resolution of shaped `f` | closest to a GGV corner/edge chain, but not a Sigray pole entry |
| `d_i` | decreasing denominator/common-power divisor for mate expansions | not `td(F)` and not a book pole multiplicity without a new theorem |
| `Delta_i`, `Gamma_i` | fractional `x`-lattice denominators | not the book's `Lambda_i` |
| `D=m+n` | leading **total polynomial degree of `f`** in this frame | not Sigray topological degree `td=[C(x,y):C(f,g)]` |
| `nu_0=n` | leading `y` exponent of shaped `f` | not automatically actual/maximal partial `y`-degree after campaign normalizations |
| `lambda_0` | degree/weight ratio of `g` to `f` at the principal chain | not a book residue or root budget |

This agrees with `ladder/REDUCTION.md`: GGV minimal-pair selection is existential,
and no `G2-PSC` theorem transports a GGV/Newton packet into a decorated Sigray
pole tree.  The present paper starts from its own shaped component and never proves
that transport.  Its finite algorithm and `cases/book_enum.py` are therefore
**complementary necessary-condition compilers over different typed inputs**, not two
implementations of the same book.

Consequences for named live lanes:

* **`(72,108)`: not excluded.** `D=72` is explicitly retained, and the printed
  alternatives include principal ratios compatible with the familiar `3/2`
  degree ratio.  At most the paper supplies extra candidate-chain predicates for
  a separately verified matching Newton frame; it does not discharge the existing
  GGV-Horruitiner reduction/transcription bridge.
* **Residue-A two-pole and TD6: unchanged.** They are expressed in topological
  degree/pole-tree data.  No theorem here maps the one-component Newton chain or
  `d_i` descent to those two poles.  `D` may be arbitrarily larger than `td`.
* **Maximum partial `y`-degree 12: unchanged.** The claim `Omega(D)>=3` concerns
  total degree.  Even `nu_0` is frame-specific; it must not be substituted for the
  campaign's maximum actual partial `y`-degree.  No maximum-12 cell is killed.

## 6. Hostile audit: gaps and ambiguities

1. The abstract says restrictions on a “Jacobian mate,” but the complexity theorem
   is false for arbitrary coordinate polynomials (for example `f=x`).  It requires
   the nonautomorphic-counterexample and shaping assumptions from the introduction.
2. The chosen Newton solution/chain and mate recoverability are imported wholesale
   from `[ML2]`.  The present enumeration is conditional on those normal-form claims.
3. The assertion `h_i in B_i` is referred to Dixmier or ML1; the principal-edge
   supported form is explicitly left for “additional computations.”  Thus the
   printed rows are necessary skeletons, not constructed Keller pairs.
4. The divisibility lemma's terminal classification and the sub-expansion lemma's
   homothetic-chain argument are compressed enough that cancellation, maximal-power,
   and ring-membership hypotheses deserve a formal reproof.  They are not mere
   arithmetic identities.
5. The recursive description has variable-name reuse (`t1` at later stages), an
   ambiguous displayed denominator/lcm update, shifting `B_i/B_{i+1}` indices, and
   several result-table typos.  A direct transcription must fail closed on these.
6. Finiteness at fixed `D` is plausible from finite initial factorizations, bounded
   `l_i,t_i`, bounded fractional denominators, and strict divisor descent.  The paper
   does not state and prove a formal soundness/completeness/termination theorem for
   the actual implementation, nor publish source, hashes, test vectors, or row count.
7. “At least three primes” means multiplicity, as forced both by the proof and by
   retained `D=64`.  Reading it as three distinct primes is refuted internally.
8. The published-version text could not be diffed.  Matching primary metadata is
   insufficient to promote away possible proof or table changes.

## 7. Smallest useful software client (one day)

Build a new, read-only checker separate from `cases/book_enum.py`; do not merge the
types.

**Input (typed JSON):** `D_bound`; a row with `(D,d0,delta,a0,b0)`; exact rational
vertices `v_i_prime,v_i`; divisors `d_i`; denominator grids `Gamma_i`; integers
`l_i,k_i,t_i`; principal/nonprincipal flags; `lambda0`; and sparse factorizations of
each printed `phi_i`.  Every value must carry its paper-page provenance.

**Output:** per-row `PASS`, `REJECT`, or `UNVERIFIED`, plus machine-readable failures
for factorization, vertex reconstruction, grid integrality, inequalities, strict
divisor descent, gcd/divisibility, sub-expansion exponent containment, principal
edge test, `lambda0`, and sparse-form degree vertices.  Emit a canonical hash and a
degree-level inventory; never emit “complete” unless a separately specified search
generator and coverage certificate agree.

**Positive controls:** hand-enter the five checked rows above, including `D=64`;
include a multi-edge `D=48` row and a `D=96` continuation row.  **Negative controls:**
change one numerator, set `d_i=d_{i-1}`, make `nu_i|k_i`, relabel `D` as `td`, reuse
the `D=90 deg(g0)` typo literally, and interpret prime factors as distinct.  Each
must fail or become `UNVERIFIED`.

**Fail-closed gate:** (a) exact rationals only; (b) no OCR ingestion; (c) all printed
symbols resolved; (d) all invariants pass; (e) independently regenerate the 19-value
set for `D<=100`; (f) compare every manually transcribed alternative, including
brace-marked contradictions; (g) abort on a count mismatch or unknown notation.
Only after that gate should a separate adapter attempt a GGV-frame comparison; no
Sigray/book assertion may be produced without an explicit `G2-PSC` witness.

## 8. Promotion language and actions

**Promote:** “Conditional on the paper's shaped-counterexample setup and imported
`[ML2]` resolution/recoverability results, the displayed exact-rational identities,
integrality conditions, sub-expansion/polynomiality conditions, and strict divisor
descent are additional necessary conditions for the resolved Newton chain.  The
leading total degree of the shaped component satisfies `Omega(D)>=3`.”

**Quarantine:** “The `D<=100` table is an author-reported implemented enumeration,
not yet independently reproducible or code-complete.  It supplies no theorem about
topological degree or maximum partial `y`-degree, no GGV-to-Sigray transport, and no
exclusion of `(72,108)`, residue-A, TD6, maximum-12, or JC2.”

Ranked actions:

1. Implement the one-day exact row checker and transcribe the full pages 16--24
   inventory with provenance; require exact regeneration of the 19-degree set.
2. Reprove/formalize the divisibility and sub-expansion lemmas, explicitly expanding
   every `[ML2]` dependency and resolving the `Gamma_i`/index ambiguities.
3. Only if (1)--(2) pass, test the `D=72`, `lambda0=3/2` rows against the campaign's
   independently typed GGV `(72,108)` packets.  Treat any match as narrowing inside
   that Newton frame, never as a book or JC2 exclusion.
