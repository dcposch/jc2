**HOSTILE GATE — exact contact, integrality, and sibling closure — Astra — 2026-09-06**

The residual **59 is not promotable**. All six proposed new removals have surviving
necessary numerical trees under the printed fixed-characteristic closure. R028 even
supplies a completion within the producer's stated depth bound satisfying both stated
lemmas. **R009 and R050 are promotably pinned to a unique necessary contact/multiplicity
pattern with `I_M = I_m = 8`**, after replacing the producer's bounded-search argument by
Moh Proposition 5.3. This does not pin coefficients or exhibit a polynomial pair.

| Gate item | Verdict | Content that survives the gate |
|---|---|---|
| (a), integer test and normalization | **CONFIRMED-WITH-FIX** | The complete final-major sum is the resultant degree, an integer. A prematurely terminated sibling sum is not that quantity. |
| (b), Lemma A | **REFUTED** | A reduced pattern need not have coprime multiplicities; an explicit local ODE counterexample is below. |
| (b), Lemma B | **CONFIRMED-WITH-FIX** | Every ancestor divisor divides every deeper characteristic exponent in the same global list. This does not license arbitrary inserted exponents. |
| (c), R009/R050 | **CONFIRMED-WITH-FIX** | Both necessary contact patterns are unique and Xu-tight; the finite proof uses neither A nor an artificial depth cap. |
| (d), six new removals | **REFUTED** | All six retain numerical completions. R028 refutes even the stated conditional search claim. |
| (e), R001 requires B | **REFUTED** | R001 is excluded by the printed fixed-list continuation and Xu, without either new lemma. |
| (f), ell sensitivity implies non-invariance | **CONFIRMED-WITH-FIX** | The local ell shift is correct. The asserted inference to non-invariance is unsupported; the descent comparison remains **OPEN**. |
| (4), 924/1,080 count | **CONFIRMED-WITH-FIX** | All raw counts reproduce. Of the 924 flat exclusions, 19 prematurely terminate upper-level siblings. |

**Custody and scope.** Before reading mathematical content, I used `awk` to join the
receipt `xmodel/exact-contact-gate-astra-20260906.run.v2`'s numbered SHA-256 and basename
fields, wrote `box/exact-contact-gate-20260906/input-manifest.sha256`, and ran
`sha256sum -c`: **7/7 OK**. All mathematical inputs were the seven frozen copies in
`/tmp/jc2-lane.QKyQBy/inputs`. No producer code or uncharged artifact tree was read; no
`ideation-*` input, ledger edit, or `jc2-lean` use occurred. Independent census, lemma,
and closure workers supplemented the root's normalization and control calculations.

References below use **X** for the frozen Xu PDF and **M** for the frozen Moh PDF.
Printed page numbers are authoritative. Reproducible layout extracts are
`box/exact-contact-gate-20260906/xu.txt` and `moh.txt`; `X:43` means extract line 43,
not a line from a previous validator. Missing Moh OCR equations were visually checked
against the PDF pages, including pp.150, 171, 179–180 and 200.

**1. The integer is literal, and the orientation is correct.**

Xu §2, PDF p.1, says exactly, `I(f,g) = deg_x Res_y(f,g)` and immediately sets
`x=t^{-1}` ([X:42–44](/home/ubuntu/jc2/box/exact-contact-gate-20260906/xu.txt:42)).
The hypotheses there are polynomials in `K[x,y]`, monic in `y`; §2 then defines
`f_xi=f-xi` for generic `xi` (X:64–73). Thus the nonzero resultant is a polynomial
in `x` over the coefficient field with the generic parameter, and its degree is an
ordinary nonnegative integer. No cover degree divides this definition.

Use Xu's orientation throughout: `deg_y f=m` is the smaller degree, `deg_y g=n`
the larger. In the campaign's opposite naming, these are the smaller and larger
roster members, respectively. At a final major disc let `rho_f` count its actual
Puiseux roots of `f_xi`, and let `lambda_g` be the `t`-order of `g` there. Then

```
Res_y(f_xi,g) = product_{f_xi(alpha)=0} g(alpha),
I(f_xi,g) = -ord_t Res_y(f_xi,g)
          = -sum_{sigma in P_M} rho_f(sigma) lambda_g(sigma)
          = n/(m+n) sum_{sigma in P_M} rho_f(sigma)(1-delta_sigma).
```

