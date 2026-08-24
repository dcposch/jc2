# `K3-LOCAL-PREFLIGHT-20260824`

- Status: **FROZEN — `COMPILER-READY/HEAVY`**
- Role: reserve W, known-negative degree-three verticality/instrument gate
- Producer/model: OpenAI Codex, GPT-5 family
- Basis: `dd11599b07eb05591b5c006791005eef19457d8e`
- Frozen synthesis:
  `xmodel/ideation-20260824T0453Z-synthesis.md`
- Synthesis SHA-256:
  `76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790`
- Execution: one exact stdlib tangent/first-obstruction calculation; no
  localized standard basis, `W_3`, `D=4`, seed/prime sweep, fleet, browser,
  or shared-ledger edit

## Verdict

The full normalized degree-at-most-three coefficient scheme and its local
prime at the promoted `F_3` Artin--Schreier point are now frozen in a
replayable compiler.  The mod-3 seed and promoted mod-9 lift both pass.  The
exact tangent map has rank six and a ten-dimensional kernel.  The divided
first obstruction is zero in the cokernel, with the independently promoted
correction `B=x^2y`.

The preregistered standard-basis gate required at most eight residual local
parameters and at most eight zero-linear-part equations.  The exact output is
ten parameters and nine such equations.  Therefore no Gröbner, saturation,
or local standard-basis run was licensed.

The stop verdict is exactly

```text
COMPILER-READY/HEAVY.
```

This is not a verticality certificate.  In particular, the report does not
claim `Ohat[1/3]=0`; established characteristic-zero low-degree results are
the reason this is a known-negative instrument gate, not a substitute for the
required local ideal identity.

## 1. Frozen coefficient scheme

Begin with arbitrary polynomials `P,Q` of total degree at most three over
`Z`.  Fix the two distinct source sections and translate their common target
value to zero:

```text
P(0,0)=P(1,0)=Q(0,0)=Q(1,0)=0.
```

The four exact linear eliminations are

```text
p00=q00=0,
p30=-p10-p20,
q30=-q10-q20.
```

Thus

```text
P = p10*x+p01*y+p20*x^2+p11*x*y+p02*y^2
    -(p10+p20)*x^3+p21*x^2*y+p12*x*y^2+p03*y^3,

Q = q10*x+q01*y+q20*x^2+q11*x*y+q02*y^2
    -(q10+q20)*x^3+q21*x^2*y+q12*x*y^2+q03*y^3.
```

Let

```text
C = Z[p10,p01,p20,p11,p02,p21,p12,p03,
      q10,q01,q20,q11,q02,q21,q12,q03].
```

For every monomial `x^i y^j` of total degree at most four, let `E_ij` be its
coefficient in

```text
P_x Q_y-P_y Q_x-1.
```

The normalized marked-collision scheme is

```text
Z_3^coll = Spec(C/I),      I=(E_ij : i+j<=4).
```

There are sixteen variables, fifteen equations, 73 nonzero integer terms in
the compiled equations, and at most eight terms in one equation.  The
artifact prints every coefficient equation in a canonical sparse format.

The promoted special point is

```text
s: p10=1, q01=1, all other variables=0 over F_3,
```

corresponding to `(P,Q)=(x-x^3,y)`.  The exact local prime is

```text
m_s=(3,p10-1,q01-1,
     p01,p20,p11,p02,p21,p12,p03,
     q10,q20,q11,q02,q21,q12,q03).
```

The target local object is

```text
Ohat = completion((C/I)_(m_s)).
```

No support restriction beyond total degree three is imposed.

## 2. Exact control replay

### 2.1 Special fibre

At `s`, the fifteen integer equation values are zero except

```text
E_20=-3.
```

They therefore all vanish modulo three.  The fixed points `(0,0)` and
`(1,0)` map to zero by construction.  This replays the promoted degree-three
Artin--Schreier Keller collision over `F_3`.

### 2.2 First Witt lift

The exact-collision integer representative of the special point is

```text
P#=x-x^3, Q#=y.
```

The registered correction gives

```text
P_2=x-x^3,
Q_2=y+3x^2y,
J(P_2,Q_2)=(1-3x^2)(1+3x^2)=1-9x^4.
```

Hence all fifteen equations vanish modulo nine and the marked collision
persists.  This is the same normalized coefficient point as the promoted
Teichmuller representative

```text
P_2'=x+8x^3,
Q_2'=y+3x^2y,
J(P_2',Q_2')=1+27x^2+72x^4,
```

because `8=-1 mod 9`.  The compiler independently checks both determinant
expansions and the two marked images.

## 3. Tangent and first-obstruction map

