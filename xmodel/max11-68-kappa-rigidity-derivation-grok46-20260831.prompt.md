# Research lane: κ≠0 rigidity descent for the max11 68 QZero/FceZero terminal branch

You are a bounded primary research lane (paper mathematics; no Lean required,
no file edits outside your lane workspace). Your task is to DERIVE, or
refute the existence of, the closing contradiction for one exactly-specified
polynomial system. Reading `jc2-lean/max11-partial-y` sources is permitted
read-only; do not edit any repository file.

## Frozen setup (all EXACT, kernel-checked in Lean unless marked derived)

Work over an algebraically closed field k of characteristic zero. On the
wall `9N = 7S`, write `N = 7m`, `m ≥ 1`. Polynomials `A, B, c, d, e, v, W,
q, s, L` in `k[X]`, scalars `alpha, gamma, epsilon, zeta(=0), eta, terminal,
i3, kappa`, with:

- `deg B = 3m` exactly, `B` squarefree (`IsCoprime B B'`), leading coeff
  `B_D ≠ 0`.
- `deg d = 8m` exactly (`d_V ≠ 0`), `deg v = 7m` exactly, `deg W = 5m`
  exactly, `deg L = 17m` exactly.
- `C0 := 81*epsilon*gamma + 27*i3 ≠ 0`, `terminal ≠ 0`.
- `W = 4A + 3v²` (exact polynomial identity; hence `deg A = 14m` with top
  cancellation `A ≡ -(3/4)v² + lower`).
- `C0·v − C(4κ) = B·q`, `deg q = 4m`. So `v ≡ v0 (mod B)` with the scalar
  `v0 = 4κ/C0`.
- `36d² − C(C0) = B·s`, `deg s = 13m`. So `d² ≡ δ (mod B)`, `δ = C0/36 ≠ 0`.
- Bridge (kernel-checked): `B ∣ B'·d·L + C(108·terminal)` with
  `L = v(W² − C(72γ)) + 48d`, and top profile
  `(B'dL).coeff(28m−1) = B_D·(3m)·d_V·v_N·W_R²`.
- Equivalent cleared form (kernel-checked): with `c1 = 162·terminal/C0`,
  `B'L + 24·c1·d` vanishes at every root of `B`, so `B ∣ B'L + C(24c1)·d`.
- Row identities at every root x of B (kernel-checked):
  `B'(x) ≠ 0`, `d(x) ≠ 0`, `C0(A'(x)v(x) − 2B'(x)) = 162·terminal`,
  `B'(AW−18γ) + 6A'd − 9dvv' − 9d'v² = 0` at x,
  `v'(x) = B'(x)q(x)/C0`, `q ≡ −6·v0·W·d (mod B)`,
  `d'(x) = B'(x)W(x)/12`.
- KERNEL-CHECKED (new): the case `κ = 0` is impossible (root-count on `B'`).
  So assume `κ ≠ 0`, `v0 ≠ 0`.
- Kernel-checked congruence: `C0·W' + 6·B'·d·(W² + 6v0²W − 72γ) ≡ 0 (mod B)`
  (a polynomial of exact degree `21m−1` divisible by `B`).
- Coordinator-derived (verify before use): multiplying by `d` and reducing
  `d² ≡ δ` gives `C0·d·W' + 36v0²δ·B'·W − (288δ/v0)·B'·d − C(144c1δ/v0)·d
  ≡ 0 (mod B)`, degree `13m−1`.

## The gap

Derive `False` from this system (for all `m ≥ 1`), or exhibit a consistent
model showing more input is needed. The prior coordinator's plan called this
"the root-count contradiction from the exact degree/top profile". The naive
inference `B ∣ X + C(c) ∧ gcd(B,X)=1 ⟹ B ∣ C(c)` is INVALID; do not use it.

## Candidate routes (attack in this order, but deviate if you see better)

1. **Riccati/Möbius factorization.** Substitute `Y = W + 3v0²`,
   `a² = 72γ + 9v0⁴` (if `a ≠ 0`): the congruence becomes
   `C0·Y' ≡ −6B'd(Y−a)(Y+a) (mod B)`, giving the Wronskian-type congruence
   `Wr(Y−a, Y+a) ≡ −(12a/C0)·B'·d·(Y−a)(Y+a) (mod B)` — compare the
   registered weighted-Wronskian machinery (`GCD369WeightedWronskian*`) and
   Theorem A (`A·C' − ν·A'·C = c ⟹ deg A ≤ 1`, exact identity). At a root
   x of B with `Y(x) = ±a`, the congruence forces `Y'(x) = 0` (double
   root); at other roots `Y'(x) ≠ 0`. Count multiplicities of `Y² − a²`
   (degree 10m) against the 3m roots of B and the degree/top data. Also
   treat the degenerate `a = 0` case (`72γ = −9v0⁴`) separately: then
   `C0Y' ≡ −6B'dY²`, and every root of B with `Y(x)=0` is at least a triple
   root of Y.
2. **Jet tower / ODE rigidity.** Differentiate the congruence and use
   `d' ≡ B'W/12`, `v' ≡ B'q/C0` to close a finite jet system at the roots
   of B; look for a forced identity `P(B', W, d)(x) = const` at all 3m
   roots where the left side is a polynomial of degree < 3m (the κ=0
   pattern), or a forced `B' ∣`-relation contradicting `deg B' = 3m−1`.
3. **Pin κ.** Search the landed terminal-branch modules
   (`Sol68FiveToSixCuspLoadedLowerRowZeta...Terminal*Scratch.lean`) for an
   exact identity constraining κ (row-two/first-integral fiber) that,
   combined with the above, forces `κ = 0` — which is already impossible.
4. **Top-profile bookkeeping.** Exact quotient chains: `B'L + C(24c1)d =
   B·M₁` with `deg M₁ = 17m−1`, `top(M₁) = 3m·v_N·W_R²`; iterate the
   congruences to force a leading-coefficient identity among
   `B_D, d_V, v_N, W_R` that contradicts their exactness.

## Report requirements

Write `xmodel/max11-68-kappa-rigidity-derivation-grok46-20260831.md` with:
verdict `DERIVED` (full contradiction, every step justified at the level of
a referee-checkable proof), `PARTIAL` (exact new identities plus what is
missing), or `BLOCKED` (why each route fails, with the precise obstruction,
and — if you find one — a consistent toy model of the full system, which
would prove more input is needed). Show all computations. Label every claim
you did not verify from the Lean sources as UNVERIFIED. No overclaims: a
plausible sketch is PARTIAL, not DERIVED.
