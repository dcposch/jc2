# Hostile different-model review — Moskowicz prime-degree source audit

| Field | Value |
|---|---|
| Claim under review | Frozen source audit of Vered Moskowicz, arXiv:2407.13795v1: the printed first-case inference `rare property ⇒ [L:R]=2` is not what MathOverflow answer 473055 proves and is false in every degree `n≥2`; the first-case theorem and the headline no-prime theorem are therefore not established as written; the second case is repairable by choosing `μ≠0` and invoking Wang plus injectivity-on-one-line; the paper cannot exclude prime degree 109 |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions below: `P=2` of the first case is already the paper's own Corollary 2.13; the successor `xy∈K(P,Q)` uses the repaired complex theorem after coefficient embedding) |
| Evidence tier | official arXiv v1 TeX (hash below) and HTML; MathOverflow question 472877 with Laurent Moret-Bailly answer 473055 and the full comment thread; Wang, *J. Algebra* 65 (1980), Theorem 41(i); Gwoździewicz, arXiv:alg-geom/9305008, Theorem 1.1; independent Kummer/UFD argument over `C(s,v)` for every `n≥2`; unmodified rerun of `cases/moskowicz_prime_degree_audit_20260824/check.py` as cubic regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:28:00Z – 2026-08-24T11:50:00Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, `math.comb`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/moskowicz-prime-degree-source-audit-20260824.md` (SHA-256 `929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210`, matches the launch prompt and `FREEZE.sha256`)
- `cases/moskowicz_prime_degree_audit_20260824/check.py` (SHA-256 `1a6174fcd8fc1648e283df316c22206ccad6d9bb103224d3704f4d6c4c9408fb`)
- `cases/moskowicz_prime_degree_audit_20260824/FREEZE.sha256` (SHA-256 `272e85c4364e33990d7dd66445ad193686263088cc371c49aec9850330eb2f3f`)

Primary sources retrieved independently of the producer:

- Official compressed TeX of arXiv:2407.13795v1 from `https://arxiv.org/src/2407.13795v1` (gzip of `prim.tex`; SHA-256 `a41bf70500b9c95c774221b0c7261d50e6bd8465b8f375e334adbbfc75adbf42`, matches the launch prompt). Line numbers below are this TeX file.
- Paper abstract/HTML: `https://arxiv.org/abs/2407.13795`, `https://arxiv.org/html/2407.13795v1`.
- MathOverflow question 472877 and accepted answer 473055, including every comment on both posts, via the page and the Stack Exchange API (`filter=withbody`).
- Gwoździewicz, *Injectivity on one line*, arXiv:alg-geom/9305008v1, Theorem 1.1, read in full from `https://ar5iv.labs.arxiv.org/html/alg-geom/9305008`.

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No AWS call was made.

Write `L=k(x,y)`, `R=k(p,q)`, and `k=C` as in the paper. A Keller map is a polynomial map `f=(p,q)` with `Jac(p,q)∈k*`. The paper's headline is: there is no Keller map with `[L:R]` prime. The proof splits on `xy∉R` (Theorem 3.2, First Case) and `xy∈R` (Theorem 3.3, Second Case).

Tried hard, and failed, to rescue the printed first case, to break the all-degree countercontrol, and to break the proposed `μ≠0` second-case repair. The LMB comment “yes” is a comment, not a proof, and is false as a universal implication. Degree two of the first case is already the paper's Corollary 2.13 and does not save odd primes. The countercontrol is not a Keller subfield.

---

## Promotion

**Accept `REFUTED-AS-PROOF / FIRST CASE UNSUPPORTED / HEADLINE NOT ESTABLISHED / SECOND CASE REPAIRABLE` at the stated scope.**

