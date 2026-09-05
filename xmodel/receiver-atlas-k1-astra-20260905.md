# k=1 monomial-Jacobian receiver and source-to-receiver atlas

Lane: `receiver-atlas-k1-astra-20260905` (Astra, primary). Receipt: `xmodel/receiver-atlas-k1-astra-20260905.run.v2`. Frozen inputs: `/tmp/jc2-lane.MMCkx9/inputs`. Computation and interface artifacts: `box/recvatlas-20260905/`.

## 0. Verdict and the correction that controls every implication

**PROVED: the literal receiver with the full forward coefficient bound is empty in every degree. Its defining ideal has a two-term unit certificate. However, the proposed common source-to-receiver map is invalid: K16 has the forbidden coefficient `[gamma*pi^0]P=-g`, a scalar unit. Consequently this emptiness does not prove K16, (8.1), or (T), and it discharges zero of the advertised 671/1110 residue.**

The phrase “Newton bound” needs an index convention. The full statement `deg_gamma [pi^j] <= 3j` for every `j>=0` includes a constant-coefficient restriction. The parenthetical statement `deg_gamma [pi] <= 3` alone does not. Removing `j=0`, or indexing coefficients down from the leading term, produces nonempty receivers. Explicit families and a complete classification of the affine-in-pi slice appear below; no complete arbitrary-degree classification of those different receivers is claimed.

A useful atlas can nevertheless be derived. It uses larger, finite polynomial receivers that admit the necessary source support. Its maps are literal coefficient homomorphisms and carry explicit ideal-membership cofactors, rather than numerical coincidences. They provide the following coverage of the historical sharpened cohort:

| Object and scope | Certified keys | UNASSIGNED keys | Source records assigned | Source records killed |
|---|---:|---:|---:|---:|
| Requested full forward wedge, Jacobian `c*gamma` | **0/132** | **132/132** | **0/296** | **0** |
| Larger receiver with Jacobian `c*gamma`, licensed descent branches | **32/132** | **100/132** | **87/296** | **0** |
| Larger monomial family, exponents `ell=0,...,8`, licensed descent branches | **132/132** | **0/132** | **296/296** | **0** |

The complementary split branches remain **296 explicit UNASSIGNED branch obligations**. These are dispositions, not a claim that all 296 split branches are realized. The larger receivers are nonempty, with exact rational witnesses. Their complete conditional assignment therefore proves an interface theorem and no source-emptiness theorem.

The finite atlas, source decorations, generator orders, localizations, and branch statuses are in `box/recvatlas-20260905/cohort/inventory.json`. The three concrete pilots are both ancestors of `(36,24,2,5)` and an exponent-one `(48,40,1,5)` source. No K16 milestone notification is warranted.

## 1. Custody, source scope, and operational record

Before reading the charged mathematical inputs, the nine checksums were generated mechanically from the receipt's `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` fields. No digest was retyped. The intake command was:

```sh
awk -F= '
/^charged_input_[0-9]+_sha256=/ {
  i=$1; sub(/^charged_input_/,"",i); sub(/_sha256$/,"",i); hash[i]=$2
}
/^charged_input_[0-9]+_basename=/ {
  i=$1; sub(/^charged_input_/,"",i); sub(/_basename$/,"",i); name[i]=$2
}
END {
  for(i in hash) {
    if(!(i in name)) exit 2;
    print hash[i] "  /tmp/jc2-lane.MMCkx9/inputs/" name[i]
  }
}' xmodel/receiver-atlas-k1-astra-20260905.run.v2 > /tmp/receiver-atlas-k1-astra-20260905.sha256
sha256sum -c /tmp/receiver-atlas-k1-astra-20260905.sha256
```

All nine entries returned `OK`. The resulting manifest is retained as `box/recvatlas-20260905/frozen-inputs.sha256`. A report skeleton was written immediately afterward, before the theorem and atlas work. The frozen `guided_gb.py` was imported directly for the exact characteristic-zero receiver controls. The frozen `moh_skeleton_full.py` was used in the cohort replay.

The sources that control the mathematics are Fable's frozen §§2.3 and 4.2–4.4, Astra's frozen §§4–5, the frozen K16 report's `(REC)`, `(DEP1)`, and `(DEP2)`, and Moh Proposition 6.3 on printed pp.197–198. The original PDF page image was inspected; its inequality is `delta*_(s-1) >= v_s/u_s`, including equality. Proposition 6.4 supplies automatic radius only when `u_s=1`. The frozen 14-row report's discussion of necessary overapproximations and unsafe tighter support is consistent with the discipline used here.

The cohort replay also reads the historical snapshot and its provenance records named by the charged Astra report. Those supplemental inputs have a separate six-entry checksum manifest in `cohort/new-read-inputs.sha256`; the snapshot digest is checked against both upstream provenance and the prior 296-row audit before emitting counts. Three supplemental K16 ansatz artifacts are listed with their actual digests in `k16_map_check.json`. These reads do not turn a historical cohort into a newly promoted census.

