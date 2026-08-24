# Round-1 TRACE-REG residue audit — portfolio root P2

- **Producer/session:** Nash (`/root/outerloop_critic`)
- **Round:** `20260824`, narrowed residue/underdetermination audit
- **Status:** INTERNAL / PRODUCER-CHECKED; no shared-ledger promotion
- **Arithmetic:** exact symbolic arithmetic over `QQ`, SymPy `1.14.0`

## Verdict: INSUFFICIENT-DATA

The conditional algebra is correct over the campaign field, but it is an
equivalent reformulation of finiteness at full scope.  The promoted boundary
packet does not determine even the quadratic trace principal part: two exact
denominator-42 completions have the same exponent support, characteristic
gcd drops, leading coefficient, and every conjugate contact, while their
`m=2` Newton-sum residues differ.

The smallest missing non-tautological datum is a **target-affine-divisor-tagged
completed branch pairing**, including the coefficient convolutions that enter
the negative integral powers after summing every ramification and residue
orbit.  For the quadratic residue at a target DVR this is, branch by branch,

```text
sum_(r+s=-e_w) a_(w,r) a_(w,s),
```

together with its residue-field trace and the grouping of all `w` above the
same target divisor.  The current contact tree does not retain these
coefficients, and the D25 source jets have no proved dictionary to them.

## 1. Exact conditional algebra

### Proposition (all hypotheses explicit)

Let

```text
k = C,
A = C[P,Q] subset B = C[x,y],
K = Frac(A), L = Frac(B), d = [L:K],
J(P,Q) = c in C*.
```

The nonzero Jacobian makes `P,Q` algebraically independent, so
`A ~= C[U,V]`, and equality of transcendence degrees makes `d` finite.  Use
the **field trace** `Tr_(L/K)`, not an `A`-module trace (the latter is not
available before finiteness).  If

```text
Tr(x^m), Tr(y^m) are in A for every 1 <= m <= d,
```

then `(P,Q)` is a polynomial automorphism.

### Proof

For `z=x` and then `z=y`, put `p_m=Tr_(L/K)(z^m)` and write the
characteristic polynomial of the `K`-linear multiplication operator `M_z` as

```text
chi_z(T) = T^d - e_1 T^(d-1) + ... + (-1)^d e_d.
```

Newton's identities are

```text
r e_r = sum_(i=1)^r (-1)^(i-1) e_(r-i) p_i,   e_0=1.
```

Characteristic zero permits division by every `1 <= r <= d`.  Induction
therefore puts all `e_r` in `A`.  Cayley--Hamilton gives `chi_z(z)=0`, so both
`x` and `y` are integral over `A`.  As `B=A[x,y]` and `A` is Noetherian,
`B/A` is finite.

There is a presentation

```text
B ~= A[X,Y]/(U-P(X,Y), V-Q(X,Y)).
```

The determinant of its relation Jacobian in `X,Y` is the unit `c`; the
Jacobian criterion makes `A -> B` etale.  It is now finite etale.  Analytically
this is a connected finite covering of simply connected `C^2`, hence has
degree one.  Equivalently `L=K`; normality of `A` and integrality then give
`A=B`.  Thus `(P,Q)` is an automorphism.

Separability is automatic over `C`.  It is needed for the inverse-branch-sum
interpretation of trace, but not for the multiplication-matrix/Newton step.
Over a nonclosed characteristic-zero field the last step may instead be made
after algebraic closure because `k[x,y]` is geometrically connected.  The
statement is false in positive characteristic: `(x^p-x,y)` has constant
nonzero Jacobian and is finite etale of degree `p`, but is not an
automorphism.

### Converse, equivalence, and the hidden degree

Because `A` is normal, if `B` is finite over `A`, then every `z in B` is
integral, `Tr(z^m)` is integral over `A` and lies in `K`, and hence
`Tr(z^m) in A`.  Consequently, map by map over `C`,

```text
first-d power traces of x and y are A-regular
    <=> x and y are integral over A
    <=> B is finite over A
    <=> (under J in C*) (P,Q) is an automorphism.
```

