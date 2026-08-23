# Grok rooftop review — Claims 1 and 2 of `sol-rooftop.md`

Adversarial check of the two hand-verifiable algebraic claims in
`xmodel/sol-rooftop.md`. Direct computation only; campaign framing ignored.
Char 0 throughout (as in the JC setting).

---

## CLAIM 1 (eq 4.1) — **CONFIRMED**

**Statement.** If `J(f,g)=j∈k*`, and `F,G` are the degree-`d,e` homogenizations,
then `F_X G_Y − F_Y G_X = j Z^{d+e−2}`.

**Partials.** `F_X` means `∂F/∂X` in `k[X,Y,Z]`, not the homogenization of
`f_x` to `deg(f_x)`. These agree after padding: the chain rule gives
`∂F/∂X = Z^{d−1} f_x(X/Z,Y/Z)`, so `(∂F/∂X)|_{Z=1}=f_x` even when
`deg(f_x)<d−1` (extra `Z` factors). Same for `Y` and for `G`. Consequently

\[
F_X G_Y-F_Y G_X
= Z^{d+e-2}\,J(f,g)\Bigl(\frac XZ,\frac YZ\Bigr),
\]

which is the degree-`(d+e−2)` homogenization of `J`. Keller is the case
`J≡j`. `F_Z` is not used in (4.1); Euler `XF_X+YF_Y+ZF_Z=dF` holds but is
orthogonal.

**Homogeneity.** `F` deg `d` ⇒ `F_X,F_Y` deg `d−1`; product-minus-product
has deg `(d−1)+(e−1)=d+e−2`.

**Dehomogenization.** `Z=1` recovers `J(f,g)=j` by the chain-rule identity
above.

**Uniqueness.** A form of deg `m=d+e−2` is `∑_{i+j≤m} a_{ij} X^i Y^j Z^{m−i−j}`.
Each `(i,j)` occurs with exactly one `Z`-power, so the monomials remain
linearly independent at `Z=1`. Dehomogenization equal to the constant `j`
forces `a_{ij}=0` for `(i,j)≠(0,0)` and `a_{00}=j`. No cancellation gap.

**Toy check (elementary automorphism, J=1).**
`g=y+x^2`, `f=x+g^2=x^4+2x^2y+y^2+x`, `d=4`, `e=2`.

- `F=X^4+2X^2YZ+Y^2Z^2+XZ^3`, `G=X^2+YZ`
- `F_X=4X^3+4XYZ+Z^3` (the `Z^3` is the padded `f_x` linear term)
- `F_Y=2X^2Z+2YZ^2`, `G_X=2X`, `G_Y=Z`
- `F_XG_Y−F_YG_X=Z^4=1·Z^{4+2−2}`

Also checked: `(x+y^2,y)`, `(x+y^2+1,y)`, `(x+y^3+y,y)`,
`(x+y^2,\,y+x+y^2)`, `(x+(y+x^2)^3,\,y+x^2)`. All give `LHS=Z^{d+e−2}`.
Euler residual 0 on each `F`.

**No gap in (4.1).** (4.2) is the 3×3 expansion along `C=Z^N` and was not
re-audited as a numbered claim; the 2×2 minor is exactly (4.1).

---

## CLAIM 2 (§5.2, eqs 5.5–5.11) — **CONFIRMED** (all of (a)–(e))

Fix coprime `2≤α<β`, `d=Bα`, `e=Bβ`, `f_B=x^d+y`, `g_B=x^e+y^{e−1}`.

**(e) Jacobian.** Direct:

\[
f_x=dx^{d−1},\; f_y=1,\; g_x=ex^{e−1},\; g_y=(e−1)y^{e−2},
\]
\[
J=d(e−1)x^{d−1}y^{e−2}−e\,x^{e−1}.
\]

Matches (5.12). Not constant: `α≥2`, `β≥3` ⇒ `e≥3`, two distinct monomials.
Checked on `(α,β,B)∈{(2,3,1),(2,3,2),(2,3,3),(3,4,1),(3,5,2),(2,5,4)}`.
(If `char p` divides both `d(e−1)` and `e`, e.g. `p|B`, then `J=0`;
irrelevant in char 0.)

**(a) Algebraic independence.** Char 0 and `J≠0` ⇒ the map `A^2→A^2` is
dominant ⇒ `f_B,g_B` alg. independent. No issue.

