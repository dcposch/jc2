# Different-model FIRST: exact volume versus a marked source coordinate (Fable 5.1 gate)

Lane `exact-volume-no-coordinate-gate-fable5-20260913`. Reviewer: Fable 5.1, fresh CLI,
different model from the producer (ROOT). Date 2026-09-13, read window 12:36Z-12:41Z.
Manual mathematics only: no CAS, interpreter, network, or execution of any source.

## Charged inputs, read WHOLE before review

| File | SHA-256 (pre-review) | Lines | Read as |
|---|---|---|---|
| `inputs/COORDINATION.snapshot.md` | `a14b2ebcb3841f175b52ef0a96835a5724aee06a6008442eb3d25f98194a99bc` | 840 | eleven separate <=80-line outputs, first |
| `inputs/CLAIM.md` | `79a4d7d63f254729e9dc2fdeea866841d082be4d19476e23f268a80b2579de16` | 192 | three separate <=80-line outputs, second |

Both files end in a single 0x0a byte; no bytes were omitted or clipped.
Post-review rehash is recorded in the closing section.

## Verdict vector

1. Actual subring, localization equalities, WHOLE chart coverage: **CONFIRMED**.
2. Image of j is exactly Y minus E1, E2 (including z=0); smooth/normal; affine-base A1 ruling: **CONFIRMED**.
3. Both one-form expressions, overlap agreement, derivatives, exact zero divisor: **CONFIRMED**.
4. Unique minimal valuation of the pure top monomial; two infinity points exclude a coordinate: **CONFIRMED**. Two-boundary necessity sanity check: **CONFIRMED** (each boundary alone admits the other coordinate).
5. Monic z-eliminant coefficients, integrality of a,b, generic degree eight, full normalization, NONCONSTANT J: **CONFIRMED**.
6. Interpretation (Keller etaleness missing, no other pair decided, no JC2 closure): **CONFIRMED as scoped**; existence of any other polynomial pair on Y is **GAP** (undecided, exactly as the producer states).

No correction to the producer's stated claim was needed. Derivations follow.

## 1. Subring, localizations, whole charts: CONFIRMED

In C[u,v]: z=uv, a=u^2 v, b=u v^2, c=u(a-1), d=v(b-1). Direct expansion gives
ab=u^3v^3=z^3; zc=u^2v(a-1)=a(a-1); zd=b(b-1); bc=u^2v^2(a-1)=z^2(a-1);
ad=z^2(b-1); cd=uv(a-1)(b-1)=z(a-1)(b-1). I used these six only as identities
holding in the actual image subring B, never as a presentation of B.

Localization at (a-1)(b-1): u=c/(a-1) and v=d/(b-1) lie in B[((a-1)(b-1))^-1];
conversely B is inside C[u,v] and (a-1)(b-1)=(u^2v-1)(uv^2-1). So
B[((a-1)(b-1))^-1]=C[u,v][((u^2v-1)(uv^2-1))^-1] inside C(u,v): an equality.

Chart (t,s): u=t^-1, v=t^2+t^3 s is a field isomorphism C(u,v)->C(t,s) with
inverse t=1/u, s=u^3v-u=c. Under it uv=t(1+ts)=ta, u^2v=1+ts=a, uv^2=t^3a^2=b,
u(a-1)=s=c, v(b-1)=t^2a(b-1)=d, all polynomial, so B sits inside C[t,s].
B[a^-1] contains t=z/a and s=c, hence B[a^-1]=C[t,s][(1+ts)^-1]; B[c^-1]
contains t=(a-1)/c, hence B[c^-1]=C[t,c,c^-1]. The two inverses agree on
D(ac) by zc=a(a-1). Since 1+ts and s have no common zero, {a!=0} and {s!=0}
cover the (t,s)-plane, so the WHOLE plane, t=0 included, is isomorphic to
D(a) union D(c) inside Y. The (r,q) chart is the u<->v, a<->b, c<->d mirror;
rechecked: uv=r(1+rq)=rb, u^2v=r^3b^2=a, u(a-1)=r^2b(a-1)=c, v(b-1)=q=d.

Cover: a point outside D(a) union D(b) has a=b=0, so (a-1)(b-1)=1. Hence
D((a-1)(b-1)), D(a), D(b) cover Y, each an open of a plane: Y is smooth,
therefore normal. B is a domain and Frac(B) contains u=c/(a-1), v=d/(b-1),
so Frac(B)=C(u,v). Y=Spec B is affine by definition, five generators.

## 2. Image of j, boundary lines, ruling: CONFIRMED