- Mark avenue 44 `REFUTED-AS-PROOF`, not merely unvetted. Do not feed arXiv:2407.13795 into the AS109 degree cross, `A_infinity`, deck-descent, or sheet-degree ledgers as a prime-degree exclusion.
- Keep the repaired second case as a known-result gate, scoped exactly as: a complex plane Keller map with `xy∈C(p,q)` is an automorphism, assuming Wang's intersection theorem and Gwoździewicz injectivity-on-one-line. The repaired argument does not use prime degree.
- A bounded new AS109 client `AS109-XY-MEMBERSHIP` is a valid independent successor, not a theorem of this freeze: an exact reason that a hypothetical `A_infinity=0` lift (or a lift carrying a descended deck symmetry) satisfies `xy∈K(P,Q)` would close that lift, after coefficient embedding into `C`. A finite-degree ansatz for `H(P,Q)=xy` is not exhaustive unless an independent degree bound for `H` is proved.

**Do not promote this to:** a constructed prime-degree Keller counterexample; a disproof of the first-case *statement* (as opposed to its printed proof); a disproof of the headline *statement*; an automatic kill of AS109; TDU at `td=109`; or any JC2 decision.

---

## Quarantine

No result here proves or disproves JC2. The cubic sweep `nontrivial_galois_images_checked = 1248` was not used as evidence for the all-exponent statement; that statement is the UFD argument in §2 below. Moskowicz's unpublished claim is not a prime-sheet theorem. Formanek's `k(p,q,x)=k(x,y)`, Jedrzejewicz–Zieliński root-closedness, and Bass–Connell–Wright Galois-Keller are used only as the paper uses them, and only where a numbered claim depends on them. The classical Galois case remains the known theorem already on the ledger: a Keller map whose function-field extension is Galois is an automorphism. It kills degree two by itself (paper Corollary 2.13) and is not a replacement for the missing odd-prime argument.

---

## Scope (not enlarged)

One paper, arXiv:2407.13795v1, two case proofs, and the precise use of MathOverflow answer 473055. Characteristic zero, `k=C`, plane Keller maps. The countercontrol is a field-theoretic family, not a Keller map. The repaired second case is a complex plane statement. No construction of a prime-degree Keller map, no AWS, and no JC2 inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | The load-bearing first-case step is TeX 411–413: rare property, then Answer 2.21 (TeX 368–370) supplies `[L:R]=2`, then Corollary 2.13. Moret-Bailly 473055 constructs a quadratic example `L=R(√u)` with coordinates `x=s+v`, `y=s+2v`. It does not prove that the rare property forces degree two. The universal reading is the questioner's later edit and the paper's Answer 2.21, not the answer | **CONFIRMED** | a proof, in 473055 or in the paper between the rare-property calculation and TeX 412, that every `R=k(u,v)⊂k(x,y)` with the rare property has `[L:R]=2`; LMB's comment “yes” counting as such a proof |
| 2 | For every integer `n≥2`, `L=C(s,v)`, `R=C(s^n,v)`, `x=s+v`, `y=s+2v` is a cyclic Galois extension of degree `n` generated by algebraically independent polynomials, and every nonconstant monomial is primitive. Unique factorization in `C[s,v]` matches the slope multisets `{1,2}` against `{ζ^{-1},2ζ^{-1}}`; equal multiplicities still cannot swap because that forces `ζ=2` and `ζ=1/2` at once. The rare property therefore imposes no degree-two restriction. The `n=2` member is LMB's example. The cubic sweep is regression only | **CONFIRMED** | `(2x-y)^n` and `y-x` algebraically dependent; `[C(s,v):C(s^n,v)]≠n`; a root of unity `ζ≠1` with `{1^{(i)},2^{(j)}}={ζ^{-1(i)},2ζ^{-1(j)}}` as multisets; the UFD argument restricted to `i≠j` with `i=j` left open |
| 3 | The countercontrol refutes the printed first-case *proof step* and leaves the first-case theorem and the headline no-prime theorem not established as written. It is not a Keller subfield, so it does not disprove the headline *statement* and does not produce a prime-degree Keller counterexample. Prime degree 109 is not excluded by this paper | **CONFIRMED** | a replacement Keller-specific argument in the paper from rare property to automorphism; the countercontrol having constant Jacobian; a constructed Keller map of prime degree; the audit treating the unsupported theorem as a counterexample |
| 4 | Second-case TeX 633 is a missing units sentence, valid in `C[x]`. TeX 693–696 is invalid as written: Step 1's contradiction uses common zeros of `(p,q)`, not of `(p-c,q)`. Choosing `μ≠0` outside the finite forbidden set gives `μx=H(p_μ,q_μ)`, hence `C[p_μ,q_μ]=C[x]`, without either step. Wang 41(i) and Gwoździewicz 1.1 apply. The repair does not use prime degree | **CONFIRMED** | a common-zero avoidance for `(p-c,q)` already in the paper's choice of `μ`; `μ=0` still forcing the embedding; Wang 41(i) not supplying `xy=H(p,q)`; Gwoździewicz requiring something the embedding does not give |
| 5 | arXiv:2407.13795 cannot exclude prime degree 109. Membership `xy∈K(P,Q)` is a valid independent successor gate via the repaired second case (after coefficient embedding into `C`). A finite-degree ansatz for `H` is not exhaustive without a bound | **CONFIRMED** | a surviving first-case argument for odd primes; the repaired second case using prime degree after all; a degree bound for `H` proved in the freeze; the audit calling a bounded search exhaustive |
| 6 | Registered regression reruns `PASS` with the four advertised Booleans. Frozen hashes and the official TeX hash match the launch prompt. Scope strings are exact | **CONFIRMED** | hash mismatch; `check.py` failing; the cubic sweep presented as the all-exponent proof; a scope string claiming a Keller counterexample or a JC2 inference |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree, match the launch prompt and `FREEZE.sha256`:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/moskowicz-prime-degree-source-audit-20260824.md` | `929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210` | prompt and `FREEZE.sha256` |
| `cases/moskowicz_prime_degree_audit_20260824/check.py` | `1a6174fcd8fc1648e283df316c22206ccad6d9bb103224d3704f4d6c4c9408fb` | prompt and `FREEZE.sha256` |
| `cases/moskowicz_prime_degree_audit_20260824/FREEZE.sha256` | `272e85c4364e33990d7dd66445ad193686263088cc371c49aec9850330eb2f3f` | self-hash of the freeze listing |
| official compressed TeX of arXiv:2407.13795v1 | `a41bf70500b9c95c774221b0c7261d50e6bd8465b8f375e334adbbfc75adbf42` | prompt; gzip of `prim.tex` |

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/moskowicz_prime_degree_audit_20260824/check.py
```