No ledger, `jc2-lean`, or `ideation-*` file was edited. All new drivers are under the requested box directory. CAS ran in the foreground, with one core per task and no more than four task slots. No modular result is promoted. The report is sealed only after the checks and all lane jobs have finished.

## 2. The receiver ring and its exact all-degree certificate

Use a characteristic-zero field `K`; reserve `ell` for the Jacobian exponent. Define

```text
Jac(P,Q) = P_gamma*Q_pi - P_pi*Q_gamma.
```

For the literal interpretation, the coefficient of `pi^j` is the coefficient at the actual nonnegative power `j`, including zero. Adopt `deg(0)=-infinity`. For arbitrary finite `N,M>=0`, set

```text
S^w_(N,M) = K[c,rho,
              p_ij : 0<=j<=N, 0<=i<=3j,
              q_ij : 0<=j<=M, 0<=i<=3j].
P = sum p_ij*gamma^i*pi^j,
Q = sum q_ij*gamma^i*pi^j.
J^w_(N,M) = ( c*rho-1, all coefficients of Jac(P,Q)-c*gamma ).
```

The coefficient generator order is `c,rho`, then `p`, then `q`; within each family order `(j,i)` lexicographically. The variables `gamma,pi` are polynomial indeterminates over this coefficient ring, not coefficient unknowns. Equivalently one may work in `K[c,c^(-1),p,q]` and omit the inverse equation. Monicity, if desired, adds `p_0N=q_0M=1` and the other leading-pi coefficient equations; it cannot invalidate a unit certificate already present.

**Theorem 1.** `J^w_(N,M)=(1)` for every `N,M`. Thus there is no nonconstant pair, or any pair at all, satisfying the full forward wedge with `c!=0`.

**Proof.** The bound at `j=0` says `P(gamma,0)=p_00` and `Q(gamma,0)=q_00`. Both are constant in gamma. Hence both gamma derivatives are divisible by pi, and so is their Jacobian. Let

```text
E_10 = [gamma^1*pi^0](Jac(P,Q)-c*gamma) = -c,
h = c*rho-1.
```

Then the literal certificate is

```text
1 = -rho*E_10 - h.                                      (W1)
```

It holds in the coefficient ring itself, without radicals, saturation heuristics, or pointwise arguments. If `c` is a fixed nonzero scalar, use `1=(-1/c)*E_10`. The proof is independent of `N,M`, so the union over all finite degree caps is empty. In fact this particular theorem is valid in every characteristic. Only the constant-coefficient support restriction was used; none of the inequalities with `j>=1` was needed. ∎

An equivalent ambient presentation retains all coefficients in a larger rectangle and includes the forbidden support coefficients as equations. In that presentation the identity above is obtained after eliminating the support equations. This presentation is useful for checking an attempted source map: a forbidden coefficient is a receiver equation whose image must belong to the necessary source ideal.

This theorem should not be mistaken for a general classification of maps with a linear Jacobian. It says that a map constant along the line `pi=0` cannot have Jacobian `c*gamma`, which is nonzero along the generic point of that line.

### 2.1 What happens under the other plausible index conventions

If the bound is imposed only at `j=1`, or for every `j>=1`, or on reverse monic coefficients `[pi^(N-j)]`, the following exact family disproves emptiness:

```text
P = pi^N + (c/2)*gamma^2,   Q = pi,   N>=1,
Jac(P,Q)=c*gamma.
```

Both polynomials are monic in pi. For the reverse convention, the constant coefficient has allowed degree `3N`, and degree two fits. These solutions are excluded by the full forward convention precisely at `j=0`.

The entire monic affine-in-pi slice can be classified. Write `P=pi+B(gamma)` and `Q=pi+D(gamma)`. Then `Jac=c*gamma` if and only if

```text
D = B-(c/2)*gamma^2+d,    d in K.                         (W2)
```

For the positive-coefficients-only bound, `B` is arbitrary. For the reverse bound at pi-degree one, require `deg B<=3`. This is a complete classification of that slice, not merely an example.

Without monicity, write `P=A*pi+B`, `Q=C*pi+D`. The pi coefficient of the Jacobian is `A'*C-A*C'`. Its vanishing makes the nonzero pair `A,C` proportional over `K`. After an invertible constant linear target change, write the pair as `(A*pi+B,E(gamma))`. Its equation is `-A*E'=c'*gamma`, so the only possibilities are

```text
(a*pi+B,       -(c'/(2a))*gamma^2+e),
(a*gamma*pi+B, -(c'/a)*gamma+e),   a!=0.                  (W3)
```

Here `B` is arbitrary. This also explains why a universal fold assertion for all linear-Jacobian pairs would need extra hypotheses: `(gamma*pi,gamma)` has Jacobian `-gamma` and is birational, with a contracted critical line. No complete classification of arbitrary-degree solutions to the weaker or reverse-index receiver is established in this lane. Their status is **NONEMPTY; COMPLETE ALL-DEGREE CLASSIFICATION OPEN**.

