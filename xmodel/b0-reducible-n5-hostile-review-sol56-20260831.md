# Hostile Review: B0-REDUCIBLE-N5 (sol56)

## 0. Executive verdict

## 1. Frozen inputs and review standard

The two frozen files matched the required SHA-256 values before any report write:

```text
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Below, `B0:n` and `CNA:n` mean line `n` of those frozen files. I treated a promoted statement as usable only at the hypotheses printed in CNA or at a scope explicitly identified by B0, and treated every new `[D]` result as needing this review rather than inheriting promotion from its label. Floors are never read as attainments, and normalization places, physical points, and parametrization points remain separate.

No CAS was run and no uncertain-duration computation was started. I did not inspect `jc2-lean` or edit any charged or canonical file. Three local primary PDFs were read and rehashed: Orevkov, *Math. USSR-Izv.* 29 (1987), `jc86.pdf`, SHA-256 `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`; Żołądek, *The Jacobian Conjecture* (2008), `zoladek2008_official.pdf`, `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad`; and Nguyen Van Chau, arXiv:math/0305088v1, `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f`. I also streamed Karol Palka, arXiv:1405.5391v2, `https://arxiv.org/pdf/1405.5391`, SHA-256 `644552cf8d543868f44d6fdf40420c2885e6d0e4255e18c03fe0af8980d34fdd`; its printed p. 1, Theorem B, states the precise Abhyankar--Moh--Suzuki rectification used below. No source file was created.

## 2. Enumeration completeness

**Verdict: the post-(G4) numerical and ownership enumeration is complete; the advertised one-survivor enumeration is not.** The exact budget is `sum(mu_l+corr_l)=4`. A trivial dicritical is pointwise `(1,0)`, and promoted branch-locus nonemptiness forces at least one `mu>=2`. After reserving cost one for `(1,0)`, the only partitions of the remaining cost three compatible with these two facts are

```text
P1  (2,1)+(1,0)
P2  (3,0)+(1,0)
P3  (2,0)+(1,0)+(1,0).
```

This confirms B0:174-202. Before applying (G4), the displayed kill sheet is not literally exhaustive: it never writes the formal rows `(1,1)+(1,1)` and `(1,1)+(1,0)+(1,0)` (and abbreviates `(1,2)+(1,0)` as `(1,2)`). All are pointwise impossible, so this is a presentation omission, not an additional survivor.

Every component of `A_F` must be the image of an affine-image dicritical. Thus ownership is a surjection from dicriticals to components. Up to relabelling equal trivial dicriticals, the five rows at B0:233-244 are exactly all surjections:

| row | component ownership | status before topology |
|---|---|---|
| P1 | separate owners, `m=2` | possible |
| P2 | separate owners, `m=2` | possible |
| P3a | three separate owners, `m=3` | possible |
| P3b | the two trivials share one owner, `m=2` | possible |
| P3c | `(2,0)` shares with one trivial, `m=2` | possible |

The cover-degree step is also sound. For a finite `h_l:A^1->D_i~`, projective completion has one point above the boundary, totally ramified of index `s_l`; Riemann--Hurwitz gives `D_i~=A^1` and `sum(e_t-1)=s_l-1`. Orevkov's local multiplicity definition and Lemma 3.1 give `M_t>=e_t mu_l`. Since Orevkov Lemma 2.1 separates finite points on the dicritical, direct summation—not an attainment argument—gives

```text
corr_l = mu_l(s_l-1) + sum_t (M_t-e_t mu_l),   with every final term >=0.
```

Hence every listed `s_l=1`: for P1, `2(s-1)<=1`; for P2, `3(s-1)<=0`; for P3, `2(s-1)<=0`; trivials already have `s=1`. This validates B0:204-225 and the `A^1` normalization claim without transferring immersivity between components.

The enumeration therefore ends with **three surviving rows before the AMS gate (P1, P3a, P3b), not one**. P3a/P3b are the report's own Survivor S2 at B0:462-472 and B0:506-519.

## 3. Profile-by-profile kill-gate audit

The gates are mathematically valid at the following scopes, but B0 overstates their promotion provenance. Żołądek Proposition 6.5(b), journal p. 457, is genuinely pointwise: `mu_x>mu_l` iff the derivative of the parametrized immersed curve vanishes, and `mu_l=1` makes that parametrization immersive. Thus (G4) kills every positive correction on a `mu=1` carrier without confusing a physical crossing with a critical parametrization point (B0:64-66,199-200).

The Zariski--Nagata gate is the all-degree statement for the finite normal model over regular `C^2`: purity makes its branch locus either divisorial or empty; if every `mu=1`, it is empty, and an irreducible finite etale cover of simply connected `C^2` has degree one. B0:183-189 instead gives the equivalent meridian argument. Either route is within the noninvertible Keller scope and kills `(1,0)^4`; no irreducibility of `A_F` is used.

