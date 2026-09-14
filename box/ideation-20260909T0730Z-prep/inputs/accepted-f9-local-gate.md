# Hostile Sol review: degree-seven local consumers and exact F9 composition

**Tag:** `f9-degree7-local-composition-gate-sol-20260909`  
**Role:** independent hostile reviewer (`sol`)  
**Frozen basis:** `0d39df3c9fd69c939a8420c54d03228b9077777d`

## Review boundary and method

This review is confined to the eight charged frozen files in `/tmp/jc2-lane.0KpMER/inputs`. Provenance paths named inside them are treated as quotations, not as access authority. The weighted-reference and source imports are consumed only at the exact scope granted by `08-review-scope.md`; their interiors are not reopened unless the new composition raises a named doubt. The transaction is used only as completed-body provenance. No acceptance is inferred from producer language, root agreement, or prior validator verdicts.

The review tests targets A–F independently, retaining zero-scalar cases, infinite orders, endpoint cases, tied terms, and possible cancellations. The construction ledger below records the initial unsealed scope; the completed verdict ledger in Section 8 supersedes its placeholders.

## Initial target ledger (unsealed construction record)

- **A — pending audit:** exact 16d-to-local hypothesis composition.
- **B — pending audit:** simple-line consumer for every `j <= 13`.
- **C — pending audit:** double/coalesced consumers in both stated ranges.
- **D — pending audit:** separated consumer in both stated ranges.
- **E — pending audit:** exhaustive factor/multiplicity composition.
- **F — pending audit:** exact external/source conclusion and finite-ideal unit conclusion.

## Evidence and OPEN ledger (unsealed)

The final evidence findings, typed OPENs (if any), retained scope, exact verdicts, dependency limitations, and terminal handoff will be appended below after all eight charged inputs have been read in full.

## 1. Custody and charged-evidence check

I read all eight charged files whole. The full SHA-256 of `01-new-local-proof.md` is `39ca337801d3c8862fbe9d1174eaf72162a53ba2ecf1d941df0504c0be6acb85`, exactly the `full_sha256` recorded by `02-new-local-transaction.json`; its recorded completed-body hash is `4e79c2302d7b547f6c353898d0130f7319c3842efa3f4337755e847e5214f884`. The accepted weighted theorem and its gate hash to the values named by the new proof and scope file. This verifies provenance only, not mathematics.

No live or provenance path named inside an input was opened. I did not read the excluded compatibility proof, supporting separated report, old degree-five proof, live D108 material, source originals, PINS, ledgers, or peer reports. No mathematical subprocess, coefficient expansion, sampling, CAS, solver, web access, agent, or external/shared write was used. The calculations below are manual hostile checks of the factored text.

## 2. Target A — CONFIRMED

**First failing arrow:** none. **Exact retained scope:** the accepted 16d polynomial-reference interface, not its proof interior, plus the explicit local argument under that interface.

The accepted parent supplies exactly the needed characteristic-zero data: finite combined-homogeneous `A_s,B_s,R_s,F,G` of degrees `21,35,7,21,35`; the full expansion `R_s=K+sum_(i=1)^7 s^i R_(7-i)`; all scalars `alpha,a0,b0,...,b4`; the displayed `q_s`; `F != 0`; `1 <= j <= 13`; `F_j=K C` with `deg C=14-j` and `K` not dividing `C`; and `ord_s G >= 2j`, including infinite order. The five `B` kernels remain present. Nothing in the local consumers requires constant Jacobian, inverse polynomiality, lower-face support, an old degree bound, or a symmetry between distinct lines.

The map `k[g,p] -> k[a,b]`, `g -> a^2`, `p -> b`, is injective. Its determinant contribution is `2a`, so `[A,B]=c g` pulls back to `2c a^3`; homogeneous dilation gives exactly `2c s^51 a^3`. In the uniform local coordinates `y=b, X=a`, reversing the variable order gives the required target

    [A_s,B_s]_(y,X)=-2c s^51 X^3.

Thus both `2a` and the chart-swap minus sign are retained. The generic coordinate `X` is nonzero and transcendental; no claim is made at `X=0`. Passing to an algebraic closure only enlarges the coefficient field: nonexistence there implies nonexistence over the starting field, while no normalization is claimed to descend back through that extension.

## 3. Target B — CONFIRMED

**First failing arrow:** none. **Range:** every simple factor and every `j <= 13` allowed by A.

