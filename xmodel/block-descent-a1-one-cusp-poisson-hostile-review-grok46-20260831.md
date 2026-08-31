# Hostile review: one-cusp Poisson locally-finite obstruction

Date: 2026-08-31 UTC
Reviewer: Grok 4.6 (independent different-model adversarial referee)
Charged packet (frozen copy): `block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md`
Charged artifact (frozen copy): `block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md.artifact.json`
Packet frozen basis named in the artifact: `b6a73150edc586af1f14a14a9c86efa3b10e2958`

No charged file was edited. No canonical ledger was edited. `jc2-lean` was not inspected. No CAS was used. Arithmetic is desk-level. No exit price is asserted.

## 0. Disposition

The packet is a conditional obstruction on the exact ring
`R=C[A,U,Z]/(U^2-A-A^2 Z)`, not a mixed/mixed horn exclusion. At that
stated scope the charged equivalences and the two fibre exclusions
survive every attack below. The Aut formula is an imported theorem; the
consequences of that formula are proved in the packet and re-checked
here.

```text
ring presentation and geometry of Spec R     CONFIRMED
Poisson bracket and Hamiltonian fields       CONFIRMED
X_H LF  <=>  LN  <=>  H in C[A]              CONFIRMED
two non-LF Hamiltonian Keller flows          CONFIRMED
cofinite image; generic fibre not A1, not C* CONFIRMED
Picard / ML / Derksen / ruling firewalls     CONFIRMED
declared scope (horn remains open)           CONFIRMED
```

Attack that failed hardest: the hyperbolic Euler field of weights
`(2,1,-2)` is locally finite and not locally nilpotent. It does not
preserve `omega`, so it is not a counterexample to (0.2). Attack that
failed next: an Euler-characteristic / covering-space attempt to close
the horn from cofinite étale image plus `pi1(A^2-E)=1`. Fibre
cardinality of a non-proper étale map is not classically constant;
partial sheets at infinity are exactly the packet's ramification
ledger. That attempt is not a missed closure.

## 1. Custody

Frozen SHA-256 values were reproduced before mathematical reading.

```text
cd27b7f6687103fae0fc4e5fe19772e0f8e62939d73a655ebf04e57905ddba05
  .../block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
a255cf39d6b3fb07c5a4c4e494921b7fa795e7881c7b21c4dccdcd2692a87a94
  .../block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md.artifact.json
```

Both matched. Independently, the unique body of the charged packet
through its first standalone body-end marker (including the terminating
newline of that marker) is 20567 bytes with SHA-256
`d25cf00344794cefc51eebf045f4c0daee52352d46d5352638a998ea432381bf`,
agreeing with the artifact. Full-file bytes 20900 likewise agree.

The load-bearing external Aut formula was checked against Dubouloz--Palka
arXiv `1701.01425v2`, Example 5.3 / (5.8) and (5.12). Their
`(u,v,w)` are the packet's `(A,Z,U)`. Miyanishi--Masuda `MM06` 4.7 was
not re-proved; it is the packet's declared Aut input.

## 2. Ring presentation and geometry of `Spec R`

**Verdict: CONFIRMED.**

Let `q=U^2-A-A^2 Z`. Gradient: `q_A=-1-2AZ`, `q_U=2U`, `q_Z=-A^2`.
Vanishing of all three forces `A=0` and `U=0`, whence `q_A=-1`, which
never vanishes. `Spec R` is smooth, hence normal, and Cartier=Weil, so
`Pic=Cl`.

On `A=0` the equation gives `U=0` with `Z` free. One height-one prime
lies over `A`, namely `P=(A,U)`, and the curve is isomorphic to `A1`.
Locally `U^2=A(1+AZ)` with `1+AZ` a unit at the generic point of `P`,
so `div(A)=2P`.