For P2 and P3c, all corrections and hence `K_tot` vanish. On the branched component `W=3`; (LOC) gives `r_p<=5/3`, so its `A^1` normalization is injective. Since its parametrization is immersive, it is a closed embedded affine line. Palka Theorem B supplies AMS rectification. Trivial-component meridians act identically, so monodromy factors through the coordinate-line complement, whose fundamental group is `Z`. Its generator has respectively cycle type `1^2 3` (P2) or `1^3 2` (P3c), hence its cyclic image is intransitive. This contradicts transitivity of the connected five-sheeted cover. The argument at B0:327-354 is therefore sound.

The provenance labels need correction: (M-2) is introduced as `[D]` at B0:316-323 and Gate AMS as `[D]` at B0:327-335; B0:703-706 itself calls all `[D]` results unreviewed. They were not already promoted merely by being used. This review independently confirms both: the complement of a complex curve is connected, so the covering action is transitive, and the hashed AMS source above has exactly the required embedded-line scope. They may be promoted now, not described as previously promoted by either frozen input.

| profile | hostile verdict | reason |
|---|---|---|
| all `mu=1` | **KILLED** | Zariski--Nagata purity / nonempty branch locus |
| all formal `mu=1,corr>0` rows | **KILLED** | pointwise (G4) |
| P1 `(2,1)+(1,0)`, `m=2` | **SURVIVES** | correction prevents the AMS smoothness step |
| P2 `(3,0)+(1,0)`, `m=2` | **KILLED** | AMS at `W=3` plus transitivity |
| P3a `(2,0)+(1,0)^2`, `m=3` | **SURVIVES** | branched component has only `W=2` |
| P3b, two trivials sharing the other component, `m=2` | **SURVIVES** | branched component again has `W=2` |
| P3c, branched carrier sharing with one trivial, `m=2` | **KILLED** | AMS at `W=3` plus transitivity |

Corollary N-A-RES does not remove all of P3a/P3b. It kills only rows satisfying its numerical inequality (B0:430-450,464), while CNA:80-92 retains explicit and numerical OPEN rows even in the older `S_4` problem. No promoted `S_5` replacement closes those rows. Thus the requested “all but S1” conclusion cannot be recovered by silently spending the AMS, Nori, or `(M-2)` gates twice.

## 4. Survivor S1 pinning

**Verdict: the core P1 cage is confirmed, but the claimed full pinning is refuted as written.** P1 forces `m=2`, distinct owners,

```text
(mu,corr,s)_A=(2,1,1),  (W_A,a_A)=(2,3);
(mu,corr,s)_B=(1,0,1),  (W_B,a_B)=(1,4).
```

There is exactly one parameter `t_0` with `K=1`, so `M_{t_0}=3`; because `h_A` has degree one, `eta_A` is critical there. Both normalizations are `A^1` with one place at infinity. Chau Theorem 1 and Corollary 2 additionally confirm a common exponent pair and one common point at infinity for all components. These are necessary pins, not realization or disjointness of the two affine components.

Globally, the `D_B` meridian is trivial. The transitive representation factors through `pi_1(C^2-D_A)` and is generated by transpositions; hence its image is `S_5`. This is PI1-S4-*shaped* only at the level of a one-curve transposition quotient. S1 has a singular branch and is expressly outside the promoted PI1-S4/N-A singularity class (B0:496-504,622-629). In fact B0 calls S2—not S1—the exact PI1-S4-shaped analogue at B0:517-519.

The local typing needs three repairs.

1. At an ordinary/tangential double point of `D_A`, B0:484 and B0:573-580 set `a_p=1`. That is one branch only. If `D_B` also passes through `p`, (LOC) instead gives `r_B=1`, `a_p=0`, and one fixed `mu=1` boundary cluster. In either case `#Fix(G_p)=1`, so the two `D_A` branch transpositions are still disjoint. The disjointness conclusion survives; the asserted affine-fibre and incidence structure does not.
2. In S1a, the unique `D_A` place at `p_0` has orbit size three and the total fixed count is two (including any trivial-owner clusters), so its local projection is the natural `S_3`. The Fox determinant divisibility quoted at B0:585-593 is at most a local necessary/sufficient knot-colouring test and remains custody-conditional as B0:695-701 admits.
3. In S1b, (LOC) forces `D_B` away from `p_0`, `a_{p_0}=0`, and **two distinct local orbits of sizes `3+2`**. B0:594-599 incorrectly allows a five-letter orbit, contrary to the promoted fibre-point/orbit dictionary. DQ-2 also cannot call the whole local image “`S_3` moving exactly three letters”: its projections must be `S_3` on the singular-branch orbit and `C_2` on the disjoint smooth-branch orbit. Any stronger product assertion needs the local inertia relations written out.

