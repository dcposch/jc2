# TD12-BCHILD/v1: shared first-child Keller/source recurrence

Date: 2026-08-29  
Producer: Sol 5.6 (Ultra), provisional independent derivation  
Basis: `76c746f698103d20019bfeb72654a361ccc5371d`

## 0. Provisional disposition

```text
SOURCE_UNDERDETERMINED
```

There is one exact parent-chart Keller convolution that serves the depth-24
`nu=25` B direction and both depth-16 `nu=17` sibling directions.  The child
root changes only the final Taylor-evaluation functional.  The frozen basis,
however, does not initialize this recurrence and therefore emits none of the
three requested non-top forward vectors.

The first genuine obstruction is sharper than a mere missing scalar.  At
each relative order the Keller equation is one linear differential equation
in two new polynomial coefficient functions, one on the f side and one on
the g side.  Moreover, the reduced `q_F` in Proposition 8.1 is obtained from
the terminal derived source polynomial `h_F` after division by a power of
the reduced `p`; it is not licensed as the top coefficient of the original
`g`.  The frozen records supply neither the exact pair/completion nor the
derived-source ladder needed to recover that missing side.

Consequently no level-one split or pure-power verdict is licensed.  The
maximum safe descendant use is the exact recurrence/interface and the
statement that all three route-specific child gates remain necessary but
unevaluated.  No route-specific coefficient emitter or CAS migration is
licensed from the current inputs.

## 1. Exact chart and base Keller convolution

Fix an exact pair `(f,g)` with `J(f,g)=1`, a fibre/branch represented by an
Eggers--Wall point `F`, and a suitable positive integer `kappa` with

```text
u = pi(F),                 n_F = kappa*u in Z.
```

On a y-side chart, write the frozen Puiseux prefix as `phi(x)` and set

```text
eta = x^u (y-phi(x)).
```

Then `d eta/dy=x^u`, so the change-of-variables identity is exactly

```text
J_(x,eta)(f^F,g^F)=x^(-u).                                (1.1)
```

For the finite Laurent expansions supplied by Statement 3.7,

```text
f^F(x,eta) = sum_r x^(r/kappa) F_r(eta),
g^F(x,eta) = sum_s x^(s/kappa) G_s(eta),                  (1.2)
```

coefficient extraction in (1.1) gives, for every integer `N`,

```text
sum_(r+s=N) (r F_r G_s' - s F_r' G_s)
    = kappa * 1_(N=kappa-n_F).                            (K_N)
```

Primes mean `d/deta`.  Formula `(K_N)` is the promised shared Keller
recurrence.  It is independent of `nu` and of the child centre.

Let `R=max{r:F_r!=0}`, `S=max{s:G_s!=0}` and define top-relative pieces

```text
P_k := F_(R-k),             Q_l := G_(S-l),
m_* := R+S-kappa+n_F.
```

Proposition 4.1 implies `m_*>=0`.  At relative grade `m`, `(K_N)` becomes

```text
sum_(k+l=m) ((R-k) P_k Q_l' - (S-l) P_k' Q_l)
    = kappa * 1_(m=m_*).                                 (K_m)
```

After grades `<m` are known, the new extremes obey

```text
 R P_0 Q_m' - (S-m)P_0'Q_m
+(R-m)P_m Q_0' - S P_m'Q_0
 = kappa*1_(m=m_*)
   - sum_(1<=k<=m-1)
       ((R-k)P_k Q_(m-k)'-(S-m+k)P_k'Q_(m-k)).            (1.3)
```

This displays the identifiability defect: one equation contains both new
functions `P_m` and `Q_m`.  If `P_m` is separately supplied, (1.3) is a
first-order linear ODE for `Q_m`; dividing by `R P_0` uses the hypotheses
`R!=0`, `P_0!=0`, characteristic zero, and then polynomiality plus the
declared support/boundary normalization must select among the integration
branches.  Nothing in the reduced top record makes that choice.  The same
observation holds with the two sides interchanged.

## 2. Exact derived-source version

The reduced pattern `q_F` cannot simply be substituted for `Q_0`.  In the
printed source one first sets `h_0=g` and recursively constructs

```text
h_(j+1) = h_j^(a_j) - s_j f^(b_j),
gcd(a_j,b_j)=1,          s_j!=0.                         (2.1)
```

Writing `H_(j,r)` for the `x^(r/kappa)` coefficient of `h_j^F`, the exact
source-coefficient recursion is

```text
H_(j+1,r)
 = sum_(r_1+...+r_(a_j)=r) prod_t H_(j,r_t)
   - s_j sum_(q_1+...+q_(b_j)=r) prod_t F_(q_t).          (S_jr)
```

Literal differentiation of (2.1), starting from `J(f,g)=1`, gives

```text
J_(x,y)(f,h_m)
 = K_m prod_(j=0)^(m-1) h_j^(a_j-1),
K_m=prod_(j=0)^(m-1) a_j.                               (2.2)
```

