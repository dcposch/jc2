# TD12-FORMAL-CASCADE-RANK/v1 — exact reduced-operator rank

Date: 2026-08-29  
Producer: Sol 5.6, desk-scale provisional descendant  
Frozen Git basis: `76c746f698103d20019bfeb72654a361ccc5371d`

## 0. Disposition

```text
LINEAR_RANK_CLOSED
NO_FORMAL_CASCADE_KILL_IN_WINDOW
NOT_A_PAIRREF
```

After fixing an explicit finite polynomial domain and target, the reduced
`Z` operator is injective.  Its nominal cokernel has dimension equal to the
number of distinct nonzero `t`-roots of the reduced top:

```text
B route:        2,
sibling route:  3.
```

The single leading-degree resonance found by Fable is real, but it is not the
whole cokernel.  It lowers the cokernel of a specially truncated **sharp
degree target** by one only when the chosen domain cap ends exactly at the
resonant monomial.  At the conditional natural top-degree cap this gives

```text
B:        1 for s=1..8, then 2 for s=9..24;
sibling:  2 for s=1..4, then 3 for s=5..16.
```

Thus there is no shared, cap-uniform one-dimensional compatibility count.
The cap-uniform count for the declared nominal target is route-specific
`2` versus `3`.

More importantly, operator cokernel does not imply that the nonlinear lower
term `K_s` has a nonzero cokernel class.  On the formal type-`(2,3)` jet
envelope, the truncated binomial response `g=c_g f^(3/2)` is polynomial
coefficient by coefficient through every homogeneous order `s<=i` and
solves all those Keller rows.  Hence order two is not a genuine formal
compatibility bite; none is forced through the depth-24/depth-16 windows
under the explicit rider `i>=depth`.  No first nontrivial order is proved by
the frozen data.

This is a rank theorem for a formal jet envelope.  It supplies no exact
pair, completion, source coefficient, non-top child vector, gate verdict,
landing, exclusion, software migration, or JC2 consequence.

## 1. Custody and exact perimeter

Only the following two sealed reports were consumed, including the source
formulas and route data already pinned inside them:

```text
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84
  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
  body 33565 / d5b099c2627b86d11345b8283080fcd746c1a0352cc8058182951710e5065feb

876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab
  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
  body 14248 / 45d79d5ed605e7a17a121971a747c10b1f4b30d4b9db805d2c090f3528f0c1dd
```

No new source interpretation is introduced.  In particular, this report
uses the reviewed chart convolution, `D_F=nu*i`, the two weight residues,
the root-floor ladder, and the Sol repair `D_g/D_F=3/2`, `r=3i/2` on an
actual type-`(2,3)` occurrence.  B and sibling remain alternative route
states with separate hypothetical source packets.

New exact standard-library control:

```text
ea911af2906b71802507bd02a5aab728645e823e2148d04b8a35e44fb5fca261
  cases/td12_formal_cascade_rank_v1_20260829/check.py

cd3288b654c831a2d51571f9a89314b1ddd639b7654d8faaedd4837d6dbc7b36
  cases/td12_formal_cascade_rank_v1_20260829/README.md
```

Ordinary and `-O` runs are byte-identical (`648` bytes), stdout SHA-256

```text
35f6f1719154755b82c58d13db8fdc9045152f8f780053cca59102d6b9e6f008.
```

They take about 2.7 seconds each on the local desk machine.  They are tiny
rational controls, not exhaustive evidence or a substitute for the proof.
No CAS, web, AWS, or heavy computation was used.

## 2. Frozen route parameters, weights, floors and caps

Use `t=eta^nu` and write the monic reduced top as

```text
P(t)=prod_(j=1)^q (t-a_j)^(m_j),       M=sum_j m_j.
```

The two cases are separate:

```text
B:  nu=25, (m_1,m_2)=(2,1),       M=3, q=2,
    P=(t-A)^2(t-B),                A,B nonzero and distinct;

S:  nu=17, (m_1,m_2,m_3)=(2,1,1), M=4, q=3,
    P=(t-A)^2(t-B_+)(t-B_-),       all three nonzero and distinct.
```

Fix an order `1<=s<nu` and an index `i>=s`.  The latter is an explicit
formal-envelope hypothesis; it covers a depth window only when
`i>=depth`.  Let `e_s` be the least residue in `{1,...,nu-1}` satisfying

```text
e_s == -M*s (mod nu).
```

Because `gcd(M,nu)=1`, it is never zero in this range.  These are exactly the
reviewed residues

```text
B: e_s == 22s (mod 25),
S: e_s == 13s (mod 17).
```

Freeze the root floor

```text
F_s(t)=prod_j (t-a_j)^(m_j*i-s).
```

For an arbitrary declared cap `N>=0`, the f-side/reduced-Z domain is

```text
D_(s,N) = { eta^e_s F_s(t) R(t) : R in C[t], deg R<=N }.
```

It has dimension `N+1`.  This is a formal domain declaration, not a claim
that source coefficients with this cap exist.

If one additionally imposes the conditional “natural” top-degree cap
`deg_eta Z<=deg_eta P(eta^nu)^i=M*nu*i`, then

