# NONMONOGENIC lane: four-coefficient bypass and class (7.1)

## 1. Scope, frozen inputs, and result status

This report is confined to the nonmonogenic Miranda residual of the
provisional `(6,4)` row.  Before using an input, the three frozen copies were
hashed; all three receipts matched the charge exactly:

```text
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  pi1s4-64-triple-cover-close-sol56-20260831.md
c99ffc7f64562ac08e81aa7e927dc04e8c0765182d99db9fdc9f10351772cf9f  pi1s4-64-triple-cover-r2-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

**Verdict: OPEN; no uniform kill is obtained.**  The proposed purely local
four-coefficient invariant obstruction fails: the binary-cubic
discriminant has a transverse cusp at the triple-root stratum, and a local
analytic coefficient map realizes the required order `5` by setting its
two transverse parameters to `v^5` and `w`.  This model is not a
globalization with the fixed `F` and charged `S_4` lift, so the full global
four-coefficient bypass remains OPEN.  The charged bounded-degree list
`{2,3,4,6}` is not a list for unrestricted local Miranda jets.  Separately,
a free, normal, locally
monogenic cubic algebra over `C[x,y]` with irreducible squarefree sextic
discriminant can fail to represent a unit.  That countermodel does not have
the row's infinity and is not known to admit the charged `S_4` lift, so it
does not prove that the residual class is nonempty.

Consequently the prior conditional theorem remains the strongest result:
every hypothetical charged representation with a monogenic cubic resolvent
is impossible; any survivor must lie in the explicitly typed nonmonogenic
`S_4`-compatible class in section 5 below.  The row geometry and fixed-tuple
routing remain provisional at exactly the scope stated by the coordinator.
No exit-price assertion is made.  No CAS was used.

## 2. Charged setup and conventions

Put `R=C[x,y]` and `D_F=V(F)`.  The frozen row data say that `F` is an
irreducible reduced sextic, that `D_F` has exactly three ordinary affine
nodes and no other affine singularity, and that its projective closure has a
single physical point `Q_infty=[1:0:0]` at infinity.  This point, the unique
place `Q_tilde` on the normalization above it, and any sheet of a cover are
different objects.  In suitable analytic coordinates `(v,w)` at the
physical point, after subtracting the even part of the charged expansion,
the place has parameter `s` with

```text
v=s^2,       w=lambda s^15+higher,       lambda!=0.    (2.1)
```

Thus the curve germ is of type `(2,15)`, has multiplicity two and
`delta_infty=7`; give `v,w` weights `2,15`, so its initial weight is `30`.
The original line-at-infinity intersection is six; it is not the exponent
`15` in the sheared local coordinate.  These data concern the curve place,
not a cover series.

For a charged surjection
`phi:pi_1(A^2-D_F)->S_4`, smooth meridians are transpositions and the two
branch meridians at every node are commuting transpositions.  Let
`q:S_4->S_3` be the quotient with kernel the Klein four group.  The charged
local calculation sends the two node meridians to the same transposition in
`S_3`.  Hence `psi=q o phi` gives a connected normal finite-flat cubic cover
whose completed algebras at a smooth branch point and at a node are,
respectively,

```text
Rhat direct-sum Rhat[t]/(t^2-u),
Rhat direct-sum Rhat[t]/(t^2-uv).                     (2.2)
```

Its generic Galois closure has group `S_3`, and its algebra discriminant is
`kappa F`, with `kappa in C^*` and multiplicity one.

Write the cubic algebra as `B=R direct-sum E`, where `E=ker(Tr)`.
Quillen--Suslin makes `E` free, but supplies no algebra generator.  In a
trace-zero basis Miranda's datum is the binary cubic

```text
I(S,T)=bS^3-3aS^2T+3dST^2-cT^3,                     (2.3)
D=b^2c^2-3a^2d^2+4a^3c+4bd^3-6abcd,                 (2.4)
disc(I)=-27D=-27kappa F.
```

Miranda's classification permits arbitrary four polynomial coefficients;
associativity imposes no further coefficient equation.  For
`theta=sz+tw`, the exact index identity is

```text
det_R(1,theta,theta^2)=I(s,t).                        (2.5)
```

Therefore `B` has a power basis exactly when
`I(R^2) intersect C^*` is nonempty.  Since every complex unit has a cube
root, this is equivalent to an `R`-point of `I(S,T)=1`.  Polynomial
`GL_2(R)` changes of the trace-zero basis act by the charged twisted action
and preserve this condition.  They can change coefficient degrees and pole
orders drastically, so raw orders of `(a,b,c,d)` are not intrinsic data.

## 3. Four-coefficient discriminant at infinity

There are two relevant strata of the discriminant hypersurface in the
four-dimensional coefficient space.  At a form with exactly one double root
the hypersurface is smooth.  For example, at
`(a,b,c,d)=(1,0,0,0)`, one has `partial D/partial c=4`.  Consequently its
pullback can be **any** plane-curve germ.  More strongly, for every
polynomial `G`,

```text
(a,b,c,d)=(1,0,G/4,0)  gives  D=G.                    (3.1)
```

Taking `G=kappa F` realizes the entire charged sextic, including its three
nodes and infinity germ, in the raw four-coefficient identity.  This datum
has a linear factor
`I=-T(3S^2+(G/4)T^2)`, so it is not a connected generic cubic field and is
not an element of the charged residual.  It nevertheless proves that the
curve geometry alone cannot contradict (2.4).

The triple-root stratum gives the exact invariant order calculation.  On
the chart where `b` is a unit, put

```text
p=bd-a^2,        q=2a^3-3abd+b^2c.                    (3.2)
```

Direct expansion, with no change to depressed global form, gives

```text
b^2D=q^2+4p^3.                                        (3.3)
```

Moreover `det(partial(p,q)/partial(d,c))=b^3`, so `(a,b,p,q)` are etale
coordinates.  The triple-root locus is `p=q=0`; its transverse
discriminant is exactly the cusp in (3.3).  If `q` is a local parameter and
`k=ord_v(p|_{q=0})`, its Newton initial form is
`q^2+gamma v^(3k)`.  It is one branch of type `(2,3k)` precisely when `k`
is odd.  Hence the charged type `(2,15)` asks for

```text
k=5,                                                   (3.4)
```

and order `5` is allowed, not excluded.

Indeed, in the coordinates of (2.1), take

```text
(a,b,c,d)=(0,1,w,v^5).
```

Then `p=v^5`, `q=w`, and

```text
D=w^2+4v^15.                                          (3.5)
```

Its normalization is `v=s^2`, `w=2i s^15`; it has one place and delta
`7`.  With `nu(v)=2`, `nu(w)=15`, the coefficient vector in the order
`(a,b,c,d)` is

```text
(+infinity,0,15,10),                                  (3.6)
```

and the two surviving discriminant terms both have weight `30`.

Raw coefficient vectors do not classify the germ.  For a series `A` of
weight `lambda`, the translated cube-locus family

```text
a=A,  b=1,  d=A^2+v^5,  c=A^3+3Av^5+w                (3.7)
```

still has `p=v^5`, `q=w` and the same discriminant.  Without accidental
coefficient cancellation its order vectors are

```text
0<=lambda<5:  (lambda,0,3lambda,2lambda),
lambda=5:     (5,0,15,10),
lambda>5:     (lambda,0,15,10).                       (3.8)
```

For a unit `A`, all four raw coefficients have order zero.  When
`lambda<5`, the five low-weight monomials in (2.4) cancel because their
leading form lies on the translated triple-root locus; the first transverse
invariant occurs at weight `30`.  At equality further cancellations can
raise individual raw orders.  Polynomial unimodular shears and interchange
of `S,T` supply still more vectors.

For reference, if `alpha=nu(a)`, `beta=nu(b)`, `gamma=nu(c)`, and
`delta=nu(d)`, the five raw term orders are

```text
2beta+2gamma,  2alpha+2delta,  3alpha+gamma,
beta+3delta,   alpha+beta+gamma+delta.                 (3.9)
```

Having the minimum attained at least twice is only a tropical necessary
condition along `D=0`; leading coefficients and transverse jets decide the
germ.  The smooth-stratum example (3.1) also shows that restriction of the
coefficients to the normalization can forget the transverse germ entirely.
Thus there is no finite, invariant list of four raw orders.

Even local connectedness and normality do not remove (3.5).  The associated
monogenic algebra

```text
C[[v,w]][z]/(z^3+3v^5z-w)
```

is `C[[v,z]]` after eliminating `w`, hence regular and a domain.  Its generic
cubic is irreducible: at the `v`-adic DVR it reduces to `z^3-w` over
`C((w))`, irreducible because the `w`-valuation of `w` is not divisible by
three.  Its nonsquare discriminant gives generic group `S_3`.  This is a
local model, and it is monogenic; it does not contradict the charged global
no-go.  It proves that no argument using only this local discriminant jet,
connectedness, normality, and generic `S_3` can supply that no-go.  Neither
this model nor (3.5) is shown to globalize over `C[x,y]` with branch `F` or
to admit the charged `S_4` lift.

The charged list `{2,3,4,6}` used the global bounds on a *selected depressed
generator*, whose homogenized coefficients had degrees two and three.
Those bounds forced a short Taylor template.  In an unrestricted local
Miranda jet `p` in (3.2) has no such bound, and `p=v^5` is legitimate.
Therefore the global four-coefficient bypass remains OPEN: a successful
exclusion would have to control global polynomial pole lattices,
cancellation, and charged compatibility, not merely the local invariant
hypersurface.

## 4. Unit representation and non-monogenic cubic algebras

The hoped-for implication from a trivial Tschirnhausen bundle and
separability off the branch is false.  A desk-checkable countermodel over
`R=C[x,y]` is

```text
I=xS^3-3S^2T+3ST^2+y^2T^3.                            (4.1)
```

Here `(a,b,c,d)=(1,x,-y^2,1)`, and direct substitution into (2.4) gives

```text
D=G=x^2y^4+6xy^2+4x-4y^2-3,
disc(I)=-27G.                                         (4.2)
```

The sextic `G` is irreducible.  Over `K=C(x)`, put

```text
P(Y)=x^2Y^2+(6x-4)Y+4x-3,
```

so `G=P(y^2)`.  The `Y`-discriminant is `16(1-x)^3`, hence `P` is
irreducible in `K[Y]`.  If the monic even quartic obtained from `P(y^2)`
factored, comparison in
`(y^2+alpha y+beta)(y^2-alpha y+delta)` would say either that `P` splits,
or that `(4x-3)/x^2` is a square in `K`.  Its valuation at `4x-3` is one,
so the latter is impossible.  Gauss's lemma proves irreducibility in
`C[x,y]`; in particular the discriminant divisor is reduced and squarefree.

Nevertheless (4.1) represents no unit.  Give `x,y` weights `2,1`.  For
nonzero `s,t` of top weighted degrees `p,q`, the four term weights of
`I(s,t)` are

```text
2+3p,       2p+q,       p+2q,       2+3q.             (4.3)
```

If `p>q`, the first is uniquely largest; if `q>p`, the last is.  If `p=q`,
the top part is `x s_p^3+y^2 t_p^3`.  Its cancellation would make
`(s_p/t_p)^3=-y^2/x`, impossible because the `x`-valuation of the right
side is `-1`.  The cases with one of `s,t` zero are immediate.  Thus

```text
I(R^2) intersect C^* is empty.                         (4.4)
```

This is not caused by a defective algebra.  Miranda's multiplication table
gives a free cubic algebra whose selected element has polynomial

```text
Z^3+3(x-1)Z+(3x-2+x^2y^2).                            (4.5)
```

It is irreducible: viewed as a quadratic in `y` over `C(x,Z)`, reducibility
would make the negative of its odd-`Z`-degree remainder a square.  Hence the
algebra is a domain.  Its selected-polynomial discriminant is `-27x^2G`,
consistent with index `I(1,0)=x` and algebra discriminant `-27G`.
Freeness over the regular ring gives `S_2`; away from `(G)` it is etale,
while at `(G)` the discriminant valuation is one, so the DVR
index-discriminant formula makes the order maximal.  It is therefore
normal.  Since `G` is nonsquare, the generic group is `S_3`.

The failure is genuinely global.  At every maximal ideal the reduction of
`I` is a nonzero binary cubic (the middle coefficients are nonzero
constants).  Some constant residue vector has nonzero value, which lifts to
a local-unit index; the algebra is locally monogenic everywhere.  It still
has no global power basis by (4.4).

The obstruction has a precise geometric home, but the example does not
separate all its layers.  Let

```text
U_I={I(S,T)=1} subset A^2_{S,T} over Spec R.           (4.6)
```

An `R`-section is exactly a normalized unit representation.  Euler's
identity prevents both relative partial derivatives from vanishing on
`I=1`, so `U_I` is relatively smooth; it is fiberwise nonempty, and the
complement of `I=0` has local generator sections.  Triviality of `E` only
provides the global coordinates `S,T`; it does not provide a section of
this nonlinear complement.

Projectively, `W^3=I(S,T)` is, away from `G=0`, a smooth genus-one family,
with the degree-three boundary `W=0`.  Its generic fiber defines a
period-dividing-three torsor under its Jacobian.  Unit representation asks
for more than vanishing of a possible generic torsor class: the point must
be integral over all of `A^2` and avoid the boundary.  The weighted-degree
argument proves the combined failure only; whether its obstruction is
already generic or occurs in extension/boundary avoidance is left OPEN.

Finally, this countermodel is not in the charged row.  Its affine branch has
two `A_2` cusps at `(1, i)` and `(1,-i)`, not three nodes.  Its degree-six
homogenization meets infinity at both `[1:0:0]` and `[0:1:0]`, not at one
place, and no compatible charged `S_4` lift is supplied.  Thus (4.1)
refutes every inference based only on UFD, freeness, local monogenicity,
normality, squarefree sextic branch, and generic `S_3`; it proves neither
emptiness nor nonemptiness of the row-specific class.

## 5. Assembly: what is killed and what survives

Fix a sextic `F` with the provisional geometry in section 2, and let
`C_F^adm` be the set of actual surjections
`phi:pi_1(A^2-V(F))->S_4` which take smooth meridians to transpositions,
take the two branch meridians at every node to commuting transpositions,
and satisfy all global peripheral relations, including the `(6,4)` cable
relation at infinity.  In braid-tuple language, the tuple itself must be
fixed by that infinity braid.  Attainment of the curve geometry does not
attain such a tuple.

The exact surviving logical subclass is

```text
R_{F,S4}^nm = {
  (phi,[I]_*):
    phi in C_F^adm,
    I=bS^3-3aS^2T+3dST^2-cT^3 over R,
    B_I isomorphic over R to B_{q o phi},
    disc(I)=-27 kappa F for some kappa in C^*,
    B_I is a normal domain,
    I(R^2) intersect C^* is empty
}.                                                        (5.1)
```

Here `[I]_*` is the twisted `GL_2(R)` orbit, not a chosen coefficient
vector.  Compatibility with `q o phi` entails more than the displayed
discriminant: the generic group is `S_3`, the cover is connected and
finite-flat, the branch is reduced with multiplicity one, and the smooth
and nodal completed algebras are exactly (2.2).  Normal-domain status is
therefore redundant in (5.1), but is retained to make the ambient
countermodel boundary explicit.

No raw coefficient degree or infinity-order condition follows from the
present data alone.  Such vectors vary under polynomial basis shears.  If a regular
coefficient chart approaches the triple-root stratum, (3.2)--(3.5) show
that transverse order `5` is admissible; if it approaches the smooth
double-root stratum, the discriminant is itself a transverse coordinate.
The actual affine datum may instead have poles after compactification and
high-order cancellations.  None of these cases has been globally excluded.

The charged monogenic theorem still gives the complementary half of a
dichotomy.  If `I(s,t)` is a unit, the corresponding element is a global
generator.  The charged one-place cancellation argument then proves the
depressed coefficient bounds, and the bounded infinity calculation gives
orders `{2,3,4,6}` rather than the required `5` (the independent affine
node/Bezout contradiction is also available).  Hence every hypothetical
charged `phi` must contribute an element of (5.1).  Conversely, emptiness of
(5.1), for every provisional row curve in scope, would complete the uniform
kill.  This report proves no such emptiness theorem.

The `S_4` lift itself supplies no distinguished element of the cubic
algebra in the charged construction.  The fact that monogenization is
additional data in general resolvent parametrizations is also visible in
primary structure theory:
Wood's Theorem 1.1 parametrizes quartic rings with a *monogenized* cubic
resolvent by binary quartic forms, whereas her recalled Theorem 1.2
parametrizes all quartic rings with cubic resolvents by pairs of ternary
quadratic forms.  Her arbitrary-base Theorem 1.1 gives the latter
parametrization over a scheme.  These theorems supply no formal generator;
they do not prove that an `S_4` resolvent satisfying this row's normality,
branch, and peripheral conditions can be nonmonogenic, and do not decide
(5.1).

The status is therefore:

| assertion | status |
|---|---|
| purely local four-coefficient invariant forbids order `5` | **REFUTED**, by (3.5) |
| global polynomial, charged four-coefficient bypass | **OPEN** |
| squarefree branch + free trace-zero bundle forces a unit value | **REFUTED**, by (4.1)--(4.4) |
| charged monogenic resolvent exists | **KILLED**, conditional on the provisional row data |
| an element of (5.1) exists | **OPEN** |
| (5.1) is empty / the `(6,4)` row is uniformly killed | **OPEN** |

The coordinator's explicit three-node curve witnesses only the geometric
row.  The fixed `S_4` tuple remains unproved.  Likewise, no `(8,4)`
representation is obtained by target equivalence without transporting its
full peripheral data.  These are floor/attainment and target/arrival
distinctions, not cosmetic qualifications.

## 6. Sources and audit notes

The frozen `TRIPLE-COVER-CLOSE` source supplies the index criterion and
Miranda conventions at lines 26--85, the audited broad countermodel at
88--155, the prior four-coefficient stopping point at 157--209, and the
conditional theorem/exact residual at 358--448.  Frozen
`TRIPLE-COVER-r2` lines 35--84 give the quotient cover and completed local
models; lines 86--165 give the four-coefficient datum; lines 224--365 are
the bounded-degree infinity and node contradictions.  Coordinator lines
70--92 type the row result as provisional and distinguish the attained
curve from the missing fixed tuple.  These are citations to the frozen
copies named and hashed in section 1.

Primary triple-cover source, streamed and hashed without saving a file on
2026-08-31:

* Rick Miranda, “Triple Covers in Algebraic Geometry,” *American Journal of
  Mathematics* 107 (1985), 1123--1158, DOI `10.2307/2374349`.
  `https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf`,
  SHA-256
  `0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875`.
  The charged use is Theorem 2.7.1/Remark 2.8.1, Proposition 3.3 and (3.4),
  Theorem 3.6/Definition 3.7, and Lemma 4.5/Proposition 4.7.

Primary sources for the distinction between arbitrary cubic resolvents and
monogenized ones, likewise streamed and hashed without saving:

* Melanie Matchett Wood, “Quartic Rings Associated to Binary Quartic
  Forms,” *IMRN* 2012(6), 1300--1320, DOI `10.1093/imrn/rnr070`,
  `https://arxiv.org/pdf/1007.5501`, SHA-256
  `043b681e2aabae78bc16e6e04e880514eb3ecabbec5f4e4a97739a981977bc2b`.
* Melanie Matchett Wood, “Parametrizing quartic algebras over an arbitrary
  base,” `https://arxiv.org/pdf/1007.5503`, SHA-256
  `b28a5d3f41cede2517f46fe26a97b60bce60318c77a6b17474b381c434317841`.

Equations (3.1)--(3.9), the irreducibility check in section 4, and the
weighted no-unit proof are direct calculations in the declared rings; no
classification theorem or computation is hidden in them.  The final audit
keeps the physical infinity point, normalization place, Puiseux parameter,
and cover monodromy separate; treats geometric attainment as no more than
geometric attainment; and makes no transfer to `(8,4)`.  No canonical
ledger was edited, `jc2-lean` was not inspected, and no CAS or
uncertain-duration computation was run.

<!-- BODY-END -->
