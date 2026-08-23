# Unrestricted K2C fails; residue-A K2C remains a separate wall

**Date:** 2026-08-23

**Inputs read in full:** `xmodel/sol-unify.md`, `xmodel/sol-bdelay.md`,
`SHEET6-DEPTH.md`.

**Tier convention:** **EXACT** means an identity or a proved
polynomial-origin construction. **FORMAL** means H1 tree arithmetic with no
asserted polynomial realization. Every new uniform statement is labelled
**CONJECTURE**.

## 0. Verdict

\[
 \boxed{\textbf{NO KELLER-TIER UNIFICATION IS PROVED.}}
\]

There are two different assertions.

1. **The literal residue-A question is open.** No actual noninvertible
   Keller pair of type `(2,3)`, `td=6`, with the residue-A two-pole entry is
   known. In particular, there is no polynomial realization of the exact
   Lemma-2.2 insertion with its fixed terminal handshake. The three proposed
   tools do not prove that such a realization is impossible.
2. **The proposed general bridge is false.** Polynomial origin, the full
   pure-boundary identity, bounded topological degree, and
   Abhyankar--Moh/semigroup compatibility do **not** bound a pole Puiseux
   denominator. Section 2 gives actual Keller automorphisms with

   \[
     \operatorname{td}=1,
     \qquad \kappa=42\cdot2^r,
   \]

   and with characteristic indices `(7,3,2,2,...,2)`. Thus the obstruction
   is genuine, not an artifact of the FORMAL sheet calculus.

The actual family is not residue A: it is a one-place coordinate family,
has reduced degree type `(1,2)`, and degree-minimizes to the identity.
Consequently it does not realize the residue-A handshake (2.7) of
`sol-unify.md`. It does prove that any **unrestricted** reading of K2C for
all Keller pairs is false. It does not refute K2C in its intended
degree-minimal, nonautomorphic, normalized type-`(2,3)` sector; that
restricted statement remains a conjecture.

Hence G2/UCD still needs its own carrier bound. KJN, if proved, closes G5
only.

## 1. What the FORMAL tower proves

At H1 arithmetic tier, the case-(II) equations give

\[
 (\rho,\nu,\bar\kappa)=(1,2,5)
 \longmapsto (2,q,2q+2),
\]

and then

\[
 (2,q,2q+2)\longmapsto(2,q',2q'+2),
 \qquad q,q'\ge2.                                  \tag{1.1}
\]

For `q=q'=2`, every step fixes

\[
 w=\frac{\bar\kappa-\rho}{\nu}=2                  \tag{1.2}
\]

and multiplies the characteristic gcd product by `2`. Repeating `r`
times gives

\[
 \kappa_i=42\cdot2^r,                              \tag{1.3}
\]

while the FORMAL pole inventory retains

\[
 \mathcal E_{\rm MR}=1,
 \qquad \operatorname{td}=6,
 \qquad \deg\Psi=36.                               \tag{1.4}
\]

Equations (1.1)--(1.4) are **EXACT H1 arithmetic** and **FORMAL as to
polynomial origin**. They do not supply coefficients of `f` and `g`.

## 2. Actual Keller fixed-`td` realization of the carrier mechanism

### Theorem 2.1 (**EXACT, polynomial-origin**)

For every `r >= 0` there is a polynomial automorphism
`Phi_r=(f_r,g_r)` of `A^2` with Jacobian `1` such that the unique pole
branch of a generic fiber `f_r=a` has characteristic product

\[
 \kappa_r=42\cdot2^r.                               \tag{2.1}
\]

Its characteristic indices are

\[
 7,3,\underbrace{2,\ldots,2}_{r+1\text{ factors}}, \tag{2.2}
\]

whereas

\[
 \operatorname{td}(f_r,g_r)=1.                     \tag{2.3}
\]

#### Construction and proof

Put `s=r+4` and

\[
 q_1=7,\qquad q_2=3,\qquad q_i=2\quad(3\le i\le s).
                                                               \tag{2.4}
\]

Define

\[
 P_0=x,\qquad P_1=y,\qquad
 P_{i+1}=P_i^{q_i}-P_{i-1}\quad(1\le i\le s),       \tag{2.5}
\]

and set

\[
 (f_r,g_r)=(P_s,P_{s+1}).                           \tag{2.6}
\]

Indeed, for

\[
 H_q(u,v)=(v,v^q-u),                                \tag{2.7}
\]

one has `J(H_q)=1` and

\[
 (P_s,P_{s+1})=H_{q_s}\circ\cdots\circ H_{q_1}(x,y).
                                                               \tag{2.8}
\]

Each `H_q` has polynomial inverse `(u,v) -> (u^q-v,u)`. Thus `Phi_r` is
a polynomial automorphism, (2.3) holds, and `J(f_r,g_r)=1`.