Thus full TRACE-REG is not a smaller theorem than properness.  The field
degree `d` exists without assuming module-finiteness, but it is unbounded in
the universal JC2 problem.  A particular pair has elementary Bezout bounds,
yet there is no fixed universal trace cutoff.  The sheet-6 formal template's
`td=6` cannot be imported into an actual TRACE-REG argument without the still
missing actual-map/paired-boundary transport.

Low moments alone have no general force.  For
`L=K(alpha)`, `alpha^d=u^-1`, all `Tr(alpha^m)` vanish for `1<=m<d`, while
`Tr(alpha^d)=d/u`.  Hence `m=1,2` is only a cheap data discriminator when
`d>2`, not an integrality test.

## 2. Exact local principal-part formula

Let `C` be an irreducible **affine** divisor of `Spec A` with completed
fraction field `K_C=kappa_v((t))`.  Decompose

```text
L tensor_K K_C = product_w L_w.
```

After tame geometric splitting, choose `t=u_w^e_w` and write

```text
z_w(u_w)^m = sum_n c_(w,m,n) u_w^n,
```

where `c_(w,m,n)` lies in the residue field `kappa_w`.  The roots-of-unity
filter and the residue-field trace give

```text
Tr_(L/K)(z^m)
 = sum_w e_w sum_(e_w | n)
     Tr_(kappa_w/kappa_v)(c_(w,m,n)) t^(n/e_w).
```

If the coefficients already lie in `kappa_v`, the factor becomes
`e_w f_w c_(w,m,n)`, where `f_w=[kappa_w:kappa_v]`.  Therefore

```text
PP_C Tr(z^m): retain every n<0 divisible by e_w,

Res_t(Tr(z^m) dt)
 = sum_w e_w Tr_(kappa_w/kappa_v)(c_(w,m,-e_w)).
```

The formula must include every local factor above the same target divisor,
not merely the conjugates of one source place.  Since `A` is normal, the
trace is in `A` exactly when these full principal parts vanish at every
affine prime divisor.  Polynomials are allowed to have poles along a chosen
compactification's target divisor at infinity; a residue there is not a
failure of `A`-regularity.  Also, an ordinary residue detects only the
`t^-1` coefficient.  TRACE-REG needs the entire negative principal part
unless an independent simple-pole/logarithmic bound has first been proved.

For geometrically split inverse branches
`z_j=sum_q a_(j,q)t^q`, the first two cases reduce to

```text
[t^-ell] Tr(z)   = sum_j a_(j,-ell),
[t^-ell] Tr(z^2) = sum_j sum_(q+r=-ell) a_(j,q)a_(j,r).
```

This quadratic convolution is precisely what a contact-only passport loses.

## 3. Exact controls

### Nontrivial tame automorphism

For

```text
P=x, Q=y+x^2, J=1, x=P, y=Q-P^2,
```

the generic affine target DVR `P=t,Q=q` gives

| trace | exact expression | principal part | residue |
|---|---|---|---|
| `Tr(x)` | `t` | `0` | `0` |
| `Tr(x^2)` | `t^2` | `0` | `0` |
| `Tr(y)` | `q-t^2` | `0` | `0` |
| `Tr(y^2)` | `(q-t^2)^2` | `0` | `0` |

In the target-infinity chart `P=t^-1,Q=q`, `Tr(x)=t^-1` and
`Tr(y)=q-t^-2`; these allowed poles verify the affine-versus-infinity
perimeter rather than contradicting regularity.

### Generically finite nonproper polynomial map

For

```text
P=x^2, Q=xy, J=2x^2, d=2,
```

the arc `x=u, y=q/u` escapes while mapping to `(P,Q)=(u^2,q)` and approaching
the affine divisor `P=0`.  With `t=P=u^2`, the two branches are
`(u,q/u)` and `(-u,-q/u)`, and

| trace | exact expression | principal part | residue |
|---|---|---|---|
| `Tr(x)` | `0` | `0` | `0` |
| `Tr(x^2)` | `2t` | `0` | `0` |
| `Tr(y)` | `0` | `0` | `0` |
| `Tr(y^2)` | `2q^2/t` | `2q^2/t` | `2q^2` |

