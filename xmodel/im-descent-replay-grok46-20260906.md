# OPEN 3 replay: I'_M vs I_M under Prop 6.3 — Grok 4.6 — 2026-09-06

```text
VERDICT.  Preservation FAILS.  Named counterexample: R063, unique parent
surviving I_M = 19, unique licensed-child config I'_M = 71/4 not in Z.
Seven further set-differences (child extras, or R001's Cor 5.3 kill not
reproduced).  32/46 complete u_s=1 rows have I'_M = I_M on every surviving
integer; 6/46 have no integer on either side; child quantity defined on 46/46.
A replay is evidence, not a lemma.  Candidate statement (FAILS) in Sec. 5.
```

No new exit-price assertion, so no `charge_basis=` line.

## 0. Custody

Manifest from the receipt's numbered `charged_input_<i>_sha256=`/`_basename=`
fields via `awk`, then `sha256sum -c` on `/tmp/jc2-lane.MIFdbX/inputs`: **4/4 OK**.
Mathematical reads were those frozen copies. No ledger, no `jc2-lean`, no
`ideation-*`, no fleet. Writes: this report and `box/im-descent-20260906/`
(`replay.py`, `replay.json` 287 KB; report+JSON ≤ 1 MB). Calculus not rewritten:
parent `I_M` from `box/exact-contact-20260906/exact_contact.py` (`tower`,
`all_flat`); child `I'_M` from `child_xu.py` (`child_tower`, `evaluate`); licensed
own data live from `box/lib/descend_own.py` (digest equals the charged copy),
not the roster's single `own_child` representative.

## 1. What was computed

**Parent.** Every flat (pattern, tower-selection) of `all_flat` on all 66 roster
rows (the charged 1,080-configuration table) and on the 46 complete `u_s=1`
rows. `'` is a generation label, not a derivative. Xu's `(f,g)` is the roster's
`(g,f)` as in the charged report §1; `I_M` is symmetric.

**Child.** `descend_own` on each of the 46: license `DETERMINED_PROP6.4`, top
`DETERMINED_COMPLETE_US1`, route `NONEMPTY`, `V` DETERMINED (one vector),
Def 5.1 radii agree with the `(ℓ+1)`-scaled formula, roster `V'` lies in the
own set, 46/46. Each vector is fed to `child_xu` and every evaluable child
pattern is tabulated. Child `I_m` is not computed (charged OPEN 2: no printed
ℓ-shifted Thm 4.7 / Cor 5.3).

**Surviving-integer test** (the OPEN 3 reading: they compared integer `I'_M=8=I_M`
after killing non-integers). Parent surviving = `{I_M : I_M ∈ Z and I_M ≥ I_m}`.
Child surviving = `{I'_M : I'_M ∈ Z}`. All-config rational equality is stronger
and already fails on the charged R009 example (`8` vs `1592/79` against `8` vs
`592/29`), so it is not the test.

Positive controls, exact against the charged report: R009 parent `8`, `1592/79`
and child `8`, `592/29`; R050 parent `8`, `123/11` and child `8`, `8`, `146/13`.
Xu §6.1(i) R002 parent `I_M=8`, `I_m=4`; §6.2(ii) R007 `I_M=10`; §6.2(i) R001
`I_M=4 < I_m=5`.

## 2. The 1,080-configuration table (task 3)

Live `all_flat` on 66 rows reproduces the charged counts exactly:

| | configs | `I_M ∉ Z` | `I_M < I_m` | integrality-alone (`∉ Z` and `≥ I_m`) | surviving (`∈ Z` and `≥ I_m`) |
|---|---|---|---|---|---|
| charged | 1,080 | 995 | 77 | 924 | (implied 79) |
| this replay | 1,080 | 995 | 77 | 924 | 79 |

