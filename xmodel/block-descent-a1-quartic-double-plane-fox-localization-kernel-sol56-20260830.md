# R4-DP3 successor: the exact Fox/localization kernel

**Status:** FINAL candidate; exact interface and determinant screen proved,
universal charged-horn vanishing remains OPEN  
**Date:** 2026-08-30  
**Owner:** double_plane_hostile_review  
**Basis commit:** adb847313c6c946d893100a2cd4c8226a5cc2f0c

## 0. Verdict

Let \(B=V(q)\subset\mathbf A^2_{\mathbf C}\) be reduced and connected,
let
\[
 D=\{s^2=q(x,y)\},\qquad U=\mathbf A^2-B,
\]
and let \(\epsilon:\pi_1(U)\to C_2=\{\pm1\}\) send every branch
meridian to \(-1\). Write \(\mathcal L_\epsilon\) for the rank-one
\(\mathbf F _3\)-local system with this sign action. If
\(\Sigma=\operatorname {Sing}D\) and \(M_p\) is the link of
\(p\in\Sigma\), then there is an exact identification
\[
\boxed{
 \operatorname {Pic}(D)[3]
 \;\cong\;
 \ker\!\left[
 H^1(U,\mathcal L_\epsilon)
   \longrightarrow
 \bigoplus_{p\in\Sigma}H^1(M_p,\mathbf F _3)
 \right].
}                                                               \tag{0.1}
\]
Here exactness means exact at the middle term; no surjectivity onto the
sum of local groups is asserted.

Equivalently, a sign cocycle gives an \(S_3=\mathbf F _3\rtimes C_2\)
meridian-transposition representation. It contributes to
\(\operatorname {Pic}(D)[3]\) exactly when every singular local image is
conjugate to \(C_2\). Thus (0.1) is the exact algebraic-topological form
of the charged local \(C_2\) gate. It cleanly distinguishes a punctured
local 3-class from a globally étale \(C_3\)-cover of \(D\).

If \(B\) is irreducible with one place at infinity and \(K_\infty\) is
its knot at infinity, boundary inclusion gives an injection
\[
 \operatorname {Pic}(D)[3]
   \hookrightarrow
 H^1(S^3-K_\infty,\mathcal L_\epsilon)
   \cong H^1(\Sigma_2(K_\infty),\mathbf F _3).                    \tag{0.2}
\]
Consequently
\[
 3\nmid\det K_\infty
 \quad\Longrightarrow\quad
 \operatorname {Pic}(D)[3]=0.                                    \tag{0.3}
\]
The converse is false. The charged polynomial one-node control has
trefoil infinity and determinant \(3\), but its affine complement group
is \(\mathbf Z\), so its middle group in (0.1) is already zero.

The broad minimal \(m=0\) horn is therefore **not closed here**. Its exact
remaining question is whether a boundary Fox 3-coloring can survive all
affine braid relations and all singular-link restriction maps. No exact
branch counter-control satisfying all of those conditions is presently
known.

## 1. Charged basis

This note sharpens the following finalized artifacts:

- block-descent-a1-quartic-double-plane-constant-unit-pic3-reduction-sol56-20260830.md,
  SHA-256
  a83e110935c96f934b80b61a2cd5a2323d4f6cbfd3212004b3be4b3256b5b39c;
- block-descent-a1-quartic-cycle0-polynomial-link-obstruction-sol56-20260830.md,
  SHA-256
  43c83d47d864537aae6fec7203111aaa3c6c52fa4bbc0e95c6877c61aa86ad57;
- block-descent-a1-quartic-cycle0-projection-propagation-obstruction-sol56-20260830.md,
  SHA-256
  e73f8e83c4031e516f0302dea94e168b5f8b8d5f0bcc6cd86f87eb927a682e14;
- block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md,
  SHA-256
  03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa.

The first proves
\[
 H^1_{\mathrm{et}}(D,\mathbf F _3)
   =H^1_{\mathrm{et}}(D,\mathbf F _3)^-
   \cong\operatorname {Pic}(D)[3]                                  \tag{1.1}
\]
for reduced connected \(B\). Comparison for finite coefficients over
\(\mathbf C\) lets us use singular topology below.

## 2. From sign cocycles to the smooth double plane