Exit code 0. Exact advertised headline:

```text
MOSKOWICZ-PRIME-DEGREE-AUDIT: PASS
rare_degree_three_control = C(s^3,v) subset C(s,v)
coordinates = x=s+v; y=s+2v
nontrivial_galois_images_checked = 1248
universal_all_exponent_argument = UFD factor matching in report
paper_first_case_supported = false
paper_second_case_repairable = true
no_prime_degree_theorem_usable = false
jc2_inference = false
```

Stdout SHA-256 `c681df8bfc7f6eba82165572cfba90a97cd5faccf390c0f03984749e54049389`. The 1248 is `(25^2-1)×2`: every `(i,j)≠(0,0)` with `0≤i,j≤24`, both nontrivial cube-root automorphisms. That finite sweep was discarded as evidence for the all-exponent claim. The all-exponent statement is the UFD argument in §2, which does not pass through `check.py`.

A second engine, written for this review and not imported from the registered script, used only `fractions.Fraction` and `math.comb`. It recorded: linear inversion `s=2x-y`, `v=y-x`; Jacobian `n(2x-y)^{n-1}` of the polynomial generators for `n=2..8`; Kummer degree `n`; swap obstruction `λ^2=1` for slope pairs `{1,λ}` with `λ∉{0,1,-1}`; and the exact two-branch factor matching of §2, including equal multiplicities and one-sided exponents. Zero failures.

---

## Independent recomputation

### 1. Load-bearing inference versus the MathOverflow answer — CONFIRMED

Paper TeX 368–371, labelled Answer 2.21:

```text
Without considering the additional condition k(u,v,x+y)=k(x,y),
it was proved in the answer that: [k(x,y):R]=[k(x,y):k(u,v)]=2.
```

Paper TeX 411–413, the only bridge from the rare-property calculation to invertibility in Theorem 3.2:

```text
Having this it is immediate that f is an automorphism; indeed,
Answer 2.21 implies that [k(x,y):k(p,q)]=2, so by Corollary 2.13,
f is an automorphism.
```

