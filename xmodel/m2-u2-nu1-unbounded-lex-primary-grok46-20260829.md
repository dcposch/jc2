# U2 (`nu_G=1`, unbounded lex) — primary research (Grok 4.6, 2026-08-29)

Lane: exact Grok 4.6, primary research, independent of the Opus equal-join
producer except at the reviewed scope of that report and of this lane's
hostile review of it.

Target: the sole currently proved-infinite reduced merge-state regime —
Prop. 9.3 case I at `nu_G=1`, `kbar in Q`, `r>=2` equal `(mu,w)` nonzero
arrivals, unbounded q-only extra count `lex`.

## 0. Custody, scope, honesty

Read at the reviewed scopes, and only those:

- `xmodel/m2-equal-join-semilinear-primary-research-opus5-20260829.md`
  (full-file `7ed65bc22f836230dada03776a1b3c6f9110c955a35b52fa28c21d0811a6c99d`);
- this lane's hostile review
  `xmodel/m2-equal-join-semilinear-primary-research-hostile-review-grok46-20260829.md`
  (full-file `8755bd5d3d1cd2721d32e5956c5b139b2cc6e0e805662d5278ededff896135ba`);
- `ladder/BOOK-OFFAXIS.md` §§0–11a as currently on disk, used at P0–P5
  (`7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77`);
- `ladder/SHEET6-MULTIPOLE.md` MP6/D9
  (`93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb`);
- `ladder/SHEET6-L1.md` L1b / the reviewed `nu=1` normalization
  (`69e6e4c1c359381c01941f641c5c7f364f95342411c8e90ed7d4aa27965f38fc`);
- `ladder/SHEET6-DEPTH.md` §1 and §5c–5d
  (`ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d`);
- printed Prop. 8.1(iv) in the normalization of `cases/l1_ode_check.py`
  header (`e766bfe27ac9a06ef6eab053dbea666f8b3d3e70a48ee8c76b88e45246c3bea9`);
- `ladder/REDUCTION.md` CRITICAL 4–7 only as already used by the reviewed
  Opus report (`0a88db0d136001a6c18343f941a80ecfaef5ceffcbe84e05c739a853d13c1936`);
- `xmodel/sol-td7-law.md` (1)–(9) as a T1-GEN specialization anchor
  (`99bd762aa458840bd8e3327fae35c7e23ad388976fb0fcb85c0fd8570ab592f2`);
- `cases/book_offaxis.py` census of L6-surviving entries (`tdmax=14`)
  (`c22e3a1f977fef94022f34378232fcc78148fa506501f71ec6a57313d6042ebc`).

The cap-free reduced P0 chain theorem is used as currently recorded in
BOOK-OFFAXIS P5 (the 2026-08-29 correction via the resolvent
`E(l*a*(1+k+lex)-kbar*d*C)=l*a*T`): at fixed `(w,M)` and St 9.4 budget
the reduced chain-state set is finite. No Sol56 source file beyond that
recorded statement was re-opened.

Not done, as instructed: no access of any kind to `jc2-lean`; no
`git status` or other workspace-wide command; no web, AWS, Singular,
msolve, Sage, PARI or heavy CAS; no canonical edit; no commit or push;
no active ideation, transport, or Q+E5-review output. Arithmetic is desk
`int`/`Fraction` and a self-contained sparse polynomial class. Writes are
exactly the two licensed paths (this report, and the uniquely named
packet under `cases/`). Scratch under `/tmp` only.

Trust perimeter: BOOK-OFFAXIS §10, MP6/D9, L1b, printed Prop. 8.1(iv),
R1.0/R2.1/R2.2, P0/P1/P2, MP2, St 9.4. Every clause inherits R4
(`alive != existent`), the P0 rider that `lambda` values are lower
bounds, and the stage-R policy that `n_e in N*` and `i`-sync are never
used to kill.

No landing, ceiling, Keller map, or JC2 inference is drawn.