### 2.2 Exact receiver controls

`receiver_exact.py` constructs the full wedge at `(N,M)=(2,2)` and calls the frozen guarded Singular wrapper over `QQ`, with the inverse row. It returns `UNIT_IDEAL_CHAR0`, accepted normal forms, dimension `-1`, and the exact certificate (W1) checked independently in SymPy. The Singular run itself takes about 0.02 seconds.

The control without a `c` inverse, at pi-degrees `(1,1)`, returns `POSDIM`, dimension seven, with accepted normal forms. The point family `P=pi`, `Q=pi+gamma^2`, `c=-2` checks that dropping the constant support condition makes the system nonempty even when `c` is a unit. These two changes therefore have the expected different effects.

An initial degree-two no-inverse control reached its declared 60-second timeout; its unpromoted result is retained in `c-zero-degree2-timeout/`. The sufficient degree-one control above replaced it. No theorem depends on that timeout or on a guessed dimension. The all-degree emptiness proof is (W1), not a finite CAS extrapolation.

## 3. Moh descent supplies a shifted Laurent support condition

On a licensed source branch, put `u=u_s`, `v=v_s`, `ell=v-u-1`, and retain the root truncation. Moh's substitution is

```text
theta=y^(-1), gamma=theta^(1/u), z=y-b*x-e,
sigma=A(gamma)+pi*gamma^v,
y=gamma^(-u),
x=b^(-1)*(gamma^(-u)-e-A(gamma)-pi*gamma^v).              (D1)
```

The finite sum `A` comes from the common inversion coefficients. For a safe finite chart it suffices to allow every exponent `0,...,v-1`; this enlarges the actual truncated sum and does not assert that every coefficient choice is realized. The source hypothesis gives polynomiality of the descended pair, monicity, and pi-degrees `n'=nu/d_s`, `m'=mu/d_s`, with `d_s=u+v` on the present cohort. The proposition gives

```text
Jac_gamma,pi(gbar(sigma),Tbar_1(sigma))
       = -(u/b)*gamma^(v-u-1).                          (D2)
```

Direct differentiation verifies the sign: `x_pi=-gamma^v/b`, `y_gamma=-u*gamma^(-u-1)`, and `y_pi=0`; therefore `Jac(x,y)=-(u/b)*gamma^ell`. The derivatives of `A` cancel from this determinant. They do not disappear from the descended polynomial coefficients.

Indeed, for `h(y,z)=sum h_ar*y^a*z^r`, its literal substitution has pi coefficient

```text
[pi^j]h(gamma^(-u),A+pi*gamma^v)
 = gamma^(v*j) * sum_(a>=0,r>=j) binom(r,j)*h_ar
                              *gamma^(-u*a)*A^(r-j).    (D3)
```

The surviving factor `A^(r-j)` invalidates the proposed argument that source polynomiality forces degree at most `v*j`. Negative gamma coefficients must cancel to obtain a polynomial; positive coefficients supplied by `A` need not vanish.

The true elementary support statement is obtained after a Laurent shear:

```text
D_tilde(gamma,pi)=D(gamma,pi-A(gamma)*gamma^(-v))
                =h(gamma^(-u),pi*gamma^v).
```

Every exponent `(i,j)` in this Laurent polynomial satisfies `i<=v*j` and `i congruent to v*j mod u`; negative `i` are allowed. The shear has determinant one but can destroy polynomiality in gamma. It is not the receiver in Theorem 1. For example `P=gamma^(-1)`, `Q=-c*gamma^3*pi` satisfy this Laurent wedge and have Jacobian `c*gamma`; the divisibility proof of Theorem 1 does not apply.

An explicit polynomiality control makes the failure visible. Set `u=1,v=3,A=gamma+gamma^2`, and in the source ring define

```text
F=y^3*z-y^2-y,  H=y*z-1,  G=F^2+H.
```

Then `(F,H,G)` descend exactly to

```text
(pi, gamma+gamma^2*pi, pi^2+gamma^2*pi+gamma).
```

The last polynomial is monic in pi and has the forbidden constant coefficient gamma. This is a counterexample to the asserted inference from polynomiality and monicity. It is not asserted to satisfy every Keller/source hypothesis, and is not a counterexample to the Jacobian conjecture. The stronger K16 control in §5 verifies the support problem on an actual reconstructed cone family.

A necessary but deliberately generous unshifted support rectangle is enough for an honest atlas. If the original polynomial has total degree at most `N` and `deg A<v`, its substitution has gamma exponents between `-uN` and `vN`, and pi-degree at most `N`. On a licensed branch, its negative gamma coefficients and its coefficients above the descended pi-degree vanish. These are precisely the extra source equations retained next.

## 4. A literal atlas with coefficient certificates

### 4.1 The enlarged source charts and their necessity