Thus the first moment cancels by conjugacy while the second detects
nonproperness.  This validates the residue computation without pretending
that a generic nonproper map is Keller.

The Keller identity itself supplies only

```text
Tr(z^m dx wedge dy) = c^-1 Tr(z^m) dP wedge dQ.
```

No identity found here forces the scalar trace principal part to cancel.

## 4. Decisive completion collision

Take `t=u^42` and

```text
z_b = u^-84 + u^-30 + u^-10 + u^-5 + a*u^-42 + b*u^42.
```

Relative to the invariant leading exponent `-84`, the non-invariant offsets
are `54,74,79`.  Their gcd sequence is

```text
42 -> 6 -> 2 -> 1,
```

so the characteristic-index sequence is `(7,3,2)`.  Both `a*u^-42` and
`b*u^42` are fixed by every `u -> zeta*u`, `zeta^42=1`.  The varying slot is
at offset `126`, strictly after the last retained characteristic/contact level
`79`.  Varying a nonzero `b` therefore changes neither the support nor any
retained conjugate difference, contact, characteristic exponent, orbit size,
or leading coefficient.

Exact orbit summation gives

```text
Tr(z_b)   = 42*(t^-2 + a*t^-1 + b*t),
Tr(z_b^2) = 42*(t^-4 + 2*a*t^-3 + a^2*t^-2
                       + 2*b*t^-1 + 2*a*b + b^2*t^2).
```

At `a=1`, completions `b=1` and `b=2` therefore have the same retained
contact decoration and the same full `m=1` principal part, but

```text
Res(Tr(z_1^2)dt)=84,    Res(Tr(z_2^2)dt)=168.
```

This is the requested first decisive discriminator.  It is a completion
collision, not a polynomial map and not a formal Keller countermodel.

## 5. Why the promoted packet cannot select between them

The audit uses P1 only for its frozen `COSTUME` perimeter; no P1 invariant is
used as a proposition.  The relevant promoted/current documents say:

1. `SHEET6-CLASSICAL.md` records the denominator-42 Newton pairs and contact
   table, while explicitly leaving the B-side same-direction and B/x
   resolution tails unpinned.
2. `GROK-MONODROMY.md` leaves the B-place partition unpinned and makes the
   x-side finite values depend on an unpinned polynomial `L(a_3)`.
3. `TRANSPORT.md` leaves the fiber-tagged paired Newton--Puiseux
   corner-to-tree functor as Conjecture T and explicitly says the GGV
   `P`-polygon does not determine residual `Q`-cancellation or pole status.
4. D25 supplies exact finite modular source jets in its own typed chart, but
   no proved construction maps their tail labels to completed inverse
   branches grouped above an affine target divisor.

Consequently, inserting either value of `b` would be an extra assumption.
Complete branch pairing or integrality cannot be assumed to manufacture it:
those are the global objects TRACE-REG was meant to prove.

## Perimeter and stop

- No trace-regularity, finiteness, or automorphism theorem is proved.
- The collision does not refute TRACE-REG; it refutes derivation of TRACE-REG
  from the currently retained boundary data.
- It does not claim to match every numerical D25 coefficient.  The point is
  that no proved D25-to-target-local coefficient dictionary exists.
- `m=1,2` and residues alone cannot establish the first-`d` criterion.
- No Keller-specific separating identity was isolated.

The registered `INSUFFICIENT-DATA` stop has fired, so no general trace engine
or descendant theorem lane is launched.

## Reproduction and artifacts

```sh
uv run --no-project --with sympy==1.14.0 \
  python3 cases/round1_trace_probe/trace_probe.py \
  --out cases/round1_trace_probe/results.json
```

- `cases/round1_trace_probe/trace_probe.py`
  - SHA-256 `faadfaf26c7184c24fc3e55a3de90c881e38b0bf12293cb245bcaa9ab5ad0372`
- `cases/round1_trace_probe/results.json`
  - SHA-256 `51f5a6e200327dd343c1c06ed2e9529ef807428531d21535caef63c655f00706`
- input-manifest SHA-256
  - `b9028b003acccabea5299d02960bac0f276c86ad00c3ea8ac62ebcd477e39c85`

No shared ledger was edited.
