# Full-normalization and generic source-pencil genus — hostile gate (Fable 5.1)

- lane=full-normalization-genus-scope-gate-fable5-20260912
- reviewer=Fable5.1 (independent hostile), status=MANUAL/PROVISIONAL, no descendants
- first_action_utc=2026-09-12T07:19:15Z (skeleton written 07:19:27Z, before any body read)
- reserve=07:38Z HARD=07:41Z (never extend)
- target=xmodel/full-normalization-genus-scope-astra-20260912.md

## 0. Custody (prepins, hashed before any body read)

Rows generated from sha256sum at 07:19:27Z on /tmp/jc2-lane.k33Qad/inputs. Every row equals the expected value in the charge.

5f9be737ef4a37be884be4655b9d19de9284f1abdd16bdbe5d08454dd40b35d9  prepin full-normalization-genus-scope-astra-20260912.md
cc1eaca421d769e576ef454780421b88a7fceb30c3bb87f7c386ccb0dd25a59b  prepin genus-zero-block-landing-gate-fable5-20260912.md
ad774a4c1e6bf06f4653ecb7d5243e87ed240710677f0300b7bbf5858538bff2  prepin genus-one-block-landing-gate-fable5-20260912.md
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  prepin keller-pencil-genus-opus5-20260902.md

Read mode: each snapshot read WHOLE including seals (four parallel reads, after the hashes). No reference followed, no other source, no code/CAS/arithmetic execution, no network/git/process inspection. Every check below is manual.

## 1. Claim, premises, verdict summary

Claim (Astra sections 1-3): F=(f,g) a hypothetical noninvertible complex Keller map, A=C[f,g], B the integral closure of A in the FULL field C(x,y), Y=Spec B, Ybar the finite normal projective normalization of P2 in C(x,y), L=Phi^*O(1). Then (i) B is literally inside C[x,y] and j: A2 -> Y is an open immersion; (ii) the free group on missed prime divisors injects into Cl(Y); (iii) Hom_A(B,A) is not free; (iv) H1(Ybar,O)=0 and the accepted genus-zero/genus-one exclusions apply to this source; (v) the general net member is the smooth completion of the generic pencil fibre, so its genus is at least two for generic direction and generic t; (vi) no ceiling and no finite-search client follow.

Accepted, not re-hardened: the promoted scroll donor theorem at the first-leg quantifier recorded in the genus-zero gate (its D); the genus-zero gate's complete-series/classification chain (its B, C, E) and the genus-one gate's reflexive-adjunction lemma (its A-C) with its structure-morphism upper-shriek canonicity (its D). Not used: the genus-zero gate F all-line affine ramification counts; the genus-one elliptic-cone aside; anything in the old pencil report above its own PROVED-HERE/UNREVIEWED tier.

Verdicts: A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED (one recorded-scope import named). E CONFIRMED. F CONFIRMED. No REFUTED item, no GAP at the charged scope.

## 2. Claim A — B inside C[x,y], quasi-finite birational, ZMT open immersion: CONFIRMED

Finiteness. A is a finitely generated C-domain and [C(x,y):C(f,g)]=N is finite because F is dominant (a nonzero Jacobian forces f,g algebraically independent). The integral closure of a finitely generated domain over a field in a finite extension of its fraction field is a finite module. Every b in B satisfies a monic equation with coefficients in A, a subring of C[x,y]; b lies in C(x,y) and C[x,y] is normal, so b is in C[x,y]. Hence A inside B inside C[x,y] literally, and j^*: B -> C[x,y] is that inclusion.

Open immersion. j is a morphism of affine finite-type C-schemes, hence separated; F = g2 o j; each fibre of j sits inside a fibre of F, finite because F is etale (Keller), so j is quasi-finite; Frac B = C(x,y) and j is dominant (injective pullback), so j is birational. Zariski's Main Theorem in Grothendieck's form (quasi-finite separated birational finite-type morphism from an integral scheme to a normal integral scheme) makes j an open immersion. Neither surjectivity nor properness follows and Astra asserts neither. Normalization in C(x,y) is local on P2, so Ybar over the target chart is Y and Phi there is g2. B is a two-dimensional normal domain, hence Cohen-Macaulay; a finite CM module over the regular two-dimensional A is locally free (Auslander-Buchsbaum), so g2 is finite flat. On j(A2) the map g2 restricts to F, which is etale, so the non-etale locus of g2 lies in Y minus j(A2).

