# Hostile audit: Theorem 2.1 (Henon family / unrestricted K2C)

Reviewer: Grok 4.6 (adversarial verifier). Date: 2026-08-23.
Target: `xmodel/sol-k2c.md` §2, Theorem 2.1. Char 0. Direct computation;
the paper was not trusted. No file changes except this review.

**Method.** Jacobian and inverse of `H_q` by hand. Sparse `Z[x,y]` expansion
of the chains `q=(2)`, `q=(2,2)`, and the actual `r=0` map
`q=(7,3,2,2)`. Fiber parametrizations `P_i(T)` from the inverse recurrence
over `Z[T]`. Homogenized `(X,Y)`-Jacobian by expansion. Zariski
characteristic indices of the `x`-branch by Newton reparametrization
`x(zU)=(\mathrm{lead})\,z^{n_0}` in `Q[[z^{-1}]]`, then running gcd on the
support of `y(z)`. Valuation argument for the Puiseux denominator at every
`r`.

Notation: paper's `s=r+4`, `q=(q_1,\ldots,q_s)=(7,3,2,\ldots,2)`.
Characteristic indices are `q_1,\ldots,q_{s-1}`, **not** including `q_s`.
The prompt's "`r=0`, `q=(7,3,2)`" is the characteristic sequence; the
composition uses four generators `(7,3,2,2)`.

---

## Verdicts on (i)–(vi)

| claim | verdict |
|---|---|
| (i) `Phi_r` is a polynomial automorphism, `J=1` | **CONFIRMED** |
| (ii) `td(f_r,g_r)=1` | **CONFIRMED** |
| (iii) pole orders `n_{s-1}=1`, `n_{i-1}=q_i n_i`, `n_0=42\cdot 2^r` on a generic fiber | **CONFIRMED** |
| (iv) char indices `(7,3,2,\ldots,2)`, `kappa_r=42\cdot 2^r` | **CONFIRMED** |
| (v) `deg f_r=kappa_r`, `deg g_r=2 kappa_r` | **CONFIRMED** |
| (vi) `(F_r)_X(G_r)_Y-(F_r)_Y(G_r)_X=Z^{3 kappa_r-2}` | **CONFIRMED** |

No refutation of Theorem 2.1. One precision note (nongeneric `a=0`) below;
it is already excluded by the paper's "generic fiber".

---

## A. Machinery: `H_q`, then `q=(2)` and `q=(2,2)`

`H_q(u,v)=(v,\,v^q-u)`. Derivative matrix `[[0,1],[-1,\,q v^{q-1}]]`,
determinant `1`. Polynomial inverse `I_q(U,V)=(U^q-V,\,U)`:

```
H_q(I_q(U,V)) = (U, U^q-(U^q-V)) = (U,V)
I_q(H_q(u,v)) = (v^q-(v^q-u), v) = (u,v).
```

Any composition is a polynomial automorphism with Jacobian `1`, hence
topological degree `1`.

**`q=(2)`.** `P_0=x`, `P_1=y`, `P_2=y^2-x`.
`H_2(x,y)=(y,\,y^2-x)`. Affine Jacobian `1`. Homogenized Jacobian `Z`.
Fiber `P_1=a`, `T=P_2`: `y=a`, `x=a^2-T`. Pole orders `n_0=1`, `n_1=0`.
Empty characteristic sequence; `kappa=1`.

**`q=(2,2)`.**
```
P_2 = y^2 - x
P_3 = (y^2-x)^2 - y = y^4 - 2 x y^2 + x^2 - y
Phi = (P_2, P_3),  deg = (2,4)
```
Affine Jacobian `=1` (expanded). Homogenized Jacobian `=Z^4=Z^{3\cdot 2-2}`.
Leading forms `Y^2`, `Y^4`. Inverse `I_2\circ I_2` recovers `(x,y)`.

Fiber `P_2=1`, `T=P_3`:
```
P_3 = T
P_2 = 1
P_1 = 1 - T          (n_1 = 1)
P_0 = T^2 - 2T       (n_0 = 2)
```
Recurrence `n_0 = q_1 n_1 = 2\cdot 1`. Zariski chars of `y` vs `x`: `(2)`,
Puiseux denominator `2`. Unique place `T=\infty`.

---

## B. Actual `r=0`: `s=4`, `q=(7,3,2,2)`, claimed chars `(7,3,2)`, `kappa=42`

```
P_2 = y^7 - x
P_3 = y^{21} - 3 x y^{14} + 3 x^2 y^7 - x^3 - y
P_4 = y^{42} - 6 x y^{35} + 15 x^2 y^{28} - 20 x^3 y^{21} - 2 y^{22}
      + 15 x^4 y^{14} + 6 x y^{15} - 6 x^5 y^7 - 6 x^2 y^8 - y^7
      + x^6 + 2 x^3 y + y^2 + x
P_5 = P_4^2 - P_3     (58 terms, deg 84)
```
`(f_0,g_0)=(P_4,P_5)`. Degrees `42` and `84`. Leading forms `Y^{42}`,
`Y^{84}`. Affine Jacobian expanded to the constant `1`. Composition inverse
`I_7\circ I_3\circ I_2\circ I_2(P_4,P_5)=(x,y)` on the nose.

Homogenized `(X,Y)`-Jacobian expanded: **`Z^{124}`**, and
`3\cdot 42-2=124`. This is (vi) at `r=0` by direct expansion, not only by
the formal identity `J(f,g)=1 => homog jac = Z^{d+e-2}`.

