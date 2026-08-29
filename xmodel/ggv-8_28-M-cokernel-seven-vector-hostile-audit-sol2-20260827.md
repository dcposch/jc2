# Hostile audit: the seven-dimensional cokernel of the `8_28` operator `M`

Date: 2026-08-27  
Reviewer lane: `a1_total_lift_design` / Sol2  
Target: §3.1 and Card B of
`xmodel/ideation-20260827T1349Z-grok.md`, SHA-256
`941aea0c2a664feb10abca88c9daeb4b07e0c8a2f7265f6f0b7e67f3e5bd2b61`.

## Overall verdict

**ALGEBRAIC LEMMA CONFIRMED; “NO RAW-PROVENANCE NEEDED” INTERPRETATION
REFUTED/REPAIRABLE.**

For

\[
 H=X^8-1,
 \qquad
 M(Y)=4HY'+6H'Y=4(X^8-1)Y'+48X^7Y,
\]

the following statements over `Q` are exact:

1. `M:Q[X] -> Q[X]` is injective.
2. As **Q-vector spaces**,

   \[
   \mathbb Q[X]=\operatorname{im}M\oplus \mathbb Q[X]_{\leq 6}.
   \]

3. Every polynomial has a unique, explicitly computable seven-coordinate
   remainder modulo `im(M)`.
4. `[1]` and `[H]` are nonzero, with
   `[H]=-(12/13)[1]`.
5. For every `n>=0`, if `V_n=Q[X]_{<=n}`, then
   `V_{n+7}=M(V_n) direct-sum V_6`, so the truncated cokernel has dimension
   seven.

The claimed strategic conclusion needs a correction.  A seven-vector is a
complete membership test **after an actual global polynomial `E_22` has been
produced**.  Rootwise R2 carrier data determine only a class modulo `H` and
do not determine this global polynomial or its seven-vector.  In fact the
unknown `H`-multiple can change the seven-vector arbitrarily:

\[
 r(HX^i)=-\frac{12}{i+13}X^i,\qquad 0\leq i\leq6,
\]

where `r` is the unique remainder map.  Thus

\[
 r\circ(H\cdot):V_6\longrightarrow V_6
\]

is a diagonal isomorphism.  Without a source-pinned raw-to-Morse compiler
that fixes the `H`-multiple, the proposed 16 factorwise types do **not** carry
one intrinsic seven-vector each.  The cokernel is the correct seven-slot
*target for* the provenance compiler, not a replacement for that compiler.

## Verdict table

| Charged point | Verdict |
|---|---|
| Monomial formula and leading degree | **CONFIRMED** |
| Injectivity on `Q[X]` | **CONFIRMED** |
| `Q[X]=im(M) direct-sum Q[X]_{<=6}` | **CONFIRMED as Q-vector spaces** |
| Explicit reduction and uniqueness | **CONFIRMED**, supplied below |
| Class of `1` | **CONFIRMED nonzero** |
| Class of `H` | **CONFIRMED nonzero**, equal to `-12/13` times `[1]` |
| `M(X/48)=1+(13/12)H` | **CONFIRMED** |
| Every `V_n -> V_{n+7}` cokernel has dimension seven | **CONFIRMED for `n>=0`** |
| Seven-vector decides membership of a fixed global `E_22` | **CONFIRMED** |
| Rootwise/factor type alone determines that seven-vector | **NOT ESTABLISHED; generally false without a lift convention/provenance** |
| The global `H`-multiple question is solved without raw provenance | **REFUTED** |
| Smallest repair | **Rename it the seven-coordinate output/obstruction target of the raw-provenance compiler** |

No correction is needed to R1, R2, or R3 at their promoted scopes.

## 1. Exact monomial action and injectivity

For `n>=0`, direct differentiation gives

\[
 \boxed{M(X^n)=4(n+12)X^{n+7}-4nX^{n-1}},             \tag{1.1}
\]

where the second term is zero at `n=0`.  If `Y` is nonzero of degree `d`
and leading coefficient `c`, (1.1) gives

\[
 \deg M(Y)=d+7,
 \qquad
 \operatorname{lc}M(Y)=4(d+12)c\neq0.                \tag{1.2}
\]

Therefore `M(Y)=0` forces `Y=0`.  This confirms injectivity.  It also shows
that a nonzero element of `im(M)` has *total degree* at least seven.  It need
not have valuation at least seven: for example

\[
 M(X)=52X^8-4.                                        \tag{1.3}
\]