**(b) `td=d(e−1)`.** Set `u=f_B`, so `y=u−x^d` and `k(x,y)=k(u,x)`. Then
`g_B=P(x)` with `P=x^e+(u−x^d)^{e−1}∈k(u)[x]`. Leading term of
`(u−x^d)^{e−1}` is `(−1)^{e−1}x^{d(e−1)}` (coeff `±1`, any char). The extra
`x^e` is strictly lower degree: `d(e−1)>e` iff `d>e/(e−1)=1+1/(e−1)`, true
for `d≥2`. So `deg_x P=d(e−1)`. Direct expansions: `(2,3,1)` gives
`P=x^4+x^3−2ux^2+u^2` (deg 4); `(2,3,2)` deg 20; `(3,4,1)` deg 9.

Field degree: `P(X)−v` is degree 1 in `v`, hence irreducible in
`k(u)[X,v]` and therefore in `k(u,v)[X]` (Gauss). So
`[k(u)(x):k(u)(P(x))]=deg P=d(e−1)`. Combined with `k(x,y)=k(u,x)`,
`td(f_B,g_B)=d(e−1)`. The paper’s “has `x`-degree `d(e−1)`, hence field
degree `d(e−1)`” is the standard polynomial-map theorem on `A^1`; not a gap.

**(c) Leading forms.** `F=X^d+YZ^{d−1}`, `G=X^e+Y^{e−1}Z`. At `Z=0`:
`F_d=X^d=(X^B)^α`, `G_e=X^e=(X^B)^β`. Checked on the six triples above.

**(d) Energy arithmetic.** Exact, no correction:

\[
\frac{td}{αβ}=\frac{d(e−1)}{αβ}=\frac{Bα(Bβ−1)}{αβ}=\frac{B(Bβ−1)}{β}=B^2−\frac Bβ.
\]

Then `\|H_∩\|^2=B^2−E_{MR}=B/β`. Sample: `(2,3,1)` → `td=4`, `E=2/3`;
`(2,3,2)` → `td=20`, `E=10/3`; `(2,3,3)` → `td=48`, `E=8`;
`(2,5,4)` → `td=152`, `E=76/5`. For fixed `(α,β)`, `B^2−B/β→∞` as `B→∞`,
and `E_{MR}/B^2→1`.

The family also satisfies the *leading-form* Jacobian vanishing
`J(X^d,X^e)=0` (both are powers of `X`), but **fails** (4.1): e.g. `(2,3,1)`
gives `F_XG_Y−F_YG_X=4XYZ−3X^2Z≠cZ^3`. So it kills “common leading power /
leading-form Keller” without touching G5.

**(e) already done.** Not a Keller counterexample; paper states this correctly.

**Implication class.** Finite generation of the (normalized) multi-Rees
algebra of `(F,Z^d)` and `(G,Z^e)` is automatic for every pair (Noetherian
base, excellent normalization). Completeness/antinefness of the rooftop is
definitional (`c=integral closure of a^β+b^α`). Common leading power holds
by (c). Energy is nevertheless unbounded in `B`. The stated implication is
genuinely refuted. Generic pairs with disjoint leading zeros still give the
endpoint `td=de`, `E_{MR}=B^2`; this family shows alignment only knocks off
`B/β`.

---

## Hodge / convexity sign — **CONFIRMED, wrong direction**

Exceptional CS / Teissier–Rees–Sharp / reverse AF:
`e_∞(I,J)^2≤e_∞(I)e_∞(J)=N^4` ⇒ `e_∞(I,J)≤N^2`. With
`e_∞(I,J)=N^2−αβ\,td` this is `td≥0`, i.e. `E_{MR}≥0`. Equivalently
`⟨X,Y⟩=B^2−E_{MR}` and `|⟨X,Y⟩|≤B^2` yield `0≤E_{MR}≤2B^2`; the extra
`\|H_∩\|^2=B^2−E_{MR}≥0` tightens to the trivial Bézout box
`0≤E_{MR}≤B^2`. G5 wants an *upper* bound on `E_{MR}` (mixed multiplicity
near its maximum). Hodge/AF supply the opposite wall.

---

## Strategic conclusion

Yes: Claim 2 shows that finite generation, antinef/rooftop convexity,
Hodge/AF/mixed volume (`E_{MR}≥0`, wrong sign), and even balanced
common-leading-power (which already implies `J(F_d,G_e)=0`) do not bound
`E_{MR}` uniformly in `B`; any G5 `td`-ceiling must use the full Keller
identity (4.1), not those structures and not the leading-form shadow of
Keller.
