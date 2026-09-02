# A2-DEV-PROJECTION — corrected reissue, wall projection, and T4 repair

Lane: `A2-DEV-PROJECTION`. Date: 2026-09-02. Agent: sol56.

This report makes no exit-price assertion. It edits no canonical ledger and
uses no `jc2-lean` source. The only workspace outputs are this report and the
source-first generator
`xmodel/a2-dev-projection-sol56-20260902.py`.

## 0. Custody and verdict

Before inspection, `shasum -a 256` on the frozen lane inputs returned exactly

```text
e8eb9d77d82b89405b052b703fab2f74de57b9775d3a8376be96a35c95a48345  a2-ubound-opus5-20260902.md
68c4802f4c4909389eea13bae09c75f744a5c4cbde0a9db76b7237c3b03f20b5  a2-e2-p0-gate-gpt55-20260902.md
86caf003268ddc40143daa68d439079dbd82d1dac41e1da93f33a661d52f96ac  cell-32-spec-sol56-20260901.md
d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b  cell-32-termination-opus5-20260901.md
717134c733adc17b3b70409b018858fb1311c37608a24f0eebe65ae79aec8b11  ideation-20260902T0741Z-sol56.md
```

All citations below name those frozen basenames and line numbers. The final
calls are:

```text
REISSUE                 COMPLETE. Seven source coefficients exact-diff to the
                        canonical corrected rows. EQ2_even contains -2qE1.

T1                      RE-DERIVED, unchanged and wall-free.
T2                      REPAIRED. The final G' sign is negative in the bracket.
O1s / DET-EO            RE-DERIVED and machine checked.

DEV-PROJECTION e=1,2,3  DECLARED CAPPED BRANCH-(A) IDEALS ARE UNIT:
                        I_e=(1), hence J_e=I_e intersect Q[c]=(1).
                        There are no c candidates and no finite-U boxes to list.

c=0, e=1,2,3            SEPARATELY TWO-ENGINE EMPTY for the declared capped
                        simultaneous-top subsystem in Chamber III.
c=-(2e+1), Wall A       SEPARATELY DECLARED; each lies in the unit capped branch
                        for e=1,2,3 and is therefore empty there.
c=-2e                   OPEN globally: the 4e-1 deviation cap is unlicensed.
OPEN[A2-K2E]            Closed only inside the decided e<=3 branches; remains
                        OPEN on c=-2e, Chamber I, and uncomputed e>=4.
Chamber I               OPEN; requires fixed-(e,g) jobs with the 2g-1 cap.

T4                      RESTORED by a new corrected proof. The live e=0 section
                        is empty; the old zero determinant is not used.
```

The main result is deliberately local in `e` and scope: it concerns the live,
simultaneous-top, branch-(A) necessary subsystem for which the deviation cap is
licensed. It does not empty an entire chamber, pin one global value of `c`,
prove all-degree A2 emptiness, or supply geometric attainment.

## 1. Canonical corrected section 1

Work in `C[Z]` in characteristic zero. A prime below means `d/dZ`, never a
label and never `d/dV`. Put `deg(0)=-infinity`. Let

```text
a,b,c5,kappa in C,       a*b*kappa != 0,
eta,s,p,C1,q,r,G in C[Z], eta != 0.
```

The names `E1,E2,D1,D2,C1,C2` always denote coefficient polynomials. In
particular, throughout this report

```text
E2 = b Z eta^2
```

and the equation at even `A`-degree two is always `EQ2_even`. Define

```text
E2 = b Z eta^2,                         D2 = a Z eta^3,
C2 = Z eta(3a s+c5 eta)/(2b),           E1 = E2' + G,
D1 = D2' + (3a/(2b)) eta G,

P  = p + A C1 + A^2 C2,                 Q  = q + A D1 + A^2 D2,
R0 = r + A E1 + A^2 E2,                 S0 = s,
H  = A + A^2 Z,                          chi = 2 + 4AZ.
```

For polynomials in `(A,Z)`, set

