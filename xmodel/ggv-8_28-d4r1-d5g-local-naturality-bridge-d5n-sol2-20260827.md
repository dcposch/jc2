# D5N: exact reviewed D4R1-to-D5G local-naturality bridge

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2

## Verdict

**`PASS-D5N-EXACT-TYPED-LOCAL-NATURALITY-BRIDGE-NO-TARGET-VERDICT`.**

The reviewed D4R1 local outputs and reviewed D5G direct determinant now meet
in one exact typed square.  Over the common 400-slot raw coefficient ring,

```text
ev_xi(sum_(n=0)^22 D_n(X)t^n)
  =q0(t)*V(t)*(t*U'(t)-8*U(t)) mod t^23,             (0.1)
```

where `ev_xi` fixes every named raw leaf and sends `X` to
`c+s(t)` in `C[c]/(c^8-1)`.  This is a theorem composition through an
independently replayed free-ring chain rule; it does not identify the local
coordinate with a global polynomial automorphism.

The generic weight-22 bridge retains the complete lower-row correction

```text
K22=sum_(n=0)^21 [t^(22-n)]D_n(c+s(t)),
R22(c)=[t^22](q0*C)-K22,
C=V*(t*U'-8*U).                                      (0.2)
```

Only after quotienting by every coefficient of `D0,...,D21` does this become

```text
R22(c)=D22(c)=H'(c)*C22.                              (0.3)
```

Even then the factor-local side recovers only `R22`.  D5G's direct
`Q22` remains load-bearing, and the global target is still exactly

```text
R22=1 and Q22=0.                                      (0.4)
```

No raw specialization satisfying the lower gate or target is constructed
here, so D5N supplies no face or family verdict.

## 1. Ambient rings and exact maps

Let

```text
C=Q[400 named positive-weight D3 raw slots],
S=C[X,t]/(t^23),
A=C[c]/(c^8-1),
H=X^8-1.
```

D5G supplies the authoritative coefficients `D_n in C[X]`.  D4R1 supplies
the node-rooted series

```text
s,U,q0,V in A[[t]]/(t^23)
```

with `xi=c+s`, `F=U+u^2`, `q0=u_X|_(u=0)`, and
`V=G_u|_(u=0)`.  The bridge is the `C`-algebra map

```text
ev_xi:S -> A[[t]]/(t^23),
raw_slot |-> the identically named D4R1 raw leaf,
t |-> t,
X |-> c+s(t).
```

All 23 root IDs for `s,U,q0,V` and the inverse coordinate `alpha` are frozen
in `RESULT.json`.  Each coefficient

```text
C_n=sum_(i+j=n) V_i*(j-8)*U_j
```

is serialized as a circuit recipe referencing the frozen D4R1 node IDs.
The full `q0*C` convolution is serialized similarly.

The raw alphabets agree by name.  D4R1 has all 400 leaves; D5G's ring also
retains all 400, although only 398 occur in the determinant expressions.
The two exact determinant-kernel slots are

```text
f_0_0: weight i=8, killed by (i-8)=0,
g_0_0: weight j=12, killed by (12-j)=0.
```

They remain legitimate local-coordinate inputs; their absence from `D` is a
mathematical kernel, not an alphabet mismatch.

The factor map is exactly

```text
C[X] -> C[c]/(c^8-1)
     -> product over X-1, X+1, X^2+1, X^4+1.
```

The verifier checks the tagged factors multiply to `H`, their order and IDs
match D4R1, and the deck/orientation are
`ORIENTED_PLUS_H`, `u=H mod t`.

## 2. Independent naturality proof

The bridge proof is a five-line identity in the free commutative differential
polynomial ring.  Write derivatives at fixed local `u` as `U_t,G_t` and
allow an arbitrary coordinate drift `u_t`.  From

```text
F=U+u^2,
F_X=2u*u_X,
F_t|X=U_t+2u*u_t,
G_X=G_u*u_X,
G_t|X=G_t+G_u*u_t,
```

