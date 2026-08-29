# Hostile review — generic affine-Faber complete-local `J` exclusion

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md` |
| Target SHA-256 | `fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim; Section 7 is an undischarged import gate, not a hidden extra hypothesis of (0.1)–(5.2) |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged artifacts were opened only because they are named; no producer status line, no `PASS` token, no modular factorization, and no charged `CONFIRMED` string is evidence |
| Method | SHA-256 of the target, both charged manifests, and every named support/source pin; independent triangular inversion; involution/parity; inverse-root series of `w=Q^{1/4}`; logarithmic-differentiation recurrence for `g^alpha`; first-variation calculus of `H=F^{5/4}+beta F^{3/4}+gamma F^{1/4}` including the polynomial-part correction; formal implicit-function theorem in the completed local ring; V1/V2 source diff. Producer Singular stdout was read only as custody, never as a derivation of (4.3) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1`,
matching the required pin. Every path in the charged `EVIDENCE.sha256` and
`FREEZE.sha256` rehashes to the printed digest. Every support/source pin
named in target §1 rehashes to the printed digest. Producer verdict
language, the target's own status line, both `PASS_GENERIC_J_EXCLUSION_DATA`
tokens, the printed `factorize(detJac)` strings, and characteristic 65521
were not used as algebraic evidence. No file other than this review was
written.

---

## Verdict

**CONFIRMED.**

In the centered monic octic chart the square-division map `F=Q^2+N` is a
polynomial automorphism with Jacobian determinant `8`. The unit change
`u=n1-(p/2)n3` makes `(c,u,n3)` a basis of every odd coefficient
direction in that chart. The moving-center coefficient of `z^7` is a
further odd direction; it is absent from the charged ordinary tails and
is not assumed away. It remains an import obligation, exactly as Section 7
states.

Ordinary Faber rows are the inverse-root coefficients of
`(H-[H]_+)(z(w))` with `w=F^{1/8}` and
`H=F^{5/4}+beta F^{3/4}+gamma F^{1/4}` (the `F^{3/2}` summand contributes
`w^{12}` on the exact square and has vanishing first square-normal
variation). Odd rows are odd in `(c,u,n3)`, even rows are even, and
therefore `R1=R3=R5=R7=0` whenever the odd coordinates vanish, for
arbitrary even coefficients, loads, even targets, and nilpotent/formal
even jets.

On the corrected affine-Faber graph the Jacobian of `(R1,R3,R5)` in
`(c,u,n3)` is the displayed block (4.3). Its determinant is the
polynomial identity

```text
-q0 K0^2 / 16 = -25 D^3 (5D+2s) (5D-2s)^2 / 2^{17},
```

with no missing factor. The block is invertible precisely on (0.1). In
the completed ordinary-Faber coefficient/load/target ring at a point of
the graph in `U`, the formal implicit-function theorem gives
`(R1,R3,R5)=(c,u,n3)` as ideals. Parity puts `R7` in `(c,u,n3)`, so
`R7=0` and, after the source tie `J-4 R7`, one has `J=0`. The saturation
`((R1,R3,R5,J-4 R7):J^infinity)` is the unit ideal of that completion.
Nilpotent thickenings and ramified formal arcs with closed point on `U`
and generic point `J != 0` do not exist. Attempted counterexamples
(Artinian odd jets, Puiseux ramification of the even parameters) are
killed by invertibility of `d_O Phi`.

On the `A`-face the block has rank two and kernel the `c`-direction; on
the `K`-face it has rank one with kernel basis (6.4). Every first-order
kernel vector is `R7`-null. The raw identities (6.1) and (6.3) hold on
the exact square before radical or saturation. The two faces are disjoint
on `D(D)`. Neither face is classified.

This is a characteristic-zero complete-local statement in the
**normalized ordinary-Faber coefficient completion** on (0.1), with
`k10=1` and centered octic coordinates. Section 7 is not discharged. The
theorem is not a total-Rees, terminal, Taylor, order-two, `(8,12)`,
maximum-twelve, or JC2 result.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md` | `fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1` | target (matches required pin) |
| `cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/RESULT.md` | `a9cb98448d0ff6bdd13120966c870cfc3be95c54bb3a7d67ac80e975e1fd3cc2` | named producer result; opened because charged; its `PASS` token is not evidence |
| `cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/EVIDENCE.sha256` | `ec59a48c4d121ec43b0cc43f36edd3b5da2d7f76bef86447b12201a3f4862093` | named evidence list; every listed file rehashes |
| `cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/FREEZE.sha256` | `149ae5131ccbeccfeea6b86151471703bb4620cc1e4c0a56d6d0b1ea21f2800d` | named freeze list; every listed file rehashes |
| `cases/max12_812_order2_exact_square_faber_generic_j_exclusion_20260826/compile_generic_j_exclusion.py` | `0098b72df237d5f32490ab41c14db8503156280c47948729ced31d4137495e11` | named compiler; source-fidelity and V1/V2 parenthesization only |
| `xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md` | `77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e` | corrected affine-Faber graph (3.1), connections (1.4), two-pivot (5.3), raw (6.3) |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/RESULT.md` | `86d9da43b1f7823a4673ed219478b1c6ff60503eccbb2892894733979468b19c` | named by the theorem; not used as a calculation |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/EVIDENCE.sha256` | `8e56b7ab944e956b9d67993e54bfc8996f02b16803889ac7dfbaa59e2ee0447c` | named by the theorem; every listed file rehashes |
| `cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/FREEZE.sha256` | `a779cdeb5be36ad70c09b1497c3719b8c0659c03b48798414d90464156993970` | named by the theorem; every listed file rehashes |
| `xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md` | `82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f` | ordinary source targets `(0,mu2,0,mu4,0,mu6,J/4)`; not a total-Rees identification of this face |
| `xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md` | `b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d` | frozen ordinary tails and inverse-root sign convention |
| `xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md` | `27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd` | freeze pin; opened because named; not used as a calculation |
| `cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` | frozen seven ordinary tails; compiler input, not a Jacobian derivation |