```text
J(X,Y)  = X_A Y_Z-X_Z Y_A,
WA(X,Y) = X_A Y-X Y_A,
WZ(X,Y) = X_Z Y-X Y_Z,

Even = 2A^2(P_A S0-Q (R0)_A)
       +4H(J(P,S0)+J(Q,R0))
       +chi(Q (R0)_Z-P_Z S0),

Odd  = 2A^2 WA(Q,S0)+4J(P,R0)+4H J(Q,S0)-chi WZ(Q,S0).
```

These are SPEC's own definitions (`cell-32-spec-sol56-20260901.md:35-80`).
Direct coefficient extraction, not transcription from SPEC's old row list,
gives the following canonical replacement block.

```text
O0:
  4(C1 r' - p' E1) + 2(q s' - q' s) = 0.

O1:
  8(C2 r' - p' E2)
  + 4(C1 E1' - C1' E1)
  + 6D1 s' - 2D1' s
  + 4Z(q s' - q' s) = 0.

O2:
  4(C1 E2' - 2C1' E2 + 2C2 E1' - C2' E1)
  + 10D2 s' - 2D2' s + 2D1 s
  + 8Z D1 s' - 4Z D1' s = 0.

E0:
  2(q r' - p' s) - kappa = 0.

EQ1_even:
  6D1 r' - 4q' E1 + 2q E1'
  + 4C1 s' - 2C1' s
  + 4Z(q r' - p' s) = 0.

EQ2_even:
  10D2 r' - 8q' E2 + 2q E2'
  + 6D1 E1' - 4D1' E1
  + 2C1 s + 8C2 s' - 2C2' s
  + 8Z D1 r'
  + 4Z(q E1' - q' E1 + C1 s' - C1' s)
  - 2q E1 = 0.

EQ3_even:
  4C2 s - 4q E2 - 2D1 E1
  + 6D1 E2' - 8D1' E2
  + 10D2 E1' - 4D2' E1
  + Z(8C2 s' - 4C2' s - 8q' E2 + 4q E2'
      + 8D1 E1' - 4D1' E1 + 12D2 r') = 0.
```

The exact source map is

```text
[A^0,A^1,A^2] Odd  -> [O0,O1,O2],
[A^0] Even-kappa   -> E0,
[A^1,A^2,A^3] Even -> [EQ1_even,EQ2_even,EQ3_even].
```

More strongly, as whole polynomial identities,

```text
Odd  = O0 + A O1 + A^2 O2,
Even = kappa + E0 + A EQ1_even + A^2 EQ2_even + A^3 EQ3_even.
```

Thus `[A^3]Odd=[A^4]Even=[A^5]Even=0` after the structural definitions.
The old SPEC display differs only at degree two:

```text
[A^2]Even = SPEC_EQ2_even_old - 2qE1,
E1=(bZeta^2)' + G.
```

This reproduces the charged gate (`a2-e2-p0-gate-gpt55-20260902.md:30-68`)
and identifies the dropped term inside
`2A^2(P_A S0-Q(R0)_A)` (`a2-ubound-opus5-20260902.md:95-150`).

## 2. Reissued T1, corrected T2, and the p-prime-free rows

The live target shear permits `c5=0` without imposing a wall
(`cell-32-termination-opus5-20260901.md:84-97`). Put

```text
d = 3a/(2b),       psi=(Z eta)',
M(W)  = 2Z eta W' - eta W - 4Z eta' W,
M2(W) = 2Z eta W' - eta W - 2Z eta' W.
```

Writing `C1=d h` and `h0=psi s`, direct expansion of the canonical `O2` gives

```text
O2 = -6a eta M2(h-h0) + (3a/b) M(sG).
```

Both Euler operators are injective on `C[Z]`: a nonzero degree-`k` input has
top multipliers `2k-1-4e` and `2k-1-2e`, respectively, which are odd and
nonzero. Also

```text
M(sG) = 2b eta M2(sG/(2b eta)).
```

The comparison is in `C(Z)`, so polynomial injectivity alone is not enough.
For a rational kernel element write `W=eta v`. Then

```text
M2(W)=eta^2(2Z v'-v).
```

