# Keller sl2/Bass test: the unresolved Casimir cokernel

September13,2026; Astra primary co-research, MANUAL/UNPROMOTED, not FIRST.
Actual first13:51:49UTC. Original substantive13:59, reserve14:02, HARD14:05.

## Outcome

**NO_CLOSING_TEST.** Bass injectivity on N does not give cohomology
vanishing. The Casimir acts null-homotopically on the entire
Chevalley--Eilenberg complex, but the explicit obstruction is

    H^2(sl2,N) = H^1(sl2,N/CN) / image H^1(sl2,N).

No supplied actual-source premise makes that quotient zero. This is a
canonical isomorphism induced by the connecting homomorphism, not a
literal identification of cochains. C here denotes the Casimir operator;
scalar fields are written mathbb C in prose where confusion could arise.
There is no promotion, new operator family or follow-on selection.

Here R=mathbb C[x,y], A=mathbb C[p,q], N=R/A for an ACTUAL Keller
pair J(p,q)=1. The lifted derivatives commute, and
e=p partial_q, f=q partial_p, h=p partial_p-q partial_q,
E=p partial_p+q partial_q. N is an A-module, not an R-algebra.
Bass torsion-freeness and global source de Rham acyclicity are stipulated
inputs at their assigned tier, not independently reverified here.

## 1. Exact complex and homotopy

For any of the modules M under discussion, use basis (e,f,h), with
[e,f]=h, [h,e]=2e, [h,f]=-2f. Identify the CE complex as

    M -> M^3 -> M^3 -> M,

where a one-cochain has values (a,b,c) on (e,f,h), and a two-cochain has
values (u,v,w) on ((e,f),(e,h),(f,h)). Then

    d0(m) = (em,fm,hm),
    d1(a,b,c) = (eb-fa-c, ec-ha+2a, fc-hb-2b),
    d2(u,v,w) = ew-fv+hu.

Thus H^2=ker(d2)/image(d1), and H^3=M/(eM+fM+hM). All operator products
act on the coefficient immediately to their right.

The coefficient Casimir C=h^2+2h+4fe=E(E+2) has the following concrete
degree-minus-one homotopy:

    s1(a,b,c) = 2fa+2eb+hc,
    s2(u,v,w) = (-2eu-hv, 2fu-hw, 2fv+2ew),
    s3(z) = (hz,-2ez,2fz).

Direct substitution using the three Lie brackets gives ds+sd=C in every
degree. For example, the first component in degree1 is
(4ef+h^2-2h)a=(h^2+2h+4fe)a; the mixed terms cancel. In degree3,
d2s3=2ef+2fe+h^2=C. This is an algebraic chain identity for arbitrary
modules, requiring neither finite-dimensionality nor local finiteness.
It says that C acts ZERO on cohomology, not that a nonzero cohomology
class would give a C-torsion vector inside the coefficient module M.

## 2. Precise missing quotient and lifting map

Use stipulated Bass injectivity of C on N and set Q=N/CN. The exact
sequence 0->N --C-->N->Q->0 induces short exact sequences

    0 -> H^k(sl2,N) -> H^k(sl2,Q)
      -> H^(k+1)(sl2,N) -> 0.

The reason is that both adjoining C maps on cohomology are zero by the
displayed homotopy. Taking k=1 gives the obstruction in the outcome.

It is completely explicit. If beta is a CE two-cocycle in N^3, then
d1(s2 beta)=C beta. Consequently s2 beta modulo CN^3 is a one-cocycle
of Q, whose connecting image is [beta]. Its class must lift from
H^1(sl2,N) to kill [beta]. Neither Bass injectivity nor the given de Rham
acyclicity supplies that lift. If s2 beta actually belongs to CN^3,
division followed by cancellation proves beta exact, but this membership
is not known either. Surjectivity of C on N would make Q=0 and suffice;
it is precisely not licensed by torsion-freeness.

At the chosen formal source point, the total-degree expansion makes C
multiply degree d by d(d+2). Modulo polynomial target functions, its formal
inverse is therefore coefficientwise division by these nonzero numbers.
The missing global statement is preservation of R/A by this inverse.
The embedding into formal series does not establish that preservation.
Changing normalized target frame gives another valid Bass statement, not
a supplied compatibility or inverse taking values in N.

## 3. Actual-source attachments, with their exact limits

On A=mathbb C[p,q], the ordinary homogeneous decomposition IS available.
The positive-degree summands have invertible C and are contracted by s/C.
On the constant summand the CE differential from degree1 to degree2 is
(a,b,c)->(-c,2a,-2b). Hence H^1(sl2,A)=H^2(sl2,A)=0 and
H^0(sl2,A)=H^3(sl2,A)=mathbb C. This uses no grading of R.

Let Z be the actual reduced finite fibre p=q=0, with n points; the chosen
source point ensures n>=1. All three vector fields vanish there. Polynomial
interpolation therefore gives a well-defined surjection

    H^3(sl2,R) -> mathbb C^n.

The constant class maps to the diagonal. Thus the map H^3(sl2,A)->H^3(sl2,R)
is injective. The coefficient long exact sequence now gives

    H^2(sl2,R) isomorphic to H^2(sl2,N),
    H^3(sl2,N) surjects onto mathbb C^n / diagonal mathbb C.

This is only a SURJECTION in degree3; no exact dimension formula is
asserted for either degree. H^2 vanishing alone has not been attached to
the fixed-point count. Surjectivity of C on N would annihilate all this
cohomology and hence force n=1, but no new proof of that surjectivity was
found. ROOT's independent torsor/local-cohomology suggestion remains an
unverified lead, not an input used for these statements.

The actual-source de Rham acyclicity is also not a missing-map substitute.
There is an explicit anchor chain map from its two-derivative complex to
CE. On one-forms and two-forms it is

    a dp+b dq -> (pb,qa,pa-qb),
    c dp wedge dq -> (-pq c,-p^2 c,-q^2 c).

It commutes with the displayed differentials. Its existence does not make
it a quasi-isomorphism or make the residual CE complex acyclic. The Lie
action has isotropy away from the fixed fibre and vanishes on that fibre;
there is no supplied acyclicity theorem for the residual terms. No
localization or support cohomology is silently identified with global
source de Rham cohomology here.

## Stop and custody scope

The exact missing source map is the lift
H^1(sl2,N)->H^1(sl2,N/CN) on the obstruction classes above, or the stronger
unproved operator surjectivity CN=N. Injectivity on coefficients and
null-homotopy on cochains do not compose to either statement. No additional
topology, averaging, SL2 integration, finite-module lemma on R, or operator
enlargement is selected. The tranche stops at this explicit gap.

TASK and current COORDINATIONa14b2ebc were authenticated and read WHOLE;
COORD was read in four bounded consecutive chunks through EOF. No other
campaign or live peer report was opened. The only execution was inert
text/hash/date, apply_patch and the unchanged pinned administrative
finalizer. No science, network, AWS, process control, new agent or protected
access. Whole readback, postpins and expected verification are recorded in
the final custody. This is a scope/connection result, not JC2 progress by
new exclusion and not a different-model review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6752`.
- Body SHA-256:
  `7e8ab44c3848e2ae15bbacf3d3150b50db50fc8ccacaf81ebb0b05e92ea71ecd`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