Thus its exact chart-coefficient equation is

```text
sum_(r+s=N) (r F_r H_(m,s)' - s F_r' H_(m,s))
 = kappa*K_m *
   [x^((N-kappa+n_F)/kappa)]
   prod_(j=0)^(m-1) (h_j^F)^(a_j-1).                    (S_N)
```

If the derived polynomials are rescaled, the nonzero constant `K_m` can be
absorbed only after recording those rescalings; it cannot silently be
dropped in a source compiler.

Proposition 8.1 constructs its reduced `p,q` from leading forms of `f` and
the `h_j`, and obtains `q` from the leading terminal `h_F` after a power of
`p` has been removed.  Its displayed Wronskian is therefore the top equation
of this construction, not a full lower recurrence for `(P_k,Q_k)`.  To run
`(S_jr)` and `(S_N)` one must supply the exact ladder
`(a_j,b_j,s_j,h_j)`, every needed Laurent coefficient, and the chart map.
None is present in either frozen reduced cell.

## 3. Child transport and the three vectors

Let `c` be a raw child centre and let the full f-top have exact multiplicity
`I>0` at `c`.  With `P_k=F_(R-k)`, the child substitution

```text
eta = c + x^(-1/kappa) z
```

shows that the diagonal of total drop `I` is

```text
v_(c,k) = [(eta-c)^(I-k)] P_k(eta),       0<=k<=I,
C_(c,1)(z) = sum_(k=0)^I v_(c,k) z^(I-k).              (3.1)
```

This is a Taylor transport formula, not a Keller recurrence.  The recurrence
that must first produce the `P_k` is `(K_m)`, or `(S_jr)+(S_N)` when the
derived source ladder is used.

### 3.1 The `nu=25` B vector

Put `T=eta^25`, `A=8u_0`, `B=9u_0`, `u_0!=0`, and choose `c_B^25=B`.
Up to its nonzero top scalar `lambda_f`, the full f-top is

```text
P_0 = lambda_f ((T-A)^2(T-B))^I.
```

Hence its known leading vector entry is

```text
v_(B,0) = lambda_f (25 c_B^24 (B-A)^2)^I != 0,          (3.2)
```

while

```text
v_B=(v_(B,k))_(k=1..I)
```

is not determined.  Under the displayed direct-entry rider only, `I=6n`
for that entry-family parameter `n`.  The frozen semi-invariance and
transport spaces impose

```text
e_k = 22k (mod 25),
ord_A(P_k)>=2I-k,       ord_B(P_k)>=I-k.                 (3.3)
```

The producer's degree-one `R_k(T)` interpolation varies the B diagonal
independently of the already fixed A diagonal while preserving (3.3) and
the degree cap.  Equation `(1.3)` would couple this freedom to an unknown
g-side/source piece, but the frozen basis supplies neither that piece nor
the support/normalization needed to eliminate it.  Interpolation proves
only top compatibility; it does not prove that either choice lifts to a
Keller pair.

### 3.2 The two `nu=17` sibling vectors

Let

```text
B_+ = ((9+3 sqrt(-1))/8) A,
B_- = ((9-3 sqrt(-1))/8) A,
c_+^17=B_+,             c_-^17=B_-.
```

The T1 solve proves these two orbit values are distinct, nonzero, and
different from `A`, up to their swap and common scale.  With

```text
p=(T-A)^2(T-B_+)(T-B_-),       T=eta^17,
P_0=lambda_f p^I,
```

the two vectors are evaluations of the same coefficient family:

```text
v_(+,k)=[(eta-c_+)^(I-k)]P_k,
v_(-,k)=[(eta-c_-)^(I-k)]P_k,          0<=k<=I,          (3.4)
```

and

```text
C_(+,1)=sum_k v_(+,k)z^(I-k),
C_(-,1)=sum_k v_(-,k)z^(I-k).
```

Their known leading entries are

```text
v_(+,0)=lambda_f(17 c_+^16(B_+-A)^2(B_+-B_-))^I !=0,
v_(-,0)=lambda_f(17 c_-^16(B_--A)^2(B_--B_+))^I !=0.    (3.5)
```

The remaining entries are not determined.  Their residue spaces satisfy

```text
e_k = 13k (mod 17).                                     (3.6)
```

The two vectors are therefore not independent inputs: both are linear
evaluations of each common `P_k`.  T1 alone also does not prove that they
are Galois conjugates.  Such a conclusion would additionally require the
coefficient pieces and chart to descend to the fixed subfield and compatible
choices of the seventeenth roots.  Exact arithmetic must at least work over
a field containing `sqrt(-1)`, `c_+`, and `c_-`; replacing the roots by
rational values is invalid.  Under the same direct-entry rider, `I=6n`.

## 4. Normalization and delay state machine

For a purported centre `c`, define the first nonzero transport diagonal

```text
d_c=min{k+r : [(eta-c)^r]P_k != 0}.                     (4.1)
```

An exact typed child of top multiplicity `I` must satisfy