At a simple line `K_y` is a unit over `k(X)`, so the complete formal inverse with `z=R_s` exists and has nonnegative `s`-order. Combined homogeneity survives the inverse: `s,X` have degree one and `z` degree seven. Modulo `s`, `F_j=K C` becomes `z` times a unit at the selected generic line. Hence, for `F=sum f_n z^n`, all `ord f_n >= j`, `ord f_1=j`, and `q0=ord f_0>j`, with `q0=infinity` allowed.

For `eta=min(j/2,q0/3)`, `eta` is finite and positive, `eta <= 13/2 < 7`, and after `z=s^eta Z` the entire `F` initial has order `3eta` and is `uZ+v` with `(u,v) != (0,0)`. Terms of degree at least two have order at least `j+2eta>3eta`. Therefore the actual `A` initial is the nonzero depressed correction

    P=Z^3+uZ+v.

The `alpha s^14 R` and `a0 s^21` terms are strictly later because `14>2eta` and `21>3eta`.

For `B`, every scalar kernel is later than `5eta` by `(5-i)(7-eta)>0`. The `b4` and `b3-5alpha/9` pieces of `q_s F` are later by `7-eta` and `14-2eta`; the retained leading piece `(5/3)z^2F` occurs at `5eta`. Since transformed `G` has coefficient orders at least `2j`, it can contribute only degree zero below `5eta`, and only degrees zero or one at `5eta`. This includes `G=0` and all zero scalar cases.

The inverse multiplies the target by the unit `y_z`; scaling to `Z` adds `eta`. Thus an earlier `B` initial of order `nu<5eta` would satisfy `2eta+nu<7eta<=91/2<51` and must commute with the monic cubic `P`. Its Euler degree is `35-nu`; for a constant initial this is positive, so the first Euler lemma gives a contradiction. A constant earlier coefficient is therefore not discarded—it is eliminated by its Euler contradiction.

At order `5eta`, `B` has a genuine monic quintic initial, including the possible linear and constant `G` terms. With `h=7-eta>0`, the initials have Euler degrees `3h` and `5h`, and the same strict target comparison makes their bracket zero. The second Euler lemma applies with positive monic degrees: the derivative constants of the generic-coordinate algebraic field are the coefficient constants, and UFD factorization forces `P=W^3`, `Q=W^5`. For a monic linear `W`, the absent quadratic term of the depressed cubic forces `W=Z`, hence `u=v=0`, contradicting the actual initial. Both Euler lemmas therefore meet their monicity, degree, derivative-constant, and `h>0` hypotheses.

## 4. Target C — CONFIRMED

**First failing arrow:** none. **Ranges:** transverse multiplicity `d=2, j<=13`, and `d=3, j<=9`, at either double line.

At `y=epsilon X`, the coefficient of `(y-epsilon X)^2` in `K` is exactly `-2epsilon X^5`, a unit over the generic-coordinate field. Solving `R_y=0` gives the moving critical point `y_c`; with `xi=R_s(y_c)` and `kappa=ord_s xi>=1` (infinity allowed), exact Taylor factorization and a square-root extension give

    R_s=xi+zeta^2,

with a full formal inverse of nonnegative `s,zeta` orders and `zeta` of combined degree `7/2`. For `F=sum c_n zeta^n`, all `ord c_n>=j`, `ord c_d=j`, and the coefficients below `d` have order strictly greater than `j`; these statements follow from the complete inverse modulo `s`, not a truncated Taylor polynomial.

Define `r=min_(0<=n<=d) ord(c_n)/(6-n)`. It is positive and finite. In the coalesced regime `kappa>=2r`, including equality and `xi=0`, scaling `zeta=s^rY` makes every term with `n<=d` have order at least `6r`, with a nonzero attained initial `U(Y)` of degree at most `d`. Every `n>d` term is later because `j+(d+1)r>=7r`. The actual monic `A` initial is

    P=(Y^2+b0)^3+U(Y),

where `b0` occurs exactly at `kappa=2r`. All scalar `A` terms are later since `r<7/2`.

The proof controls the whole `B`, not just `qF`: `ord_s(B_s-R_s^5)>=1` survives the nonnegative-order inverse. An initial at `nu<10r` has degree `n` with `nr<=nu-1`. The target comparison is `5r+nu<15r<51`. With `h=7/2-r>0`, the first Euler obstruction is strictly positive:

    35-nu-nh > 35-7nu/(2r) > 0.

