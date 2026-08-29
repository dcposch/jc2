# Hostile review — TD6 V89H11 free-variable-count correction

| Field | Value |
|---|---|
| Target | Frozen V89H11 producer result and first hostile report, restricted to the free-variable-count conflation. Charged pins: first report, live amendment, wording erratum, `P12_FLAG_RESULT.md`, R1 client |
| Overall verdict | **CORRECTED** |
| Smallest failing identity | none. The empty-nonpivot functional is not a false computation. The false object is the dimension label `17` for the nonpivot quotient |
| Smallest bad coefficient / denominator / omission | the phrase "17 nonpivot coordinates" / "17-parameter" as a quotient dimension. Independent count: 132 transport-free section coordinates, 38 frozen FIRST pivots, **94** nonpivots. The number 17 is the number of nonzero *parameter records* in the earlier pure-q14 cokernel class (empty monomial plus 16 singletons), not the number of free jet coordinates |
| Reviewer / model | Grok 4.6 (xAI). Independent corrective hostile review. The first report's `CONFIRMED` is withdrawn as a controlling verdict because it repeats the wrong count. Producer `PASS` banners are custody only |
| Method | SHA-256 of all five charged pins; independent local rebuild of the transported kernel and literal FIRST/P12 through H11's nested V87/H6/H5 parents (wrapper environment, no AWS, no flag solve); Gaussian reconstruction of the frozen 38-pivot list; parse of the frozen V89H6 17-record positive class; source inspection of `empty_parameter_value`. No Singular, Sage, Lean, or `jc2-lean`. The full H11 triangular solve and 2,893-term substitution were not re-executed: they do not depend on the numeral 17 |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Correction-prompt SHA-256 `3e642c7e7e28e3bfd463dbe653ba2d1cd5e55d0b24accb6464b93f5b91b8a754` matched the written charge. Independently recomputed SHA-256 of every required pin matches. No file other than this review was written. The frozen producer package, the first hostile report, campaign ledgers, and `jc2-lean` were not edited.

---

## Verdict

**CORRECTED.**

The first V89H11 hostile report is algebraically right about the empty-nonpivot functional and wrong about the dimension of the nonpivot quotient. Jet parameters in the literal transported kernel are the 132 free section coordinates remaining after 3,470 transport pivots are eliminated from the 3,602-dimensional `(f,g)` chart (`nf=976`, `ng=2,626`). The frozen FIRST block selects 38 distinct pivots from those 132 labels. The complementary count is 94, not 17.

The number 17 is the number of nonzero *parameter records* in the earlier pure-q14 cokernel class: the empty parameter monomial together with 16 singleton monomials, all with q-support exactly `(14,)`. Those 16 singleton labels are 16 of the 94 nonpivots. They are not the quotient.

H11's `empty_parameter_value` never assumes, enumerates, or bounds 17 nonpivots. It builds a dictionary from the complete 38-pivot list and sends every monomial that contains a variable outside that dictionary to zero. The triangular solve is `A(q) p = rhs(q)` with every nonpivot already omitted. The computed object is therefore `P12(p0, 0)` with `0` the origin of all 94 nonpivot coordinates. Replacing the written dimension 17 by 94 does not change `p0`, the 13-term functional, the H7 comparison, or the denominator firewall.

The first report's `CONFIRMED` cannot stand, because Charge 4 of that report states as a mathematical split that the jet is "38 pivots `p` and 17 nonpivots `n`." That statement is false. The theorem it was defending survives as one exact empty-nonpivot P12 quotient functional over all 22 licensed q in the frozen `F=0` scope, with quotient dimension 94.