The last equality is **X Theorem 5.1, p.7**, with the definition immediately above
it (X:342–377). Minor roots contribute zero by Definition 4.3 (X:217–220). Lemma
4.4's proof gives `delta=1+lambda_f+lambda_g` at a final major root
(X:231–236), and Lemma 2.1 gives the ratio `lambda_f:lambda_g=m:n`.
The report uses exactly this normalization when its leaves really are final.

There is no hidden `m/n`, `1/L`, or extra Galois division. Switching which polynomial
is counted on a common major disc gives `rho_g=(n/m)rho_f`; hence
`n rho_f/(m+n)=m rho_g/(m+n)`, checking the swap directly.
All conjugate discs must be included once. A **per-disc** contribution need not be
integral: on R009 it is `1/2`, and sixteen conjugates sum to `8`. Applying the integer
test to that half would be an error.

For an unsplit packet born at `(rho,delta_0,lambda_f=-a)`, where `a>0`, root-product
valuation gives `lambda_f(delta)=-a+rho(delta-delta_0)`. Set
`kappa=rho(1-delta_0)-a`. Solving the final-major equality gives

```
delta_final = 1-(n+m)kappa/((n+m)rho-m),
J_final     = n rho kappa/((n+m)rho-m).
```

These formulas are correct **if the packet has no intervening split**. If it splits,
they compute the hypothetical immediate-final contribution, not the sum of its
eventual final-major leaves. This distinction, rather than a wrong resultant
normalization, is the central failure in the claimed census pruning.

**2. Four printed controls, rederived independently.**

At a level-2 factor of reduced multiplicity `r`, use
`rho=mr/d_2`, `a=m(1-delta_2)/(n-M_2)`, and the preceding formulas. An unsplit minor
factor instead ends at `delta_0+a/rho`. The following entries include the global
constant `1` on the minor side and count every conjugate disc:

| Xu case; reduced pattern | `a` at level 2 | Final-major discs: count × rho, delta | `I_M` | `I_m` |
|---|---:|---|---:|---:|
| §6.1(i), `(75,50)`, two A=5 orbits `(2,2)` | 2 | `10 × 4`, `2/3` | `10·4·(3/5)·(1/3)=8` | `1+(4-1)=4` |
| §6.1(ii), `(2,1,1)` | 2 | `5 × 4`, `2/3` | 4 | `1+3+10(6/5-1)=6` |
| §6.2(i), `(84,56)`, A=7 orbits `(2,1)` | 2 | `7 × 4`, `16/21` | `7·4·(3/5)·(5/21)=4` | `1+2+7(9/7-1)=5` |
| §6.2(ii), zero `1`, A=4 orbit `(5)` | `7/2` | `4 × 10`, `7/12` | `4·10·(3/5)·(5/12)=10` | `1+2+(2-1)=4` |

These are Xu's printed `8/4`, `4/6`, `4/5`, `10/4`, respectively; source
X pp.8–9, lines 402–452. The checks are independent `Fraction` calculations in
`controls.py`, with the individual radii, orders, root counts and swapped-orientation
equality retained in `controls.json`. Agreement confirms the formulas on their proper
domain; it does not make an unfinished tree final.

**3. Lemmas A and B, and the printed replacement for sibling closure.**

**A is false as a necessary pattern filter.** Moh Proposition 4.6(1) gives a common
polynomial `p` with prescribed degree. Its conclusions (3)–(5) say that `q` is
squarefree, every root of `p` is a root of `q`, and `p` is not a power **of q**
(M p.170, lines 1632–1644). They do not say that `p` is not a proper power.
The characteristic divisor is global data, not the maximal power of each local polynomial.

Xu's first control already contradicts A: `d_2=gcd(75,50)=25`, `m/d_2=2`, and
`p=((pi^5-c_1)(pi^5-c_2))^2`. All ten reduced multiplicities are `2`.
Taking the square root as the new reduced polynomial would require the noninteger
putative divisor `25/2`. The producer both accepts this printed control and imposes
the incompatible gcd-one filter on sibling continuations.

There is also an explicit polynomial counterexample to the claimed local inference.
Write `z` for the local pi variable and set

```
h=z^10-5z^5+5,  s=z^6-3z,  p=h^2,  q=h s.
deg p=20, deg q=16,
5h s'-3h' s=-75,
20p q'-16p' q=-300p.
```