All fourteen hashes match the values printed in the target, the review
prompt, or the charged manifests. The affine-`mu2` evidence and freeze
manifests were rehashed path-by-path. Characteristic 65521 is a software
control only.

---

## Strongest exact theorem that survives

Work over a field `k` of characteristic zero. In the centered monic octic
chart, write

```text
Q = z^4 + p z^2 + c z + r,
N = n3 z^3 + n2 z^2 + n1 z + n0,
F = Q^2 + N,
u = n1 - (p/2) n3,
Delta = p^2 - 4 r,     D = Delta/4,     s = 5 D - 4 beta.
```

Let `R_ell` be the ordinary Faber tails of the frozen source: if
`w=F^{1/8}` with monic inverse `z(w)`, and if `g` is the polynomial part
of `F^{3/2} + k10 F^{5/4} + k6 F^{3/4} + k2 F^{1/4}`, then
`R_ell = -[w^{-ell}] g(z(w))`. Restrict to the normalized face `k10=1`
with loads `(1,beta,gamma)`. On the affine-Faber graph

```text
beta = (5 D - s)/4,
gamma = D (5 D - 4 s)/16,
mu2 = D^2 s / 32,
c = n3 = n2 = n1 = n0 = 0,
```

inside the open

```text
U = D( D (5 D + 2 s) (5 D - 2 s) ),
```

complete the ordinary coefficient/load/target ring at any `k`-point `x`
of that graph. In that completed local ring:

1. `(R1, R3, R5) = (c, u, n3)` as ideals.
2. `R7` lies in `(c, u, n3)`, hence `R7=0` on the odd-row locus.
3. After adjoining the source equation `J-4 R7`, one has `J=0`, and
   `((R1,R3,R5,J-4 R7):J^infinity)=(1)`.