So no earlier `B` initial exists. At `10r`, `R_s^5` supplies the unique degree-ten monic term and every part of `B_s-R_s^5` has degree below ten. The second Euler lemma then forces the common monic quadratic. Comparing the two highest lower coefficients (`Y^5` and `Y^4`) makes that quadratic exactly `Y^2+b0`, so `U=0`, a contradiction. The prohibited degree-four correction never enters because `deg U<=3`.

The endpoint margins are strict in both exact ranges:

    d=2: r<=13/4<7/2 and 15r<=195/4<51;
    d=3: r<=3<7/2 and 15r<=45<51.

## 5. Target D — CONFIRMED

**First failing arrow:** none. **Ranges:** the same `d=2,j<=13` and `d=3,j<=9` ranges, in the genuinely separated regime `kappa<2r`.

Here `xi` is nonzero and finite. For every `n`, not only `n<=d`, the coefficient bounds give

    ord c_n+n kappa/2>3kappa.

For `n<=d` this is `(6-n)(r-kappa/2)>0`; for `n>d`, `ord c_n>=j>=(6-d)r` supplies the strict inequality. Even/odd regrouping into `U(z),V(z)` is coefficientwise `s`-adically convergent because the powers of the positive-order `xi` drive the orders to infinity. It yields the exact two sheets

    F_+-=U(z) +- b_s sqrt(1-z/xi)V(z),  ord b_s=kappa/2,

and the coefficient bounds `ord U_l+l kappa>3kappa` and `ord V_l+kappa/2+l kappa>3kappa`. Individual sheet coefficients may have negative orders after division by powers of `xi`; the argument never assumes otherwise.

The definitions of `q0,q1` allow either value to be infinite, while the actual anchors make `eta=min(q0/3,q1/2)` finite and strictly greater than `kappa`: `c_2` gives `ord U_1=j` for `d=2`, and `c_3` gives `ord V_1=j` for `d=3`; every later summand contains a positive power of `xi` and is strictly later. Thus

    d=2: eta<=j/2;
    d=3: eta<=j/2+kappa/4<2j/3;

so `eta<7`. After `z=s^eta Z`, each positive binomial shift is later than its own base by a positive multiple of `eta-kappa`. Bases of degree at least two are later than `3eta`. At an attained degree zero or one, the two sheet initials form `(a+b,a-b)`, which cannot vanish on both sheets. Hence the two actual depressed cubics have a nonzero correction on at least one sheet; no one-sheet cancellation or generic sample is used.

The same regrouping is applied to the entire `G`. Its base coefficients have order at least `2j`, and the global base minima exist because the bounds tend to infinity with degree. A shifted term cannot be a first global minimum: it is later than its own base. At a minimum the two-sign tuple prevents cancellation on both sheets. Below `5eta`, the earliest possible base has degree zero for `d=2` (`2j>=4eta`) and at most one for `d=3` (`2j>3eta`). The scalar kernels and lower `q_s` terms are strictly later, while `z^5` and `(5/3)z^2F` start at `5eta`. The first Euler lemma, including the degree-one factor `28-nu+eta>28-4eta>0`, excludes every earlier whole-`B` initial.

The sheet change contributes the genuine pole `y_z=y_zeta/(2zeta_+-)`, so the target order is `51-kappa/2`; scaling by `z=s^eta Z` adds `eta`. This determinant calculation already includes the `X`-dependence of the inverse. The required strict comparisons are

    d=2: 7eta+kappa/2 <= 7j/2+kappa/2 < 15j/4 <=195/4<51;
    d=3: 7eta+kappa/2 <= 7j/2+9kappa/4 < 5j <=45<51.

At `5eta`, no earlier base remains whose binomial shift could reappear; the complete `G` contributes at most linear and constant terms. Each sheet therefore has the exact monic quintic initial

    Q_+-=Z^5+(5/3)Z^2(u_+- Z+v_+-)+ell_+- Z+e_+-,

of Euler degree `5(7-eta)`. The common-linear Euler lemma forces `u_+-=v_+-=0` on each sheet, contradicting the nonzero two-sign tuple. This is a separated-sheet argument, not a rename of the coalesced chart or a symmetry assertion about the two distinct double factors.

## 6. Target E — CONFIRMED

