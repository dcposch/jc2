# Source-custody audit — R7R2 Theorems R1/R2 and the exponential-factor claim

**Auditor:** Sol Ultra subreview (`/root/r7r2_source_pin`)  
**Date:** 2026-08-27  
**Target:** `xmodel/ggv-r7r1-rank-two-irregularity-hostile-review-opus5-20260827.md`  
**Target SHA-256:**
`6e4f197aaa3c68983cd9e479e8d1e41994d33d277a9413f816ea3a664302d759`
(`MATCH`, recomputed before review)  
**Status:** `SOURCE-PINNED / CONFIRMED WITH SCOPE REPAIRS`

## 0. Executive verdict

| Claim | Verdict | Exact repair |
|---|---|---|
| R1: `h^1(E) <= h^1(A)+h^1(B)` for `0 -> A -> E -> B -> 0` on the fixed affine curve `U` | **CONFIRMED** | Regularity is not needed for the inequality itself.  What is needed is an actual short exact sequence of finite-rank connections and finite-dimensional de Rham cohomology. |
| R1 closes a general rank-two escape | **NOT ESTABLISHED** | It closes only a rank-two object exhibited as an extension of the two named row connections.  No such filtration is automatic from “keeping two series together”; irreducible rank two is outside R1. |
| R2: polynomial-client `P,W` are algebraic and their cyclic `D_(X,s)`-modules are regular holonomic | **CONFIRMED over `C`**, with the ambient module made explicit | Define each cyclic module inside the algebraic localization/direct image of a finite étale cover on a dense open.  Do not write that the possibly singular normalization itself has a structure-sheaf `D`-module without this reduction. |
| R2 gives zero irregularity at `s=0`, `Z(H)`, and infinity | **CONFIRMED WITH TERMINOLOGY REPAIR** | On the surface the statement is `IR_D(M)=0` (vanishing irregularity complex) for every divisor `D`; a scalar `Irr_x` belongs to a curve connection.  Infinity is included only after specifying an algebraic smooth compactification and algebraic direct image. |
| Algebraic six operations preserve regular holonomicity for nonproper maps | **CONFIRMED** | This is HTT Theorem 6.1.5 for morphisms of smooth **algebraic** varieties.  In the analytic category, direct image requires properness (HTT Theorem 6.1.11). |
| “An exponential twist is the only escape” | **OVERSTATED** | Safe statement: six operations applied only to regular-holonomic inputs cannot create irregularity; an irregular input or a non-regularity-preserving construction is necessary.  Formal exponential factors diagnose positive slope after ramification (and, on a surface, after modification), but this does not force a global rank-one twist by `e^f` with rational `f` on the original base. |

The two mathematical cores therefore survive.  R2 is a genuine closure of
automatic irregularity for the individual algebraic-function clients `P` and
`W` and for anything obtained from those regular objects by algebraic six
operations.  R1 is a genuine extension-subadditivity lemma, not a theorem
about every possible higher-rank client.

## 1. Theorem R1 — independent derivation and exact scope

Let `U` be a connected smooth affine complex curve and let

```text
0 -> A -> E -> B -> 0
```

be a short exact sequence of algebraic finite-rank integrable connections on
`U`.  In the campaign application,
`U = A^1_C - Z(H)` and `r = #Z(H)` counts distinct geometric roots.

The de Rham complexes form a short exact sequence.  Since `U` is affine of
dimension one, their hypercohomology vanishes above degree one.  The relevant
part of the long exact sequence is

```text
0 -> H0(A) -> H0(E) -> H0(B) --delta--> H1(A)
  -> H1(E) -> H1(B) -> 0.
```

Writing `d = rank(delta)` gives

```text
d = h0(A) + h0(B) - h0(E),
h1(E) = h1(A) + h1(B) - d
      = h1(A) + h1(B) - (h0(A)+h0(B)-h0(E)).
```

Thus

```text
h1(E) <= h1(A)+h1(B),
```

with equality exactly when `delta=0`.  This proves R1.  Regular singularity is
not used in this diagram argument; it is used in the next numerical
specialization.

For a regular rank-`n` connection on this `U`, Deligne comparison identifies
algebraic de Rham cohomology with cohomology of its rank-`n` local system, and
the Euler characteristic is

```text
chi_dR(E) = n chi_top(U) = n(1-r).
```

Since `H2_dR(U,E)=0`,

```text
h1(E) = h0(E) + n(r-1).
```

For rank two, `h0(E)<=2`; on connected `U`, equality means the monodromy is
trivial and hence the connection is trivial.  A nontrivial rank-two regular
connection therefore satisfies `h1(E)<=2(r-1)+1`.