```text
e_s + nu(deg F_s+N) <= M*nu*i,
deg F_s = M*i-q*s,
```

and, since `e_s>0`, the largest allowed cap is

```text
N_nat(s)=q*s-1.                                      (2.1)
```

The source packet does not currently pin this as the actual lower-piece cap;
it is analyzed because it is the cap used by Fable's dimension heuristic.

## 3. Exact root-floor factorization

The reviewed reduced equation is

```text
c_g P^(r-1) L_s(Z_s) = -K_s,

L_s(Z) = D_F P Z' - i(D_F-s)P' Z,       D_F=nu*i,
```

where primes before the reduction mean `d/deta`.  Define

```text
C(t)=gcd(P,P')=prod_j(t-a_j)^(m_j-1),
S(t)=rad(P)=P/C=prod_j(t-a_j),
J(t)=P'/C,
U_s(t)=S*F_s'/F_s
      =sum_j (m_j*i-s) S/(t-a_j).
```

Here the displayed derivatives of `P,F_s,S` are `d/dt`.  Substituting
`Z=eta^e_s F_s R` and differentiating `t=eta^nu` gives exactly

```text
L_s(Z)
 = nu*i * eta^(e_s-1) F_s C * T_s(R),                 (3.1)

T_s(R)
 = nu*t*S R'
   + [e_s*S + nu*t*U_s - (nu*i-s)t*J]R.               (3.2)
```

Thus the full output floor, before the quotient polynomial, is

```text
eta^(e_s-1) P^(r-1) F_s C.
```

At a `t`-root of multiplicity `m_j` its exponent is
`m_j(r+i)-s-1`, exactly the floor obtained by adding the prefactor.

The declared nominal target is therefore

```text
Y_(s,N) = eta^(e_s-1) P^(r-1) F_s C * C[t]_(<=N+q).   (3.3)
```

Nonzero scalar factors `c_g*nu*i` do not affect rank.  Equation (3.3) is an
explicit target definition; replacing it by an unknown “natural target” is
not allowed in the count.

## 4. Rank, resonance and cokernel theorem

Set

```text
h_s=(M*s+e_s)/nu=ceil(M*s/nu),
n_*(s)=q*s-h_s.                                        (4.1)
```

The coefficient of `t^(n+q)` in `T_s(t^n)` is

```text
nu*n + e_s + M*s - nu*q*s = nu(n-n_*).                (4.2)
```

So there is exactly one leading-degree resonance, at the integer monomial
`t^n_*`.

### Theorem 4.1 — injectivity

`T_s:C[t]->C[t]` is injective for `1<=s<nu`.

Indeed, `T_s(R)=0` is equivalent through (3.1) to `L_s(Z)=0`.  Its nonzero
formal solution is

```text
Z=constant*P(eta^nu)^(i-s/nu).
```

Both route tops have a simple nonzero `t`-root, hence simple eta-roots there.
Since `s/nu` is not an integer, this is not a polynomial.  Thus the declared
polynomial domain has zero kernel.

### Theorem 4.2 — nominal finite-cap and intrinsic cokernel

For every `N>=0`, (3.2) maps `C[t]_(<=N)` into
`C[t]_(<=N+q)`.  By injectivity its rank is `N+1`; the nominal target has
dimension `N+q+1`.  Therefore

```text
dim coker(T_s : C[t]_(<=N) -> C[t]_(<=N+q)) = q.       (4.3)
```

For `N>n_*`, adjoining the next source monomial and the next highest target
monomial adds one pivot by (4.2).  The quotient stabilizes.  Hence on the
full polynomial ring

```text
dim C[t]/T_s(C[t]) = q.                                (4.4)
```

Consequently the intrinsic/nominal count is exactly two for B and exactly
three for the sibling.  A leading resonance is not synonymous with a
one-dimensional cokernel.

### Theorem 4.3 — sharp degree target

Let `d_s(N)` be the largest degree actually attained by `T_s(R)` for
`deg R<=N`, and take the alternative sharp ambient target
`C[t]_(<=d_s(N))`.  Equation (4.2), and the nonzero leading coefficient of
`T_s(t^(n_*-1))`, give

```text
d_s(N)=N+q-1   if N=n_*,
d_s(N)=N+q     otherwise;

sharp cokernel=q-1 if N=n_*,
sharp cokernel=q   otherwise.                           (4.5)
```

This one-unit drop is a cap-endpoint artifact: if the cap continues beyond
the resonant monomial, higher source monomials restore the nominal top
degree.

At the conditional natural cap (2.1), `N_nat=n_*` exactly when `h_s=1`,
equivalently `M*s<nu`.  Therefore:

```text
B, M=3,nu=25,q=2:
  endpoint resonance s=1..8;
  natural sharp cokernel 1 for s=1..8, 2 for s=9..24.

S, M=4,nu=17,q=3:
  endpoint resonance s=1..4;
  natural sharp cokernel 2 for s=1..4, 3 for s=5..16.
```

This is the exact correction to the proposed common “one infinity
cokernel” count.