For a source record `alpha=(n,m,u,v,full decorations)` use `N=n`, `M=m` and work over `QQ`, or any characteristic-zero extension. Choose the source orientation of Moh's displayed pair, `F=source g`, `G=source T1`, with `Jac_XY(F,G)=1`. A nonzero original Jacobian scalar can be normalized first by an invertible scalar target change. Define

```text
R_alpha = QQ[b,beta,e,a_0,...,a_(v-1),
             f_rs (r+s<=N), g_rs (r+s<=M)],
F(X,Y)=sum f_rs*X^r*Y^s,    G(X,Y)=sum g_rs*X^r*Y^s,
A(gamma)=sum_(r=0)^(v-1) a_r*gamma^r,
Xtilde=beta*(gamma^(-u)-e-A(gamma)-pi*gamma^v),
Ytilde=gamma^(-u).
```

All source indices are nonnegative, and each coefficient family is ordered lexicographically by `(r,s)`, after the displayed scalar and truncation variables. Set `LF=F(Xtilde,Ytilde)` and `LG=G(Xtilde,Ytilde)`. Let `I_alpha` be generated by:

1. `b*beta-1`;
2. every coefficient `k_rs` of `K(X,Y)=Jac_XY(F,G)-1`;
3. every coefficient of `LF` outside `0<=gamma exponent<=vN`, `0<=pi exponent<=n'`;
4. the analogous coefficients of `LG` using `vM,m'`.

The upper gamma bounds already hold identically; the effective new rows in items 3–4 are negative-gamma rows and excessive-pi rows. This is an explicit finite necessary ideal on the licensed branch. It is not an identification with a pre-existing terminal ideal, and it does not silently impose the full characteristic tower's stronger equations.

Necessity is a source theorem: Proposition 6.3 supplies a truncation and coordinates for each licensed actual source, and its polynomiality and degree conclusions supply items 3–4. Adjoining these witness coordinates produces a chart lying over each such source. Allowing all coefficients in `A` enlarges the chart. The statement is conditional on the radius branch; the numerical key does not license that branch. The complementary branch is retained explicitly.

The only inverted source coordinate here is `b`, represented by `beta`; `b=0` is outside this declared Moh coordinate chart, whose nonzero leading slope is part of (D1). There is no inversion of a leading coefficient discovered by reduction, a root difference, a discriminant, or gamma in the coefficient ring. Gamma inversion is used only to expand auxiliary Laurent polynomials.

### 4.2 One finite common receiver per coarse key

For a cohort key `beta_key=(n',m',ell,V2')`, take maxima over its source records:

```text
Bp=max(v*N), Bq=max(v*M).
S_beta = QQ[c,rho,
            p_ij (0<=i<=Bp,0<=j<=n'),
            q_ij (0<=i<=Bq,0<=j<=m')].
P=sum p_ij*gamma^i*pi^j, Q=sum q_ij*gamma^i*pi^j,
J_beta=(c*rho-1, all coefficients of Jac(P,Q)-c*gamma^ell).
```

Receiver generator order is `c,rho`, then `p`, then `q`, each family lexicographically ordered by `(i,j)`. These are finite rectangles with no monicity or exact-degree requirement. Dropping those requirements makes a necessary overapproximation; it does not prove that lower-degree receiver points realize the marked source. All inherited `M'`, `V'`, heights, and branch data remain attached to the separate source records.

The literal homomorphism is

```text
phi_alpha_beta(p_ij) = [gamma^i*pi^j] LF,
phi_alpha_beta(q_ij) = [gamma^i*pi^j] LG,
phi_alpha_beta(c) = -u*beta,
phi_alpha_beta(rho) = -b/u.                             (A1)
```

Extra receiver coefficients map to zero when they lie beyond that source's support. Every image is a finite polynomial in the displayed source generators. For clarity, the contribution of `f_rs` to `phi(p_ij)` is obtained by expanding

```text
beta^r*gamma^(-u*s)
       *(gamma^(-u)-e-sum a_h*gamma^h-pi*gamma^v)^r.
```

Choose counts `t0,te,t_0,...,t_(v-1),j` summing to `r`. The gamma exponent is `-u*(s+t0)+sum h*t_h+v*j`. When it equals `i`, add

```text
beta^r * r!/(t0!*te!*j!*product t_h!)
       *(-1)^(te+j+sum t_h)*e^te*product a_h^t_h.
```

This finite multinomial formula declares each generator image without relying on matching variable names or a solver. The `g_rs` images use the identical rule.

### 4.3 Exact pullback cofactors, before any emptiness claim

Let `P*=phi(P)`, `Q*=phi(Q)`, and write `E=LF-P*`, `H=LG-Q*`. Every coefficient of `E,H` is a source generator of type 3 or 4, or identically zero. Chain rule and bilinearity give the polynomial identity in the auxiliary Laurent ring

```text
Jac(P*,Q*)+u*beta*gamma^ell
 = -u*beta*gamma^ell*K(Xtilde,Ytilde)
   -Jac(E,LG)-Jac(P*,H).                               (A2)
```

