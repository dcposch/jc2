# keller-trace-image-gate-fable5-20260911 — hostile review of (T)

Reviewer: Fable 5.1 (different model). Skeleton created 2026-09-11 20:14:51 UTC;
body written 20:19–20:25 UTC. Manual mathematics only: no CAS, code, network,
Git or live artifacts. Scientific inputs are the three charged snapshots at
/tmp/jc2-lane.uaHAWi/inputs, hashed BEFORE reading; all three match the
expected values.

| basename | SHA-256 |
|---|---|
| keller-trace-image-root-20260911.md | 76fa7291c32150f8728b704116fdc92171ad40bf4c468bddfb1f01e0bf55c025 |
| yekutieli-9602011v2.pdf | 21fb0150c5c16fbb2d02e9eae0f69aefb5e3d3e3e998d4ea21878107b025470b |
| chau-0305088v1.pdf | 8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f |

Selected scope: ROOT read whole. Yekutieli printed pp27–33 (Section 7,
Theorems 7.1, 7.5, 7.10, Corollaries 7.6–7.9, Example 7.13, and the printed
proofs of 7.5, 7.10, 7.1) read via pdftotext. Chau pp1–2 read for the
nonproper-set interface only. ROOT Section 8 is not reviewed. Nothing outside
these pages is a premise of any verdict below.

## Summary verdict

(T) survives every falsification attempt I could mount in the window. Gates
A–E are each CONFIRMED; two citation-scope notes are recorded (not gaps in
the mathematics) and one notational ambiguity. Strongest safe scope: for every
actual complex Keller map, Tr_(L/K)(R) equals the inverse image of the
reducible IC submodule L_D, and equals A plus the W-orbits of the nonzero
coefficients (d_i)_p/d_i, (d_i)_q/d_i. No JC2, degree, source-realization or
novelty content is claimed or implied.

## Gate A — derivations, trace, H2(M)=0: CONFIRMED

Inverse-Jacobian check: from ∂_x = P_x∂_p + Q_x∂_q, ∂_y = P_y∂_p + Q_y∂_q,
the displayed δ_p = (Q_y∂_x − Q_x∂_y)/c and δ_q = (−P_y∂_x + P_x∂_y)/c are
the correct inverses; δ_p(P)=1, δ_p(Q)=0, δ_q(P)=0, δ_q(Q)=1. They preserve R
because c is a constant. Their commutator is a derivation of L vanishing on
K, hence zero by uniqueness of extension over the separable algebraic
extension L/K. Trace commutes with them: each embedding σ: L→Ω satisfies
σ∘D = D∘σ by the same uniqueness, and Tr is the sum over embeddings. So M is
a W-submodule of K containing A (Tr(a/N)=a). M ⊂ A[1/d]: over the complement
of the actual D the map is finite, R[1/d] is integral over the normal ring
A[1/d], and traces of integral elements lie in A[1/d].

H2(R)=0 in the lifted frame, verified explicitly: for h ∈ R put B = ∫ch dx
(polynomial), so d(B dy) = ch dx∧dy = h dp∧dq. Solving the frame change with
the constant-Jacobian inverse gives B dy = α dp + β dq with
α = −Q_xB/c, β = P_xB/c ∈ R, and d(α dp + β dq) = (δ_pβ − δ_qα) dp∧dq
because δ_p, δ_q are dual to dp, dq on L. Hence h = δ_pβ − δ_qα and
Tr(h) = ∂_p Tr(β) − ∂_q Tr(α), giving M = ∂_pM + ∂_qM. The functor
E ↦ E/(∂_pE+∂_qE) is the cokernel of E² → E, so it is right exact and
surjections induce surjections; ROOT uses only this, never lower-degree
surjectivity. Confirmed.

## Gate B — generic fullness M_η = K: CONFIRMED

Audited line by line. O = A_η is a DVR (A regular, height-one prime). C, the
integral closure of O in L, is a finite torsion-free O-module by separability
(trace-dual argument), and C ⊂ R_η because R_η is a localization of a UFD,
hence normal, with fraction field L. R_η is not finite over O: finiteness at
η means x, y satisfy monic equations over A_η, clearing denominators gives
R_f finite over A_f for some f ∉ η, so F is finite, hence proper, over the
open set D(f) ∋ η, contradicting η lying in the closed nonproper set. This
uses only that the actual D is the non-finiteness locus (Chau p1
definition via compact neighbourhoods; finite ⇔ proper for affine maps).

