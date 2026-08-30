# R4-DP3 checkpoint: constant units and the exact Picard 3-torsion gate

**Status:** FINAL candidate; exact reduction proved, R4-DP3 itself remains OPEN  
**Date:** 2026-08-30  
**Owner:** double_plane_hostile_review  
**Basis commit:** b3d98d87e9bb9664da7b175b76204bb7eadf1e5d

## 0. Verdict

Let
\[
 A=\mathbf C[x,y],\qquad R=A[s]/(s^2-q),\qquad
 D=\operatorname {Spec}R,
\]
where \(q\in A\) is reduced and nonconstant and the branch curve
\(B=V(q)\) is connected. These hypotheses hold for the charged
minimal \(m=0\) quartic horn.

Then
\[
 R^*=\mathbf C^*,
 \qquad
 H^1_{\mathrm{et}}(D,\mathbf F _3)
    \cong \operatorname {Pic}(D)[3],
 \qquad
 \iota^*=-1
 \text{ on this group},
\]
where \(\iota(s)=-s\). Consequently the charged obstruction is exactly
\[
 H^1_{\mathrm{et}}(D,\mathbf F _3)^-=0
 \quad\Longleftrightarrow\quad
 \operatorname {Pic}(D)[3]=0.
\]

This removes the unit/Kummer ambiguity completely. It does **not**
prove the desired vanishing: the remaining problem is genuine Cartier
3-torsion on the singular affine double plane. In particular it is a
Picard problem, not merely a Weil class-group computation.

## 1. Charged input and scope

The exact double-plane gate and its independent hostile review are:

- block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md,
  SHA-256
  1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb;
- block-descent-a1-quartic-discriminant-double-plane-etale3-gate-hostile-review-sol56-20260830.md,
  SHA-256
  71f582454d2a4f7981aae91fca5a40399c5f536f67870a03f56e596ff9984391.

Those artifacts prove that the minimal \(m=0\) branch would require a
nonzero anti-invariant étale \(C_3\)-torsor on \(D\). The present note
only sharpens that gate. It neither changes the charged branch topology
nor asserts a universal vanishing theorem.

The proof below actually uses only that \(q\) is squarefree and \(V(q)\)
is connected. The stronger charged conditions (components normalized
by \(\mathbf A^1\), source incidence forest, one extra two-point
identification, and one common place at infinity) are reserved for the
remaining Picard calculation.

## 2. Constant-unit theorem

### Proposition 2.1

If \(q\in\mathbf C[x,y]\) is reduced and nonconstant and \(V(q)\) is
connected, then every unit of \(R=A[s]/(s^2-q)\) is constant.

### Proof

Every element of \(R\) has a unique expression \(u=a+bs\), with
\(a,b\in A\). If \(u\) is a unit, multiplication by \(u\) on the free
rank-two \(A\)-module \(R\) is invertible. Its determinant is
\[
 N(u)=a^2-qb^2\in A^*=\mathbf C^*.
\]
Multiplying \(u\) by a constant, possible because \(\mathbf C\) is
algebraically closed, we may suppose \(N(u)=1\). Hence
\[
                  (a-1)(a+1)=q b^2.                 \tag{2.1}
\]
If \(a\) is constant, (2.1) immediately forces \(b=0\), and the proof
is finished. Assume from now on that \(a\) is nonconstant; in particular
\(a-1\) and \(a+1\) are both nonzero.

For a nonzero polynomial \(f\), call the product of the irreducible
factors occurring to odd exponent its *odd support*. Since \(A\) is a
UFD and \(q\) is squarefree, (2.1) says that the odd support of
\((a-1)(a+1)\) is exactly \(q\). No nonconstant irreducible can divide
both \(a-1\) and \(a+1\). Let \(q_-\) (respectively \(q_+\)) be the
product of the irreducible factors of \(q\) dividing \(a-1\)
(respectively \(a+1\)). Then \(q=q_-q_+\), up to a nonzero constant.
The closed subsets \(V(q_-)\) and \(V(q_+)\) cover \(B\), and they are
disjoint: a common point would satisfy \(a=1\) and \(a=-1\).
Connectedness of \(B\) therefore forces one of them to be empty.