Both `h` and `q` are squarefree, `gcd(h,s)=1`, all roots of `p` lie in `q`, and
every multiplicity of `p` is `2`. This is precisely the reduced differential equation
from Moh's Appendix A.3/A.4 route on p.171, with `P=20,Q=16` and nonzero constant.
It has the required two A=5 orbits, since the two values of `z^5` are
`(5±sqrt(5))/2`. Expansion and gcd checks are in `lemmas_audit.py`. This refutes A
in the printed necessary calculus; it does not assert a global Keller-pair witness.

**B has a valid, narrower statement.** Moh p.150 constructs the expansion with
`eta=g(x,y)^(-1/n)`, with **x fixed**, and writes `f` as a series in `eta` with
coefficients in `k[x]`. His definitions give

```
d_1=n,  d_i=gcd(n,M_1,...,M_{i-1}),
M_i=min{a: f_a(x) != 0 and d_i does not divide a}.
```

Consequently every nonzero eta-support exponent `a<M_i` is divisible by `d_i`;
in particular `d_i | M_j` for **every** `j<i`. In a major tower an ancestor has
the larger index, so this is the requested every-ancestor condition, equivalently
`n-M_j ≡ n (mod d_i)`. A newly hypothesized eta-support exponent below an ancestor
must obey it if that ancestor's divisor is to remain fixed. The expansion and its
meaning are on M p.150 (extract lines 533–572; formulas checked in the page image).

What does not follow is that an arbitrary effective parameter `M=n-W` assigned to
a physical t-disc is a new nonzero eta-support exponent. Congruence alone does not
connect the two series or permit modification of a frozen complete characteristic
prefix. Thus B is **CONFIRMED-WITH-FIX**.

The requested random check uses `random.Random(20260906).sample(rows,20)` on the
frozen census roster. The sampled rows are
`R001 R003 R004 R007 R008 R010 R013 R017 R020 R033 R038 R039 R040 R046 R048 R050 R058 R059 R060 R063`.
All **20/20** gcd chains and **88/88** ancestor/deeper pairs pass. Same-index negative
controls confirm `d_i` does **not** divide the characteristic `M_i` itself. The JSON
records every index and divisor. This corroborates the actual lattice statement;
it does not test a missing free-W-to-eta identification.

**The stronger replacement is printed.** Definition 5.1(4), p.179, applies the fixed
characteristic data to every tower. Proposition 5.3, p.180, takes **any** factor of
`p_r` with multiplicity `V_r>d_r/(n-M_r)` and forces its next major disc to be
`D_{r-1}`, using **the same `M_{r-1},d_{r-1}` list**, with the radius printed there.
It is not a choice of an arbitrary intermediate exponent. The proof rules out an
intervening value `M_r>L*>M_{r-1}` using Proposition 4.4, then proves the radius
equality (M pp.180–183; extract 2157–2317). The summary theorem p.200(4) repeats
the assertion for every above-threshold sibling (M:3231–3247).

At `D_1`, Proposition 4.6's nonzero constant differential determinant makes both
leading polynomials squarefree and disjoint: a common root or a repeated root
would annihilate both determinant terms. Thus `D_1` is final, with no further major
extension. A branch formed at level `r` has only the remaining fixed indices
`r-1,...,1`. For these six rows `s=4`; after the level-3 split there is at most
one further nonfinal major split at level 2, then the final level 1. For R009,
R050 and R001, `s=3`, so a major sibling born at level 2 goes directly to finality.

This supplies a printed finite bound in the **correct** model. The producer's
depth cap on arbitrary extra-W splitting excludes branches with more than two
recursive splits in that larger artificial search. No printed bound on that
artificial state space was supplied. Increasing its cap would not repair the false
primitivity filter or its incorrect empty-search result.

**4. R009, R050 and R001 after the correction.**

For R009, `P_2=48,Q_2=33,A_2=16,lo_2=16/11`; the two patterns compatible with
`V_2=2` are `(z=0;2,1)` and `(z=16;2)`. The first has:

| Packet | Number of discs | f roots per disc | Final delta | Xu contribution |
|---|---:|---:|---:|---:|
| Principal minor | 1 | 32 | 3 | minor `2` |
| Level-2 minor orbit | 16 | 2 | `21/16` | minor `5` in total |
| Selected final majors | 16 | 4 | `19/24` | major `8` in total |