direct expansion of

```text
E=12F_XG-8FG_X-t(F_XG_t-F_tG_X)
```

gives

```text
E=u_X*(24uG-8(U+u^2)G_u-t(2uG_t-U_tG_u)).            (2.1)
```

The two `u_t` terms cancel exactly.  Setting `u=0` gives

```text
E|_(u=0)=u_X*G_u*(tU_t-8U).                          (2.2)
```

The verifier expands both sides as sparse free-ring polynomials and checks
literal equality.  D4R1 identifies `u_X=q0`, `G_u=V` on the critical
section, while D5G identifies `sum D_n t^n` with the same raw-coordinate
`E`.  Applying `ev_xi` proves (0.1).  Thus the bridge uses the reviewed
meanings of the D4R1 outputs, not an alias or a numerical specialization.

## 3. Generic weight 22 and the lower-row gate

Before imposing equations, substitution by `X=c+s(t)` mixes lower rows into
weight 22.  Formula (0.2) is the honest generic comparison.  `RESULT.json`
pins each component of `K22` to both a direct-row digest and the required
shift coefficient.

The lower ideal is

```text
I_<22=(all X-coefficient polynomials of D0,...,D21) in C.
```

The exact census is:

```text
22 rows enumerated,
D0 identically zero,
D1,...,D21 nonzero generically,
608 coefficient generators,
31,357 source terms.
```

Every generator has its own digest and a pointer into the frozen D5G direct
artifact.  D5N performs only the formal base change `C -> C/I_<22`; it does
not claim this quotient has a field point or corresponds to a raw Keller
object.

In that quotient, the left side of (0.1) vanishes below weight 22.  Since
`q0_0=H'(c)=8c^7` is a unit, triangular coefficient comparison forces

```text
C0=...=C21=0.
```

The weight-22 coefficient is therefore `H'(c)C22`, proving (0.3).  The
load-bearing negative fixture is

```text
D21=X, s=t:
t^21 D21(c+s)=c*t^21+t^22.
```

It contributes one to the endpoint coefficient and is rejected by the
simplified bridge.  This is why local endpoint comparison cannot run while
any lower row remains live.

## 4. Remainder and global `H`-multiple custody

The verifier independently replays D5G's monic division in `C[X]`:

```text
D22=H*Q22+R22, deg_X R22<8.
```

The frozen counts are

```text
D22: 778 terms,
Q22: 523 terms,
R22: 778 terms.
```

Reduction `X->c` kills `H*Q22`, so local/factor data recover `R22(c)` and
nothing more.  CRT is injective on the degree-`<8` representative, which
recovers `R22`, but no CRT operation recovers `Q22`.

The exact mutation

```text
D22 -> D22+H
```

leaves `D22(c)`, every tagged factor value, and `R22` unchanged while
replacing `Q22` by `Q22+1`.  D5N replays this mutation and explicitly rejects
a target verdict from local data alone.  Monicity makes (0.4) equivalent to
the global identity `D22=1`, even over the lower quotient.

## 5. Custody and replay

D5N pins the reviewed D4R1 producer and Fable5 review, the reviewed D5G
producer and independent audit, the D3 raw source, and the held D5 design.
It mutates none of them.

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_d4r1_d5g_local_naturality_bridge_d5n_20260827/verify_d5n.py \
  --check \
  cases/ggv_8_28_d4r1_d5g_local_naturality_bridge_d5n_20260827/RESULT.json
```

## Scope firewall

D5N proves an exact typed raw/local naturality bridge, a complete
coefficientwise lower-row gate, the generic lower-shift correction, and
continued custody of the global `H`-multiple.  It does not solve the lower
gate, prove its quotient proper, impose `R22=1` or `Q22=0`, construct a
Keller specialization, establish GGV landing, exclude the `8_28` face or
family, prove `G2-PSC`, `G2-BD`, construct a counterexample, or resolve JC2.