Thus one of \(a-1,a+1\) has empty odd support and hence, after absorbing
a nonzero constant into a square, is \(r_1^2\). The other differs from
it by the nonzero constant \(2\), so after scaling it has the form
\[
                    r_1^2-c_1,\qquad c_1\in\mathbf C^*,             \tag{2.2}
\]
and its odd support is \(q\).

Choose \(\lambda_1^2=c_1\). The factors
\(r_1-\lambda_1\) and \(r_1+\lambda_1\) have no common zero, and their
odd supports again partition \(B\) into two disjoint closed subsets.
Connectedness makes one odd support empty. That factor is a constant
times a square, say
\[
                    r_1\mathbin{\pm}\lambda_1=d_1 r_2^2,
                    \qquad d_1\in\mathbf C^*.                       \tag{2.3}
\]
Substitution in the other factor gives, after multiplication by a
constant, \(r_2^2-c_2\) with \(c_2\ne0\) and odd support \(q\). The
same argument iterates.

If \(r_1\) were nonconstant, total degrees in (2.3) would give
\[
 \deg r_1=2\deg r_2,
 \quad \deg r_2=2\deg r_3,
 \quad\ldots .
\]
Thus the positive integer \(\deg r_1\) would be divisible by \(2^n\)
for every \(n\), a contradiction to the standing assumption that
\(a\), hence \(r_1\), is nonconstant. Therefore only the constant case
can occur; as checked above it has \(b=0\) and \(a=\pm1\) under the
normalization. Undoing the constant scaling gives
\(R^*=\mathbf C^*\). \(\square\)

### Checks on hypotheses

- Reducedness is essential in the parity step.
- Connectedness is used exactly to prevent the odd support from splitting
  between the two constant-separated factors.
- No normality or special singularity type is used in Proposition 2.1.
- Nonconstancy excludes the vacuous unbranched case.

## 3. Kummer and involution

Because \(3\) is invertible and \(\mathbf C\) contains \(\mu_3\), the
Kummer sequence gives an equivariant exact sequence
\[
0\longrightarrow R^*/R^{*3}
 \longrightarrow H^1_{\mathrm{et}}(D,\mathbf F _3)
 \longrightarrow \operatorname {Pic}(D)[3]
 \longrightarrow0 .                                                \tag{3.1}
\]
Proposition 2.1 and divisibility of \(\mathbf C^*\) make the left term
zero, proving
\[
 H^1_{\mathrm{et}}(D,\mathbf F _3)
       \cong \operatorname {Pic}(D)[3].                             \tag{3.2}
\]

The morphism \(\pi:D\to\mathbf A^2\) is finite flat of degree two, with
deck involution \(\iota\). For every line bundle \(L\) on \(D\), the
norm identity is
\[
 \pi^*\operatorname {Nm}_{D/\mathbf A^2}(L)
       \cong L\otimes\iota^*L .                                    \tag{3.3}
\]
Since \(\operatorname {Pic}(\mathbf A^2)=0\), (3.3) yields
\(\iota^*[L]=-[L]\) in \(\operatorname {Pic}(D)\). The isomorphism
(3.2) is equivariant, so every étale \(3\)-class is anti-invariant:
\[
 H^1_{\mathrm{et}}(D,\mathbf F _3)^+
       =0,
 \qquad
 H^1_{\mathrm{et}}(D,\mathbf F _3)^-
       =H^1_{\mathrm{et}}(D,\mathbf F _3).                          \tag{3.4}
\]

For completeness, squarefree \(q\) makes \(D\) normal: it is a
hypersurface, hence \(S_2\), and its singular locus lies over the finite
singular locus of the reduced plane curve \(B\), hence has codimension
two. This normality is needed for the Weil-divisor discussion below,
not for (3.1)--(3.4).

## 4. Picard/class-group and local-extension firewall

