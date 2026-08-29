# HENS-CT rank-one control R0: typed target, exact controls, and blocked certificate interface

Date: 2026-08-28  
Author: Sol Ultra / Codex, HENS-CT lane  
Status: **TOOL-INTERFACE FAILURE; NO ALGEBRAIC TELESCOPER OR CERTIFICATE EMITTED; NO PROMOTION**

## 0. Verdict

This lane did **not** instantiate the first algebraic HENS-CT certificate.
It fixes the charged identity and all of its receiver/section/index typing,
and it supplies exact replay and mutation controls, but the frozen
`ore_algebra`/PassageMath route stopped before algebraic composition.  The
terminal missing interface is precise:

```text
OreAlgebra(ZZ[ss,xx,yy], "Dss", "Dxx", "Dyy").gens()

NotImplementedError: polynomials over Multivariate Polynomial Ring in
ss, xx, yy over Integer Ring are not supported in Singular
```

The exception is raised while `ore_algebra` constructs its associated
commutative operator algebra.  Thus no annihilating ideal `J`, telescoper
`L`, certificate operator `C`, algebraic certificate `B=C(Q)`, or direct
field remainder was produced.  In particular, the reviewed scalar residue
recurrence below is **not** being relabelled as a creative-telescoping
certificate.

The small source/evidence package is

```text
cases/ggv_hens_ct_rank_one_control_r0_20260828/
```

Its `REPLAY.md`, `SOURCE.sha256`, and `EVIDENCE_MANIFEST.sha256` give the
replay map and immutable hashes.

## 1. Frozen mathematical charge

The rank-one control from the reviewed `R3` calculation is

```text
H=X^4,               p=X,
A=X^7+X^4+1,
F=X^8+A t,
P^8=X^8+s A P,
Q=P^2.
```

Writing `P=Xy` gives the selected Hensel branch

```text
h=1+X^-3+X^-7,
y^8=1+s h y,
y(s=0)=1,
Q=X^2 y^2.
```

The charged algebraic field and the required certificate identity are

```text
E=Q(s,X)[y]/(y^8-1-s(1+X^-3+X^-7)y),

0 != L in Q(s)<D_s>,
B in E,
L(Q) dX = d_X B.                                      (1.1)
```

Equivalently, an Ore certificate operator `C` may first be emitted with

```text
L-D_X C in Ann(Q),       B=C(Q),
```

but success still requires the independent direct reduction of
`L(Q)-d_X B` to zero in `E`.  A zero residue, a scalar recurrence, or a
coefficientwise Laurent primitive is weaker than (1.1).

## 2. Correct receiver gauge

For `H=X^4`, the R8 connection is especially transparent:

```text
nabla_m(f)=(f'+m f/X)dX,
V_m=coker(nabla_m),
basis(V_m)=X^(-m-1)dX.                                (2.1)
```

For coefficient sector `b` and section index `k`, the three indices are

```text
n=b+4k                    physical coefficient,
m=n+22                    physical row,
m0=b+22                   fixed receiver.             (2.2)
```

The physical coefficient is

```text
q_n=alpha_n X^2 h^n,
alpha_n=2/(n+2) binom((n+2)/8,n).
```

R8's fixed-receiver form is not `H^k q_n dX`.  It is

```text
X^(-m0) q_(b+4k)dX in V_m0.                           (2.3)
```

Indeed, if `c_(b,k)=X^(-(n+22))q_n`, then
`H^k c_(b,k)=X^(-m0)q_n`.  Multiplication by `X^m0`
identifies (2.1) with ordinary exact differentials:

```text
X^m0 nabla_m0(g)=d_X(X^m0 g).
```

Consequently (1.1) is exactly the convenient ordinary gauge.  If it were
available, its twisted fixed-receiver certificate would be

```text
L(X^-m0 Q)dX=nabla_m0(X^-m0 B).                       (2.4)
```

The coordinate of (2.3) in the basis of (2.1) is
`Res_0(q_n dX)`, as required.

## 3. Four-section typing of a genuine certificate

Let `i^2=-1` and define the physical coefficient projector

```text
Pi_b Q(X,s)=(1/4) sum_(ell=0)^3 i^(-b ell)Q(X,i^ell s)
           =s^b S_b(X,z),
z=s^4,
S_b=sum_(k>=0)q_(b+4k)z^k.                            (3.1)
```