This distinction is harmless for the direct-sum proof but should be kept
when saying “lowest image degree.”

## 2. Exact reduction algorithm

Let `P` be a polynomial.  If its current degree is `m>=7` with coefficient
`p_m`, set

\[
 c_m=\frac{p_m}{4(m+5)}
\]

and replace

\[
 P\longleftarrow P-c_m M(X^{m-7}).                    \tag{2.1}
\]

The `X^m` term cancels, and the only new term is

\[
 \frac{m-7}{m+5}p_m X^{m-8}.                          \tag{2.2}
\]

Hence the degree strictly decreases.  Iterating terminates with
`r(P) in V_6`, and the accumulated monomials `c_m X^{m-7}` give an explicit
`Y` satisfying

\[
 P=M(Y)+r(P).                                          \tag{2.3}
\]

The sum is direct: if `M(Y)` lies in `V_6`, (1.2) forces `Y=0`.  Thus both
`Y` and `r(P)` are unique.  This proves the infinite direct-sum statement,
not merely a dimension heuristic.

Equivalently, modulo `im(M)`,

\[
 X^7\equiv0,
 \qquad
 X^m\equiv\frac{m-7}{m+5}X^{m-8}\quad(m\geq8).        \tag{2.4}
\]

For `m=8k+j`, `0<=j<=6`, repeated reduction gives

\[
 r(X^{8k+j})=
 \left(\prod_{s=1}^{k}
 \frac{j+8s-7}{j+8s+5}\right)X^j,                    \tag{2.5}
\]

while `r(X^{8k+7})=0`.  Formula (2.5) is a replayable closed form for all
seven quotient coordinates.

## 3. Truncations

For `n>=0`, (1.1) maps `V_n` into `V_{n+7}`.  Injectivity gives
`dim M(V_n)=n+1`; Section 2 gives `M(V_n) intersect V_6=0`.  Since

\[
 (n+1)+7=n+8=\dim V_{n+7},
\]

one obtains

\[
 \boxed{V_{n+7}=M(V_n)\oplus V_6}.                    \tag{3.1}
\]

Thus the stated finite truncation has cokernel dimension seven for every
`n>=0`.  This is a degree-filtered statement.  It should not be silently
relabelled as a quotient-ring statement: `im(M)` is a Q-linear subspace, not
an ideal.  Indeed `X^7=M(1)/48` lies in `im(M)`, while `X^8` does not by
Section 4.

## 4. The classes of `1` and `H`

Since a nonzero image has degree at least seven,

\[
 r(1)=1\neq0.                                          \tag{4.1}
\]

Equation (1.3) gives

\[
 [X^8]=\frac1{13}[1].                                 \tag{4.2}
\]

Therefore

\[
 \boxed{[H]=[X^8-1]=-\frac{12}{13}[1]\neq0}.          \tag{4.3}
\]

The charged fixture is exact:

\[
 M(X/48)=\frac{13}{12}X^8-\frac1{12}
        =1+\frac{13}{12}H.                            \tag{4.4}
\]

Equations (4.3)--(4.4) are the same relation.  Grok's shorter test
`M(aX+b)=52aX^8+48bX^7-4a` is also sufficient: any preimage of a degree-eight
polynomial would have degree one by (1.2), and coefficient comparison makes
`M(aX+b)=H` impossible.

## 5. The decisive hostile check: arbitrary `H`-multiples fill the cokernel

For `0<=i<=6`, applying (2.4) once gives

\[
 r(X^{i+8})=\frac{i+1}{i+13}X^i.
\]

Consequently

\[
 \boxed{r(HX^i)
 =r(X^{i+8}-X^i)
 =-\frac{12}{i+13}X^i}.                               \tag{5.1}
\]

Every diagonal coefficient is nonzero over `Q`.  Hence an arbitrary
seven-vector `e=sum_(i=0)^6 e_iX^i` can be cancelled by the degree-at-most-six
multiple

\[
 q_e=\sum_{i=0}^6\frac{i+13}{12}e_iX^i,
 \qquad
 r(e+Hq_e)=0.                                         \tag{5.2}
\]

In particular, `e=1` gives `q_e=13/12` and recovers (4.4).

This is the smallest countercheck to the strategic overreading.  R2 says
explicitly that root-local carrier data do not control the global
`H`-multiple.  But (5.1) shows that this omitted multiple is capable of
moving in **every** cokernel direction.  Knowing a branch or factor pattern
modulo `H` therefore cannot assign a canonical seven-vector.  Choosing the
unique degree-`<8` interpolation of local values merely chooses one
representative; adding `Hq` preserves every rootwise value and can change its
remainder arbitrarily.