N > 1 ramification. Zariski-Nagata purity (Y normal, A2 regular, g2 finite dominant): the non-etale locus of g2 is empty or of pure codimension one. If empty, g2 is a connected finite etale cover of complex A2 of degree N, and A2 is simply connected, so N = 1. Hence for N > 1 at least one ramification prime divisor exists, and by the previous paragraph j misses it.

N = 1 exception. Then B = A (A normal, K = Frac A), so j = F: A2 -> A2 is an open immersion. A missed prime divisor of the factorial target is div(a) with a in A inside C[x,y]; a = a(f,g) would be a nowhere-vanishing polynomial in x,y, hence a nonzero constant, so its zero set is empty. Thus the complement of F(A2) has codimension at least two, Hartogs on the normal target gives O(F(A2)) = C[u,v], and since F: A2 -> F(A2) is an isomorphism, C[u,v] -> C[x,y] is onto, i.e. F is invertible. So noninvertibility forces N > 1. Every step checked; no gap.

## 3. Claim B — missed principal divisors and the lattice in Cl(Y): CONFIRMED

Let D_1..D_r be the prime divisors of Y contained in the closed set Y minus j(A2). Suppose sum n_i D_i = div(a) with a in K^*. On the normal Y, a is regular off its polar support and a^{-1} off its zero support (algebraic Hartogs), and both supports lie in the union of the D_i, disjoint from j(A2). So a and a^{-1} lie in O(j(A2)) = C[x,y], whence a is in C^*, div(a) = 0 and every n_i = 0. The map from the free group on D_1..D_r to Cl(Y) is injective. The special case (a nonzero b in B whose nonempty zero set is entirely missed) is the same computation with n_i >= 0: j^*b = b vanishes nowhere on A2, so b is a constant, so its zero set is empty. Inputs used: normality of Y, the open immersion of A, and O(A2)^* = C^*. No proper intermediate field, no d1, no Galois hypothesis, no BD-GAL citation. With A, every ramification component has infinite order in Cl(Y). No gap.

## 4. Claim C — nonfree Hom_A(B,A) by canonical duality: CONFIRMED

Normalization of the module. Set omega_Y = H^{-2}(pi_Y^! C) for the structure morphism pi_Y: Y -> Spec C. Since pi_Y = pi_{A2} o g2, pi_Y^! = g2^! pi_{A2}^!, and pi_{A2}^! C = Omega^2_A[2] = A df^dg [2]. For the finite flat g2, g2^!(M) = Hom_A(B,M) in degree zero with B acting through the first argument. So omega_Y is Hom_A(B,A) as a B-module, the isomorphism depending only on the generator df^dg. This is the same structure-morphism normalization the genus-one gate D made load-bearing; it removes the invertible-twist ambiguity, so the module proved nonfree below is exactly Hom_A(B,A).

The section. omega_Y is torsion-free of rank one and S2 on the normal Y (genus-one gate A), so it is reflexive and equals the pushforward of its restriction to the smooth locus Y_reg, complement of a finite set, where it is Omega^2. The 2-form g2^*(df^dg) on Y_reg therefore extends uniquely to a global section s of omega_Y. Order: at a height-one prime T of B over the height-one prime p of A both local rings are DVRs; characteristic zero makes the extension tame with separable residue fields; with uniformizers t and h, h = u t^e (e = e_T, u a unit) and a common second coordinate q, one has dh^dq = t^{e-1}(e u + t du/dt) dt^dq with the bracket a unit. So ord_T(s) = e_T - 1 >= 0, positive exactly on ramification components, which exist by A because N > 1.

