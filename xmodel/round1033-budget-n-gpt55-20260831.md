# BUDGET-N Source Typing Report

## Hash Verification

Frozen lane inputs were verified before use:

```text
329182487ac3e771be9aa73ded7b9f21c6ea3fd8e13235caafb8e103c96007a3  inputs/ideation-20260831T1033Z-grok46.md
eeb4670511f35b7c52f03fa03d334eadff9eb3b7f3b6e18011beb7de4e73c54b  inputs/block-descent-a1-rank4-dicritical-typing-d1-d4-grok46-20260831.md
bc4ff4046e4f481e87c451440a078929eee22eae16c59c2bc31ddfd5bb4a9bec  inputs/block-descent-a1-rank4-dicritical-typing-hostile-review-gpt55-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  inputs/ideation-20260831T1033Z-synthesis.md
```

The charged originals were not inspected. The rank-four typing packet is treated only as a routing input; no rank-four bracket is exported to general degree.

## Source Inventory

Primary sources used and byte pins:

| Source | Pin |
|---|---|
| S. Yu. Orevkov, *On three-sheeted polynomial mappings of C^2*, Math. USSR-Izv. 29 (1987), 587-596. Local cached PDF [refs/jc86.pdf](/Users/dc/code/math/jc2/refs/jc86.pdf). | `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db` |
| Nguyen Van Chau, *Non-zero constant Jacobian polynomial maps of C^2*, Ann. Polon. Math. 71 (1999), 287-310. Local cached PDF [refs/chau1999_apm71_full.pdf](/Users/dc/code/math/jc2/refs/chau1999_apm71_full.pdf); fresh IMPAN stream `http://matwbn.icm.edu.pl/ksiazki/apm/apm71/apm7135.pdf`. | local `ed63b44c6a48f85c80b66e4b95b93618f1b3a4bead536a7ad7ee1bfa5084aac7`; fresh `febddbecb4c54d354fefca1a7e7730fcc18c0e2807fe3e03b5af8017b1d59d39` |
| Nguyen Van Chau, *Non-proper value set and the Jacobian condition*, arXiv:math/0305088v1 (2003), published note corresponding to the 2004 citation. Local cached PDF [refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf](/Users/dc/code/math/jc2/refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf); fresh arXiv stream `https://arxiv.org/pdf/math/0305088`. | `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f` |
| Nguyen Van Chau, *Pencil of irreducible rational curves and Plane Jacobian conjecture*, arXiv:0905.3939v3; Ann. Polon. Math. 101 (2011), 47-53. Fresh arXiv stream `https://arxiv.org/pdf/0905.3939`. | PDF `c7eee42dfb8cc18b07598748457763d5cf54fdbcb7b574bbf295d26fafed079c`; abs page `02759c06f559e4813183a4339b22c3a6887f11d7ed23ca0cbee262aa9d2346b4` |

Extracted source points. Orevkov defines `L_F` as the nonconstant finite-value part of the boundary after regularisation, proves each `L_FC` chain has a unique `L_F` endpoint, defines the local multiplicity `mu_x`, and states Lemma 4.2:
`sum_{l subset L_F}(mu_l f* + sum_{x in pi(l)-{infty}}(mu_x f* - mu_l f*)) = N - 1`, with nonnegative inner summands and Corollary 4.3 `sum mu_l <= N-1`. The symbol `N` is the geometric multiplicity of the map, not a degree-four parameter.

Orevkov Lemma 3.1 is the local normal form at a generic branch point: in suitable holomorphic coordinates the map is `u=x'`, `v=y'^k`. Thus a genuinely nontrivial inertia/ramification index has `k>=2`, and this is a statement about generic inertia, not about the fundamental group of the target component.

Chau 2011, under finite fibres, defines a dicritical component as an irreducible boundary component on which `(p_l,q_l)` is nonconstant and writes
`A_F = union_l (f(l) cap C^2)` over dicritical components. Chau 2004 gives the series-level analogue and converse for irreducible components of `A_f`, but the line-level 2011 statement is the clean source for the owner map here. Chau 1999 records the Newton-Puiseux/function-level background and an Orevkov formula restatement; no termwise series-to-line correction transfer is used below.

## Typing Matrix