---

## 1. Verdict

**`U2_REDUCED_FINITE`**

After LL-1/MP6 absorption of the `nu=1` eta slot, the most general U2
shape that can remain unbounded in `lex` is

```
p = Rad^mu,   q = Rad * S,   deg Rad = r >= 2,   deg S = L >= 1,
```

with `Rad` squarefree, roots off `0`, `S` squarefree and coprime to
`Rad`, equal arrival multiplicity `mu`, equal arrival invariant `w`,
no 0-arrival, and `eps = k = 0`. A free 0-root and every non-chain
`p`-orbit are killed for unbounded `L` by (NE), because `dp` is
independent of `L` while `dq ~ L`. The `e0=1` variant is the subcase
`S(0)=0`, not an independent slot.

Printed Prop. 8.1(iv) is equivalent, uniformly in `L` and in `mu`, to

```
r * Rad * S' - L * Rad' * S = C' != 0.                 (U2-ODE)
```

The extra polynomial `S` **does** exist in arbitrarily high degree:
at `r=2` a D9-style logarithmic residue (equivalently, the unique
monic `S` giving `C'=0`) kills the even-`L` class, and every odd `L`
survives with `C' != 0`; at `r>=3` the class `L ≡ 1 (mod r)` survives
on the power shape `Rad = t^r - A`, `A != 0`, while `r | L` is
T1-dead. The nonzero RHS gate is explicit: the Prop. 8.1(iv) constant
is `C = mu C' / (r+L)`, so `C != 0` iff `C' != 0`.

Those surviving shapes do **not** produce infinitely many legal
terminals at any fixed `(td, entry)`. Exact transport is

```
dp = r*mu,   dq = r+L,   E = mu*L,   M = gcd(r*mu, r+L),
kbar = w*(r+L)/L,   w_tr = w*(r+L-1)/L -> w,   lambda_G = 0.
```

`w_tr > w` strictly. If `w >= 1` the merge itself is never a P1
terminal. Composing with the cap-free P0 chain theorem and P1
`j = M(1-w_t) in N*` / `psi = ceil(M/j)-1`, every zero-cost trunk
keeps `M_t` in a finite divisor set of `M_G` (hence a finite grid of
legal `w_t`), and every dirty step has `M'` dividing a
budget-bounded `l+Sm`. Hitting that finite grid forces a linear
polynomial in `L` to divide a budget-bounded integer, so only
finitely many `L` can reach a legal terminal. This is the U2 analogue
of Sol56's finite reduced chain set: the infinite reduced merge-child
`(w_tr, M)` sequence is real as a merge-local fact and is quotiented
to a finite terminal set by P0/P1 at fixed budget.

Mandatory negative control: the `td=7` class-A `(2,2t)` tail is
`r=2`, `mu=1`, `L=2t-2` even, `dp=2`, `dq=2t`, `w_tr = 2 + 1/(t-1)`,
matching P3. It is T1-dead (`C'=0`) for every `t>=2`, and separately
first-step-inversion budget-dead (0 fitting routes, remaining budget
`3-psi <= 2`, no caps). Second uniform death: the smallest `td=8--14`
source row is `td=8`, `m=2`, type `(2,3)`, `Lambda=(4,4)`,
`M=[2,2]`, `w_0=3/2`. Direct equal-`mu` arrivals have `mu | 2`, a
2-power, so every `L` is T1-dead or MP2-dead. A symmetric post-jump
`(A)` arrival with `mu=3` is MP2-alive on the AP `L ≡ 1 (mod 6)`,
and the finite-`L` theorem leaves at most finitely many cells; the
charged one-step scan fits a single `L=1` route at exact St 9.4
equality (slack 0) and fits none of `L in {7,13,19,25}`.

Nothing here is a Keller map, a landing, or Statement-3.9 gluing of
arrival bases to `Rad`. Pattern-tier T1 existence of high-degree `S`
is not a formal `(f,g)`.