Accordingly, Card B's proposed “16 types, one seven-vector each” is not yet
licensed.  The 16 zero/nonzero patterns on the four Q-irreducible factors of
`H` may be a valid finite factor census, but a pattern does not determine the
global polynomial lift.  It also does not by itself fix continuous carrier
values, deck data, or the lower-jet cleanup.  Those are exactly the raw
provenance obligations already retained by R1/R2.

Indeed, after the determinant unit is restored, both R2 branches impose the
same rootwise scalar equation `E_22(c)=1` at every root `c` of `H`.  The
degree-`<8` interpolation of those scalar values is therefore simply `1` for
all 16 patterns.  Any distinction between the patterns must enter through
the carrier polynomials and the global `Hq` term, neither of which is fixed by
the scalar interpolation.  An independent raw support bound could restrict
the allowed `q`, but deriving that bound and its attainable image is again a
provenance calculation.

## 6. What the seven-vector does accomplish

The lemma is still useful and should be retained at its exact strength.  Once
a source-pinned compiler has produced a literal global `E_22`, the seven
coordinates of `r(E_22)` are necessary and sufficient for
`E_22 in im(M)`.  The compiler no longer needs an unbounded polynomial
membership solve: it can reduce by (2.1) and emit seven exact rationals (or
seven expressions in the surviving raw parameters).

The honest workflow is therefore

```text
raw 2S/3S rows and source coefficients
  -> replayed global Morse/approximate-root cleanup
  -> literal polynomial E22, including its H-multiple
  -> exact reduction r(E22) in Q[X]_{<=6}
  -> test the seven coordinates.
```

This is a substantial compression of the **output test**, but not of the
input/provenance theorem.  It supplies a seven-slot field for `G2-PSC`; it is
not `G2-PSC`, a face exclusion, or a global landing theorem.

The smallest wording repair to Grok §3.1 is:

> `coker_Q(M)` is canonically represented by `V_6`.  It is the complete
> seven-coordinate obstruction for a *fixed, globally produced* `E_22`.
> Rootwise carrier types do not determine this vector because the unknown
> `H`-multiple maps surjectively onto `coker_Q(M)`; raw provenance remains
> necessary to compute it.

Card B should therefore be redesigned to compile raw provenance first and
then reduce its actual output.  It must not stop after 16 interpolated
rootwise patterns unless a separate theorem proves that the interpolation is
the raw global representative.

## 7. History check and independent replay

The pre-`1349Z` history contains the operator but not this cokernel theorem:

- R1 (`66121bdd...`) proves the leading-degree law, the fixture
  `M(X/48)=1+(13/12)H`, and nonmembership of `1` inside its two named
  ansatzes.
- R2 (`0f8f3833...`) proves the two local carrier types and explicitly leaves
  the global `H`-multiple outside its conclusion.
- The R3 producer (`b1851156...`) uses the same endpoint operator only for
  its artificial squarefree replacement edge.  Its later review
  (`27fcd256...`) confirms that narrow result but is not counted as a
  pre-`1349Z` source.
- Repository searches before the `1349Z` reports find unrelated cokernel
  modules but no statement `Q[X]=im(M) direct-sum V_6`, no monomial recurrence
  (2.4), and no calculation (5.1).

Thus the vector-space lemma and the diagonal `H`-multiple calculation are new
relative to the checked campaign history.  The latter is also why the
no-provenance interpretation cannot be promoted.

A desk-scale exact-Q replay checked (1.1)--(5.2) for monomials through degree
39, reconstructed an independent dense degree-60 rational polynomial from
`M(Y)+r`, verified `r(1)=1`, `r(H)=-12/13`, and verified the seven diagonal
values in (5.1).  These checks are guards; the displayed identities are the
proof.

## Scope firewall

- The direct sum is a direct sum of Q-vector spaces, not ideals or
  `Q[X]`-modules.
- The seven-vector decides membership only for a fixed global polynomial.
- Rootwise equality modulo `H` does not determine a global lift.
- The lemma neither supplies raw `2S/3S` provenance nor identifies a formal
  Morse chart with a polynomial source transformation.
- Nothing here excludes the original `8_28` family, proves `G2-PSC` or
  `G2-BD`, or proves JC2.