On `P_s=a`, take

\[
 T=P_{s+1}.
\]

The inverse recurrence is

\[
 P_{i-1}=P_i^{q_i}-P_{i+1}.                         \tag{2.9}
\]

It expresses every `P_i`, hence `x,y`, as a polynomial in `T`. At the
unique point `T=infinity`, let `n_i` be the pole order of `P_i`. Then

\[
 n_{s-1}=1,
 \qquad
 n_i=\prod_{j=i+1}^{s-1}q_j\quad(0\le i\le s-2),   \tag{2.10}
\]

because (2.9) gives `n_{i-1}=q_i n_i>n_{i+1}` for
`1 <= i <= s-1`; the seed is `n_{s-1}=1`. In particular,

\[
 n_0=\prod_{j=1}^{s-1}q_j
     =7\cdot3\cdot2^{r+1}
     =42\cdot2^r.                                  \tag{2.11}
\]

The relations

\[
 P_{i+1}=P_i^{q_i}-P_{i-1},
 \qquad q_i n_i=n_{i-1}>n_{i+1}
 \quad(1\le i\le s-1),                            \tag{2.12}
\]

are an actual approximate-root chain. Its running gcd sequence is

\[
 \gcd(n_0,\ldots,n_i)=n_i,
 \qquad \frac{n_{i-1}}{n_i}=q_i.                   \tag{2.13}
\]

By the standard approximate-root/Puiseux correspondence, (2.12)--(2.13)
is exactly the characteristic-index sequence (2.2). Equivalently, the
completion of the fiber is
`C((T^{-1}))`; `x=P_0(T)` has pole order `n_0`, while
`T=P_{s+1}(x,y)`, so `x,y` generate the full completion. Therefore the
minimal Puiseux denominator over `x` is `n_0`, proving (2.1).

Finally, direct degree induction in (2.5) gives

\[
 \deg f_r=\kappa_r,
 \qquad \deg g_r=2\kappa_r.                        \tag{2.14}
\]

Thus this family pays for every new characteristic factor by increasing
the polynomial degree, not the topological degree. \(\square\)

### Boundary identity in the family

Let `F_r,G_r` be the homogenizations. From (2.3), (2.8), and (2.14),

\[
 (F_r)_X(G_r)_Y-(F_r)_Y(G_r)_X
 =Z^{\deg f_r+\deg g_r-2}
 =Z^{3\kappa_r-2}.                                 \tag{2.15}
\]

Hence the family satisfies the **entire** pure-boundary identity, not only
its leading-form shadow. It simultaneously satisfies every successive
Puiseux coefficient cancellation forced by that identity. Nevertheless
the length in (2.2) and the product (2.1) are unbounded.

## 3. Why the three proposed tools do not prove residue-A K2C

### 3.1 Pure-boundary Jacobian

The identity

\[
 F_XG_Y-F_YG_X=jZ^{d+e-2}                           \tag{3.1}
\]

is an exact compatibility system at the boundary. It contains no
degree-independent stopping index. In Theorem 2.1, every new approximate
root increases `(d,e)` from `(kappa,2kappa)` and increases the required
vanishing order `d+e-2` with it. Equation (2.15) shows that the new
coefficient equations remain soluble for arbitrarily long chains.

Thus (3.1) cannot imply

\[
 \operatorname{td}\le T\Longrightarrow\kappa_i\le K(T)              \tag{3.2}
\]

on all Keller maps: (3.2) is **FALSE** by Theorem 2.1.

### 3.2 Polynomial degree and approximate roots

For a fixed polynomial fiber of degree `d_f`, a pole of `x` on its
normalization has order at most `d_f`: the total pole divisor of `x=X/Z`
has degree at most the intersection number with `Z=0`, namely `d_f`.
The primitive Puiseux denominator divides that pole order. Therefore

\[
 \kappa_i\le d_f,                                   \tag{3.3}
\]

and, since every characteristic index is at least `2`,

\[
 \#\{\text{characteristic pairs on the branch}\}
 \le \lfloor\log_2 d_f\rfloor.                    \tag{3.4}
\]

These are **PROVED fixed-degree bounds**. They do not answer K2C because
`td` does not bound `d_f`. Theorem 2.1 has equality
`kappa_r=d_f` while `td=1`.

In the counterexample normal form, type `(alpha,beta)` fixes only the
reduced degree ratio. It does not bound the common degree scale `B`.
Lemma 2.2 spends that scale on the inserted carriers. KJN bounds `td`, not
`B`.

### 3.3 Semigroup arithmetic

The chain (2.10)--(2.13) is a polynomial-origin value-semigroup/
approximate-root realization of arbitrarily many gcd drops. Hence
divisibility, strict gcd descent, and semigroup consistency do not bound
their number at fixed `td`.