Bounding step: if Tr(R_η) ⊂ t^(−b)O then for r ∈ R_η, a ∈ C we have
ra ∈ R_η (ring, C ⊂ R_η), so Tr(t^b r a) ∈ O, i.e. t^bR_η ⊂ C^∨. C^∨ is a
finitely generated O-module (nondegenerate form, O noetherian), so
t^bR_η ≅ R_η would be finitely generated — contradiction. Thus Tr(R_η) is an
O-submodule of K with valuations unbounded below; an element of valuation −m
generates t^(−m)O, so the submodule is K. Localization of the image equals
image of the localization since Tr(r/s) = Tr(r)/s. No pole-of-a-power
assumption, no product-of-traces confusion, no ramification data used.
Confirmed.

## Gate C — reducible extension of Yekutieli's integral quotient: CONFIRMED

Source scope verified on p27 and p32: "X ⊂ Y an integral curve with
arbitrary singularities", and "from here to the end of this section we
consider an integral curve X". Corollary 7.7 (p29) gives
0 → L(X,Y) → H^{n−1}_X O_Y → (H^n_Z O_Y) ⊗ V → 0 with V(x) = Coker(k(x) →
∏ k(x̃)). Over C every k(x̃)=C, so V(x) = C^(r_x−1) with r_x = #π^{−1}(x) =
number of analytic branches, and the quotient is ⊕ δ_x^(r_x−1). This is (Y)
exactly. Global sections over affine A² give A[1/d_i]/A with W acting;
submodules of a finitely generated W-module are finitely generated, so
"unique simple coherent submodule" is "unique simple submodule". The proof of
7.5 (p33) does use point-module classification ("C ≅ K(A)^r").

Point modules: δ_z ≅ C[ξ,η] with p−a, q−b acting as −∂_ξ, −∂_η and ∂_p,
∂_q as multiplication; simple (differentiate to a constant, multiply back),
H2(δ_z) = C[ξ,η]/(ξ,η) = C. Koszul: W is free as a right C[p,q]-module, so
right multiplication by the regular sequence (p−a, q−b) resolves δ_z, and
Hom into δ_{z'} gives the Koszul complex of left multiplication. For z'=z it
is the polynomial de Rham complex of C[ξ,η], so Ext^1 = 0 (Poincaré lemma,
char 0). For z'≠z one operator is (a'−a) − ∂_ξ, invertible since ∂_ξ is
locally nilpotent, so the complex is contractible. Hence every finite
extension of point modules splits. I note the E=0 direction of Gate D does
not even need this: a nonzero finite-length module has a simple quotient
δ_z, and right exactness gives H2(E) ↠ H2(δ_z) = C.