---

## 2. `nu=1` normalization, and the most general unbounded U2 shape

Not 3.4 forces `nu=1` on `V_{2,a}\V_{1,a}`. Case I applies, `kbar in Q`
is legal, N1 is off. The `nu>=2` pattern of R1.0 / the Opus report

```
p = eta^eps * Pfull(t),   q = eta * Rad(t) * S(t),   t = eta^nu,
dq = 1 + nu*(r0+k+lex)
```

**cannot be copied to `nu=1`**. At `nu=1` one has `t=eta`, so the
legacy eta slot and the `t`-polynomial live in the same variable.
MP6(c): `q = eta·rad(p)·Π(eta^nu-b_s^nu)` for `nu>=2`, **eta-factor
absorbed at `nu=1`**. L1b / `l1_ode_check.py` family B: the
all-`mu=1` shape is `p=(eta-a1)(eta-a2)`, `q=p*s`,
`(dp,dq)=(2,2+l)`, `M=gcd(2,2+l)`, not `(dp,dq)=(2,3+l)`.

The absorbed equal-`mu` pattern with a free 0-root of multiplicity
`eps` and `k` non-chain orbits is

```
p = eta^eps * Π_e (eta-c_e)^mu * Π_j (eta-d_j)^{m_j},
dq = e0 + r + k + L,   dp = eps + r*mu + Sm.
```

Root law (R1.0, L1 §1a): `e0=1` is forced if `eps>=1`; if `eps=0`
then `e0 in {0,1}` with `e0=1` meaning `0` is among the extras.

(NE) on a free 0-root is `eps*dq < dp`. Here `dp` is independent of
`L` and `dq ~ L`, so `eps>=1` empties all sufficiently large `L`.
The same bound kills every non-chain orbit `m_j>=1`. Hence:

> **Lemma (unbounded-lex support).** A U2 configuration with
> unbounded `L` has `eps=0` and `k=0`. The `e0=1` variant is the
> specialisation `S(0)=0` of the `e0=0` shape `q = Rad*S`.

The surviving shape is the display of §1. Degrees and transport
follow R2.1 with `nu=1` (no extra `+1` in `dq`):

```
E = mu*dq - dp = mu*L,
kbar = mu*w*dq/E = w*(r+L)/L,
rho  = dp/dq = r*mu/(r+L),
w_tr = kbar - rho = w*(r+L-1)/L,
M    = gcd(r*mu, r+L).
```

(S) is `E>0` i.e. `L>=1`, which is MP7's `l=0` kill at `nu=1`. P2
prices arriving edges and `q`-extras at 0, so `lambda_G=0`. As
`L -> infinity`, `kbar -> w` and `w_tr -> w` strictly from above.
This is the P3 formula at `(mu,w,r)=(1,2,2)`:
`w_tr = 2(L+1)/L`, and `dq=2t` forces `L=2t-2`, hence
`w_tr = (2t-1)/(t-1) = 2 + 1/(t-1)`.

The naive (eta-not-absorbed) formulae `dq=1+r+L` and
`w_tr = w*(r+L)/((mu-eps)+mu*L)` are the `nu>=2` specialisations
and are illegal at `nu=1`. The packet mutation `q = eta*Rad*S`
with absorbed `rho = r mu/(r+L)` is a nonzero residual, for every
charged `(r,mu,L)`.

---

## 3. Attack 1 — Prop. 8.1(iv), uniformly in `lex`

Start from the normalized identity
`rho p q' - p' q = C p` with `C != 0` and `rho = dp/dq`
(`l1_ode_check.py` / R1.0; this is printed Prop. 8.1(iv) after
Cor. 6.1 top cancellation). Substitute `p = Rad^mu`,
`q = Rad*S` at `t=eta`:

```
p' = mu Rad^{mu-1} Rad',   q' = Rad' S + Rad S',
lhs = Rad^mu * [ (rho-mu) Rad' S + rho Rad S' ].
```