Let `B subset A_F` be the reduced charged branch, with `m_nt` components whose generic compactification inertia is nontrivial and `m_triv` components whose generic inertia is trivial; `m=m_nt+m_triv`. An owner of a component `B_i` means a dicritical boundary component `l` whose affine image closure is `B_i`.

| Dependency | all N | degree-four only | absent |
|---|---|---|---|
| (D1) each Orevkov/Chau dicritical `l` has one irreducible nonconstant affine image `alpha(l)` | Sourced: irreducible curve mapped nonconstantly; Orevkov `L_F`, Chau 2011 dicritical component. | - | - |
| (D2) `alpha` surjects onto `Irr(A_F)`, hence onto `Irr(B)` | Sourced: Chau 2011 finite-fibre component union; Keller maps have finite affine fibres. | - | - |
| (D3) every owner/dicritical has `mu_l >= 1` | Sourced/derived from Orevkov's domain multiplicity. | - | - |
| (D4) Orevkov budget `N-1=sum_l(mu_l+corr_l)`, `corr_l>=0` | Sourced: Orevkov Lemma 4.2 and Cor. 4.3. | - | - |
| distinct-owner-per-component lemma | Derived from (D1)-(D2): choose one owner over each `B_i`; one irreducible source image cannot be two distinct target components. | - | - |
| owner multiplicity `mu_l>=2` for a component with nontrivial generic inertia | Typed conditionally: by Orevkov's local form `v=y'^k`, genuine nontrivial inertia means `k>=2`, hence the corresponding generic local multiplicity on an owner is at least two. This uses inertia, not nontrivial `pi_1`. | A separate degree-four inertia input may eliminate `m_triv`; that input is not exported to general `N`. | - |
| trivial-inertia fork: does such a component own a dicritical, and at what cost? | Yes, it still owns a dicritical by (D2), but primary sources type only `mu_l>=1` by (D3). | - | `mu_l>=2` for trivial inertia is absent. |

## First Absent Load-Bearing Hypothesis

The first absent load-bearing hypothesis for the strong bound is:

> every component of the reduced charged branch has an owner dicritical with `mu_l >= 2`.

Primary sources prove this only for components whose generic compactification inertia is actually nontrivial. They do not prove that a component with trivial generic inertia costs two in Orevkov's sum. They do prove that such a component still owns a dicritical and costs at least one. Therefore the source-typed general-degree output is the weighted bound

```text
2*m_nt + m_triv <= N - 1.
```

This statement does not use "nontrivial pi1 of a component" as a proxy for nontrivial inertia. A separate theorem that only supplies nontrivial `pi1` does not increase `m_nt` unless it also identifies the generic inertia.

## Symbolic Replay

Choose distinct owner dicriticals for the `m_nt+m_triv` components of `B`. For nontrivial-inertia owners use `mu>=2`; for trivial-inertia owners use only `mu>=1`:
`2*m_nt + m_triv <= sum_{owners} mu_l <= sum_{l subset L_F} mu_l <= N-1`.

At `N=4`, if one consumes the separate degree-four inertia input `m_triv=0`, this specializes to `2*m <= 3`; hence `m<=1`.

## N=5 Case

At `N=5`, primary sources alone give

```text
2*m_nt + m_triv <= 4.
```

Explicit cases:

| `m_nt` | allowed `m_triv` | resulting `m` bound |
|---:|---:|---:|
| 0 | `m_triv <= 4` | `m <= 4` |
| 1 | `m_triv <= 2` | `m <= 3` |
| 2 | `m_triv <= 0` | `m = 2` |
| >=3 | impossible | impossible |

Thus rank five is not forced irreducible by Orevkov-Chau sources alone. If an additional, separately sourced rank-five theorem proved all charged components nontrivial-inertia, then the same inequality would collapse to `2*m<=4`, i.e. `m<=2`; that extra theorem is not present here.

## Conclusion

Primary sources support the all-degree Orevkov-Chau budget and the distinct-owner construction. They do not support exporting the rank-four doubling to trivial-inertia components. The reduced charged branch of a canonical degree-`N` proper block therefore satisfies the typed weighted component bound

```text
2*m_nt + m_triv <= N - 1
```

with the trivial-inertia coefficient equal to one. The strong all-degree bound `2m<=N-1` is `OPEN` at the first absent hypothesis `mu_l>=2` for trivial-inertia owners.

<!-- BODY-END -->