Mayer–Vietoris (3): H^1_Z(A)=0 by depth 2 on the regular surface;
H^2_{(f)}(A)=0 since the Čech complex of one element has length one. H^2_Z
depends only on the set Z, so intersection multiplicity is irrelevant, one
δ_z per point. Induction: L_{D'} ⊕ L_k injects via (3); the quotient is an
extension of H^2_Z by ⊕δ^(r'_z−1) ⊕ ⊕δ^(r_{k,z}−1), giving multiplicity
(r'_z−1)+(r_{k,z}−1)+1 = r_z−1 at z ∈ Z because branch sets of components
with no common component are disjoint; the extension splits by the Ext
computation. Length counted is W-length (each δ_z simple), not O-length.
Confirmed.

Generators: the charged pages state C_{X/Y} = [df/f] only in Example 7.13
(nodal cubic); the general identification is Prop 5.11, outside pp27–33
(citation-scope note 1). I verified membership independently with Theorem
7.1: for a = [f_p/f] and α = g dp∧dq, aα = [g df∧dq/f] = −[g dq∧df/f],
whose Res^lc_{w,σ} is −(g dq)|_X ∈ Ω^1_{k(X)}, a differential regular on X̃
at every x̃, so every Res_{(w̃,x̃)} vanishes. This is precisely the mechanism
of the printed proof of 7.10 (p33). Since L_i is simple, any nonzero such
class generates it; both classes cannot vanish (d_i ∤ (d_i)_p, (d_i)_q unless
d_i is constant). So the second equality of (T) holds.

## Gate D — the short global proof: CONFIRMED (full equality)

Containment (5): E = image(M → H/L_D) is a W-quotient of M inside the
semisimple point module (4). If E ≠ 0 then H2(E) ≠ 0 (semisimplicity, or
the simple-quotient argument above), but H2(M)=0 and right exactness force
H2(E)=0. So M/A ⊂ L_D. Converse: L_i → H/(M/A) is zero or injective by
simplicity. Localization at η_i is exact; (A[1/d])_{η_i} = K since d ∈ η_i,
so H_{η_i} = K/O and by (2) (M/A)_{η_i} = K/O, quotient zero. (L_i)_{η_i} ≠ 0
because s·(d_i)_p/d_i ∈ A with s ∉ η_i would force d_i | (d_i)_p. Injective
nonzero into zero is impossible, so L_i ⊂ M/A for every i. Both containments
give M/A = L_D, hence M = π^{−1}(L_D). Inputs used: (1), (2), (4), simplicity
of L_i, exact localization. No A¹-normalization, Betti comparison,
holonomicity or direct-image statement about R appears anywhere in the
chain. Confirmed.

Sanity controls I ran by hand (not premises): (x,y) ↦ (x²,y) on C*×C gives
M = A[1/p] = (T); (x,y) ↦ (x²,xy) likewise; the torus (x²,y²) gives
M = A[1/(pq)] ∋ 1/(pq), violating (T) exactly because H2(R) = C, matching
ROOT's torus control and showing (1) is load-bearing.

## Gate E — node specialization and controls: CONFIRMED

Flat base change: S = C[[u,v]] is flat over A, so M ⊗ S ↪ S[1/d] = S[1/(uv)]
and M ⊗ S is the Ŵ-span of 1 and the coefficients a_i = (d_i)_p/d_i,
b_i = (d_i)_q/d_i, with Ŵ = S⟨∂_p,∂_q⟩ = S⟨∂_u,∂_v⟩ by the invertible
formal Jacobian. Components not through z have a_i, b_i ∈ S. For the node,
dd_i/d_i = du/u + dv/v + d(unit)/unit (self-node) or the two components
give du/u + reg and dv/v + reg separately; the unit term is a regular form.
Rewriting a dp + b dq in du, dv shows S·{1,a,b} = S + S/u + S/v, and
∂_u^k(1/u) = (−1)^k k!/u^{k+1} generates S[1/u]; S[1/u] + S[1/v] is
Ŵ-stable and contains no monomial u^{−a}v^{−b} with a,b ≥ 1. So (6) holds and
the quotient is H^2_{(u,v)}(S). This is a consequence of (T) plus explicit
generators, with no zero-defect, inertia or two-transposition input, and no
completion of R. Controls: M0 = A[1/u]+A[1/v] has H2=0 (integrate in the
other variable) and is not an algebra; (C*)² has H2 = C, fails (1);
A¹×G_m satisfies (T) with M = A[1/u] but is not a Keller selfmap, so (T)
does not characterize the source; (x,xy) has M = R not ∂_q-stable, so the
Jacobian condition is indispensable; identity has d=1, M=A, and an
artificial divisor breaks (2) since R_η is then finite. All check.

## Notes, not gaps

1. Citation scope: "finite étale complement" is the standard non-finiteness
   reading of the nonproper set (Jelonek); Chau pp1–2 supply the definition,
   curve-ness and A_f = {R_0 = 0} only. The theorem's Gate B needs exactly
   the definition, which Chau p1 gives.
2. Citation scope: general C_{X/Y} = [dd_i/d_i] is Prop 5.11 (outside the
   charged pages); replaced above by a direct Theorem 7.1 verification.
3. Notation: ROOT's "W(d_i,p/d_i)" must be read as W·((d_i)_p/d_i), the
   W-orbit of the p-coefficient of the log form; the comma is not an
   argument separator.

Strongest safe surviving scope: (T), both equalities, for every actual
complex Keller map with its actual reduced nonproper divisor, as a
necessary-condition interface; the nodal consequence (6). No JC2 solution,
geometric-degree bound, source realization or novelty is asserted. No
charge_basis is declared.

<!-- BODY-END -->