With `rho = r mu/(r+L)` this is

```
lhs = p * (mu/(r+L)) * ( r Rad S' - L Rad' S ).
```

Hence Prop. 8.1(iv) holds iff the U2-ODE is a **nonzero constant**
`C'`, and then `C = mu C'/(r+L) != 0` automatically. This is the
T1-GEN identity of the reviewed Opus report, specialised to
absorbed `nu=1` (the Opus T1-GEN assumed `q = eta*W` with `t=eta^nu`
independent, which is the `nu>=2` formula). At `r=2`, `mu=1` it is
L1b/D9 verbatim: `2 p s' - l p' s = c' != 0`.

The identity is verified as a polynomial identity in `eta` and in
the symbolic pattern coefficients, not by sampling, on the eight
charged tuples `(r,mu,L)` in
`{(2,1,1),(2,1,2),(2,1,3),(2,2,1),(3,1,1),(3,2,1),(3,1,2),(4,1,1)}`,
zero residual terms. Three mutations fire: naive eta slot; dropped
`nu`-absorption in `rho`; the even-`L` `r=2` path giving `C'=0`.

**Existence of `S` in high degree.** The U2-ODE is first-order linear
in `S` at fixed `Rad`. Top degree `t^{r+L-1}` always cancels
(Cor. 6.1 at `nu=1`).

*r=2.* The map on monic degree-`L` polynomials is square. For any
squarefree quadratic `Rad`, there is a unique monic `S` of degree
`L`. On `Rad = t^2-A`:

```
(t^2-A) S' - L t S = C'/2,
```

the recurrence `(m-1-L) s_{m-1} = A(m+1) s_{m+1}` determines `S`
from `s_L=1`, and `C' = -2 A s_1`. This vanishes for every even
`L` and is nonzero for every odd `L in {1,3,...,13}` (charged;
the pattern continues by the recurrence, the only obstruction to
continuing being a zero denominator `m-1-L`, which is `-1,-2,...`
and never zero on that range). Even `L=2n-2`, `n>=2`, is D9: the
antiderivative of `Rad^{-n}` has logarithmic residue
`(-1)^{n-1} binom(2n-2, n-1) != 0` at each simple root
(charged `n=2..11`; `n=2` residue `= -2`, matching L1b's `l=2`
residue). The linear-algebra form `C'=0` is the stronger RHS-gate
statement of the same kill: a polynomial `S` exists, but it makes
the right-hand side of Prop. 8.1(iv) vanish, contradicting `⊖ != 0`.
On a generic quadratic `t^2+t+1` the same even/odd split holds.

*r>=3, power shape `Rad = t^r-A`, `A!=0`.* The sparse ansatz
`S = t·h(t^r)` has degree `L=1+r k`. The recurrence
`(t^r-A) S' - L t^{r-1} S = C'/r` determines `S` with
`C' = -A r s_1 != 0` on every charged `(r,k)` in
`r=2..5`, `k=0..4`. This is the family `S=t`, `Rad=u^r+c` at
`k=0`, shifted. When `r | L` the same `Rad` yields `C'=0` or a
non-coprime `S` (charged `(2,2),(2,4),(3,3),(3,6),(4,4)`).

*Dickson consecutive.* `|L-r|=1`, `Rad = D_r(t,alpha)`,
`S = D_L(t,alpha)`, `alpha=2`, gives `C' != 0` for
`r=2..6` (the `z + alpha/z` computation: the Wronskian reduces
to `2 r L alpha^r` precisely when `|L-r|=1`). This is a second
explicit family, not needed for the high-degree existence claim
(the power family already supplies infinitely many `L` for each
`r`).

*Generic `Rad`.* A generic cubic `t^3+t+1` admits no legal `C'!=0`
solution for `L=1..12`. High-degree `S` is a special-`Rad`
phenomenon (polynomials with few critical values: powers and
Dickson), which is allowed: T1 solves for the pair `(Rad,S)`
jointly, and the arrival bases are not yet glued.

