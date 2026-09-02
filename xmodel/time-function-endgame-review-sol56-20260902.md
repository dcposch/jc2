# Hostile review: TIME-FUNCTION ENDGAME

**Lane/date:** `TIME-FUNCTION-ENDGAME`, hostile review, 2026-09-02. **Scope:**
nine items, `D=105`, 15 star rows plus two extensions, three controls, and the
DELTA-DENOM measurement. No ledger edit; no `jc2-lean`.

Citations: `TF`, `I17`, and `D1` denote the three frozen reports; named drivers
are under `box/tfe-drivers-20260902/` unless called frozen.

## 0. Executive verdict

BOTTOM-ODE, STAR-SIMPLE, STAR-SUM, and STAR-ABC survive reproof. The full
flagship does not: local completion is not global polynomial interpolation;
STAR-RESIDUE has one bad normalization; STAR-EIGEN is unsupported at `A=1`; and the
order-two driver sends its source to the wrong exponents. The restricted map
has three positive resonances, not `mu Z_{>0}`, and omits visible outer-root
degrees. The 15 decisions and two extensions pass, but not 15 explicit points.
The `D=105` counts reconcile; `k=20,N=6` is permitted, not attained. Full typed
verdict: section 13.

## 1. Custody and reproduction

The mandatory hash gate was run before opening the inputs. All five hashes
matched exactly:

```text
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  d1-subtree-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  bottomode.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  d1floor.py
```

Live prefixes match `TF:39-42`; live/frozen `bottomode.py` and `d1floor.py`
are identical. One-core exact CAS reproduced both order logs; an independent
SymPy calculation rebuilt the matrix/source. Controls 1, 3, 4 and every star
ideal were rerun.

## 2. From JAC-FIBRE to the exact local identity

### 2.1 What JAC-FIBRE really gives

Let `g(x,tau_i(x)) = c_2` on a simple branch of a generic fibre. Then

```text
g_x + g_y tau_i' = 0,
d/dx f(x,tau_i) = f_x + f_y tau_i' = (f_x g_y - f_y g_x)/g_y = c/g_y.
```

Thus, for a pre-existing Keller pair,

```text
f(x,tau_i(x)) = c integral dx/g_y(x,tau_i(x)) + a_i.
```

This is the exact series identity behind the promoted valuation statement
`I17:14-17` and `D1:203-214`. Since `g-c_2` is monic with `n` distinct generic
roots and `deg_y f=m<n`, `f` is indeed the unique degree-`<n` Lagrange
interpolant through these `n` values. That global programme is stated at
`I17:94-100`.

Now put

```text
x=t^(-1),                 y=w(t)+pi t^delta,
F(t,pi)=f(x,y),           G(t,pi)=g(x,y).
```

The change-of-variables determinant is

```text
det d(x,y)/d(t,pi) = -t^(delta-2),
```

so the full polynomial Jacobian, not merely its valuation, gives

```text
F_t G_pi - F_pi G_t = -c t^(delta-2).                         (2.1)
```

Write `F=t^lambda_f Phi`, `G=t^lambda_g Gamma`. Without assuming order
matching, the exact normalized equation is

```text
(lambda_f Phi+t Phi_t) Gamma_pi
 -(lambda_g Gamma+t Gamma_t) Phi_pi
 = -c t^[delta-1-(lambda_f+lambda_g)].                        (2.2)
```

At a bottom disc, D1-PIN supplies
`lambda_f+lambda_g=delta_1-1`; see `D1:328-350` and the independent radius
formulas at `D1:143-158`. Therefore the exponent on the right of (2.2) is zero,
and `TF:202-213` is exact coefficient by coefficient:

```text
(lambda_f Phi+t Phi_t) Gamma_pi
 -(lambda_g Gamma+t Gamma_t) Phi_pi = -c.                     (LOCAL-KELLER)
```

Thus the one-variable Keller equation is the leading bracket in `pi`, while
the untruncated identity is exact for an actual Keller pair.

### 2.2 Why item 1 is still a GAP

`TF:234-238` says that coefficients polynomial in `x` are the same as
`Phi,Gamma in C[[t^eta]][pi]`, and concludes that all coefficient equations are
the conjunction of interpolation conditions (i)--(ii). That identification is
false. The completed Puiseux ring permits arbitrary infinite fractional-power
tails. It does not say that the Lagrange coefficients lie in `C[x]`; it does not
glue constants `a_i` under monodromy; and it does not enforce compatibility
among all `n=105` branches or among the candidate bottom discs. The report's
own `TF:715-718` correctly concedes that a local solution is not attainment of
a Keller pair.

There is a second overstatement at `TF:215-218`: bare order mismatch need not
make (2.1) unsatisfiable. If the nominal leading bracket is earlier than the
Jacobian order, its leading coefficient can vanish and the constant Jacobian
can occur later. `TF:220-222` invokes exactly that sub-leading behaviour at
higher discs. At `D_1` there is no damage because D1-PIN independently proves
the equality; it should not be re-derived from an order comparison that has
not excluded cancellation.

**Line repair for `TF:234-238`:**

