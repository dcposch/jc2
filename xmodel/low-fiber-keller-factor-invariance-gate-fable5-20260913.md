# Keller right-factor invariance under low-fiber chains — different-model FIRST

Fable 5.1, September 13 2026. MANUAL / DIFFERENT-MODEL FIRST of ROOT's
CLAIM.md (low-fiber postcomposition preserves polynomial Keller right
factors). Consumed without reverification: Keller mapping degree 2,3
excluded; no strict intermediate K<M<L with [M:K]=2,3; birational Keller
is an automorphism; finite/proper plane Keller is an automorphism;
TOWER-FIRST and EMBEDDED-FIRST at their stated conditional tiers.

## Verdict summary

- Main theorem (right-factor set equality, unique `i_0`, `i=phi_m...phi_1 i_0`, no bound on `[L:E_0]`): **CONFIRMED**.
- Section 1 compositum inequality and last strict drop, including `M_0=K E_0 != L`: **CONFIRMED**.
- Section 2 lemma `R cap Frac(A)=A` for dominant quasi-finite plane maps, and polynomial (not merely rational) descent: **CONFIRMED**.
- Section 3 finite-source corollary: **CONFIRMED**. Source-coordinate corollary: **CONFIRMED**; the principal kernel, `Omega_(R/A)=0`, and unit-derivative steps are unwritten in CLAIM.md and are supplied below. A free strengthening (rational source coordinate) is recorded.
- Section 4 all-fiber application to `G`, identity stabilizations, conjugations, finite compositions: **CONFIRMED**, with the reading that conjugation is by polynomial automorphisms.
- Degree-six and degree-four controls, projection exclusion: **CONFIRMED** as stated; the degree-four control refutes only the hypothesis transfer, not the conclusion (no conclusion-failure control can exist short of a JC2 counterexample).
- Section 6 strategic consequence: **CONFIRMED** for the full-output factorization shape only; arbitrary initial `j`, restricted steps of degree `>=4`, projections, and JC2 stay open.
- No REFUTED item and no GAP inside the charged claim. No numerical smooth-degree or monodromy statement is inferred.

Notation below follows CLAIM.md: `L=C(x,y)`, `K=C(f,g)`, `R=C[x,y]`, `A=C[f,g]`, `E_r=C(Z_r)` pulled back into `L`, `M_r=K E_r`.


## 1. Compositum inequality and the last strict drop

Pullback along the dominant `j_r:A2->Z_r` embeds `E_r` in `L`; the restricted dominant map `Z_(r-1)->Z_r` gives `E_r subset E_(r-1)` compatibly, and `[E_(r-1):E_r]<=3` is the hypothesis. From `j_m=i h` every coordinate of `j_m` is a polynomial in `f,g`, so `E_m subset K` and `M_m=K`. Nothing about `i` beyond polynomiality is used.

**Inequality.** The `M_r`-linear map `E_(r-1) tensor_(E_r) M_r -> L` has image the subalgebra `M_r[E_(r-1)]`, spanned over `M_r` by an `E_r`-basis of `E_(r-1)`, so of dimension `<=[E_(r-1):E_r]`. A finite-dimensional domain over a field is a field, so the image is the compositum `M_r E_(r-1)=K E_r E_(r-1)=K E_(r-1)=M_(r-1)`. Hence `[M_(r-1):M_r]<=3`. Only this inequality is used; no divisibility or equality is claimed anywhere. Sol's `Q(cuberoot 2, zeta)` control in TOWER-FIRST shows equality and divisibility both fail in general, and I found no step of CLAIM.md that silently uses either.

**Last strict drop.** `L/K` is finite: the nonzero Jacobian makes `f,g` algebraically independent and `x,y` algebraic over `K`. So every `M_r` is an actual intermediate field `K subset M_r subset L`, finite over `K`. Suppose `M_0 != K`. Let `r` be the largest index with `M_(r-1) != M_r`; then `M_r=...=M_m=K` and `1<[M_(r-1):K]<=3`, so the degree is exactly 2 or 3. Exhaustive dichotomy: `M_(r-1)=L` gives Keller mapping degree 2 or 3, excluded by premise 1; `K<M_(r-1)<L` is a strict intermediate field with second leg 2 or 3, excluded by premise 2. Hence `M_0=K`, i.e. `E_0 subset K`.