So: `S` exists in arbitrarily high degree; D9 kills a parity class
at `r=2`; `r | L` is T1-dead on the power shape; only finitely many
*generic*-`Rad` degrees would survive, but U2 is not restricted to
generic `Rad`.

---

## 4. Attack 2 — `M`, successor `w`, lambda, P0/P1

On the surviving shape,

```
M = gcd(r*mu, r+L).
```

Specialisations:

- `r=2`, `L` odd: `M = gcd(mu, L+2)` (since `L+2` is odd). MP2
  requires that `mu` have an odd prime factor `p` with
  `L ≡ -2 (mod p)`. If `mu` is a 2-power, `M=1` for every odd `L`,
  and every even `L` is T1-dead: **uniform death**.
- `L = 1+r k`: `M = gcd(mu, r(k+1)+1)`. MP2 lives for infinitely
  many `k` iff some prime `p | mu` does not divide `r`.

`w_tr = w(1+(r-1)/L)` is strictly decreasing in `L` to `w`, with
unbounded numerator on every infinite AP of `L` (e.g. `r=2`,
`w=2`, odd `L`: `w_tr = 2(L+1)/L` in lowest terms, numerator
`2(L+1)`). `lambda_G=0`. The merge is a P1 terminal only if
`w_tr < 1`, i.e. only if `w < L/(r+L-1) < 1`. Off-axis entries
have `w_0 >= 1`, and `w_tr > w >= 1`, so the merge itself is
never a terminal. A trunk is required.

**Zero-cost trunk.** Neutral and resonant clean steps (P0) cost 0.
Resonance has `M' | l | M_G`, so `M_t` stays in the finite divisor
set of the (periodic, hence finite-valued) `M_G`. P1 then admits
only finitely many terminal weights `w_t = 1 - j/M_t`. An
`L`-independent multiplier `n/Delta` hits a fixed target for at
most one `L`, because `w_tr(L)` is strictly monotone. An
`L`-dependent `Delta` growing with `L` imposes `L-1` dividing a
constant (from `(n-1)nu+1 = Delta` with `n` a multiple of `L`).
Hence only finitely many `L` reach a zero-cost terminal.

**Dirty trunk.** Each of the `k` northeast `p`-orbits costs at
least 1, so `k` is bounded by the remaining St 9.4 budget at
fixed `td`. Then `Sm <= k(l-1)` is bounded, and the child
`M' = gcd(dp, dq) | (l+Sm)` is bounded. P1 again supplies only
a finite grid of legal `w'`. For `r=2` on the AP `L=6t+1` with
`w_tr = (2/3)(L+1)/L` (the post-`(A)` shape), a dirty step has

```
w' = 2 s (L+1) / (L E),    s = 1+k+lex,    E | 6(L+2) T,
```

with `T = Sm+l-eps*s`. For `eps=0`, `T=Sm+l` is budget-bounded;
for `eps>=1`, `T>=1` bounds `lex` independently of `L`. Hitting a
grid value `tau = p/q` forces `L | 2 s q` and then
`L+1` divides a budget-bounded integer. If `s` is taken
proportional to `L` (the `eps=0` Sol56 bound allows `lex = O(num(w))
= O(L)`), one still obtains `E ~ L+1` dividing `O(L+2)`, hence
`L+1 | 2T`, finitely many `L`. The same reduction applies to a
"focusing" dirty step that would send infinitely many `L` to one
`(w,M)`: that focusing requires `E ~ L+1 | 6(L+2)T`, again
finite. At most `B` dirty steps occur, `B` bounded at fixed `td`.
The `r>=3` law `w_tr = w(r+L-1)/L` has the same shape, with
`gcd(L, r-1)` bounded by the entry's `r <= m`.