Inverting the element `A` (not the prime `P`) yields
`R[A^{-1}]=C[A,A^{-1},U]`, a UFD. Nagata therefore generates `Cl(R)`
by `[P]`, and `div(A)=2P` bounds the order by two. Nonvanishing: if
`P=div(h)` then `h^2/A` has divisor zero, so `A` is a square in
`Frac(R)=C(A,U)` up to a unit of `R`. The ordinary `A`-adic valuation
of `C(A,U)` (DVR `C(U)[A]_{(A)}`) has value one on `A`, so `A` is not
a square. This valuation is not `ord_P`; the packet uses both, in the
correct rings. Thus `Pic(R)=Z/2<[P]>`.

Units: `R[A^{-1}]^*=C^* A^Z`. A unit of `R` is therefore `c A^n`;
regularity of it and its inverse along `P` forces `n=0`, so `R^*=C^*`.

The ruling `A:Spec R->A1` is trivial on `D(A)`: the fibre over `a!=0`
is `Spec C[U]`. This is the unique additive `A1`-fibration of the
pseudo-plane `S(2,2,1)` (Gizatullin / Masuda--Miyanishi, as used by
DP). No smoothness, normality, unit, or class claim used later is
false.

## 3. Poisson structure and Hamiltonian fields

**Verdict: CONFIRMED.**

The three brackets of (0.1) annihilate `q` by Leibniz:

```text
{A,q}=4UA^2-4UA^2=0,
{U,q}=2A^2-A^2(2+4AZ)+4A^3 Z=0,
{Z,q}=-2U(2+4AZ)+4U+8AZU=0.
```

They descend to `R`. Jacobi on the three generators:

```text
{A,{U,Z}}={A,2+4AZ}=16AU,
{U,{Z,A}}={U,-4U}=0,
{Z,{A,U}}={Z,2A^2}=-16AU.
```

The sum vanishes. Skew and Leibniz are by construction of a bivector,
so the structure is Poisson on `R`. Rank two: `{A,U}=2A^2` on `D(A)`,
and on `A=U=0` one has `{U,Z}=2`. The inverse form on `D(A)` is
`omega=dA wedge dU/(2A^2)`. The `(U,Z)` chart gives
`omega=dU wedge dZ/(2+4AZ)`, regular and nonvanishing along `P`. In
dimension two every algebraic 2-form is closed, so `omega` is
symplectic. Hamiltonian fields satisfy
`L_{X_H} omega=d(i_{X_H} omega)=d(+/- dH)=0`.

Because `R^*=C^*`, every other algebraic symplectic form is a constant
multiple of `omega`. The specific constants in (0.1) are immaterial to
(0.2); only that some `C^*` multiple is preserved, and that the
hyperbolic weights act on it by `lambda^{-1}`.

## 4. Locally finite iff locally nilpotent iff `H in C[A]`

**Verdict: CONFIRMED.**  The semisimple case is not a hole.

### 4.1 External Aut formula, specialized

DP (5.12) for `S(k, rbar k, 1)`, at `k=2`, `rbar=1`, reads
`alpha(u,w)=(lambda^2 u, lambda epsbar w + u^2 Q(u))`. The root of
unity `epsbar=+/-1` is absorbed into `lambda` exactly as DP does, so
every automorphism is of the packet's form (4.1). The third coordinate
is not optional: substituting `A' = lambda^2 A` and
`U' = lambda U + A^2 Q(A)` into `U'^2=A'+(A')^2 Z'` and cancelling
`A` (the identity is polynomial, so it extends across `A=0`) yields
exactly

```text
Z' = lambda^{-2} Z + 2 lambda^{-3} U Q + lambda^{-4} A^2 Q^2.
```

On `D(A)`, `d(A^2 Q)` is a multiple of `dA`, so
`phi^* omega = lambda^{-1} omega`. Thus every algebraic torus action
has a character `lambda: T -> G_m`, and `lambda` trivial forces the
action into the ind-unipotent `Q`-subgroup. A morphism from a torus to
a unipotent algebraic group is trivial. A nontrivial torus therefore
has nontrivial `lambda`, hence cannot preserve `omega`. This is (4.3).
The standard hyperbolic action of weights `(2,1,-2)` scales `omega` by
`lambda^{-1}`, in agreement.

### 4.2 Locally finite plus volume-preserving implies locally nilpotent