> For a pre-existing Keller polynomial pair, LOCAL-KELLER is an exact necessary
> identity in the completed bottom-disc ring and gives a coefficient equation
> at every exponent. Membership in that completed ring is only local formal
> regularity/no-log. Polynomiality of the global Lagrange interpolant in `x`,
> compatibility of the `n` branch constants, and inter-disc gluing remain
> separate conditions.

Verdict: **GAP** for the charged equivalence; **CONFIRMED/CAN** for the exact
necessary coordinate identity.

## 3. BOTTOM-ODE and the normalization of `kappa`

At order zero put `Phi_0=p_f`, `Gamma_0=p_g`. LOCAL-KELLER gives

```text
lambda_f p_f p_g' - lambda_g p_g p_f' = -c.                  (3.1)
```

Moh's level-one proportionality is
`lambda_f/lambda_g=m/n=d/e`, while Def. 5.1(1) gives

```text
deg p_g = a_1=e V_2,        deg p_f=b_1=d V_2;
```

see `D1:136-155`. Multiplying (3.1) by `e/lambda_g` yields

```text
d p_f p_g' - e p_g p_f' = kappa,      kappa=-e c/lambda_g.  (3.2)
```

Since

```text
lambda_g(delta_1) = -e(1-delta_1)/(d+e),
q = (1-delta_1)de/(d+e),
```

one obtains exactly

```text
kappa = c(d+e)/(1-delta_1) = c d e/q != 0.                  (3.3)
```

This confirms the sign, degrees, and all three correct expressions in
`TF:242-253`.

For the mandatory control `(f,g)=(y,x+y^k)`, with the convention
`[f,g]=f_xg_y-f_yg_x`,

```text
c=-1, delta_1=-1/k, (d,e,V_2)=(1,k,1), q=1,
p_f=pi, p_g=1+pi^k,
p_f p_g' - k p_g p_f' = -k = cde/q.
```

This independently confirms `TF:259-262`; controls `k=2,...,7` reproduce it.

The delivered `bottomode.py` reproduces the selected system. Its nondegenerate
component is

```text
p_g=pi^3+p_1 pi,
p_f=q_2(pi^2+(2/3)p_1),
kappa=(4/3)p_1^2 q_2,       p_1 q_2 != 0.
```

The other component has `q_2=0`, violates `deg p_f=2`, and has `kappa=0`.
The one-orbit conclusion follows from this normal form; the nominal dimension
routine at `bottomode.py:63-78` is only `pass`.

Verdict: **CONFIRMED — CAN promote.**

## 4. STAR-SIMPLE, STAR-RESIDUE, and STAR-SUM

### 4.1 Simplicity and coprimality

If `p_g(z)=p_g'(z)=0`, equation (3.2) gives `kappa=0`. The symmetric argument
handles a repeated root of `p_f`, and a common root also kills both terms.
Thus `p_f` and `p_g` are squarefree and coprime. `TF:288-299` is complete.
In the Puiseux interpretation, the `f` roots in `D_1` therefore have distinct
`t^delta_1` coefficients, which is a genuine strengthening of the promoted
`g`-star statement.

Verdict STAR-SIMPLE: **CONFIRMED — CAN promote.**

### 4.2 Residue identity and a concrete arithmetic error

At a root `c_i` of `p_g`, (3.2) gives

```text
p_f(c_i) p_g'(c_i) = kappa/d.                                (4.1)
```

The core of `TF:301-306` is correct. Its last expression on line 303 is not:

```text
kappa/d = c(d+e)/[d(1-delta_1)] = c e/q,
```

not `c e/(1-delta_1)`. The report's own normalization is a countercheck:
`c=1/15`, `(d,e)=(2,3)`, `delta_1=3/4`, `kappa=4/3` at `TF:281-282`, so
`kappa/d=2/3`, while the printed expression is `4/5`.

**Line repair for `TF:303`:** replace `c e/(1-delta_1)` by
`c(d+e)/(d(1-delta_1)) = c e/q`.

Verdict STAR-RESIDUE: **GAP as printed; core identity CONFIRMED. CAN promote
after the one-line correction.** No later STAR-SUM calculation uses the bad
expression.

### 4.3 The sum identities

Because `deg p_f<deg p_g` and `p_g` is squarefree, partial fractions and (4.1)
give

```text
p_f(pi)/p_g(pi)
 = sum_i [p_f(c_i)/p_g'(c_i)]/(pi-c_i)
 = (kappa/d) sum_{k>=0} pi^(-k-1)
       sum_i c_i^k/p_g'(c_i)^2.                              (4.2)
```

The left side first appears at power `pi^[-(a_1-b_1)]`. Hence

```text
sum_i c_i^k/p_g'(c_i)^2 = 0,
      0 <= k <= a_1-b_1-2=(e-d)V_2-2,

sum_i c_i^(a_1-b_1-1)/p_g'(c_i)^2
      = (d/kappa)(lc p_f/lc p_g) != 0.                       (4.3)
```

The first range is empty when its upper endpoint is negative. This exactly
confirms `TF:394-410` and the user's stated range.

Verdict STAR-SUM: **CONFIRMED — CAN promote.**