> **Theorem (U2 reduced-finite at fixed `(td,entry)`).** On the
> absorbed U2 shape, at a fixed off-axis entry and St 9.4 budget,
> only finitely many `L` can reach a P1-legal terminal. The
> infinite reduced sequence `(w_tr(L), M(L))` is a merge-local
> fact and is not a counterfamily to a finite terminal ledger.

This is the merge-side companion of the cap-free P0 chain theorem:
U1 has constant/periodic child state, U2 has an infinite child
sequence that P1 quotients to finite.

---

## 5. Attack 3 — `td=7` control, and the smallest `td=8--14` row

**`td=7` class-A `(2,2t)` tail (mandatory negative control).**
The unique L6-surviving off-axis entry is type `(2,3)`,
`Lambda=(3,4)`, poles `(1,1,2)⊕(1,2,3)`, `M=[1,2]`, `w_0=(2, 3/2)`.
Class A equal-`(1,2)` join at `nu_G=1` is P3's tail: `r=2`, `mu=1`,
`dp=2`, `dq=2t` (`t>=2`), `L=2t-2` even, `M=2`,
`w_tr = 2+1/(t-1)`. Two independent deaths:

1. *T1.* Even `L`, `C'=0` for every `t>=2` (charged `t=2..15` on
   the closed form, and `t=2..11` on the recurrence). D9 residue
   `(-1)^{n-1} binom(2n-2,n-1)` with `L=2n-2` is the log form of
   the same kill.
2. *Budget, first-step inversion.* Chain 2 has already spent
   `lambda=3` (the `eps`-step that realises `w=2`). Remaining
   budget is `3-psi <= 2`. Cap-free one-step from
   `(w_tr, M)=(2+1/u, 2)`, `u=t-1`, with Sol56 bounds
   (`k <= 2`, `E | l*num(w)*T`, no `nu`/`lex` cap) yields **0
   fitting routes** on `t=2..8` (charged; `t=2..11` in the test
   suite). This is P4's inversion, reproduced without the engine's
   `nu<=400` / `lex<=6` loops.

Either death closes the tail. T1 is the stronger, budget is the
P4 control the brief demanded.

**Smallest `td=8--14` source row.** Current census, L6-surviving,
`td=8..14`, the unique smallest row is

```
td=8, m=2, type (2,3), Lambda=(4,4),
poles (a,b,nu)=(1,2,3) twice, M=[2,2], w_0=3/2, 3/2.
```

It is the unique equal-`w` off-axis entry at `td=8`. Direct
equal-`mu` arrivals have `mu | b = 2`, so `mu in {1,2}`, both
2-powers. By §4, every `L` is T1-dead or MP2-dead: **second
uniform death**, 32 charged `(mu,L)` cells, 0 MP2-alive.

The same source row admits a symmetric post-jump `(A)` arrival
(printed St 9.6 `(21,15)`, `lambda>=2`, `w -> 2/3`, `M -> 3`,
`mu=3` at the step-cell, the P2 "direct from `(A)`" clause).
Then `r=2`, `mu=3`, `L` odd, `M=gcd(3,L+2)=3` iff `L ≡ 1 (mod 6)`.
`w_tr = (2/3)(L+1)/L`, which is in `(2/3,1)` for `L>=3` and equals
`4/3` at `L=1`. Self-terminal: `j=3(1-w_tr)=(L-2)/L` is never in
`N*` on this AP. Cap-free one-step with remaining budget 3
(generous for `psi=1`, spent 4, budget `7-psi`):

| `L` | `w_tr` | one-step hits | St 9.4 fitting |
|---|---|---:|---:|
| 1 | `4/3` | 4 | 1 (exact: spent `4+2=6`, `psi=1`, budget 6) |
| 7, 13, 19, 25 | `(2/3)(L+1)/L` | 0 | 0 |