Corollary 2.13 is the standard fact that a degree-two extension is Galois, plus Bass–Connell–Wright Theorem 2.1 (paper Theorem 2.12): a Galois Keller extension is an automorphism. That corollary is not under attack. The load-bearing step is the implication `rare property ⇒ [L:R]=2`.

Laurent Moret-Bailly, MathOverflow answer 473055 (accepted; edited 2024-06-12), in full mathematical content:

> Start with `R=C(u,v)` and consider its quadratic extension `L=R(√u)=R(s)=C(s,v)` with `s^2=u`.
>
> Take an element `z` of `L` … `R(z)=L` iff `z∉R` (because `[L:R]=2`) iff `σ(z)≠z` where `σ` sends `z(s,v)` to `z(-s,v)`.
>
> We can also view `L` as `C(x,y)` in many different ways; let us pick `x=s+v`, `y=s+2v`. For `(i,j)≠(0,0)`, `x^i y^j=(s+v)^i(s+2v)^j` and `σ(x^i y^j)=(-s+v)^i(-s+2v)^j` are always different, so `R(x^i y^j)=L`.

This starts with a chosen quadratic extension and then *chooses coordinates* so that every nonconstant monomial is primitive. It answers the question “must `R=C(x,y)`?” with no, by exhibiting a degree-two example. It does not take an arbitrary subfield `R⊂C(x,y)` satisfying the rare property and prove `[C(x,y):R]=2`.

The questioner's first comment (2024-06-12) asked whether LMB had proved the universal implication. LMB replied “First comment: yes, but I would not be surprised if your ‘rare’ property were not rare at all.” That comment is the strongest rescue of the paper, and it fails:

- It is a comment, not the answer, and it contains no proof.
- LMB's later comments are construction language: “`(x,y)` as defined is algebraically free and generates `L` over `C`, whence an isomorphism `C(x,y)≅L`.”
- The questioner still did not read it as a general theorem. Comment 1232103: “I do not understand why the choice `x=s+v`, `y=s+2v` is possible; it implies that `v=y-x`, which may not hold. So even if this was just an example, how we guarantee that there is a valid choice?”
- The universal sentence “If `C_{R,i,j}` holds for every `(i,j)≠(0,0)`, then `[C(x,y):R]=2`” appears in the *questioner's* July 11 2024 edit of the question, not in answer 473055. The paper was submitted five days later (2024-07-16) and copied that sentence into Answer 2.21.

Tried to rescue by reading LMB's method as a general coordinate change on an arbitrary rare-property extension. There is no such change in the answer: `s` is defined as a square root of a chosen generator of a quadratic extension built first. The `n≥3` family of §2 is the same construction with `s^n` in place of `s^2`, and it is a counterexample to the universal implication. A comment cannot override that.

Precision, non-blocking: for a *prime-degree* extension the rare property is equivalent to “no nonconstant monomial lies in `R`”, because every element outside `R` is primitive. The first-case calculation may well establish that weaker statement for a hypothetical prime-degree Keller map with `xy∉R`. That is not a degree-two theorem.

### 2. All-degree countercontrol — CONFIRMED

Fix an integer `n≥2`. Set `L=C(s,v)`, `R=C(s^n,v)`, `x=s+v`, `y=s+2v`. The linear change is invertible over `C`:

```text
s = 2x - y,     v = y - x,
R = C((2x-y)^n, y-x) ⊂ C(x,y).
```

Both generators are in `C[x,y]`. The Jacobian of `(s,v)` with respect to `(x,y)` is `det|(2,-1),(-1,1)|=1`. The Jacobian of `(s^n,v)` with respect to `(s,v)` is `n s^{n-1}`. Hence

```text
Jac_{(x,y)}((2x-y)^n, y-x) = n(2x-y)^{n-1} ≠ 0
```

as a polynomial in characteristic zero, so the generators are algebraically independent. The extension `C(s,v)/C(s^n,v)` is the standard Kummer extension of degree `n` (minimal polynomial `T^n-s^n` over `C(s^n,v)`; `C` contains the `n`-th roots of unity). It is cyclic Galois, generated by `σ_ζ: s↦ζs`, `v↦v` for `ζ^n=1`.