**CORRECTED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Charged pins | five SHA-256 values | all five match |
| 1. Kernel count | 132 parameters, 38 pivots, 94 nonpivots | independently rebuilt; `3602 - 3470 = 132`; FIRST/P12 labels `== set(range(132))` before and after `F=0`; 38-pivot list matches the frozen H6 printout; complement has 94 labels |
| 1. The 17 | empty + 16 singletons in the pure-q14 class | 17 rows in `Q14_MOD_F_POSITIVE_COKERNEL_CLASS.tsv`; all q-monomial `(14,)`; 16 singleton labels are a proper subset of the 94 nonpivots; 78 nonpivots are absent from that class |
| 2. Wrong statements | producer result and first report | first report Charge 4 and the verdict paragraph treat 17 as `dim(n)`. The client/result-artifact slogan `full_17_parameter_normal_form_computed=false` uses the same wrong numeral. `P12_FLAG_RESULT.md` itself does not write the numeral 17 as a count |
| 3. `empty_parameter_value` | every non-pivot variable, not 17 | membership in the complete 38-pivot dictionary; `position is None` zeros the term; no occurrence of 17 in that function |
| 4. Theorem survival | empty-nonpivot functional after `17 → 94` | survives unchanged. Unique `p0` is the solution of `A p = rhs` at all nonpivots zero. That origin is independent of a false label for `dim(n)` |
| 5. Controlling verdict | `CORRECTED` / `FALSIFIED` / `CONFIRMED` | **CORRECTED**. Not `FALSIFIED`: the computation does not rely on 17. Not `CONFIRMED`: the first report's 17-nonpivot split is a false statement |

---

## 0. Charged pins

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| first hostile report | `0d38db4f56b710cbd9ce438cfb096b589115275da47d04dc802e80d164fa7345` | `CONFIRMED` report that repeats "17 nonpivot coordinates" |
| live amendment | `908de28bff116799c100b54613f9cf906b32c130fbb588f1115bb3caff4f818f` | charges the 94-versus-17 distinction |
| `P12_FLAG_FREE_COUNT_ERRATUM.md` | `c6bc9942ec60b90433f6044d299cce6e2f4e49ffd237d3680d118b73c39babd2` | producer wording erratum |
| `P12_FLAG_RESULT.md` | `1e418dfeaf600def4cbfaae885b860b5303faa90a2fdaea59fc4003a137fa2a2` | frozen producer result |
| R1 client | `8b87985d2071c40b295e280fce94a6465826dd06478089adca34e70df123fcba` | H11 replay; contains `full_17_parameter_normal_form_computed=false` |

The original H11 review prompt SHA `e7b13084ae539bbf13cef69424afe67ba3854b815e08f986a78199a0d5271006` is the parent charge named in the amendment; it is not re-opened here except for the free-count repair.

Nested compiler pins reached from the charged H11 client, independently rehashed and matching the first report:

| Pin | SHA-256 |
|---|---|
| H6 parent client in the H11 case | `1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757` |
| H5 parent client | `a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b` |
| V87 parent client | `7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463` |

---

## 1. Charge 1 — 132 parameters, 38 pivots, 94 nonpivots, versus 17 records

The 132-count is not an assert copied from a later sibling. It is the number of transport-free section coordinates in H11's own V87 parent.

Independent local execution, with the frozen R1 wrapper environment

```text
TD6_Q_EXPONENT=2
TD6_PIVOT_POLICY=ascending
TD6_PIVOT_SCOPE=all-staged
TD6_Q_SCOPE=q2-q14-q16-q24
TD6_F_SPECIALIZATION=exact-C-equals-V2-minus-U3-over-U
TD6_FUNCTIONAL_SCOPE=empty-parameter-allq
```

and without calling H11 `main`, rebuilt the two transports and factored them:

```text
nf = 976
ng = 2626
nf + ng = 3602
n_transport_pivots = 3470   (all distinct)
events = 2
n_free_section = 3602 - 3470 = 132
```

The free labels are disjoint from the 3,470 transport pivots and together exhaust `{0,...,3601}`. V87 then remaps those 132 free section coordinates onto parameter labels `{0,1,...,131}` (`replay_v87tfaq_total_f_allq.py` lines 340–342). That is the ambient jet of FIRST and P12.

The same process via `v87.build_bands` / `compile_first` / `compile_current_degree12` produced 38 FIRST rows and 2,893 P12 terms. Every parameter monomial label appearing in raw FIRST, in raw P12, in `F=0`-specialized FIRST, and in specialized P12 is exactly `set(range(132))`. No extra labels, no missing labels, and specialization does not drop a coordinate.

`h5.base_pivot_columns(specialized_first)` returned 38 distinct pivots, in this order:

```text
0, 2, 1, 3, 4, 5, 7, 10, 14, 19, 23, 26, 28, 29, 30, 31, 32, 33, 34, 35,
39, 42, 46, 52, 57, 63, 71, 78, 86, 95, 103, 110, 116, 121, 125, 128, 130, 131
```