Put \(\widetilde U=D-\pi^{-1}(B)\). It is the unramified double cover of
\(U\) classified by \(\epsilon\). If
\[
 G=\pi_1(U),\qquad H=\ker\epsilon=\pi_1(\widetilde U),
\]
restriction and the index-two Hochschild--Serre sequence give
\[
 H^1(G,\mathbf F _3^\epsilon)
       \cong H^1(H,\mathbf F _3)^-.                                \tag{2.1}
\]
There are no higher-index correction terms here because \(2\) is
invertible in \(\mathbf F _3\).

Let \(m\) be a meridian around a smooth point of \(B\). Passing from
\(\widetilde U\) to \(D_{\mathrm{reg}}\) fills the corresponding
ramification divisor and kills \(m^2\). If \(z:G\to\mathbf F _3\) is a
sign cocycle, then
\[
                    z(m^2)=z(m)-z(m)=0.                            \tag{2.2}
\]
Thus every anti-invariant class automatically extends over the smooth
ramification divisor. Conversely, restriction from \(D_{\mathrm{reg}}\)
is injective because \(\pi_1(\widetilde U)\to\pi_1(D_{\mathrm{reg}})\)
is surjective. Hence
\[
 H^1(D_{\mathrm{reg}},\mathbf F _3)^-
       \cong H^1(U,\mathcal L_\epsilon).                            \tag{2.3}
\]

This automatic smooth extension is important: the only extension tests
left are at singular points of the double plane, not along the generic
branch divisor.

## 3. Singular-link localization

A sufficiently small neighborhood of an isolated complex surface
singularity \(p\in D\) is a cone on its link \(M_p\). Therefore
\(\pi_1(D)\) is obtained from \(\pi_1(D_{\mathrm{reg}})\) by normally
killing the images of all \(\pi_1(M_p)\). Applying
\(\operatorname {Hom}(-,\mathbf F _3)\) gives an injection
\[
 H^1(D,\mathbf F _3)\hookrightarrow
 H^1(D_{\mathrm{reg}},\mathbf F _3)
\]
whose image is the simultaneous kernel of restriction to the links.
Combining this statement with (1.1) and (2.3) proves (0.1).

There is a completely equivalent representation formulation. A sign
cocycle \(z\) defines
\[
 \rho_z(g)=(z(g),\epsilon(g))
       \in \mathbf F _3\rtimes C_2\cong S_3.                        \tag{3.1}
\]
Coboundaries conjugate \(\rho_z\) by \(A_3\). Every meridian maps to a
transposition because
\[
 (z(m),-1)^2=(0,+1).
\]
For a singular point \(b\in B\), let \(G_b\) be the local branch
complement group and \(H_b=\ker(\epsilon|_{G_b})\). The restriction in
(0.1) vanishes exactly when
\[
 z|_{H_b}=0
 \quad\Longleftrightarrow\quad
 \rho_z(G_b)\text{ is conjugate to }C_2.                            \tag{3.2}
\]
This is precisely the local \(C_2\) condition.

Two standard checks expose the Picard/class-group firewall:

- at a branch node, \(D\) has an \(A_1\) singularity and
  \(H_1(M_p,\mathbf Z)=\mathbf Z/2\), so no mod-3 punctured class exists;
- at an ordinary branch cusp, \(D\) has an \(A_2\) singularity and
  \(H_1(M_p,\mathbf Z)=\mathbf Z/3\); a punctured 3-class can exist, but
  a nonzero such restriction is exactly what (3.2) excludes from a
  globally étale class.

Thus local \(A_2\) class-group 3-torsion is not automatically a Picard
3-class.

## 4. Infinity injection and the determinant gate

Assume in this section that \(B\) is irreducible and has one
normalization place at infinity. For a generic finite projection, the
group of the closed boundary braid \(K_\infty\) has the same fibre
meridian generators as the affine Zariski--van Kampen presentation.
The affine group is obtained by imposing the separate finite braid
relations, whereas the boundary group imposes only their product
relation. Hence there is a meridian-compatible surjection
\[
 \pi_1(S^3-K_\infty)\twoheadrightarrow\pi_1(U).                     \tag{4.1}
\]
Inflation for (4.1) is injective in degree one, giving the first
injection in (0.2).