No radical is involved. Here is a coefficient certificate for each receiver row. Write `E=sum e_ab*m_ab`, `H=sum h_ab*m_ab`, where `m_ab=gamma^a*pi^b` and `(a,b)` runs through the excluded support. For `r_ij=[gamma^i*pi^j](Jac(P,Q)-c*gamma^ell)`, (A2) becomes

```text
phi(r_ij)
 = sum_(r,s) k_rs * (-u*beta*[gamma^(i-ell)*pi^j]
                               Xtilde^r*Ytilde^s)
   + sum_(a,b) e_ab * (-[gamma^i*pi^j]Jac(m_ab,LG))
   + sum_(a,b) h_ab * (-[gamma^i*pi^j]Jac(P*,m_ab)).      (A3)
```

Each cofactor is a finite element of `R_alpha`. The auxiliary negative exponents disappear after coefficient extraction; they do not demand a further localization of the coefficient ring. If desired, expand every Jacobian by

```text
Jac(gamma^a*pi^b,gamma^d*pi^e)
       =(a*e-b*d)*gamma^(a+d-1)*pi^(b+e-1).
```

The inverse row has image `phi(c*rho-1)=b*beta-1`. Thus (A3) and this last identity prove the literal inclusion `phi(J_beta) subset I_alpha`. They give a finite certificate matrix for every source, valid at its actual `N,M`, not merely for the small CAS controls.

Consequently, if a receiver certificate is `1=sum A_i*r_i`, applying phi and then (A3) yields a source certificate with coefficients `sum_i phi(A_i)*C_ik`, where `C_ik` are the displayed pullback cofactors. This is the required certificate transport. If the source localization were represented without an inverse variable, clearing its finitely many denominators would yield a power of the localizing element in the original ideal; its zero locus would still require a separate branch.

The same argument explains exactly why omitting negative or excessive-pi rows is unsound. The projection from a Laurent polynomial to its retained rectangle does not commute with differentiation and multiplication. The correction terms in (A2) are necessary. An exact negative control takes the source pair `(y,z)` with Jacobian one: its Laurent descent has Jacobian `-gamma`, while the nonnegative-gamma projection of the first component is zero and the projected pair has Jacobian zero.

### 4.4 The larger receivers are provably nonempty

For every key in this finite inventory, the declared caps contain

```text
P=pi, Q=pi+gamma^(ell+1),
c=-(ell+1), rho=-1/(ell+1).                            (A4)
```

This is a rational point of `J_beta`; the inventory checks every cap. More generally, `P=pi+B(gamma)`, `Q=P-c*gamma^(ell+1)/(ell+1)+d` gives the full monic affine slice for a fixed scalar `c`, with `B` restricted to the declared gamma caps. Therefore none of these larger receiver ideals is unit. They cannot kill any source by emptiness, including the 32 keys assigned to their exponent-one part.

The maps are valid because their equations and cofactors were proved. Their usefulness for eliminating marked source configurations would require a stronger receiver retaining further necessary information. A small number of nonempty supersets is not evidence that the actual solve workload has compressed by the same factor.

## 5. K16 and the (8.1) atom: explicit map and exact obstruction

Fix `t>=2` and a field factor of `QQ[d]/(3d^2-t-1)`. Treat both factors separately at split indices. Use the frozen scalar units `y,g`, set `q=2t+1`, `e=3t+1`, and `c=-yg`. The normalized positive source ideal is `I_+`; its reconstructed coefficient ring is `R_t=K[c1,...,c_(t-1),b]`. The high recurrence determines `B,eta,W`, and the charged identity says

```text
tau=-(gy/3)*B*eta mod I_+,
T0=yg+tau, I_full=I_++(T0).
```

The positive cone `I_+`, its open atom chart `tau!=0`, and the full terminal ideal `I_full` are three different objects. In particular a cone point with `tau=0` is not a point of `I_full`.

Write `z=pi-gamma` and, after the banked spine,

```text
x=h-b4=pi^3*(z+b1)+B*pi^2+b*pi,
Kaux=x^2*C-y*b, Faux=x*T-g*b, Yaux=x*S-b*T-g*B,
Q=U(x)+Kaux(x)/pi+y*x/pi^2,
P=P0(x)+Yaux(x)/pi+Faux(x)/pi^2+g*x/pi^3.               (K1)
```

Here `x` is the substituted auxiliary polynomial, not an independent coordinate. The Laurent display cancels to ordinary polynomials. Additive gauges in `P0` do not affect the argument. The exact reconstructed identity is

```text
Jac_gamma,pi(Q,P)=c*gamma+(tau-c)*pi mod I_+.             (K2)
```

**Uniform support obstruction.** In every allowed factor and at every `t`,

```text
[gamma*pi^0]P=-g.                                      (K3)
```

Gamma first enters `x` as `-gamma*pi^3`. A polynomial in `x` divided by at most `pi^2` cannot contribute a gamma term at pi-degree zero. The last summand in (K1) contributes exactly `-g*gamma`. Cancellation of negative Laurent powers does not change this coefficient. Thus the normalized K16 reconstruction has precisely a coefficient that the full forward wedge prohibits. Its coefficient is a scalar unit, not a potential vanished-leader branch.

