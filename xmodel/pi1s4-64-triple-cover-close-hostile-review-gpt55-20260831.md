# Hostile Review: Triple-Cover-Close Report (Sol)

## 0. Hash And Source Controls

## 1. Monogenicity And Consequence (1.4)

## 2. Unit-Representation Criterion And UFD Obstruction

## 3. Davenport/Mason Machinery And Band Analysis

## 4. Specialization, Extremals, And (5.3)-(5.5)

## 5. Assembly And R2 Scope Consumption

## 6. Residual Class (7.1) And Fixed-Tuple Avoidance

## 7. Verdicts And Promotion Recommendation

---

## 0. Hash And Source Controls

Input hash verification passed before reading the frozen copies:

```text
140215427ecc2fe5ba9a176aa53ede5a6d07c0e697e6d99be3541f30044bb002  pi1s4-64-triple-cover-close-sol56-20260831.md
c99ffc7f64562ac08e81aa7e927dc04e8c0765182d99db9fdc9f10351772cf9f  pi1s4-64-triple-cover-r2-sol56-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

The close report's mathematical scope is as stated at lines 19--24 and
360--368: conditional on the provisional `(6,4)` row geometry and on an
actual globally monogenic cubic resolvent. The coordinator still labels the
row-sweep data provisional and leaves `(6,4)` OPEN at lines 70--91. The r2
report supplies the resolvent cover, normality/flatness, and reduced
discriminant at lines 35--84, but explicitly stops before a global power basis
at lines 86--165 and 367--388.

Primary/source streams reopened and hashed on 2026-08-31, no source file saved:

```text
0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875  https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf
b629733a8c7c64007110e06e5ffc73212eb4b87bcbd6dbcf5416cac485c51a2d  https://matwbn.icm.edu.pl/ksiazki/aa/aa71/aa7122.pdf
0ff263ee1baf3d54a18be83616784a262a1888df80e1470b7096a211b1cb7d91  https://matwbn.icm.edu.pl/ksiazki/aa/aa74/aa7447.pdf
012e63dbe3d95a8caae8482354042e8c150509f35ef3b6c66a1ccc28fe707446  https://content.ems.press/assets/public/full-texts/serials/em/55/3/609/online/10.1007-s000170050074.pdf
467701925109586976ca8f89ec614ee95c5ad740084b969a93ba3795b0cdb740  https://rikkyo.repo.nii.ac.jp/record/8708/files/AA00610867_54-01_04.pdf
```

Miranda was checked for the triple-cover data, index/discriminant form, and
branch divisor statements used in close sections 1--3. Snyder's proof gives exactly
the polynomial Mason inequality `deg c <= n0(abc)-1` for coprime one-variable
polynomials. Zannier section 5/Proposition 2 and Shioda sections 2--5 confirm that equality
in Davenport's `deg(f^3-g^2) >= n+1` is the DS/Belyi/weighted-tree extremal
case, and Shioda records `St(5)=4` plus the order-five examples. I did not
attribute content to inaccessible original Davenport/Stothers/Mason texts.

## 1. Monogenicity And Consequence (1.4)

Verdict: **CONFIRMED at conditional scope**.

Let `R=C[x,y]` and `B=pi_*O_X`. Since `3` is invertible, translation by
`Tr(theta)/3` moves any generator into the trace-zero summand
`E=ker(Tr)`. Quillen-Suslin makes `E` free, so Miranda's construction gives
a binary cubic index form

```text
I(S,T)=B0 S^3 - 3A0 S^2T + 3D0 ST^2 - C0 T^3.
```

For `theta=sz+tw`, Miranda's multiplication table gives
`det(1,theta,theta^2)=I(s,t)`. Hence `theta` is a global power-basis
generator iff this determinant is a unit. The close report's criterion

```text
B monogenic over R  iff  I(s,t) in C^* for some s,t in R
```

is the correct one. The extra sentence that a unit value forces `(s,t)` to be
unimodular is also correct: if a maximal ideal contained both `s,t`, the
homogeneous cubic value would vanish modulo that ideal. A unimodular column
extends to `GL_2(R)`, so this is equivalent to putting a unit in the selected
`S^3` coefficient after a basis change.

The claimed consequence (1.4) also follows, with only sign/constant
normalization hidden in `kappa`. A monogenic cubic algebra is
`R[Z]/(Z^3+aZ+b)` after trace depression, and its algebra discriminant is a
nonzero scalar multiple of `4a^3+27b^2`. The r2 report gives the resolvent
discriminant divisor as `kappa F` with multiplicity one at lines 73--84.
Thus (1.4) is valid exactly under the additional global-monogenicity
hypothesis. It is not an unconditional reduction from a free
Tschirnhausen module to a depressed cubic.

The close report correctly refutes the earlier "linear factor/power basis"
replacement: a projective section through the bad-generator cubic divisor is
not a section avoiding it. The surviving problem is unit representation by
the index form, not projective-module freeness or factorization.

## 2. Unit-Representation Criterion And UFD Obstruction

Verdict: **CONFIRMED as a genuine obstruction; not a row counterexample**.

For

```text
I=xS^3-3S^2T+3ST^2+y^2T^3,
```

the Miranda branch polynomial is

```text
G=x^2y^4+6xy^2+4x-4y^2-3.
```

Re-derivation: with `Y=y^2`, this is
`x^2Y^2+(6x-4)Y+4x-3`; its discriminant over `C(x)` is
`16(1-x)^3`, not a square. If substituting `Y=y^2` made a factorization over
`C(x)`, then either the quadratic in `Y` already split, or the constant/leading
ratio `(4x-3)/x^2` would be a square. Neither condition holds. Since the
coefficients are primitive in `C[x]`, `G` is irreducible in `C[x,y]`, and the
sextic is reduced.

The no-unit argument is also correct. Use weights `wt(x)=2`, `wt(y)=1`. If
`s,t` are nonzero with weighted top parts of degrees `p,q`, then for `p>q`
the unique leading term of `I(s,t)` is `x s_p^3`; for `q>p` it is
`y^2 t_q^3`; and for `p=q` the leading part is
`x s_p^3+y^2t_p^3`, which cannot vanish because `-y^2/x` has `x`-valuation
`-1`, not divisible by `3`, in `C(x,y)^*`. The cases `s=0` or `t=0` are
immediate. Thus `I(R^2)` contains no nonzero constant.

Local monogenicity does not rescue the global statement. Modulo any maximal
ideal, the form is not the zero cubic because the middle coefficients are
nonzero constants; over the infinite residue field some vector has nonzero
value, making the determinant a local unit. Normality is plausible and
sufficiently justified for this use: the free finite algebra over the regular
surface is `S_2`; away from `G` it is etale; and at `(G)` the discriminant
valuation is one, so the DVR order is maximal.

This refutes any attempted theorem "UFD + free + locally monogenic + normal
connected cubic + irreducible reduced sextic branch implies power basis." It
does not refute the charged row, because its projective closure has two
infinity points (`X^2Y^4=0`), not the charged one-place `(2,15)` infinity
germ.

## 3. Davenport/Mason Machinery And Band Analysis

Verdict: **CONFIRMED; the generic-line dichotomy is refuted as stated**.

Assume a global depressed power basis has already been obtained and write,
after absorbing constants,

```text
A^3-B^2=F,      deg F=6.
```

If top terms do not cancel, then `deg A<=2` and `deg B<=3`. If either bound
fails, the top degrees must satisfy `3 deg A = 2 deg B`, so

```text
deg A=2k,      deg B=3k,      k>=2.
```

Now restrict to a generic affine line. The leading homogeneous parts of
`A,B,F` vanish on only finitely many directions, so a nonempty open set of
directions preserves all three degrees. A further open condition makes the
line transverse to the reduced sextic and avoids the three nodes, so
`H=F|ell` has degree six with six simple zeros.

The gcd condition is not missing. If `A(p)=B(p)=0`, then `F(p)=0`; at such a
point the quadratic tangent cone of `A^3-B^2` is either a square or the
multiplicity is at least three, never an ordinary node. Since the row has only
ordinary affine nodes and no other affine singularities, `V(A,B)` is empty.
Then `V(A,F)` and `V(B,F)` are empty too, because on `F=0` one has
`B^2=A^3`. Thus the specialized one-variable polynomials `P,Q,H` are
pairwise coprime on the same generic-line open set.

Mason applied to `P^3-Q^2-H=0` gives

```text
6k <= deg rad(PQH)-1 <= 2k+3k+6-1,
```

hence `k<=5`. This leaves exactly four high-cancellation bands:

```text
(deg A,deg B)=(4,6),(6,9),(8,12),(10,15).
```

Only the last is a Davenport-Stothers equality case: Davenport's bound is
`deg(P^3-Q^2) >= k+1`, and here `deg H=6`, so equality holds only at `k=5`.
Zannier's Proposition 2 classifies equality cases by weighted trees; Shioda
defines DS triples by `deg f=2m`, `deg g=3m`, `deg h=m+1`, records
`St(5)=4`, and displays the order-five examples. None of that classifies the
nonextremal `k=2,3,4` bands. Therefore the old "low degree or extremal"
dichotomy was false; the close report correctly repairs it by retaining all
four bands until the two-variable row argument kills them.

## 4. Specialization, Extremals, And (5.3)-(5.5)

Verdict: **CONFIRMED; no cancellation residual remains in the monogenic
case**.

Let `C=V(F)`. The previous gcd check implies that the images of `A` and `B`
have no zeros in the affine coordinate ring `O(C)`, hence are units. On `C`,
`B^2=A^3`. Therefore

```text
t=B/A,      t^2=A,      t^3=B.                         (5.1)
```

The row has one point over infinity on the projective normalization. Since
`t` is a unit on the affine curve, the divisor of its pullback is supported at
that single point; a principal divisor has degree zero, so the coefficient at
that point is zero. Thus `t` extends as a nowhere-zero regular function on the
projective normalization and is constant. Hence `A=c^2` and `B=c^3` modulo
`F`, so

```text
A=c^2+FP,      B=c^3+FQ.
```

It follows immediately that `F | J(A,B)`: differentiate these congruences, and
every term in `dA wedge dB` has a factor `F`.

Now assume a high-cancellation band, so `deg A=2k`, `deg B=3k`, `2<=k<=5`.
Define

```text
omega=2A dB - 3B dA.                                  (5.3)
```

The identities in (5.4) are exact. First, from `F=A^3-B^2`,

```text
dF=3A^2 dA - 2B dB.
```

Then

```text
B omega = 2AB dB - 3B^2 dA
        = 2AB dB - 3(A^3-F)dA
        = -A(3A^2 dA - 2B dB) + 3F dA
        = 3F dA - A dF.