**The case `M_0 != L`.** This is the only place the new theorem departs from TOWER-FIRST, where `M_0=L` because `[L:E_0]<=3` was itself a tower step. Here `M_(r-1) subset M_0 != L`, so only the second branch can fire, and premise 2 does all the work. Premise 2, as consumed, applies to every intermediate field of the finite extension `L/K`, not only to fields of a special geometric shape, so no hidden hypothesis on `M_(r-1)` is needed. `[L:E_0]` never enters: `L/E_0` can have any degree, and the chain is never compared against `L`. **CONFIRMED.**

Attacks tried: equal `M`-steps with strict `E`-steps (harmless, the argument only reads the `M`-chain); `M_(r-1)` failing to be a field (impossible, it is a subfield of `L`); premise 2 needing `[L:M]` control (it does not, the consumed statement bounds `[M:K]` only); `m=0` (vacuous, fine).


## 2. R ∩ Frac(A) = A and polynomial descent

**Lemma replay.** `F=(f,g)` dominant quasi-finite, so `A=C[f,g]` is isomorphic to `C[U,V]` and elements of `Frac(A)` are `a(f,g)/b(f,g)` with `a,b` coprime in `C[U,V]`. Assume the quotient lies in `R` and `b` is nonconstant. Take an irreducible `p | b`. Then `p(f,g)` is a nonconstant polynomial, since `p(f,g)=c` would be an algebraic relation `p-c=0`. Take an irreducible `q | p(f,g)` in the UFD `R` and `C=V(q)`, an irreducible curve. `p` vanishes on `F(C)`, so `F(C) subset V(p)`; `F(C)` is infinite because fibres are finite, hence Zariski-dense in the irreducible curve `V(p)`, whose proper closed subsets are finite. If `a(f,g)` vanished on `C`, `a` would vanish on `F(C)` and therefore on `V(p)`, so `a` would lie in `I(V(p))=(p)` by the Nullstellensatz (`(p)` is prime, hence radical), contradicting coprimality. So `q | b(f,g)` and `q` does not divide `a(f,g)`. If `a(f,g)=r*b(f,g)` with `r in R`, then `q | a(f,g)`: contradiction. Thus `b` is constant. **CONFIRMED.**

**Cancellation at divisors.** The numerator and denominator `a(f,g)`, `b(f,g)` may share factors in `R` even though `a,b` are coprime upstairs; the argument is immune to this, because it exhibits one prime `q` of `R` dividing the denominator and not the numerator, which in a UFD is exactly the statement that the reduced fraction is not in `R`. No reduction step is needed.

**Keller maps qualify.** `J(f,g)` a nonzero constant gives `f,g` algebraically independent (dominance) and `h` étale, hence unramified, hence quasi-finite. So `R cap K = A`.

**Polynomial descent.** Each coordinate `j_k` lies in `R` and, by Section 1, in `E_0 subset K`. So `j_k in A`, i.e. `j_k=P_k(f,g)` with `P_k in C[U,V]` unique because `C[U,V]->A` is injective. Setting `i_0=(P_1,...,P_(n0))` gives `j=i_0 h` with polynomial `i_0`; no denominator survives, so this is polynomial, not merely rational, descent. **CONFIRMED.**

**Negative control.** `F=(x,xy)`: the fibre over `(0,0)` is the line `x=0`, quasi-finiteness fails, `y=(xy)/x` lies in `R cap C(x,xy)` and not in `C[x,xy]`, and `J=x`. Checked; it isolates quasi-finiteness as the load-bearing hypothesis.


## 3. Uniqueness and both implications

- Uniqueness of `i_0`: if `i_0 h=i_0' h` then `i_0-i_0'` vanishes on the dense set `h(A2)`, so `i_0=i_0'`. The same argument makes `i` unique given `j_m=i h`.
- `i=phi_m...phi_1 i_0`: `j_m=phi_m...phi_1 j=(phi_m...phi_1 i_0) h` and `j_m=i h`; dominance of `h` identifies the two left factors.
- Reverse implication: `j=i_0 h` gives `j_m=(phi_m...phi_1 i_0) h` by composition; no hypothesis on the chain is needed for this direction.

All three: **CONFIRMED.** The equivalence is therefore an exact equality of the two right-factor sets `{h : j_m = i h}` and `{h : j = i_0 h}` over polynomial Keller `h`.


## 4. Finite-source properness and the monogenic coordinate argument