The hypothetical generator. If omega_Y were free it is free of rank one; take a generator eta and write s = b eta, b in B. Restrict to the open j(A2) inside Y_reg: open restriction of pi^! gives omega_Y restricted = Omega^2_{A2} = C[x,y] dx^dy, so eta restricts to c' dx^dy with c' in C^* (a generator of a free rank-one module is a unit), while s restricts to F^*(df^dg) = Jac(F) dx^dy = c dx^dy, c in C^*. Hence j^*b = c/c', and because j^* is the literal inclusion, b = c/c' in C^*. Then s = (c/c') eta generates omega_Y, so ord_T(s) = 0 at every height-one T, contradicting ord_T(s) = e_T - 1 >= 1 on a ramification component. So omega_Y, hence Hom_A(B,A), is not free.

Attacks. Nonempty ramification: supplied by A, not assumed. Finite duality: used with B locally free over A, from A. Codimension-two singular points: they enter only through reflexive extension and the global-generator hypothesis; no smoothness, Gorenstein, rational-singularity or Q-Cartier input appears, and a global generator would make Y Gorenstein as a consequence, not a premise. No gap.

## 5. Claim D — H1(O)=0 and the accepted genus-zero/genus-one proofs on THIS source: CONFIRMED

H1. j followed by Y inside Ybar is a rational map P2 --> Ybar regular on A2; indeterminacy on a smooth projective surface is resolved by finitely many point blowups, giving rho: Z -> Ybar proper and birational (j is birational). Ybar normal gives rho_* O_Z = O_Ybar (Zariski connectedness), and the five-term Leray sequence injects H1(Ybar, rho_* O_Z) into H1(Z,O) = H1(P2,O) = 0. This is the genus-zero gate's route at degree one; it never asserts R^1 rho_* O = 0, rational singularities, Gorensteinness or a Q-Cartier K.

Genus zero. The genus-zero gate's B and C use only Ybar, L and H1 = 0, with d replaced by N = L^2; no d1 occurs. Its D needs a dominant everywhere-defined first leg A2 -> U = Y minus supp Ram(g2); j is one, since j(A2) is dense in Y and misses Ram by A. The recorded quantifier ("every dominant everywhere-defined first leg, finite or not") contains a birational leg. I record this as a consumed import: the donor text is not among my inputs, and a silent use of d1 >= 2 inside that theorem would be a hidden hypothesis; nothing in the recorded statement has one. Its E is replaced by B above: in the rank-one cases Cl(Y) is finite, while A plus B put a copy of Z inside Cl(Y). No proper-block hypothesis survives.

Genus one. The genus-one gate's A-C concern Ybar and the complete series only and output omega_Ybar tensor L = O. L restricted to Y is trivial via the pullback of the section of O(1) cutting the line at infinity, nowhere zero on Y = Phi^{-1}(A2). Open restriction of the structure-morphism upper shriek gives omega_Ybar restricted to Y = omega_Y, the module of C, so omega_Y = O_Y, contradicting C. The single genus-one step that cited BD-GAL (its D, the nonfree relative dual for proper K) is replaced by C, proved for the full field. Both exclusions therefore hold for this source and this affine canonical module. No gap.

## 6. Claim E — line net versus complete |L|; genus >= 2 for the generic fibre: CONFIRMED

The net V = Phi^* H0(P2,O(1)) inside H0(Ybar,L) has dimension three, is base-point free and defines the finite surjective Phi. Members through a point p are the lines through Phi(p), a hyperplane of V; the finitely many singular points give finitely many hyperplanes, so a general net member avoids Sing(Ybar). Smoothness: characteristic-zero Bertini for the base-point-free system on the smooth quasi-projective Ybar minus Sing. Irreducibility, checked explicitly for the finite net: Jouanolou's Bertini theorem for a morphism from an irreducible variety to projective space with image of dimension at least two gives Phi^{-1}(ell) irreducible for general ell; Phi is finite surjective onto P2, so the hypothesis holds. That image-dimension condition, not "non-pencil" by itself, is what Astra's phrase must mean; it is satisfied. Smooth plus irreducible gives integral and connected. The general member of the complete |L| is smooth, integral and disjoint from Sing (genus-zero gate B). Both curves are zero schemes of sections of L, effective Cartier of class L; 0 -> L^{-1} -> O_Ybar -> O_C -> 0 gives the same chi(O_C) = chi(O_Ybar) - chi(L^{-1}) for both, so 1 - g_net = 1 - g_complete. Only the Cartier class is used, no adjunction and no canonical class.

Dense affine part. Phi contracts no curve, so a boundary curve D lies in Phi^{-1}(ell) only if Phi(D) = ell; a general ell is none of the finitely many lines Phi(D), so the irreducible C_net is not inside Ybar minus j(A2) and meets j(A2) in a dense open. Because g2 o j = F, that open is Phi^{-1}(ell) meets j(A2) = j(F^{-1}(ell meets A2)) = j({alpha f + beta g = t}). Hence C_net is the smooth projective completion of the affine curve alpha f + beta g = t and its genus is the sectional genus, at least two by D. Scope: this holds for ell in a dense open of the dual plane, i.e. for all but finitely many directions and, for each such direction, all but finitely many t; not every direction, not every t, no special fibre. For a proper intermediate field the source curve maps with degree d1 onto the block curve and Riemann-Hurwitz changes the genus, so no identification is claimed there; Astra states this. No gap.

## 7. Claim F — controls and scope: CONFIRMED

Controls, verified by hand against the two gates' recorded data. Automorphism: N = 1, B = A, Ybar = P2, L = O(1), sectional genus zero, no ramification; C's contradiction needs a ramification component, so nothing fires. Degree-eight P1 x P1 cover: genus one, omega = L^{-1}, free affine dual, ramified; by C it is not the full normalization of any Keller map, and it shows finite covers alone are unrestricted. P2 with O(4): genus three, so rationality of Ybar gives no upper bound. None uses the unaccepted all-line counts.

Old identities. FORK-GENUS 2g-2 = N - kappa - Lambda + Psi and, under the old H2/profile hypotheses, 2g-2 = -N + n(W-S) - kappa are consumed only at the old report's own PROVED-HERE/UNREVIEWED tier and only for the substitution g >= 2. I re-derived Psi - Lambda >= kappa + 2 - N and n(W-S) >= N + kappa + 2 from those displays; both are floors on fork excess and on n(W-S) and bound nothing above (not n, delta_aff, satellite mass, degree, or any enumeration). The old report's g_L is the genus of the smooth model of the generic pencil member for generic direction, the same object as C_net, so the substitution is type-correct. MF-DEFECT: the old report restates it as "kappa = 1 implies g_L >= 1" (its section 7); E implies g_L >= 2 without kappa = 1, and Astra frames this as a comparison to a dated text, not a current OPEN. Nothing is promoted: no 61 computations, price.py output, driver, CHAIN-CEILING or H2 theorem. No all-genus>=2 exclusion, primitive exclusion, block-existence theorem, degree closure, N=4 consequence or JC2 claim is made, and the text says so.

Missing invariant, exactly: an unconditional Keller-specific upper bound g_L <= 1 on the sectional genus of the full normalization, equivalently Z.K_X <= -N on the resolved source model, or Psi - Lambda <= kappa - N in the old report's language. No input supplies it. Even the old conditional CHAIN-CEILING (Psi = 0, unproved, UNREVIEWED) would give only g_L <= (N - kappa)/2, compatible with g_L >= 2 whenever N - kappa >= 4, so the client is a genuine new ceiling, not a re-reading of old floors. No gap.

## 8. Remaining GAPs

None at the charged scope. Two named imports, not gaps: (1) the scroll donor theorem's recorded first-leg quantifier, consumed as including the birational leg; (2) upper-shriek functoriality (composition and open restriction) identifying omega_Y with Hom_A(B,A). One precision, not a gap: Astra's E should cite the image-dimension hypothesis of Jouanolou's theorem rather than "non-pencil". Writes: this report only; skeleton replaced by write 1, write 2 appended, postpin rows appended from sha256sum output, marker appended last. No artifact_finalize, no charge_basis (no exit-price assertion is made), no seal.

## 9. Postpins (generated from sha256sum after the review text was written)

5f9be737ef4a37be884be4655b9d19de9284f1abdd16bdbe5d08454dd40b35d9  postpin full-normalization-genus-scope-astra-20260912.md
cc1eaca421d769e576ef454780421b88a7fceb30c3bb87f7c386ccb0dd25a59b  postpin genus-zero-block-landing-gate-fable5-20260912.md
ad774a4c1e6bf06f4653ecb7d5243e87ed240710677f0300b7bbf5858538bff2  postpin genus-one-block-landing-gate-fable5-20260912.md
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  postpin keller-pencil-genus-opus5-20260902.md
- postpin_utc=2026-09-12T07:27:24Z

<!-- BODY-END -->
