# D108 upper envelope from the polynomial Euler element

2026-09-06. Desk `model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

**PROVED, conditional only on the explicitly retained external theorem:**
every characteristic-zero Keller specialization of the frozen D108 source
admits one A-translation making its B-top faces exactly `A^24 B^84` and
`A^16 B^56`. No B-exponents above 84 or 56 occur even before translation.
The translation preserves the complete fixed `(4,-1)` faces and both
unique total leaders. This discharges the gate's missing interface (U),
not the whole published-case composition or JC2. A fresh independent gate
is still required. No novelty claim is made for these shape consequences.

## 1. Frozen input and exact external theorem

Read the complete terminal gate
`xmodel/d108-published-case-gate-fable5-20260906.md`, SHA-256
`7c6a045bf2995a2efe1d1715a8c4d2390030ea79172f7ea61f82c42a9281cfa8`.
Its confirmed input facts are polynomial Keller F,G in K[A,B], with

```text
ell_(1,1) F=A^24 B^84, ell_(1,1) G=A^16 B^56,
ell_(4,-1) F=[A(AB^4-1)^7]^3,
ell_(4,-1) G=[A(AB^4-1)^7]^2.
```

Only these source facts and `[F,G] in K*` are needed below. No residual
point, genericity, minimality, or coefficient-radical claim is assumed.
The terminal producer `d108-published-case-interface-astra-20260906.md`
was also read fully, SHA-256
`528d745faac9de5a7e80a57e534c1f36377eb99b8576c1cfa72894fa3b110a1e`:
its §2 gives `h_top=(X+W)^8 W^28`, so the displayed total monomials
follow directly under A=X+W, B=W. Its broader closure claim is not
consumed across the subsequent gate's identified gap.

Primary source: Guccione–Guccione–Valqui, *On the shape of possible
counterexamples to the Jacobian Conjecture*, arXiv:1401.1784v3, Theorem
2.6, with Remark 2.5 and endpoint conventions 1.5–1.8. The local primary
text `box/census-coverage-20260905/core-ggv-layout.txt` has SHA-256
`e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1`.
Read the entire theorem statement/proof, its supporting §§1–2 through
that proof, and notes [4]–[5]; also read Proposition 4.7 and note [14]
for historical comparison. Theorem 2.6's existence result, including
its cited upstream lemma, is retained as EXTERNAL-THEOREM, not reproved.

The precise part used: for a polynomial Keller pair P,Q, a primitive
integer direction `(rho,sigma)` with `rho+sigma>0` and `v(P)>0` admits
a polynomial homogeneous Euler element E of weight `rho+sigma`, with

```text
[E,ell P]=ell P,
st(P) parallel st(E), or st(E)=(1,1).
```

The polynomial clause is Theorem 2.6(1), not its Laurent-only conclusion.
The direction need not have rho>0: `(0,1)` lies in V_{>0} and is allowed.
For these directions st is the support point maximizing `i-j` on the
face. Remark 2.5 says that monomial E forces `E=cAB` and, since the
weight sum is positive, ell P monomial. None of these statements has a
minimal-counterexample hypothesis. Note [14] already uses an analogous
linear Euler element for a translation; its minimal-pair setting is not
silently imported into the argument below.

## 2. Upper-envelope lemma from the total leading monomial

**Lemma.** Let P belong to a polynomial Keller pair over a characteristic-
zero field. Suppose its total leading form is the single monomial
`c A^a B^b`, with `c!=0`, `a,b>0`. Then `deg_B P=b` (and, by swapping
the variables, `deg_A P=a`).

Suppose a support point `(i,j)` has j>b. Unique total leading form gives
`i+j<a+b`, hence i<a and
`0<(j-b)/(a-i)<1`. Choose the maximum of these finitely many rational
ratios, and write it in lowest terms as `rho/sigma`. Thus
`0<rho<sigma`. For the weight `rho i+sigma j`, `(a,b)` ties with at least
one of the selected points and dominates all support points:
points with i<=a,j<=b are immediate; when i>a,j<b the strict total-
degree inequality remains strict after replacing the A-weight 1 by
`rho/sigma<1`; the remaining points are covered by maximality.

Consequently this is an exposed nonmonomial face with start `(a,b)`;
its other points have smaller A and larger B coordinates. Explicitly
the direction along that face is a positive multiple of
`(-sigma,rho)`, which has positive cross product with `(rho,sigma)`
and agrees with the paper's counterclockwise endpoint convention.
The weight of P is `rho*a+sigma*b>0`, so Theorem 2.6 applies.

Any polynomial monomial `A^u B^v` of weight `rho+sigma` has v<=1.
If v=1, then u=1; if v=0, then u=1+sigma/rho must be an integer.
Thus E has support contained in `{(1,1),(1+sigma/rho,0)}`. If only one
term occurs, Remark 2.5 contradicts the nonmonomial P face. Therefore
both occur (in particular rho=1 by primitivity), and

```text
st(E)=(1+sigma/rho,0) != (1,1).
```

Theorem 2.6(2) now forces this point to be parallel to `(a,b)`, impossible
because b>0. This contradiction proves `deg_B P<=b`; the leading
monomial gives equality. The swap argument has Keller bracket changed
only by a nonzero sign. No simple-root assumption occurs anywhere.

## 3. The top B-face is a single shifted power when b>a

Write `ell_(0,1) P=p(A)B^b`. By the lemma, `deg p=a`, with leading
coefficient c. Apply Theorem 2.6 at `(0,1)`: its polynomial Euler
element necessarily is `E=e(A)B`, where e is a nonzero polynomial.
With the convention `[R,S]=R_A S_B-R_B S_A`, the identity is exactly

```text
b e' p-e p'=p.                                         (ODE)
```

Assume b>a>0. If e has degree zero, the left side has degree a-1,
contradiction. If `r=deg e>=2`, its highest coefficient is
`lc(e)*c*(br-a)!=0`, and degree `a+r-1>a`, again a contradiction.
Hence `e=alpha A+beta`, and comparison of degree a gives
`alpha=1/(b-a)`. Setting `s=beta/alpha`, equation (ODE) becomes

```text
(A+s)p'=a p,    hence p=c(A+s)^a.                       (TOP)
```

The last implication follows by translating A+s to a new variable
and comparing all polynomial coefficients; it includes all root
multiplicities and works over K itself. In particular no extraction
of roots or field extension is needed. The translation parameter is
also `s=[A^(a-1)]p/(a*c)`.

## 4. Simultaneous F,G normalization and fixed-face preservation

Apply §§2–3 to F with `(a,b)=(24,84)`. It follows that

```text
deg_B F=84,   ell_(0,1) F=(A+s)^24 B^84.
```

Apply §2 to G: `deg_B G=56` and
`ell_(0,1) G=q(A)B^56`, where q has degree 16 and leader 1.
The maximal possible B-weight of their bracket is `84+56-1=139>0`.
Since the actual bracket is a nonzero constant, its weight-139 part
must vanish, equivalently (also Proposition 1.13)

```text
56 p' q-84 p q'=0,     p=(A+s)^24.
```

Cancel the nonzero polynomial `(A+s)^23` in this polynomial identity.
It gives `(A+s)q'=16q`, whence `q=(A+s)^16`. Thus both components
have the SAME translation parameter, not independently chosen roots.