### R1 scope failure in the reviewed inference

R1 compares `E` with `A` and `B` only after an exact filtration with precisely
those constituents has been supplied.  It does **not** compare an arbitrary
rank-two connection with any chosen pair of rank-one row connections.

A minimal numerical countercheck exposes the distinction.  Take two
nontrivial rank-one regular connections `A,B` on `U`; then
`h1(A)+h1(B)=2(r-1)`.  The nontrivial rank-two connection
`E = O_U direct-sum L`, with `L` a nontrivial regular rank-one connection, has
`h0(E)=1` and `h1(E)=2(r-1)+1`.  There is no contradiction: this `E` is not an
extension of the chosen `A,B`.

Accordingly, the promotable consequence is:

> Packaging two reviewed row connections into an extension cannot increase
> their total `H1_dR` capacity.  A proposed coupled rank-two client must first
> exhibit that extension (or another filtration) before R1 applies.

The sentence “the rank-two escape is quantitatively empty even if the object
existed” is too broad without that clause.

## 2. Theorem R2 — algebraicity

Work first over `C`; this is the scope of the regular-holonomic sources below.
Let `F,G in C[X,t]`, let `P` satisfy

```text
P^8 = F(X,sP),
```

and set `W=G(X,sP)/P^12` wherever this expression is defined.  Write
`F(X,t)=sum_(j=0)^d F_j(X)t^j`.  Then `P` is a root of

```text
A(T)=T^8-sum_(j=0)^d F_j(X)s^jT^j in C(X,s)[T].
```

This polynomial is nonzero.  If `d!=8`, its largest occurring `T`-degree makes
that immediate.  If `d=8`, the coefficient of `T^8` is
`1-F_8(X)s^8`, which is also nonzero because `s` is transcendental over
`C(X)`.  Monicity is unnecessary.  Hence `P` is algebraic over `C(X,s)`, and
`W`, being rational in `X,s,P`, is algebraic as well.

This algebraicity step is valid over any characteristic-zero coefficient
field.  The source-pinned regular-holonomic conclusion below is stated over
`C`.  For a particular finite polynomial client over another characteristic-
zero field, one may spread its finitely many coefficients to a finitely
generated subfield and choose a complex embedding; descent back to the
original field is not claimed by this audit.

## 3. R2 — clean regular-holonomic construction

The review's phrase “embed in a localization of `pi_* O_Y` for the finite
normalisation” has the right idea but skips a singular-source issue: the
normalization of a surface need not be smooth, so `O_Y` should not casually be
used as a classical `D_Y`-module.

The clean proof avoids that issue.

1. Let `L/C(X,s)` be a finite extension containing `P,W`.  Shrink
   `S=A^2_C` to a principal dense open `j:V -> S` so that the normalization
   `q:Vtilde -> V` in `L` is finite étale and `P,W` are regular on `Vtilde`.
   Characteristic zero gives separability; clearing denominators and removing
   the discriminant gives such a `V`.  Both `V` and `Vtilde` are smooth.
2. `O_Vtilde` with its trivial connection is regular holonomic.
   HTT Theorem 6.1.5 sends it under the finite algebraic direct image to the
   regular-holonomic connection `q_+ O_Vtilde` on `V`.
3. The cyclic sub-connections generated by the sections `P` and `W` are
   regular: the category of regular holonomic modules is closed under
   submodules (HTT Definition 6.1.1 and the paragraph immediately following
   it).
4. Apply the algebraic open direct image `j_+`.  HTT Theorem 6.1.5 applies to
   this nonproper algebraic morphism.  The cyclic modules

   ```text
   M_P := D_S . P,       M_W := D_S . W
   ```

   are understood as submodules of the appropriate cohomology of
   `j_+ q_+ O_Vtilde`; hence they are regular holonomic.

This proves the corrected R2 statement.  It also shows exactly where
“algebraic” is load-bearing.  HTT Theorem 6.1.11 gives analytic direct-image
preservation only for proper maps, whereas Theorem 6.1.5 has no properness
hypothesis in the algebraic category.

## 4. Divisors, the surface invariant, and infinity

On a smooth surface, irregularity along a hypersurface is a constructible
**irregularity complex** `IR_D(M)`, not in general a single number.  Mebkhout's
regularity criterion, as summarized precisely by Roucairol Definitions 2.2
and 2.6, says that a regular holonomic object has zero irregularity complex
along every hypersurface (and, algebraically, after projective embedding).

Therefore R2 yields