If nonzero `v in C(Z)` has integral `Z`-valuation `m`, the lowest Laurent
coefficient of `2Zv'-v` is multiplied by `2m-1`, never zero. Thus the rational
kernel is also zero. It follows that the unique rational candidate for `C1`
is polynomial exactly when `eta | sG`.

Consequently the wall-free form of T1 is

```text
eta | sG,
C1 = d[(Z eta)'s + sG/(2b eta)].                         (T1)
```

This is the source derivation at
`cell-32-termination-opus5-20260901.md:127-185`; it never consumes
`EQ2_even`.

For T2 define

```text
Xi = 12ab eta^3 eta'(eta'+2Z eta'')
   + 4d s(eta s'-eta' s)
   + 8b eta(q eta'-q' eta)
   + 12a eta^3 r'
   + 12a eta[(eta eta''-eta'^2)G + eta eta' G'].
```

Exact collection of the canonical `EQ3_even` gives the repaired identity

```text
EQ3_even = Z^2 Xi
 - (3a/b)[eta G^2 + 2Z eta' G^2 - 2Z eta G G'],

Z^2 Xi = (3a/b)[eta G^2 + 2Z eta' G^2 - 2Z eta G G'].    (T2)
```

The final sign is negative. The bracket is not
`(Z eta^2 G^2)'/eta`; their difference is `-4Z eta G G'`. The regression
`a=b=1, eta=Z, G=Z^2, s=q=r=0` gives `27Z^5` from the source and the corrected
form, versus `3Z^5` from the retired derivative form
(`a2-e2-p0-gate-gpt55-20260902.md:108-125`).

Multiplying `O1` by `s` and eliminating `p's` using `E0` gives

```text
O1s = 8s C2 r' - 8E2(qr'-kappa/2)
    + 4s(C1 E1'-C1' E1)
    + 6D1 s s' - 2D1' s^2
    + 4Zs(qs'-q's) = 0,

O1s = s O1 - 4E2 E0                                      (identity).
```

Thus no division by `s` occurs in the generator; equivalence with `O1` is
asserted only later on the live `s!=0` section. This is the p-prime-free row
requested in `a2-ubound-opus5-20260902.md:257-283`.

For the determinant checksum put

```text
W = q s'-q's,
T = -(C1 E1'-C1' E1)/2 - 3D1 s'/4 + D1' s/4 - ZW/2,

DET_EO = (sC1-qE1)T + (W/2)(sC2-qE2)
       + (kappa/2)(E1C2-C1E2).
```

This is exactly the augmented determinant of the three affine rows in
`(r',p')`, so `E0=O0=O1=0` implies `DET_EO=0`. The generator exact-diffs its
determinantal syzygy. It is a checksum, not an additional ideal generator, as
required by `ideation-20260902T0741Z-sol56.md:163-217`.

## 3. Machine-readable source generator and controls

The accompanying Python file builds `Even` and `Odd` first, extracts each
requested exponent with `Poly(...).nth(j)`, and only then compares with the
canonical rows. Its normalizer is exact `cancel(together(expand(...)))` over
SymPy 1.14.0. Run

```text
python3 xmodel/a2-dev-projection-sol56-20260902.py check
python3 xmodel/a2-dev-projection-sol56-20260902.py system --format json
```

The checked generator's SHA-256 is
`f4945ca9bb57555d8101705d6aee6d167bacac4faf6d8e4d0e8bbe62fd748797`.

The check reports `PASS` for all seven source images, both whole-polynomial
reconstructions, the three forbidden higher coefficients, T1, corrected T2,
`O1s`, `DET_EO`, and all three deviation clearings. Its stale-source canary is

```text
actual [A^2]Even - SPEC_EQ2_even_old = -2q[(bZeta^2)'+G] != 0.
```

The planted raw source-identity control, after dropping the live `kappa!=0`
open, is

```text
a=b=1, eta=s=Z, G=-2Z^2, c5=kappa=0,
p=0, C1=(3/2)Z^2, q=(3/4)Z, r=1/4,
C2=(3/2)Z^3, D1=Z^3, D2=Z^4, E1=Z^2, E2=Z^3.
```