The correct fixed-receiver integrand is therefore

```text
X^(-(b+22)) S_b(X,z)dX,                               (3.2)
```

not the literal/double-weighted `sum H^k q_(b+4k)z^k`.

For an emitted ordinary-form operator

```text
L=sum_j a_j(s)D_s^j,
```

the mandatory four-section type check is

```text
a_j(i s)=i^j a_j(s) for every j.                      (3.3)
```

When (3.3) holds, write `a_j(s)s^-j=r_j(z)`.  On
`s^b f(z)`, the induced operator is

```text
L_b=sum_j r_j(z) prod_(ell=0)^(j-1)(b+4 theta_z-ell),
theta_z=z D_z.                                        (3.4)
```

If `Pi_b B=s^b T_b`, projection of (1.1) would give the correctly typed
certificate

```text
L_b(S_b)dX=d_X T_b,
L_b(X^(-(b+22))S_b)dX
  =nabla_(b+22)(X^(-(b+22))T_b).                      (3.5)
```

If (3.3) fails, one must section the algebraic input separately or construct
and certify an equivariant common left multiple; one may not silently read
four scalar recurrences off a non-equivariant operator.  Because this lane
emitted no `L` or `B`, (3.3)--(3.5) are the frozen success interface, not a
claimed output.

## 4. Reviewed scalar control and all startup indices

The exact residue coordinate is

```text
c_n=Res_0(q_n dX)
   =n alpha_n
   =2n/(n+2) binom((n+2)/8,n).                        (4.1)
```

The primitive reviewed recurrence is

```text
D7(n)c_(n+8)=N7(n)c_n,                                (4.2)

D7(n)=n(n+1)(n+3)(n+4)(n+5)(n+6)(n+7),
N7(n)=-(1/8) prod_(j=0)^6 ((7n-2)/8+j).
```

The only nonnegative zero of the forward coefficient `D7` is `n=0`.
Thus `c0=0` is automatic and `c1,...,c8` are a sufficient unsectioned
startup block.  The corresponding maximal row is `m=8+22=30`.

For `s_(b,k)=c_(b+4k)`, (4.2) becomes

```text
A_b(k)s_(b,k)+B_b(k)s_(b,k+2)=0,

A_b(k)=(1/8) prod_(j=0)^6 ((28k+7b-2)/8+j),
B_b(k)=(4k+b)(4k+b+1)(4k+b+3)(4k+b+4)
       (4k+b+5)(4k+b+6)(4k+b+7).                     (4.3)
```

The disambiguated startup table is

| coefficient sector `b` | section indices required | max physical `n` | max row `m=n+22` | forward singularity |
|---:|---:|---:|---:|---|
| 0 | `k=0,1,2` | 8 | 30 | `B_0(0)=0` only |
| 1 | `k=0,1` | 5 | 27 | none |
| 2 | `k=0,1` | 6 | 28 | none |
| 3 | `k=0,1` | 7 | 29 | none |

At this control `c1=1/4`, so it already fails row 23.  Row 30 is only the
sufficient recurrence cutoff, not its minimal survival-decision row.

## 5. Exact replay and required mutations

`replay_rank_one_controls.py` is standard-library-only.  It reconstructs
`q_n` as exact Laurent polynomials through the needed range, verifies
(4.1)--(4.3), and terminates with

```text
PASS_RANK_ONE_CONTROLS
```

It also rejects all four preregistered mutations:

1. **Omitted `+22`, actual receiver retained.**  At `b=1,k=0`, the correct
   coefficient in `V_23` is `1/4`; replacing `X^-23 q_1` by `X^-1 q_1`
   makes the `X^-24 dX` coordinate zero.
2. **Literal/double `H^k`.**  The first stored witness is
   `(b,k,n)=(0,2,8)`: correct coordinate `4807/1048576`, literal-weighted
   coordinate `0`.
3. **Wrong projector phase.**  Replacing `i^(-b ell)` by `i^(b ell)`
   extracts physical sector `-b`, detected at `b=1` because `c1 != c3`.
4. **False sector parity.**  The true free invariant is that the `b=2`
   section has zero odd-`k` coefficients; `b=0` is not even, since
   `c4=-15/512`.

These checks validate typing and the known scalar formulas.  They do not
supply the absent algebraic `B`.

## 6. Bounded AWS execution and terminal interface

