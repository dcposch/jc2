# Source audit — Moskowicz prime generic-degree claim

**Verdict: `FIRST CASE UNSUPPORTED / HEADLINE THEOREM NOT ESTABLISHED AS
WRITTEN / SECOND CASE REPAIRABLE`.**

- Paper: Vered Moskowicz, *There are no Keller maps having prime degree field
  extensions*, arXiv:2407.13795v1 (submitted 2024-07-16),
  <https://arxiv.org/abs/2407.13795>.
- Source retrieved from the official arXiv source link on 2026-08-24;
  compressed TeX SHA-256
  `a41bf70500b9c95c774221b0c7261d50e6bd8465b8f375e334adbbfc75adbf42`.
- Cited MathOverflow post:
  <https://mathoverflow.net/questions/472877/a-subfield-r-subseteq-mathbbcx-y-with-many-generators-w-rw-math>.
- Audit scope: the two case proofs and the precise use of the MathOverflow
  answer.  This is a validity audit, not a priority claim.
- JC2 inference: none.  The audit does not prove that a prime-degree Keller
  map exists; it proves that this paper does not exclude one.

## 1. Load-bearing failure

The paper defines the **rare property** for a subfield

```text
R=k(p,q) subset L=k(x,y):
R(x^i y^j)=L for every (i,j)!=(0,0).
```

Its TeX lines 368--370 state that the cited MathOverflow answer proves every
such extension has degree two.  Lines 411--413 use exactly that statement to
finish the first case: the preceding argument establishes the rare property,
then the purported degree-two conclusion makes the extension Galois and hence
the Keller map invertible.

The cited answer proves no universal implication.  It starts with a chosen
quadratic extension `L=R(sqrt(u))` and constructs coordinates for which all
nonconstant monomials are primitive.  It is an **example of degree two**, not
a proof that the rare property forces degree two.  The later edit in the
question repeats the stronger interpretation, but that assertion is not in
the answer and has no proof there.

Thus the implication

```text
rare property  =>  [L:R]=2
```

used at TeX lines 370 and 412 is unsupported.

## 2. Exact countercontrol: the rare property occurs in every degree

The missing field-theoretic implication is in fact false.  Fix any integer
`n>=2`, put

```text
L=C(s,v),             R=C(s^n,v),
x=s+v,                y=s+2v.
```

The linear change is invertible:

```text
s=2x-y,               v=y-x,
R=C((2x-y)^n,y-x) subset C(x,y),
[L:R]=n.
```

Both generators of `R` are polynomials in `x,y` and are algebraically
independent.  The extension is cyclic Galois, with `s -> zeta*s`, `v -> v`
for `zeta^n=1`.

Let `(i,j)!=(0,0)`.  If a Galois element fixes

```text
x^i y^j=(s+v)^i(s+2v)^j,
```

unique factorization in `C[s,v]` says that the two linear-factor multisets
with slopes `{1,2}` and `{1/zeta,2/zeta}` agree, with multiplicities `i,j`.
If only one exponent is nonzero, its factor immediately gives `zeta=1`.  If
both are nonzero and the multiplicities distinguish the factors, each factor
is fixed and again `zeta=1`.  If the multiplicities allow a swap, a swap would
require simultaneously `1/zeta=2` and `2/zeta=1`, which is impossible.
Therefore the stabilizer is trivial, the orbit has size `n`, and

```text
R(x^i y^j)=L
```

for every nonconstant monomial.  The rare property therefore places **no
degree-two restriction at all**.  Taking `n=3` already contradicts the exact
implication used in the paper.  The MathOverflow answer is the `n=2` member
of essentially this family.

The registered replay checks the cubic Galois action exactly over
`Q[zeta]/(zeta^2+zeta+1)` for `0<=i,j<=24` and both nontrivial automorphisms.
That finite sweep is regression only; the UFD argument above proves all
exponents and all `n>=2`.

## 3. Consequence for the first case

The algebra before the failing step may establish that a hypothetical
prime-degree Keller extension with `xy notin k(p,q)` has the rare property.
It cannot then conclude degree two.  The control above is not itself a
Keller subfield, so it does not disprove the paper's *headline conclusion*;
it disproves the general field lemma on which the printed proof relies.

No replacement argument exploiting additional Keller structure appears
between the rare-property calculation and the degree-two invocation.
Accordingly:

```text
Theorem “First Case”       NOT ESTABLISHED AS WRITTEN
headline no-prime theorem  NOT ESTABLISHED AS WRITTEN
prime degree 109           NOT EXCLUDED BY THIS PAPER
```

The AS109 `A_infinity=0` gate must therefore remain live rather than being
killed by arXiv:2407.13795.

## 4. The second case is repairable

The second case assumes `xy in k(p,q)`.  Wang's intersection theorem gives
`xy=H(p,q)` for a polynomial `H`.  The paper chooses a horizontal line
`y=mu` avoiding the finitely many common zeros of `p,q` and then spends two
steps proving that neither restriction is zero or constant.

There are two presentation problems:

1. TeX line 633 jumps from
   `c=-r(x,mu)q_x(x,mu)` to `q_x(x,mu)` constant.  This is valid only after
   saying that a product of two polynomials equal to a nonzero scalar makes
   both factors units.
2. TeX lines 693--696 apply Step 1 to `(p-c,q)`.  The chosen line avoids
   common zeros of `(p,q)`, not of `(p-c,q)`, so the final contradiction of
   Step 1 does not carry over.  Step 2 is therefore invalid as written.

Neither issue is fatal.  Since the base field is infinite, choose `mu` not
only outside the finite forbidden set but also `mu!=0`.  Restriction of
`xy=H(p,q)` then gives

```text
mu*x=H(p(x,mu),q(x,mu)).
```

Hence `x` belongs to `C[p(x,mu),q(x,mu)]`; the reverse containment is
automatic.  Thus

```text
C[p(x,mu),q(x,mu)]=C[x]
```

without either Step 1 or Step 2.  The restricted map is a polynomial
embedding of the line, and the cited injectivity-on-one-line theorem then
makes the Keller map an automorphism.  This repair does not use prime degree.

The valid scoped consequence is therefore:

> A complex plane Keller map satisfying `xy in C(p,q)` is an automorphism,
> assuming Wang's intersection theorem and the cited injectivity-on-one-line
> theorem.

## 5. Campaign disposition and successor

- Mark avenue 44 `REFUTED-AS-PROOF`, not merely unvetted.
- Do not use the claimed no-prime-degree theorem in the AS109 degree cross,
  `A_infinity`, deck-descent, or sheet-degree ledgers.
- Preserve the repaired second case as a known-result gate.
- A bounded new AS109 client is **`AS109-XY-MEMBERSHIP`**: seek an exact
  reason that an `A_infinity=0` lift, or a lift carrying a descended deck
  symmetry, must satisfy `xy in K(P,Q)`.  Membership alone would close that
  lift.  A finite-degree ansatz for `H(P,Q)=xy` is not exhaustive unless an
  independent degree bound for `H` is proved.

## 6. Replay

Run:

```text
python3 cases/moskowicz_prime_degree_audit_20260824/check.py
```

Expected headline:

```text
MOSKOWICZ-PRIME-DEGREE-AUDIT: PASS
paper_first_case_supported = false
paper_second_case_repairable = true
no_prime_degree_theorem_usable = false
jc2_inference = false
```

The replay and this report are to be frozen before different-model review.