Thus `I_M=8`, `I_m=1+2+5=8`. On the other pattern the zero sibling is
`(rho,kappa)=(32,20)`. Its **forced** final radius is `29/79` and the complete
major sum is `8+960/79=1592/79`, nonintegral. It also fails final Galois congruence:
the increment denominator is `79`, while `rho_f=32`. The actual preceding centre
stabilizer has `L=1` on this zero branch; the producer's coarser `L=16` happens to
give the same obstruction. Proposition 5.3 permits no intermediate major continuation.

For R050, `P_2=21,Q_2=9,A_2=4,lo_2=7/3`. The two patterns are
`(z=1;4,1)` and `(z=5;4)`. In the first, the principal minor has 14 roots at
delta `3`; the five level-2 minor discs each have 2 roots at delta `2`; and four
final-major discs have 8 roots at delta `19/28`. Hence
`I_M=8`, `I_m=1+2+5=8`. In the second, the zero sibling has
`(rho,kappa)=(10,4)`, forced final radius `13/22`, and total
`I_M=8+35/11=123/11`. Its actual increment denominator is **22**, from `L=1`;
the producer's coarser `L=4` gives **11**. Both exceed `rho_f=10` and fail finality.
There is no extra major continuation to search.

Independent derivative checks close the same accounting. Xu Theorem 3.4 gives
`I(f_xi,f_y)=128+62+4=194` on R009 and `56+28+2=86` on R050. Xu Theorem 4.7(i)
gives respectively `127+62+5=194` and `55+26+5=86`. Equation (4.3) then reconstructs
`I(f_xi,g)=8` in each case. These checks are retained in `controls.json`.

The margin-zero conclusion needs one final qualification. A minor packet cannot
be arbitrarily declared unsplit on all rows. For a packet whose nominal zero
radius is `delta*=delta_s+b/rho>1`, an earlier genuine split into `k>=2` packets
of sizes `rho_j` changes the sum of nominal minor costs by

```
Delta=(k-1)(delta_s-1)+b(sum_j 1/rho_j - 1/rho) > 0.
```

If `delta_s>=1`, positivity is immediate. Otherwise use
`b>rho(1-delta_s)` and `rho sum 1/rho_j>=k^2` to obtain strict positivity.
Iterating handles subsequent splits. Unary changes of centre preserve the valuation
intercept and slope. At zero order a repeated `f_xi` leading root would, by X Lemma
2.1(ii), also be a leading root of `g`, giving positive order of `g` on that branch,
contrary to X Corollary 4.5 for the original Moh minor packet. The endpoint is final.
Thus every earlier genuine minor split raises the minor side above `8` and is
excluded on these two rows. What is pinned is the necessary contact and multiplicity
pattern, up to the still-undetermined coefficients; existence remains **OPEN**.

R001 has the two analogous patterns. `(z=0;2,1)` gives Xu's `4<5` exclusion.
The zero-7 alternative has a forced final sibling with 14 f roots, radius `7/17`,
and complete `I_M=152/17`, also failing the final denominator-17 condition.
There are no further major levels. The claimed dependence on B was a feature of
the artificial search, not of the printed argument. R001 remains the pre-existing
Xu removal without A or B.

**5. Explicit completions of all six claimed dead rows.**

`closure_fixed.py` independently enumerates the remaining fixed levels, uses exact
rationals, checks integer `P,Q`, multiplicity thresholds, root counts, Galois orbits
and final residues, and distinguishes actual zero-centre stabilizers. It imposes
neither A nor an extra-W depth cap. The following small certificates suffice to
defeat all six exclusions; they are necessary numerical/face data, not polynomial
pairs. Distinct named nonzero orbit constants are understood.

For R025–R028, `(n,m)=(180,120)`, `M=(-120,132,150,178)`. At level 3 choose

```
delta_3=1/6,  p_3=pi^4(pi^6-c).
zero branch:       (rho,kappa,L)=(40,30,1),
six nonzero arms:  (rho,kappa,L)=(10,5,6).
```

Each small arm is forced to level 2 with `W=48`, `delta=1/3`, `P=5,Q=4,A=1`.
Choose reduced multiplicities `(2,3)`. The two final-major packets are
`(rho,kappa,delta,J)=(4,1,13/18,2/3)` and `(6,7/3,7/12,3/2)`.
Each small arm contributes `13/6`, so the six contribute **13**, with no minor cost.

The large zero branch is forced to level 2 at `delta=1/5`, `P=20,Q=16,A=5`.
Two useful choices give:

| Large-branch A=5 orbit multiplicities | Major total | Additional minor cost | Rows whose selected V path occurs |
|---|---:|---:|---|
| `(1,1,2)` | 4 | 2 | R025, R026, R027 when combined with the small arms |
| `(1,3)` | 9 | 1 | R028, also R025 and R027 |

The principal minor baseline is `1+(5-1)=5`. Consequently there are certificates
`(I_M,I_m)=(17,7)` for **R025, R026, R027**, and `(22,6)` for **R028**.
The selected contacts are exactly the roster's: small-arm multiplicity 2 gives
R025's `13/18`, small-arm multiplicity 3 gives R027's `7/12`, and the large-branch
multiplicities 2 and 3 give R026's `2/3` and R028's `1/2`.

R028 is a direct counterexample to the described *conditional* search result.
The reduced multiplicity sets at its splits are `{4,1}`, `{1,3}`, `{2,3}`,
all with gcd one, so it satisfies A as well. Its only nonfinal sibling split uses
`M_2=132`, divisible by both common-ancestor divisors `12` and `6`; final
`M_1=-120` obeys every remaining ancestor divisibility. Its small-sibling search state
uses `d=60`, giving `P=5,Q=4`, within the allowed divisor range. It has one nonfinal
split followed by finality, within depth two under either counting convention.
Therefore the producer's empty result is not explained by an unexplored deeper
branch. Its stated constraints admit this completion.

The **same R028 coarse configuration** has the producer's flat value
`I_M=111/4`, `I_m=6`. Correctly completing its six small siblings replaces that
noninteger by **22**. This is a concrete false exclusion among the claimed 924:
the problem is an unfinished sum being identified with a resultant degree.

For R057/R058, `(n,m)=(192,144)`, `M=(-144,156,174,190)`. Choose
`delta_3=1/7`, `p_3=pi^3(pi^7-c)`. Each of the seven small arms reaches level 2
at `delta=4/7`, with `P=4,Q=3,A=1`; use multiplicities `(1,3)`.
Together they contribute major `9` and minor `1`: the minor radii are `8/7`,
the final-major radii `3/4`. The zero sibling reaches level 2 at `delta=1/4`,
`P=12,Q=9,A=4`; take `p_2=(pi^4-a)^3`. Its four final majors have 9 f roots,
radius `9/16`, and total major contribution `9`. Adding the principal baseline
`5` gives **`(I_M,I_m)=(18,6)` on both R057 and R058**. R057 selects the small arm;
R058 selects the zero branch. The cube in this valid reduced face is another
instance rejected by false Lemma A.

These are not merely partitions checked by root counts. Local reduced auxiliary
equations `P p q'-Q p' q=Cp`, with squarefree `q` and `C!=0`, are certified for
the displayed internal faces in `closure-controls.json` and `closure_controls.py`.
For example the small `(2,3)` face at `P=5,Q=4` can use
`p=z^2(z-1)^3`, `q=z(z-1)(25z^2-35z+7)`, yielding `C=21`.
For the R057/R058 cube face, `p=(z^4-a)^3` and
`q=z(z^4-a)(z^4-5a/4)` give `P=12,Q=9,C=15a^2`.
The script also verifies all three required final polynomial degree types, including
their constant determinant, squarefreeness, coprimality and Galois supports. Independent
`closure_audit.py` passes **1,294** exact checks on the nine target trees.
Global coefficient compatibility remains unproved: the rows are typed **OPEN**.

**6. The 924/1,080 replay and its exact scope.**

The independent census engine enumerates at each selected level
`p_i=pi^z product(pi^{A_i}-c_j)^{r_j}`, with
`P_i=V_{i+1}d_i/d_{i+1}`, `Q_i=V_{i+1}(n-M_i)/d_{i+1}`, and
`A_i=den(L_i delta_i)`, using Moh's coarse
`L_i=lcm(den(delta_{i+1}),...,den(delta_s))`. It checks
`z+A_i sum r_j=P_i`, `[z>0]+A_i #j<=Q_i`, no multiplicity equal to `P_i/Q_i`,
and a selected multiplicity `V_i`. At `A_i=1`, translation-equivalent patterns
are represented with `z=0`; retaining redundant distinguished zero roots would
instead count 2,021 objects. Cartesian products of the normalized level choices
give precisely **1,080**. This convention reproduces the producer rather than
silently tightening its lattice. R063 and R066 alone contribute 509 and 230.