The authorized machine was `r6c`, instance `i-040b7a1c2ed72d4cc`, DMI host
`ip-172-30-0-150`.  Each mathematical launch rechecked Amazon EC2 DMI,
at least 450 GiB available memory, zero swap, and no competing heavy job.
The frozen limits were one process, 400 GiB virtual memory, 1800 seconds for
installation, and 14400 seconds for composition plus CT.  No local CAS and
no `r6d` capacity were used.

The exact software state at the terminal failure was

```text
Python 3.12.3
PassageMath components 10.8.10
ore_algebra commit 18680180c884fac869a064db99f29a221aad9dfe
optional-extension disabling patch sha256
  d0501816e90405d7a82efb6bbb939339f1dbb5c20d3700f28448fdeb680e356a
patched setup.py sha256
  38da4b778c52ea2b20105e9f15661c4a09c9776e06971fbcd989163a549d2f7a
```

The terminal sequence was:

1. The unmodified pinned package failed while compiling the optional
   analytic extension `dac_sum_c.c` (`unknown type name slong`).  This was
   unrelated to exact CT.
2. The checked-in one-line source patch disabled only optional analytic
   extensions.  The pure-Python install then succeeded in about 59 seconds.
3. Modular PassageMath lacked monolithic `sage.all`.  A fresh-process smoke
   identified its installed aggregate `sage.all__sagemath_symbolics`; this
   source-only import repair succeeded.
4. The final emitter stopped while constructing the *outer* Ore generators
   with the Singular coefficient-ring exception in Section 0.  Runtime was
   0.57 seconds and peak RSS 160144 KiB.  It never reached the charged field,
   algebraic composition, or CT.

The exact final traceback and resource record are in
`evidence/final_ore_base_ring_interface_failure/ct.stderr`; the complete
installed package freeze is adjacent.

### Operational disclosures

Several pre-mathematical setup attempts stopped on missing host build
components (`python3.12-venv`, `pkg-config`, compiler, MPFR, MPFI).  During
that diagnosis I mistakenly installed Ubuntu's unrelated bioinformatics
package named `libarb-dev`; it pulled irrelevant dependencies.  It was not
used by this lane and was left in place rather than removed destructively.
An early DMI guard checked product name instead of system vendor and was
repaired before the charged launch.  One source-only namespace
`...T010745Z_v3` was abandoned before launch because its source-hash preflight
correctly detected three omitted provenance files.  None of these attempts
performed annihilator or CT computation.

## 7. Precise missing interface and clean continuation

The first missing interface is not mathematical Hermite reduction yet.  It
is a compatible construction of the multivariate differential Ore algebra
needed by `annihilator_of_composition`.  At this pinned version,
`associated_commutative_algebra()` dispatches to
`MPolynomialRing_libsingular` with coefficient ring `ZZ[ss,xx,yy]`, which
the installed Singular bridge rejects.

A successor must first freeze and independently validate one narrow adapter,
for example:

- construct the outer Ore algebra over the fraction field of the coordinate
  ring, if `annihilator_of_composition` preserves the intended derivations;
  or
- force the generic polynomial-ring implementation / use an upstream version
  whose Singular dispatch handles this base.

Before charging the control, that adapter should replay the small algebraic
integral example shipped in `ore_algebra.ideal.ct` **with certificates** and
verify `L-D_X C` by exact ideal reduction.  Only then should it run the
frozen control and add the independent field action

```text
y_s = h y/(8y^7-s h),
y_X = s h' y/(8y^7-s h),
L(X^2y^2)-d_X(C(X^2y^2))=0 in E.                      (7.1)
```

No such adapter was preregistered in this lane, so it stops here rather than
turning a sequence recurrence into a fictitious certificate.

## 8. Scope firewall

This result proves neither the HENS-CT method on the control nor any
campaign branch.  It changes no statement about branch P/Q, survivor cells,
polynomial `G`, raw determinants, endpoint fibres, GGV landing, or JC2.
The only bankable outputs are:

- the exact charged certificate interface (1.1);
- the corrected receiver and four-section typing (2.1)--(3.5);
- the reviewed scalar/startup controls and mutation suite; and
- the reproducible software boundary in Sections 6--7.

The proof-of-method obligation remains open until a nonzero algebraic
`L,C,B` and the direct zero remainder (7.1) are actually archived and
independently reviewed.
