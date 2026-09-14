# D125 pure center: a uniform low-alpha restriction, with the remaining gap

2026-09-07. **PASS for the necessary bound 3 ord(alpha) >= 2j; GAP for
ord(alpha) >= j.** This follows from the actual moving-reference source and
accepted14v first contact, not an assumed quadratic/Pell residue. It retains
all scalar centralizer kernels and intermediate coefficients. The interval
2j/3 <= ord(alpha) < j remains unresolved. No guarded point, finite-arc
existence, generic-fiber exclusion, runtime gain or JC2 conclusion follows.

Inputs are accepted14c/f/g/v at their stated source/centralizer trust. Their
whole producer proofs were read; no new classification or primary theorem is
imported. The earlier pure-uniform producer supplies history only, not a
premise. Its Fable gate and countercontrol were not consumed. The original
07:57 lease/empty partial survived the interruption; this same task resumed
at21:39, with no intervening source/worker activity.

## 1. Exact source-derived valuation theorem

Consider a genuine characteristic-zero K[[s]] arc in the literal source, with
nonzero k(s) of order m and pure exceptional center. Use the actual normalized
references and notation of14v:

    R_s=R_{t(s)},  R=R_-3=p²V,  V=g³+p³-3p,
    F=A-R_s³-alpha R_s,  ord(F)=j<m,
    F_j=R C,  C even, C(0)=0, V does not divide C.

C is a regular polynomial. Its degree/weight/ordinaryness conditions are as
in14v, not new free hypotheses. Let a=ord(alpha) be finite; alpha=0 is not
addressed by a finite a. The accepted scalar-reference normalization gives
ord(G)>=2j and ord(delta)>=j+1, and the exact identity

    [A,B]=[R_s,H]+[F,G],
    H=(3R_s²+alpha)G-delta F-(5/3)R_s F².          (1)

Since [F,G] has order at least3j and the target bracket has order3m>3j,
[R_s,H]=0 modulo s^(3j). Applying the accepted polynomial centralizer K[R]
coefficient by coefficient gives

    H=b_s(R_s) modulo s^(3j),                    (2)

where b_s has scalar coefficients. Inductively subtract the first scalar
polynomial in R_s; its moving-reference corrections occur at higher orders.
This proves (2) without freezing R_s or deleting any intermediate order.
EVERY scalar power is retained; neither its linear nor cubic coefficient is
assumed zero.

Pass to an algebraic closure of K and put L=Kbar(V). At the generic point of
V, 3p²g² is a nonzero element of L. Thus there is a unique formal change
g=g(s,z) in L[[s,z]], with initial g, satisfying R_s(g(s,z),p)=z. This is the
elementary formal implicit construction: at every successive total degree,
the new coefficient is solved by division by that fixed nonzero derivative.
It introduces no negative s or z powers. Inverting p and g here is only a
function-field proof device, not a localization of the source client.

Write F(g(s,z),p)=sum f_n(s) z^n. Every f_n has order at least j, and

    [s^j]f_0=0,       [s^j]f_1=C modulo V.         (3)

The involution sigma:(g,p)->(-g,-p) acts on L. Oddness of R_s and uniqueness
of the implicit construction give sigma(g(s,z))=-g(s,-z). Hence
sigma(f_n)=(-1)^(n+1)f_n: odd n have even coefficients, even n odd ones.

Choose the scalar Puiseux series r_s with r_s²=-alpha/3. It has order a/2
and nonzero leading scalar rho. Put U=F(g(s,r_s),p), f=ord(U). Its even part
has first term s^(j+a/2) rho C|V: higher odd n begin strictly later.
C|V is nonconstant, since a constant residue would equal zero by evaluation
at O=(0,0), contradicting V not dividing C. Therefore U is nonzero,

    f <= j+a/2,                                  (4)

and its leading coefficient psi in L is nonconstant. If it occurs earlier
than j+a/2 it is nonzero odd; if at that order its even part is the nonconstant
rho C|V. Neither case can be a scalar. No regularity of the higher Taylor
coefficients is asserted or needed.

Evaluate (2) at this critical root. Nonnegative formal valuations preserve
its precision, and the G factor vanishes exactly:

    -delta U-(5/3)r_s U² = b_s(r_s) mod s^(3j).    (5)

Let d=ord(delta), allowing infinity. If
min(d+f,a/2+2f)<3j, its coefficient in (5) is a nonzero scalar polynomial
of degree1 or2 in psi, equal to a scalar. This is impossible: a nonconstant
element of L is transcendental over the algebraically closed constant field.
This also covers equal orders, when both terms occur. Consequently

    d+f >= 3j,    a/2+2f >= 3j,
    3a >= 2j,    d >= 2j-a/2.                    (6)