```text
[(eta-c)^r]P_k=0 for k+r<I,
d_c=I,
[(eta-c)^I]P_0!=0.                                      (4.2)
```

Thus its `C_(c,1)` is automatically nonzero, has exact degree `I`, and has
nonzero leading coefficient.  The guard still must be explicit:

1. `d_c<I`: an early Laurent term violates the claimed child transport;
   this is a chart/source mismatch, not a pure-power pass.
2. `d_c=I` but `deg C<I` or `C=0`: incompatible with exact multiplicity
   `I`; classify the input as incomplete or mistyped, never as pure.
3. `d_c>I`: also incompatible with the asserted exact top multiplicity.
   If multiplicity was not frozen, recompute the actual top/drop and restart;
   do not silently call this a delayed pass.
4. If the finite input does not reach `d_c`, return `NEED_MORE_SOURCE`.
5. If the first legitimate next coefficient lies on a finer exponent
   lattice, return `DENOMINATOR_JUMP`.  The depth-24/depth-16 no-jump routes
   reject that branch before their endpoint.

Only after (4.2) does one test

```text
deg gcd(C,C')=I-1,
```

and then the binomial/catalecticant pure-power identities.  A passing
polynomial has one root `alpha`; recenter `z -> z-alpha` and carry the full
Laurent state, not merely `C`, to the next level.  Two roots give the
route-specific split kill.  The same state machine is used for B through
levels 1--24 and for each sibling direction through levels 1--16.

## 5. Smallest safe interface and software consequence

```text
TD12_BCHILD_V1_Input =
  PairRef(f,g)
  + fibre and exact Puiseux branch prefix
  + completion/evaluation map and suitable kappa
  + exact support/top indices R,S
  + source ladder (a_j,b_j,s_j,h_j), if reduced q is consumed
  + coefficient/gauge normalization and coefficient field
  + route record (nu,I,root orbit,raw centre,depth cap).

RecurrenceState =
  all P_k,Q_k, or all F_r,H_(j,r), through the current grade
  + polynomial support bounds
  + selected free-side/gauge data
  + denominator/nonvanishing certificates.

Output =
  v_B, v_+, v_-
  + C-polynomials and normalized recenterings
  + one of OK, SPLIT, EARLY_TERM, DEGREE_DROP, NEED_MORE_SOURCE,
    DENOMINATOR_JUMP, SOURCE_UNDERDETERMINED, CHART_UNTYPED.
```

A generic exact checker for `(K_m)`, Taylor transport, normalization, gcd,
and binomial identities is mathematically licensed once those inputs exist.
A standalone route-specific generator is not: it would have to invent the
missing PairRef, g/source coefficients, support choices, or gauge.  Therefore
there is no licensed software migration or heavy computation from this
result alone.

## 6. Custody and scope

The full frozen manifest was rehashed before the derivation.  Exact hashes:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829  xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md
3f214db8c12d022c2852dfadbbc268d105484343a8f6d4664765a08d3efcea03  xmodel/m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
70cf67b2241b1361e958e673b81d883f34a87be9e5fe3631a3a36c35646c3060  xmodel/m2-td12-u1-sibling-exact-charge-r1-hostile-review-fable5-20260829.md
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
432a4152387cff943e220a6236912f2481a1ea3004d2c53ae95f14eb267f1ab0  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-hostile-review-grok46-20260829.md
635aecffbd226acbc29787cec86bc1fdcdfa459e1aa38a8d1a8acb5d6593b72a  xmodel/m2-20260829-promotions-theorem-interface-pass-sol56.md
91521dc126449ae217315b657493f2b9a170c630013d8c547cceab7f2e680113  xmodel/ideation-20260829T0820Z-synthesis.md
d3cf9d608427e4410ccb8b3ce04539fb22d854b9e58e6354d15115c3b48d564b  xmodel/ideation-20260829T0820Z-crosspoll-fable5.md
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
```

Passages actually charged: printed Statements 3.7 and 3.9, Propositions
4.1--4.2 and 8.1; B producer sections 4--6 and its hostile-review sections
6--7; sibling charge sections 1 and 4 and hostile-review section 5; sibling
T1 producer sections 2--7 and its hostile review; theorem-interface pass
section 4.1; the normalization/source-emitter discussion in the frozen
ideation synthesis and Fable cross-pollination.  The remaining manifest
members were perimeter-hashed but are not mathematical dependencies of the
new recurrence.

This report proves no existence of the reduced cells in an actual tree, no
formal germ, no polynomial Keller pair, no route kill, no panel exclusion,
no landing/coverage theorem, no degree bound, and no JC2 conclusion.

*End of sealed report body.*

## Seal

- Body length: `14033` bytes (all bytes before this heading).
- Body SHA-256:
  `79d4d37c57247977e5cdcb8cd6394aeda2908fe13ffc87e345f284f61e0a00f0`.
- Frozen Git basis:
  `76c746f698103d20019bfeb72654a361ccc5371d`.
