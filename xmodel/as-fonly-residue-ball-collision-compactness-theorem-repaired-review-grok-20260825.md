**Limitation.** This review used only the listed files (read-only). No Bash, CAS, network, or writes. SHA-256 values were not recomputed. Control arithmetic below was done by hand. The first Grok review is not in-tree; repairs were checked against the parent theorem and the first-review prompt.

**Scope.** Audit of the repaired lemma in `xmodel/as-fonly-residue-ball-collision-compactness-theorem-repaired-20260825.md` and `cases/as_fonly_residue_ball_collision_repaired_20260825/`. Not an audit of live filtered AS solver state.

---

### 1. Unique digit-by-digit preimages on \(R_n=\mathbb{Z}/3^n\mathbb{Z}\)

**Claim is correct.** Let \(F=(P,Q)\) over \(R_n\) with \(\det JF=1\) in \(R_n[x,y]\) and \(F\equiv(x-x^3,y)\pmod{3}\). Over \(\mathbb{F}_3\), \(x-x^3=0\) identically, so each of \((0,0),(1,0),(2,0)\) maps to \((0,0)\). Each source ball \(r+3R_n^2\) therefore lands in the target ball over \((0,0)\).

Taylor in any commutative ring, with \(\delta=3^kh\), puts remainder terms in \(3^{2k}\). For \(k\ge 1\), \(2k\ge k+1\), so
\[
F(x_k+3^kh)\equiv F(x_k)+3^k\,JF(x_k)h\pmod{3^{k+1}}.
\]
The congruence uses only \(JF(x_k)\bmod 3\). Polynomial \(\det JF=1\) implies that this reduction is invertible over \(\mathbb{F}_3\) (in fact \(J(x-x^3,y)=I\)). The digit equation is linear over a field and has exactly one solution \(h\in\mathbb{F}_3^2\). Nilpotents in \(R_n\) do not create extra digits. Induction gives a unique preimage of any target \(z\equiv(0,0)\pmod{3}\) in each of the three balls, hence a bijection of finite sets of equal size.

The special fibre is not surjective on \(\mathbb{F}_3^2\)-points (image is the line \(x=0\)). The lemma correctly restricts to the target ball over \((0,0)\).

**Writeup regression.** Parent §2 names a general \(z\) and the range \(1\le k<n\). Repaired §1 states the bijection, then writes the Taylor identity without \(z\) and without \(k\ge 1\). “Exactly one \(h\) solves the next digit” does not, as written, specify the inhomogeneous equation
\[
JF(x_k)h\equiv(z-F(x_k))/3^k\pmod{3}.
\]
The argument is the standard one; the symbols needed to make it a proof were dropped.

### 2. Unit \(x\)-separation; moving versus marked

**Correct.** The three preimages have distinct \(x\)-residues \(\{0,1,2\}\), so every pairwise \(x\)-difference is a unit in \(R_n\). The first two balls give
\[
P(a,b)=P(c,d),\quad Q(a,b)=Q(c,d),\quad u(a-c)=1
\]
with Hensel-moving points, not marked representatives \((0,0),(1,0)\). The lemma does not claim a collision of fixed integer labels.

Hand check of the frozen control, \(P=x+2x^3+441x^5+108x^7\), \(Q=y-6x^2y+18x^4y-27x^6y\):
- \(\det JF=P_xQ_y=(1+6x^2+2205x^4+756x^6)(1-6x^2+18x^4-27x^6)\)
  \(=1+2187x^4-12393x^6+34992x^8-45927x^{10}-20412x^{12}\),
  which is \(1\bmod 9\) and \(\bmod 27\);
- preimages of \((0,0)\): \((0,0),(7,0),(2,0)\) mod \(9\); \((0,0),(7,0),(20,0)\) mod \(27\);
- unit inverses \(5,4,2\) mod \(9\) and \(23,4,2\) mod \(27\);
- \((7,0)\) and \((20,0)\) are not the marked residues \((1,0),(2,0)\).

Negative control \((x-x^3,3y)\): on the ball over \((0,0)\) mod \(9\), the second coordinate is identically \(0\), so \((0,3)\) is missed; \(\det=3\) is not a unit mod \(3\). Load-bearing.

### 3. Nested compactness / König, unrelated finite-level solutions

**Correct, with one false parenthetical.** Fix finite allowed monomial sets \(S_P,S_Q\). Let \(X_n\subset\mathbb{Z}_3^N\) be coefficient vectors satisfying every coefficient of \(\det JF-1\) and the AS reduction modulo \(3^n\). Each \(X_n\) is closed. A solution over \(R_n\) lifts arbitrarily to \(\mathbb{Z}_3^N\), so \(X_n\) is nonempty whenever the finite scheme is. Nested nonempty compact sets have nonempty intersection; equivalently, the inverse system of nonempty finite solution sets has nonempty inverse limit (images in each \(S_n\) stabilize, then a thread exists). Exhibited solutions at different \(n\) need not be compatible.