**First failing arrow:** none. **Exact retained scope:** factorization after scalar extension, followed by the already confirmed local consumers.

Over the algebraic closure, `K=M^2V` has three distinct simple lines from `V=b(b^2-3a^2/2)` and two distinct double lines `b-a,b+a` from `M`. For each simple line, failure to divide `C` would give the prohibited simple-line hypothesis, so all three divide `C`. At either double line, failure to divide `C` would make the multiplicity of `F_j=KC` exactly two, prohibited for every `j<=13`; hence both double lines also divide `C`.

Thus `rad(K)`, of degree five, divides the nonzero polynomial `C` of degree `14-j`, forcing `j<=9`. Since `K` does not divide `C`, and all five lines already occur in `C`, at least one double line occurs in `C` with multiplicity exactly one. It then occurs in `F_j` with multiplicity exactly three, contradicted by the `d=3,j<=9` consumer. This neither equates the multiplicities of the two double lines nor confuses the two local sheets over one selected line with those two distinct factors.

## 7. Target F — CONFIRMED

**First failing arrow:** none. **External dependency boundary:** accepted 16a/b and their expressly imported primary statements for forward source attachment; accepted 16c plus its reviewed reverse contract only for identifying the finite guarded source ideal.

The local result itself says that no characteristic-zero weighted `21/35` receiver with leaders `H^3,H^5` and bracket `c g`, `c != 0`, can satisfy the accepted 16d interface. Accepted 16a/b state that every actual ordinary complex Keller counterexample of exact degrees `84/140` produces precisely such a normalized receiver. Therefore the forward composition excludes actual ordinary `84/140` counterexamples at that accepted import tier. Reverse ordinaryness is not used in this implication.

Separately, the accepted reverse contract identifies the same finite guarded 16c ideal `I_F9` over `Q` and proves: it is proper exactly when an actual complex `84/140` counterexample exists. The exclusion therefore makes `I_F9` the unit ideal (equivalently, no complex zero and Nullstellensatz/faithful scalar extension give `1 in I_F9`). This is only an existential unit conclusion. It supplies no displayed cofactors, computed certificate, coefficient emission, solver run, or new specialization. Reverse ordinaryness remains relevant only to that exact ideal equivalence.

No conclusion is drawn about a maximum degree of `140`, a degree census, configurations `126/128/132/135`, arbitrary partial degrees, all-degree JC2, or a public/literature proof. No source point is exhibited or claimed; rather, the exact `84/140` candidate class is excluded. The result also does not upgrade the accepted source imports beyond their stated field and theorem-interior perimeter.

## 8. Exact verdict ledger, dependencies, and terminal handoff

- **A: CONFIRMED.** Exact 16d-to-local hypotheses, cover determinant, order-51 target, chart sign, fields, degrees, normalization, and `F/G` interface compose.
- **B: CONFIRMED.** The simple consumer covers every `j<=13`, including constant earlier `B`, infinite `q0`, zero scalars, and `G` at and below `5eta`.
- **C: CONFIRMED.** The coalesced consumer covers `d=2,j<=13` and `d=3,j<=9`, including `xi=0`, `kappa=2r`, all `c_n`, and the whole `B`.
- **D: CONFIRMED.** The separated consumer controls both sheets and the entire `G/B`, negative individual sheet orders, `X`-dependent chain rule, anchors, cancellations, and both strict endpoint ranges.
- **E: CONFIRMED.** The five-factor cover and exact multiplicity-one-at-some-double-line step are exhaustive without a false equality assumption.
- **F: CONFIRMED.** Exact ordinary `84/140` exclusion and, separately, existential unit status of the same guarded 16c ideal follow at the accepted dependency perimeter.

There is no REFUTED or GAP target and therefore no retained partial caused by a failing arrow. The conditional dependencies remain load-bearing: removing the accepted 16d interface voids A and all downstream local composition; removing either local double regime voids E; removing accepted 16a/b leaves the local weighted theorem intact but voids the ordinary `84/140` attachment; removing the accepted reverse contract leaves that exclusion intact but voids identification of the guarded ideal and its unit conclusion.

## OPEN(S) RAISED

None. The undecided questions outside this exact degree pair and outside the accepted import perimeter are limitations, not new OPEN entries.

## Terminal handoff

The substantive hostile review is complete. Root alone may adjudicate or promote it; this report authorizes no descendant, computation, external message, or public action.
<!-- BODY-END -->