On the 46 complete rows (620 parent configs): 47 integer, 20 with `I_M < I_m`,
556 killed by integrality alone, 44 surviving configs. Per row: 6 have *no*
integer parent `I_M` (R025–R028, R057, R058 — the charged two-major-tower
rows); R001 has an integer `4` with `4 < 5`; the other 39 have at least one
surviving integer. Full per-config ledger: `replay.json`.

## 3. Partition of the 46 (task 2)

Child `I'_M` is **defined on 46/46** (0 undetermined). 140 child configs.

**`I'_M = I_M` on every surviving integer (32):** R004 R005 R006 R007 R008 R009
R011 R014 R017 R018 R021 R022 R030 R031 R032 R033 R034 R036 R037 R039 R040 R041
R042 R046 R047 R048 R050 R056 R059 R060 R061 R064. Shared values include R009
and R050 at 8, R007 at 10, R014 at `{6,12}`.

**Both defined, neither integer (6):** R025–R028, R057, R058. Rationals move
except R058 (`209/9 = 209/9`). Integrality-failure is shared; the value is not.

**Difference (8), values:**

| row | parent surviving `I_M` | child surviving `I'_M` |
|---|---|---|
| R001 | (none; integer 4 with `I_M=4 < I_m=5`) | `{4}` |
| R002 | `{8}` | `{4, 8, 13}` |
| R003 | `{9}` | `{9, 13}` |
| R010 | `{12}` | `{6, 12}` |
| R013 | `{16, 24}` | `{8, 16, 24, 32}` |
| R019 | `{18}` | `{9, 18}` |
| R020 | `{18}` | `{9, 18}` |
| **R063** | **`{19}`** | **(none; unique child `I'_M = 71/4`)** |

R063 child is `(n',m')=(42,28)`, `s'=3`, `ℓ=1`, `V'=(3,7)`, one pattern
`p_2=π^5(π^{A}-c)^3`, `p_3` selected at `r=7`. Extra child integers on
R002/R003/R010/R013/R019/R020 come from child patterns with no parent
counterpart (ℓ-shifted Prop 4.6 at the child top). Dropping parent Cor 5.3
moves only R001 to `{4}={4}`; R063 and the extras remain.

## 4. FALLACY-v2

*Floor/attainment.* Surviving integers are exact values of the charged
functionals, not a floor. `I_M ≥ I_m` is not `I_M = I(f_ξ,g)`.
*Carrier/attainment.* Rows are `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.
Extra child integers are extra necessary configs, not a realized pair.
*Prime label.* `'` is the child generation.
*Variable/ring map.* Declared in §1; matching names are not a proof.
*Merge-free/M-descent.* Own `V'` from `descend_own`, never copied `V`.
*Child `I_m`.* Typed OPEN (charged OPEN 2); not filled by analogy. Extra
child integers might fail an unprinted child Cor 5.3; **R063 does not use
that gap** (`71/4 ∉ Z` fails the same integrality test).
*Replay is evidence; type counts.* 32 matches are MEASURED, not a proof.

## 5. Verdict

Candidate statement (the OPEN 3 lemma-shape):

> On a complete `u_s=1` necessary tower, the set of integer `I_M` of flat
> parent configurations with `I_M ≥ I_m` equals the set of integer `I'_M` of
> licensed Prop 6.3 child configurations.

**FAILS.** Counterexample R063: parent surviving `{19}`, licensed child
`I'_M = 71/4 ∉ Z`. That is itself a descent-sensitive test: the unique
parent integer is not reproduced after Prop 6.3. Weaker unique-value
preservation fails on the same row. Inclusion “every parent surviving
integer appears as a child integer” fails only on R063.

OPEN 3, as a universal identity, is closed in the negative. The 32 matching
rows remain evidence that equality is frequent, not that it is a theorem.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6251`.
- Body SHA-256:
  `33f48b33880a1f48cab701122c0ad6696847afc8a585211e7352f6977d3fb1c0`.
- Frozen basis: `2794a5417c8f4142e02a29968c3b3fb7e814c4d4`.