Let `D` be locally finite with `L_D omega=0`. A finite-dimensional
`D`-stable subspace `V` containing `1` and algebra generators exists.
Each `exp(tD)` is an algebra automorphism of `R` (char 0, local
finiteness: on eigenvectors it is scaling, on Jordan blocks it is
unipotent polynomial). Its Zariski closure `G` in `GL(V)` is a
connected commutative linear algebraic group acting on `R`. Preservation
of `omega` is a closed condition, so `G` preserves `omega`. A
nontrivial torus part would contradict (4.3). Hence `G` is unipotent,
`D|_V` is nilpotent, and Leibniz spreads nilpotence to `R`.

Incommensurable eigenvalues make the analytic curve dense in a
higher-dimensional torus; the torus still lies in `G` and still
preserves `omega`. That only strengthens the argument.

**Attack, semisimple case.** The Euler derivation of the hyperbolic
`C^*`-action,

```text
E = 2A d/dA + U d/dU - 2Z d/dZ,
```

preserves `(q)` because `E(q)=2q`, is locally finite, and is not
locally nilpotent. It is the unique obvious candidate to break the
equivalence. Cartan gives `L_E omega = -omega != 0`, so `E` is not
Hamiltonian and not volume-preserving. Mixed Jordan of a Hamiltonian
`D` would still put a torus in the Zariski closure of the flow, which
(4.3) forbids. There is no leftover locally finite non-nilpotent
Hamiltonian.

### 4.3 Kernel of every nonzero LND is `C[A]`

An LND exponentiates to a `G_a`-action. `Hom(G_a,G_m)=0`, so `lambda=1`
and `delta(A)=0`. After inverting `A`,
`R_A tensor C(A) = C(A)[U]`, whose nonzero LNDs have kernel `C(A)`.
Then `R cap C(A)=C[A]`: localization produces a Laurent polynomial in
`A`, and regularity along `P` kills negative exponents. Thus
`ker(delta)=C[A]` and `ML(R)=Dk(R)=C[A]`.

For nonconstant `H`, if `X_H` is locally finite then Section 4.2 makes
it a nonzero LND, so `H in ker(X_H)=C[A]`. (Casimirs are constants
because the Poisson tensor is everywhere of rank two, so `X_H` is
automatically nonzero.) Conversely, for `H in C[A]`,
`X_H=H'(A) X_A` with `X_A(A)=0`, `X_A(U)=2A^2`, `X_A(Z)=4U`, and
`X_A^3=0` on generators, hence locally nilpotent. This is (0.2).

A slice for an LND would give `R=C[A,s]` by the slice theorem, hence
`Pic=0`, contradicting Section 2. So no locally finite Hamiltonian has
a slice.

## 5. Transfer to a hypothetical quartic Keller pair

**Verdict: CONFIRMED.**  The quartic field degree is not used.

A pair `f,g in R` with `{f,g}=c in C^*` makes `c^{-1} X_f` a Hamiltonian
derivation with slice `g`, and `-c^{-1} X_g` a Hamiltonian derivation
with slice `f`. Both would be forbidden LNDs if locally finite. Hence
both flows are non-locally-finite, and neither Hamiltonian lies in
`C[A]`. Exactly two flows are charged because each coordinate of a
symplectic coframe is a Hamiltonian with a polynomial slice.

Independently: if (say) `f=alpha A+beta`, then `X_f` is a multiple of
`X_A`, and `X_A` vanishes identically along `P` (at `A=U=0` one has
`X_A=2A^2 d/dU+4U d/dZ=0`), so it cannot have a slice. The packet's
remark that this direction does not use `[Frac(R):C(f,g)]=4` is
accurate.

Smoothness of each coordinate morphism: `{f,g}=c` means `df wedge dg`
is a nonvanishing multiple of `omega`, so `(f,g)` is étale and each
projection is a submersion. Surjectivity: omitting `a` would make
`f-a` a unit, contradicting `R^*=C^*`.

## 6. Cofinite image, degree-four ledger, exclusion of `A1` and `C*`

