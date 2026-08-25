# Hostile different-model review — AS fixed-support low-`y` adic escape

| Field | Value |
|---|---|
| Document under review | `xmodel/as-fonly-low-y-adic-escape-bridge-20260825.md` |
| Imported theorem | `xmodel/gcd3-69-coverage-composition-20260824.md` |
| Imported review | `xmodel/gcd3-69-coverage-composition-review-claude-20260824.md` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest failing handoff | none |
| Smallest missing hypothesis | none |
| Reviewer / model | Grok 4.6 (xAI), different model family from the producer and from the imported composition reviewer |
| Mode | read-only; the three charged files were read in full; no file edit, shell, CAS, Python, network, or delegate |

Producer PASS strings and SHA pins were not used as evidence.

## Promotion

Accept the following and nothing more.

Fix finite monomial sets `S_P,S_Q` whose `y`-exponents are at most eleven.
For `n>=1`, let `X_n` be the set of coefficient vectors in
`(Z/3^n)^N`, `N=|S_P|+|S_Q|`, of maps `F=(P,Q)` satisfying

```text
support(P) subset S_P,       support(Q) subset S_Q,
F = (x-x^3,y) mod 3,
det J(F)=1 in (Z/3^n)[x,y]
```

where the last condition means that every coefficient of `det J(F)-1`
vanishes.  Then some finite `n` has `X_n` empty.  Equivalently, there is no
`F in Z_3[x,y]^2` with those supports, that special-fibre reduction, and
`det J(F)=1` as a polynomial identity over `Z_3`.

In particular, the complete total-degree-seven map-only AS coefficient
scheme — 72 monomial coefficients and all 91 coefficients of `det J-1` in
total degree at most twelve — is empty at some finite 3-adic depth.  The
depth is not produced.

Consequently, a complete AS solution of actual `y`-degree at most eleven
that exists at every finite precision cannot keep its allowed monomials
inside any one finite envelope.  A fixed `x`-degree cap is such an envelope,
so it fails at some finite depth depending on the cap.

## Firewall

This gives no first empty depth, effective Nullstellensatz/cokernel
certificate, support-growth rate, covered chronological DAG, or uniform `n`
that empties every low-`y` envelope at once.  It does not empty a displayed
fibre at the next precision and does not license discarding nonreduced
Kuranishi strata.

The result concerns only the residue tube `F=(x-x^3,y) mod 3`, only
`Z/3^n`-points of complete determinant-one coefficient schemes, and only
`y`-exponents at most eleven.  It neither handles an arbitrary Keller
residue, reduces a characteristic-zero Keller pair to this tube, nor proves
or disproves JC2.

The quadratic line `(U,V)=(t*x^7,2*t*x^6*y)` is a valid negative control
against ordinary smooth Hensel continuation at the AS special fibre.  It is
not a proof that every current fibre dies at the next step.

Formal invertibility of `(x-x^3,y)` in `F_3[[x,y]]` is true and irrelevant:
the inverse-function theorem at the origin supplies a series inverse, not a
polynomial automorphism of `F_3[x,y]`.

## 1. Compactness, exact determinant, and points versus schemes

If every `X_n` is nonempty, let `C_n` be its cylinder in the compact ball
`Z_3^N`.  Finite allowed sets make `N` finite.  Each `C_n` is a finite union
of residue classes, hence closed, and

```text
C_(n+1) subset C_n.
```

Nested compactness gives one vector lying in every `C_n`.  The displayed
solutions at consecutive depths need not themselves form a chain: reduction
of polynomial identities gives the nesting, and compactness manufactures a
compatible tower.

With bounded supports, `det J(F)-1` has finitely many coefficients, each an
integer polynomial in the `N` coefficient coordinates.  At the intersection
point every such coefficient is zero modulo `3^n` for all `n`, hence zero in
`Z_3`.  Thus `det J(F)=1` is an exact identity in `Z_3[x,y]`.

This argument uses point-set nonemptiness: `X_n` consists of actual
`Z/3^n` coefficient vectors.  Properness or geometric nonemptiness of a
coefficient ideal over an extension would not suffice.  If the allowed sets
omit a required seed monomial, `X_1` is already empty and the theorem holds
vacuously.

## 2. Handoff from the maximum-eleven theorem

The imported reviewed statement says that, over every characteristic-zero
field `k`, a Keller pair with maximum actual partial `y`-degree at most
eleven is a polynomial automorphism.  It is not a generic-leading-coefficient
statement.