**Inverse recurrence on `P_4=a`**, `T=P_5` (generic `a=1`):
```
P_4 = 1                         n_4 = 0
P_5 = T                         n_5 = 1
P_3 = 1 - T                     n_3 = 1 = n_{s-1}
P_2 = T^2 - 2T                  n_2 = 2 = q_3 n_3
P_1 = T^6 - 6 T^5 + 12 T^4 - 8 T^3 + T - 1     n_1 = 6 = q_2 n_2
P_0 = P_1^7 - P_2               n_0 = 42 = q_1 n_1
```
Strict inequality `q_i n_i > n_{i+1}` at each step; no leading-term
cancellation. Running gcd: `42,6,2,1` with ratios `7,3,2`. Same pole
orders at `a=2`. Product `7\cdot 3\cdot 2=42=42\cdot 2^0`.

**Zariski characteristics of the `x`-branch** (reparam `x=z^{42}`, residual
`0` in `Q[[z^{-1}]]` to order `80`). Support of `y(z)` at `a=1` and `a=2`:
leading `z^6`, then first new gcd-dropping term `z^{-34}`, then `z^{-39}`.
Drops
```
(42,6) --nu=7--> 6,     (6,-34) --nu=3--> 2,     (2,-39) --nu=2--> 1.
```
Characteristic indices **`(7,3,2)`**, remaining gcd `1`, Puiseux
denominator **`42`**. Naive Tschirnhausen `T=z` (no unit correction)
produces a spurious `z^5` term and fake indices `(7,6)`; that is an
artifact. After the correct reparametrization the paper's sequence is
the actual Zariski sequence.

Completion argument (any `r`, no series): on a generic fiber,
`C[x,y]\cong C[T]`, `v_\infty(x)=-n_0`, `x^{-1}=t^{n_0}\cdot(\mathrm{unit})`
with `t=T^{-1}`, and `T=g_r(x,y)`, so
`[C((T^{-1})):C((x^{-1}))]=n_0`. Minimal Puiseux denominator over `x`
is exactly `n_0`.

**Degrees.** Induction `deg P_0=deg P_1=1`, `deg P_{i+1}=q_i deg P_i`
because `q_i deg P_i > deg P_{i-1}`. Thus
`deg(P_2,\ldots,P_5)=(7,21,42,84)` at `r=0`. For general `r`,
`deg f_r=7\cdot 3\cdot 2^{r+1}=kappa_r`, `deg g_r=q_s kappa_r=2 kappa_r`.

**`r=1` spot-check** (`q=(7,3,2,2,2)`): fiber pole orders
`[84,12,4,2,1,0,1]`, affine degrees `[1,1,7,21,42,84,168]`. Matches
`kappa_1=84`, `deg g=168`, claimed ratios `(7,3,2,2)`.

**Nongeneric `a=0`:** pole orders still `(42,6,2,1)` but the Zariski series
of `y` misses the last drop (`kappa=21`, chars `(7,3)`). Not a counterexample:
the paper states generic fiber.

---

## C. Unrestricted K2C

The family is a genuine automorphism (`td=1`) for every `r\ge 0`. The pole
Puiseux denominator is `kappa_r=42\cdot 2^r\to\infty`. The full
pure-boundary identity holds (expanded at `r=0`; for general `r` it is the
identity `J=1` plus (v)). Therefore

> bounded `td` + polynomial origin + the full boundary identity
> ⇏ bounded `kappa`.

**Ruling: unrestricted K2C is genuinely FALSE.**

This is not an artifact of H1 sheet calculus. It is also not a new
phenomenon beyond Jung–van der Kulk *except* for the boundary-identity
clause: the identity does not supply a degree-independent stopping index,
because each new approximate root raises `(d,e)` and with it the vanishing
order `d+e-2`. Directly visible in the family: the identity is satisfied
at every length.

---

## D. Scope: residue-A / type `(2,3)` / degree-minimal

The family does **not** enter the intended sector.

- Invertible, `td=1`, not `td=6`.
- One place at infinity: leading form `Y^{kappa}`, point `[1:0:0]` only;
  germ `u\sim v^{6/7}` at `r=0` is a single branch (`gcd(6,7)=1`).
  Residue-A is a two-pole inventory.
- Reduced type `(1,2)` (`deg g/deg f=2\in N_{>0}`). Sigray Lemma 2.1
  *excludes* integer slope ratios; type `(alpha,beta)` requires
  `2\le alpha<beta` coprime. This is never type `(2,3)`.
- Lexicographic degree-minimization under `K\circ Phi_r\circ L` with
  `K=Phi_r^{-1}` returns a linear automorphism. The degree-minimal
  representative has `kappa=1`. The long approximate-root chain is a
  re-embedding, not an invariant of the Aut-orbit.

So: honest scoping. Restricting K2C to lexicographically degree-minimal
nonautomorphic Sigray-normalized type-`(2,3)` (and, for UCD-A-min, the
residue-A `td=6` inventory) is the *minimal* restriction that actually
avoids this family. The Henon maps do not secretly realize that sector,
and composing them on the domain or target of a hypothetical residue-A
pair is undone by the same minimization.

**No overreach in the exclusion.** The paper already records that the
family is not residue A and does not realize the handshake (2.7) /
FORMAL equalities (4.1) of `sol-unify.md`.

**Mild rhetorical overreach only:** "realizes the carrier mechanism" means
"realizes unbounded gcd-drop length at fixed `td` in the automorphic
one-place category." It does not produce a polynomial residue-A pair, and
it does not show the FORMAL `l=0` tower is polynomial-origin. The document
states this in §4; the theorem statement itself does not claim otherwise.

---

## One-line rulings

- Unrestricted K2C ("bounded `td` + polynomial origin + boundary identity
  ⇒ bounded `kappa`", all Keller pairs): **FALSE**, by this family.
- Degree-minimal / nonautomorphic / type-`(2,3)` scoping: **legitimate**.
  The Henon family does not threaten that sector.
- Residue-A K2C / UCD-A-min: **untouched**, remains a conjecture.
