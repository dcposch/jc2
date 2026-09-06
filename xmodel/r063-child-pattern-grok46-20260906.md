# DATA: child printed-closure I'_M, I'_m — Grok 4.6 — 2026-09-06

```text
TYPE. DATA (a replay, not a theorem).
R063 child: 0 printed-complete configs in either convention.
  Shifted ungated I'_M = 71/4 (the earlier exact-contact value); D1 galois
  fails on the zero-centre sibling. Unshifted lattice empty. Neither equals 19.
R009/R050 child: unshifted empty; shifted has 1 printed-complete config each
  with I'_M = 8 = parent I_M. 71/4 does not appear. I'_m is 7 (R009) and
  11/2 (R050), not the parent I_m = 8.
Parent R063 printed-complete N = 0 (frozen table reproduced). The charged
comparison target 19 is the earlier flat/coarse survivor, not a printed-
complete parent tree.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` joined by index with `awk`,
then `sha256sum -c` on `/tmp/jc2-lane.e1ztmS/inputs`: **6/6 OK**. Mathematical
reads were those frozen copies plus the gate scripts
`box/exact-contact-gate-20260906/{census_replay.py,closure_fixed.py}` (path
redirect only; identities not rewritten). No ledger, no `jc2-lean`, no
`ideation-*`, no fleet. Driver: `box/r063-child-20260906/r063_child.py`.
JSON 47 KB. Report+JSON ≤ 1 MB.

## 1. What was computed

**Own child.** `descend_own` on the frozen roster rows. All three:
`DETERMINED_PROP6.4`, top `DETERMINED_COMPLETE_US1`, route `NONEMPTY`,
`V` DETERMINED (one vector), Def 5.1 radii agree with the `(ℓ+1)`-scaled
formula, `ℓ = v_s − u_s − 1 = 1`. `'` is a generation label, not a
derivative. Child source `(n',m',s',M',d',V')`:

| row | `(n',m')` | `s'` | `M'` | `V'` |
|---|---|---:|---|---|
| R063 | `(42,28)` | 3 | `(-28,35,40)` | `(3,7)` |
| R009 | `(48,32)` | 2 | `(-32,37)` | `(2)` |
| R050 | `(49,14)` | 2 | `(-14,46)` | `(4)` |