Consequently no formal arc in this completed chart, including nilpotent
thickenings and finite ramified extensions of the even-parameter ring,
can specialize to `x` while remaining `J`-nonzero.

On `D(D)` the residual divisors `5 D + 2 s = 0` and `5 D - 2 s = 0` are
disjoint. The first differential has rank two (resp. one) there, with
kernel the `c`-direction (resp. the span of `(c,u,n3)=(1,2 D,0)` and
`(0,0,1)`). Every first-order kernel vector has vanishing `dR7`. Those
two faces are not classified.

This is not a total-Rees statement, not a statement in an uncentered
octic chart, not a classification of `Delta=0` or `k10=0`, and not a
terminal, Taylor, order-two, `(8,12)`, maximum-twelve, or JC2 theorem.

---

## Attack 1 — triangular isomorphism `F=Q^2+N` and odd directions `(c,u,n3)`

**CONFIRMED.** There is no hidden odd octic direction in the centered
chart. The moving-center direction is flagged, not assumed away, and is
outside the present ring.

Expand `Q^2`:

```text
z^8 + 2 p z^6 + 2 c z^5 + (p^2+2 r) z^4
    + 2 p c z^3 + (c^2+2 p r) z^2 + 2 c r z + r^2.
```

Adding `N` produces exactly (2.2). The inverse

```text
p = a6/2,     c = a5/2,     r = (a4-p^2)/2,
n3 = a3-2 p c, n2 = a2-c^2-2 p r,
n1 = a1-2 c r, n0 = a0-r^2
```

is polynomial over `Z[1/2]`. Ordered as
`(p,c,r,n3,n2,n1,n0) |-> (a6,a5,a4,a3,a2,a1,a0)`, the Jacobian is block
triangular: the high `3 x 3` block is

```text
( 2  0  0 )
( 0  2  0 )
( 2p 0  2 ),
```

determinant `8`, and the low `4 x 4` block is the identity. In
characteristic zero the map is an automorphism of affine `7`-space. It
neither loses nor introduces a centered octic coefficient.

The involution `z |-> -z` fixes `(p,r,n2,n0)` and negates `(c,n3,n1)`.
The change `u=n1-(p/2)n3` is unitriangular in `(n1,n3)` with Jacobian
`1` at every point, including `p=0`. Thus `(c,u,n3)` is a global basis
of the odd subspace of the centered chart.

The uncentered coefficient `a7` is odd and is **not** among `a0,...,a6`.
The frozen ordinary tails are ten-tuples in `(a0..a6,k10,k6,k2)` with no
`a7`. The theorem's ring therefore has no moving-center gauge direction,
and the completeness claim for `(c,u,n3)` is exact in that ring. Any
total-Rees compiler that retains an uncentered or translation variable
must either print a unit gauge-fix or keep that variable as an extra odd
coordinate before importing (5.1). Section 7 item 1 is this obligation;
it is not silently discharged here.

---

## Attack 2 — parity of ordinary Faber rows, including the inverse-root convention

**CONFIRMED.** `R1=R3=R5=R7=0` at odd coordinates zero, identically in
every even coefficient, load, even target, and nilpotent/formal even jet.

The charged source constructs Faber polynomials as nonnegative parts
`F_j=[F^{j/8}]_+`, sets
`g=F_{12}+k10 F_{10}+k6 F_6+k2 F_2`, takes the monic inverse of
`w^8=F(z)`, and emits `R_ell=-[w^{-ell}] g(z(w))`. On the exact square
with `k10=1` one has `F^{3/2}=Q^3`, a polynomial, so `F_{12}(z(w))=w^{12}`
and does not affect rows one through seven. The remaining generating
function is

```text
H = F^{5/4} + beta F^{3/4} + gamma F^{1/4}
  = sqrt(Q) (Q^2 + beta Q + gamma)
```