**Verdict: CONFIRMED** for (6.7) and (6.8). Equation (6.9) is correct
Riemann--Hurwitz bookkeeping for an irreducible general fibre, not a
completed curve classification. The packet does not claim the latter.

### 6.1 Cofinite image

Étale morphisms are open. If an irreducible curve `V(p)` were omitted
from the image of `h=(f,g)`, then `p(f,g)` would never vanish, hence
would be a unit, hence constant, contradicting dominance (already
from `{f,g}=c`, without degree four). In `A2` a closed set containing
no curve is finite, so `h(Spec R)=A2-E` with `E` finite.

### 6.2 Generic fibre is not `A1`

If a general fibre of `f` were `A1`, the unique additive ruling of this
pseudo-plane would force `C[f]=C[A]`, so `f=alpha A+beta`, already
excluded. The packet phrases this as "the standard affine-surface
`A1`-fibration construction" producing an LND with kernel `C[f]`, then
invokes (6.3). That construction is standard in char 0 once the generic
fibre is `A1` and `f` is primitive, but it is the thinnest sentence in
the proof. Primitivity is cheap: `f=phi(h)` with `deg phi>1` would make
`{f,g}=phi'(h){h,g}=c`, so `phi'` is constant. The uniqueness of the
`A1`-ruling on `S(2,2,1)` repairs the sentence with no blast radius.
A parallel topological route: a smooth surjective `A1`-fibration has
no multiple fibres, so `pi1` would be trivial and `S` would be `A2`,
contradicting `Pic=Z/2`.

### 6.3 Generic fibre is not `C*`

For general `a` with `{f=a}` missing `E`, the restriction
`g: C_a -> A1` is surjective and étale. Degree four, when used, is
`[Frac(R):C(f,g)]=4`, equal to the number of geometric preimages of a
general point of the line; it is not needed for the `C*` exclusion.

If `C_a` were `C*` with coordinate `t`, then `g` would be a Laurent
polynomial with `dg/dt` nowhere zero, so `dg/dt=c t^n`. The case
`n=-1` is not the derivative of a Laurent polynomial. For `n!=-1`,
`g=alpha t^{n+1}+beta` omits `beta` as `t` runs over `C*`. Not
surjective. The mixed control `U` in Section 6.1 of the packet is the
sharp comparison: `U` is smooth and surjective with generic fibre
`C*`, but `{U,s}=1` has general rational solution `s=1/(2A)+h(U)`,
and the order-two pole of `1/(2A)` along `P` (`ord_P(A)=2`) forces
`h` to have a pole of order two at `U=0`, which is then uncancelled
along `Q={U=0,1+AZ=0}` where `A` is a unit. So `U` is not a Keller
coordinate, and it does not evade (6.8).

### 6.4 Ledger, genericity, and a covering-space false close

All ramification of the completed degree-four map `Cbar_a -> P1` lies
in `S=Cbar_a-C_a`. Riemann--Hurwitz `sum (e_p-1)=2 gamma+6` plus
`sum_{p|infty} e_p=4` gives (6.9). Surjectivity implies that over each
finite value at least one unramified point of `C_a` remains, so the
deleted points over that value have `sum e_p <= 3`. For primitive `f`
a general fibre is irreducible, so a single `gamma` is legitimate.
Special coefficients are not used. The ledger is finite bookkeeping
and a successor, not an enumeration.

"Hyperbolic" in the packet means neither `A1` nor `C*`. A disconnected
union of copies of `A1` is not a general fibre of a primitive
morphism, so it is not a hidden surviving type.

A tempting Euler close was checked and rejected. If `S -> A2-E` were a
4-sheeted covering then `pi1(A2-E)=1` and `e(S)=1` would kill it.
That would require fibre cardinality of `h` to be classically constant
on `A2-E`. For a non-proper étale map, partial sheets at infinity make
cardinality drop along loci still in the image, without ramifying on
`S`. The map is a local biholomorphism and is not a covering map. The
packet is right not to claim a horn exclusion from (6.7) alone.

## 7. Negative controls

**Verdict: CONFIRMED.**  The packet's own proofs do not use the
shortcuts they break.

