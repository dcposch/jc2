# grok46 ideation 20260906T0000Z — small notes (not the report)

Custody: 12/12 charged SHA-256 OK via awk manifest + `sha256sum -c` against
`/tmp/jc2-lane.sj9fLK/inputs`. Receipt `xmodel/ideation-20260906T0000Z-grok46.run.v2`.
Xu 2016 opened from `refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf`
only to print eq (7.1) / Lemma 7.1 / Cor 7.5 (packet-named candidate). No other
`xmodel/ideation-20260906T0000Z-*` body was read.

## Roster ES leaves (family C): 36 records, not 38

Charged `roster.jsonl` enumerates 36 objects of type `ES_NECESSARY_LEAF_NOT_ATTAINMENT`
on 20 `u_s>=2` rows. Charged residual65-structure prices 38. Do not invent the two.

| row | (n,m) | us | rho leaves (Q, λ) |
|-----|-------|----|-------------------|
| R012 | 108,72 | 2 | 3 (Q=1, λ=1+1) |
| R015 | 99,66 | 3 | 2 (Q=1, λ=2+1); 5/2 (Q=2, λ=1+1+1) |
| R016 | 168,112 | 2 | 2 (Q=1, λ=1+1) |
| R023 | 165,110 | 2 | 4 (Q=1, λ=1+1) |
| R024 | 165,110 | 2 | 4 (Q=1, λ=1+1) |
| R029 | 168,112 | 3 | 3/2 (Q=2, λ=1+1+1) |
| R035 | 144,108 | 2 | 3 (Q=1, λ=1+1) |
| R038 | 135,90 | 4 | 2 (3+1); 5/2 (2+2); 5/2 (2+1+1); 8/3 (1^4) |
| R043 | 168,112 | 3 | 3 (2+1); 3 (1^3); 7/2 (1^3) |
| R044 | 147,42 | 2 | 2 (1+1) |
| R045 | 147,63 | 2 | 2 (1+1) |
| R049 | 189,126 | 2 | 3 (1+1) |
| R051 | 180,144 | 2 | 3 (1+1) |
| R052 | 165,99 | 3 | 2 (2+1); 5/2 (1^3) |
| R053 | 200,150 | 3 | 2 (2+1); 2 (1^3) |
| R054 | 175,70 | 2 | 2 (1+1) |
| R055 | 171,114 | 5 | 2 (4+1); 5/2 ×3; 8/3 (2+1^3); 11/4 (1^5) — 6 leaves |
| R062 | 180,135 | 4 | 2 (3+1); 5/2 ×2; 8/3 (1^4) |
| R065 | 180,120 | 3 | 5/2 (1^3) |
| R066 | 162,108 | 2 | 3 (1+1) |

Cor 7.5 threshold (vs+1)/(us+1): R015 us=3,vs=8 → 9/4=2.25; R012 us=2,vs=7 → 8/3≈2.667.
Surviving leaves sit at or above that threshold, or split to fewer than `us` roots.

## Xu (7.1) printed (arxiv 1604.07683v4 p.11)

∂(Ts(σ), g(σ))/∂(t,π) = −J · (Ts)_f(σ) · t^{−2+δ}

(99,66) §8: (7.1) kills all split δ except δ=2 (reproduces Moh two-root, eq 8.2) and
δ=5/2 (holds identically via q1 = −2 ∫ p³). That identity is why c is not forced
nilpotent by the face ODE alone.

## Margin-0 Xu rows (family A)

R009 (192,128) M=(−128,148,190) V=(2,3) δ=(19/24,5/16,−1) → child (48,32; M'=37; V'=2; δ'=(4/3,−1/5); 388 unk)
R050 (196,56) M=(−56,184,194) V=(4,3) δ=(19/28,1/4,−1) → child (49,14; M'=46; V'=4; δ'=(5/7,−1); 1392 unk)
R011 margin 1: (140,84) → (35,21), 471 unk.

## Do not

- Rerun band engines at T_J < n+m−2 (cone-vertex: T0 = 178 / 163).
- Rerun 2500-generator char-degree fleet (compute-bound OPEN; disk).
- Treat 36 roster leaves as 38.
- Promote T2 ∈ rad J_t for t≤8 from (T)_8 as the uniform statement.
