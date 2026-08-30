# D3 Halphen CFS state machine: one constructible survivor

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `7ce5611ffcb382e43976f552f8287c1e1bf4fb89`  
Lifecycle: **EXACT PROVISIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Assume the promoted degree-three Hodge/four-row theorem and the still-
provisional triple-line first-jet gate.  In the index-three Halphen row with
one length-two defect at the triple fibre, the plane ternary cubic has exact
CFS level two while its minimal strictly-henselian-insoluble floor has level
one.  Keep the raw coefficient-base degree-three form

```text
F=x^3+tF1+t^2F2+t^3F3,                                  (0.1)
F1=a x^3+ell x^2y+m x^2z+x(q0 y^2+q1 yz+q2 z^2)+H(y,z).
```

The CFS line-move state machine gives two conclusions.

1. The double-root first-jet branch

```text
H=y^2z,             q2=0
```

is empty.

2. The triple-root branch `H=y^3` is nonempty locally, but collapses to one
explicit constructible family.  Before constant normalization its first jet
satisfies

```text
q2=q1=0,            Q=q0 y^2,
m=3s with s!=0.                                             (0.2)
```

After constant coordinate and coefficient-base rescaling, followed by a
constant shear, one may take

```text
m=3,                ell=0,
q0=0 or 1.                                                   (0.3)
```

The higher raw coefficients then obey two cube equations, one equality and
one principal-open condition displayed in Section 4.  Thus the previous five
Borel first-jet orbits reduce to two shards, but neither shard is eliminated.

There is an exact positive control:

```text
F=(x+t z)^3+t y^3+t^3x^2z.                                 (0.4)
```

It is a normal, generically smooth, raw base-degree-three local ternary cubic
of exact level two whose level-one drop is CFS-critical.  It is not a
dominant-`A2` map, a proof that the global four-row configuration is attained,
or a counterexample to JC2.

## 1. Loaded inputs and scope

The argument uses the following promoted or explicitly provisional inputs.

- The one-point index-three row has plane level exactly two and minimal
  Halphen floor exactly one.
- Its generic torsor is strictly-henselian insoluble.  In residue
  characteristic zero, a minimal insoluble ternary cubic has level one and
  reduction equal to a nonzero cube of a linear form.
- The central plane cubic is `3L`, normalized to `x^3`.
- The first-jet invariant gate leaves only `H=y^2z,q2=0` or `H=y^3`.
- The coefficient-base degree is literally at most three in the raw global
  trivialization.

The CFS facts are Theorem 4.3, Definition 5.1, Lemmas 5.2--5.4 and 5.8, and
Proposition 5.6 of Cremona--Fisher--Stoll, *Minimisation and reduction of
2-, 3- and 4-coverings of elliptic curves* (arXiv:0908.1741).  In particular,
their line move preserves level; for a nonminimal ternary cubic it exposes a
common factor within four iterations; and a critical ternary cubic in residue
characteristic different from three is minimal, insoluble, and level one.

This packet proves a necessary local constructible classification.  It does
not infer a global surface, arc, polynomial map, or JC2 conclusion from a
finite coefficient list.

## 2. The forced three-line cycle

The central reduction is `x^3`, whose singular locus is the line `x=0`.
The CFS line move is forced:

```text
E1=L_x(F)=t^-1 F(tx,y,z).
```

Its reduction is `H`.  Both `y^2z` and `y^3` have singular line `y=0`, so the
second move is again forced:

```text
E2=L_y(E1)=t^-2 F(tx,ty,z).
```

Put

```text
C2=[z^3]F2.
```

Direct coefficient extraction gives

```text
(E2)_0=z^2(q2 x+C2 z).                                    (2.1)
```

If (2.1) is nonzero, its singular locus is exactly `z=0`.  The next forced
line move is

```text
L_z(E2)=t^-3 F(tx,ty,tz)=F,                               (2.2)
```

where the last equality is spatial homogeneity of degree three.  This exact
three-cycle cannot occur here.  The plane model is nonminimal because its
level is two and its minimal floor is one; CFS Theorem 4.3 therefore forces a
common coefficient factor, hence a level drop, within four moves.  Repeating
(2.2) forever would contradict that theorem.

Consequently

```text
q2=0,                 C2=0,                               (2.3)
```

and `E2` is divisible by `t`.  Along this fixed forced path, the resulting
drop is

```text
M=t^-1E2=t^-3F(tx,ty,z).                                  (2.4)
```

It has level one, is minimal and strictly-henselian insoluble, and therefore
`M_0` must be a nonzero cube by CFS Lemma 5.8.