This is byte-for-byte the pivot list printed by the frozen V89H6 exact result (`pivots=[...]` in `Q14_MOD_F_COKERNEL_EXACT_RESULT.txt`). The selection uses only `coefficient.constant()`, so it is independent of which positive-q coordinates are retained. All 38 labels lie in `{0,...,131}`. The complement inside that set is 94 labels:

```text
6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27,
36, 37, 38, 40, 41, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 56,
58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77,
79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 94,
96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109,
111, 112, 113, 114, 115, 117, 118, 119, 120, 122, 123, 124,
126, 127, 129
```

Specialized FIRST row keys minus the pivot set also have cardinality 94: every nonpivot actually appears in the affine FIRST block.

The 17 is a different object. The frozen V89H6 positive cokernel class (digest `56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2`, 17 data rows, `positive_records=17`) consists of the parameter monomials

```text
(), (6,), (8,), (9,), (11,), (12,), (13,), (15,), (16,),
(17,), (18,), (20,), (21,), (22,), (24,), (25,), (27,)
```

each with q-monomial exactly `(14,)`. That is one empty parameter record plus 16 singleton records. H6 `RESULT.md` already called these "17 parameter records", which is correct language for a remainder TSV and is not a count of free jet coordinates. The 16 singleton labels are a proper subset of the 94 nonpivots listed above. The other 78 nonpivots do not appear in that class. Conflating "17 nonzero records of one specialized remainder" with "17 nonpivot coordinates of the FIRST affine space" is the error.

`v85.restore_base_qd_state()` was called at exit of the count process. The producer package was not modified.

---

## 2. Charge 2 — every materially wrong statement

Materially wrong means a statement that treats 17 as the dimension of the nonpivot quotient, or as the number of free jet parameters of the unique original-FIRST normal form. SHA prefixes that happen to contain the digits `17`, the H7 numerator term `710528/15 U^{17}`, and ordinary line numbers are not charged.

### First hostile report
(`xmodel/td6-v89h11-allq-p12-flag-functional-hostile-review-report-20260826.md`, SHA `0d38db4f…`)

| Location | Statement | Why it is wrong |
|---|---|---|
| Verdict, line 25 | "There is no q-dependent change of the 17 nonpivot coordinates" | There are 94 nonpivot coordinates. The surrounding sentence about a constant flag on the 38 *pivot* indices is true, and is not rescued by writing the wrong count |
| Charge 4, line 206 | "Jet parameters split as 38 pivots `p` and 17 nonpivots `n`" | The split is 38 + 94 inside 132. This is the load-bearing false sentence: it sets `dim(n)=17` as the ambient ring of the unique normal form |
| Charge 4, line 228 | "if the 17 nonpivot coordinates were replaced by a q-dependent linear combination" and "The 17 nonpivot variables are never renamed" | Same false dimension. The geometric claim (the flag does not mix nonpivots) is true for the actual 94 |
| Charge 4, line 232 | "not the remaining 17-parameter polynomial `P12(f(n), n) - P12(p0, 0)`" | The uncomputed remainder is a 94-parameter polynomial. The boolean "H11 did not compute the full NF" is true |
| Charge 10, line 344 | quoted slogan `full_17_parameter_normal_form_computed=false` | Accurate quotation of a wrong numeral in the frozen result artifact |
| Charge 10, line 351 | "the full normal form in the 17 free jet parameters" | Paraphrase that turns the artifact slogan into a dimension of the jet. The firewall paragraph of `P12_FLAG_RESULT.md` that Charge 10 also cites does *not* write 17 |

The first report's overall verdict **CONFIRMED** (header, lines 21 and 44) is therefore not a valid controlling verdict for promotion. Charges 1–3 and 5–9 of that report, and the unimodularity / `A p = rhs` / digest / denominator facts, are not re-opened: they do not use the numeral 17 as an algebraic input.

### Frozen producer result
(`P12_FLAG_RESULT.md`, SHA `1e418dfe…`)

The 67-line producer result does **not** contain the numeral 17 as a free-count. Its closing firewall (lines 63–67) says only "the full normal form in the remaining free jet parameters." That sentence is unnumbered and is not false. The erratum's attribution of the exact phrase `"full 17-parameter normal form"` to this file's closing paragraph is slightly off: that numbered phrase is not in `P12_FLAG_RESULT.md`.

The numbered slogan lives in the frozen result artifact that `P12_FLAG_RESULT.md` cites by SHA, and in the charged client that emitted it:

| Location | Statement |
|---|---|
| R1 client line 427 | `full_17_parameter_normal_form_computed=false` |
| `ALLQ_P12_FLAG_FUNCTIONAL_RESULT.txt` line 17 (digest `591d6ac5…`, cited at `P12_FLAG_RESULT.md` line 61) | the same slogan |

The boolean `false` is correct: H11 did not compute a full normal form. The qualifier `17-parameter` is the wrong dimension. Provenance, not independently charged here, is `PREREGISTRATION_P12_FLAG.md` line 39 ("It does not compute the full 17-parameter normal form"), which the first report quotes at Charge 10.

No other sentence of `P12_FLAG_RESULT.md` asserts a 17-dimensional quotient. The 38 FIRST rows, 22 q coordinates, 13-term support, digests, and denominator maxima in that file are outside this correction.

---

## 3. Charge 3 — `empty_parameter_value` does not assume 17 nonpivots

The implementation is `replay_v89h11_allq_p12_flag_functional.py` lines 245–266. The complete function, with no omitted branch, is:

```text
def empty_parameter_value(polynomial, pivots, pivot_values):
    pivot_position = {variable: index for index, variable in enumerate(pivots)}
    out = QPoly()
    retained = 0
    for count, (monomial, coefficient) in enumerate(sorted(polynomial.items()), 1):
        value = QPoly.coerce(coefficient)
        for variable in monomial:
            position = pivot_position.get(variable)
            if position is None:
                value = QPoly()
                break
            value *= pivot_values[position]
        if value:
            out += value
            retained += 1
        ...
    return out, retained
```

Facts about this function, all read from the charged client:

1. `17` does not occur in its source.
2. `pivots` is `h5.base_pivot_columns(specialized_first)`, asserted at lines 299–300 to be 38 distinct variables. The dictionary is therefore the complete frozen 38-pivot list, not a 17-element subset.
3. For a P12 monomial `m`, every factor is looked up with `.get`. If any factor is absent from that dictionary, the whole monomial is replaced by `QPoly()` (zero) and the inner loop breaks. That is substitution of *that* nonpivot by zero, and it applies to every variable outside the 38-pivot set.
4. If every factor is a pivot, the monomial is evaluated at the corresponding entries of `pivot_values`. The empty monomial `()` keeps its coefficient. The output is therefore `P12(p0, 0)` with `0` the origin of the complement of the 38-pivot set.
5. Nonpivots are never enumerated, listed, or counted. There is no `range(17)`, no 17-element complement, and no special case for the 16 singleton labels of the q14 class.

The triangular solve that produces `p0` is likewise independent of `dim(n)`: it is `A(q) p = rhs(q)` in original 38-by-38 pivot coordinates (lines 331–335), i.e. the FIRST system with every nonpivot already omitted. A hypothetical implementation that zeroed only the 16 q14-class singletons and left the other 78 nonpivots free would not have a unique `p0`. H11 does not do that. The unique 38-vector it emits is possible only because *all* 94 nonpivots are set to zero.

---

## 4. Charge 4 — the theorem survives with dimension 94

Write `R` for the same coefficient ring the first report used: `E3_D[q_2,...,q_14,q_16,...,q_24]` localized at `D(U*H*B3)` after `F=0`. Jet parameters are 132 coordinates, split as 38 pivots `p` and **94** nonpivots `n`.

The 38 FIRST rows remain affine-linear in those 132 coordinates (V87 `source_polynomial` emits only `()` and linear `(variable,)`; H11 line 289 asserts `len(monomial) <= 1`). Unimodularity of the 38-by-38 pivot block `A(q)` over `R` is the V89H10T flag theorem: after a constant change of pivot basis and a constant permutation, `N = A(0)^{-1}A(q) - I` is strictly upper triangular, so `I+N` is unipotent and `A^{-1}` lies in `M_{38}(R)`. None of that uses `dim(n)`.

Unimodular row operations over `R` still produce a Groebner basis `p_j - f_j(n)` of the original FIRST ideal in `R[p,n]`, now with `n` of length 94. The unique original-FIRST normal form of a polynomial is its remainder in `R[n]`. The empty-nonpivot coefficient of that remainder is the constant term of `P12(f(n), n)` as a polynomial in 94 nonpivot variables, which equals `P12(f(0), 0)` for any polynomial. And `f(0)` is the unique solution of `A p = rhs`. That identification does not depend on writing 17 or 94 for `len(n)`, provided `n` is the actual complement of the 38-pivot set and is not mixed by a q-dependent coordinate change.