```

Second,

```text
d omega = d(2A dB)-d(3B dA)
        = 2 dA wedge dB - 3 dB wedge dA
        = 5 dA wedge dB.
```

The coefficients of `3F dA-A dF` have degree at most `2k+5`. Since
`deg B=3k`, each nonzero coefficient of `omega` has degree at most
`(2k+5)-3k=5-k`. If `omega=0`, then `J(A,B)=0` from `d omega=0`. If
`omega != 0` and `k<=4`, then `d omega=5J(A,B) dx wedge dy` has degree at
most `4-k<6`. If `k=5`, the coefficients of `omega` are constant, hence
`d omega=0` and again `J(A,B)=0`. Because `F` is irreducible of degree six
and divides `J(A,B)`, all cases force

```text
J(A,B)=0.                                             (5.5)
```

Over characteristic zero, `J(A,B)=0` implies algebraic dependence. The
polynomial Luroth theorem then gives `A=U(r)`, `B=V(r)` for some
`r in C[x,y]`. The proof sketched in the close report is acceptable:
normalize `C[A,B]` in its function field; a general line gives a nonconstant
map from `P^1` to the smooth projective model, forcing genus zero; the
normalization embeds in `C[x,y]`, so its units are constants, hence it is
`C[r]`. Then `F=A^3-B^2=W(r)`. Since `C` is algebraically closed and `F` is
irreducible, `W` is linear. Thus `r` is affine in `F`, and `A,B in C[F]`.
Positive degrees in `C[F]` are multiples of six, but none of
`(4,6),(6,9),(8,12),(10,15)` has both degrees divisible by six.

This eliminates the three nonextremal bands and the order-five
Stothers-Zannier extremal band. Linewise DS normalizations do not need to be
promoted to a fixed two-variable family; the global Jacobian argument excludes
the entire high-cancellation regime.

## 5. Assembly And R2 Scope Consumption

Verdict: **CONFIRMED as a conditional monogenic-resolvent no-go**.

The assembly in close section 6 consumes r2 at the right scopes. The unconditional
part from r2 is only this: a charged `S4` representation, after quotienting
by the Klein four subgroup, gives a connected finite-flat normal triple cover
with discriminant divisor `kappa F` and simple branch multiplicity along the
row curve. This is r2 lines 35--84. It does not include a power basis.

The close report then adds one extra hypothesis: the resolvent cubic algebra
is globally monogenic. By section 1 of this review, that gives a depressed equation
`Z^3+aZ+b` and `4a^3+27b^2=kappa F`. By sections 3--4, the high-cancellation bands
are impossible for an irreducible one-place sextic with only ordinary affine
nodes. Therefore the missing r2 high-degree-cancellation premise is replaced
by a proof, yielding `deg a<=2`, `deg b<=3`.

Only after that replacement does r2's bounded-cubic analysis apply. The
leading-form/infinity contradiction at r2 lines 167--270 has exactly that
premise and rules out the charged one-place `(2,15)` germ, since its local
table allows orders `2,3,4,6` but the row requires `5`. The independent
affine-node/Bezout contradiction at r2 lines 272--365 also has exactly that
premise and forces the coefficient `a` to be constant, after which the sextic
factors over `C`.

Thus the promoted theorem should be phrased narrowly:

```text
No hypothetical charged (6,4) S4 representation with the provisional row
geometry can have a globally monogenic S3 resolvent.
```

The theorem does not say that no charged `S4` representation exists. It says
any such representation must have a nonmonogenic resolvent, unless the
provisional row data later fail.

## 6. Residual Class (7.1) And Fixed-Tuple Avoidance

Verdict: **CONFIRMED; (7.1) is the right residual cage**.

The residual class must remember five pieces of data, and close (7.1) does:
the charged `S4` representation `phi`, the twisted `GL2(R)` orbit of the
Miranda index form, compatibility with the actual quotient resolvent
`B_{q o phi}`, the reduced branch discriminant, normal connected algebra
behavior, and failure of unit representation. The compatibility condition is
not cosmetic: a random nonmonogenic Miranda cubic with branch `F` need not
come from the quotient of a charged `S4` cover.

The twisted action is the correct one. Changing a basis of the trace-zero
rank-two module transforms the binary cubic index form by the determinant
twist; using an untwisted orbit would confuse a coordinate change with a
different cubic algebra. The discriminant condition
`disc(I)=-27 kappa F` is also the right invariant normalization up to the
fixed Miranda scalar. The condition `B_I is a normal domain` packages
connectedness and normality; compatibility with `B_{q o phi}` then imports
the local smooth-branch and node models from r2.

The unit condition is exact:

```text
I(R^2) cap C^* = empty.
```

If a unit value existed, homogeneity and the fact that every complex unit has
a cube root would rescale it to `I=1`, giving a global generator and triggering
the monogenic contradiction. If no unit value exists, Quillen-Suslin freeness
has not been contradicted; the UFD example in section 2 shows that this situation is
real in nearby geometry.

The fixed-tuple gate's refuted global-cubic move is avoided. Close sections 1--3
explicitly reject "free implies power basis" and the direct four-coefficient
bypass; close section 6 states the theorem only for globally monogenic resolvents;
close section 7 leaves row-specific global monogenicity OPEN. I found no place where
the report charges a fixed tuple, physical curve position, and cover series
as if they were the same object. No exit-price assertion is made.

## 7. Verdicts And Promotion Recommendation

Overall verdict: **CONFIRM-AS-SCOPED**. The hostile default does not find a
mathematical refutation of the close report's revised claims, provided the
word "conditional" remains attached to the monogenic-resolvent theorem and
the row data remain provisional.

| item | verdict |
|---|---|
| section 1 monogenicity formulation | **CONFIRMED**: unit representation by the Miranda index form is the exact criterion. |
| consequence (1.4) | **CONFIRMED conditional on global monogenicity** and r2's reduced discriminant. |
| Quillen-Suslin freeness implies power basis | **REFUTED**. Freeness supplies the variables, not a unit value. |
| UFD obstruction example | **CONFIRMED** as a genuine free/local/normal/no-unit obstruction, but not row-shaped. |
| direct four-coefficient bypass | **OPEN**; close correctly does not promote it. |
| generic-line "low degree or extremal" dichotomy | **REFUTED as stated**: Mason leaves four bands. |
| three nonextremal bands | **KILLED** by the row-specific global Jacobian argument. |
| order-five Stothers-Zannier extremal band | **KILLED** by the same (5.3)--(5.5) argument. |
| section 6 r2 consumption | **CONFIRMED**: r2 is used only after monogenicity plus the new cancellation lemma provide bounded degree. |
| residual class (7.1) | **CONFIRMED exact**: twisted action, quotient compatibility, normal domain, discriminant, and no-unit condition are all needed. |
| row-specific global monogenicity | **OPEN**. |
| unconditional kill of `(6,4)` | **OPEN**. |
| fixed-tuple/global-cubic gate hazards | **AVOIDED** in this close report. |

Promotion recommendation:

```text
PROMOTE: refutation of freeness-implies-power-basis.
PROMOTE: refutation of the generic-line low-or-extremal dichotomy.
PROMOTE: row-specific high-cancellation exclusion for monogenic depressed
         cubics with the stated irreducible one-place/nodal sextic geometry.
PROMOTE: conditional monogenic-resolvent no-go for the provisional (6,4) row.
DO NOT PROMOTE: unconditional row kill, row-specific global monogenicity, or
                direct four-coefficient Miranda exhaustion.
KEEP OPEN: exact nonmonogenic S4-resolvent residual class (7.1).
```

Minor clerical note: the close report's own receipt block records hashes for
r2, a fixed-tuple review, and the coordinator, not the current three frozen
inputs including the close report itself. This review verified the current
prompt's three hashes in section 0; the clerical mismatch is not a mathematical
defect.

<!-- BODY-END -->