## 3. Double-root death and first triple-root cube

### 3.1 Double-root branch

For `H=y^2z`, the first-jet gate already supplies `q2=0`; (2.3) adds `C2=0`.
Write

```text
R=[xz^2]F2,       U=[yz^2]F2,       C3=[z^3]F3.
```

Then

```text
M_0=x^3+m x^2z+q1 xyz+y^2z+R xz^2+U yz^2+C3 z^3.          (3.1)
```

This is not a cube.  Since its `x^3` coefficient is one, a cube can be
normalized to `(x+alpha y+beta z)^3`.  Its zero `x^2y` coefficient forces
`alpha=0`, after which its `y^2z` coefficient is zero, contradicting the unit
coefficient in (3.1).  This eliminates the entire double-root branch.

### 3.2 Triple-root branch

Take `H=y^3`.  Again (2.3) is forced.  With the same coefficient notation,

```text
M_0=x^3+m x^2z+q1 xyz+R xz^2+U yz^2+C3 z^3.               (3.2)
```

Put `m=3s`.  Comparing (3.2) with `(x+s z)^3` shows that it is a cube exactly
when

```text
q1=U=0,             R=3s^2=m^2/3,
C3=s^3=m^3/27.                                             (3.3)
```

Thus `Q=q0y^2`; the state machine has already reduced the five first-jet
Borel orbits to the zero and nonzero `q0` cases.

## 4. Exact critical flags

After (3.3), `M_0=(x+s z)^3`.  Use `X=x+s z`, so old `x=X-sz`, and perform
the next forced line move along `X=0`.  For the coefficients of `F2`, write

```text
A=[x^3],  B=[y^3],  P=[x^2y],  T=[xy^2],
V=[x^2z], M111=[xyz], Q021=[y^2z].
```

For `F3`, put

```text
V3=[x^2z], M3=[xyz], Q3=[y^2z], R3=[xz^2], U3=[yz^2].
```

The first transverse reduction is

```text
y^3+b y^2z+c yz^2+d z^3,                                  (4.1)

b=Q021-s q0,
c=U3+s^2 ell-s M111,
d=-s^3 a+s^2 V-s R3.
```

It is a cube exactly when

```text
3c=b^2,                    27d=b^3.                       (4.2)
```

Indeed, with `lambda=b/3`, the change `Y=y+lambda z` turns (4.1) into

```text
Y^3+(3c-b^2)/3 Yz^2
   +((27d-b^3)/27-b(3c-b^2)/9)z^3.
```

Assume (4.2) and perform the line move along `Y=0`.  Before cancellation the
final reduction is

```text
z^2(kappa X+theta Y+eta z),
theta=c-2lambda b+3lambda^2.
```

Since `lambda=b/3`, the first equation in (4.2) makes `theta=0`
automatically.  The reduction is therefore

```text
(kappa X+eta z)z^2,                                       (4.3)
```

where

```text
kappa = 3a s^2+2ell s lambda+q0 lambda^2
        -2V s-M111 lambda+R3,

eta = -A s^3-P s^2lambda-T s lambda^2-B lambda^3
      +V3 s^2+M3 s lambda+Q3 lambda^2.                    (4.4)
```

The minimal insoluble model must again have nonzero cube reduction.  Hence
the exact last critical condition is

```text
kappa=0,                    eta!=0.                       (4.5)
```

The nonzero chart is load-bearing.  Equations alone only compute the closure
and include a false boundary.

Conditions (4.2)--(4.5) force `s!=0`.  If `s=0`, then `d=0`; (4.2) gives
`b=lambda=0`; (4.5) first gives `R3=0`, while every term in `eta` vanishes,
contradicting `eta!=0`.

Since `s!=0`, a constant `z`-scaling normalizes `m=3`.  A constant shear
`z -> z-(ell/3)y` then kills `ell` while preserving `H=y^3` and
`Q=q0y^2`.  If `q0!=0`, the local changes

```text
t_old=q0^-3 t,       y_old=q0 y,       z_old=q0^3 z
```

normalize it to one while preserving the three displayed unit coefficients.
This proves (0.3) when a local/base-coordinate rescaling is allowed.  If
other globally marked base data freeze that coordinate, the honest shard is
`q0!=0`, not the literal equation `q0=1`.

## 5. Nonempty local positive control

For (0.4), the forced drop is

```text
M=(x+z)^3+t y^3+t^2x^2z.
```

In the coordinate `X=x+z`, this is

```text
M=X^3+t y^3+t^2(X-z)^2z.                                 (5.1)
```