For residue A there is an additional category obstruction: its generic
fiber is multi-place. The one-place Abhyankar--Moh inequality does not
apply to an individual residue-A `P_i` branch; `AM-CHECK.md` verifies that
the banked `P_i` data lies on the local, finite-center side. The applicable
per-branch gcd arithmetic is precisely the arithmetic which permits the
`l=0`, `nu=2` descent. No banked conductor or genus quantity bounded by
`td` prices the added factors.

## 4. Exact scope: what has and has not been realized

Theorem 2.1 realizes all of the following with actual polynomials:

\[
 J=1,
 \quad \operatorname{td}\text{ fixed},
 \quad \kappa=42\cdot2^r,
 \quad r\to\infty,
\]

and it realizes the repeated factor `nu=2` through genuine approximate
roots. It therefore removes the proposed general polynomial-origin
obstruction.

It does **not** realize the FORMAL residue-A equalities

\[
 (\alpha,\beta)=(2,3),\quad
 (a_P,b_P,\nu_P)=(1,1,2)\text{ at two poles},\quad
 w=2,\quad \operatorname{td}=6,                    \tag{4.1}
\]

or the fixed merge datum `(bar-kappa,D/i,rho)=(5,3,1/2)`. The Hénon
family is an automorphism, has one pole, and has reduced type `(1,2)`.
After lexicographic minimization under polynomial equivalence it becomes
the coordinate pair.

Accordingly:

\[
 \boxed{
 \begin{array}{l}
 \text{actual residue-A realization of Lemma 2.2: UNKNOWN;}\\
 \text{polynomial-origin prohibition from (3.1), AM, and semigroups:
 FALSE in general;}\\
 \text{prohibition in the degree-minimal nonautomorphic residue-A sector:
 CONJECTURE.}
 \end{array}}
                                                               \tag{4.2}
\]

Claiming the first line impossible would be a new exclusion theorem for
the `td=6` noninvertible Keller sector. None of the three tools supplies
that theorem.

## 5. Minimal remaining lemma and implication chain

The unrestricted K2C statement must be retired or restricted. The smallest
well-typed replacement is:

> **CONJECTURE UCD-A-min.** There is an integer `K_A` such that every
> lexicographically degree-minimal, nonautomorphic Keller pair in Sigray
> normal form of type `(2,3)` with the residue-A `td=6` pole inventory has
>
> \[
>   \max_i\kappa_i\le K_A.                          \tag{5.1}
> \]

The corresponding general bridge would be:

> **CONJECTURE K2C-min.** For fixed coprime integers
> `2 <= alpha < beta` and fixed `T`, there is an integer
> `K(alpha,beta,T)` such that every lexicographically degree-minimal,
> nonautomorphic Sigray-normalized Keller pair of type `(alpha,beta)` and
> `td <= T` satisfies
>
> \[
>   \max_i\kappa_i\le K(\alpha,\beta,T).            \tag{5.2}
> \]

The degree-minimal clause removes the exact re-embedding phenomenon of
Theorem 2.1: polynomial automorphisms can store arbitrarily long removable
approximate-root chains at fixed `td`. The nonautomorphic/type/residue
clauses are necessary because the unrestricted assertion is already false.

An equivalent direct target for G2 is a uniform bound on the number of
case-(II) `l=0` characteristic factors between the pole entry and its
merge. A bound on the size of each factor is insufficient; repeated `2`
already diverges.

If UCD-A-min were proved, then the depth consequence would be exact:

\[
 \prod_j\nu_j\le\kappa_i\le K_A,
 \qquad \nu_j\ge2
 \Longrightarrow
 d_{\rm sh}\le\lfloor\log_2K_A\rfloor.            \tag{5.3}
\]

The only honest unification chain is therefore conditional:

\[
 \begin{array}{c}
 \mathrm{KJN}(C)
 \Longrightarrow \operatorname{td}\le C\alpha\beta
 \qquad\text{(**EXACT**)},\\[2mm]
 \mathrm{KJN}(C)+\textbf{CONJECTURE K2C-min}
 \Longrightarrow \mathrm{UCD}
 \Longrightarrow d_{\rm sh}\le\lfloor\log_2K\rfloor
 \Longrightarrow \mathrm{G2},\\[2mm]
 \mathrm{KJN}(C)\Longrightarrow\mathrm{G5}.
 \end{array}                                       \tag{5.4}
\]

Without **CONJECTURE K2C-min/UCD-A-min**, the middle line does not follow.
Theorem 2.1 proves that no argument using only bounded `td`, polynomial
origin, (3.1), and ordinary approximate-root/semigroup axioms can supply
it.

\[
 \boxed{\textbf{HEADLINE: G2 AND G5 REMAIN SEPARATE AT THE KELLER TIER.}}
\]