For a knot \(K\), reduced Fox 3-colorings are equivalently nonzero
classes in
\[
 H^1(S^3-K,\mathcal L_\epsilon)
   \cong H^1(\Sigma_2(K),\mathbf F _3).                             \tag{4.2}
\]
The finite group \(H_1(\Sigma_2(K),\mathbf Z)\) has order
\[
                       |\Delta_K(-1)|=\det K.                      \tag{4.3}
\]
Equations (4.2)--(4.3) prove (0.3).

The same conclusion has a useful direct \(S_4\) proof. Suppose the
boundary knot group surjects onto \(S_4\) with a meridian mapping to a
transposition. The mod-two subgroup maps onto \(A_4\), and meridian
squares map to the identity. The map therefore descends to
\(\pi_1(\Sigma_2(K))\twoheadrightarrow A_4\). Abelianizing and using
\[
                            A_4^{\mathrm{ab}}\cong C_3
\]
shows \(3\mid\det K\). This is the boundary shadow of the double-plane
Picard gate.

For a reducible branch, infinity is a link and the one-variable knot
determinant statement is not the correct invariant. One must retain the
full sign-specialized Alexander/Fox matrix. No knot-determinant claim is
made for that lane.

## 5. Why trefoil determinant \(3\) still loses globally

The exact polynomial control
\[
 X(t)=t^4+t^3-t,\qquad Y(t)=t^2
\]
has one ordinary affine two-point identification, one place at infinity,
and trefoil boundary braid \(\sigma_1^3\). Thus
\(\det K_\infty=3\), and the boundary group has a nontrivial Fox
3-coloring. In the standard trefoil presentation
\[
 \langle a,b\mid aba=bab\rangle,
\]
the assignment \(a\mapsto(12)\), \(b\mapsto(23)\) is an explicit
surjection to \(S_3\).

The affine projection has a simple tangency factor \(\sigma_1\) and a
node factor \(\sigma_1^2\). Separate affine van Kampen relations give
\[
 \pi_1(U)=\langle a,b\mid a=b,\ [a,b]=1\rangle
          \cong\mathbf Z.                                         \tag{5.1}
\]
For \(G=\mathbf Z=\langle m\rangle\) acting on
\(\mathbf F _3^\epsilon\) by \(-1\), a cocycle is determined by
\(z(m)\), while
\[
 \delta c(m)=(-1)c-c=-2c=c
\]
fills all of \(\mathbf F _3\). Therefore
\[
                   H^1(U,\mathcal L_\epsilon)=0.                  \tag{5.2}
\]
The node link is \(A_1\) and has no mod-3 class, so nothing is lost at
the final local-extension map. The boundary coloring dies earlier:
the individual affine tangency relation \(a=b\), invisible in the total
boundary determinant, collapses all colors. This exactly explains why
\[
 \det K_\infty\equiv0\pmod3
\]
is necessary but not sufficient.

## 6. An infinite false-positive family

The same separation between infinity and affine relations occurs in the
polynomial family
\[
 X=t^3,\qquad Y=t^{3r+1}(t+1),\qquad r\ge1.                         \tag{6.1}
\]
Its implicit equation is
\[
 q_r=X^{3r+2}+3X^{2r+1}Y+X^{3r+1}-Y^3=0.                          \tag{6.2}
\]
Indeed direct substitution makes the four terms cancel.

If \(X(t)=X(u)\) and \(t\ne u\), then \(u=\zeta t\) for a primitive
cube root \(\zeta\), and equality of \(Y\) forces \(t=\zeta\).
Thus the sole unordered two-point identification is
\(\{\zeta,\zeta^2\}\). Its two tangent slopes differ by
\(-(\zeta-\zeta^2)/3\), so it is an ordinary node. At \(t=0\) the
parametrization has the unibranch type \((3,3r+1)\). There are no other
affine singularities. The normalization is \(\mathbf A^1\), the image
has exactly one extra cycle, and there is one normalization place at
infinity.

The local cusp knot is \(T(3,3r+1)\), while the infinity knot is
\(T(3,3r+2)\). For even \(r\),
\[
 \det T(3,3r+1)=1,\qquad \det T(3,3r+2)=3.                          \tag{6.3}
\]
Thus the infinity determinant passes and the local cusp has no mod-3
punctured class. Nevertheless the cusp uses all three sheets of the
\(X\)-projection. Its local \(C_2\) condition makes all three transported
fibre meridians equal in \(S_3\); those meridians generate the affine
complement group. Hence the global image is \(C_2\), not \(S_3\), and
the kernel (0.1) is zero.