on `F=Q^2`. Algebraically `H(z(w))=w^{10}+beta w^6+gamma w^2`, so
`R_ell=[w^{-ell}](H-[H]_+)(z(w))`, matching the sign convention of the
connection classification. The inverse of `w^4=Q(z)` coincides with the
inverse of `w^8=Q(z)^2`.

If odd coordinates vanish, `F` is an even function of `z` for arbitrary
`(p,r,n2,n0)` and arbitrary loads. Then `z(-w)=-z(w)`, while `g` (even
`j`) is even in `z`, so `g(z(w))` is even in `w`. Only even negative
powers appear: `R1=R3=R5=R7=0` as polynomial identities in the even
parameters. Even targets `(mu2,mu4,mu6)` do not enter the row
polynomials. Because the identities are polynomial, they hold after any
nilpotent or formal extension of the even-parameter ring.

The same involution, acting by
`(c,u,n3)|->(-(c,u,n3))` at fixed even coordinates, is the sign flip of
`(a5,a3,a1)`. It sends `z(w)` to `-z_{flipped}(-w)` and makes odd rows
odd polynomials in `(c,u,n3)` and even rows even polynomials, still with
`n0,n2,p,r,beta,gamma` as even parameters. This is the identity the
compiler labels `GENERIC_J_PARITY_ALL`; it is a consequence of the
involution, not of a restriction to the graph.

---

## Attack 3 — independent derivation of matrix (4.3) and determinant (4.4)

**CONFIRMED.** The displayed block is the first differential of the
ordinary rows. The determinant identity has no missing divisor. Formula
(4.1) is the `z`-principal part of the indicated rational function; after
the inverse-root expansion it produces the `(u,n3)` columns.

Write `T=z^2+p/2` and `Q=T^2-D` on the exact square at `c=0`. The
polynomial part of `H` on the graph is (3.2). Differentiating in `T`
gives the division identity

```text
A_T = (T^2-D)(5 T^2 + C0) + K0,
```

with `C0=(5 D-3 s)/4` and `K0=5 D(5 D-2 s)/16`. For a square-normal
variation `delta F=N` of degree at most three, at fixed `w`,

```text
delta z = -N/(2 Q Q'),     Q' = 4 z T,
```

and the first variation of the remainder is

```text
delta R = [N A'/(2 Q Q')]_- - A1,
```

where `A1=[(dH/dF) N]_+` is the variation of the polynomial part and
`[ ]_-` is the principal part at infinity in `z`. The two summands
together are exactly the `z`-negative part of `N A'/(2 Q Q')`, which is
(4.1). (The `F^{3/2}` summand cancels at first order:
`(3/2) Q N + (Q^3)' delta z=0`.)

For the `u`-direction, `N=z`. The polynomial part `A1=(5/4) z T` cancels
the nonnegative part of `N A'/F'`, leaving

```text
delta R_u = (C0/4)(z/T) + (K0/4) z/(T Q).
```

For the `u=0`, `n3`-direction, `N=z T` and

```text
delta R_{n3} = (K0/4) z/Q.
```

Composing with the unperturbed odd inverse root and using
`Q(z(w))=w^4` together with the expansion

```text
z/T = w^{-1} - (p/4) w^{-3} + B0 w^{-5} + O(w^{-7}),
B0 = -p^2/32 - D/4,
```

produces the second and third columns of (4.3) through row five. The
same expansions through `w^{-7}` give the `R7` derivatives used in
Attack 5.

The `c`-column is not square-normal: `Q` itself moves. Logarithmic
differentiation of `g^alpha=(1+p t^2+c t^3+r t^4)^alpha` at `c=0`,
converted by the connections (1.4) including the explicit `c`-terms
`(c/2)h2` in `R5`, yields

```text
dR1/dc = q0,     dR3/dc = -p q0/4,     dR5/dc = q0 B0,
```

with `q0=D(5 D+2 s)/32`. This is the first column of (4.3). Equivalently,
through row seven one has `dR_odd/dc=q0 [w^{-odd}](z/T)`.