The `L=1` fit is a **single** pattern-tier cell at slack 0, not an
infinite family. The finite-`L` theorem of §4 says there is no
infinite continuation of this table. The next equal-`w` rows
(`td=12` type `(2,5)`, `M=[3,3]`, `w_0=4/3`, `mu | 3`; type
`(3,5)`, `M=[2,2]`, `w_0=3/2`; the `td=12` `m=3` `[2,2,2]` star)
are the same theorem, not a second search: `mu | 2` dies as at
`td=8`; `mu=3` is the post-`(A)` analysis with a cheaper chain
(`lambda=0` direct from the poles). Direct `td=12` type `(2,5)`
at `L=1` has a clean resonant terminal `(w,M)=(2/3,3)`, `psi=2`,
`lambda=0`, slack 9 — again a single cell, the `L=1` member of a
T1-alive AP that P1 quotients to finite.

No infinite budget-fitting formal counterfamily was found, and
§4 forbids one at any later `td<=14` entry.

---

## 6. Attack 4 — pattern, gluing, landing, Keller

| tier | status |
|---|---|
| Pattern / T1 (U2-ODE, `C'!=0`, squarefree coprime `(Rad,S)`) | infinite `L` exist; r=2 even killed; power class `L≡1 (mod r)` lives |
| MP2 / (S)/(NE)/(R) | 2-power `mu` at `r=2` uniformly dead; otherwise an infinite AP of `L` may be MP2-alive |
| P0/P1 terminal ledger at fixed `(td,entry)` | **finite `L`** (Theorem, §4) |
| Statement 3.9 / coefficient gluing of arrival bases to the roots of `Rad` | not performed; T1 rigidifies the pair `(Rad,S)` and does not realise it from pole Puiseux data |
| Landing of a chain at those bases | not performed |
| Absolute `(f,g)` / Keller map / JC2 | not claimed |

The `td=8` post-`(A)` `L=1` exact-fit and the `td=12` type-`(2,5)`
`L=1` clean terminal are pattern-tier cells under R4 and the
`lambda`-lower-bound rider. They are not gluing theorems and they
are not infinite families. No missing source datum is required for
the infinitude question: the census row at `td=8` is unique of
equal-`w` type `(2,3)`, and the finite-`L` theorem does not read
any further entry. A finite typed discriminator for *which* of the
finitely many surviving `L` are T1-and-budget alive at a named
later entry is the one-step/Sol56 menu already used in §5, run at
that entry's `(w,M,budget)` — it is a finite check, not a missing
global datum.

---

## 7. Outcome meanings, and the stop condition

**`U2_REDUCED_FINITE`** (this report). At every fixed `(td, entry)`,
the U2 regime contributes only finitely many P1-legal terminals.
The infinite reduced merge-child sequence is quotiented by P0/P1.
Together with the reviewed U1 semilinear quotient (constant /
periodic child) and the cap-free P0 chain theorem, the reduced
ledger at merges and chains is finite in every currently
proved-unbounded reduced-state regime.

**`U2_INFINITE_FORMAL_COUNTERFAMILY`** would have meant an explicit
infinite AP of `L` with T1-alive `(Rad,S)`, MP2-alive `M`, and a
uniform P0 route to a P1 terminal inside the shared St 9.4 budget,
at a named entry. Not found; §4 forbids it at pattern/budget
scope.

**`PARTIAL`** would have meant a missing source datum or an
unresolved dirty-trunk Diophantine. The `td=8` row is present in
the current census; the dirty-trunk Diophantine reduces to
`L+1` dividing a bounded integer.

**Stop.** Do not spend a further desk day on unbounded `lex`.
Remaining U2 work, if any, is a finite cell list (T1 solves plus
the Sol56 menu at the finitely many `L` that the divisor condition
permits), then Statement-3.9 gluing of those cells, which is a
different object. The highest-leverage object after this report
is the U1 coefficient/gluing question named by the hostile review
§11 (realisability of `t^r-A` at infinitely many admissible
`nu>=2`), not U2.