Direct substitution with `U^2=A(1+AZ)` gives `(U')^2=A'(1+A'Z')` for
`A'=U^2`, `Z'=4Z`, `U'=U(1+2AZ)`. Direct brackets, reduced by the
same equation, give (7.3): the Poisson tensor pulls back by the
nonzero constant 4, so `eta` is étale. Generically `U^2=A'`, so the
function-field degree is at most two. The involution
`U |-> -U`, `Z |-> Z`, `A |-> -A-1/Z` of `Frac(R)` fixes the three
coordinates of `eta` and is nontrivial; it is birational rather than
regular (it blows up at `Z=0`), which is enough for field degree
exactly two. This is DP (5.8) with first coordinate rewritten as
`U^2`.

`eta^*(A)=U^2` is not in `C[A]`, so ML/Derksen are not covariant under
arbitrary étale maps. `div(U)=P+Q` with `Q=(U,1+AZ)`, and
`eta^* P=P+Q`, so `eta^*[P]=0` in `Z/2`. Finite covering
multiplicativity plus `e(R)=1` shows `eta` is not finite, hence not
proper, matching the cited paper. None of these facts is an input to
Sections 4--6: those use the Aut formula, `omega`, `Pic`, units, and
kernels of LNDs, all Aut-level.

The three derivation firewalls in the packet's Section 8 are correct
and correctly scoped. `D=d/dx + y d/dy` on `C[x,y]` has a slice and is
locally finite but not locally nilpotent; its divergence is 1, so it
does not touch (5.1). On `C[s,t,t^{-1}]` the same shape preserves
`ds wedge dt/t` without being Hamiltonian. On `A2`, "Hamiltonian with
a polynomial slice implies locally nilpotent" is equivalent to JC2
via Rentschler.

## 8. Scope limits

**Verdict: CONFIRMED.**  No charged wording overreaches into a horn
exclusion, a general Hamiltonian-slice lemma, or étale functoriality
of ML/Pic/the ruling.

The surviving target (0.6) is conditional: two algebraically
independent non-locally-finite Hamiltonians with `{f,g}=c` and field
degree 4, plus a boundary packet this file does not prove. The
boundary packet is not used in any proved line of (0.2), (6.7), or
(6.8). Table 9's "branch closed" entries are closed only for LND
slices, locally finite Hamiltonian slices, `A1` generic fibres, and
`C*` generic fibres of a Keller coordinate. The mixed/mixed horn is
marked open. Formula (0.5) is labelled a firewall, not a map to `A2`.

## 9. Weakest exact hypotheses, correction, next test

**Hypotheses actually used.** Complex numbers (char 0, algebraically
closed). The hypersurface ring `R` above. The Poisson structure (0.1),
or any `C^*` multiple. The full Aut group of `S(2,2,1)` in the shape
DP (5.12) / MM06 4.7. For the Keller transfer: `f,g in R` with
`{f,g} in C^*`. For the numerical ledger (6.9) only: field degree 4.
Nothing in the proved statements needs the charged `(3,1)+(2,2)`
boundary.

**Correction and blast radius.** No correction to a charged claim.
Optional tightening of the `A1`-fibre sentence: cite uniqueness of the
additive ruling on this pseudo-plane instead of an unnamed "standard
construction". Blast radius zero.

**Best next falsification test.** Independently of MM06, try to produce
a single polynomial automorphism of `R` whose `lambda` is identically
`1` but which does not lie in the additive `Q`-family, or whose
pullback of `omega` is `omega`. One such map would put a symplectic
torus or a non-unipotent locally finite Hamiltonian into Aut, and
would collapse (0.2). Desk check: the candidate `H=U` already fails
local finiteness (`X_U(A)=-2A^2`, `X_U^2(A)=8A^3`, degrees of `A`
unbounded). The same unbounded-degree test on `H=U+A` and `H=Z` is
the cheapest direct probe of (0.2) that does not trust Aut. If (0.2)
stands, the live remaining break of the horn is the packet's successor
2: realize (6.9) by an actual degree-four completion and couple the
deleted points to the charged boundary census.

<!-- BODY-END -->