Column operation `col_u - (C0/(4 q0)) col_c` on `D(q0)` makes the
determinant transparent, and the resulting identity extends as a
polynomial:

```text
det(4.3) = -q0 K0^2 / 16.
```

Substituting the displayed `q0` and `K0` gives

```text
q0 K0^2 = 25 D^3 (5 D+2 s)(5 D-2 s)^2 / 2^{13},
det     = -25 D^3 (5 D+2 s)(5 D-2 s)^2 / 2^{17}.
```

The only prime factors in characteristic zero are `D`, `5 D+2 s`, and
`5 D-2 s`. The last occurs to order two, matching kernel dimension two
on the `K`-face; `5 D+2 s` occurs simply, matching kernel dimension one
on the `A`-face. The combination `C0=0` does not divide the determinant.
The two-pivot identity `det d(R6,R2-mu2)/d(beta,gamma)=D^4/64` is a
separate even-row calculation on `c=0` and is a unit on `D(D)`, as
claimed in (5.3).

---

## Attack 4 — formal implicit-function theorem, `J`-saturation, counterexamples

**CONFIRMED.** No nilpotent or ramified counterexample to the all-orders
statement on `U` exists. The completion, parameter ring, uniqueness,
ideal equality, parity membership of `R7`, and `J`-saturation are
correct, and they are local to the normalized ordinary-Faber chart.

Let `x` be a point of the graph (3.1) in `U`. Complete the full ordinary
coefficient/load/target ring at `x`. Write `O=(c,u,n3)`, let `E` be the
even parameters `(p,D` or `r`, `n0,n2,beta,gamma,mu2,mu4,mu6,J,...)`,
and `Phi=(R1,R3,R5)`. The ambient completion is a formal power series
ring, hence regular.

By Attack 2, `Phi(E,0)=0` identically, including for Artinian or formal
jets in `E`. By Attack 3, `det d_O Phi` is a unit of the residue field
of `x`, hence a unit of the completed local ring. The formal implicit-
function theorem supplies a unique power-series section
`O=psi(E)` with `Phi(E,psi(E))=0` and `psi` vanishing at the closed
point. The zero section is already such a solution, so `psi=0`.
Equivalently, `Phi=U O` for a `3 x 3` matrix `U` invertible over the
completion, and therefore

```text
(R1,R3,R5)=(c,u,n3)
```

as ideals of the completed local ring, not merely as reduced vanishing
loci.

`R7` is an odd polynomial in `O`, hence lies in the ideal `(c,u,n3)`
already before completion. On the odd-row locus one has `R7=0`. The
source equation `J-4 R7` then yields `J=0`, so `J` lies in
`(R1,R3,R5,J-4 R7)` in the completion. The saturation of that ideal by
`J` is therefore the unit ideal: some power of `J` (in fact `J` itself)
lies in the ideal, which is the statement that `V(R1,R3,R5,J-4 R7)`
does not meet `D(J)` in the completed neighbourhood.

Counterexamples that fail:

- Artinian odd jet `O=epsilon v` in `k[epsilon]/epsilon^N`. The linear
  term is the unit Jacobian times `epsilon v`; Hensel uniqueness forces
  `O=0`.
- Ramified Puiseux arc `O=t^{1/n} v+...`. After the finite ramified base
  change `s^n=t` this is a power-series arc in the completed ring of the
  ramified even-parameter extension. The Jacobian remains a unit, so
  again `O=0`.
- Zero-divisors in the completion. The ambient completed ring is a
  power series ring over a field, hence an integral domain. An
  invertible matrix times `O` vanishes only if `O=0`.

The cubic identity (6.1) supplies a genuine nonlinear odd solution only
off `U`, where `q0=0` and uniqueness fails. That is consistent with
Section 6 and is not a counterexample to (5.1).