```text
IR_{s=0}(M_P)=IR_{s=0}(M_W)=0,
IR_{Z(H)}(M_P)=IR_{Z(H)}(M_W)=0.
```

To include infinity, choose an algebraic smooth compactification, for example
`i:S=A^2 -> P^2` (or a resolved divisor completion).  Algebraic Theorem 6.1.5
gives `i_+M_P,i_+M_W` regular holonomic, so their irregularity complexes along
the boundary divisor vanish.  HTT Theorem 6.1.12 is the equivalent
compactification test: an algebraic holonomic module is regular iff its
analytic meromorphic extension on a divisor completion is regular.

For any curve slice or curve-valued client obtained by algebraic inverse/direct
image, the induced meromorphic connection is regular, and its usual scalar
irregularity at every point is zero.  Ramification of the algebraic functions
at `Z(H)` is compatible with this conclusion; algebraic branching does not
create positive slope.

This validates “zero at `s=0`, `Z(H)`, and infinity” after replacing the
surface shorthand `Irr=0` by the precise assertions above.

## 5. Algebraic six operations and what they actually close

HTT Theorem 6.1.5 states for a morphism of smooth algebraic varieties that
duality, both direct images, and both inverse images preserve the bounded
derived category with regular-holonomic cohomology.  Tensor/Hom are obtained
from external product, diagonal inverse image, and duality.  Consequently:

> Any object constructed solely from the regular-holonomic clients `M_P,M_W`
> (and other regular-holonomic campaign inputs) by algebraic six operations,
> subquotients, extensions, and cohomology remains regular holonomic.

This is the source-backed closure statement.  It rules out creating positive
irregularity “for free” by an ordinary algebraic direct image, including a
nonproper one.  It does not rule out an additional differential object that is
not shown to lie in this regular closure.

## 6. “Exponential twist is the only door” — exact boundary

There are two distinct statements in the review; only the first is fully
justified.

### 6.1 Justified

If every input is regular holonomic and every operation is one of the
algebraic regularity-preserving operations above, the output cannot be
irregular.  Hence a successful irregularity avenue must introduce either:

- an irregular input (an exponential module is the standard example), or
- a construction/limit not covered by that closure theorem, together with a
  proof that the resulting finite-rank holonomic object is forced by Keller
  data.

Roucairol Definition 3.1 and Remark 3.3 give a canonical sufficient example:
twisting a regular module by an exponential meromorphic connection can produce
an irregular holonomic module.

### 6.2 Not justified as written

Levelt--Turrittin is a **formal local classification**, not a global generation
theorem.  On a curve, after finite ramification, a meromorphic connection
formally decomposes into factors `E^phi tensor R_phi`, with `R_phi` regular.
On a surface, Kedlaya Theorem 6.4.1 obtains good formal structure only after a
sequence of point blowups (and the local definition permits ramified covers).
Thus positive slope is detected by nonconstant polar exponential factors only
after those operations.

It does **not** follow that an irregular campaign client must globally be a
rank-one twist

```text
d + df + nu dH/H            with f rational on the original U.
```

The Airy connection is a standard warning: it is rank two and irregular at
infinity, and its formal factors have ramified phases
`+/- (2/3)z^(3/2)` rather than a rational phase on the original `z`-line
(Guzzetti, Section 4.1).  Likewise, a surface connection may have turning
points before modification.

Therefore the review's proposed rational exponential gate is a useful
**sufficient revival test**, not a necessary and exhaustive one.  The narrow
promotable wording is:

> Six operations on the present regular-holonomic algebraic inputs cannot
> produce positive irregularity.  Any revival must specify an additional
> finite-rank holonomic client outside that regular closure and prove it is
> Keller-forced.  A nonzero formal exponential factor after the appropriate
> ramification/modification is the local certificate of positive slope; a
> global rational exponential twist is one concrete way, not the only proven
> way, to obtain such a certificate.

## 7. Exact source pins

All sources below were opened and the cited statements checked.  These are
author monographs/papers or the standard technical monograph, not secondary
web summaries.