It gives source `Even=Odd=0` exactly. Because `kappa=0`, it is not a point of
the live corrected system; it is typed only

```text
artifact=SUBSYSTEM_POINT
attainment=NECESSARY
```

At that point `X=Y=0`, and all three reconstruction tests hold pointwise:

```text
eta^2 | s^2+X,       eta | 3a s^2+Y,
s | qr'-kappa/2,     quotients 1, 3Z, 0;     p'=0.
```

This positive control proves that the source encoder accepts a planted point
of the corrected source identities; it is not an attainment witness. A second
control exercises
the actual `msolveio -> qqideal -> msolve` path on the corrected s-free
subsystem:

```text
g=Z, K=1/12, x=7+Z/6, y=1/2+Z/3, tt=12.
```

It makes the corrected normalized `F1,F2,F3` and `gamma*K*tt-1` vanish. The
checked-in `control` subcommand adds shifted coordinate generators for this
point; `qqideal` returns `NONEMPTY, dim=0, degree=1`, and SymPy returns the
seven coordinate pins rather than `[1]`. The strict payload hash is

```text
d79e1e075a4e48e2e6e49752c212433ae27829d58ce16d73a255cd8cb2fbbeb2
```

This control stops before `F4` and the square/reconstruction stage, so it too is
typed only `artifact=SUBSYSTEM_POINT`, `attainment=NECESSARY`; it is not a
reconstruction candidate. The preceding raw source control is the one for
which all three divisibility remainders are computed and zero.

## 4. Corrected deviation system

Set

```text
X = 4b eta^2 r-s^2,       Y = 4b^2 eta q-3a s^2,
N(W) = eta W'-2W eta'.
```

After T1 and `E0`, substitute

```text
r=(s^2+X)/(4b eta^2),       q=(3a s^2+Y)/(4b^2 eta).
```

The following three polynomial clearings exact-diff to the canonical source
rows:

```text
F1 = 4b^2 eta^2 EQ1_even,
F2 = 2b^2 eta^2 EQ2_even,
F3 = b EQ3_even.
```

They contain no `s` or any derivative of `s`. Explicitly, with

```text
V = 2Zb eta^2 eta'' - 2Zb eta eta'^2 + 2b eta^2 eta'
  - 2G eta' + eta G',
```

one has

```text
F1 = 8Zb^2 kappa eta^2
   + 3a(3E1-b eta^2)N(X) - 4E1 N(Y) + 2VY.
```

For a compact complete display of `F2`, put

```text
AX = 3aZ(4Zb eta eta' + 3b eta^2 + 2G),
AY = -2Z(2Zb eta eta' + 3b eta^2 + G),
W2 = 4Z^2b eta^2 eta'' + 2Zb eta^2 eta'
   - 2ZG eta' + 2Z eta G' - G eta,

Psi2 = 6ab eta^2[
    4Z^2b^2 eta^3 eta' eta'' - 4Z^2b^2 eta^2(eta')^3
  + 4Zb^2 eta^3(eta')^2 + 2ZbG eta^2 eta''
  - 6ZbG eta(eta')^2 + 2Zb eta^2 G' eta'
  + 2bG eta^2 eta' - 2G^2 eta' + G eta G'].

F2 = AX N(X) + AY N(Y) + W2 Y + Psi2.
```

Finally set

```text
Xi0 = 12ab eta^3 eta'(eta'+2Z eta'')
    + 12a eta[(eta eta''-(eta')^2)G + eta eta'G'],
Kminus = eta G^2 + 2Z eta'G^2 - 2Z eta G G'.
```

Then the corrected third row is

```text
F3 = bZ^2 Xi0 + Z^2[3aN(X)-2N(Y)] - 3a Kminus.
```

This re-confirms DEV-FREE at the scope stated in
`a2-e2-p0-gate-gpt55-20260902.md:249-301`. Notice that `b EQ3_even`, not the
retired derivative-form normalization, is the polynomial source clearing.

## 5. The coefficient ideals and exact projection

On the charged live, simultaneous-top branch (A), for `e>=1` specialize
`a=b=eta_e=1`, `c5=0`, and in Chamber II write