---

## 8. Packet

`cases/m2_u2_nu1_unbounded_lex_grok46_20260829/` — exact
`int`/`Fraction`/symbolic arithmetic, stdlib only, no floats, no
search caps, no engine import, no network, no CAS. Cap tokens
(`NUCAP`, `MAXNU`, `--cap`) are refused by both executables. The
T1 identity is a self-contained exact sparse multivariate
polynomial class over `Q` (the same class used to certify T1-GEN
in the reviewed Opus packet, copied for self-containment).

```text
a23403a231f0418b0e036248baa6d3846933335a50b3fcc421bf8edb4d626779  polyexact.py
e47cb02b44291fd5d964211f9347a4c0d0d4bfedba09c4e5a42c71c6b02bcc70  u2_core.py
ed9eefec8d648915551cbb3faa5a61c784a51fb35f08181915f37f4924cdac99  controls.py
655474012b308365f1b14de28f1237c872d8a975ac8eda6a9f818fdc1baa204a  emit_u2.py
1018470f35c8e73748f7ed1a31d0016022c19dfce861615e903301286309096d  test_u2.py
8b4175a42e673e096650deeba4ac67dc27c64275b11bdbf72e676e6daefbd811  README.md
a6670fa1b2d5dfecbf37ced757fac081b6c74334b88aa7e041fc90f59354b6b6  charged emission body
52eafb22bae8c6ca2d4a94ea4cf1348e310851de1d1f72bb2c090694b62d5f81  charged emission file (/tmp/u2.json)
```

---

## 9. Replay

```sh
cd cases/m2_u2_nu1_unbounded_lex_grok46_20260829
python3    emit_u2.py --output /tmp/u2.json
python3 -O emit_u2.py --output /tmp/u2-O.json
cmp /tmp/u2.json /tmp/u2-O.json
python3    test_u2.py
python3 -O test_u2.py
```

Observed:

```
emit_sha256 a6670fa1b2d5dfecbf37ced757fac081b6c74334b88aa7e041fc90f59354b6b6
t1_identities 8
r2_parity 11
td7_inversion_fitting 0
td8_direct_mp2_alive 0
U2_EMIT_PASS
CMP_OK
U2_NU1_TEST_PASS checks=148
U2_NU1_TEST_PASS checks=148
```

Cap refusal (both executables): `--cap` exits 2 with `REFUSED cap token`.

Independent `/tmp` work, not imported from the packet: absorbed
versus naive-eta identities; `r=2` even/odd recurrence; D9 binomial
residues; power-family `L=1+r k`; Dickson consecutive; P3
`(2,2t)` closed forms; cap-free tail inversion; `td=8` direct
and post-`(A)` one-step. The census of L6-surviving entries was
read from `book_offaxis.census` / `book_enum.entries` as in the
hostile review; the capped `close_p` menu was not used.

Files written: this path, and
`cases/m2_u2_nu1_unbounded_lex_grok46_20260829/`. Scratch under
`/tmp` only.

**Outcome: `U2_REDUCED_FINITE`.**

---

## 10. Scope firewall

This report does not assert: a landing theorem; completeness at
any `td`; restoration of a prime-`td` exclusion; realisability of
any cell; Statement-3.9 gluing; `G2-BD`; a cofinal bound on `td`;
or any JC2 consequence. It does not access `jc2-lean`. It does
not change any panel status: P5's `0 DEAD / 0 ALIVE / 2691 OPEN`
remains the honest grid-level statement. What changes is that
regime U2, the one place the reduced merge-child state set was
proved infinite, is now finite at the P1-terminal ledger of every
fixed `(td, entry)`, at recorded pattern / superset scope.

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = 49fdda2b84e4a405f6432239546826a943326a5357f10efb26eaa8b2a149a1b6
(sha256 of this file up to and including the line "*Report body ends...*", i.e. of the first 24143 bytes)