**Finite source.** With `j=i_0 h`, the graph morphism `(id,h):A2_s -> A2_s x_(A^n0) A2_t` is well defined because `j=i_0 h`, and is a closed immersion because the base `A^n0` and the map `i_0` are separated. The second projection is the base change of `j` along `i_0`, hence finite when `j` is finite (finiteness is stable under base change). A closed immersion followed by a finite map is finite, so `h` is finite directly; the CLAIM's route via proper plus quasi-finite (Zariski) is also valid. The accepted finite Keller automorphy premise then applies. A proper affine `j` is finite, so the same argument runs. **CONFIRMED.**

**Coordinate source: principal kernel.** Let `a in D subset A` (Section 2), `b` a complementary coordinate, so `R=C[a,b]=A[b]`. Let `P` be the kernel of `A[T]->R`, `T->b`. It is nonzero because `b` is algebraic over `K` (`L/K` finite), prime because `R` is a domain, and of height `3-2=1` in the affine domain `A[T]` (isomorphic to `C[U,V,T]`, dimension 3, quotient of dimension 2). Height-one primes of a UFD are principal, so `P=(P)` with `P` irreducible, hence primitive in `T`, and of positive `T`-degree since a nonzero element of `A` is nonzero in `R`. Equivalent route: clear denominators of the minimal polynomial of `b` over `K` to a primitive `P in A[T]`; any kernel element is divisible by `P` in `K[T]`, and Gauss's lemma lifts the divisibility to `A[T]`.

**Relative differentials and unit derivative.** `Omega_(R/C)=R dx + R dy` and `Omega_(R/A)` is its quotient by the `R`-span of `df, dg`. The transition matrix from `dx,dy` to `df,dg` is the Jacobian, whose determinant is a unit, so `df,dg` span and `Omega_(R/A)=0`. From the presentation `R=A[T]/(P)`, the conormal sequence gives `Omega_(R/A)=R dT/(P_T(b) dT)=R/(P_T(b))`. Hence `P_T(b)` is a unit of `C[x,y]`, i.e. a nonzero constant `lambda`.

**Conclusion of the descent.** `P_T-lambda` lies in the kernel `(P)` and has `T`-degree below `deg_T P`; a nonzero multiple of `P` in the domain `A[T]` has `T`-degree at least `deg_T P`, so `P_T=lambda`, `P=lambda T+P_0` with `P_0 in A`, and `b=-P_0/lambda in A`. Thus `R=A[b]=A` and `h` is an automorphism. **CONFIRMED**; the three steps the task asked to justify are all elementary and now written.

**Free strengthening (not a correction).** Section 2 gives `R cap Frac(D) subset R cap K = A`. So the corollary holds whenever a source coordinate is a RATIONAL function of the coordinates of `j`, not only a polynomial one. Example: `j=(st, s t^2, 0)` has `D=C[st, s t^2]`, whose every element has vanishing differential at the origin, so `D` contains no coordinate; but `t=(s t^2)/(st) in R cap Frac(D)`, so every Keller right factor of `j`, and by the theorem of any admissible chain image of `j`, is an automorphism. Generically injective `j` (`Frac(D)=L`) gives `R=A` outright. ROOT may adopt this at no cost; it widens the discard test.


## 5. Degree-six control, all-fiber application, projections

**Degree-six control.** `j=(s, s t^6, 0)`: image closure is the plane `z=0` (dimension 2); over `(s_0,u_0,0)` with `s_0 != 0` the fibre is the six roots of `t^6=u_0/s_0`, so the generic degree is 6; the fibre over `(0,0,0)` is the line `s=0`, so `j` is not finite; `D` contains `s`. The coordinate corollary therefore applies after every chain satisfying the theorem. It is not a Keller map and carries no JC2 degree statement. **CONFIRMED.**

**All-fiber application.** EMBEDDED-FIRST gives every point fibre of `G` at most three points. `G x id` has fibres equal to fibres of `G` times a point. Conjugation `psi^-1 G psi` by a polynomial AUTOMORPHISM `psi` puts fibres in bijection; conjugation by a non-invertible polynomial map would not preserve the bound, so CLAIM.md's "polynomial conjugations" must be read as automorphisms, which is what equation (54) of the cited source uses (`Psi` with polynomial inverse, `sigma` a swap). Restriction: by continuity `Z_r` is the closure of `phi_r(Z_(r-1))`, the restricted map is dominant, its fibres sit inside ambient fibres so have at most three points, hence it is quasi-finite, `dim Z_r=2` is automatic, and in characteristic zero the generic fibre has exactly `[E_(r-1):E_r]` points, so the degree is at most three. A finite composition is handled one step at a time; no bound on the full iterate's fibre count is used. **CONFIRMED.**