1. **Hotta--Takeuchi--Tanisaki, _D-Modules, Perverse Sheaves, and
   Representation Theory_**,
   [full book PDF](https://ananddeopurkar.org/seminars/mhm/hottaetal.pdf).

   - Proposition 5.3.4, printed pp.153--154 (PDF pp.160--161): regular
     integrable connections are closed under short exact sequences.
   - Proposition 5.3.6, printed p.154 (PDF p.161): regularity is equivalent to
     regularity on some/every divisor completion, so algebraic regularity
     includes infinity.
   - Definition 6.1.1 and following paragraph, printed pp.161--162 (PDF
     pp.167--168): regular holonomic modules and closure under submodules,
     quotients, and extensions.
   - Theorem 6.1.5, printed p.162 (PDF p.168): duality and algebraic direct and
     inverse images preserve `D^b_rh` for **any morphism of smooth algebraic
     varieties**.
   - Theorem 6.1.6, same page: curve-testing criterion.
   - Theorem 6.1.11, printed p.163 (PDF p.169): in the analytic category,
     inverse image is unrestricted but direct image is stated for proper maps.
   - Theorem 6.1.12, same page: divisor-completion/analytification test for an
     algebraic holonomic module.

2. **Deligne, _Équations différentielles à points singuliers réguliers_, LNM
   163 (1970)**,
   [IAS author-hosted scan](https://publications.ias.edu/sites/default/files/Number9.pdf).

   - Theorem II.6.2, printed p.99 (PDF pp.100--101): algebraic/analytic de Rham
     comparison for a regular integrable algebraic connection.
   - Section II.6.19, printed p.109 (PDF p.111): the Euler characteristic of
     the associated rank-`n` local system is `n chi_top(X)`; together with the
     comparison theorem this gives the regular de Rham Euler formula used in
     R1.
   - Theorem II.5.9, printed p.97 (PDF pp.99--100): regular algebraic
     connections correspond to analytic connections/local systems; this is
     background, not needed to replace the direct-image proof of R2.

3. **Céline Roucairol, “Irregularity of an analogue of the Gauss--Manin
   systems,” Bull. SMF 134 (2006), 269--286**,
   [journal PDF](https://smf.emath.fr/system/files/2017-08/smf_bull_134_269-286.pdf).

   - Definitions 2.1--2.2, journal p.273 (PDF p.4): irregularity complex along
     a hypersurface and analytic regularity by its vanishing.
   - Definitions 2.5--2.6 and Theorems 2.7--2.8, journal p.274 (PDF p.5):
     algebraic regularity includes the projective boundary; `O_X` is regular;
     algebraic direct image preserves regular-holonomic cohomology.
   - Definition 3.1 and Remark 3.3, journal pp.274--275 (PDF pp.5--6): the
     exponential twist and the fact that it is holonomic and can be irregular.

4. **Kiran Kedlaya, “Good formal structures on flat meromorphic connections,
   I: Surfaces”**, [arXiv:0811.0190](https://arxiv.org/abs/0811.0190).

   - Definition 4.3.1, printed p.40: a good decomposition has local factors
     `E(phi_alpha) tensor R_alpha` with regular `R_alpha`.
   - Theorem 6.4.1, printed p.59: on a smooth surface with normal-crossings
     polar divisor, a good formal structure is obtained after a modification
     by point blowups; the surrounding definitions allow the necessary
     ramified extension.  This is why a single global rational phase is not a
     consequence of formal classification.

5. **D. Guzzetti, “Uniqueness of asymptotic solutions for linear systems of
   ODEs with isolated singularities of general type,” Izvestiya: Mathematics
   90:1 (2026), 87--108**, [publisher full text](https://www.mathnet.ru/eng/im9694),
   [journal PDF](https://www.mathnet.ru/links/0d71bf9855652d8b6183ca0201495dae/im9694_eng.pdf).
   Section 4.1, journal p.101, writes the Airy formal exponent matrix with phases
   `+/- (2/3)z^(3/2)` and slope `3/2`, providing a concrete ramified
   higher-rank counterexample to “rational rank-one phase on the base is
   necessary.”

## 8. Promotion boundary

The source-pinned conclusions prove no Keller-pair nonexistence, survivor
exclusion, endpoint theorem, or JC2 result.  They establish only:

1. exact-sequence subadditivity of row de Rham capacity on the fixed affine
   curve;
2. algebraicity and regular holonomicity of the individual polynomial-client
   functions `P,W` over the complex `(X,s)` surface;
3. vanishing of their irregularity complexes at all divisors, including the
   projective boundary; and
4. preservation of that regularity under algebraic six operations.

They do not close an unspecified irreducible higher-rank client, a nonlinear
support/descent object, or a branch-cycle CSP.  They also do not make a global
rational exponential twist a necessary form of every possible irregular
revival.

## 9. Custody and firewall

- `jc2-lean` was not entered, listed, searched, read, built, status-inspected,
  or modified.
- No canonical ledger, producer, frozen case, adapter, or AWS job was changed.
- No CAS or heavy computation was run.  Temporary source PDFs/text were kept
  under `/tmp` only.
- Exactly one repository file was written: this source-audit report.