All orders are measured in the original s normalization; half-integral
orders arise only in the proof's scalar quadratic extension. This is a
uniform necessary source restriction, not a finite-jet sufficiency theorem.

## 2. Correction: the scalar cubic kernel cannot be silently dropped

One can choose scalar references with [p³]G=[p¹⁵]G=0: their coefficient
matrix has units [p¹⁵](R_s³+F)=1 and [p³]R_s=t(s), with t(0)=-3.
Nevertheless this does NOT imply the cubic coefficient of b_s is zero.
Write b_s=b1 R_s+b3 R_s³+.... Literal low coefficient extraction yields,
at the precision where (2) holds,

    -b1 h = alpha e,
    b1 t-b3 h³ = alpha [p³]G +3h²e+3delta h³
                               +(5/3)alpha²h³.   (7)

Here h=t+3 and [p]G=e+delta h. My pre-interruption advisory omitted the
b3 h³ term. Its shorter formula requires a separate b3=0 normalization;
that change may alter [p³]G. Formula (7) corrects that advisory, not any
frozen earlier report. The proof above avoids this issue by retaining all
of b_s(R_s). No ell=0 valuation claim is made.

## 3. An earlier remainder really can defeat the proposed q balance

A single factored countercontrol shows why (2) alone does not force
2q=2j+a or the desired Pell residue at2j+a. Take the actual ordinary generators

    L=g+p, r=pL², C=r²-RL=3p³L(gL+1),
    r'=r+R/3, M=L+2r/3+R/9;  r'²-C=RM.

Set alpha=s^7, delta=-5s^14/3 and

    F=s^8 RC+s^11 r'+s^12 r'C/6,
    G=(5/9)s^16 RC²+(10/9)s^19 Cr'+(5/27)s^20 r'C²
                         +(5/9)s^22 M+(5/27)s^23 CM.

Then H=0 modulo s^24. The only late cancellations to check are
(5/3)s^22 R(RM+C-r'²) and (5/9)s^23 RC(RM+C-r'²).
Thus the earlier delta term cancels the first mixed square at22, while the
intermediate r'C/6 term absorbs alpha C² at23. Here j=8,a=7,q=11, so
2q=22 differs from 2j+a=23. No actual high-degree product is expanded.

For specificity define A=R³+alpha R+F and
B=R^5+gamma R+(5R²/3-5alpha/9)F+G, with gamma=delta-5alpha²/9.
This is a point of the full UNGUARDED source over K[s]/(s^24), with k=s^11.
Indeed all factors lift ordinarily; A corrections have degree<=11 and its
lower-edge bound, B corrections degree<=21. The only changing weight3 A
face is k g²p; the two B weight5 faces are (5k/3)g^8p^5 and (5k²/9)g.
Total faces and origins persist. Finally (1) gives the complete Jacobian
equations modulo s^24, since [F,G] starts at24 and the target at33. If the
optional whole B_15 slice is wanted, subtract its coefficient times entire A.

CRUCIALLY it is NOT a saturated DVR survivor. Its exact low values are

    y=-3s^7, x=2s^11, e=5s^22/9,
    x²-3ky=9s^18+4s^22,  e-5kx/9=-5s^22/9.

Both required saturated low equations fail. The inverse guard cannot hold
with nilpotent k. This countercontrol isolates the missing use of those low
equations in the remaining interval; it does not refute ord(alpha)>=j for
genuine arcs or propose an arc continuation.

## 4. Evidence and stop

Twelve capped normal/-O controls pass with identical exact rational-string
witnesses, zero Assert nodes and actual mutations of the delta sign,
intermediate coefficient, alpha G term, scalar cubic kernel and leading C.
They expand only degree<=5 actual generators, small scalar p-jets and the
four-variable UNIVERSAL formal H identity. Actual C,R³,R^5 and A/B products
remain circuits. Final witness SHA256
`84d8b19b5c139d61dcb0d3f3ae22a58c81ab2414d2852450520a1fb48252ad05`.
Replay check.py normally/-O under30wall/25CPU/512MiB with Python -B before
imports. Only final-witness*.json/final-replay.json are charged controls;
earlier outputs remain as a pre-correction test record.

The new bound (6) is PRODUCER-CHECKED pending independent review. The exact
remaining missing arrow is using full source, especially saturated lows, to
eliminate 2j/3<=a<j with all subsequent mixed and scalar terms retained.
No Pell identity was assumed, no unrelated conditional lemma substituted,
and no serial ramification computation was launched. No AWS/SSH/CAS/source
build, solver, new agent, live gate read or canonical edit occurred. Owned
inputs/artifacts are pinned in custody; transaction publication is verified
and all writers idle at handoff. STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8632`.
- Body SHA-256:
  `e09fb9531169fdb6a10f78c4e47e8c653028ec5d4a767c403e21be50a0156108`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