The first report's *reason* that the identification does not fail is still correct, once 17 is replaced by 94: `S` and the permutation act on the 38-dimensional pivot index space; nonpivots are never renamed; `W` maps back to original pivot coordinates before substitution. What was false was only the name `17` for those nonpivots.

Therefore:

- The computed 13-term functional (digest `530d3c78…`), the 37-nonzero pivot solution (digest `ea9537be…`), the pure-q14 H7 comparison, and the denominator maxima `U^7 V^4 (V^2-4U^3)^2` / `U^5 V^4 (V^2-4U^3)^2` are the empty-nonpivot data of a 94-dimensional quotient, not of a 17-dimensional one.
- Those artifacts do not become false when the dimension label is repaired.
- A full 94-variable normal form is still uncomputed. Repairing the count does not promote H11 to H12's job.

If the client had enumerated 17 nonpivots and solved or reduced only in those directions, the claim would be `FALSIFIED`. It does not. The numeral 17 is a slogan in a firewall banner, not an input of the solve.

---

## 5. Charge 5 — controlling verdict, smallest theorem, scope firewall

**CORRECTED.**

`CONFIRMED` is unavailable: Charge 4 of the first report, and the client/artifact slogan `full_17_parameter_normal_form_computed=false`, are wrong as dimension statements. The amendment forbids `CONFIRMED` in that situation.

`FALSIFIED` is unavailable: the empty-nonpivot computation and the quotient identification `P12(p0, 0)` = empty coefficient of the unique original-FIRST normal form do not rely on the numeral 17. They rely on the complete 38-pivot dictionary and on unimodularity of `A(q)`, both of which hold.

`CORRECTED` is the remaining verdict: the theorem survives with a wording/count repair `17 → 94`.

### Smallest valid theorem

On the frozen V89H10T `F=0` specialization, over the registered open `D(U*H*B3)`, with all 22 independent untruncated coordinates

```text
q2,...,q14,q16,...,q24
```

and with q15 absent only as the reviewed target shear of frozen `(p,q)=(t^{15}, t+···+t^{25})`:

the 38 original packed FIRST rows are affine-linear in the 132 transport-free section coordinates. Their 38-by-38 pivot block, on the frozen pivot list

```text
0, 2, 1, 3, 4, 5, 7, 10, 14, 19, 23, 26, 28, 29, 30, 31, 32, 33, 34, 35,
39, 42, 46, 52, 57, 63, 71, 78, 86, 95, 103, 110, 116, 121, 125, 128, 130, 131
```

is unimodular over the localized q-polynomial ring. Setting every one of the complementary **94** nonpivot coordinates to zero and solving by strict-upper back-substitution in the frozen flag basis yields a unique original-coordinate pivot value `p0`. Substituting that `p0` into literal P12 (2,893 parameter terms) equals the empty-nonpivot coefficient of the unique original-FIRST normal form. That coefficient is the frozen 13-term functional with digest

```text
530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8
```

support exactly `(), q3, q4, ..., q14`, total q-degree one, no mixed-q terms, and with pure-q14 E3-coordinate-0 value equal to the promoted V89H7 functional, nonzero. Output denominators remain inside the registered radical of `U*H*B3` after `F=0`, with the same maxima as in `P12_FLAG_RESULT.md`.

### Scope firewall

This is one empty-nonpivot quotient functional only.

It does not compute the full 94-variable original-FIRST normal form of P12. It does not prove a unit ideal or a source-point exclusion. It does not cover a unit-q chart. It does not license q15 as a source coordinate. It does not supply a total-Rees map. It does not close TD6. It does not resolve JC2. Sibling files in the same case directory that are not named in `P12_FLAG_FREEZE.sha256` remain outside this frozen theorem, including any later full-normal-form gate.

The first report's `CONFIRMED` is not a promotion licence. The producer erratum withdraws only the numerical wording; this review is the independent adjudication the amendment required before any promotion.

---

## Custody

The independent count wrote no case-directory file. It used the charged R1 client and nested parents in place, with `v85.restore_base_qd_state()` at exit. The producer package, the first hostile report, campaign ledgers, and `jc2-lean` were not modified. This file is the only write.
