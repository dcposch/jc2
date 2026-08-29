# Hostile review: cyclic semi-invariance repair

Date: 2026-08-28  
Reviewer: GPT-5.6-terra / Codex  
Reviewed file hash: `9feb612a58a8db274886ec748b7c1349f2672a0ae416e74f14116a45272e01ea`  
Overall verdict: **CONDITIONAL; the cyclic lemma is correct, but the
Statement 8.5 application needs two explicit compatibility lines.**

## Executive finding

No genuine characteristic-vertex counterexample to the proposed
semi-invariance law was found.  On either tree component, the coefficient
selected by Notations 3.9--3.10 is one Laurent `t`-coefficient, and the
prefix stabilizer makes that coefficient a single effective cyclic
eigencharacter.  The kernel argument really forces `e_j | N`, and the ODE
then forces the character of `p_(h,G)` to be `1` modulo `nu_G`.

The coordinator report overstates the completion in two places:

1. `G notin V_(2,a)` plus Statement 3.18 is not, by itself, the displayed
   one-orbit formula `p_G=(eta^nu-c^nu)^l`.  One must add the short
   root-realization/no-second-orbit argument using Definition 3.4 and
   Notation 3.8 (or cite a corrected result which contains it), and retain
   an arbitrary nonzero scalar factor `C`.
2. Proposition 4.6 may be used only after identifying `G` as a correctly
   typed `T_a^+` or `T_a^-` terminal-tower packet, with the centred first
   polynomial and the required shift `b`.  The printed Statement 8.5 does
   not spell this out, and the coordinator report merely calls `h=h_G`.

With those lines supplied, the repair proves the needed gcd conclusion of
Statement 8.5.  It also supplies the *formal zero-order residual descent*
needed in Section 7 after the arbitrary-truncation extension below.  It does
not identify the resulting quotient line with a component of a final common
graph resolution, so it does not repair the distinct Section 7
coefficient-chart/no-duplication gap.

## Clause ledger

| clause | verdict | check / minimal fix |
|---|---|---|
| Definition 3.1 divisibility below `beta_j` | **PASS** | For `e=e_(j-1)`, Definition 3.1 makes `beta_j` the first nonzero supported exponent not divisible by `e`.  Thus every supported `r<beta_j` is divisible by `e` (including `r=0`), and `e | kappa`. |
| `y`-side stabilizer and sign convention | **PASS** | With `x=t^(-kappa)`, `y=phi(t)+t^(beta_j)eta`, `zeta in mu_e` fixes `x` and `phi`; sending `eta` to `zeta^(-beta_j)eta` fixes the full substituted point.  Hence `A(zeta t,zeta^(-beta_j)eta)=A(t,eta)` and `A_N(zeta^(-beta_j)eta)=zeta^(-N)A_N(eta)`.  Both signs in the coordinator report are correct. |
| `x`-side | **PASS** | Exchange `x` and `y`: take `y=t^(-kappa)`, `x=phi(t)+t^(beta_j)eta`.  The same calculation, including the `zeta^(-beta_j)` action and coefficient character `zeta^(-N)`, applies verbatim.  It should be written once in the repaired lemma rather than called merely “symmetric.” |
| Effective action | **PASS** | `gcd(e,beta_j)=e_j`, so the image of `mu_e` under `zeta -> zeta^(-beta_j)` has order `e/e_j=nu_F`.  The action on `eta` therefore factors through the effective scalar group `mu_(nu_F)`. |
| Kernel forcing | **PASS** | The kernel is `mu_(e_j)`.  For `zeta` in it, the coefficient relation reads `A_N=zeta^(-N)A_N`; a nonzero selected coefficient forces `e_j | N`.  After this, `beta_j r = N (mod e)` has one solution `r (mod nu_F)`, so all eta monomials of `A_N` occupy one residue class and `A_N=eta^s R_N(eta^(nu_F))`. |
| Selected residual is one `t`-coefficient | **PASS** | The truncation is finite and `a(x,y)` is polynomial, so its substitution is a finite Laurent polynomial in `t` with polynomial eta-coefficients.  Notation 3.10 selects one nonzero coefficient (the sign change is `N=-j` when the source writes `x^(j/kappa)`), not a sum of different `t`-weights. |
| Suitable-denominator multiples | **CONDITIONAL** | The claim is true only with synchronized refinement.  If `K'=L K`, use `t=(t')^L`, so `n'=Ln`, `e'=Le`, the selected exponent becomes `N'=LN`, and `e'/gcd(e',n')=e/gcd(e,n)`.  State this.  A bare “suitable denominator only refines grading” is insufficient without the coordinate relation. |
| Characteristic-vertex semi-invariance for arbitrary polynomial `a` | **PASS** | No Jacobian or resolution input is used.  The proof applies to every polynomial, including a shifted terminal polynomial `g-b`, once it is a correctly typed polynomial input. |
| One-orbit shape of `p_G` in Statement 8.5 | **CONDITIONAL** | The source and coordinator say that `G notin V_(2,a)` and Statement 3.18 yield `(eta^nu-c^nu)^l`, `c!=0`.  Statement 3.18 gives realization of a rotated nonzero root, not this formula alone.  Add: a second effective `mu_nu` root orbit (or a zero root together with a nonzero orbit) gives two realized branches whose first different coefficient is at `pi(G)`, hence puts `G` in `V_(2,a)` by Definition 3.4.  If only zero occurs, Statement 3.16 makes `nu_G=1`.  Thus for `nu>1` exactly one nonzero orbit occurs, all roots have one multiplicity, and `p_G=C(eta^nu-c^nu)^l` for `C in C*`.  The omitted scalar is harmless for the character argument but is not licensed by Notations 3.9--3.10. |
| ODE character argument | **CONDITIONAL** | Given the one-orbit formula and a typed Proposition 4.6 identity, it is correct.  If `p(omega eta)=p(eta)` and `q(omega eta)=omega^s q(eta)`, then `q'(omega eta)=omega^(s-1)q'(eta)` and `p'(omega eta)=omega^(-1)p'(eta)`.  Thus both ODE terms have character `s-1`, while the nonzero `p^mu` term has character zero, forcing `s=1 (mod nu)`.  The sign/scalar on the right side is irrelevant. |
| Proposition 4.6 compatibility | **CONDITIONAL** | It must be stated that the `h` in the ODE is the terminal `h_(G,b)` of Proposition 4.2 or 4.3, that `G` lies in its allowed side, and that the centred first polynomial and the condition-(7) shift are the ones used there.  The printed `p_(h,G)` in Statement 8.5 and the report's “terminal tower polynomial” do not themselves establish this. |
| `nu=1` split | **PASS** | `gcd(1,deg p_(h,G))=1` is automatic; no eta-factor assertion is necessary. |
| Conclusion `gcd(nu_G,deg p_(h,G))=1` for `nu>1` | **PASS, conditional on the preceding two rows** | From `q=eta R(eta^nu)`, `deg q=1+nu deg R`, hence it is coprime to `nu`.  This is exactly the final arithmetic input used in the corrected Statement 8.5 computation. |