## 5. Does a cokernel condition actually bite `K_s`?

No such conclusion follows from rank alone.  The target of (4.3) contains
many polynomials that never arise as the structured lower-order cross term
`K_s`.  The frozen source data supply no numerical lower jets with which to
evaluate its cokernel class.

There is a stronger formal negative result on the actual type-`(2,3)` ratio.
Fix any depth `d<=i` below the RHS landing and arbitrary pieces

```text
P_0=P^i,
P_s in eta^e_s F_s C[t]                       (1<=s<=d),
```

with the declared top-degree caps.  In a dummy grade variable `z`, set

```text
f_hat=P^i + sum_(s=1)^d z^s P_s,

g_hat=c_g P^r *
      (1 + sum_(s=1)^d z^s P_s/P^i)^(r/i)
      mod z^(d+1),

r/i=3/2.                                               (5.1)
```

Every coefficient of `g_hat` is a polynomial.  A monomial at total grade
`s=s_1+...+s_k` has, at a root of multiplicity `m`, exponent

```text
m(r-i*k) + sum_j(m*i-s_j) = m*r-s >=0.                 (5.2)
```

After removing the matched linear response and the common factor
`P^(r-i)`, the corresponding `Z_s` exponent is `m*i-s>=0`.  Weight residues
add to `e_s`, and the top-degree caps are preserved: before and after the
common-factor removal the degree bounds are those of `P^r` and `P^i`,
respectively.

Since `g_hat` is a truncated formal function of `f_hat`, its chart Jacobian
with `f_hat` vanishes coefficientwise.  Restoring the omitted top
`x`-monomials does not change this: `D_g=(3/2)D_F`, so the top powers align
with the same formal relation.  Hence every homogeneous equation
`E_s` for `s<=d` is solved, and its structured `K_s` lies in the image of
the reduced operator.  At order two the explicit correction is

```text
Z_2=(3/8) P_1^2/P^i,                                  (5.3)
```

whose root floor is exactly `F_2` because `F_1^2/P^i=F_2` (including the
weight carry in `eta`).  The checker verifies (5.3) on one nonzero exact
sample in each route.

This proves:

- `s=1` is vacuous (`K_1=0`);
- `s=2` is not a universal formal bite;
- indeed no homogeneous row through `s<=i` constrains the arbitrary f-side
  formal jet envelope;
- under `i>=24`, neither the B depth-24 nor sibling depth-16 window has a
  formal Keller compatibility obstruction of this kind.

It does **not** prove that arbitrary jets extend to a polynomial `g`, an
exact pair, or even to orders beyond the declared truncation.  At `s=i+1`
the simple-root divisibility proof (5.2) no longer follows from these floors;
the inhomogeneous RHS lands only at
`s*=D_F+D_g-kbar_F`, outside both gate windows.  The frozen data therefore
prove no first genuine nontrivial order.  They identify only the next places
where new source information could matter.

## 6. Exact controls

The checker uses one rational distinct-nonzero root set in each route, the
actual `(nu,M,q)` values, `i=30`, and twelve tiny matrix cases concentrated
at the resonance/natural-cap boundaries.  It verifies:

```text
root-floor identity (3.1)--(3.2),
rank=N+1,
nominal cokernel=q,
sharp formula (4.5),
the two complete natural-cap tables from their closed formulas,
one exact nonzero order-two binomial solve per route.
```

The output table hashes are

```text
B  1d52051fec7bfbdcb76f6a2326640567a6dedc7bfe6a3ea929cab2beb757d69c
S  f1074d459ee4bc4414e15ed491aba7db1ad4cab1b926216814faa5134a3b0c03
```

These controls sample the theorem; they do not establish it by enumeration.

## 7. Maximum safe descendant use

Promotable after review:

1. the explicit root-floor quotient operator (3.2);
2. injectivity and nominal/intrinsic cokernel `q`;
3. the cap-endpoint resonance formula (4.5) and the B/sibling tables;
4. the formal binomial-lift lemma through `s<=i`.

Not licensed:

1. identifying `Y_(s,N)` with the unknown source `K_s` target without a
   route packet;
2. a one-dimensional cascade, an order-two kill, or any depth-gate verdict;
3. treating the formal binomial lift as a polynomial `g` or a `PairRef`;
4. building a standalone source recurrence engine or launching AWS/CAS.

The next concrete source lane remains route-separated PairRef/completion
construction.  A purely formal successor, if desired, is the beyond-floor
`s=i+1` divisibility audit, but it does not outrank obtaining actual source
jets.

## 8. Scope firewall

This report is not an exact pair, source realization, completion, germ,
landing, gate, exclusion, degree bound, counterexample, or JC2 result.  It
does not link B and sibling source states.  No canonical/source/LL-1 file was
edited; no commit or push was made.

## Seal

- Body length: `13264` bytes (all bytes before this heading).
- Body SHA-256: `805e551279f47ff7cecc235f906a940b80ad384e1db05178f6792240448ee853`.
- Frozen Git basis: `76c746f698103d20019bfeb72654a361ccc5371d`.