Let `(A,B)` be a degree-at-most-three coefficient variation satisfying the
four collision linearizations already built into the normalized variables.
At the special fibre,

```text
D J_s(A,B)=[A,y]+[x-x^3,B]=A_x+B_y       over F_3.
```

In the ordered Jacobian rows

```text
1,x,y,x^2,xy,y^2,x^3,x^2y,xy^2,y^3,x^4,x^3y,x^2y^2,xy^3,y^4,
```

the six nonzero tangent equations are

```text
delta p10 + delta q01 = 0,
2 delta p20 + delta q11 = 0,
delta p11 + 2 delta q02 = 0,
delta q21 = 0,
2 delta p21 + 2 delta q12 = 0,
delta p12 = 0.
```

All nine higher rows have zero linear part.  Exact row reduction over `F_3`
therefore gives

```text
rank(D Phi_s)=6,
dim(T_s Z_3^coll)=16-6=10.
```

One pivot choice is

```text
p10,p20,p11,p21,p12,q21,
```

with free columns

```text
p01,p02,p03,q10,q01,q20,q11,q02,q12,q03.
```

The full `15 x 16` matrix and a ten-vector kernel basis are emitted by the
artifact.

For the integer center `(P#,Q#)`, the divided equation error modulo three is

```text
E=(J(P#,Q#)-1)/3 = -x^2 = 2x^2.
```

The first lifting equation is

```text
D Phi_s(A,B)=-E=x^2.
```

Taking `A=0`, `B=x^2y` gives `B_y=x^2`; hence the obstruction class in
`coker(D Phi_s)` is exactly zero.  The solver and the preregistered witness
independently return the same single-coordinate solution `delta q21=1`.
This explains the mod-9 survivor without making any statement about a lift to
the next precision.

## 4. Localized certificate estimate and exact stop

A valid negative output would have to print

```text
g*3^N = sum_(i+j<=4) H_ij E_ij,       g notin m_s.       (4.1)
```

Then `g` is a unit in the local ring and (4.1) proves `3^N=0`; conversely,
zero generic fibre guarantees some identity of this form.  Failure to find a
lift or a Gröbner timeout proves nothing.

The mod-9 point already implies that no certificate with `N=1` can exist:
under the map to `Z/9`, a factor `g notin m_s` maps to a unit, while `3g` is
nonzero.  The first possible exponent is therefore `N>=2`.

After all exact collision eliminations, the local system still has:

```text
16 variables,
6 unit-linear pivots,
10 residual tangent parameters,
9 equations with zero linear part.
```

This fails both preregistered Stage-B bounds (`10>8` parameters and `9>8`
residual equations).  More importantly, the required computation is
mixed-characteristic and must retain transformation data, not merely produce
a reduced basis over `Q` or `F_3`.  A future compiler has two honest options:

1. a local standard basis over `Z_(3)` at `m_s`, retaining the representation
   matrix for (4.1); or
2. a global characteristic-zero unit-ideal computation with transformation
   data, followed by denominator clearing.  An integer identity
   `m=sum H_ij E_ij`, with `m=3^N g` and `3 not-divides g`, would yield (4.1).

Neither was run.  The ten-dimensional singular tangent and an already
surviving first obstruction make a small untracked Gröbner attempt an
unjustified substitute for that compiler.  The exact stop is therefore
`COMPILER-READY/HEAVY`, not `VERTICAL-CERTIFICATE`.

## 5. Artifact and hash record

| Artifact | SHA-256 | Role |
|---|---|---|
| `cases/k3_local_preflight_20260824/PREREGISTRATION.md` | `bf55181156e906f1cbc6081fd688f278ce0bd05b595ff52755e7f5b636adcf9c` | frozen scheme, cap, verdicts, Stage-B gate |
| `cases/k3_local_preflight_20260824/preflight.py` | `99b9aa535a1396f373ccb6f3765f708b88bd2252fee5c794e4336ebb56dbd7f4` | exact sparse compiler, controls, tangent/obstruction |
| canonical stdout of `preflight.py` | `64704d211aad05766f4f75b39f44e66c1370ca718495a45d3387917c5e9c8a40` | full equations, matrix, kernel, controls |
| `cases/k3_local_preflight_20260824/result.json` | `c9c1201b46231b55b79ccde1bd50bfaeafa7d1dc7720a2a9ecd05168f7f0900f` | concise frozen result |

Replay:

```text
python3 cases/k3_local_preflight_20260824/preflight.py
```

The replay completes in about `0.1 s` on the local host.  JSON validation and
a second replay passed.  No descendant is launched and no mathematical claim
is promoted.