## 5. STAR-ABC: degree, squarefreeness, and passport

Use `Q=p_f`, `P=p_g`, so `deg Q=b=dV`, `deg P=a=eV`, and

```text
H=d QP'-e PQ'=kappa.                                         (5.1)
```

Choose `rho=(lc Q)^e/(lc P)^d`, so the leading degree `deV` cancels in

```text
C=Q^e-rho P^d,
```

and put `gamma=deg C<deV`. Since `P,Q` are coprime, `C` is not zero. Direct
differentiation gives the load-bearing identity

```text
C'P-dCP' = -Q^(e-1) H.                                      (5.2)
```

The leading coefficient on the left is
`lc(C)lc(P)(gamma-deV)`, which is nonzero. Therefore

```text
gamma+a-1=b(e-1),
gamma=V(de-d-e)+1.                                           (5.3)
```

This handles the vanished degree-`deV` leader. If `C(z)=C'(z)=0`, (5.2) forces `Q(z)=0`; then
`C(z)=-rho P(z)^d=0`, contradicting coprimality. Thus `C` is squarefree.
At a root of `P`, `C=Q^e` is nonzero; at a root of `Q`, `C=-rho P^d` is
nonzero. Consequently `P,Q,C` are pairwise coprime and all three are
squarefree, as required by the user's audit.

For Mason--Stothers take `A=Q^e`, `B=-rho P^d`, `A+B=C`. Then

```text
deg rad(ABC)=deg(PQC)=a+b+gamma=deV+1,
max(deg A,deg B,deg C)=deV=deg rad(ABC)-1.                    (5.4)
```

So the bound is attained with equality. Conversely, starting with the degree
in (5.3), equation (5.2) gives

```text
deg[Q^(e-1)H] <= gamma+a-1=b(e-1),
```

hence `deg H<=0`. It cannot be zero as a polynomial: `H=0` would make
`Q^e/P^d` constant, impossible for nonconstant coprime `P,Q`. Thus
`H=kappa in C*`. This direct argument is the safest repair for the compressed
“equality of degrees forces” sentence at `TF:449-453`.

Finally set

```text
R=Q^e/P^d,         deg R=deV,        R(infinity)=rho.
```

The `dV` simple roots of `Q` have local degree `e`, giving
`[e^(dV)]` over zero. The `eV` simple roots of `P` have local degree `d`,
giving `[d^(eV)]` over infinity. The `gamma` roots of `C` are simple and hence
unramified over `rho`. At the source point infinity,

```text
R-rho=C/P^d ~ s^[deV-gamma]
              =s^[(d+e)V-1],       s=1/pi,
```

so the third profile is

```text
[(d+e)V-1, 1^gamma],       gamma=V(de-d-e)+1.                 (5.5)
```

Moreover

```text
R'=-kappa Q^(e-1)/P^(d+1),
```

so there are no other branch values. Riemann--Hurwitz closes:

```text
dV(e-1)+eV(d-1)+[(d+e)V-2]=2deV-2.
```

After rescaling `rho` to 1 this is a three-point Belyi map with exactly the
charged passport. `TF:456` prints an erroneous extra factor `e` in `R'`; the
correct derivative is the display above. This harmless scalar does not change
the zeros or passport. With that repair and the explicit converse step,
`TF:431-459` is correct.

Verdict: **CONFIRMED — CAN promote.**

## 6. STAR-EIGEN: the `A=1` gap

The semi-invariance idea at `TF:536-547` can be repaired. Choose a common
Puiseux denominator and let `H` stabilize the head `w`. For `h in H`, define
the scalar by which it moves the disc coordinate through

```text
xi(h)=h(t^delta_1)/t^delta_1,
A=|xi(H)|.
```

Comparing leading terms in `f(w+pi t^delta_1)` and
`g(w+pi t^delta_1)` proves that `p_f` and `p_g` are semi-invariants, possibly
with different eigencharacters. For a generator of the cyclic image, their
eigenvalues are `xi^b_1` and `xi^a_1`. The nonzero Wronskian scales by
`xi^(a_1+b_1-1)`, so

```text
A | a_1+b_1-1=(d+e)V_2-1.                                  (6.1)
```

For `A>1`, each polynomial has support in one residue class modulo `A`.
Evaluation of the Wronskian at `pi=0` then forces exactly one pattern:

```text
(a_1,b_1)=(1,0) mod A, with pi|p_g and pi not|p_f; or
(a_1,b_1)=(0,1) mod A, with pi|p_f simply and pi not|p_g.    (6.2)
```

For `A=1`, however, all residue classes coincide and the two Wronskian terms
can both contribute at zero. No root at zero is forced. The displayed theorem
`TF:541-546` nevertheless includes the bracketed root assertions at `A=1`.
Its own exact `(d,e,V)=(3,5,1)` row has `A=1` (`TF:421-423`) and the witness at
`TF:513` has

```text
p_g(0)=-10/27,       p_f(0)=-1/3,
```

so neither root alternative follows from BOTTOM-ODE plus `A=1`; its Wronskian
is `35/27`. This is an abstract star, not an attained Keller disc, so it
refutes the advertised algebraic inference/test rather than the possibility
that extra geometry forces a root. `starcheck.py:89-94` checks only vacuous
congruences modulo 1, not the bracketed root claim.