```text
eta = Z^e + sum(eta_j Z^j, 0<=j<e),
G   = c Z^(2e) + sum(G_j Z^j, 0<=j<2e),
X   = sum(X_j Z^j, 0<=j<4e),
Y   = sum(Y_j Z^j, 0<=j<4e).
```

The cap `deg X,deg Y<=4e-1` is licensed in this scope in Chamber II only when
`c!=-2e`, and in Chamber III unconditionally
(`a2-e2-p0-gate-gpt55-20260902.md:280-301`). The coefficient ideal below is a
necessary s-free subsystem in that scope, not a presentation of every point in
the named chamber.
The declared rational ring is exactly

```text
Q[eta_0..eta_(e-1), G_0..G_(2e-1), X_0..X_(4e-1),
  Y_0..Y_(4e-1), kappa, tt, c],
```

with all variables except `c` in the first elimination block and `c` last.
The adapter-safe map removes underscores only:

```text
eta_j -> etaj, G_j -> Gj, X_j -> Xj, Y_j -> Yj;
kappa -> kappa, tt -> tt, c -> c.
```

Every image and the complete ordered generator list are emitted before a
solver call. The ideal `I_e` is generated by every `Z` coefficient of
`F1,F2,F3` and the explicit Rabinowitsch row

```text
kappa*c*(c+2e)*tt - 1 = 0.
```

No `sat()` or saturation wrapper occurs. The generator expands this row to
parser-safe monomials before `msolveio` emission.

### 5.1 Main results

The exact job census is

| `e` | variables | generators | `Z` degrees `(F1,F2,F3)` | block eliminant `J_e` |
|---:|---:|---:|---:|---|
| 1 | 14 | 20 | `(5,6,5)` | `(1)` |
| 2 | 25 | 39 | `(12,13,10)` | `(1)` |
| 3 | 36 | 58 | `(19,20,15)` | `(1)` |

For each row, direct msolve block elimination with `-e nvars-1 -g 2` prints the
one-element basis `[1]` in the remaining `c` block. The full explicit ideal
also has basis `[1]` through `qqideal 0.2.0`/`msolveio 0.2.1` calling msolve
0.10.1. Independent SymPy 1.14.0 over literal domain `QQ`, grevlex and the same
ordered generators returns `[1]` in approximately `0.10`, `2.08`, and `18.13`
seconds. Thus this is a two-engine characteristic-zero decision, not a modular
EMPTY promoted by itself.

The strict payload hashes emitted by the checked-in generator are

```text
e=1  fda311032b3d7e17c5a9f982f4e6ebdda1660bee74835663c8c5a1ee334ffde2
e=2  f490f75701ad6dfe58c9bf4805c37cafd70b2e0c6418d287231091e95d067694
e=3  d44b3c635ec4c60850597fec5cff1cf89b6a8ecdcedb183124a027686ccde1fe
```

Therefore

```text
1 in I_e,       J_e=I_e intersect Q[c]=(1),       e=1,2,3.
```

The declared capped branch-(A) subsystem is empty. This is the first outcome
on Card 1, so
there are no roots of a nonconstant eliminant to list and no branch-(A)
finite-`U` boxes: the finite box is the empty set for each of `e=1,2,3` in the
main scope. Nothing is handed to `EQ4/O1s`.

### 5.2 Parser negative control

The literal parenthesized string

```text
kappa*c*(c+2)*tt-1
```

must never be sent directly to msolve 0.10.1. In a deliberate `e=1` negative
control, msolve reported zero invalid rows but block elimination emitted
`(c+2)^3`; that is a parser artefact, not a wall pin. `msolveio 0.2.1` rejects
the parentheses, while the expanded row

```text
c^2*kappa*tt + 2c*kappa*tt - 1
```

returns `[1]`. This is exactly the variable/ring-map and explicit-
Rabinowitsch guardrail in FALLACY-v2; the spurious nonconstant eliminant is not
consumed.

## 6. Required branch ledger

The unit main ideal does not license merging exceptional scopes. The branch
ledger is:

| branch | `e=1,2,3` status | reason / next action |
|---|---|---|
| Chamber-II branch (A), `c*kappa*(c+2e)!=0` | `EMPTY` | Declared capped s-free necessary subsystem; main two-engine unit ideal. |
| `c=-(2e+1)` branch-(A) stratum | `EMPTY`, separately declared | It is nonzero and distinct from `-2e`, hence a specialization of the main unit capped subsystem; no retired wall is imposed. |
| Wall A, `3c+6e+2=0`, branch (A) | `EMPTY`, separately declared | Also lies in the main open for `e>=1`; the conclusion comes from the unit ideal, not the old Wall-A determinant. |
| `k=2e` inside the preceding capped scope | `EMPTY`, separately declared | The coefficient ideal did not remove or divide by `(k-2e)`; its unit basis kills this stratum within the declared scope. |
| `c=0` (Chamber III) | `EMPTY`, separately computed | Declared capped simultaneous-top subsystem only. Substitute `c=0`, remove `c`, and use `kappa*tt-1`; msolve and SymPy both give `[1]`. |
| `c=-2e` | `OPEN[A2-CMINUS2E]` | A2-DEV-BOUND does not license the `4e-1` cap. A capped probe is not a branch decision. |
| Chamber I, `g>2e` | `OPEN[A2-CHAMBER-I]` | Generate fixed `(e,g)` jobs with `deg X,deg Y<=2g-1` and an explicit row `kappa*G_g*tt-1`; no global `g` cap is known. |
| `e>=4` | `OPEN[A2-DEVBOX-EGE4]` | Same safe generator; launch per `e`, preserving the exceptional splits. |

For the separately licensed `c=0` computations, the strict payload hashes are

```text
e=1  c40340613126b1b1862804d7df5e575514abbdbe8185b602be3123f799c9b407
e=2  301ac9f1268161e795fe930c170184d70fead52f23ed18bfbbb2907baf91d77b
e=3  77da3c2bc2c62342c3fe5eb8bfa8f662045c38442ac170a991f206ce89abed52
```

SymPy's `c=0` checks took about `0.12`, `4.95`, and `58.92` seconds. Fresh
`/usr/bin/time -l` repeats of the largest `e=3` main and `c=0` SymPy jobs used
`99,926,016` and `97,517,568` bytes maximum RSS, respectively (about 100 MB),
and completed in `21.68` and `60.04` seconds. Thus the decided main and `c=0`
jobs are below both desk-scale limits. A coordinator job for `c=-2e` must
first prove a replacement degree cap or introduce an honest increasing cap and
return only capped evidence; it may not reuse the `4e-1` bound. Chamber I jobs
must state `(e,g)` in the job key and use the `2g-1` bound. `box01` is the
appropriate queue for either family.

The global label `OPEN[A2-K2E]` is narrowed, not erased: it is closed for
`e<=3` only in every capped subsystem actually decided above, including `c=0`, but remains
open on `c=-2e`, Chamber I, and `e>=4`. No claim is transported across those
scope boundaries.

## 7. T4 repaired on the corrected `e=0` section

The old T4 proof cannot be repaired by changing one determinant: corrected
`EQ2_even` makes its top determinant zero
(`a2-e2-p0-gate-gpt55-20260902.md:90-105`). The following is a new finite
proof from source rows.

Let `eta=eta_0 in C*` and define nonzero constants

```text
B=b eta_0^2,       tau=3a eta_0/(2b),
K=kappa/(tau B^2).
```

Normalize the variables by

```text
g = G/B,                       h = s^2/(2B^2),
x = X/(2B^2) = 2r/B-h,         y = Y/(6aB^2) = q/(tau B)-h,
i = x'-2y'.
```

The inverse substitutions are

```text
G=Bg,       r=B(x+h)/2,       q=tau B(y+h),
kappa=tau B^2 K.
```

T1 gives

```text
C1=tau s(1+g/2), C2=tau Zs,
E1=B(1+g), E2=BZ,
D1=tau B(2/3+g), D2=(2/3)tau BZ.
```

Direct source extraction yields the exact factorizations