At z=0 the identities force ab=0, a(a-1)=0, b(b-1)=0, so (a,b) is (0,0),
(1,0) or (0,1). With a=1, ad=(b-1)z^2 forces d=0 and c is free; these points
are exactly the line t=0 of the (t,s) chart (t=0 gives a=1, z=0, b=0, d=0,
c=s), so E1 is an actual closed affine line of Y, not just a solution set of
relations. E2 is r=0 of the (r,q) chart. E1 and E2 are disjoint (a=1 vs a=0).
With (a,b)=(0,0) the point lies in D((a-1)(b-1)) where u=-c, v=-d: the image
of the source axes uv=0. On D(z): B[z^-1] contains a/z=u and b/z=v, so
B[z^-1]=C[u,v,(uv)^-1]. Thus j maps {uv!=0} isomorphically onto D(z) and
{(u^2v-1)(uv^2-1)!=0} isomorphically onto D((a-1)(b-1)); these two sources
cover A^2 (a source point has uv!=0 or a=b=0), and the two targets are exactly
Y minus (E1 union E2), because the only z=0 points outside D((a-1)(b-1)) are
(a,b)=(1,0),(0,1). Source points never meet E1 or E2 since uv=0 forces a=b=0.
So j is an isomorphism of A^2 onto Y minus (E1 union E2), z=0 image included;
B is a domain so no component is discarded.

Ruling: B[c^-1]=C[t,c,c^-1] means D(c) is A^1_t x G_m, so every fibre of
c:Y->A^1 over c!=0 is A^1_t, with affine base. On the source, c!=0 forces
u!=0 and v=(c+u)/u^3, a G_m; the point t=0, s=c of E1 is the missing u=infinity.
The fibre c=0 is reducible (line u=0; curve u^2v=1 plus its E1 point; all of
E2). The producer asserts nothing about it, so no conflict.

## 3. Forms, overlap, derivatives, divisor: CONFIRMED

beta=-v du, d beta=-dv^du=du^dv. Chart 1: du=-t^-2 dt, so
beta=(t^2+t^3s)t^-2 dt=(1+ts)dt=beta1, polynomial on the whole (t,s)-plane;
d beta1=(s dt+t ds)^dt=-t dt^ds=omega1. Direct check:
du^dv=(-t^-2 dt)^(t^3 ds + ... dt)=-t dt^ds, agreeing.
Chart 2: du=(2r+3r^2q)dr+r^3dq, beta=-r^-1 du=-(2+3rq)dr-r^2dq=beta2,
polynomial; d beta2=-3r dq^dr-2r dr^dq=3r dr^dq-2r dr^dq=r dr^dq=omega2;
direct: du^dv=r^3dq^(-r^-2dr)=r dr^dq, agreeing.
beta, beta1, beta2 are ONE rational form on C(u,v) in three coordinate
systems, regular on D((a-1)(b-1)) (open in the source plane), on D(a) and on
D(b) (opens in the two planes); these cover Y, so the form is a global regular
1-form, an element of Omega_B because Y is smooth affine. omega=d beta is
globally exact with j^*omega=du^dv. Zeros: none on D((a-1)(b-1)); t=0, i.e.
E1, simple, on D(a) since dt^ds is nowhere zero; r=0, i.e. E2, simple, on
D(b). Hence div(omega)=E1+E2 exactly, multiplicity one each.

## 4. Valuation argument and the two-boundary sanity check: CONFIRMED

Let H=sum h_ij u^i v^j in B have total degree D>=1. Along E1 (chart 1,
ord_t): u^i v^j=t^(2j-i)(1+ts)^j has order 2j-i. For (i,j)!=(D,0) with
i+j<=D: if j=0 then i<D so -i>-D; if j>=1 then -i+2j>=-(D-j)+2j=-D+3j>-D.
So the t^(-D) coefficient of H in C[s]((t)) is exactly h_D0, and regularity
of H along E1 forces h_D0=0. The mirror along E2 (ord_r, order 2i-j) forces
h_0D=0. Hence the top form H_D is divisible by uv, and for EVERY h0 the
closure of {H=h0} in P^2 meets the line at infinity at [1:0:0] and [0:1:0],
two distinct points. If H were a coordinate, (H,G) an automorphism sigma,
then {H=h0}=sigma^-1{x=h0} is the image of a polynomial map A^1->A^2, which
extends to P^1->P^2; the closure of the level curve is the image of P^1 and
its points at infinity are the image of the single point infinity. One point
cannot be two. No degree bound, envelope or classification is used. Correct.

Sanity, both boundaries needed: on Y minus E2 (source plane glued to the
(t,s)-plane along t!=0) the element v=t^2(1+ts) is regular (ord_t=2), so the
source coordinate v extends there; only the pure-u^D constraint survives and
v has no such term. Mirror: u=r^2+r^3q extends over Y minus E1. Consistency
with B: ord_r(v)=-1 along E2 and ord_t(u)=-1 along E1, so neither is in B.
The exclusion genuinely uses both opposing valuations -i+2j and 2i-j; each
alone kills one pure power and admits the other coordinate. Confirmed.