This family is a negative control, not a counterexample. It satisfies the
charged normalization/cycle/one-place topology and the local \(C_2\)
condition while showing, infinitely often, that determinant \(3\) at
infinity still need not produce \(\operatorname {Pic}(D)[3]\).

## 7. Finalized total-delta consequence

The finalized total-delta artifact cited in Section 1 proves the following
independent quartic theorem. If \(B\) is irreducible with normalization
\(\mathbf A^1\), and its affine complement has a transitive
meridian-transposition representation to \(S_4\), then
\[
                         \Delta_{\mathrm{aff}}(B)\ge3.              \tag{7.1}
\]
For total delta two, the one-place infinity knot is a prime genus-two
iterated cable. The only candidates are
\[
 T(2,5),\qquad C_{2,\pm1}(T(2,3))
\]
and their mirrors, with determinants \(5\) and \(1\), respectively.
Equation (0.3), equivalently the direct \(A_4^{\mathrm{ab}}=C_3\)
argument, excludes them. The apparent connected-sum survivor of
determinant \(9\) is excluded by the finalized one-place prime-knot
interface. Genus zero and one are disposed of by meridional rank.

Therefore the actual irreducible \(\mathbf A^1\) quartic horn is already
closed whenever its complete affine singularity census has total delta at
most two. This is a combined campaign consequence, not an assertion that
\(\operatorname {Pic}(D)[3]\) vanishes for every abstract branch in that
range.

The finalized sharp control \(B_3=\{(x,y)=(t^3,t^4)\}\) has total delta
three and an explicit transitive \(S_4\) coloring. It does **not** answer
R4-DP3: all three star transpositions occur in its sole local cusp group,
so the local image is \(S_4\), its resolvent local image is \(S_3\), and
condition (3.2) fails. In double-plane language its 3-class is punctured
at the singular point rather than globally étale.

Thus an irreducible charged survivor must have total affine delta at least
three while arranging every singular local image inside a conjugate
\(C_2\); its primitive overlap must be assembled globally, not concentrated
in the delta-three cusp.

## 8. Maximum-safe campaign update

The exact search target is now a linear kernel, not a vague request for a
three-cover:
\[
 \operatorname {Pic}(D)[3]
 =
 \left\{
 \begin{array}{l}
 \text{global sign/Fox classes satisfying every affine braid relation}\\
 \text{and restricting trivially to every double-plane singular link}
 \end{array}
 \right\}.                                                       \tag{8.1}
\]

For speed, every candidate should be screened in this order:

1. compute the full Fox matrix over \(\mathbf F _3\) at sign
   \(t=-1\), not only an integral determinant;
2. for an irreducible one-place branch, discard immediately if
   \(3\nmid\det K_\infty\);
3. impose each finite affine braid relation separately;
4. impose the singular-link kernels, especially at \(A_2\)-type points;
5. only after a nonzero class survives, attempt polynomial algebraization
   and the quartic/ruling gates.

A proof of universal vanishing must show that the boundary Fox space has
zero intersection with the affine/local kernel for every charged branch.
An exact counter-control must exhibit a nonzero vector in that intersection
and then realize it by the charged algebraic branch. Neither final step is
claimed here.

## 9. Verification and custody

- Equations (0.1)--(0.3) were reconstructed from fundamental groups,
  index-two cohomology, conical singular neighborhoods, and the standard
  Fox/double-branched-cover identity.
- The trefoil control was checked both by its presentations and by the
  explicit twisted \(H^1(\mathbf Z,\mathbf F _3^\epsilon)\) calculation.
- Equations (6.1)--(6.3), the unique identified pair, and transversality
  were checked by exact hand algebra. No numerical or heavy CAS inference
  is used.
- No replay is attached: the load-bearing content is the localization
  theorem and its group-cohomological proof, which a finite symbolic script
  would not certify.
- No top-level ledger, coordination file, active sibling artifact, or Lean
  workspace was read or modified.

**Final classification:** FINAL+VERIFIED EXACT FOX/LOCALIZATION INTERFACE;
R4-DP3 BROAD HORN OPEN.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15365`.
- Body SHA-256:
  `dcf65ce1a097831c1e314f8524ae3e9b41837935817f306049ca82bfd7c69379`.
- Frozen basis: `adb847313c6c946d893100a2cd4c8226a5cc2f0c`.