For normal \(D\), Cartier divisors give an injection
\[
                  \operatorname {Pic}(D)\hookrightarrow\operatorname {Cl}(D).
\]
It is unsafe to replace the left side by the right side. A Weil
3-torsion class can be non-Cartier at a singular point and then describes
only punctured local monodromy, not a finite étale cover of all of \(D\).
Equivalently, any class-group calculation must also check that its image
in every local class group vanishes.

This recovers the charged local \(C_2\) gate in divisor language. At an
\(A_1\) point the local obstruction is 2-primary and cannot support a
mod-3 punctured class. At an \(A_2\) point a local 3-class can occur,
but it is precisely the kind of punctured class that need not extend
étale across the singular point. Therefore:

- proving \(\operatorname {Cl}(D)[3]=0\) is sufficient for the desired
  vanishing;
- finding \(\operatorname {Cl}(D)[3]\ne0\) is not sufficient for a
  counter-control;
- an exact counter-control must produce a nonzero *Cartier* 3-torsion
  class, or equivalently a connected finite étale \(C_3\)-cover of \(D\).

The previously charged positive \(S_3\) control with branch normalization
\(\mathbf G_m\) is compatible with this theorem: its nonzero class must
lie in \(\operatorname {Pic}(D)[3]\), not in the unit term of (3.1).

## 5. Explicit quarantine: the monogenic collapse is open

There is a useful but incomplete observation for a globally monic
depressed cubic
\[
                         T^3+aT+b .
\]
Under appropriate no-triple-root and nonvanishing hypotheses, the root
separations on branch normalizations are units. Because the charged
normalization components are \(\mathbf A^1\), those units are constant,
and compatibility through the connected incidence can force the
restrictions of \(a\) and \(b\) to the branch curve to be constant.

This does **not** imply that \(a,b\in\mathbf C[x,y]\) are globally
constant. The coefficient map may collapse the entire branch curve to
one smooth point of the cubic discriminant. Excluding that possibility
requires an additional polynomial identity/Mordell--Catalan argument.
No such argument is supplied here. Accordingly, any blanket
“monogenic cubic impossible” statement is quarantined as **OPEN** and
must not be used downstream.

## 6. Exact remaining lane

After this reduction, R4-DP3 has one target:
\[
                      \operatorname {Pic}(D)[3]=0                  \tag{6.1}
\]
for the charged minimal \(m=0\) branch topology. The next attack should
identify (6.1) with the kernel of local restrictions in the sign/Fox
cohomology of \(\mathbf A^2-B\):

1. compute \(H^1(\mathbf A^2-B,\mathbf F _3^{\mathrm{sign}})\), whose
   cocycles are \(S_3=\mathbf F _3\rtimes C_2\) lifts of the meridional
   sign character;
2. impose trivial restriction at every punctured singular link, which
   is the extension condition from a quasi-étale cover to an étale cover
   of \(D\);
3. impose the one-place-at-infinity relation. A Fox determinant or
   \(\Delta(-1)\bmod3\) is only a screen, not a proof: the charged nodal
   control already shows that a boundary 3-coloring can die after the
   interior and extension relations are imposed.

This localization/Fox calculation is a successor task and is not
claimed here.

## 7. Verification and custody

- The proof is symbolic and general; no CAS replay would certify the UFD
  parity/connectedness argument or the Kummer/norm functoriality, so no
  replay script is attached.
- The unit proof was checked independently at every use of reducedness,
  connectedness, algebraic closedness, and degree descent.
- The Picard/class-group distinction and the singular-point extension
  condition are explicit.
- The monogenic shortcut is explicitly excluded from the theorem.
- No top-level ledger, coordination file, or Lean workspace was read or
  modified.

**Final classification:** FINAL+VERIFIED EXACT REDUCTION / R4-DP3 OPEN.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10840`.
- Body SHA-256:
  `16f5dab006998778620a7275345364e24db8482319e095b9f644ec7dd537bece`.
- Frozen basis: `b3d98d87e9bb9664da7b175b76204bb7eadf1e5d`.