There is a literal coordinate map straightening the critical line:

```text
chi(gamma)=Gamma+(1-tau/c)*Pi,   chi(pi)=Pi.              (K4)
```

Its determinant is one and it uses only the scalar unit `c`. Substituting (K2) gives `Jac(chi(Q),chi(P))=c*Gamma mod I_+`. But `[Gamma*Pi^0]chi(P)=-g` still. Straightening the linear Jacobian does not repair the forbidden support.

On the atom chart declare the localization `R_t[tau^(-1)]`. Set `lambda=c/tau`, and restore monicity by

```text
Qhat=lambda^q*chi(Q), Phat=lambda^e*chi(P).
```

The leading Pi degrees are `4q,4e`, and

```text
Jac(Qhat,Phat)=c*lambda^(q+e)*Gamma,
[Gamma*Pi^0]Phat=-g*lambda^e.                           (K5)
```

A relaxed receiver accepting these actual polynomial supports has the literal coefficient map `a_ij -> [Gamma^i Pi^j]Qhat`, `b_ij -> [Gamma^i Pi^j]Phat`, `C -> c*lambda^(q+e)`, `Cinv -> c^(-1)*lambda^(-q-e)`. Its Jacobian rows pull back into the localized positive ideal by (K2), substitution, and scaling. Its inverse row maps to zero.

In the ambient presentation of the requested wedge, however, the support equation `b_10=0` maps to **the unit `-g*lambda^e`**. Proving that this unit belongs to the localized source ideal would already prove the atom chart empty. Assuming this membership as a necessary-support fact would assume the theorem being sought. On `I_full`, `tau=c`, so the shear and scaling are the identity and the same obstruction is `-g`. This does not rule out abstract homomorphisms to an already zero quotient; it rejects the proposed source reconstruction as an independent proof of that quotient's emptiness.

### 5.1 An exact K16 family that catches the error

The frozen `(REC)` reconstructs an entire free-`b` cone family at `t=2,d=-1`:

```text
y=1/5, g=7/125, c=-7/625,
C=x, W=-25*x^5/4+(5*b/2)*x^2, B=eta=b1=0,
U=x^5-(b/2)*x^2, P0=x^7-(7*b/20)*x^4,
T=14*x^2/25, S=7*b*x/25+7*x^4/5,
x=pi^3*(pi-gamma)+b*pi.
```

The driver `k16_map_check.py` substitutes into F3 and REC, verifies polynomiality of (K1), and computes the Jacobian exactly over `QQ[b]`. It obtains

```text
deg_pi Q=20, deg_pi P=28; both monic,
Jac(Q,P)=7*(pi-gamma)/625,
[pi^0]Q=0, [pi^0]P=-7*gamma/125.
```

Its complete support scan finds exactly one full-wedge violation: `(gamma exponent,pi exponent)=(1,0)` in `P`, with coefficient `-7/125`. Every proposed positive-pi coefficient inequality passes. This is an exact family, not a modular or numerical point.

On `Gamma=gamma-pi`, `Pi=pi`, its Jacobian becomes `-7*Gamma/625`, while the forbidden coefficient remains. The Pi degrees change to `(15,21)` with leading coefficients `-Gamma^5,-Gamma^7`; monicity is not preserved on this `tau=0` branch. One must not apply the `tau^(-1)` normalization there. This directly falsifies the claim that Fable's advertised exceptional cone controls are points of the full forward-wedge receiver.

### 5.2 The conditional K16 chain remains conditional

The charged valid implication chain is

```text
B*eta vanishes on V(I_+)
 <=> tau belongs to radical(I_+)
 <=> (8.1), equivalently I_full=(1)
  => terminal normalized chart empty
  => original K16 ray system empty at that t
  => (T) at that t.
```

It uses the charged cone lemma, scalar normalizers, and spines; it does not identify literal `T0` with `tau`. This lane proves none of the new all-`t` antecedents. Its typed disposition for the proposed wedge is `UNASSIGNED[K16-SUPPORT-PI0]`. The charged finite successes remain unchanged. There is no new whole K16 index, no all-ray closure, and no implication discharging (8.1) or (T) from Theorem 1.

## 6. Cohort replay, three concrete interfaces, and exact coverage

The historical selected cohort consists of 296 `u_s>=2` records and 132 keys `(n',m',ell,V2')`. `cohort_inventory.py` checks membership against the prior audit, reconstructs each row with the frozen skeleton implementation, verifies the windows and conditions (8)–(13), and checks `d_s=u+v` and terminal radius `-1`. It retains all decorations and does not infer realizability from the arithmetic checks.

| ell | Keys | Source rows |
|---:|---:|---:|
| 0 | 43 | 141 |
| 1 | 32 | 87 |
| 2 | 19 | 22 |
| 3 | 11 | 18 |
| 4 | 11 | 11 |
| 5 | 6 | 7 |
| 6 | 8 | 8 |
| 7 | 1 | 1 |
| 8 | 1 | 1 |
| **Total** | **132** | **296** |