**Line repair for `TF:541-546`:** retain (6.1) for every `A`; state (6.2) only
for `A>1`; state explicitly that `A=1` imposes no zero at the chosen origin.
Also replace the undefined `A'` at `TF:537` by the declared common denominator
and the map `xi` above.

Verdict: **GAP as a geometric theorem; its stated `A=1` algebraic inference is
REFUTED — CANNOT promote as displayed.** The repaired divisibility and `A>1`
dichotomy **CAN**. `OPEN[EIGEN-A]` at `TF:700-704` remains separate.

## 7. The `D = 105` candidate and the two census object types

The selected arithmetic row recomputes exactly:

```text
n=105, m=70, K=35, (d,e)=(2,3), s=3,
M=(-70,-63,103), d-chain=(105,35,7,1), V=(1,4,1),
delta=(3/4,71/95,-1),
(a_1,a_2,a_3)=(3,60,105), (b_1,b_2,b_3)=(2,40,70),
(lambda_g)_1=-3/20, (lambda_f)_1=-1/10,
u=20, q=3/10.
```

The window checks are `5/24 < 1 <= 20` and `7/2 < 4 <= 7`, exactly as
`TF:130-148` reports. The declared sorting key in `pick105.py:45-48` selects
this row uniquely among the arithmetic survivors. Thus it is a valid
`(UNI)`-surviving *candidate*: `k=20` is within `kV_2<=u` and would give
`N=kV_2q=6`.

`pick105.py:43-44` has a stale comment naming `n-m` and `K`; line 48 and
`TF:122-124` actually use `(s,min N,e,m,M,V)`. Repair the comment; the executed
key and unique winner are unaffected.

It is not an attainment theorem. Frozen `d1floor.py:264-276` merely enumerates
integers for `1<=k<=floor(u/V_2)`. D1-PIN proves
`sum_B V_2(B)<=u` (`D1:345-354`), not that every permitted `k` occurs and not
that this row has exactly 20 actual bottom discs. `TF:168-169` and `TF:143`
turn the capacity into “there are `k=20`” without route-to-tree data. The safe
wording is:

> This row is not killed by `(UNI)` arithmetic. Its permitted list is
> `N in {3,6}`; under the charged floor `N>=6`, only the formal choice `k=20`,
> `N=6` remains. Attainment by a full branch packet is OPEN.

The counts reconcile exactly as follows. A “group” is
`(m,M_2,...,M_s,V_s)`. A lower-`V` assignment (called a “V-skeleton” by the
picker) additionally fixes the lower `V_i`. At `D=105` there are 5,037
assignments over 264 groups:

| arithmetic window | surviving assignments | groups with at least one surviving assignment | killed groups |
|---|---:|---:|---:|
| integer `N>=2` | 90 | 69 | 195 |
| integer `N in [4,16]` (D1's H2 column) | 64 | 55 | 209 |
| integer `N>=6` | 63 | 48 | 216 |
| integer `N in [6,16]` | 49 | 42 | 222 |

Therefore D1's `264/209` at `D1:549-553` means 264 groups and 209 groups for
which *every* lower-`V` assignment dies in `[4,16]`; it leaves 55 groups. It is
fully consistent with 63/49, which counts assignments and uses lower bound 6.
The 64 versus 49 assignment difference comes from the different lower bound;
49 assignments need not map injectively to groups and in fact map to 42.

One local census sentence is false: `TF:126-128` says ten of the 63 share
`(d,e,V_2)=(2,3,1)`. Exact enumeration gives **18**, of which 16 admit a value
in `[6,16]`; only two also have the selected `delta_1=3/4`. The fixed numerical
resonance data therefore do not apply verbatim to the claimed ten. The winner
and 63/49 totals are unchanged.

Verdict: skeleton arithmetic and count reconciliation **CONFIRMED/CAN**;
actual `k=20`, `N=6` attainment **GAP/CANNOT**.

## 8. The `D = 105` operator and the broken resonance recurrence

### 8.1 Order zero and the restricted linear map

After affine/scalar normalization, BOTTOM-ODE has the unique nondegenerate
orbit

```text
Gamma_0=p_g=pi^3-pi,       Phi_0=p_f=pi^2-2/3,
lambda_g=-3/20,            lambda_f=-1/10,
mu=-lambda_g/3=-lambda_f/2=1/20.
```

Thus order zero being a single orbit is **CONFIRMED**.

For coefficient vectors `(u_0,u_1,u_2,v_0,v_1,v_2,v_3)`, independent SymPy
expansion of `L_E` gives the matrix

```text
[ 1/10-E       0          0          0       1/15        0          0 ]
[    0      -E-1/20       0       3/10-2E      0       2/15         0 ]
[ 3E-3/10      0       -E-1/5       0       1/5-2E      0         1/5]
[    0       3E-3/20      0          0          0      1/10-2E      0 ]
[    0          0         3E         0          0         0        -2E]
```

for

```text
L_E : C[pi]_{<=2} plus C[pi]_{<=3} -> C[pi]_{<=4}.
```

The gcd of its nonzero maximal minors is

```text
E(10E-1)(20E-3)(20E-1)/4000.                                (8.1)
```

Consequently the delivered fixed-degree table is correct:

```text
generic E:                 rank 5, kernel 2, cokernel 0;
E in {0,1/20,1/10,3/20}: rank 4, kernel 3, cokernel 1;
E=1/5=4mu:                rank 5, kernel 2, cokernel 0.
```

This reproduces `orders.py:28-43` and `TF:327-334`.

### 8.2 Literal resonance claim: REFUTED

`TF:89-96` and the charge say that the rank drops exactly at
`E in mu Z_{>0}`. Equation (8.1) refutes this: the positive set for this map is
only

```text
{mu,2mu,3mu};       4mu and every later multiple are non-resonant.
```

`TF:328-330` itself says `4mu` is not a root, contradicting its executive
wording. Typed line `TF:756` already contains the finite repair.

### 8.3 Actual first and second restricted coefficients

Taking the charged `eta=delta_1-delta_2=1/380`, the restricted order-one
kernel is exactly

```text
Phi_1=(2/3)s_1 pi^2+(2/3)s_0 pi+(76/675)s_1,
Gamma_1=s_1 pi^3+s_0 pi^2-(37/225)s_1 pi-(1/3)s_0.
```

This independently confirms `TF:345-352`. The quadratic self-source belongs
at `2eta=1/190`. At that exponent, direct computation gives

```text
rank M(1/190)=rank [M(1/190)|-source]=5,
```

so the true second coefficient of this restricted evenly spaced expansion is
unobstructed with a two-dimensional affine fibre.

`order2.py:40-46` instead forms the order-one self-source once and feeds it to
`L_mu`, `L_2mu`, and `L_3mu`. But these are orders 19, 38, and 57 when
`mu=19eta`. At order 19 the source must contain every pair `i+j=19`, not just
`i=j=1`; orders 2 through 18 must first be solved. Thus the printed quadrics

```text
s_0s_1,      225s_0^2+376s_1^2,      s_0s_1
```

are correct compatibility functions for three artificial inhomogeneous
linear systems, but they are **not** recurrence conditions at the resonant
orders. `TF:354-375` is refuted in that interpretation. Likewise
`TF:376-379` counts 19 positive non-resonant orders strictly below `mu`; there
are 18, namely `k=1,...,18`.

The general source formula `TF:227-231` must sum over
`epsilon_i+epsilon_j=epsilon_k`; it may use `i+j=k` only after an evenly spaced
`epsilon_k=k eta` lattice has been established.

### 8.4 The omitted outer-root degrees

There is a prior geometric gap. The factorization at `TF:172-190` says that
the 57 outer `g` roots and 38 outer `f` roots already contribute at
`eta=1/380` factors of the form

```text
product_out (1+pi t^eta/W_rho(t)).
```

Therefore generically

```text
Gamma_1 contains pi p_g sum_(g,out) 1/W_rho(0),
Phi_1   contains pi p_f sum_(f,out) 1/W_rho(0),
```

of degrees 4 and 3. This conflicts with the caps 3 and 2 imposed at
`TF:323-325` and `orders.py:29`. Enlarging just order one to degrees `(3,4)`
gives 9 unknowns, 6 equations, rank 6, kernel 3 at `eta`; the high-degree
equation is `3u_3-2v_4=0`. The outer multiplicities may explain that relation,
but the report neither derives it nor separates prescribed outer data from a
seven-variable inner correction. The resonance polynomial itself changes
when the spaces change.

Nor does the skeleton prove that `1/380` is the first exponent of every inner
root tail; it is the first *displayed forced outer activation*. A complete
coefficient support/semigroup must be declared before numbering “orders 1 and
2”.

**Repair:** decompose each coefficient into prescribed outer and unknown inner
parts, prove the higher-degree equations for the former, establish the actual
exponent semigroup, and then run the full recurrence. The first bounded target
is the left-cokernel functional at `k=19` after retaining all 18 lower pairs.

Verdict item 6: order zero and the restricted rank table are
**CONFIRMED/CAN**. The infinite resonance statement and the resonant quadrics
as recurrence equations are **REFUTED**. Full positive dimension and “no kill”
for the charged skeleton are **GAP/CANNOT**.

## 9. Nullstellensatz existence table

`star.py:38-47` takes monic translation-normalized `Q=p_f`, kills the
`pi^-1,...,pi^[-(b-2)]` coefficients of `Q^(e/d)`, and lets `P=p_g` be the
polynomial part. Write `Q^(e/d)-P=sum_{r>=1}h_r pi^-r`. Then

```text
W=dQP'-ePQ'=-dQH'+eHQ',
[pi^k]W=sum_{i=k+2}^b [d(i-k-1)+ei] q_i h_(i-k-1),  k>=1.
```

Every positive coefficient of `W` is therefore in
`(h_1,...,h_(b-2))=TRUNC`; exact expansion verified this for all 17 runs. It
is legitimate to saturate using the constant coefficient `kappa`.

For each row I audited the declared ring as

```text
QQ[q_0,...,q_(b-2),w]
```

with generator order `list(unk)+[w]`; `pi` has been eliminated before the
Groebner call. The augmented ideal is

```text
I=<TRUNC equations, w kappa-1>.                               (9.1)
```

This directly decides whether `V(TRUNC)` meets `D(kappa)` over the algebraic
closure. It is equivalent to the needed localization/saturation existence
test; `I` is proper iff a nondegenerate star exists over `C`. A known exact
`(2,3,1)` witness gives `kappa=3` and passes. Adding `kappa=0` to (9.1) gives
Groebner basis `[1]`, the required negative control.

At `starexist.py:27`, explicitly pass `domain=sp.QQ` and assert the returned
domain/generator order. SymPy inferred the right ring; the hostile rerun made
these checks explicit.

The one-core rerun reproduced all 15 basis sizes and all 15 proper-ideal
verdicts:

| `(d,e,V)` | `(a_1,b_1)` | truncation equations | GB size | verdict |
|---|---:|---:|---:|---|
| `(2,3,1)` | `(3,2)` | 0 | 1 | REALISABLE |
| `(2,5,1)` | `(5,2)` | 0 | 1 | REALISABLE |
| `(2,7,1)` | `(7,2)` | 0 | 1 | REALISABLE |
| `(3,4,1)` | `(4,3)` | 1 | 3 | REALISABLE |
| `(3,5,1)` | `(5,3)` | 1 | 3 | REALISABLE |
| `(3,7,1)` | `(7,3)` | 1 | 4 | REALISABLE |
| `(2,3,2)` | `(6,4)` | 2 | 3 | REALISABLE |
| `(2,5,2)` | `(10,4)` | 2 | 5 | REALISABLE |
| `(2,7,2)` | `(14,4)` | 2 | 10 | REALISABLE |
| `(4,5,1)` | `(5,4)` | 2 | 9 | REALISABLE |
| `(4,7,1)` | `(7,4)` | 2 | 15 | REALISABLE |
| `(5,6,1)` | `(6,5)` | 3 | 29 | REALISABLE |
| `(5,7,1)` | `(7,5)` | 3 | 44 | REALISABLE |
| `(2,3,3)` | `(9,6)` | 4 | 8 | REALISABLE |
| `(2,5,3)` | `(15,6)` | 4 | 48 | REALISABLE |

The complete rerun took 10.8 seconds. Two extensions fit comfortably inside
the charged 15-minute allowance:

| extra `(d,e,V)` | `(a_1,b_1)` | truncation equations | GB size | seconds | verdict |
|---|---:|---:|---:|---:|---|
| `(2,3,4)` | `(12,8)` | 6 | 25 | 14.6 | REALISABLE |
| `(7,8,1)` | `(8,7)` | 5 | 403 | 220.2 | REALISABLE |

The `b_1=7` row is outside the `D<=120` census; `(2,3,4)` is inside, reducing
that census residual from 205 to 204. These computations do not prove
STAR-ALLV.

`starexist.py:20-29` prints properness, not a point. `TF:505-515` lists six
exact witnesses and `star_run.log` reaches eight; seven original rows have no
delivered coordinates. Proper ideals prove existence, not an explicit point.
Also `TF:527-532` wrongly suggests all `b_1<=6` cases were decided: the census
triples `(2,7,3)`, `(3,4,2)`, `(3,5,2)`, `(3,7,2)`, `(6,7,1)` have `b_1=6`
and were not in the table. Repair this to “the 15 listed triples, each with
`b_1<=6`.”

Verdict item 7: **CONFIRMED** for 15/15 existence over `C`; two further
existence decisions **CONFIRMED**. **GAP/CANNOT** for “all 15 with explicit
witnesses.” Promote the table as a Nullstellensatz existence table, not as a
15-point witness table.

## 10. Controls

I reran three of the four suites, including the required two-tower suite:

```text
control1.py   24 checks, 0 failures
control3.py   12 checks, 0 failures
control4.py   21 checks, 0 failures
-----------------------------------
rerun         57 checks, 0 failures
```

Together with control 2's delivered 21/0 log this explains the charged total
78/0.

Control 1 is exact: for `(y,x+y^k)`, the integral equals the fibre root and
the interpolant is `y`. Control 3's polynomial criterion is also exact. If
`T=(c_2-x^j)^(1/k)` and the interpolant is `(H/T)y`, polynomiality requires a
polynomial `p` satisfying, up to a harmless nonzero scalar,

```text
(c_2-x^j)p'-(j/k)x^(j-1)p=1.                                (10.1)
```

For `deg p=r`, the highest coefficient in (10.1) is proportional to
`-(r+j/k)` at degree `r+j-1`, so it cannot cancel. A solution exists only for
`j=1`. Thus all eight non-Keller rows `j=2,3`, `k=2,...,5` fail condition (ii);
the displayed hypergeometric antiderivatives are consistent with the exact
degree obstruction. The phrase “grows like `j-1`” at `TF:613` is rhetoric,
not a separately measured norm, and should not be promoted.

Control 4 contains a real bookkeeping bug. At `control4.py:71-73` the list for
`lambda_g(delta_1)` excludes the selected centre root `rho`. The definition
of `lambda_g` includes its contribution `min(delta_1,infinity)=delta_1`.
Consequently the sums printed at `TF:620-627` are wrong. Restoring that term
gives:

| row | `delta_1` | corrected `lambda_f` | corrected `lambda_g` | corrected sum | `delta_1-1` | `deg W` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | `-1/2` | `-3/2` | `-2` | `-7/2` | `-3/2` | 2 |
| 1 | `-1/2` | `-2` | `-3` | `-5` | `-3/2` | 3 |
| 2 | `-2/3` | `-10/3` | `-3` | `-19/3` | `-5/3` | 4 |
| 3 | `-1/2` | `-5/2` | `-3` | `-11/2` | `-3/2` | 2 |
| 4 | `-1/3` | `-3` | `-2` | `-5` | `-4/3` | 2 |
| 5 | `-1/2` | `-3` | `-4` | `-7` | `-3/2` | 5 |
| 6 | `-1/3` | `-3` | `-4` | `-7` | `-4/3` | 2 |

All seven remain non-Keller, all seven still fail order matching, and the
bottom brackets still have positive degree `2,3,4,2,2,5,2`. Thus the intended
negative-control conclusion survives, but “78/0” did not validate the printed
lambda values: the assertions merely expected each row to fail.

Verdict item 8: **GAP as printed**. Controls 1 and 3 and the qualitative
two-tower failures **CAN** be promoted; the two-tower lambda table must first
be replaced by the corrected one above. The controls remain automorphism or
non-Keller checks, not evidence that a noninvertible Keller skeleton is
globally realised.

## 11. DELTA-DENOM measurement only

The one-core rerun of `deltadenom.py` reproduces the charged predicates and
counts over the 902,893 admissible lower-`V` assignments in `D=48,...,120`:

```text
denom(delta_1) divides n:              6,719  (0.74%)
denom(delta_1) divides n or m:         8,634  (0.96%)
(UNI), integer N>=6 assignments:       9,553
  among them denom(delta_1) divides n: 3,266 (34.19%)
Moh rows: divides n on 5/6; divides n or m on 6/6.
```

The rerun took 35.15 seconds. For the selected row, `denom(3/4)=4` divides neither 105 nor 70, and
`denom(71/95)=95` does not divide 105. These are exactly the measurements at
`TF:681-694`. The program tests elementary divisibility predicates on census
outputs; it does not enumerate branch ramification partitions and does not
prove a necessary filter. Per the charge, I make no filter verdict.

Verdict item 9: **CONFIRMED — CAN promote only with the type MEASURED / NOT A
FILTER.**

## 12. FALLACY-v2 audit and bounded residuals

- **Flag/place/series:** this review keeps fibre branches `tau_i`, the formal
  disc coordinate `pi`, lower-`V` assignments, and full branch packets
  distinct. None is promoted to a physical place ledger.
- **Per-ray/exit-set charge:** no new exit price is asserted, so no
  `charge_basis` declaration is emitted.
- **Carrier/attainment:** the picker supplies a representative arithmetic
  value of `k`; it does not supply `FULL_ACTUAL_FIRST_SEPARATION`. The repair in
  section 7 treats `N=6` only as permitted.
- **Floor/attainment:** `sum V_2<=u` is a cap. Equality and 20 discs require a
  packet witness.
- **`sat()` wrapping:** section 9 declares the coefficient ring and generator
  order, uses the augmented ideal rather than a name-matched wrapper, and runs
  both a `kappa=3` positive witness and the `kappa=0` negative control.
- **Raw remainder degree:** section 5 explicitly cancels the degree-`deV`
  leader, excludes `C=0`, and checks the next leader before taking `deg C`.
- **Variable/ring map:** `(x,y)->(t,pi)` and its determinant are explicit;
  `pi` is eliminated before the star ideal is placed over `QQ`.
- **Prime/derivative:** every prime on `p_f,p_g,P,Q,C` denotes `d/dpi`;
  `F_t` denotes `d/dt`.
- **Merge-free/M-descent and target/arrival index:** neither mechanism is used
  in a promoted conclusion here.

The remaining OPENs are bounded as follows.

1. **OPEN[GLOBAL-INTERP].** Test the 105 branches, constants/monodromy, and
   degree-`<105` interpolant for membership in `C[x]`, then glue the packet.
2. **OPEN[D105-TRUE-RECURRENCE].** First derive the exponent support and the
   outer/inner decomposition. Conditional on step `eta=1/380`, solve the 18
   lower coefficient pairs before evaluating the single cokernel functional
   at `k=19`; to audit all three restricted resonances, continue finitely to
   `k=57` and test `k=19,38,57`.
3. **OPEN[D105-PACKET-ATTAINMENT].** The selected row has `1<=k<=20`; construct
   the actual bottom-disc packet or prove which `k` occur. Only `k=20` reaches
   the charged `N>=6` floor.
4. **OPEN[STAR-POINTS].** Extract coordinates for seven unprinted original
   rows plus the two new rows. **OPEN[STAR-ALLV]:** 204 `D<=120` census triples
   remain after adding `(2,3,4)`; five undecided ones already have `b_1=6`.
5. **OPEN[EIGEN-A].** One worked `s>=3` tower with explicit head still suffices
   to test the proposed formula for `A`; this is independent of repaired
   STAR-EIGEN.
6. **OPEN[DELTA-DENOM].** Measurement confirmed; the separate lane must decide
   whether actual ramification partitions impose anything stronger.

## 13. Typed verdict and promotion block

```text
HASH GATE                 CONFIRMED: all five frozen SHA-256 values exact.

ITEM 1 LOCAL-KELLER       GAP.
  CAN                     exact necessary identity in the completed D_1 chart,
                          coefficientwise for an existing Keller pair.
  CANNOT                  identify C[[t^eta]][pi] with C[x]-polynomial
                          Lagrange interpolation or global branch gluing.

ITEM 2 BOTTOM-ODE         CONFIRMED -- CAN.
                          d p_f p_g' - e p_g p_f' = kappa,
                          deg p_g=eV_2, deg p_f=dV_2,
                          kappa=-ec/lambda_g=c(d+e)/(1-delta)=cde/q.
CONTROL (y,x+y^k)         CONFIRMED: c=-1, q=1, bracket=-k.

ITEM 3 STAR-SIMPLE        CONFIRMED -- CAN.
ITEM 3 STAR-RESIDUE       GAP AS PRINTED.
  CAN AFTER REPAIR        p_f(c_i)p_g'(c_i)=kappa/d
                          =c(d+e)/(d(1-delta))=ce/q.
  REFUTED EXPRESSION      ce/(1-delta).
ITEM 3 STAR-SUM           CONFIRMED -- CAN, including terminal nonzero value.

ITEM 4 STAR-ABC           CONFIRMED -- CAN.
                          C=p_f^e-rho p_g^d has degree
                          V_2(de-d-e)+1; p_f,p_g,C are pairwise coprime and
                          squarefree; Mason equality and Belyi passport close.

ITEM 5 STAR-EIGEN         GAP AS A GEOMETRIC THEOREM -- CANNOT AS DISPLAYED.
  CAN AFTER REPAIR        A|(d+e)V_2-1 for all A; root dichotomy only A>1.
  REFUTED INFERENCE       abstract (3,5,1), A=1 star has both values nonzero;
                          no attained Keller-disc counterexample is claimed.

D=105 CENSUS              CONFIRMED AS ARITHMETIC.
                          5037 assignments / 264 groups; [4,16] leaves
                          64 assignments / 55 groups, hence 264/209;
                          >=6 leaves 63/48; [6,16] leaves 49/42.
D=105 N=6 ATTAINMENT      GAP -- CANNOT. k=20 is permitted, not realised.
TF 'TEN SHARE (2,3,1)'    REFUTED: exact count 18 (16 in [6,16]).

ITEM 6 ORDER ZERO         CONFIRMED -- CAN: one nondegenerate orbit.
ITEM 6 RESTRICTED L_E     CONFIRMED -- CAN:
                          generic 7/5/rank5/ker2/coker0;
                          rank4/ker3/coker1 at mu{0,1,2,3} only.
RESONANCE = mu Z>0        REFUTED: 4mu is already non-resonant.
RESTRICTED ETA k=1,2      CONFIRMED: eps=1/380,1/190; no cokernel.
RESONANT QUADRICS         REFUTED AS RECURRENCE CONDITIONS.
FULL OUTER-FACTOR SYSTEM  GAP; degree caps omit forced pi*p terms.
ITEM 6 OVERALL            REFUTED AS CHARGED -- CANNOT PROMOTE NO-KILL.

ITEM 7 NULLSTELLENSATZ    CONFIRMED: 15/15 REALISABLE -- CAN.
EXTRAS                    CONFIRMED: (2,3,4), b_1=8; (7,8,1), b_1=7.
EXPLICIT 15 WITNESSES     GAP/NOT DELIVERED -- CANNOT.

ITEM 8 CONTROL COUNT      MEASURED: delivered 78/0; rerun three suites 57/0.
CONTROL 3 HYPERGEOMETRIC  CONFIRMED by exact polynomial obstruction -- CAN.
CONTROL 4 LAMBDA TABLE    REFUTED; centre-root term omitted.
CONTROL 4 CONCLUSION      CONFIRMED AFTER REPAIR: all 7 still fail ORD/ODE.

ITEM 9 DELTA-DENOM        CONFIRMED MEASUREMENT ONLY -- CAN AS MEASURED.
                          6719/902893; 8634/902893; 3266/9553; Moh 5/6,6/6.
FILTER CONSEQUENCE        NOT ADJUDICATED; none promoted.

FLAGSHIP OVERALL          CANNOT PROMOTE AS WRITTEN.
SAFE PROMOTION            BOTTOM-ODE; STAR-SIMPLE; corrected STAR-RESIDUE;
                          STAR-SUM; STAR-ABC; repaired STAR-EIGEN divisibility;
                          restricted finite-rank table; exact measurements.
```

<!-- BODY-END -->