**Degree-four control.** `phi=(a,ab,c,d)` is birational; on `j=(0,s,s^4,t)` the restricted map is `(0,s,s^4,t)->(0,0,s^4,t)`, degree 4, and the ambient fibre over `(0,0,c,d)` contains a free `b`. Verified. It shows only that generic ambient degree does not transfer. It is not a conclusion-failure control: `h=(s^4,t)` is not Keller, and no conclusion-failure control can exist without a JC2 counterexample, since if every Keller map is an automorphism both factor sets are trivially equal. That vacuity is inherent to every construction filter, not a defect of this claim.

**Projections.** `h=pi j_m` gives `K subset E_m`, the reverse of the containment `E_m subset K` that starts Section 1. Correctly excluded. **CONFIRMED.**


## 6. Strategic consequence and scope

The theorem does change the initial-factor test, for one shape: full-output factorization `j_m=i h` with polynomial `i`. The Keller right factors of `j_m` are exactly those of `j`, so finite `j` and (rationally) coordinate-containing `j` can be discarded before any chain of `G`-type steps is built, with no bound on `deg j`, on the chain length, or on coefficients. Against TOWER-FIRST the genuine gains are the unbounded initial degree and the factor-set form of the conclusion. **CONFIRMED.**

Open and untouched, exactly as CLAIM.md states: initial `j` with no independent Keller-factor exclusion (non-finite `j` whose coordinates generate a field containing no source coordinate); restricted steps of degree at least 4, including generically birational ambient maps with infinite exceptional fibres; arbitrary projections; factorizations with merely rational `i`; JC2 itself. Long's four-dimensional instance stays conditional on the cited source data per EMBEDDED-FIRST. No numerical smooth-degree or monodromy consequence follows, and none is inferred here.

Recommendation: promote at MANUAL / PROVED tier, conditional on the four consumed premises and on the conditional tiers of TOWER-FIRST and EMBEDDED-FIRST; record the rational-coordinate strengthening of Section 4 as a producer-side amendment candidate.

## Metadata, custody and disclosures

- CLAIM.md `940942db7942e0588677e5f10b17c1dbddf7961bb02a3a84e58c1ce3f3f853ca`
- COORDINATION.snapshot.md `77ec0b282f4813ee9a2b71ebced492cc6f0b9262acf90a28f444ed9a507190bd`
- EMBEDDED-FIRST.md `12799476c027a8b8d96c6e153c62471e5579d6303da6c1b90f09fda431838b29`
- TOWER-FIRST.md `63e69b73ced5f3b5026632f4c6e70c70a83daaa90ae39d6e1da3f4688b6418d5`
- Hashed at 11:07:52 UTC before review; all four read WHOLE from `/tmp/jc2-lane.VezVLm/inputs` only: COORDINATION in eleven reads of at most 80 lines, CLAIM in three, the two FIRSTs in one each; EOF bytes checked with `od`, no clipping observed. No other file, link or corpus was read. Post-draft rehash is appended after readback.
- Authoring disclosure: no `apply_patch` binary exists on this host (checked `compgen`, `ops/`, local bin). The report was authored with GNU `patch` applied to unified diffs supplied on stdin, the nearest patch-based equivalent. No Write/Edit tool, shell redirection, heredoc file write, substitution script or interpreter touched the file. First patch attempt failed as malformed (miscounted hunk lengths) and changed nothing.
- Times: start 11:07 UTC, skeleton 11:12, sections 1-3 11:14, sections 4-6 and metadata by 11:17.

- Post-draft rehash at 11:16:14 UTC: all four input hashes unchanged and equal to the pins above. Complete readback done in two bounded chunks (lines 1-80, 81-100) with EOF bytes checked. Word count 2220 by `wc -w`, which counts the four 64-hex hash tokens and code tokens; prose is within the 2200-word target.
- No tool-boundary violation beyond the disclosed patch-tool substitution. No shared ledger, protected tree, network, process control, CAS or scientific interpreter was used; no other report or file was written.

<!-- BODY-END -->