Among the 87 exponent-one records, 72 have `(u,v)=(2,4)` and 15 have `(u,v)=(3,5)`. Thus even the exponent-one part of this `u_s>=2` cohort has shifted slope four or five, whereas the slope three discussed for Fable's 671 records comes from their separate `u_s=1` population. Equality of `ell` cannot equate the support maps.

### 6.1 The collided `(36,24,2,5)` key, two actual source interfaces

The source records are

| `(n,m)` | `M2,...,Ms` | `V2,...,Vs` | `u,v` | Inherited `M'`, including `M1'` |
|---|---|---|---|---|
| (126,84) | (-14,63,124) | (5,10,5) | (2,5) | (-24,-4,18) |
| (126,84) | (112,119,124) | (5,10,5) | (2,5) | (-24,32,34) |

Each has `d_s=7`, `n'=36`, `m'=24`, `ell=2`. On its separately declared radius branch `delta*_(s-1)>=5/2`, take

```text
A=a_0+a_1*gamma+...+a_4*gamma^4,
Xtilde=beta*(gamma^(-2)-e-A-pi*gamma^5),
Ytilde=gamma^(-2), phi(c)=-2*beta, phi(rho)=-b/2.
```

Their common target rectangles have caps `(Bp,n')=(630,36)` and `(Bq,m')=(420,24)`, with Jacobian `c*gamma^2`. For each source, (A1) is its actual coefficient homomorphism, and (A3) is the certificate for every target equation. This validates the common receiver despite the distinct characteristic sequences. The source records and ideals remain separate; no isomorphism of their decorated descendants is asserted.

Their inherited terminal anchors are 17 and 1, respectively; the associated conditional inherited terminal-radius formula gives `-3/17` and `-3`. Those numbers are retained in the inventory and are not substituted for the original minor-disc licensing radius. Neither row has exponent one, and neither is assigned to the requested wedge. Each returns `ASSIGNED_CONDITIONAL_BROAD_MONOMIAL_RECEIVER` on the licensed branch and `UNASSIGNED_SPLIT_OBLIGATION` on the complement.

### 6.2 A concrete exponent-one source

Take `(n,m)=(144,120)`, `M2,...,Ms=(132,138,142)`, `V2,...,Vs=(5,5,4)`. Then

```text
u=2, v=4, d_s=6,
(n',m',ell,V2')=(48,40,1,5),
M'=(-40,44,46).
```

On `delta*_(s-1)>=2`, the literal substitution is

```text
A=a_0+a_1*gamma+a_2*gamma^2+a_3*gamma^3,
Xtilde=beta*(gamma^(-2)-e-A-pi*gamma^4),
Ytilde=gamma^(-2), phi(c)=-2*beta, phi(rho)=-b/2.
```

The target caps are `(576,48)` and `(480,40)`, and the target Jacobian is `c*gamma`. The pullback of its inverse equation is `b*beta-1`; all Jacobian rows pull back by (A3). This is an actual certified map to the larger exponent-one receiver. It is not an assignment to the full forward wedge. The inherited terminal anchor is one, and the retained conditional inherited terminal radius is `-2`.

All three pilots therefore have literal maps with ordinary ideal-membership certificates on their licensed branches. All three remain UNASSIGNED for the requested wedge and on their complementary split branches. The two collided rows validate legitimate sharing; the third prevents an exponent mismatch from hiding the support problem.

### 6.3 What the exact validation establishes

The three pilot interfaces instantiate the universal finite-ring construction at their actual source degrees, including all negative and excessive-pi rows. The mathematical identities (A1)–(A3) prove every generator image for those sizes. They do not depend on expanding the entire high-degree system in CAS.

As independent exact algebra controls, `receiver_exact.py` expands generic quadratic source pairs for `(u,v)=(1,3),(2,5),(2,4)`, splits off their negative-gamma and excessive-pi rows, and checks the chain-rule identity and the coefficient correction identity as exact zero polynomials. These small controls test signs, orientation, and projection handling; they are not represented as Gröbner solves of the 126- or 144-degree source charts. The cohort driver separately verifies the actual metadata, degree caps, scalar images, and branch declarations.

The inventory's `132/132` means every key has a proved common larger receiver on licensed descent charts. It does not mean every original source route is covered: all 296 records have `u_s>=2`, so Proposition 6.4 cannot discard the complement. It also does not mean a single empty receiver has been found. The full requested receiver coverage is exactly `0/132`, and its UNASSIGNED count is exactly 132.

## 7. Residue, all-degree verdict, and promotion boundaries