The \(\mathbb{Z}_3\) point has \(\det JF=1\) coefficientwise (each coefficient of \(\det JF-1\) is \(0\) mod \(3^n\) for all \(n\)). Finite-ring Hensel along that single map, not a patchwork of finite-level collisions, yields a compatible moving collision over \(\mathbb{Z}_3\). Finite support is used later for finite type, not for compactness of \(\mathbb{Z}_3^N\).

**Defect.** “coefficients may vanish … (equivalently the degrees are at most a fixed cap)” is false. A degree cap is one choice of \(S_P,S_Q\). A lacunary set (the triangular control) is not a full diamond of the same degree. Treating them as equivalent would license silent growth of the allowed set, which §5 forbids.

### 4. Finite-type affine scheme and \(\mathbb{Q}_3\to\overline{\mathbb{Q}}\to\mathbb{C}\)

**Correct.** \(Y\) is affine of finite type over \(\mathbb{Z}\): finitely many coefficients in \(S_P,S_Q\), points \((a,b),(c,d)\), unit \(u\), and finitely many equations (every coefficient of \(\det JF-1\), the two collision equations, \(u(a-c)-1=0\)). Collision polynomials are polynomial in coefficients and source coordinates. AS reduction is deliberately not an equation of \(Y\); it is used only to produce the \(\mathbb{Z}_3\) point.

A \(\mathbb{Z}_3\)-point of \(Y\) gives a homomorphism \(\mathbb{Q}[Y]\to\mathbb{Q}_3\), so \(\mathbb{Q}[Y]\ne 0\) and the defining ideal over \(\mathbb{Q}\) is proper. Faithful flatness of \(\mathbb{Q}\to\overline{\mathbb{Q}}\) keeps the coordinate ring nonzero. Weak Nullstellensatz supplies a \(\overline{\mathbb{Q}}\)-point; any embedding \(\overline{\mathbb{Q}}\to\mathbb{C}\) supplies a complex point. The unit equation keeps sources distinct; coefficientwise \(\det JF-1=0\) gives constant Jacobian one. The \(\mathbb{C}\)-point uses the same monomial slots: support may drop, not grow. That is a JC2 counterexample, **conditional** on all-depth survival of the same complete fixed-support scheme, which is not claimed.

Terminology repair from the parent’s “finite integral scheme” is present.

### 5. AWS control: AS assertion and regression-only scope

**Present.** `replay_repaired.py` pins parent `replay_controls.py` at
`6835141d2b5eabcc41897e1280698902c39f65d12cabc89c10f3ddb6e9b10509`, then asserts
\[
P\bmod 3=x-x^3,\qquad Q\bmod 3=y
\]
before Jacobian or Hensel. Frozen map coefficients: \(441\equiv108\equiv 0\bmod 3\), \(2\equiv -1\bmod 3\). Custody: rc \(0\), endpoint `PASS-AS-RESIDUE-BALL-COLLISION-CONTROLS`, stdout scope string
“finite-ring positive controls only; no all-depth existence, fixed-support lift, Qbar point, or JC2 inference.”
The job was not re-run here. Hashes internally match `FREEZE.txt` / `AWS_CUSTODY.md` / `OUTPUT.sha256` as written, not as recomputed.

Parent §4’s sentence that the controls are finite-depth regressions is gone from repaired §4; the restriction still appears in the payload and in §5 (“finitely many depths”). Not a mathematical error.

### 6. Q5/H6 firewall

**Present and correctly negative.** §5 requires one fixed allowed monomial set, every determinant coefficient, the same AS component, integer reconstruction, and arbitrarily deep survival. It excludes filtered high bands, incomplete lower rows, growing support, and finite depth. Explicitly: Q5/H6 still owes Q4 through Q0 and is not a complete map modulo \(243\); no collision inference attaches. That is a citation ban, not consumption of the live gate.

First-review prompt repairs that are present: three-ball unique digits; moving vs marked; compactness for unrelated complete solutions; coefficientwise determinant; finite-type affine \(Y\); support may drop; AS assert before consuming the control; Q5/H6 firewall.

---

### Defects (repaired theorem only)

1. **False equivalence** in §2: a fixed finite monomial set is not equivalent to a degree cap. Delete “equivalently the degrees are at most a fixed cap,” or replace by “a total-degree cap is one such choice.” This is the only defect that could distort later citations.

2. **Incomplete inductive writeup** in §1: restore a general target \(z\equiv(0,0)\pmod{3}\) and the range \(1\le k<n\), as in the parent. The bijection claim is right; the displayed Taylor identity is not yet a proof of unique preimages of arbitrary targets.

No other defect affects the lemma. Compactness, coefficientwise \(\det=1\), moving collisions, finite-type transfer, control AS assert, regression-only payload, and the Q5/H6 ban stand.

CONFIRMED_WITH_REPAIRS