## Arbitrary-truncation extension and Section 7

The coordinator's written lemma is stated only at a characteristic exponent
`beta_j/kappa`.  That alone does **not** close Section 7, whose critical-value
flag may be an arbitrary rational truncation.  The natural extension in the
follow-up request is valid with one essential precision.

Let `u=n/K`, choose a common/suitable Puiseux denominator `K`, and write on
the `y`-side

```text
x=t^(-K),
y=phi(t)+t^n eta,
phi(t)=sum_(r<n) c_r t^r.
```

Define

```text
e = gcd(K, { r<n : c_r != 0 }).
```

The inclusion of `K` is indispensable.  Then `mu_e` fixes `x` and the
prefix, acts by `eta -> zeta^(-n)eta`, and has effective image of order

```text
m=e/gcd(e,n).
```

For every polynomial `h`, if

```text
H(t,eta)=h(t^(-K),phi(t)+t^n eta)=sum_N t^N H_N(eta),
```

then

```text
H_N(zeta^(-n)eta)=zeta^(-N)H_N(eta).                  (A)
```

The identical statement holds on the `x`-side after interchange of `x,y`.
The kernel `mu_(gcd(e,n))` forces `gcd(e,n) | N` for every nonzero `H_N`, and
each such coefficient is one effective `mu_m` character.  Under a refinement
`K'=LK`, all of `n,e,N` scale by `L`, so `m` and the conclusion are unchanged.

If `d_(h,F)=0`, Notation 3.10 selects `N=0` (its `x^(j/K)` index is `j=0`).
Equation (A) then makes `p_(h,F)` invariant under the effective action, hence

```text
p_(h,F)(eta) in C[eta]^(mu_m) = C[eta^m].
```

Therefore this corrected arbitrary-truncation lemma **does supply the
zero-order cyclic polynomial-descent step** for Section 7: at a cv flag apply
it to `h=f-a` and `h=g`, whose centred orders are both zero.  It supplies no
more: it does not prove that this formal quotient is the actual affine chart
of a divisorial component on one final graph resolution, that finite
collision points remain in that chart, or that different components cannot
duplicate a direction cluster.  Those remain the separate
resolved-direction-chart lemma obligations.

If `e` is instead read as the gcd of supported exponents *without* `K`, the
assertion is false.  For example `K=3`, `phi=t^2`, and `n=3` has support-gcd
two, but `t -> -t` changes `x=t^(-3)` and is not a deck symmetry of the
substitution.  This is not a counterexample to the corrected definition
including `K`; it is the minimal reason that condition must be explicit.

## Minimal repair

Retain the coordinator's coefficient proof, but make these changes:

1. State it with a chosen suitable denominator and the synchronized
   refinement rule; include the one-sentence `x`-side calculation.
2. Insert the Definition 3.4/Notation 3.8 argument proving the unique
   nonzero effective root orbit of `p_G` under `G notin V_(2,a)` and
   `nu_G>1`, writing `p_G=C(eta^nu-c^nu)^l` with `C!=0`.
3. Cite or prove the exact Proposition 4.6 packet at `G` (side, centred
   polynomial, terminal `h_(G,b)`, and shift hypothesis) before applying the
   ODE.
4. Add the arbitrary-truncation corollary above.  Cite it in Section 7 only
   for zero-order residual descent, never for the global coefficient-chart or
   no-duplication assertions.