Here `Q_3` has characteristic zero, `F` lies in `Q_3[x,y]^2`, and its
determinant is the unit `1`.  The allowed monomials bound the actual
`y`-degrees by eleven.  Exact vanishing of a leading slot can only lower an
actual degree; a coefficient divisible by three but nonzero in `Z_3` remains
nonzero over `Q_3` but still lies under the same support bound.  Hence the
reviewed theorem makes `F` a polynomial automorphism over `Q_3`.

## 3. Integrality of the polynomial inverse

Let

```text
a=F(0) in Z_3^2,        G=F-a,        L=JG(0).
```

The seed vanishes at the origin, so `a=0 mod 3`.  We have `G(0)=0`, the same
special fibre, and `det JG=1`, so `L in GL_2(Z_3)`; independently `L=I mod
3`.

For the formal inverse orientation `G o H=id`, write homogeneous pieces

```text
G=L+G_2+G_3+...,        H=H_1+H_2+H_3+... .
```

The degree-one equation gives `H_1=L^(-1) in M_2(Z_3)`.  At degree `d>=2`,
the term containing `H_d` is `L H_d`; every contribution from `G_k`, `k>=2`,
uses only `H_1,...,H_(d-1)`, because inserting `H_d` there has degree at least
`d+k-1>d`.  Thus

```text
L H_d = an integral expression in G,H_1,...,H_(d-1).
```

Composition introduces multinomial integers only as multipliers.  Solving
uses `L^(-1)` and never divides by `d`; in particular no hidden division by
three occurs.  Induction gives `H in Z_3[[x,y]]^2`.

The opposite orientation `H o G=id` is equally integral: its degree-`d`
equation solves by linear substitution with `L^(-1)`.  A one-sided formal
inverse with unit linear part is two-sided, so uniqueness identifies the two
recursions.

The maximum-eleven theorem supplies a polynomial inverse of `G` over `Q_3`.
It vanishes at the origin and is therefore a formal inverse.  Uniqueness in
`Q_3[[x,y]]` identifies its monomial expansion with `H`; its finitely many
coefficients all lie in `Z_3`.  Finally

```text
F^(-1)(z)=G^(-1)(z-a),
```

and translating an integral polynomial by `a in Z_3^2` preserves integral
coefficients.

Attempts to break this step all lose a charged hypothesis.  `(x,3y)` has a
nonintegral inverse but nonunit determinant.  `(x,y+x/3)` is not integral.
Formal invertibility without polynomial automorphy gives an integral series
that need not terminate; the characteristic-zero theorem is precisely what
forces termination.  No counterexample survives all charged hypotheses.

## 4. Reduction contradiction

Let `Phi in Z_3[x,y]^2` be the inverse.  Both identities

```text
F o Phi=id,             Phi o F=id
```

reduce modulo three, so `(x-x^3,y)` would have a two-sided polynomial
inverse over `F_3`.  An `F_3` polynomial automorphism induces a bijection on
`F_3^2`.  But Fermat gives `x-x^3=0` at each of the three field elements;
for example `(0,0)` and `(1,0)` have the same image.  This point-set argument
does not identify the nonzero polynomial `x^3-x` with the zero polynomial.
The contradiction closes the proof.

## 5. Consequence audit and negative control

Total-degree-seven monomials form a finite 72-coordinate envelope with
`y`-exponent at most seven.  Its determinant has the full 91 coefficient
rows through degree twelve, so the live complete D7 scheme is an exact client
of the theorem.  Some depth is empty, but no particular depth is selected.

Likewise, an arbitrarily deep complete low-`y` AS sequence cannot remain in
one finite monomial envelope.  This does not give a uniform depth across all
envelopes or exclude supports that grow with precision.

For the quadratic control, over `F_3` the linearized Keller operator is
`U_x+V_y`.  With `(U,V)=(t*x^7,2*t*x^6*y)`,

```text
U_x=t*x^6,       V_y=2*t*x^6,       U_x+V_y=0.
```

The literal reduced determinant is `1+2*t^2*x^12`.  This disproves ordinary
smoothness along that tangent line.  Other combinations or nonreduced
strata may have vanishing higher obstruction, so no fibrewise next-step
terminality follows.

## Verdict

**CONFIRMED.**  There is no failing identity, handoff, or missing hypothesis.
The strongest promotion and strict firewall are exactly those stated above.

Nonblocking prose note: the producer sentence “gives a coefficient vector in
every `C_n`” should be read as “gives one coefficient vector lying in all
`C_n`”; its following sentence already uses the intended single vector.