| Flat calculation | Reproduced count |
|---|---:|
| Total configurations | 1,080 |
| Nonintegral major sum | 995 |
| Major sum below unsplit minor sum | 77 |
| Both defects | 71 |
| Nonintegral, but passes the flat minor inequality | **924** |
| Integral, but fails the flat minor inequality | 6 |
| Passes flat minor inequality | **1,003** |
| Passes both flat comparisons | 79, across 59 rows |

Thus the raw count is exact; 924 is a subset of **1,003** inequality-passing flat
configurations, not of 1,080 configurations all retained by that inequality.
The roster contains 66 pre-Xu rows; the charged coverage report removes R001, giving 65.

Exactly **19** configurations have a different-multiplicity major sibling born
above level 2. All 19 occur among the 924. Their distribution is R022:1;
R025–R028:3,4,2,2; R047:4; R048:1; R057–R058:1,1. Their flat values require
the unsupported early finality. The other **905** integrality-only configurations
have no such unfinished major sibling, so their complete major arithmetic can
serve as an exclusion of those specified configurations. This counts configurations,
not realized pairs or conditions independent of the full Galois/ODE constraints.

The six target rows contribute **13**, not 14, coarse configurations in the very
enumeration reproducing all four headline totals. The `census_replay.json` file
contains every compact pattern and rational value, permitting direct verification
of all sums and overlaps. Its minor quantity is labeled `Im_unsplit`: at `u_s>1`,
in particular, the principal order `V_s/u_s` is not unconditionally attained.
Xu's discussion of `(99,66)` explicitly allows earlier principal-minor splitting
(X §8, pp.12–13, lines 640–678). No floor has been promoted to exactness there.

**7. The ell shift and the promotion decision.**

Xu Lemma 4.1 is valid for arbitrary polynomial `J`, and its right side is
`-J(t^{-1},alpha)t^{-2}` (X:193–202). For `J=c x^ell`, this becomes
`-c t^{-ell-2}`. At a final major disc with nonzero leading determinant this gives
`delta=lambda_f+lambda_g+1+ell`; the zero-order minor argument gives
`delta>1+ell`. Moh's p.171 Remark explicitly changes Proposition 4.6(3) to
`lambda=(-1-ell+delta)/(n-M_r)` (M:1711–1718; displayed formula visually checked).
The local ell sensitivity is therefore confirmed.

For a complete major/minor partition satisfying the corresponding shifted source
hypotheses, the norm argument has weighted major expression
`n/(n+m) sum rho_f(1+ell-delta)`. A realized polynomial resultant still has integer
degree. The shift by itself does **not** prove non-invariance under descent:
the transformation also changes radii, root counts, and the relevant branch sets.
The report itself finds `I'_M=I_M=8` on both targeted rows, which demonstrates why
changed formulas alone settle neither direction. A theorem comparing the parent
and child partitions, or a counterexample to that comparison, is missing.
The full child minor inequality is likewise not printed as Xu Theorem 4.7 under
nonconstant Jacobian. Keep that part **OPEN**, as the producer partly acknowledges.

Promote the resultant integrality statement for **complete** final-major sums,
the corrected fixed-list closure principle, and the two unique Xu-tight necessary
contact patterns. Do not promote Lemma A, the six exclusions, the 924 count as
exclusions of all completions, or the claimed proof of descent non-invariance.
The six proposed removals supply no reduction from the frozen residual **65**;
**59 is rejected by this gate**. No assertion of polynomial realization is made.

**Replay and FALLACY-v2.** From the repository root, run the following small scripts:

```
sha256sum -c box/exact-contact-gate-20260906/input-manifest.sha256
python3 box/exact-contact-gate-20260906/controls.py
python3 box/exact-contact-gate-20260906/lemmas_audit.py
python3 box/exact-contact-gate-20260906/census_replay.py
python3 box/exact-contact-gate-20260906/closure_fixed.py
python3 box/exact-contact-gate-20260906/closure_controls.py
python3 box/exact-contact-gate-20260906/closure_audit.py
```

`rho` counts roots, `A` describes conjugacy increments, a disc is a packet, and the
eta-characteristic list is global data; none is substituted for another. The report
separates completed major sums from hypothetical termination values and minor floors
from attained equality. All source maps and indices are declared. No new exit-price
assertion is made, so no `charge_basis` line applies. Notes and exact JSON certificates
are under `box/exact-contact-gate-20260906/`; the body is sealed below.

<!-- BODY-END -->