Fable's charged count `671/1110` measures exponent-one descendants inside the complete historical `u_s=1` phase. This count is independently reproduced from the hash-checked snapshot in `cohort/us1-residue-audit.json`: its exponent histogram is `{1:671,2:317,3:71,4:9,5:33,6:3,7:6}`. Applying either stored Xu filter to that phase instead gives `647/1076`. Thus `671/1110` is the charged historical population, not a newly surviving sharpened residue. For that population, the radius is automatic and `ell=1` means `v=3`. This makes (D1) available; it does not erase `A`, turn shifted Laurent support into unshifted polynomial support, or remove K16's unit forbidden coefficient.

Accordingly, this lane's discharged fraction is **0/1110**, including **0/671** of the advertised exponent-one clients. The fraction `671/1110` remains a population measurement, not a killed population. The literal receiver's unit certificate can be used only after a necessary source pullback is proved. For the proposed K16 reconstruction, its failed support image is explicit; for the cohort, the compiler returns the requested UNASSIGNED states.

The final theorem dispositions are:

- **PROVED-HERE, ALL DEGREE:** the literal full forward-wedge receiver has ideal `(1)`, with certificate (W1).
- **PROVED-HERE, NECESSARY MAPS:** the larger finite atlas has explicit homomorphisms and ordinary ideal-membership cofactors (A1)–(A3), covering 132/132 cohort keys on licensed branches; its exponent-one subfamily covers 32/132.
- **PROVED-HERE, NONEMPTY:** every larger receiver in this finite atlas has witness (A4). The alternative parenthetical/reverse-index receivers also have explicit families; the entire affine slice is classified.
- **REJECTED AS STATED:** the source-polynomiality argument for the full forward wedge, and the claim that the reconstructed K16 cone belongs to that receiver.
- **OPEN:** complete arbitrary-degree classification for the weakened/marked receivers, new all-`t` K16/(8.1)/(T) closure, and a receiver atlas that both covers and eliminates all source branches.

An all-degree completion still needs a theorem that every remaining source branch reaches an appropriate necessary receiver, together with an elimination or classification theorem strong enough for the source markings and a valid treatment of the split alternatives. Neither an integer key nor a growing finite census supplies that theorem. The present construction shows how to make a map honest, and why honesty by itself does not make a nonempty receiver eliminate its clients.

## 8. Reproduction, guardrail checks, and completion

Primary reproducible artifacts:

| Path under `box/recvatlas-20260905/` | Content |
|---|---|
| `frozen-inputs.sha256` | Receipt-generated nine-input manifest |
| `receiver_exact.py`, `receiver-exact-results.json`, `receiver-exact.out` | Uniform certificate, exact wrapper controls, shifted-support and projection controls |
| `literal-unit/`, `c-zero-control/` | Exact-Q Singular scripts, outputs, and accepted guarded certificates |
| `c-zero-degree2-timeout/` | Retained unpromoted diagnostic timeout |
| `k16_map_check.py`, `k16_map_check.json` | Exact free-`b` F3/REC family, Jacobian, support failure, and reorientation |
| `cohort_inventory.py`, `cohort/inventory.json` | All 296 sources, 132 receivers, maps, caps, and branch dispositions |
| `cohort/pilot-interfaces.json`, `cohort/summary.json`, `cohort/us1-residue-audit.json` | Three concrete interfaces, coverage counts, and the 671/1110 population replay |
| `cohort/new-read-inputs.sha256` | Supplemental historical cohort provenance |
| `receiver-audit.md`, `k16-map.md`, `cohort/README.md` | Independent derivations supporting this report |

The drivers run from the repository root with `python3`. Numerical libraries are limited to one thread; the guarded wrapper explicitly requests one Singular core. The relevant commands are:

```sh
sha256sum -c box/recvatlas-20260905/frozen-inputs.sha256
sha256sum -c box/recvatlas-20260905/cohort/new-read-inputs.sha256
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 box/recvatlas-20260905/receiver_exact.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 box/recvatlas-20260905/k16_map_check.py
PYTHONDONTWRITEBYTECODE=1 python3 box/recvatlas-20260905/cohort_inventory.py
```

FALLACY-v2 checks: source, receiver, and auxiliary polynomial rings are distinct; all coefficient maps and generator orders are declared; localizations have explicit inverse rows; split and tau-zero branches are retained; no scalar-state coincidence is used as a pullback proof. Projection errors have a negative control. No `sat()` return wrapper is used. No lower bound is promoted to attainment, and no physical-place or exit-count claim is made. No new exit-price assertion is made, so the charge-basis validator returns `ABSENT`; no charge-basis line is applicable.

The receiver and map proofs were independently audited. Exact controls pass. The frozen and supplemental input manifests are rechecked at completion, no lane computation remains running, and the final report receives its BODY-END integrity seal. The result is a proved empty literal receiver, a proved larger conditional atlas, and an explicit failure of the proposed common-receiver elimination chain.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `37214`.
- Body SHA-256:
  `ed776bdd39cb3de61301a70d934898898a7041622fee0db5f5eaedd2ab4ddfa2`.
- Frozen basis: `e7079e10ac6d2a5be8c93f4cfbb0bb1b97c5816c`.