Let `(i,j)≠(0,0)` and suppose `σ_ζ` fixes the monomial `x^i y^j`. Then, as elements of `C[s,v]`,

```text
(s+v)^i (s+2v)^j  =  (ζs+v)^i (ζs+2v)^j
                  =  ζ^{i+j} (s + ζ^{-1} v)^i (s + 2ζ^{-1} v)^j.
```

`C[s,v]` is a UFD. Linear forms `s+av` and `s+bv` are associate if and only if `a=b`, after normalising the coefficient of `s` to `1`. Unique factorization therefore identifies the irreducible-factor multisets

```text
{ 1 (multiplicity i),  2 (multiplicity j) }
{ ζ^{-1} (multiplicity i),  2ζ^{-1} (multiplicity j) }.
```

Three exhaustive patterns:

- One-sided, `i=0` and `j≠0`: `{2}={2ζ^{-1}}`, so `ζ=1`.
- One-sided, `j=0` and `i≠0`: `{1}={ζ^{-1}}`, so `ζ=1`.
- Both nonzero. Same-order pairing: `1=ζ^{-1}` and `2=2ζ^{-1}`, so `ζ=1`. Cross pairing, which can occur only when `i=j`: `1=2ζ^{-1}` and `2=ζ^{-1}`, hence `ζ=2` and `ζ=1/2` simultaneously, impossible in `C`.

No other pairing exists: the two left-hand forms `s+v` and `s+2v` are non-associate, and the two right-hand forms are non-associate because `ζ^{-1}=2ζ^{-1}` would give `1=2`. Therefore the stabilizer is trivial, the orbit has size `n`, and `R(x^i y^j)=L` for every nonconstant monomial. The same argument with `x+y=2s+3v` shows that optional extra generator is likewise primitive.