```text
EQ1_even = tau B^2 F1 + 2Z E0,
EQ2_even = 2tau B^2 F2,
EQ3_even = 2tau B^2 F3,
s O0 modulo E0 = 2tau B^3 F4,
```

where

```text
F1 = 2i + 3g x' - 4g y' + 2y g' + 2KZ,
F2 = 3Zi + 2Zg x' - 2Zg y' + (2Zg'-g)y + gg',
F3 = 2Z^2 i - g^2 + 2Zgg',
F4 = ih - yg h' + (1+g)(K-yx').
```

Thus the first row becomes `EQ1_even=tau B^2 F1` on `E0=0`; the discarded
multiple is recorded explicitly. No division by `s` was used in the `F4`
identity. From `F1=0`, using
`i=x'-2y'`, obtain

```text
g x' + 2y g' + 2(1+g)i + 2KZ = 0.                       (A)
```

Subtracting `Z(A)` from `F2=0` gives

```text
g y = gg' + Z(1-g)i - 2KZ^2.                            (B)
```

Equation `F3(0)=0` forces `Z|g`, and

```text
i = g(g-2Zg')/(2Z^2).
```

Putting this into (B) shows

```text
2KZ^2 = g[g' + (1-g)(g-2Zg')/(2Z) - y].
```

The bracket is polynomial because `Z|g`; since `K!=0`, one has `g|Z^2`.
Because the live section has `G!=0`, there are exactly two cases.

If `g=gamma Z^2`, `gamma!=0`, then

```text
i = -(3/2)gamma^2 Z^2,
y = -2K/gamma + (gamma/2)Z + (3gamma^2/2)Z^3.
```

The `Z^1` coefficient of (A) is `-6K`, impossible.

If `g=gamma Z`, then

```text
i = -gamma^2/2,
y = gamma/2 + (gamma^2/2-2K/gamma)Z,
x' = 2K/gamma.
```

The definition `i=x'-2y'` pins `K=gamma^3/12`. Put
`delta=gamma-4K/gamma^2=2gamma/3`. The last row becomes

```text
-(gamma^2/2)[h+Z(1+delta Z)h']
-K delta Z(1+gamma Z)=0.                                (C)
```

Write `s=s_0+s_1Z+...`. The constant coefficient of (C) forces `s_0=0`, so
both the constant and linear coefficients of `h=s^2/(2B^2)` vanish. The
`Z^1` coefficient of (C) is then

```text
-K delta = -gamma^4/18 != 0,
```

a contradiction. This exhausts the corrected live `e=0` section.

As a finite CAS check, the `g=gamma Z^2` stratum reduces to

```text
Q[gamma,K,tt],       <6K, gamma*K*tt-1> = (1).
```

The `g=gamma Z` first-jet ideal is in
`Q[gamma,K,x1,y0,y1,u0,u1,tt]`, with
`u=s/(sqrt(2)B)` and hence `h=u^2`, and generators

```text
2x1-4y1+gamma^2,
2gamma*y0-gamma^2,
2gamma*y1-gamma^3+4K,
gamma*x1-2K,
gamma^2*u0^2,
2gamma^4*u0*u1+K*gamma^3-4K^2,
gamma*K*tt-1.
```

Direct msolve 0.10.1 and SymPy 1.14.0 both return `[1]`. These ideals use
explicit Rabinowitsch variables and merely check the displayed proof. They are
reproducible from the checked-in generator via

```text
python3 xmodel/a2-dev-projection-sol56-20260902.py t4ideal g1 --format msolve
python3 xmodel/a2-dev-projection-sol56-20260902.py t4ideal g2 --format msolve
```

with payload hashes `7378c5461d4e328b60ff3107b00b355c5c7f4f5e6ddfc5b06397e6d3804a1327`
and `985d7c79a7403fb10c9a2bef67fffee37b1b608527bee23192cddf4a16000e53`,
respectively.

Therefore:

```text
THEOREM T4_REPAIRED.
On the fully corrected, wall-free live A2 section over C (after the licensed
c5=0 target shear, with the conclusion transported back),
a*b*kappa != 0, eta != 0, G != 0 implies deg(eta)>=1.
Equivalently EMPTY[G!=0, deg eta=0].
```