The coefficient valuations in the CFS monomial order are

```text
X^3:0,  y^3:1,  X^2z:2,  Xz^2:2,  z^3:2,
all other coefficients: infinity.
```

They satisfy Definition 5.1 exactly, including the three exact coefficients
`X^3`, `y^3`, `z^3`; hence `M` is critical and has level one in
characteristic zero.  Reversing the single drop makes (0.4) exact level two.

The local total surface is normal.  Along the generic point of its central
line,

```text
F_t|_(t=x=0)=y^3!=0.
```

The generic cubic is smooth.  The `y` derivative forces `y=0`; a singular
projective point cannot have `z=0`.  Set `z=1`, `x=t(r-1)`.  After removing
units, the `x` and `z` derivatives are

```text
3r^2+2t^2(r-1),          3r^2+t^2(r-1)^2.
```

Their difference is `t^2(r-1)(r-3)`, and neither `r=1` nor `r=3` zeros the
first expression in `C((t))`.  Generic smoothness and regularity at the
generic central-line point leave only a finite singular locus; the Cartier
surface is `S2`, hence normal.

This positive control proves that CFS minimisation plus raw base degree three
cannot by itself kill the Halphen row.  Its bihomogeneous global closure is a
new object to audit, not an already validated four-row surface.

## 6. Executable replay

The exact symbolic replay is

```text
ops/d3_halphen_cfs_state_machine_replay.py
SHA-256 2570d44ec3c31b4b559299099be196dd52b13b7ba1cfe4539043f96fc823ee9c
```

It checks the two forced central forms, the exact three-cycle, the double-root
cube obstruction, both triple-root cube flags, the `s=0` obstruction, and the
normal/generic-smooth critical positive control.  It contains zero Python AST
`assert` nodes.

Run:

```bash
d3cfs_tmp=$(mktemp -d)
python3 ops/d3_halphen_cfs_state_machine_replay.py > "$d3cfs_tmp/ordinary.json"
python3 -O ops/d3_halphen_cfs_state_machine_replay.py > "$d3cfs_tmp/O.json"
python3 -OO ops/d3_halphen_cfs_state_machine_replay.py > "$d3cfs_tmp/OO.json"
cmp "$d3cfs_tmp/ordinary.json" "$d3cfs_tmp/O.json"
cmp "$d3cfs_tmp/ordinary.json" "$d3cfs_tmp/OO.json"
wc -c "$d3cfs_tmp/ordinary.json"
shasum -a 256 "$d3cfs_tmp/ordinary.json"
```

All outputs are byte-identical, 1130 bytes, with SHA-256

```text
52c7b6445a61ae5f518b46aa93d971603b1a0d4d7c1445767c047904c2df701a.
```

The mutation

```text
python3 ops/d3_halphen_cfs_state_machine_replay.py --mutate-cycle-scale
```

exits nonzero with `FAIL:three-line CFS cycle identity failed`.

## 7. Disposition and successor

This packet is provisional until a different-model hostile review checks the
CFS theorem interface, raw-versus-gauged coefficient bookkeeping, constant
normalizations, and positive control.

The cheapest decisive successor is no longer a large invariant ideal.  It is
the intersection of the explicit constructible locus (3.3), (4.2), (4.5)
with genuinely global conditions:

1. homogenize over the full coefficient base and audit every other fibre;
2. impose the promoted length-two Hodge/GR divisor concentrated at `t=0`;
3. test total-space normality and rationality, not just local normality;
4. impose the binding polarization and dominant-rational-`A2` interface;
5. only then use AWS elimination if the two normalized shards survive.

The positive control should be homogenized and audited first.  It may expose
the cheapest missing global obstruction or provide a sharp negative control
for that obstruction.

Firewalls:

- The cycle contradiction uses both exact plane level two and Halphen floor
  one; it is not a conclusion from three formal substitutions alone.
- Minimal strictly-henselian insolubility is what turns each lowered
  reduction into a cube.
- Raw base degree three must be retained; parameter-dependent first-jet
  gauges create determined higher powers and cannot be truncated as free
  coefficients.
- `eta!=0` is an open condition, not an ideal generator.
- The positive control is a local ternary-cubic survivor, not a global
  surface theorem, an arc, a polynomial map, or a proof/disproof of JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12211`.
- Body SHA-256:
  `6389a15fff6ec1ddbb8945676e8c8cce2c71f0a07ef27ff0fb81c217238d4ff8`.
- Frozen basis: `7ce5611ffcb382e43976f552f8287c1e1bf4fb89`.