The slope pair `{1,2}` is essential. For a pair `{1,λ}` the cross pairing is `λ^2=1`. The excluded values are `λ∈{0,1,-1}`: `λ=0` collapses a coordinate, `λ=1` makes `x=y`, and `λ=-1` is the exchange involution `C(xy,x+y)`, whose diagonal monomials *are* fixed (the questioner's own non-example). LMB's choice `λ=2` is the `n=2` member of this family.

The control is not Keller: the Jacobian `n(2x-y)^{n-1}` is nonconstant for `n≥2`. That is required for claim 3, not a defect of claim 2.

Tried to break the UFD argument at equal multiplicities, at one-sided exponents, and at roots of unity other than `-1`. The three-branch analysis is exact and does not pass through a degree bound on `(i,j)` or through the cubic cyclotomic ring of `check.py`. Taking `n=3` already contradicts the implication used at TeX 370 and 412.

### 3. Logical consequence — CONFIRMED

The printed first-case proof, after whatever it may establish about the rare property, invokes a false field lemma and stops. No Keller-specific replacement appears between the rare-property calculation and TeX 412. So:

```text
printed first-case proof step     REFUTED
Theorem 3.2 “First Case”          NOT ESTABLISHED AS WRITTEN
headline no-prime theorem         NOT ESTABLISHED AS WRITTEN
prime degree 109                  NOT EXCLUDED BY THIS PAPER
```

The countercontrol is not a Keller map, so it does not exhibit a prime-degree Keller extension and does not disprove the headline *statement*. An unsupported theorem is not a constructed counterexample. The producer states this distinction explicitly; it survives a hostile reading.

Precision, non-blocking, from trying to rescue the first-case *theorem*: if `[L:R]=2`, Corollary 2.13 already makes `f` an automorphism, with no rare property and no MathOverflow citation. So the first-case statement is true for `P=2` by the paper's own Galois corollary, independently of `xy`-membership. That does not establish Theorem 3.2 as written (the printed proof is the rare-property path), and it does not touch odd primes. The headline still fails, because it claims every prime.

No argument was found that Keller structure plus “no nonconstant monomial in `R`” forces Galois of odd prime degree. Galois-Keller would finish the job if Galois were known; that is an equivalent of the plane Jacobian conjecture, not a lemma of this paper.

### 4. Second case, printed gaps, and the `μ≠0` repair — CONFIRMED

Assume `xy∈R`. Wang, *J. Algebra* 65 (1980), Theorem 41(i), stated as paper Theorem 2.5:

```text
k(p,q) ∩ k[x,y] = k[p,q].
```

The hypotheses match a plane Keller map over a characteristic-zero field: `Jac(p,q)∈k*`. Thus `xy∈k[p,q]`, so `xy=H(p,q)` for some `H∈k[T_1,T_2]`. That first paragraph of Theorem 3.3 is correct.

Proposition 2.19: `p` and `q` have finitely many common zeros, because a common nonconstant factor would divide the Jacobian. Correct. The `y`-coordinates of those zeros are a finite forbidden set. The paper chooses `μ` off that set.

**Product of polynomials (TeX 632–633).** From `p=(y-μ)r` one gets `c=-r(x,μ) q_x(x,μ)` with `c∈k*`. The paper jumps to `q_x(x,μ)≡e∈k*`. This is valid in `C[x]`: a product of two polynomials equal to a nonzero constant forces both factors to be units, hence nonzero constants. If `r(x,μ)=0` then `c=0`, a contradiction, so that case is already excluded. The missing sentence is presentation, not a hole.

**Step 2 (TeX 693–696) is invalid as written.** The paper says: if `p(x,μ)≡c∈k*`, apply Step 1 to the Keller pair `(p-c,q)`. The Jacobian is unchanged, so `(p-c,q)` still have no common factor and only finitely many common zeros. The *terminal* contradiction of Step 1 is a common zero of `(p,q)` on the line `y=μ`, which was forbidden by the choice of `μ`. The corresponding point for `(p-c,q)` is a common zero of `p-c` and `q`, i.e. a point with `p=c` and `q=0`. That locus was not avoided. The two finite sets are in general disjoint. There is no circular repair by “avoid both”, because the constant `c` is `p(x,μ)` itself and is not known when `μ` is chosen. Step 2 therefore does not carry.

Tried to rescue Step 2 by a different contradiction: if `p(x,μ)≡c≠0`, the line `y=μ` contains no common zero of `(p,q)`, which is consistent with the choice of `μ`, not contradictory. The Jacobian identity does not help. Step 2 stays broken.

**The `μ≠0` repair.** The base field is infinite. Choose `μ` off the finite forbidden set *and* `μ≠0`. Restrict the polynomial identity `xy=H(p,q)`:

```text
μ x = H(p(x,μ), q(x,μ)).
```

Then `x=μ^{-1} H(p_μ,q_μ)∈C[p_μ,q_μ]`. The reverse inclusion `C[p_μ,q_μ]⊆C[x]` is automatic. Hence `C[p_μ,q_μ]=C[x]`. Both Step 1 and Step 2 are unnecessary: if both restrictions were constant and `μ≠0`, the right-hand side would be constant and `μx` would be constant as a polynomial, which it is not. One restriction may be constant; the other then generates `C[x]`, which is still an embedding of the line.

This also exposes an extra printed gap that the repair closes: the paper's own sentence “hence `μx=H(…)`, which shows `k[x]=k[p(x,μ),q(x,μ)]`” is false for `μ=0` even after Steps 1–2, because one obtains only `0=H(p(x,0),q(x,0))`. The paper never excluded `μ=0`.

**Embedding to Gwoździewicz.** Paper Definition 2.15: a polynomial map `g:k→k^2` is an embedding iff `k[g_1,g_2]=k[t]`. The restricted map `x↦(p(x,μ),q(x,μ))` is therefore an embedding, hence injective on points (paper Proposition 2.16). So `f` is injective on the affine line `y=μ`.

Gwoździewicz, arXiv:alg-geom/9305008, Theorem 1.1, read in full: if `k` is algebraically closed of characteristic zero, `H:k^2→k^2` is polynomial with `Jac H∈k*`, and `H` is injective on some line, then `H` is a polynomial automorphism. Hypotheses match `k=C` and a Keller map injective on `y=μ`. The proof reduces the line to `y=0` by an affine automorphism, invokes Abhyankar–Moh on a polynomial embedding of the line, and finishes by a Newton-polygon comparison. The repair supplies the embedding algebraically, so Abhyankar–Moh applies directly; for a Keller map the differential is everywhere invertible, so a mere set-theoretic injection on a line is automatically an immersion, but that extra fact is not needed here.

The repaired theorem does not use prime degree. Scoped conclusion, as the producer states it:

> A complex plane Keller map satisfying `xy∈C(p,q)` is an automorphism, assuming Wang's intersection theorem and Gwoździewicz injectivity-on-one-line.

Tried to break the repair by taking `μ=0`, by allowing a constant restriction, and by asking whether Wang produces a rational rather than polynomial `H`. Wang's intersection puts `xy` in `k[p,q]`, so `H` is a polynomial. The identity restricts as polynomials. `μ≠0` is the only extra choice, and it is available.

### 5. Campaign consequence and successor — CONFIRMED

The first case is the remaining case for a hypothetical AS109 lift: there is no theorem of this paper that a prime-degree Keller map with `xy∉k(p,q)` is an automorphism. Prime degree 109 is not excluded. Avenue 44 must be marked `REFUTED-AS-PROOF`. The paper remains unusable in the AS109 degree cross, `A_infinity`, deck-descent, and sheet-degree ledgers.

If a hypothetical exact lift satisfies `xy∈K(P,Q)` with `K=Q_p`, Wang over the coefficient field (or after a finitely generated embedding into `C`) gives `xy=H(P,Q)`. The repaired second case over `C` then makes the complexification an automorphism, hence the original map is an automorphism over the coefficient field (the polynomial inverse is unique and Galois-invariant). Hensel noninjectivity of an exact AS109 lift is then a contradiction. Membership alone would close that lift. That is a valid independent successor, not a theorem of this freeze: one still needs an exact reason that the lift satisfies the membership.

A search for `H` of bounded degree with `H(P,Q)=xy` is a probe. Cancellation in `H(P,Q)` prevents reading a degree bound for `H` off `deg(xy)=2`. Without an independent bound, a finite ansatz is not exhaustive. The producer states this and does not treat a search as a proof.

### 6. Replay, hashes, and scope strings — CONFIRMED

All four frozen hashes match. The official TeX hash matches. The registered script exits 0 and prints the four advertised Booleans:

```text
paper_first_case_supported = false
paper_second_case_repairable = true
no_prime_degree_theorem_usable = false
jc2_inference = false
```

Those Booleans are labels, not evidence. The mathematical claims were re-derived from the paper, from answer 473055, from Wang 41(i), from Gwoździewicz 1.1, and from the UFD/Kummer argument. The script correctly describes its own cubic sweep as regression and points at the report for the universal argument. TeX line citations 368–370, 411–413, 632–633, and 693–696 were checked against the retrieved `prim.tex` and match.

Producer scope is exact: the audit does not prove that a prime-degree Keller map exists; it proves that this paper does not exclude one. No JC2 inference is claimed. The freeze listing contains only the report and `check.py`, which is the right scope for a validity audit.

---

## What was not consumed

Formanek Theorems 1–2 and the Jedrzejewicz–Zieliński square-factorial/root-closed package were not re-proved. They sit upstream of the rare-property calculation. Claim 1 does not need them: even if that calculation is correct, the degree-two inference fails. Claim 3 does not need them either. Wang 41(i) and Gwoździewicz 1.1 were checked at the level of hypotheses and application, not by reproducing Wang's forty-page separability paper or Abhyankar–Moh.

The `deg_y≤5` frontier, TDU, and the AS109 Hensel/`A_infinity`/deck gates are outside this freeze. They are mentioned only to record that this paper does not land in those ledgers.

---

## Disposition

**Overall: CONFIRMED.**

Promote the audit as a source-validity result: Moskowicz arXiv:2407.13795v1 is `REFUTED-AS-PROOF` for the no-prime-degree theorem; the first case is unsupported as written; the second case is repairable over `C` without prime degree; prime 109 stays live; `xy∈K(P,Q)` is an honest successor gate and not a finite search.

Do not promote a Keller counterexample, a disproof of the headline statement, an AS109 kill, or JC2.