Let `tau(A)=A-s`, `tau(B)=B`. This polynomial automorphism has Jacobian
one, and

```text
ell_(0,1) tau(F)=A^24 B^84,
ell_(0,1) tau(G)=A^16 B^56.
```

Translation creates no higher B powers. Each replacement term in
`(A-s)^i B^j` has A-exponent <=i, with equality only for the original
monomial. Therefore it preserves both unique total leaders. It also
strictly lowers `(4,-1)` weight by `4k` for each k>=1 decrease in the
A-exponent; hence both complete fixed `(4,-1)` faces are unchanged.
This includes all numeric endpoint and edge coefficients, not just
the direction. The original highest-A faces remain unchanged as well.
In source coordinates `X=A-B, W=B`, tau is simply `X -> X-s, W -> W`.

The new polynomials need not obey every optional coefficient gauge of
the original parameter chart. That is immaterial for this interface:
the permitted translation preserves Keller-ness, all listed published
case data, and supplies precisely the missing upper-envelope (U).
It is not asserted to be a unit certificate for the ambient source
ideal, nor does it erase any retained external proof/certificate debt.

## 5. Tiny exact controls and custody

`box/d108-upper-envelope-euler-20260906/check.py` uses only Python's
standard library and exact rational arithmetic, with 25-second CPU
and 512-MiB address-space caps. It checks the vertical Euler sign and
constant, common root for degrees 24/16, rejection of a shifted G-root,
translation sign, endpoint orientation and allowable Euler support,
and full translated `(4,-1)` faces plus total leaders for both powers.
The checker SHA-256 is
`d169f48554949d6660cb1749725913e5a28adbfadba0ab2fb782b8a5f37789a3`.
Normal and `python3 -O` runs each returned twelve PASS markers and
`ALL_EXACT_CONTROLS_PASS`; the shifted-root mutation was rejected in
each run. Checks use explicit exceptions, not erasable assertions.

The non-Keller negative geometry control is
`P=A^24 B^84+A^22 B^85`: it has the required unique total monomial but
violates the envelope, with exposed normal `(1,2)`. With `Q=B` its
bracket is nonconstant. Thus the proof uses Keller-ness through the
polynomial Euler theorem; unique total support alone is insufficient.
The controls do not solve a source specialization or certify a
Jacobian unit. No AWS, CAS package, live peer body, shared-ledger edit,
or `jc2-lean` access. All owned jobs terminate before report sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9204`.
- Body SHA-256:
  `379feb67d8ae83afc25a5edefb01013e121587addb6e4f91a27be81d19fcb1aa`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