**Printed closure.** Same `cf.patterns` / `Closure.node` packet arithmetic as
the frozen integrality table (actual centre `L`: zero keeps `L`, nonzero
`lcm(L,den δ)`; Prop 5.3 along the child's own `M'`-list; `D_1` final by
Prop 4.6; residues `ρ_f,ρ_g ≡ 0 or 1 (mod A)`, not both 1). Enumeration
starts at the child top `i=s'` with `ρ=m'`, `L=1`. `A=1` translations are
identified, matching the parent table, not the coarser `census_replay.configs`
count.

**Two conventions.** Unshifted: `1` in `δ` and `κ` (Jacobian `J=1` formulas
on the child's `M',V'`). Shifted: printed `1 → 1+ℓ` (Xu Lemma 4.1
`−c t^{-ℓ-2}`; Moh Prop 4.6(3)*). Radii from `def51_radii(..., multiplier=1+ℓ)`.
`I'_M` is the complete final-major sum. `I'_m := 1 +` unsplit minor excesses
is Xu Cor 5.3's expression applied to the child's packets (**DATA**; child
Thm 4.7 is not printed, typed OPEN as a theorem). Ungated numbers keep the
`D_1` `J` when residues fail, for the 71/4 comparison only.

Parent control: `cf.Closure.run()` on the frozen roster source.

## 2. Parent printed closure (control)

| row | `N` complete | survivors | charged comparison `I_M` |
|---|---:|---|---|
| R063 | **0** | — | 19 (flat/coarse, earlier replay) |
| R009 | 1 | `(8,8)` | 8 |
| R050 | 1 | `(8,8)` | 8 |

R063 parent `N=0` reproduces the frozen integrality table (empty complete
tree: unique actual-`L` `p_3=π^{21}`, `p_2=π^{12}(π^{10}-c)^3`, zero sibling
`D_1` with `A=59` fails residues). It is **not** a printed-complete `I_M=19`.
R009/R050 unique `(8,8)` likewise reproduce that table.

## 3. Child configurations

**Unshifted** (`ℓ=0` formulas, unscaled Def 5.1 radii). All three rows:
**0** admissible selected patterns (the `A`-lattice at child `D_{s'}` does
not contain `V'`). No `I'_M`, no `I'_m`, no 71/4, no match to 19 or 8.

Shifted radii: R063 `(7/6,−1/3,−2)`; R009 `(4/3,−1/5)`; R050 `(5/7,−1)`.

**Shifted** (`ℓ=1`). Selected-path patterns, printed-complete pairs, ungated
numerical trees:

| row | # patterns | # complete | complete `(I'_M, I'_m)` | ungated `I'_M` | equals parent `I_M`? |
|---|---:|---:|---|---|---|
| R063 | 1 | **0** | — | `71/4` | no |
| R009 | 2 | **1** | `(8, 7)` | `8`, `592/29` | **yes**, complete `8` |
| R050 | 2 | **1** | `(8, 11/2)` | `8`, `146/13` | **yes**, complete `8` |

R063 unique shifted pattern: `p_3=(π^{A}-c)^7` (`z=0`), `p_2=π^5(π^3-c)^3`,
`A_2=3`, `L_0=1`. Selected arm `D_1`: `L=3`, `A=2`, `ρ_f=6`, `J=3` (galois
OK, three conjugates). Zero sibling `D_1`: `L=1`, `A=24`, `ρ_f=10`,
`ρ_g=15`, `remf=10`, `δ=13/24`, `J=35/4` (**galois FAIL**). Product empty.
Ungated sum `3·3 + 35/4 = 71/4`. `I'_m` packets `=0`, so the Cor 5.3
expression is `1`.

R009 complete pattern `p_2=π(π^5-c)^2(π^5-d)` (`z=1; 1,2`), selected
nonzero `r=2`. Minors: one zero copy plus five `r=1` copies, excesses
`1+5=6`, `I'_m=7`. `I'_M=5·(8/5)=8`. The other pattern `z=6; (2)` has a
zero-centre major sibling, `D_1` `A=29`, `ρ_f=12`, galois FAIL; ungated
`8+360/29=592/29` (the earlier exact-contact extra).

R050 complete pattern `p_2=(π-c)(π-d)^2(π-e)^4` (`z=0; 1,2,4`), `A=1`.
Minor excesses `4+1/2=9/2`, `I'_m=11/2`. `I'_M=8`. The `(3,4)` sibling is
major, `D_1` `A=13`, `ρ_f=6`, galois FAIL; ungated `8+42/13=146/13`.

`census_replay.configs` actual-`L` counts (shifted) are 2, 2, 7 on
R063/R009/R050: the extra objects are `A=1` `z>0` translations or
zero-selected faces that `cf.patterns` (the parent table's filter) drops.
The printed-complete counts above use that filter.

## 4. The four questions

1. **Number of child configurations** (printed-complete / selected patterns /
   ungated numerical): R063 `0/1/1` shifted and `0/0/0` unshifted; R009
   `1/2/2` shifted and `0/0/0` unshifted; R050 `1/2/2` shifted and `0/0/0`
   unshifted.
2. **Values.** Unshifted: none. Shifted complete: R009 `(I'_M,I'_m)=(8,7)`;
   R050 `(8,11/2)`. Shifted ungated extras: R063 `71/4`; R009 `592/29`;
   R050 `146/13`.
3. **Equals parent `I_M`?** Unshifted: no (empty). Shifted complete: R063
   no (empty, so not 19); R009 yes (`8=8`); R050 yes (`8=8`). Ungated
   shifted R063 is `71/4 ≠ 19`.
4. **Does 71/4 reappear?** Only as R063's **ungated shifted** numerical sum.
   It is not a printed-complete value and does not appear unshifted.

`I'_m` is not the parent `I_m=8` on R009/R050. That is a measured
difference of the Cor 5.3 expression, not a child theorem.

## 5. FALLACY-v2

*Floor/attainment.* `I'_M` is the node's complete major sum, not a floor.
`I'_m` unsplit is a floor; equality `I'_M=I(f_ξ,g)` is not claimed.
*Carrier/attainment.* Rows remain `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.
An empty complete tree is not a pair and is not promoted.
*Prime label.* `'` is the child generation.
*Variable/ring map.* Child `(n',m',M',d',V')` from `descend_own`; matching
names are not a proof.
*Merge-free/M-descent.* Own `V'` from `descend_own`, never copied `V`.
*Pole/interior.* Prop 4.6 `r=1` is used only at `D_1` after the vertex class
(final major/minor by `κ` sign) is checked.
*Child Thm 4.7.* Typed OPEN; `I'_m` is the printed parent formula evaluated
on child packets, not filled by cap or analogy.
*Replay is evidence; type DATA.* R009/R050 `I'_M=8` is MEASURED under the
shifted printed closure, not a descent-partition theorem.

Positive controls: parent R009/R050 unique `(8,8)`; R063 parent empty;
shifted ungated extras `592/29` and `146/13` match the frozen exact-contact
child replay; R063 ungated `71/4` matches that replay's unique child value.

Replay: `python3 box/r063-child-20260906/r063_child.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7410`.
- Body SHA-256:
  `86d5cfb4759afcaa38993497223634bc9d3f46bcb82501277fa17e8cc1f38b17`.
- Frozen basis: `ce6e23ea53f8493b1cea8c03ddde5684f53eecce`.