The even-row block (5.3) is not required for the odd-row IFT: `Phi(E,0)=0`
holds for arbitrary even jets, whether or not the even rows are solved.
Solving `(beta,gamma)` against `(R6,R2-mu2)` on `D(D)` merely specialises
`E` to the graph before the odd IFT is applied.

---

## Attack 5 — `A` and `K` faces, kernel, `dR7`, raw identities (6.1) and (6.3)

**CONFIRMED.** Rank, kernel bases, `R7`-nullity of every first-order
kernel, and both raw identities recompute as displayed.

On `s=-5 D/2` one has `q0=0`, `C0=25 D/8`, `K0=25 D^2/8`. The first
column of (4.3) vanishes. The `(1,2; 2,3)` minor is `C0 K0/16=625 D^3/1024`,
a unit on `D(D)`, so the rank is two and the kernel is the `c`-direction.
Along that direction `dR_odd=q0 (z/T)=0` as a series through row seven
(and, by the same factor `q0`, as far as the `z/T` mode continues). Even
rows have vanishing first `c`-derivative at `c=0` by parity. Direct
evaluation of the inverse-root formula for `dR7/dc` at `s=-5 D/2` is
the zero polynomial.

On `s=5 D/2` one has `q0=5 D^2/16`, `C0=-5 D/8`, `K0=0`. The third
column vanishes and every `2 x 2` minor involving a later Jacobian row
or the `R7` row against the first row vanishes, so the rank is one and
`dR7` lies in the span of the first Jacobian row. A basis of the kernel
is (6.4):

```text
v_c = (1, 2 D, 0),     v_3 = (0, 0, 1).
```

The combination `col_c + 2 D col_u` is zero because
`q0+2 D (C0/4)=5 D^2/16+2 D(-5 D/32)=0`. In original normals,
`v_c` has `n1=2 D` and `v_3` has `n1=p/2`, with polynomials `2 D z` and
`z T`. For `v_3`, `delta R=(K0/4) z/Q=0` identically as a function of
`z`, so every first-order tail including `dR7` vanishes. For `v_c`,
the independently computed series satisfy
`dR7/dc + 2 D (dR7/du)=0` after restricting to `s=5 D/2`. The two
divisors are disjoint on `D(D)`: their simultaneous vanishing forces
`s=0` and then `D=0`.

Identity (6.1) is the exact-square polynomial

```text
128 R3 + 32 p R1 = c^3 (5 Delta - 8 beta).
```

It follows from `R1=h1`, `R3=h3+(p/4)h1` together with the combination
`128 h3+64 p h1` of the first two odd Laurent rows, and it holds before
any equation of the seven-row ideal. On the `A`-face
`beta=15 D/8`, so `5 Delta-8 beta=5 D=5 Delta/4`, a unit on `D(D)`. The
Newton balance `ord(5 D+2 s)=2 ord(c)` is the first-order reading of
`q0 c` against this cubic; it is a fan initial datum, not a
classification. Identity (6.3) is the raw quintic of the charged
connection theorem, again an exact-square polynomial identity with no
predecessor, radical, or saturation. Both identities were recomputed
from the logarithmic-differentiation recurrence and connections (1.4).

---

## Attack 6 — compiler, exact-Q evidence, V1/V2, characteristic 65521

**CONFIRMED.** V1 is parser-negative only. V2 is a parenthesization
repair. Characteristic 65521 is a software control. The compiler
reconstructs the frozen ordinary tails and checks non-tautological
identities; those identities were not trusted, they were rederived.