The projective genus budget is exact:

```text
delta_infinity + delta_aff = (deg(D_A)-1)(deg(D_A)-2)/2.
```

For S1a, `delta_aff=delta(p_0)+sum k_p`; for S1b, `delta(p_0)` must mean the whole two-branch germ and satisfies the sharper bound `delta(p_0)=delta(C_sing)+I(C_sing,C_smooth)>=1+2=3`. B0:523-535 omits this refinement. The formula `deg D_A=3+2g_L+Sigma_infinity>=4` is internally consistent conditional on Gate TG, but Gate TG and the alleged independent graph proof both consume the same uncustodied generic-line `pi_1` surjection (B0:391-405,421-428,695-701). Hold the degree floor from promotion pending that custody; rename its transversal genus `g_L`.

Finally, B0:601-608 falsely infers that S1 needs another affine double point. A connected graph of generic-line meridian transpositions gives at least four edges and a degree floor; those meridians occur at smooth intersection points and may connect the two remaining letters through braid monodromy at infinity. It gives no affine-singularity count. “S1 with no other singularity is impossible” must be replaced by **OPEN**.

## 5. Ramified-cover escape at N=5

**CONFIRMED at `N=5`; REFUTED for the stated next-degree threshold.** Lemma B is a floor, and here that is enough. If `s_l>=2`, then `corr_l>=mu_l(s_l-1)`. A `mu=1` carrier cannot ramify because pointwise (G4) gives `corr=0`; hence a ramified carrier has `mu>=2`, `corr>=2`, and costs at least four. Reducibility requires a second component owner, costing at least one more. The total would be at least five, whereas the `N=5` Orevkov budget is four. Equivalently, applying the floor to P1--P3 gives `s_l=1` term by term as in §2. This proves the narrow “cannot occur at `N=5`” claim without assuming equality or a witness.

B0:220-222 and B0:668-675 then make an off-by-one error. At `N=6`, the budget is already five, and the necessary packet

```text
(mu,corr,s,K) = (2,2,2,0) + (1,0,1,0),   m=2,
(W,a) = (4,2) and (1,5)
```

meets every displayed budget and floor. It is only an arithmetic possibility, not a Keller-map attainment, but it proves that the first possible ramified reducible profile is at `N=6`, not `N=7`. The ramified-cover remainder must therefore reopen at `N>=6`; the recommendation to run `N=6` as if ramification were absent is unsafe.

## 6. NORI-BC-SELF-TANGENT-COEFF dependency

There is **no coefficient conflict** in the promoted gate, but the coordinator's test-object status is stale. The proven theorem-level condition is

```text
C'^2 > 2r_1 + 4T.
```

For the irreducible residual, `delta_aff=r_1+T` and the promoted infinity identity is `C'^2-2delta_aff=3d-2-M_infinity`. Substitution gives exactly

```text
M_infinity + 2T <= 3d-3.
```

Thus the `4T` and `2T` at CNA:23-49 live at different algebraic levels. B0:432-439 may consume the promoted scalar `+2T` gate for S2; B0:441-443 should be clarified, not used to replace it by `+4T`. S1 remains outside the gate because its distinguished singular branch violates the double-point-of-two-smooth-branches hypothesis. The coefficient OPEN bars improving the theorem-level `4T` to `2T` (which would remove `+2T` from the scalar gate); it does not invalidate the proved gate.

The specific “untestable” rational sextic at CNA:96-98 is in fact settled by Akyol--Degtyarev, *Geography of irreducible plane sextics*, arXiv:1406.1491v2, `https://arxiv.org/pdf/1406.1491`, streamed SHA-256 `724fccc5a0a192585420e484f56da4c6238b32d0dc506bc4e39606526779d70f`. Printed p. 5 states the induced-Dynkin-subgraph degeneration criterion; deleting vertices `4,8,12,16` from the `A19` chain in Table 2 (p. 7) leaves `5A3`. Theorem 2.5 (p. 8) therefore makes the non-special irreducible stratum `M_1(5A3)` nonempty. Each `A3` is a tacnode with delta two, so five consume the sextic arithmetic genus ten and the curve is rational. Corollary 2.9 (p. 9) gives `pi_1(P^2-D)=Z/6` for this nonmaximizing, nonexceptional stratum.

Hence the extremal test has a **positive, abelian** answer. That does not prove a general `4T -> 2T` improvement, so `OPEN[NORI-BC-SELF-TANGENT-COEFF]` remains, but its existence/group subquestion and the label `UNTESTABLE-AT-DESK` must be retired.

## 7. Promotion recommendation

## References checked
