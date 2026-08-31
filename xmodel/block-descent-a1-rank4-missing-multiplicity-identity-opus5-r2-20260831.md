# BD-A1 rank-four: the missing-multiplicity fibre identity (2.3)

status: COMPLETE -- (2.3) REFUTED as stated; corrected identity (2.3') PROVED;
        charged consequence (m=1) PROVED without (2.3)
lane: primary research, prove-or-refute (2.3)
date: 2026-08-31
model: opus5 (r2)

charged inputs (SHA-256 verified before any analysis):

```text
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f  block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190  block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
```

## 0. Verdict

**(2.3) IS REFUTED AS STATED. A CORRECTED IDENTITY IS PROVED UNCONDITIONALLY.
THE CHARGED CONSEQUENCE SURVIVES, AND ON THE CHARGED ROWS (2.3) ITSELF IS
RECOVERED FROM A PROMOTED CONSTRAINT.**

Four separate statements; each is proved below and none depends on the
ledger's row bookkeeping.

**(V1) Corrected identity (proved, Section 5).**  Let `S` be a smooth affine
surface, `F:S->C^2` a dominant *etale* morphism of geometric degree `N`
(any Keller map `C^2->C^2` is such, with `S=C^2`).  Let `B_i` be an
irreducible component of the nonproper-value curve `A_F`.  Then for all `z`
in a Zariski-open dense subset of `B_i`,

```text
N = f(z) + sum_{l in L_F, Phi(l)=closure(B_i)}  s_l * mu_l,          (2.3')
```

where `f(z)=#F^{-1}(z)`, `mu_l` is the generic local degree of the extended
map along the dicritical `l` (the Orevkov base multiplicity), and
`s_l=deg(Phi|_l : l -> closure(B_i))`.  Every other boundary place --
polar/constant (image inside the target line at infinity) and
finite-contracted (image a finite point) -- contributes to no generic fibre.
That exclusion is *proved* (Sections 2--3), not assumed; finite-contracted
boundary components do occur for general polynomial maps.

**(V2) (2.3) as written is false.**  It omits the factor `s_l`.  Hand
control (Section 7): `F(x,y)=(x,x^2y^4)`, `N=4`, `A_F={u=0}` irreducible, a
single dicritical `l` with `mu_l=2` and `s_l=2`.  At generic `z=(0,b)` one
has `f(z)=0`, so `N=4=0+s*mu=4` while `f(z)+sum mu_l=0+2=2 != 4`.  The
failure mode is neither of the two anticipated in the brief: no boundary
place contributes to the fibre of `z` without a dicritical image through
`z`, and there is no multiplicity leakage at a special point.  The defect is
purely that a dicritical line meets the generic fibre in `s_l` points, not
one.  `(2.3)` is exactly the special case `s_l=1` for every `l` over `B_i`,
i.e. every dicritical over `B_i` birational onto its image.

**(V3) On the charged rows, `s_l=1` is forced, so (2.3) holds there.**  The
local monodromy (divisorial inertia) at `B_i` has cycle type

```text
{ mu_l  repeated  s_l  times : l over B_i }  union  { 1^{f(z)} }      (0.1)
```

(Proposition 5.3).  The promoted constraint "divisorial inertia is a
transposition or a three-cycle" (ledger Section 0) forces a dicritical over
`B_i` with `(mu_l,s_l)=(2,1)` resp. `(3,1)`, and then either the
degree-four Orevkov budget (Corollary 5.5) or the companion-census equality
(Corollary 5.4(3)) forces `s_l=1` for *every* dicritical over `B_i`, so that
(2.3) holds verbatim: `4=2+2` resp. `4=1+3`.  Neither of those two payments
is part of (2.3)'s statement, which is why the statement is false while its
charged instance is true: Lemma 2.3's bridge is sound in its intended
application and false in the generality in which it is stated.

**(V4) Lemma 2.3's conclusion `m=1` does not need the equality at all**
(Theorem 10.1).  Proposition 5.3 gives each component `B_i` its own
dicritical `l_i` with `mu_{l_i} >= 2`; the `l_i` are distinct because their
images are; every Orevkov bracket is nonnegative and
`bracket_{l_i} >= mu_{l_i} >= 2`; hence

```text
2m  <=  sum_{i=1}^{m} bracket_{l_i}  <=  sum_{l in L_F} bracket_l = N-1 = 3,
```

so `m=1`.  Provisional Lemma 2.3 may therefore be de-conditionalized on
(2.3): its conclusion follows from its own promoted inputs plus Orevkov's
formula as the ledger already cites it.  The residual risk moves from (2.3)
onto Orevkov 1987 Lemma 4.2 / Chau 1999 Remark 4.9 as quoted, which I have
not re-derived (Sections 11--12).

Scope in one line: (2.3') needs `F` etale and dominant with a finite fibre
over `z`; it does not need Keller beyond etale-ness, does not need `d1=1`,
does not need `N=4`, and does not need `A_F` reduced or irreducible.

## 1. Statement, notation, and what is consumed

`F=(f,g):C^2->C^2` is a polynomial map with `det JF` a nonzero constant
(Keller), noninvertible, of geometric degree
`N=[C(x,y):F^*C(u,v)]=#F^{-1}(generic)`.  For the charged application the
first leg is trivial (`d1=1`), so `F` is the second leg `pi` itself and
`N=4`.  `A_F` is the set of nonproper values: `z in A_F` iff `F` is not
proper over any neighbourhood of `z`; by Jelonek it is either empty (iff `F`
is proper, hence -- with etale-ness -- an automorphism) or a curve.
`B subset A_F` is the reduced target branch of the block, `B_i` its
irreducible components, `m=#Irr(B)`.  `f(z):=#F^{-1}(z)` is the number of
*finite* source preimages (a set count; multiplicities are all `1` because
`F` is etale).

From the ledger (first charged input) I consume only two things: the
promoted-constraint list of its Section 0, and the verbatim statement of
(2.3) inside its Lemma 2.3.  Specifically used below:

- `N=4`, generic divisorial inertia a transposition or a three-cycle, with
  companion (finite-fibre) cardinalities `2` on a `(2,1,1)` component and
  `1` on a `(3,1)` component;
- every component of `B` is a component of `A_F`;
- Orevkov's degree-at-infinity formula in the ledger's own quotation,

```text
  deg_geo(F)-1 = sum_{l subset L_F} [ mu_l + sum_{u in l}(deg_u F* - mu_l) ],
```

  with all displayed corrections nonnegative and only finitely many nonzero
  (Orevkov 1987 Lemma 4.2; Chau 1999 Remark 4.9);
- dicritical images cover `A_F` (Chau 2004 Lemma 1).

No row of the ledger's Sections 1--3 is used, and no conclusion below
depends on its bookkeeping.  `PROVISIONAL` genus-ladder and one-cusp
narrowing items are not used at all.

Two reading conventions must be fixed before anything can be proved, because
the whole question turns on them.

**(C1) `mu_l` is the generic local degree.**  In the quoted formula the
inner sum runs over `u in l` and is finite; that forces `deg_u F*` to be a
local degree at `u` and `mu_l` to be its generic value along `l`, so that
all but finitely many terms vanish.  Both charged function-pair inputs gloss
it the same way ("`m_L` is the generic local degree", cyclic normalization
(4.1)), and I have confirmed it against the primary source rather than the
packets: Chau 1999 Remark 4.9 (p.309) displays (4.9) and says in the same
sentence "where `mu_l` is the degree `deg_u f^*` for generic `u in l`"
(`refs/chau1999_apm71_full.pdf`, attributed to Lemma 4.2 of [O1]).  I take `mu_l := ` generic local degree, and I *prove* in
Proposition 4.1 that this equals `ord_l Phi^*(V)` for `V` a local equation
of the image curve at a generic point -- i.e. a transverse multiplicity,
with no factor of `s_l` built in.  If some other source defines `mu_l` as
`s_l` times the transverse multiplicity, then (2.3) is true by definition
and vacuous; the ledger's Lemma 2.3 proof, which reads
`sum_i (N-f(B_i)) + corr = N-1` with `corr` the *same* nonnegative Orevkov
corrections, is only consistent with (C1).

**(C2) `L_F` is the set of dicritical boundary curves whose image is not
contained in the target line at infinity.**  Equivalently (Section 2) whose
image is a component of `closure(A_F)`.  Boundary curves mapping *onto* the
target line at infinity are not in `L_F` and carry no `mu_l` term.


## 2. The compactification and the typing of boundary curves

Fix any smooth projective compactification `S subset X` on which `F`
extends: start from `S=C^2 subset P^2`, take the rational map
`P^2 --> P^2` induced by `F`, and resolve its indeterminacy.  All
indeterminacy points lie in `P^2 - C^2 = L_infinity^{src}`, because `F` is a
morphism on `C^2`; so the blowups occur only over the source line at
infinity, `S` is untouched, and we obtain

```text
Phi : X -> P^2,   X smooth projective,   S subset X open dense,
D := X - S  a connected curve (a tree of rational curves),
Phi|_S = F,      deg Phi = N.                                     (2.1)
```

Write `L_infinity subset P^2` for the *target* line at infinity.  Because
`F(S) subset C^2`, we have `Phi^{-1}(L_infinity) subset D`; being the
preimage of a divisor under a dominant morphism it is a union of irreducible
components of `D`.

**Typing.**  Each irreducible `E subset D` is complete and irreducible, so
`Phi(E)` is an irreducible closed subset of `P^2` of dimension `0` or `1`.
Exactly one of the following holds.

```text
(D)  dicritical:        dim Phi(E)=1 and Phi(E) != L_infinity;
(P)  polar/constant:    Phi(E) subset L_infinity
                        (either Phi(E)=L_infinity, or Phi(E)= one point of it);
(C)  contracted-finite: Phi(E)={z_E} with z_E in C^2.
```

Type (D) components are the elements of `L_F`; by Lemma 2.1 their affine
images are exactly the components of `A_F` (Chau 2004 Lemma 1 is the same
statement; Lemma 2.1 proves both directions independently).

Type (C) is not vacuous, and it is where a fibre identity could leak.
Witness `F=(x,x^2y)`: in the chart `x=s`, `y=1/(s*tau)` (exceptional
`E={s=0}`, coordinate `tau`) one has `f=s -> 0` and `g=s/tau -> 0` for every
`tau`, so `E` is contracted to the finite point `(0,0)`.  A proof of (2.3)
must therefore *exclude* type (C) from generic fibres, not ignore it.

**Lemma 2.1 (nonproper values are exactly the finite boundary image).**
`A_F = Phi(D) intersect C^2`.

*Proof.*  (subset)  For `z in C^2 - Phi(D)` choose a compact neighbourhood `K` with
`K cap Phi(D)=empty`.  Then `Phi^{-1}(K)` is closed in the compact `X` and
misses `D`, hence is a compact subset of `S`; the same holds for every
compact subset of `int K`, so `F` is proper near `z` and `z notin A_F`.

(superset)  Let `z=Phi(p)` with `p in D`.  Since `S` is dense in `X`, pick
`p_n in S` with `p_n -> p`.  Then `F(p_n) -> z`, and `(p_n)` has no
subsequence convergent in `S`.  Let `K` be a closed ball around `z`; for
large `n`, `p_n in F^{-1}(K)`, which is therefore not compact.  Hence `F` is
not proper over any neighbourhood of `z`, i.e. `z in A_F`.  QED

Consequently `A_F` is the union of the affine parts of the type-(D) image
curves together with the finitely many type-(C) image points.  (Jelonek's
purity theorem says the latter are not isolated in `A_F`; nothing below uses
this.)

**Lemma 2.2 (the generic fibre meets the boundary only in dicriticals over
`z`).**  Let `B_i` be an irreducible component of `A_F`.  There is a finite
subset `Z_i subset B_i` such that for every `z in B_i - Z_i`:

```text
(i)   Phi^{-1}(z) is finite;
(ii)  Phi^{-1}(z) intersect D = disjoint union over l in L_F with
      Phi(l)=closure(B_i)  of  (Phi|_l)^{-1}(z);
(iii) each point of that set is a smooth point of D lying on the single
      component l, is not a critical point of Phi|_l, and lies in the open
      dense subset of l on which the local degree of Phi is generic.
```

*Proof.*  `Phi` is generically finite, so its positive-dimensional fibres
form a curve `Exc` and `Phi(Exc)` is finite; put `Phi(Exc) cap B_i` into
`Z_i`, giving (i).  Let `p in Phi^{-1}(z) cap D` lie on a component `E`, so
`z in Phi(E) cap C^2`.  Type (P) is impossible, since
`Phi(E) subset L_infinity` misses `C^2`.  Type (C) forces `z=z_E`; there
are finitely many such components, so put their images into `Z_i`.  Type (D)
gives an irreducible curve `Phi(E) ni z`; if `Phi(E) != closure(B_i)` the
intersection is finite, into `Z_i`.  That is (ii).  For (iii) add the images
of the finitely many corners of `D`, the branch values of the finitely many
`Phi|_l` over `B_i`, and the images of the finite non-generic-degree sets of
Proposition 4.1(a).  `Z_i` is a finite union of finite sets.  QED

Lemma 2.2 is precisely method requirement 1: no polar/constant component and
no contracted component can meet a *generic* fibre, and the only boundary
places in the fibre of a generic `z in B_i` lie on dicritical lines whose
image passes through `z` -- indeed whose image *is* the closure of `B_i`.

## 3. Degree bookkeeping on the compactified map

**Lemma 3.1 (conservation of number).**  Let `z in P^2` with `Phi^{-1}(z)`
finite.  Then

```text
sum_{p in Phi^{-1}(z)} mult_p(Phi) = N,                            (3.1)
```

where `mult_p(Phi) = dim_C O_{X,p} / Phi^# m_{P^2,z} O_{X,p}` is the local
degree (equivalently the topological local mapping degree at the isolated
preimage `p`).

*Proof.*  The set `Delta subset P^2` of points with positive-dimensional
`Phi`-fibre is finite (image of the exceptional curve `Exc`), and `z notin
Delta` by hypothesis.  Choose an open ball `W ni z` with
`W intersect Delta = empty`.  Then `Phi : Phi^{-1}(W) -> W` is proper (as
`X` is compact) with all fibres finite, hence finite; `W` is connected and
`Phi` is surjective, so this finite map has a well-defined degree, equal to
the number of preimages of a point of `W` over which it is unramified.  The
locus in `P^2` with fewer than `N` preimages is a proper closed subvariety,
so a general point of `W` has exactly `N` preimages, all lying in
`Phi^{-1}(W)`.  Hence the degree is `N`, and conservation of number for a
finite flat-over-a-smooth-base map (equivalently, additivity of the
topological degree over an isolated fibre) gives (3.1).  QED

**Corollary 3.2 (raw fibre identity).**  For `z in C^2` with `Phi^{-1}(z)`
finite,

```text
N = sum_{p in F^{-1}(z)} mult_p(F)  +  sum_{p in Phi^{-1}(z) cap D} mult_p(Phi).
                                                                   (3.2)
```
If moreover `F` is etale (e.g. Keller), every finite preimage has
`mult_p(F)=1` and the first sum is the *set* count `f(z)`:

```text
N = f(z) + sum_{p in Phi^{-1}(z) cap D} mult_p(Phi).               (3.3)
```

*Proof.*  `Phi^{-1}(z)` is the disjoint union of `F^{-1}(z)` and
`Phi^{-1}(z) cap D`, with `mult_p(Phi)=mult_p(F)` on `S`; apply Lemma 3.1.
Etale gives `mult_p(F)=1`.  QED

(3.3) is where -- and the only place where -- the Keller hypothesis enters:
it converts a multiplicity-weighted count into the cardinality `f(z)` that
(2.3) speaks about.  Note also that etale-ness gives `Exc cap S = empty`
free of charge, since an etale map is quasi-finite.


## 4. Local multiplicity along a dicritical line

Throughout this section `l in L_F`, `Gamma := Phi(l) subset P^2` is its
irreducible image curve, `sigma := Phi|_l : l -> Gamma`,
`s := s_l = deg(sigma)`, and `tilde{sigma} : l -> Gamma^nu` is the lift of
`sigma` to the normalization (`l` is smooth, being a component of a tree of
rational curves, so the lift exists).  Define

```text
mu_l := mult_l ( Phi^* Gamma ),                                    (4.0)
```

the coefficient of `l` in the pullback of the divisor `Gamma`.  It is a
positive integer because `l subset Phi^{-1}(Gamma)`.

**Proposition 4.1 (local degree along `l`).**
(a) For every `p in l` outside a finite set, `mult_p(Phi) = mu_l`.  Hence
`mu_l` *is* the generic local degree, i.e. the Orevkov base multiplicity
under reading (C1).
(b) Let `u in l` be any point with `z'=Phi(u) in C^2` and `Phi^{-1}(z')`
finite near `u`, and let `e_u` be the ramification index of `tilde sigma` at
`u`.  Then `mult_u(Phi) >= e_u * mu_l`.  No smoothness of `Gamma` at `z'`
and no smoothness of `D` at `u` is required.

*Proof.*  Work in local analytic coordinates `(t,w)` at `p in l` with
`l={t=0}`, `p=(0,0)`, and in local coordinates `(U,V)` at `z=Phi(p)` with
`Gamma={V=0}` and `U|_Gamma` a coordinate on `Gamma` (possible whenever `z`
is a smooth point of `Gamma`, and `V` is then a local equation of `Gamma`).
By (4.0),

```text
V o Phi = t^{mu_l} * psi(t,w),        psi(0,w) not identically 0.   (4.1)
```

The local degree at an isolated preimage is the local intersection number
`mult_p(Phi) = I_p(h_1,h_2)` of the two germs `h_1 = U o Phi - U(z)` and
`h_2 = V o Phi`.  Since `h_2 = t^{mu_l} * psi`, additivity of intersection
numbers gives

```text
I_p(h_1,h_2) = mu_l * I_p(h_1,t) + I_p(h_1,psi)
             = mu_l * ord_w (h_1(0,w)) + I_p(h_1,psi).             (4.2)
```

Now `h_1(0,w) = U(sigma(0,w)) - U(z)` is the image parametrization read in
the coordinate `U` of `Gamma`, so `ord_w h_1(0,w) = e_p`, the ramification
index of `tilde sigma` at `p`.  This gives (a):

(a) Discard the finitely many `p in l` that are singular points of `D`, or
have `Phi(p) in L_infinity`, or have `Phi(p) in Sing(Gamma)`, or are
ramification points of `tilde sigma`, or lie on `{psi(0,w)=0}` (a finite
set, since `psi(0,w) not== 0`).  For the remaining `p`, `e_p=1` and
`I_p(h_1,psi)=0` because `psi(p) != 0`; so `mult_p(Phi)=mu_l`.

(b) The above local model needs `Gamma` smooth at `Phi(u)`, which fails at
the singular points of `Gamma` -- exactly where the ramification of
`tilde sigma` may hide.  So argue instead by the projection formula.  Let
`Gamma_1` be the analytic branch of `Gamma` at `z'` traced by `Phi|_l` near
`u`, `G_1` a local equation of `Gamma_1`, and `n:(C,0)->(C^2,z')` its
normalization parametrization, so that `Phi(0,W) = n(tau(W))` with
`ord_W tau = e_u` (this is the definition of `e_u`).  The other branches of
`Gamma` at `z'` are distinct germs from `Gamma_1`, so their pullbacks do not
contain `l`; hence

```text
mult_l(Phi^* G_1) = mult_l(Phi^* Gamma) = mu_l,
Phi^* G_1 = t^{mu_l} * psi,     psi(0,W) not identically 0.        (4.2')
```
Let `L` be a generic line through `z'`, so `I_{z'}(Gamma_1,L) = mult_{z'}(Gamma_1)`
and `ord_tau (L o n) = mult_{z'}(Gamma_1)`.  The projection formula for a
finite germ (conservation of number) gives

```text
I_u(Phi^*G_1, Phi^*L) = mult_u(Phi) * I_{z'}(Gamma_1, L)
                      = mult_u(Phi) * mult_{z'}(Gamma_1),
```
while (4.2') and additivity give

```text
I_u(Phi^*G_1, Phi^*L) = mu_l * I_u(t, Phi^*L) + I_u(psi, Phi^*L)
                     >= mu_l * ord_W ( (L o Phi)(0,W) )
                      = mu_l * ord_W (L o n o tau)
                      = mu_l * mult_{z'}(Gamma_1) * e_u.
```
Divide by `mult_{z'}(Gamma_1) > 0`.  QED

Proposition 4.1(a) is a construction, not a name-match: it identifies the
"generic local degree" of the cited formula with the divisorial quantity
(4.0), which is what makes it computable.  Chau's dicritical-image lemma is
used only through Lemma 2.1, which proves both inclusions directly.

**Corollary 4.2 (boundary contribution of one dicritical at a generic image
point).**  For all `z` in a Zariski-open dense subset of `Gamma cap C^2`,

```text
sum_{p in l cap Phi^{-1}(z)} mult_p(Phi)  =  s_l * mu_l.           (4.3)
```

*Proof.*  A generic `z` has exactly `s_l` preimages on `l` (`tilde sigma`
has degree `s_l` and is unramified over a generic point; `Gamma` is smooth
at a generic point so `Gamma^nu -> Gamma` is bijective there), and each of
them avoids the finite bad set of Proposition 4.1(a).  QED

**Proposition 4.3 (Orevkov bracket bound).**  Write
`bracket_l := mu_l + sum_{u in l}(deg_u f^* - mu_l)` for the `l`-th summand
of Orevkov's formula (4.9).  Then

```text
bracket_l  >=  mu_l * s_l.                                         (4.5)
```

*Proof.*  Three source facts fix the geometry, and I check each against the
construction above rather than by name.

(i) In Orevkov's reduction, quoted verbatim in Chau 1999 p.309, the source
is `(C^2 sqcup D sqcup {infinity}, D, infinity)` where "`D` is the union of
a finite number of curves homeomorphic to `C`".  So each dicritical `l`
carries exactly *one* place over the target point at infinity, and the sum
`sum_{u in l}` in (4.9) runs over all of `l = C`, i.e. over every point of
`l` whose image is finite.  In my model this says `k := #tilde
sigma^{-1}(infinity) = 1`.

(ii) Chau 1999 states, in the same sentence, "`mu_l` is the degree
`deg_u f^*` for generic `u in l`".  That is Proposition 4.1(a) verbatim, so
`mu_l = mult_l(Phi^* Gamma)` by (4.0) -- and in particular `mu_l` carries no
hidden factor `s_l`.  This closes reading (C1) from the source.

(iii) Chau 2004 Theorem 1 gives a polynomial parametrization
`xi |-> (A xi^{md}+..., B xi^{me}+...)` of every component of `A_F`, and
Lemma 1 of the same paper realises it as `f_phi`, i.e. as `Phi|_l` on the
affine part of `l`.  A finite surjection `A^1 -> Gamma^nu` forces
`Gamma^nu = A^1` (genus `0` by Luroth, one place at infinity by properness),
which is the ledger's pinned "normalization `= A^1`".

Now `tilde sigma : l = P^1 -> Gamma^nu = P^1` has degree `s_l`, and by (i)
its ramification over the point at infinity is `s_l - 1`; Riemann--Hurwitz
`-2 = -2 s_l + R` gives `R = 2 s_l - 2`, so the ramification carried by the
affine part `l = C` is exactly `s_l - 1`.  By Proposition 4.1(b) -- which
now holds at *every* affine point, singular image or not --

```text
deg_u f^* - mu_l  =  mult_u(Phi) - mu_l  >=  mu_l (e_u - 1) >= 0,
```
and summing over the affine ramification points gives
`bracket_l >= mu_l + mu_l (s_l-1) = mu_l s_l`.  QED

The one step I assert rather than prove is the comparison
`deg_u f^* = mult_u(Phi)` between Orevkov's topological local degree in his
reduction and the algebraic local degree of my `Phi` at a point `u in l`
with finite image and finite fibre; both count the preimages near `u` of a
nearby generic value, so they agree, but I have not read [O1] itself.  Call
this reading **(C3)**.  Note also that Orevkov's source model
`(C^2 sqcup D sqcup {infinity})` implicitly asserts that all non-dicritical
boundary maps to the target point at infinity -- i.e. that type-(C)
components (Section 2) do not occur for Keller maps.  That is an unpaid
hypothesis of the quoted formula; none of my results uses it, because
Lemma 2.2 disposes of type (C) directly.

(4.5) is the normalization step the charged function-pair producer used
("bracket at least `m*s`", cyclic normalization Section 4), here re-derived,
with the singular-image case closed by the projection formula.

## 5. The corrected identity, its proof, and the monodromy cycle type

**Theorem 5.1 (corrected missing-multiplicity identity).**  Let `S` be a
smooth affine surface, `F:S->C^2` a dominant etale morphism of geometric
degree `N`, `A_F` its nonproper-value set, `B_i` an irreducible component of
`A_F`.  Then for all `z` in a Zariski-open dense subset of `B_i`,

```text
N  =  f(z)  +  sum_{l in L_F : Phi(l)=closure(B_i)}  s_l * mu_l.   (2.3')
```

*Proof.*  Take `z in B_i - Z_i` with `Z_i` the finite set of Lemma 2.2,
enlarged by the finitely many points excluded in Corollary 4.2 for each of
the finitely many `l` over `B_i`.  By Lemma 2.2(i) the fibre `Phi^{-1}(z)`
is finite, so Corollary 3.2 applies and gives
`N = f(z) + sum_{p in Phi^{-1}(z) cap D} mult_p(Phi)`.  By Lemma 2.2(ii)
that boundary sum decomposes over the dicritical lines whose image is
`closure(B_i)`, and by Corollary 4.2 the contribution of each such `l` is
`s_l*mu_l`.  QED

**Corollary 5.2 ((2.3) is exactly the `s=1` case).**  (2.3) holds at a
generic point of `B_i` iff every dicritical over `B_i` is birational onto
its image (`s_l=1`).  In general it fails one-sidedly:
`f(z) <= N - sum_l mu_l`, with equality iff all `s_l=1`.

The following proposition is the structural content that makes the charged
application work, and it is what the ledger's Lemma 2.3 was implicitly
reaching for.

**Proposition 5.3 (inertia cycle type).**  Keep the hypotheses of
Theorem 5.1 and let `z in B_i` be generic.  Let `delta` be a meridian of
`B_i` at `z` (the boundary of a small disc transverse to `B_i` at `z`,
inside a ball meeting `A_F` only in `B_i`).  The monodromy of the
`N`-sheeted covering `F : S - F^{-1}(A_F) -> C^2 - A_F` along `delta` is a
permutation of cycle type

```text
{ mu_l  repeated  s_l  times : l in L_F over B_i }  union  { 1^{f(z)} }.
                                                                   (5.1)
```

*Proof.*  Choose a ball `W ni z` as in Lemma 3.1, small enough that
`W cap A_F = W cap B_i` is a smooth disc and `Phi^{-1}(W) -> W` is finite of
degree `N`.  Then `Phi^{-1}(W)` is the disjoint union of connected open
neighbourhoods `V_p` of the points `p in Phi^{-1}(z)`, with
`V_p -> W` finite of degree `mult_p(Phi)`.

For `p in F^{-1}(z)`: `F` is etale at `p`, `mult_p=1`, so `V_p -> W` is an
isomorphism and `V_p subset S`; it is a single sheet, fixed by the
monodromy, contributing a `1`-cycle.  There are `f(z)` of these.

For `p in Phi^{-1}(z) cap D`: by Lemma 2.2(iii), `p` is a generic point of a
dicritical `l` over `B_i`, so Proposition 4.1's local model applies with
`e_p=1` and `psi(p) != 0`.  In coordinates `(t,w)` at `p` and `(U,V)` at
`z`, with `B_i = {V=0}`, we have `U o Phi = U(z) + w*unit + t(...)` and
`V o Phi = t^{mu_l}*unit`.  Over a point `(U_0,V_0) in W` with `V_0 != 0`,
solving `U o Phi = U_0` first (implicit function theorem in `w`) and then
`t^{mu_l} = V_0 * unit^{-1}` gives exactly `mu_l` preimages in `V_p`, all
with `t != 0`, hence all in `S`.  Continuing `V_0` once around `0` permutes
the `mu_l` roots `t` cyclically.  So `V_p` contributes exactly one cycle, of
length `mu_l`.  By Corollary 4.2 there are `s_l` such `p` on each `l`.

The cycle lengths sum to `N` by Corollary 3.2, so (5.1) is the full cycle
type.  QED

In words: *escaping sheets form one cycle per dicritical point of the
fibre, of length the generic local degree there; finite preimages are the
fixed points.*  Conversely the divisorial inertia determines the dicritical
data over `B_i` up to the ambiguity between `mu=1` dicriticals and finite
preimages.

**Corollary 5.4 (the charged rows satisfy (2.3) verbatim).**  Assume the
promoted rank-four constraints of ledger Section 0: `N=4` and the generic
divisorial inertia at each component `B_i` of `B` is a transposition or a
three-cycle.  Then:

1. There is a distinguished dicritical `l_i` over `B_i` with
   `mu_{l_i} = 2` (transposition case) or `3` (three-cycle case), and
   `s_{l_i} = 1`.
2. Every other dicritical `l` over `B_i` has `mu_l = 1`, and
   `f(z) = u_i - sum_{l != l_i} s_l` where `u_i = 2` resp. `1`.
3. If in addition the companion census equality `f(B_i) = u_i` holds (the
   "companion fibre cardinalities `2,1,0`" of the charged function-pair
   input Section 1), then `l_i` is the *only* dicritical over `B_i` and
   (2.3) holds verbatim: `4 = 2+2` resp. `4 = 1+3`.
4. Unconditionally on 3, `N - f(B_i) >= 2` at every component.

*Proof.*  Finite preimages give `1`-cycles (Proposition 5.3), so the unique
non-trivial cycle of a transposition or three-cycle must come from a
dicritical point, forcing some `l_i` over `B_i` with `mu_{l_i} in {2,3}`
equal to that cycle length.  If `s_{l_i}` were `>= 2` the cycle type would
contain two cycles of length `mu_{l_i} >= 2`, i.e. would be `(2,2)` or
worse -- excluded.  Any other dicritical over `B_i` contributes cycles of
length `mu_l`, which must be `1`.  Then (5.1) and Theorem 5.1 give 2 and 4;
under 3 the count `f(z)=u_i` forces `sum_{l != l_i} s_l = 0`.  QED

**Corollary 5.5 ((2.3) is true on the charged rows, without the companion
census).**  Assume `N=4`, Orevkov's formula (4.9) as quoted, and generic
divisorial inertia at each component `B_i` of `B` a transposition or a
three-cycle.  Then `s_l = 1` for *every* dicritical `l` over every `B_i`,
and (2.3) holds verbatim at a generic point of every component:
`4 = f(z) + sum_{l over B_i} mu_l`.  The census values are
`(mu,s,f)=(2,1,2)` resp. `(3,1,1)`, with one alternative left open by the
budget alone: a transposition component may carry one extra `mu=1`, `s=1`
dicritical, and then `f(z)=1` and (2.3) reads `4=1+(2+1)`.

*Proof.*  The budget is `sum_{l in L_F} bracket_l = N-1 = 3` with every
`bracket_l >= 0`.  By Proposition 4.3, `bracket_l >= mu_l s_l`.  Hence no
dicritical whatsoever can have `mu_l >= 2` and `s_l >= 2`, which would cost
`>= 4`.  By Corollary 5.4(1) there is `l_i` over `B_i` with `mu_{l_i} in
{2,3}`; therefore `s_{l_i}=1`, and `bracket_{l_i} >= 2`.  Any further
dicritical `l` over `B_i` has `mu_l=1` by Corollary 5.4(2); if it had
`s_l >= 2` its bracket would be `>= 2` and the two brackets together would
cost `>= 4 > 3`.  So `s_l=1` for it too, and the budget leaves room for at
most one such extra line (none when `mu_{l_i}=3`).  Every `s_l` being `1`,
Theorem 5.1 reduces to (2.3).  QED

So the charged bridge is sound, but only after (a) the `s_l` factor is put
in, and (b) either the inertia constraint plus the degree-four budget
(Corollary 5.5) or the companion census (Corollary 5.4(3)) is spent.  (2.3)
is not a general theorem and must not be quoted as one at other `N`, at
`d1>1`, or for components of `A_F` outside `B`.


## 6. Genericity, honestly

Could a correction be supported over a curve's worth of `z`, i.e. be
generic?  It cannot.  Here is the complete list of what Sections 2--5
discard, with the reason each set is finite; all are subsets of the curve
`B_i`, so "finite" and "not generic" coincide.

```text
(Z1) Phi(Exc) cap B_i          -- images of curves contracted by Phi.
     Finite: Phi generically finite => Exc a curve => Phi(Exc) finite.
(Z2) images of type-(C) boundary components.
     Finite: finitely many components of D, one image point each.
(Z3) Sing(B_i) and B_i cap (other components of closure(A_F)).
     Finite: distinct irreducible curves meet in finitely many points.
(Z4) branch values of tilde sigma_l : l -> B_i^nu, for l over B_i.
     Finite: a nonconstant morphism of smooth projective curves has
     finitely many ramification points.
(Z5) Phi(corners of D) and Phi({psi_l(0,w)=0}) for l over B_i.
     Finite: D has finitely many singular points; psi_l(0,w) is a
     nonzero function on l (Proposition 4.1), so it has finitely many
     zeros.
```

(Z2) is the only entry that could conceivably have hidden a curve's worth of
corrections, and it is exactly the failure mode the brief asked me to look
for ("a boundary place contributing to the fibre of `z` without a dicritical
image through `B_i`").  It is finite *by definition of the typing*: a
boundary component whose image swept a curve would be dicritical.  Type-(C)
components are real (the `F=(x,x^2y)` witness in Section 2), but each one
perturbs exactly one point of the target.  Likewise (Z5) is the only entry
that could have hidden "multiplicity leakage at a special point", and
(4.2) makes the leakage explicit and finite:

```text
mult_u(Phi) - mu_l  =  mu_l*(e_u - 1) + I_u(h_1, psi_l)  >=  0.     (6.1)
```

There is a clean statement about what happens at the discarded points where
the fibre is still finite, which also fixes the direction of every failure.

**Proposition 6.1 (one-sided degeneration).**  Let `F` be etale and
`z' in C^2` arbitrary.  Then `f(z') <= f(z)` for `z` generic in any
component `B_i` through `z'`, and if `Phi^{-1}(z')` is finite then

```text
sum_{p in Phi^{-1}(z') cap D} mult_p(Phi)  =  N - f(z')
                                           >=  sum_{l over B_i} s_l*mu_l.
                                                                    (6.2)
```

*Proof.*  `F` etale means each `p in F^{-1}(z')` has a neighbourhood mapped
isomorphically onto a neighbourhood of `z'`; distinct `p` give disjoint such
neighbourhoods (shrink), so every `z` near `z'` has at least `f(z')`
preimages, and `f(z')` is finite (etale => quasi-finite).  Hence
`f(z') <= f(z)`.  Corollary 3.2 at `z'` and Theorem 5.1 at `z` give (6.2).
QED

So at every point of `B_i`, generic or not, the boundary of the fibre is at
least the generic dicritical mass, never less.  In particular the `(3,1)`
cusp increment "`+mu`" that the charged function-pair inputs place at the
unique unibranch value is an instance of (6.2), and the `(2,2)` node is
budget-free precisely because it has two normalization preimages each
carrying the generic packet -- both readings are consistent with (6.1)--(6.2)
and neither needs a new hypothesis.

## 7. Controls computed by hand

All four controls are non-Keller maps with completely explicit dicritical
structure, computed in a toric chart at infinity: for coprime weights the
monomial valuation `nu(x)=a, nu(y)=-b` is divisorial, and if `t` and `w` are
monomials in `x,y` of `nu`-weights `1` and `0` generating the same lattice,
then `(t,w) |-> (x,y)` is birational, `{t != 0}` maps into `C^2`, and
`l := {t=0}` is a boundary curve of the resulting partial compactification.
`mu_l`, `s_l` and local degrees are intrinsic to the divisor and the map, so
they may be read off in that chart.  No CAS was used or needed; every step
below is a two-line substitution.

**(K1) `F=(x,xy)`, `N=1`.**  Weights `(1,-1)`: `t=x`, `w=xy`,
`(x,y)=(t,w/t)`, `Phi(t,w)=(t,w)`.  So `l={t=0}` maps isomorphically onto
`Gamma={u=0}`: `s=1`, `mu=1`, `f=0`, and `1 = 0 + 1*1`.  It shows `mu_l=1`
occurs.

**(K2) `F=(x,xy^2)`, `N=2`.**  Weights `(2,-1)`: `t=xy`, `w=xy^2`,
`(x,y)=(t^2/w, w/t)`, so on `{w != 0}`

```text
Phi(t,w) = (t^2/w, w).
```
`l={t=0}` maps to `(0,w)`: `s=1`.  `mu = I((t^2)*unit, w-w_0) = 2`.
`A_F={u=0}`; at generic `z=(0,b)`, `b != 0`, `f(z)=0`.  Identity:
`2 = 0 + 1*2`.  Monodromy check of Proposition 5.3: the two solutions
`y = +-sqrt(b/x)` are exchanged as `x` circles `0`, so the inertia is a
transposition and the cycle type is `(2)` -- exactly one `2`-cycle from one
dicritical point, no fixed sheets.  This is the miniature of the charged
`(2,1,1)` pattern.  (2.3) also holds here, `s` being `1`.

**(K3) `F=(x,x^2y^4)`, `N=4`: the refutation of (2.3).**  Weights `(2,-1)`:
`t=xy`, `w=xy^2`, `(x,y)=(t^2/w,w/t)`, and

```text
u = x = t^2/w,      v = x^2y^4 = (xy^2)^2 = w^2,
Phi(t,w) = (t^2/w, w^2)   on {w != 0}.
```
Hence `l={t=0}` maps to `(0,w^2)`, i.e. onto `Gamma={u=0}` with

```text
s_l = 2,        mu_l = mult_l(Phi^* {u=0}) = ord_t(t^2/w) = 2.
```
Nonproper set: `y^4=b/a^2` is solvable for `a != 0`, so
`F(C^2)={a != 0} u {(0,0)}` and `F` is proper over `{a != 0}`; `(0,0)` has
the line `{x=0}` as fibre.  So `A_F={u=0}` is irreducible, and at generic
`z=(0,b)` there is no finite preimage at all, `f(z)=0`.  Theorem 5.1 in its non-etale form (Corollary 3.2 plus
Corollary 4.2) reads

```text
4 = N = 0 + s_l*mu_l = 2*2.                                        (7.1)
```
Since the corrected identity already accounts for all of `N`, there is no
second dicritical over `{u=0}`; therefore

```text
f(z) + sum_{l over B} mu_l = 0 + 2 = 2  !=  4 = N,
```
and (2.3) fails by a factor `s_l=2`.  The failure is not at a special point
and involves no exotic boundary place: it is generic on `{u=0}`, and the
only boundary place in the fibre is a dicritical line whose image passes
through `z` -- there are simply two points of it in each fibre.

**(K4) `F=(x,xy^2+y)`, `N=2`, with a nonempty finite fibre over the branch.**
For `x=a != 0`, `ay^2+y=b` has `2` roots, so `N=2`; for `x=0`, `y=b` is the
unique solution, so `f(0,b)=1` for every `b`, and the second root
`y ~ -1/a` escapes, so `{u=0} subset A_F`.  Chart: weights `(1,-1)` give
`t=x`, `w=xy`, `v=(w^2+w)/t`, which is not yet a morphism along `{t=0}`;
the arcs have `w -> -1`, so set `w=-1+t*xi`.  Then

```text
x = t,   y = -1/t + xi,   u = t,   v = -xi + t*xi^2,
```
a morphism near `{t=0}`.  So `l={t=0}` maps to `(0,-xi)`: `s=1`, and
`mu = mult_l Phi^*{u=0} = ord_t(t) = 1`.  Identity:

```text
2 = N = f(z) + s*mu = 1 + 1.                                       (7.2)
```
Cycle-type check: the bounded root and the escaping root are
distinguishable, so the inertia at `{u=0}` is *trivial*, matching (5.1)
`= {1} union {1^1}`.  This is the configuration Corollary 5.4 excludes on
the charged rows, and it shows that the exclusion really does consume the
promoted inertia constraint: a `mu=1` dicritical is invisible to the
inertia's cycle type.  (`det JF = 2xy+1` is `1` along `x=0`, so the finite
preimage counts with multiplicity one and (7.2) is a fair test of (3.3).)

Every control reproduces the proved identity; (K3) alone contradicts (2.3).


## 8. What `mu=1` does and does not give

The analogous comparison lives in the *cyclic normalization* input at
Section 4, equations (4.2)--(4.4); the *coordinator integration* carries it
at its Section 3, equation (3.2), its Section 4 being the Euler/orbit
ledger.  In both it reads, for `H=pi o f_mu` of degree `4mu`,

```text
4mu - 1  >=  (2mu*r + mu) + (mu - 1)  =  2mu*r + 2mu - 1,          (8.1)
```
with the three summands being: generic ramification-boundary mass `2mu` on
each of the `r` components of `B`; the unibranch `(3,1)` cusp increment
`mu`; and one unit for each of the `mu-1` deleted cyclic lines.

**What `mu=1` gives.**  Term by term: `2mu*r -> 2r`, `mu -> 1`,
`mu-1 -> 0`, and `4mu-1 -> 3`.  The inequality becomes `3 >= 2r+1`, hence
`r=1`.  The *shape* of the argument therefore does transfer to the Keller
map itself: a per-component missing-multiplicity mass of at least `2`,
weighed against the budget `N-1=3`.  That is exactly the chain of
Theorem 10.1 below, and it is the content the ledger's Lemma 2.3 was after.
In this sense the specialization is not vacuous.

**What `mu=1` does not give.**

1. *No statement about the charged row transfers.*  The row hypotheses
   `Pic(U)=Z/mu`, `mu>=2`, `mu|d1` are contradictory at `d1=1`, as the
   producer says twice ("`mu|1` contradicts `mu>=2`").  So the `mu=1`
   reading is not a specialization of the theorem about `H`: it is a
   different map, `F=pi` itself, with `f_mu` the identity.  Everything
   downstream of the deleted lines evaporates -- `C0=pi(Phi)`, its forced
   self-identification (4.6), saturation, and the Euler/orbit ledger
   (0.5)--(0.6) all need `mu-1 >= 1`.
2. *The `2mu` per component is an input, not an output.*  In the producer it
   comes from `sum_j e_j f_j = mu` for `Ubar -> Y` multiplied by "the
   rank-two local factor of `pi`" -- i.e. it presupposes that the generic
   missing multiplicity of `pi` over each component is `2`.  At `mu=1` the
   cyclic factor is `1` and *all* that is left is that presupposition.  So
   the `mu=1` argument is circular unless the `2` is derived independently.
   Proposition 5.3 with the promoted inertia constraint is such a
   derivation (Corollary 5.4(4)); the companion census is another.
3. *The cusp increment is not available in general.*  The `+mu -> +1` term
   needs a `(3,1)` unibranch value on `B`, which the charged one-cusp row
   has by hypothesis and a general reducible rank-four row need not.  It is
   also not needed: `3 >= 2r` already gives `r=1`.
4. *Direction and `s`-awareness.*  The producer's comparison is an
   inequality throughout and is explicitly `s`-aware ("its bracket is at
   least `ms`").  (2.3) is an equality and `s`-blind.  So the ledger's
   Section 2 sentence "It is the same comparison the function-pair producer
   used ... specialised to `mu=1`" is inaccurate in exactly the respect that
   matters: the equality is a strengthening absent from the source, and that
   strengthening is what fails.  The one-sided statement the source does
   make is the one the conclusion needs.

## 9. Weakest exact hypotheses and scope

```text
Theorem 5.1 / (2.3'):   S smooth quasi-projective surface (affine not
                        needed), F:S->C^2 dominant morphism, etale.
                        NOT needed: Jacobian constant (only nowhere zero),
                        N=4, d1=1, A_F reduced or irreducible, one place at
                        infinity, Chau, Orevkov, any promoted constraint.
                        If F is not etale: (3.2) holds verbatim with
                        sum_p mult_p(F) in place of f(z).
Prop 5.3 (cycle type):  same hypotheses as Theorem 5.1.
Prop 4.1:               no hypothesis beyond Phi being a morphism near the
                        point considered and the fibre being finite there.
Prop 4.3 (bracket):     readings (C1),(C3); Orevkov's reduction (each
                        dicritical homeomorphic to C); Gamma^nu = A^1,
                        which is where Keller is genuinely spent, via
                        Chau 2004 Theorem 1 + Lemma 1.
Cor 5.4:                + N=4 and the promoted inertia constraint.
Cor 5.5, Thm 10.1:      + Orevkov's formula (4.9) as quoted.
```

Keller enters in exactly three places and nowhere else: (a) etale-ness, to
make `f(z)` a set count in (3.3); (b) Chau's Theorem 1, to know
`Gamma^nu=A^1` in Proposition 4.3; (c) the validity of Orevkov's formula,
which is stated for Keller maps.  `d1=1` is used only to identify `F` with
the second leg `pi` so that `N=4`; nothing in Sections 2--6 sees it.

Scope limits.  Everything is two-dimensional (the Section 2 trichotomy and
the finiteness of `Phi(Exc)` both use `dim=2`); nothing is asserted for
`n>=3`.  Nothing here decides JC2, excludes `R4-CYCLE-1`, treats the
primitive/no-block horn, or bears on the ledger's `n22` families.

## 10. Consequence for provisional Lemma 2.3 and the rank-four rows

**Theorem 10.1 (reducible branch excluded; Lemma 2.3's conclusion, without
(2.3)).**  Let `F` be a noninvertible plane Keller map, let a rank-four
proper block be given in the canonical normalization (`d1=1`, `N=4`), and
let `B = union_{i=1}^m B_i` be its reduced target branch.  Assume the
promoted constraint that generic divisorial inertia at each `B_i` is a
transposition or a three-cycle, and Orevkov's formula (4.9) as quoted.  Then
`m=1`.

*Proof.*  For each `i`, Corollary 5.4(1) supplies a dicritical `l_i` over
`B_i` with `mu_{l_i} in {2,3}`.  The `l_i` are pairwise distinct because
their images `closure(B_i)` are distinct irreducible curves.  All
corrections in (4.9) being nonnegative, `bracket_{l_i} >= mu_{l_i} >= 2`,
and all other brackets are `>= 0`, so

```text
2m  <=  sum_{i=1}^m bracket_{l_i}  <=  sum_{l in L_F} bracket_l  =  N-1 = 3.
```
Hence `m <= 3/2`, i.e. `m=1`.  QED

Three remarks on the ledger.

- Theorem 10.1 uses neither (2.3), (2.3'), Proposition 4.3, nor the
  companion census: only Proposition 5.3 (the new ingredient), the promoted
  inertia constraint, and the quoted Orevkov formula.  Provisional
  Lemma 2.3's *conclusion* may therefore be de-conditionalized on (2.3),
  while its *statement* must be repaired to (2.3') or restricted by
  Corollary 5.5.  Every row killed by Lemma 2.3 stays killed, and rank four
  collapses onto the irreducible one-place ladder as intended.
- The ledger's Lemma 2.2 (`m <= 3`) is untouched by the `s_l` defect: its
  proof consumes `3 = N-1 >= sum_l mu_l >= #Irr(A_F)`, which is an
  inequality in the safe direction, and the `s_l` factor only strengthens
  it.
- The residual risk of the rank-four reducible-row emptying is now
  concentrated in a single external citation, Orevkov 1987 Lemma 4.2 as
  quoted by Chau 1999 Remark 4.9, together with readings (C1) and (C3).
  (C1) is confirmed verbatim from Chau 1999; (C3) is not.

## 11. Blocked and declined computations

No CAS was run.  None was needed: every computation here is a two-line
substitution in a toric chart at infinity, a Riemann--Hurwitz count, or a
local intersection number, done by hand (K2 was computed twice, by an
explicit chain of point blowups and by the weight-`(2,-1)` chart, with
agreement).

Two reference PDFs already in `refs/` were read with `pdftotext -layout`
(text extraction, sub-second, read-only): `chau1999_apm71_full.pdf` for
Remark 4.9 / formula (4.9), and `chau2004_nonproper_value_set_arxiv_
math0305088.pdf` for Lemma 1, Theorem 1 and Corollary 2.  The known
stacked-fraction extraction hazard does not affect the quoted material,
which is prose plus a single displayed double sum.

Declined, with reasons:

```text
- Any Groebner/resultant search for a Keller-type map with s_l >= 2:
  the relevant family is not a finite desk-scale search and would need a
  CAS of uncertain duration.  BLOCKED by the computation rule; recorded
  as OPEN-1 instead.
- Machine computation of A_F for the controls (K1)-(K4) via
  Res_y(P-u, Q-v): replaced by hand arguments (explicit solvability and
  explicit properness over {a != 0}).  Not needed.
- Reading Orevkov 1987 [O1] itself: not present in refs/.  Recorded as
  OPEN-3.
```

## 12. Open items and successor

```text
OPEN-1 (typed OPEN, non-blocking).  Can a noninvertible plane Keller map
  have a dicritical l with s_l >= 2?  Constraints proved here: at N=4 it is
  impossible when mu_l >= 2 (Corollary 5.5); when mu_l = 1 it costs at
  least s_l of the budget N-1; and by Chau 2004 Theorem 1 the
  parametrization degrees (md, me) of the image force s_l | m, the
  parametrization being a polynomial in (xi-c)^{s_l}.  A general answer
  would let the ledger state (2.3) as a theorem instead of a hypothesis.
OPEN-2 (typed OPEN).  Reading (C3): deg_u f^* (Orevkov's topological local
  degree) = mult_u(Phi) (algebraic local degree).  Asserted, not proved.
  Affects Proposition 4.3, Corollary 5.5 and, through the bracket bound
  only, nothing in Theorem 10.1.  Also unpaid: Orevkov's source model
  implies no type-(C) boundary component for a Keller map.
OPEN-3.  Orevkov 1987 Lemma 4.2 is consumed as quoted, not re-derived.
OPEN-4 (cheapest successor).  Exclude mu_l = 1 dicriticals over a branch
  component of a rank-four block.  By Proposition 5.3 they are exactly the
  configurations invisible to the divisorial inertia (control (K4) realises
  one for a non-Keller map), and they are the only remaining route by which
  a component's finite fibre could be smaller than the census value u_i.
  Excluding them makes Corollary 5.4(3) unconditional and removes the last
  dependence of (2.3) on the degree-four budget.
```

Recommended ledger repair, for whoever holds the canonical file (I have
edited nothing): in provisional Lemma 2.3, replace (2.3) by (2.3') of
Theorem 5.1, add Proposition 5.3 as the justification of the per-component
mass `N-f(B_i) >= 2`, and cite Theorem 10.1 for the conclusion `m=1`.  The
proof text "Corrections in Orevkov's sum are supported at special points of
dicritical lines, hence vanish at generic `z`" is correct as far as it goes
(Section 6 proves it) but is not sufficient for the equality, because the
`s_l` multiplicity is generic, not a correction.

<!-- BODY-END -->