The compiler pins the five freeze sources and the canonical all-tail
digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`.
It emits `F0..F6` by (2.2) with the `u`-change, reconstructs each `R_ell`
from the frozen ten-tuples with `k10=1` and affine loads `(beta,gamma)`,
and checks: the triangular inverse against `raw0..raw6`; parity under
`(c,u,n3)|->(-(c,u,n3))`; the seven graph rows including
`R2=D^2 s/32`; the nine entries of (4.3); the determinant identity;
`A`-face rank two plus `dR7/dc=0`; `K`-face rank one plus `dR7` row
proportional to Jacobian row one; and (6.1), (6.3) on `n_i=0`. None of
these checks is a rewriting of a `PASS` string. The Jacobian comparison
is against closed forms, not against `det != 0`.

Byte-for-byte, V2 differs from V1 only by parentheses that force
polynomial exponentiation before division:

```text
p^2/4-D          ->  (p^2)/4-D
D^2*s/32         ->  (D^2)*s/32
Kvec^2/16        ->  (Kvec^2)/16
625*D^3/1024     ->  625*(D^3)/1024
5*D^2/16         ->  5*(D^2)/16
```

V1 Singular stdout contains `poly ^ number failed` at
`subst(f,r,p^2/4-D)` and the validator records
`FAIL_MISSING_OR_NONUNIQUE:GENERIC_J_AFFINE_GRAPH_ROWS=1`. V1 has no
mathematical status. V2 exact-Q and `F_65521` both report
`compiler_rc=0`, `engine_rc=0`, and
`validator=PASS_GENERIC_J_EXCLUSION_DATA`. Every non-determinant endpoint
line is literally identical between the two fields. The determinant
factorizations have the same exponent vector `1,1,2,3` on
`(leading coefficient, 5 D+2 s, -5 D+2 s, D)`; only the coefficients
reduce modulo `65521`. Time/RSS claims match `/usr/bin/time -v` in
stderr (Q: 11784 KiB, `p65521`: 11876 KiB, zero swaps). Characteristic
65521 is not used as a characteristic-zero proof.

---

## Attack 7 — firewall; Section 7 is not discharged

**CONFIRMED as a restriction of scope, not as a promotion.**

The theorem is valid only in the completed normalized ordinary-Faber
coefficient chart with `k10=1` and centered octic coordinates. Its
Section 7 total-Rees consumption gate has **not** been discharged.

What the present argument actually uses:

- centered `(a0..a6)` and the automorphism (2.2);
- ordinary inverse-root Faber rows of the frozen source, targets
  `(0,mu2,0,mu4,0,mu6,J/4)`;
- the normalized loads `(1,beta,gamma)`;
- the two even pivots (5.3) only as a compatible graph description on
  `D(D)`;
- the odd block (4.3) and determinant (4.4);
- parity in `(c,u,n3)` and the absence of `a7` from this ring.

What Section 7 still requires before any campaign import:

1. a printed centered change, including any moving-center gauge, from
   the literal total-Rees compiler;
2. the ordinary rows, inverse-root convention, and target tie, pulled
   back through every retained Rees power;
3. two-sided `k10` normalisation and identification of `(1,beta,gamma)`
   after those powers;
4. (5.3), (4.3), and (4.4) over exact `Q` from that complete source;
5. parity equivariance of every retained correction variable, or an
   explicit unit gauge removing an extra odd moving-center variable;
6. raw (6.1) and (6.3) before radical, saturation, or support
   substitution.

The present compiler performs the normalised-face instances of 1 (in the
centered chart), 2, 4, 5 (for `(c,u,n3)` only), and 6. It does not print
a two-sided `k10` identification, does not retain Rees powers, and does
not treat an uncentered odd variable. Failure of any remaining item stops
the import, as the theorem itself states.

Explicit non-promotions: this review does not classify the `A`-face, the
`K`-face, `Delta=0`, or `k10=0`; does not run terminal `[6,2]` or either
Taylor family; does not construct or exclude a global strict source arc;
and does not close the complete square branch, order two, `(8,12)`,
maximum twelve, or JC2.

---

## Scope sentence

The exact theorem that survives is the complete-local, scheme-theoretic
exclusion of `J`-nonzero formal arcs from the affine-Faber graph on
`U=D(D(5 D+2 s)(5 D-2 s))` in the completed centered ordinary-Faber
coefficient chart with `k10=1`. It is not a total-Rees theorem.

CONFIRMED