There is no surviving `e=0` locus and hence no reconstruction divisibility to
test there. T5's former reliance on T4 for removal of `e=0` is repaired; its
unaffected `e>=1` argument keeps its charged scope.

## 8. Engine custody and state ladder

The default adapter stack was installed only into an isolated temporary
directory because it was absent from the base interpreter:

```text
qqideal 0.2.0
msolveio 0.2.1
msolve 0.10.1
msolve executable SHA-256:
cc992ccc89cefdcff9ea697ecd05fc4fe99cca8592b423d30d9cca0e04a00ea2
SymPy 1.14.0
```

`qqideal` was given an explicit `Ideal` already containing the Rabinowitsch
row; its `.saturate()` method was never called. `msolveio` emitted every parser-
safe payload. SymPy rebuilt the same ordered rational ideals independently.

Execution-budget violation: an exploratory SymPy run on the *unlicensed capped
probe* `e=2,c=-4` had no correctly armed watchdog, exceeded the charged
15-minute limit, and was interrupted after 1463 seconds without a basis. No
statement in this report consumes that run. This is another reason the global
`c=-2e` row remains `OPEN`; any retry is a coordinator job with a hard timeout
and, first, a licensed cap.

The only nonempty objects published here are the two deliberately planted
controls. Both are typed exactly

```text
artifact=SUBSYSTEM_POINT
attainment=NECESSARY
```

No decided DEV locus survives. The open rows in Section 6 are problem scopes,
not points. Nothing in this report is called a curve, a map, or a `(B3)`
object. If a future `c=-2e` or Chamber-I subsystem point appears, it must pass,
pointwise and before any promotion,

```text
eta^2 | s^2+X,
eta   | 3a s^2+Y,
s     | qr'-kappa/2,
```

then reconstruct `r,q,p'`, integrate `p'` polynomially, and pass all seven raw
source rows. Even a resulting `FULL_EO_POINT` would not by itself supply
`ACTUAL_MAP` attainment (`ideation-20260902T0741Z-sol56.md:427-440`).

## 9. FALLACY-v2 audit and handoff

* **Flag/place/series and carrier/attainment.** None is identified with another.
  This lane has coefficient varieties and two synthetic controls only; no exit,
  carrier, cover, or attainment statement is made.
* **Floor versus attainment.** `deg X,deg Y<=4e-1` is consumed only in its
  charged chambers. It is not used on `c=-2e`; the capped probe there is not
  promoted.
* **Explicit Rabinowitsch.** Every open is a displayed equation with `tt`.
  There is no `sat()` wrapper. The parenthesized-parser canary is recorded and
  rejected.
* **Raw degree and vanished leaders.** `c=0`, `c=-2e`, `c=-(2e+1)`, Wall A,
  `k=2e`, and Chamber I are separate ledger rows. Zero polynomials remain
  allowed inside upper-bound boxes.
* **Variable/ring map.** Mathematical and adapter names, coefficient field,
  variable order, specialization, generator count, and payload hash are all
  emitted. Matching names alone are never treated as a coercion.
* **Prime notation.** Every prime is declared to mean `d/dZ`.
* **No unsafe analogy.** The retracted wall and RAY-2 are never imposed. T4 is
  restored by new corrected equations, not by the old determinant.

Coordinator handoff, in order:

```text
1. Review and consume the canonical seven-row block and checked generator.
2. Mark only the declared capped simultaneous-top DEV-PROJECTION branch-(A)
   main and c=0 subsystems EMPTY for e=1,2,3; do not empty whole chambers.
3. Launch no more stale wall cells. For c=-2e, first derive a valid degree cap;
   otherwise return capped evidence only. For Chamber I, key jobs by (e,g).
4. Continue e>=4 only with the same source and parser canaries.
5. Restore C32 T4 and the e=0 dependency of T5; retain every unrelated open.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25621`.
- Body SHA-256:
  `f140a677c1672aa96bd4acc1fe784caa7210fc1816ddd0ac0c00d9a2e685ce14`.
- Frozen basis: `12601209d7e66b2247ff2bc283620e2836af3226`.
