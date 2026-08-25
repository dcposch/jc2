# Hostile different-model review — AS F-only D7 degree-ten pointwise gate

| Field | Value |
|---|---|
| Claim under review | Frozen producer: on the reviewed aligned deep `p=3,D=7` branch, retain the original nonreduced divided-carry predecessor. After exact linear elimination the next degree-ten mixed-carry equations are the affine system `A(base) xi + beta(base)=0` with `A` of size `8 x 9`. Field-valued rank zero is exactly the degree-five-zero vertical component; every nonzero degree-five point has rank three; ranks one, two, and four do not occur; the vertical component is compatible; on the nonzero rational-normal-cone component, compatibility has exactly two reduced endpoint branches. This is a scoped pointwise gate, not emptiness of `D=7` and not a lift or JC2 statement |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks below; remaining next-carry rows, other associated-top branches, full `D=7`, all-depth lifting, characteristic zero, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent integer Jacobian expansion over `Z` (320 `(U,V)` samples and 2304 `(U,V,C,D)` samples, zero remainder); independent sparse `F_3` coefficient emitter using integer-then-mod-3 derivatives, not the producer dictionaries; independent reconstruction of the 15-row high ideal `H`, the `8 x 9` matrix `A`, and the inhomogeneous column `beta`; reversible `7 x 7` accepted-divergence block; independent Singular Groebner bases, Fitting/minor ideals, saturations, radicals, and `minAssGTZ`; cone-chart substitutions; `F_3` pointwise rank census on both charts; reversed-column matrix check; integer controls rebuilt from `det J` over `Z`; unmodified rerun of the eight registered programs as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `a04affb7247fb5e87cad4e87f5926ab440254b24` (the charged basis) |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (unrelated max12 / websweep commit; charged basis remains an ancestor; producer bytes unchanged) |
| Review window (UTC) | 2026-08-24T19:25:39Z – 2026-08-24T19:37:05Z |
| Python | host CPython 3.14.6 (hashes, integer identities, sparse emitter, rank census, registered replays) |
| Singular | 4.4.1 |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-d7-degree10-pointwise-20260824.md` (SHA-256 `e4311a80aef2d3617c7b449e16cb19d34cfe25d31c558bb68f78ddc02fcae4ab`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/FREEZE.txt` (SHA-256 `c92a911df945c64f8d148819e22aa985a6393be3643cec8002474c89e272bab1`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/MANIFEST.sha256` (SHA-256 `426210cbdbd61e0ec0fa92d39344d3746c8a4a421df7c07c70f5a0cab968e2a5`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/README.md` (SHA-256 `2ed36cb4a940d3fca3b47ba584b605ea6a422112a7f139dbbcabd5525e1a4309`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/audit_pointwise_static.sing` (SHA-256 `f1461b2826019bc10069d0222957b47f3fc6d3847af871274349a793c21cc2e5`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/generate_reduced_pointwise.py` (SHA-256 `2f573c9d55ca73d5483a0d625c9285cfdfb6122b3b437d30d402974ac45249bf`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/generate_degree10_gate.py` (SHA-256 `fd76a59e75de80b871f773879c8911e5dec1905375912b2074793fcdc4ff3ef5`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/audit_source_compression.py` (SHA-256 `f72a7cec68d732dc99d867abc24c9822b4e245aec098a795d013e036916bda38`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/replay_degree10_controls.py` (SHA-256 `ec97e86622ec5c4673135e30d34c6364abc1aa0fd4a32334af2d905f5405202a`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/audit_high_radical_components.sing` (SHA-256 `d5b2a9750676f9cc37d2469cd9b1ea7daec6d584ef52a87b801311ba930258ef`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/audit_main_a_chart.py` (SHA-256 `465f459154dfa370dcfee2f7d7404277895a024de6e302318f6bb19cfb247e90`)
- `cases/as_fonly_d7_degree10_pointwise_20260824/audit_main_g_chart.py` (SHA-256 `1487dc1ab124e476a1e8bab0a5b65490fc5e2bdb90d2517d14dbd2a8c736fb4c`)

Confirmed divided-carry predecessor, consumed as the named source and to refuse promotion into a second-digit classification:

- `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md` (SHA-256 `cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194`)
- `xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-review-grok-20260824.md` (SHA-256 `4e915fb6f7e8701d1932b2b28df76db35859520bc94ffe8fb08a1cd679936ae8`), overall **CONFIRMED**

The charged basis is `a04affb7247fb5e87cad4e87f5926ab440254b24`. Review started there. During the window an unrelated commit `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`) advanced `HEAD`; it does not touch this gate. The charged basis remains an ancestor. Named producer artifacts remain uncommitted. Recomputed producer hashes at close match the launch table. No producer, case, canonical, prompt, log, run, ladder, coordination, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_d7_d10_pointwise_review/` and did not import `generate_degree10_gate.py`, `generate_reduced_pointwise.py`, `audit_source_compression.py`, `replay_degree10_controls.py`, or any Singular payload as mathematical evidence.

Tried hard, and failed, to leak an omitted degree-one/two or degree-six Frobenius coefficient into the degree-ten row after the relevant division modulo three; to make the fifteen linear eliminations a radicalization or a hidden localization; to change `H` by reversing generators or switching to `lp`/`Dp`; to find a rank-one, rank-two, or field-valued rank-four point of `H`; to make `I_4(A)` vanish on nonreduced `H` rather than only on `sqrt(H)`; to make `sqrt(J)` strictly larger or smaller than `C_a ∩ C_g`; to cover a nonzero field point of the cone with `a=g=0`; to make the `g`-chart compatibility ideal equal to `(z)` rather than `(z^3)`; to cancel the displayed `a=1` cap-boundary monomial `2x^3 y^5` by a cap-seven divergence; to make the vertical or `g` control fail modulo `81`; and to promote the gate to a complete next-digit classification, full `D=7` emptiness, all-depth lifting, characteristic zero, a counterexample, or JC2.

---

## Promotion

**Accept `ON THE REVIEWED ALIGNED DEEP BRANCH, RETAIN THE ORIGINAL NONREDUCED DIVIDED-CARRY PREDECESSOR. AFTER EXACT LINEAR ELIMINATION, THE NEXT DEGREE-TEN MIXED-CARRY EQUATIONS ARE AN AFFINE SYSTEM A(base) xi + beta(base)=0 WITH A OF SIZE 8 BY 9. FIELD-VALUED RANK ZERO IS EXACTLY THE DEGREE-FIVE-ZERO VERTICAL COMPONENT; EVERY NONZERO DEGREE-FIVE POINT HAS RANK THREE; RANKS ONE, TWO, AND FOUR DO NOT OCCUR; THE VERTICAL COMPONENT IS COMPATIBLE; ON THE NONZERO RATIONAL-NORMAL-CONE COMPONENT, COMPATIBILITY HAS EXACTLY TWO REDUCED ENDPOINT BRANCHES.`**

On the map-only aligned deep branch `P=x-x^3+3U+9C`, `Q=y+3V+9D` with the confirmed 40-variable/30-row first-digit ideal:

- Over `Z`, `det J(P,Q)-1=3L+9(K+C_x+D_y)+27M+81N` with the displayed signs of `L,K,M,N`. After the first residual is divisible by three, the degree-ten coefficient of `(det J-1)/27` modulo three is exactly `M_10`. No omitted lower layer and no degree-six Frobenius coefficient contributes there.
- Exact linear elimination of the fourteen first-divergence rows plus the divided-linear Cartier row is an isomorphism
  `full 40-variable predecessor = A^11 x Spec(H)`
  onto the displayed 15-row nonreduced high ideal `H` in `F_3[h,p,q,r,s,t,w,a,b,c,d,e,f,g]`. Here `A^11=A^7 x A^4` is the omitted low factor times the four derivative-invisible degree-three coefficients. The six degree-six Frobenius coefficients remain an additional free `A^6`. Over `dp`+`redSB`: reduced Groebner size `254`, `dim(H)=7`, radical Groebner size `29`. Dropping the free `h`, `minAssGTZ` returns two dimension-six primes: the vertical prime `(a,b,c,d,e,f,g)` and a 29-generator rational-normal-cone incidence prime. Fitting starts from nonreduced `H`; the radical and the two primes never replace it.
- Solving the seven degree-six accepted-divergence rows is reversible over `F_3` on the seven dependent columns
  `(c7_1,c7_2,d7_2,c7_4,c7_5,d7_5,c7_7)`,
  leaving the displayed nine free digits `xi`. Independently regenerated `A` and `beta` match the static matrix, including signs.
- Over the original nonreduced `H`:
  `I_1(A)=Z5=(a,b,c,d,e,f,g)` as polynomial ideals,
  `I_4(A)=0` modulo `sqrt(H)` but not modulo `H`,
  `(H+I_3(A)):Z5^infinity=(1)`.
  Consequently, among field-valued points of `H`, rank zero is exactly the vertical component, every nonzero degree-five point has rank three, and ranks one, two, and four are absent.
- Compatibility `J=(H+I_4(Aug)):Z5^infinity` has Groebner size `53` and dimension six. Two-sided,
  `sqrt(J)=C_a ∩ C_g`
  with `C_a=(b,c,d,e,f,g,s,w)` and `C_g=(a,b,c,d,e,f,p,q)`, both of dimension six including free `h`. The `a≠0` chart has compatibility ideal `(z)`; the `g≠0` chart has compatibility ideal `(z^3)`, whose field support is `z=0`. The two charts cover every nonzero field point of the cone. The outcome is the displayed four-line field-valued list (13), not a scheme-theoretic two-component claim and not a complete next-digit classification.
- Integer controls: the vertical and `g`-endpoint maps extend one cap-seven digit further with literal determinant `1+81x^4+648x^6+1134x^8`, hence `1 mod 81`. The displayed `a=1` point passes the degree-ten row and then fails the separate cap-seven degree-eight boundary at `2x^3 y^5`. That failure is a pointwise negative control, not a proof that the entire `a`-endpoint family is killed.

**Do not promote this to:** a classification of every remaining next-carry row on the survivor locus; a statement about other associated-top branches; emptiness or nonemptiness of `FONLY_(3,7)(D=7)` or of the full depth-seven locus; all-depth lifting or nonlifting of the vertical or `g` controls; a polynomial, restricted-analytic, or characteristic-zero lift or no-lift theorem; a counterexample to JC; or any JC2 inference. Do not replace `H` by `sqrt(H)`, by a minAss prime, or by a cone chart before forming Fitting ideals. Do not read the `g`-chart multiplicity `z^3` as a second reduced component. Do not read (13) as a complete next-digit classification, and do not read the displayed `a=1` failure as a proof that every `a`-endpoint point fails the degree-eight boundary.

**Smallest honest successor.** Attach the remaining next-carry rows of degrees nine down through the cap boundary to the vertical and `g` endpoint branches, reconstruct every surviving digit over the original integer expansion `(2)`, and only then attempt the following depth. Retain nonreduced `H` (and the thickening of `J`) through that recursion. A reduced-only calculation still covers field-valued points of *this* gate; it is not an honest successor for accepted-digit / Fitting recursion.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as a complete next-digit classification, or as emptiness/nonemptiness of `D=7`;
- this gate as all-depth lifting or nonlifting, a characteristic-zero statement, a counterexample, or JC2;
- replacement of the original nonreduced `H` by `sqrt(H)`, by `P_v`, by `P_m`, or by either cone chart, before the Fitting ideals are formed;
- the equality `I_4(A)=0` as an identity modulo nonreduced `H` (it holds modulo `sqrt(H)` and therefore on field-valued points);
- the equality `J=C_a ∩ C_g` as schemes (only `sqrt(J)` equals the endpoint union);
- the `g`-chart ideal `(z^3)` as a second reduced component;
- the displayed `a=1` cap-boundary failure as a proof that the whole `a`-endpoint family is killed.

The earlier 29-row first-residual predecessor remains quarantined; no statement here uses it. Producer strings `PASS-DEGREE10-SOURCE-COMPRESSION`, `PASS-DEGREE10-ENDPOINT-CONTROLS`, `PASS-STATIC-POINTWISE`, `PASS-REDUCED-POINTWISE`, `PASS-HIGH-DECOMPOSITION`, `PASS-MAIN-A-CHART`, and `PASS-MAIN-G-CHART` were not used as evidence. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim.

---

## Scope (not enlarged)

One prime `p=3`; one total-degree cap seven; the aligned deep branch of the confirmed 30-row first-digit ideal; the degree-ten mixed-carry row after exact linear compression; field-valued rank and compatibility strata of that affine system. No rectangular support, no enumerator, no AWS, no gauge cap, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | From `P=x-x^3+3U+9C`, `Q=y+3V+9D`, the identity `det J-1=3L+9(K+C_x+D_y)+27M+81N` holds over `Z` with the displayed signs. After the first residual is divisible by three, the only total-degree-ten term of `(det J-1)/27` modulo three is `M_10`. Omitted degree-one/two layers and degree-six Frobenius coefficients do not contribute there | **CONFIRMED** | a leftover sign on `K` or `M`; `L/3` or a lower second-digit layer reaching degree ten after the division; a degree-six Frobenius monomial producing a nonzero degree-ten residue modulo three |
| 2 | The 40-variable/30-row predecessor compresses by invertible linear elimination to `A^11 x Spec(H)` with the displayed 15-row `H`, `dim(H)=7`, reduced Groebner size `254`, radical size `29`, two dimension-six minAss primes after dropping free `h`, and no radicalization or hidden localization of `H` | **CONFIRMED** | a vanished or extra high row; a coefficient mismatch against independently reduced `K`; rank of the fifteen linear rows less than fifteen; `dim(H)` other than 7 in the 14-variable `dp` ring; a third minAss prime; Fitting formed from `sqrt(H)` or a cover piece |
| 3 | Independently regenerated `A` is the displayed `8 x 9` matrix and `beta` matches the static inhomogeneous column, including signs. The seven accepted-divergence rows have rank seven on the sixteen `(C_7,D_7)` coordinates and rank seven on the seven dependent columns, so the solve is reversible | **CONFIRMED** | a sign or entry mismatch in `A` or `beta`; dependent `7 x 7` block of rank less than 7; a free digit appearing in `beta` after the solve |
| 4 | Over original nonreduced `H`: `I_1(A)=Z5`; `I_4(A)=0` modulo `sqrt(H)` and not modulo `H`; `(H+I_3(A)):Z5^infinity=(1)`. Field-valued rank zero is exactly vertical; every nonzero degree-five field point has rank three; ranks one, two, and four are absent on field-valued points | **CONFIRMED** | `I_1(A)` unequal to `Z5`; a field point of `H` with `I_4≠0`; saturation of `H+I_3` by `Z5` not unit; a field-valued rank-one, rank-two, or rank-four point |
| 5 | `J=(H+I_4(Aug)):Z5^infinity` has size `53` and dimension six, and `sqrt(J)=C_a ∩ C_g` two-sided. Both endpoint ideals have dimension six including free `h`. The `a≠0` chart recovers compatibility `(z)`; the `g≠0` chart recovers `(z^3)` with reduced support `z=0`. If `a=g=0` on the cone, the catalecticant rows force `b,...,f` to vanish on field-valued points, so the two charts cover every nonzero field point. This is not a scheme-theoretic two-component claim | **CONFIRMED** | a two-sided remainder between `sqrt(J)` and `C_a ∩ C_g`; chart compatibility other than `(z)` / `(z^3)`; a nonzero field point of the cone with `a=g=0`; reading `(z^3)` as a second reduced component |
| 6 | Independently rebuilt vertical, `a`, and `g` integer controls have `det J=1 mod 27` and zero degree-ten next residual. Vertical and `g` extend one cap-seven digit to maps with literal determinant `1+81x^4+648x^6+1134x^8`, hence `1 mod 81`. The displayed `a=1` point has next residual `x^6+xy^5+2x^3 y^5` modulo three and fails the cap-seven degree-eight boundary at `2x^3 y^5`. That failure is pointwise, not a family statement | **CONFIRMED** | a nonzero residue modulo 27 at any of the three points; a degree-ten term in any of the three residuals; vertical or `g` failing modulo 81 inside cap seven; the `a=1` residual missing `2x^3 y^5`; a proof that every `a`-endpoint point fails the degree-eight row |
| 7 | The result is only the degree-ten pointwise gate on this branch. Inferences about remaining next-carry rows, other branches, full `D=7`, all-depth lifting, characteristic zero, a counterexample, or JC2 are out of scope | **CONFIRMED** | `FONLY_(3,7)(D=7)=∅` or `≠∅` asserted; (13) sold as a complete next-digit classification; the successor sold as already computed, or as a reduced-only calculation of the Fitting program |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Registered commands, rerun unmodified from the case directory:

```sh
python3 audit_source_compression.py
python3 replay_degree10_controls.py
Singular -q audit_high_radical_components.sing
Singular -q audit_pointwise_static.sing
python3 generate_reduced_pointwise.py | Singular -q
python3 audit_main_a_chart.py | Singular -q
python3 audit_main_g_chart.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

All eight exited 0. Manifest contents matched. Static Fitting printed `H` Groebner/dim/radical `254/7/29/7`, rank-zero equals `Z5`, `A4` remainder `0` modulo the radical, nonzero rank-`≤2` empty, compatibility size/dim `53/6` with radical size/dim `14/6` equal to the endpoint union, and vertical `beta` remainder `0`. Generated Fitting printed the same numerical ledger. High `minAssGTZ` in the 13-variable ring (drop free `h`) printed two dimension-six primes of Groebner sizes `7` and `29`. The `a`-chart printed compatibility `(z)`; the `g`-chart printed compatibility `(z^3)`. These runs were regressions only.

Recomputed SHA-256 (all match the launch prompt and `FREEZE.txt`):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-degree10-pointwise-20260824.md` | `e4311a80aef2d3617c7b449e16cb19d34cfe25d31c558bb68f78ddc02fcae4ab` |
| `cases/as_fonly_d7_degree10_pointwise_20260824/MANIFEST.sha256` | `426210cbdbd61e0ec0fa92d39344d3746c8a4a421df7c07c70f5a0cab968e2a5` |
| `cases/as_fonly_d7_degree10_pointwise_20260824/FREEZE.txt` | `c92a911df945c64f8d148819e22aa985a6393be3643cec8002474c89e272bab1` |
| `audit_pointwise_static.sing` | `f1461b2826019bc10069d0222957b47f3fc6d3847af871274349a793c21cc2e5` |
| `generate_reduced_pointwise.py` | `2f573c9d55ca73d5483a0d625c9285cfdfb6122b3b437d30d402974ac45249bf` |
| `generate_degree10_gate.py` | `fd76a59e75de80b871f773879c8911e5dec1905375912b2074793fcdc4ff3ef5` |
| `audit_source_compression.py` | `f72a7cec68d732dc99d867abc24c9822b4e245aec098a795d013e036916bda38` |
| `replay_degree10_controls.py` | `ec97e86622ec5c4673135e30d34c6364abc1aa0fd4a32334af2d905f5405202a` |
| `audit_high_radical_components.sing` | `d5b2a9750676f9cc37d2469cd9b1ea7daec6d584ef52a87b801311ba930258ef` |
| `audit_main_a_chart.py` | `465f459154dfa370dcfee2f7d7404277895a024de6e302318f6bb19cfb247e90` |
| `audit_main_g_chart.py` | `1487dc1ab124e476a1e8bab0a5b65490fc5e2bdb90d2517d14dbd2a8c736fb4c` |
| `README.md` | `2ed36cb4a940d3fca3b47ba584b605ea6a422112a7f139dbbcabd5525e1a4309` |

Predecessor hashes, unchanged:

| Artifact | SHA-256 |
|---|---|
| divided-carry erratum | `cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194` |
| divided-carry hostile review | `4e915fb6f7e8701d1932b2b28df76db35859520bc94ffe8fb08a1cd679936ae8` |

---

## Independent recomputation

### 1. Integer orientation and the degree-ten row — CONFIRMED

Let `P_0=x-x^3`, `Q_0=y`, `P=P_0+3U+9C`, `Q=Q_0+3V+9D` in `Z[x,y]`. Direct expansion of the Jacobian, with integer derivatives and no reduction, gives

```text
det J(P,Q)-1
  = 3L + 9(K + C_x + D_y) + 27 M + 81 N,
```

with

```text
L = U_x + V_y - x^2,
K = (U_x - x^2) V_y - U_y V_x,
M = (U_x - x^2) D_y + C_x V_y - U_y D_x - C_y V_x,
N = C_x D_y - C_y D_x.
```

Three hundred twenty structured-plus-hashed `(U,V)` samples through degree seven left a zero remainder against the truncated identity `3L+9K`. Two thousand three hundred four `(U,V,C,D)` samples through degrees five and seven left a zero remainder against the full identity. No leftover `27`-term exists before a second digit is adjoined, and the sign of `M` is the displayed one.

On the first-digit scheme `L=3 L_3`. The first residual is then `L_3+K+C_x+D_y`. After that residual is itself divisible by three, 

```text
(det J-1)/27 ≡ (L_3+K+C_x+D_y)/3 + M   (mod 3),
```

since `3N` vanishes. Degree bounds on the charged branch `U_7=V_7=0` with displayed layers of degree at most five:

| Source | Maximum total degree |
|---|---|
| `L` from displayed `U,V` | 4 |
| `L` from a degree-six Frobenius monomial | 5 |
| `K` from two degree-five layers | 8 |
| `K` from degree five with degree six | 9 |
| `K` from two degree-six layers | 10, with integer factor `9` |
| `C_x+D_y` from a cap-seven second digit | 6 |
| `M` from displayed `U,V` and a degree-seven second digit | 10 |
| `M` from displayed `U,V` and a lower second digit of degree `≤6` | 9 |
| `M` from a degree-six first digit and a degree-seven second digit | 11 |
| `M` from a degree-six first digit and a degree-six second digit | 10, with integer factor `3` |

Thus the preceding divided quotient has degree at most eight, lower second-digit layers reach degree at most nine, and the only total-degree-ten term modulo three is `M_10` from displayed degree five against a degree-seven second digit. A double degree-six cross in `K` is divisible by nine, hence vanishes after the further division modulo three. Direct integer samples `U=x^6`, `V=y^6` against both a top second digit and a degree-six second digit produced degree-ten Jacobian coefficients divisible by `81`, hence `0` in `(det J-1)/27` modulo three.

Degree-one and degree-two coefficients cannot meet `M_10`: their derivatives have degree at most one. They occupy three independent linear divergence rows in ten variables, which is an `A^7` factor of first-digit acceptance and is invisible to (1).

### 2. Exact source compression — CONFIRMED

Independent `F_3` derivatives of generic `(U,V)` in degrees `1..5` produced the same fourteen nonzero first-divergence rows and fifteen nonzero carry rows of degrees eight and seven as the confirmed predecessor, plus the Cartier row `u5_3+v5_2`. Counts: `40` variables, `30` rows. The ten degree-one/two names occur only in the three low divergence rows, which have rank three, hence an independent `A^7` factor. Carry rows and `M_10` are free of those ten names.

Degree three has eight coefficients and three independent linear constraints

```text
u3_1 = 0,    v3_1 = 2 u3_2,    v3_2 = 1.
```

The four remaining names `u3_0,u3_3,v3_0,v3_3` are derivative-invisible modulo three (pure Frobenius monomials `x^3`, `y^3`) and do not appear in `K` at degrees eight or seven, nor in raw `M_10`. The only relevant degree-three parameter is `h=u3_2`. Degree four and degree five plus Cartier give the displayed affine normal form (4)--(5). The fifteen linear rows (three low, three degree-three, four degree-four, five degree-five including Cartier) have disjoint supports across degrees and rank fifteen, so the elimination is an isomorphism of affine schemes, not a saturation and not a passage to `sqrt(H)`.

Substituting the normal form into the fifteen carry rows produces exactly the displayed generators (6):

```text
ac+2b^2, ad+bc, 2bd+2c^2,
af+be+cd, 2ag+bf+ce+d^2, bg+cf+2de,
df+2e^2, 2dg+ef, eg+2f^2,
as+2br+2cp, 2bs+cr+2dp,
aw+2bt+2cq+ds+2er+2fp,
2bw+ct+2dq+2es+fr+gp,
dw+2et+2fq, 2ew+ft+gq.
```

None of these contains `h`. In the 14-variable ring `F_3[h,p,q,r,s,t,w,a,b,c,d,e,f,g]` with `dp` and `redSB`:

```text
reduced Groebner size(H) = 254
dim(H)                   = 7
radical Groebner size    = 29
dim(sqrt(H))             = 7
```

Reversed generators give two-sided remainder `(0,0)` against this basis. The same ideal has reduced sizes `63` in `lp` and in `Dp`, and size `95` after reversing the variable order; dimension seven is invariant. In the 13-variable ring that drops free `h`, dimension drops to six and `minAssGTZ` returns exactly two dimension-six primes:

- `P_v=(a,b,c,d,e,f,g)`, Groebner size 7;
- a 29-generator incidence prime `P_m` whose generators are the catalecticant/incidence relations of the rational normal curve of degree six, including the displayed degree-four matching conditions such as `sa-rb-pc` and `wa-tb-qc`.

This decomposition describes field support of `H`. Every Fitting ideal below is formed from the original 15-row `H`.

The six degree-six Frobenius coefficients are not among the 40 displayed variables and remain a free `A^6` of first-digit acceptance. They are not silently removed from (1): they do not meet `M_10` modulo three.

### 3. The affine `8 x 9` system — CONFIRMED

The seven degree-six coefficients of `K+C_x+D_y` are, for monomial `x^k y^{6-k}`,

```text
(k+1) c7_{k+1} + (7-k) d7_k = -K_{k,6-k}     over F_3.
```

Explicitly the unit-triangular system

```text
k=0:  c7_1 + d7_0 = -K_{0,6}
k=1:  2 c7_2       = -K_{1,5}    ⇒  c7_2 = K_{1,5}
k=2:  2 d7_2       = -K_{2,4}    ⇒  d7_2 = K_{2,4}
k=3:  c7_4 + d7_3 = -K_{3,3}
k=4:  2 c7_5       = -K_{4,2}    ⇒  c7_5 = K_{4,2}
k=5:  2 d7_5       = -K_{5,1}    ⇒  d7_5 = K_{5,1}
k=6:  c7_7 + d7_6 = -K_{6,0}.
```

The `7 x 16` coefficient matrix in `(C_7,D_7)` has rank seven. The `7 x 7` block on the dependent columns `(c7_1,c7_2,d7_2,c7_4,c7_5,d7_5,c7_7)` has rank seven, hence is invertible over `F_3`. The nine free names are exactly the displayed `xi`. The solve is therefore reversible: every accepted degree-six divergence class has a unique dependent completion for each free `xi`.

Independent substitution of this solve together with the linear normal form into the eight nonzero degree-ten coefficients of `M` produces the displayed matrix (7) and an inhomogeneous column that matches the static `beta` polynomial-by-polynomial, including every sign. The eight nonzero mixed slots are

```text
(0,10), (1,9), (3,7), (4,6), (6,4), (7,3), (9,1), (10,0).
```

The three vanishing slots `(2,8)`, `(5,5)`, `(8,2)` are the Cartier-type bidegrees at total degree ten. No degree-one/two name and no invisible degree-three name appears in `A` or in `beta`. The parameter `h` does appear in `beta`, which is why it is retained.

A global sign error on `M` would flip `A` and `beta` simultaneously and would contradict both the static matrix and the integer controls of §6. A sign error on the seed `-x^2` would change `K_6` and therefore `beta`, and is ruled out by the Jacobian identity of §1.

### 4. Field-valued rank/Fitting classification — CONFIRMED

Write `Z5=(a,b,c,d,e,f,g)`, `A_i` for the ideal of `i`-minors of `A`, and `Aug=[A|beta]`. Independently emitted `H`, `A`, and `beta` in the 14-variable `dp` ring give:

```text
I_1(A) = Z5                                    (two-sided, as polynomial ideals)
I_4(A)  reduces to 0 against sqrt(H)
I_4(A)  has 1296 remainders against nonreduced H
(H + I_3(A)) : Z5^infinity = (1)
(H + I_2(A)) : Z5^infinity = (1)
```

So rank zero is exactly vanishing of the degree-five coordinates, with no appeal to `H`. Every field-valued point of `H` lies on `sqrt(H)`, hence has `I_4(A)=0` and rank at most three. On the open set `Z5≠0` the saturation says `I_3(A)` is already the unit ideal modulo `H`, hence rank at least three. Ranks one and two are therefore absent on the nonzero locus, and rank four is absent on field-valued points. Rank four is *not* disproved as a scheme-theoretic statement on nonreduced `H`: the 1296 remainders show that `I_4(A)` does not lie in `H`. That is exactly why the producer wrote equation (9) modulo `sqrt(H)` rather than modulo `H`. Among field-valued points the classification is complete.

A matrix-changing check, reversing the nine columns of `A`, preserves `I_1(A)=Z5`, vanishing of `I_4` modulo `sqrt(H)`, and the unit saturation of `H+I_3` by `Z5`.

An `F_3` census on both standard cone charts, with `a∈{1,2}` or `g∈{1,2}` and the five remaining chart parameters ranging through `F_3`, produced only ranks

```text
vertical:            rank(A)=0, rank(Aug)=0
nonzero a-chart:     rank(A)=3
nonzero g-chart:     rank(A)=3
a-chart with z=0:    rank(Aug)=3     (compatible)
a-chart with z≠0:    rank(Aug)=4     (incompatible)
g-chart with z=0:    rank(Aug)=3
g-chart with z≠0:    rank(Aug)=4
```

No rank one, two, or four occurred for `A` itself. The displayed `a=1` point has `rank(A)=rank(Aug)=3`. A generic cone point with `z=1` has `rank(A)=3` and `rank(Aug)=4`.

On the vertical component `H+Z5=Z5`, and `beta` reduces to zero. Equation (1) is compatible there, with a 9-dimensional affine space of digits `xi`.

### 5. Compatibility and field support — CONFIRMED

Formed from original nonreduced `H`,

```text
J = (H + I_4(Aug)) : Z5^infinity
```

has reduced Groebner size `53` and dimension six. Its radical satisfies both containment directions against `C_a ∩ C_g`:

```text
size(sqrt(J)) = 14 = size(std(C_a ∩ C_g)),
dim = 6,
two-sided remainders (0,0).
```

The scheme-theoretic comparison goes only one way: `J ⊂ C_a ∩ C_g` with an 8-generator remainder in the other direction. So `J` is a nonreduced thickening of the endpoint union. Field support is the reduced union; the producer correctly takes the radical only after `J` is formed, and does not claim `J=C_a ∩ C_g` as schemes.

Both `C_a` and `C_g` have dimension six in the 14-variable ring (free coordinates `(h,p,q,r,t,a)` and `(h,r,s,t,w,g)` respectively).

The two standard charts, with independently substituted `A` and `beta`, give:

```text
a ≠ 0:  b=az, c=az^2, d=2az^3, e=2az^4, f=2az^5, g=2az^6,
        s=pz^2+rz, w=tz+qz^2,
        I_4(A)=0, I_3(A)=(1), compatibility ideal (z).

g ≠ 0:  f=gz, e=gz^2, d=gz^3, c=2gz^4, b=2gz^5, a=2gz^6,
        p=sz^2-rz, q=wz^2-tz,
        I_4(A)=0, I_3(A)=(1), compatibility ideal (z^3).
```

Over `F_3` one has `-1=2`, so the `g`-chart formulae `p=sz^2-rz` and `p=sz^2+2rz` coincide; likewise for `q`. The `g`-chart ideal is equal to `(z^3)` two-sided and is not equal to `(z)`; its radical is `(z)`. That is genuine nonreduced multiplicity on this chart, with field support `z=0`. It is not a second reduced component.

Coverage: imposing `a=g=0` on the nine catalecticant rows of `H` produces a zero-dimensional ideal whose radical is the origin `(a,b,c,d,e,f,g)` but which is not itself the origin (nilpotent generators `f^2`, `ef`, `e^2-df`, …). Every *field-valued* point of the cone with `a=g=0` is therefore the origin, which is the vertical component already accounted for. The two charts cover every nonzero field point. They do not cover the fat origin as schemes; the producer does not claim that they do.

Thus the complete field-valued outcome of this gate is exactly (13):

```text
vertical: a=...=g=0                         survives;
a endpoint: b=...=g=0 and s=w=0             survives D10;
g endpoint: a=...=f=0 and p=q=0             survives D10;
every other nonzero cone point               fails D10.
```

No global polynomial section is asserted. The remaining next-carry rows are not solved.

### 6. Integer controls — CONFIRMED

Rebuilding `P=x-x^3+3U+9C`, `Q=y+3V+9D` over `Z` at the three displayed points:

| Point | `(U,V,C,D)` | `(det J-1) mod 27` | residual `/27` mod 3 | cap-7 mod-81 extension |
|---|---|---|---|---|
| vertical | `(0, x^2 y, 2x^5, 0)` | `0` | `x^6` | yes, `E=2x^7`, `F=0` |
| `a=1` | `(y^5, x^2 y, 2x^5+2x^2 y^5, 0)` | `0` | `x^6 + x y^5 + 2 x^3 y^5` | no |
| `g` | `(0, x^2 y+x^5, 2x^5, 0)` | `0` | `x^6` | yes, `E=2x^7`, `F=0` |

None of the three residuals has a degree-ten term, which independently confirms compatibility of these three field points with (1) without using `A` or `beta`.

The two extensions are

```text
P = x - x^3 + 18 x^5 + 54 x^7,
Q_vertical = y + 3 x^2 y,
Q_g        = y + 3 x^2 y + 3 x^5.
```

For both, the literal integer determinant minus one is

```text
81 x^4 + 648 x^6 + 1134 x^8,
```

which is `0 mod 81`. These are finite-precision controls only.

The displayed `a=1` residual modulo three is exactly (15). The degree-eight monomial `2x^3 y^5` cannot be hit by `E_x+F_y` for `deg(E,F)≤7`, whose divergence has degree at most six, and the bidegree is not a Cartier slot. This is one point of the `a`-endpoint family `C_a`, namely `a=1` with all other high coordinates zero (plus the seed `v3_2=1`). Other points of `C_a` have free `(h,p,q,r,t)` and are not evaluated. The producer correctly refuses to kill the family.

### 7. Scope arrows — CONFIRMED

Section 6 of the producer, the freeze typed-separate-boundary paragraph, and the README scope sentence all refuse: remaining next-carry rows on the full survivor locus; other associated-top branches; full `D=7`; all-depth lifting of the vertical or `g` controls; a polynomial / restricted-analytic / characteristic-zero lift or no-lift theorem; a counterexample; JC2. Equation (13) is not called a complete next-digit classification. The `a=1` failure is typed as a pointwise negative control. Radicals are used only after Fitting ideals are formed, and only to describe field support. None of these arrows is crossed.

The smallest honest successor is as in the promotion block: remaining next-carry rows on the vertical and `g` branches, reconstructed from the original integer expansion, retaining nonreduced structure.

---

## Attacks that failed to refute

- Leaking degree-one/two coefficients into `M_10` or into `H`.
- Feeding a degree-six Frobenius monomial into the degree-ten residue modulo three, either through `K` or through `M`.
- Making the fifteen linear rows less than rank fifteen, or making the compression a saturation / radicalization.
- Changing `H` by `lp`, `Dp`, reversed generators, or reversed variables.
- Finding a third minAss prime of `H`, or making `H` radical.
- A sign error in `A` or `beta`; a non-invertible accepted-divergence block.
- A field-valued point of `H` with rank one, two, or four; `I_1(A)` unequal to `Z5`.
- Making `I_4(A)` vanish on nonreduced `H` (it does not; 1296 remainders), which would have collapsed the producer’s modulo-`sqrt(H)` distinction.
- A two-sided remainder between `sqrt(J)` and `C_a ∩ C_g`; making `J` equal the endpoint union as schemes.
- Making the `g`-chart compatibility equal `(z)`; covering a nonzero field point of the cone by `a=g=0`.
- Cancelling `2x^3 y^5` at the displayed `a=1` point by a cap-seven divergence; making the vertical or `g` control fail modulo `81`.
- Promoting (13) to a complete next-digit classification, full `D=7`, all-depth lifting, characteristic zero, a counterexample, or JC2.

---

## Non-blocking remarks

1. Reduced Groebner size `254` is the `dp`+`redSB` size of `H` in fourteen variables. The same ideal has reduced sizes `63` in `lp` and in `Dp`. Quote the size together with the order, or quote the two-sided ideal. Dimension seven is order-invariant.
2. `I_4(A)` has 1296 remainders modulo nonreduced `H` and reduces to zero modulo `sqrt(H)`. Rank four is absent on field-valued points and is not disproved on the nilpotent thickening. The producer already wrote equation (9) this way.
3. `J` is properly contained in `C_a ∩ C_g` (8-generator converse remainder). Field support uses the radical, as claimed. Successor Fitting recursion must retain the thickening.
4. Imposing `a=g=0` on the nine catalecticant rows yields a fat origin, not the reduced origin. Chart coverage is a field-valued statement.
5. The `g`-chart formula `p=sz^2-rz` is the `F_3` rewrite of `p=sz^2+2rz` used by the chart generator. They agree.
6. In the 13-variable high-radical ring that drops `h`, one has `dim(H)=6` rather than `7`. Restoring free `h` restores dimension seven. The two minAss primes remain the vertical prime and the cone incidence prime.
7. The eight nonzero mixed slots omit the three Cartier-type bidegrees at degree ten. That vanishing is parallel to the universal Cartier lemma for `K`, not a missing equation.

None of these remarks changes a coefficient, a dimension, a containment, a rank stratum, or a numbered verdict.