## 5. Eliminant, finiteness, degree eight, Jacobian: CONFIRMED

In B[c^-1]=C[t,c,c^-1]: d=t^2 a(b-1)=t^2(1+tc)(t^3(1+tc)^2-1), t-degree
2+1+3+2=8, leading coefficient c*c^2=c^3. So t is algebraic over C(c,d),
trdeg C(c,d)=2, c and d are algebraically independent, and
[C(c)(t):C(c)(d)]=deg_t d=8: the generic degree of (c,d):Y->A^2 is exactly 8.

Eliminant: cd=z(ab-a-b+1)=z^4-zS+z gives zS=z^4+z-cd with S=a+b. From
zc=a(a-1), zd=b(b-1): a^2-a=cz, b^2-b=dz, so S^2-2z^3-S=(c+d)z. Multiply by
z^2 and substitute zS:
(z^4+z-cd)^2 - z(z^4+z-cd) - 2z^5 - (c+d)z^3
= z^8+z^2+c^2d^2+2z^5-2cdz^4-2cdz - z^5-z^2+cdz - 2z^5-(c+d)z^3
= z^8 - z^5 - 2cd z^4 - (c+d) z^3 - cd z + c^2 d^2.
Every coefficient matches the producer's display; monic in z; an identity in
the domain B, hence valid at z=0 too. Then a,b are integral over C[c,d][z]
by the two quadratics, so B=C[c,d][z,a,b] is finite over C[c,d]. B is normal
with Frac(B)=C(u,v), so B is the integral closure of C[c,d] in C(u,v):
e:Y->A^2_(c,d) is the full-field normalization, finite, generic degree 8.

Jacobian: c_u=3u^2v-1=3a-1, c_v=u^3, d_u=v^3, d_v=3b-1, so
J=(3a-1)(3b-1)-u^3v^3=9z^3-3a-3b+1-z^3=1-3a-3b+8z^3, nonconstant; at u=1
(a=v, b=v^2, z=v) it is 1-3v-3v^2+8v^3. Total output degree is four. Confirmed.

## 6. Interpretation: CONFIRMED as scoped; other pair GAP

Proved: a smooth normal affine Y; an open j:A^2->Y whose complement is two
disjoint affine lines; a finite full-field normalization Y->A^2 of generic
degree 8; an affine-base A^1 fibration; a globally exact regular 2-form
extending du^dv with divisor E1+E2; and no nonconstant element of B is a
coordinate of the marked source plane. So the implication "exact extending
volume + open whole plane chart + affine-base ruling + finite normalization
=> marked source coordinate" is refuted by this control. The pair (c,d) has
nonconstant J, so Keller etaleness is exactly the missing hypothesis; the
control is not, and does not produce, a Keller counterexample. Whether some
OTHER pair in B^2 is Keller on the source is addressed by no argument in
CLAIM.md and stays GAP, as the producer states. No JC2 closure, degree
frontier, classification or classical-bound reproof is implied; I performed
no family search. "Wright-type" is a label, not a load-bearing citation.
FALLACY-v2: no exit price is asserted, so no charge_basis line is declared.

## Closing custody and disclosure

- Post-review rehash at 12:42:18Z, after all reading and derivation:
  `inputs/COORDINATION.snapshot.md` = `a14b2ebcb3841f175b52ef0a96835a5724aee06a6008442eb3d25f98194a99bc`,
  `inputs/CLAIM.md` = `79a4d7d63f254729e9dc2fdeea866841d082be4d19476e23f268a80b2579de16`;
  both unchanged from the pre-review table. The first 8481 bytes of CLAIM.md
  hash to `766b0006603da80ab6dab06dee571dfdb54d0c4d05313b4ec978d13c04f9dc2a`,
  matching the producer's declared body SHA-256 (consistency only; a seal
  is not a proof).
- Authoring: apply_patch only (skeleton; two section appends; one repair;
  this section; then the marker). No Write/Edit, shell redirection, heredoc
  file write, interpreter, CAS or test ran. Deviation disclosed: the second
  section append duplicated the sentence "D(b). Hence div(omega)=E1+E2
  exactly, multiplicity one each." because I supplied it as an added line
  instead of a context line; the duplicate was removed by one apply_patch
  delete before this section was written, and the whole draft was read back
  in <=80-line chunks before and after. No other file was touched; no
  network, fleet, shared ledger, or repository path outside the two charged
  inputs and this report was accessed.
- No seal, manifest, or charge_basis line is authored here; the external
  launcher owns custody. Substantive content complete before 12:48Z.

<!-- BODY-END -->
