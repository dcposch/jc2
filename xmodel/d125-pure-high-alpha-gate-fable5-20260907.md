# D125 pure center, high-alpha obstruction: independent Fable gate

2026-09-07/08. Independent review of the producer theorem in `ha-producer.md`
(SHA256 `3eaf5610aede5885efa1c9aba95dc2016269952f5c0983675abfacc79b9c9bed`):
no genuine finite pure-center source arc in the accepted14v first-contact
setup has ord(alpha) >= j, including alpha identically zero. Charged inputs
are the twelve frozen snapshots only; accepted14c/f/g/v are imported at their
stated scopes and external-theorem trust. 14y, 15b, the pending lower-alpha
critical-remainder theorem and any live review are not premises and were not
read. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d` is provenance
only. No exit price is asserted and no exit-basis line is declared. No
nilpotent-jet-to-arc, nonempty-boundary, source-coverage, guarded-emptiness
or JC2 conclusion is drawn.

**Overall: all six targets CONFIRMED at the charged scope; no GAP found in
the theorem. One evidence-description defect is scoped separately (Section 8).**

## 1. SOURCE SCOPE: CONFIRMED

The producer works in the accepted14v references at the pure exceptional
center: V=g^3+p^3-3p, R=p^2 V, S=p^3+g p^2-p, R_s=R+h S with h=t(s)+3, h(0)=0.
I checked R_t - R_{-3} = (t+3)(g p^2+p^3-p) = (t+3)S against the 14f family, so
the moving R_s is exactly the 14v reference. The hypotheses used are exactly
14v's conclusions for a genuine K[[s]] arc with k=kappa s^m+..., kappa nonzero:
F=A-R_s^3-alpha R_s with ord F=j<m, F_j=R C, C even with C(0)=0 and V not
dividing C, ord G>=2j after the 14v kernel removal, ord delta>=j+1, F odd of
degree<=13 and weight<=3, G odd of degree<=23. The weight bound w(G)<=5 is a
one-line consequence of w(B)<=5 (14c B polygon; consistent with 14g's
B_1=d g+e p), w(R_s)=1 and w(q_s F)<=2+3. C mod V is nonconstant because a
constant residue c gives V | (C-c), and evaluating at O=(0,0) on V forces c=0,
contradicting V not dividing C. The saturated low rows and [p]F=alpha h are
retained; nothing in the proof sets them to zero or uses them. The three
regimes ord(alpha)=j, ord(alpha)>j, alpha=0 differ only in whether the scalar
alpha_j is nonzero, and the proof handles all three. The theorem is stated for
this normalized odd, lambda2=0 source, not an arbitrary unequal source; no map
theorem is used. 14v's own text calls its first-contact theorem provisional;
this gate imports it at the charged accepted scope and does not re-review it.

## 2. FINITE DIVISION: CONFIRMED

Independently: R_s = g^3 p^2 + p^5 + (h-3)p^3 + h g p^2 - h p, so the only
monomial divisible by g^3 p^2 is g^3 p^2 itself with coefficient exactly 1 (h S
contributes p^3, g p^2, p only). The replacement g^3 p^2 -> R_s - p^5 - h g p^2
+ (3-h)p^3 + h p uses monomials of g-degree 0 or 1, total degree<=5 and weight
<=1, so each step strictly lowers the g-degree and never raises total degree
or weight; in lex g>p the leading monomial strictly decreases inside a finite
monomial set, so the division terminates. Coefficients stay in K[[s]] because
the leading coefficient is 1, and the ideal s^j K[[s]] is preserved, giving
ord(P_i)>=j and ord(Q_i)>=2j. Degree and weight drop by 5 and 1 per quotient,
so F=P0+R_s P1+R_s^2 P2 and G=Q0+...+R_s^4 Q4 are exact with deg P_i<=13-5i,
w(P_i)<=3-i, deg Q_i<=23-5i, w(Q_i)<=5-i. Injectivity: if V | P with P normal
and w(P)<=5, then P=V U with w(U)<=-10, every monomial of p-degree 0 or 1 has
weight >=-7, so p^2 | U and P=R U'; the lex leading monomial of R U' is
g^3 p^2 times lm(U'), impossible for a normal P unless U'=0. No ordinariness
and no monic-p division is used. Taking s^j coefficients, (P0)_j = R(C-(P1)_j
-R(P2)_j) is normal, weight<=3, and divisible by V, hence zero: q>j including
q=infinity, and (P1)_j = C mod R, so ord P1 = j exactly. All replacement
monomials are odd, so the division preserves parity: P0, P2, Q0, Q2, Q4 are
odd and P1, Q1, Q3 even. eta=min(j/2,q/3) satisfies j/3<eta<=j/2.

## 3. NEWTON REGULARITY: CONFIRMED

In L=Kbar(V), g is a simple root of R(X,p)=p^2(X^3+p^3-3p) because
R_X(g,p)=3g^2p^2 is nonzero in L, so Hensel gives a unique G(s,z) in L[[s,z]]
with G(0,0)=g and R_s(G,p)=z. Write A=c_0(G,p)+z c_1(G,p)+z^2 c_2(G,p)+z^3
with c_0=P0, c_1=P1+alpha, c_2=P2, and z=s^eta Z after the Puiseux
normalization. Each c_i is normal of weight<=5, so its first s-coefficient
has a nonzero residue on V; G-g has positive s-order, so the implicit
corrections to c_i(G,p) start strictly after ord(c_i). Since ord(c_i)+i eta
is at least the minimum order for every i, no correction ever reaches an
initial form. Orders are q>=3eta, eta+j>=3eta, 2eta+ord c_2>=2eta+j>3eta and
exactly 3eta for Z^3, so the initial is Z^3+uZ+v with u=(C|V)+alpha_j if
eta=j/2 (else 0), v=(P0)_q|V if eta=q/3 (else 0), no Z^2, distinct Z-powers
unable to cancel, and at least one of u, v nonconstant (u is even and
nonconstant; v is odd and nonzero, hence not in Kbar). The producer's caution
about later implicit coefficients is warranted and correctly scoped: the
first-order coefficients are G_01=1/(3g^2p^2) and G_10=-h_1 S/(3g^2p^2), which
have poles at O of orders 8 and 5; the proof never needs their regularity.
The derivative rule is correct: D on L-coefficients and d/dZ never lower
s-order, and d/dz = s^(-eta) d/dZ is the only shift.

## 4. ALL B TERMS: CONFIRMED

I rederived (4) from the 14v definitions symbolically: with q_s=5R_s^2/3
+beta-5alpha/9 and delta=gamma-beta alpha+5alpha^2/9,
B-beta A = R_s^5+(delta-5alpha^2/9)R_s+(5R_s^2/3-5alpha/9)F+G exactly. The
z-power coefficients of B* are c_5=1, c_4=(5/3)P2+Q4 (order>=j, weight
>5eta), c_3=(5/3)P1+Q3 (order>=j, weight>=5eta), c_2=(5/3)P0-(5alpha/9)P2+Q2
(order>=min(q,2j), weight>=5eta), c_1=delta-5alpha^2/9-(5alpha/9)P1+Q1 and
c_0=-(5alpha/9)P0+Q0. Below 5eta only the scalar delta can enter c_1 (the
rest has order>=2j, weight>=5eta) and only Q0 can enter c_0, because
alpha P0 has order>=j+q>=5eta. So an initial of weight nu<5eta is dZ+e with d
scalar and e the odd regular residue of Q0's first coefficient. The Z^5 term
s^(5eta)Z^5 is exact and cannot be cancelled, so nu<=5eta; at nu=5eta the
initial is monic of degree 5 with no Z^4 term because c_4 has weight>5eta.
Parity is not a new normalization: A and B are odd by the 14c hypothesis,
beta is scalar, and the division preserves parity, so u, c, e are even and
v, d, f odd directly from the polynomial coefficients. The actual source
even gives d=(5/3)v and f0-free f without invoking parity. The dZ+e bracket
is 3De Z^2 - d Du Z + (u De - d Dv); vanishing forces De=0, e odd scalar
hence 0, then d nonzero and Du=Dv=0, contradicting Section 3; d=0 included.

## 5. TARGET AND POLES: CONFIRMED

The chain rule is an algebraic identity in L[[s,z]]: for f~=f(G,p),
[f~,h~]_(z,p) = G_z [f,h]_(g,p)(G,p) with G_z = 1/R_{s,g}(G,p) and
R_{s,g}=p^2(3g^2+h) invertible in L[[s,z]]. With [A,B]=-(5/9)k^3 g^2 and
[A,B-beta A]=[A,B], the target is -(5/9)k^3 G^2/(p^2(3G^2+h)), of order
exactly 3m with initial -(5/9)kappa^3/(3p^2) = -5 kappa^3/(27 p^2),
independent of Z. The bracket of initials of weights 3eta and nu sits at
2eta+nu (the s^(-eta) derivative factor is included, not lost). All cases
are retained: for nu<5eta, 2eta+nu>3m is an order contradiction, 2eta+nu<3m
forces [P,Q]=0 (Section 4), and 2eta+nu=3m is excluded by the pole bound;
for nu=5eta the same three cases with 7eta versus 3m. At O=(0,0) on V,
V_g=0 and V_p=-3, so g is a local parameter; p(3-p^2)=g^3 gives ord_O(p)=3;
differentiating V gives dp/dg=g^2/(1-p^2), so D=(1-p^2)/g^2 d/dg maps regular
functions to pole order at most 2, while the target coefficient has pole
order 6. Since no implicit correction enters any initial, all coefficients
of P and Q are polynomial residues plus scalars, regular on affine V, so the
bound applies. Nothing assumes 3m>7eta and nothing from the lower-alpha
argument is used.

## 6. DEGREE 3/5 ELIMINATION: CONFIRMED

Rederived symbolically with d0 and f0 retained: [P,Q] for P=Z^3+uZ+v and
Q=Z^5+cZ^3+dZ^2+eZ+f has Z^5 row 3c'-5u', Z^4 row 3d'-5v', and after
c=5u/3+c0, d=5v/3+d0, e=5u^2/9+c0 u+e0, f=10uv/9+c0 v+(2/3)d0 u+f0 the Z^3
and Z^2 rows vanish identically; f0 never appears. The remaining rows are
(5/9)[(u^2-K)u'-6vv'-(18/5)d0 v'] and (5/9)[2uvu'+(u^2-K)v'+(6/5)d0 uu'] with
K=9e0/5. The shift v -> v+3d0/5 turns both into (6) exactly, so d0 is
eliminated without parity; parity gives d0=0 directly as the producer says,
and c0, e0 stay free. D(u^3/3-Ku-3v^2) equals the first row, so the first
integral holds; the determinant (u^2-K)^2+12uv^2 with the first integral
substituted is (7/3)u^4-6Ku^2-4L0 u+K^2, leading coefficient 7/3. A nonzero
Kbar-polynomial relation makes u algebraic over Kbar, hence in Kbar because
Kbar is algebraically closed; then u'=0, the first row gives v'=0 (v=0
included), so both are scalar, contradicting Section 3. No common-generator
theorem over L[Z] is imported; only these identities and the constant field
of D on L being Kbar (verified by the minimal-polynomial argument).

## 7. Replay in fresh reviewer scratch

Charged `ha-checker.py` and `ha-factor-helper.py` were copied byte-for-byte
into a fresh mktemp scratch at the two required box paths, hashed before and
after (`d4b9f1aa...` and `25be0862...`, unchanged), never edited, and the
scratch was deleted after copying outputs. Interpreter: Python 3.12.3,
`/usr/bin/python3 -I -B` and `-O`, each child under ulimit CPU 25 s, address
space 512 MiB, timeout 30 s.

| optimized | mode | exit | failure marker |
|---|---|---|---|
| normal | positive | rc=0 | marker= |
| normal | --omit-hp | rc=1 | marker=ValueError: actual division reconstruction |
| normal | --wrong-filtered-input | rc=1 | marker=ValueError: actual filtered input |
| normal | --wrong-target-factor | rc=1 | marker=ValueError: actual target division factor |
| normal | --wrong-q0 | rc=1 | marker=ValueError: formal 3/5 coefficient elimination |
| normal | --wrong-quartic | rc=1 | marker=ValueError: formal determinant quartic |
| -O | positive | rc=0 | marker= |
| -O | --omit-hp | rc=1 | marker=ValueError: actual division reconstruction |
| -O | --wrong-filtered-input | rc=1 | marker=ValueError: actual filtered input |
| -O | --wrong-target-factor | rc=1 | marker=ValueError: actual target division factor |
| -O | --wrong-q0 | rc=1 | marker=ValueError: formal 3/5 coefficient elimination |
| -O | --wrong-quartic | rc=1 | marker=ValueError: formal determinant quartic |

Positive stdout is byte-identical to `ha-witness.json` and
`ha-witness-optimized.json` (`85b3e0ea...`). The scratch `--record` run
passed with 12 runs and the same witness hash; its returncodes and stdout
hashes match the charged `ha-replay.json` exactly, while mutation stderr
hashes differ (path-dependent tracebacks, as expected). Input pins before and
after the gate: IDENTICAL.

## 8. Evidence scope, separately from theorem validity

- The checker comment "Parity is indispensable to the depressed cubic
  conclusion" and its toy (every monomial of (g+p)^3 has odd degree) are a
  mis-description: the toy is vacuous and proves nothing about
  indispensability, and Section 6 shows the constant shift removes d0 without
  parity. Not a countercontrol, not a mutation, not a theorem defect.
- The witness field `local_pole_orders` is a recorded constant, not a
  computed check; the pole orders are proved in Section 5 and rechecked here.
- The three valuation controls are illustrations; the universal inequalities
  are proved and were also swept on a grid (j<25, q<80 or infinity).
- The five changed-object modes each trip their intended verifier; they are
  the charged mutation evidence.

## 9. Own evidence and custody

Independent stdlib script `fable5_independent_checks.py` (26 checks, PASS,
same caps, no CAS, no source materialization, no high powers) covers the
replacement rule, identity (4), the full 3/5 bracket with d0 and f0 retained,
the shift, first integral, quartic, the dZ+e bracket, and the local orders at
O. No AWS/SSH, solver, source builder, new agent, live peer read, canonical
edit or descendant was used. All evidence writers finished before this
report was written; nothing is written after it. STOP/IDLE.

Charged inputs (pre and post identical):

| input | sha256 |
|---|---|
| accepted14c-source.md | `19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc` |
| accepted14f-boundary.md | `129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2` |
| accepted14g-low-rows.md | `57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a` |
| accepted14v-first-contact.md | `9b3538b8d7d65477f5fb273ce8abb4b9556c8529dc374dc9affb4266f2793fb8` |
| ha-checker.py | `d4b9f1aa715d8bcb47475a1dd90f3115d7d111b0f9612a430cde713774d31c68` |
| ha-factor-helper.py | `25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66` |
| ha-producer-custody.json | `64ac1f6170cb652d0fed422adff76fb37f90b6f2c2df42f55963372cafcb9ea1` |
| ha-producer.artifact.json | `b4fd01c9c2e1e51f526649d77d66cafe172952dd87e1c0dc982818315034ff38` |
| ha-producer.md | `3eaf5610aede5885efa1c9aba95dc2016269952f5c0983675abfacc79b9c9bed` |
| ha-replay.json | `7a6bad86a0703b2f2e7a802b39314cd00131f522181300d8da2f3e13af2d5e9c` |
| ha-witness-optimized.json | `85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25` |
| ha-witness.json | `85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25` |

Own evidence under `box/d125-pure-high-alpha-gate-fable5-20260907/`
(full list with bytes in `custody.json`):

| file | sha256 |
|---|---|
| PINS-pre.txt | `2623c5b8dfd396d10fca0893c7bfeec2cc8a3770d4e3137827aa4321baa7d892` |
| PINS-post.txt | `2623c5b8dfd396d10fca0893c7bfeec2cc8a3770d4e3137827aa4321baa7d892` |
| scratch-hashes-pre.txt | `bc55f07d3f63c04126f640f52bad8b2734ffc6ee0554b8ae81e77cd5718d78e6` |
| scratch-hashes-post.txt | `e601959140c1e7ba10996b4e0b5f6b29a377d4d920e61fd3e1032f3a9b5e7751` |
| replay-individual.tsv | `4b70e00665d554215f582e30ded0e56086cb7bfa000e5407521996c5915f24fb` |
| scratch-replay.json | `aa9c23ed1cb4d731456fbbe8fd6e40fcd6d42c795d845785a7c803be5e588ee5` |
| scratch-witness.json | `85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25` |
| scratch-witness-O.json | `85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25` |
| record.stdout | `421da512dab68aadb69eabbd81707302da85172f2908dfc46f8f848610c3b348` |
| fable5_independent_checks.py | `1b4ffcbaf72cbfb7248357d03e964dedb2248fdb91e0af67edf936e412bc66ba` |
| fable5_independent_checks.out | `6133d908810864c95a538e553b3bd420099abf060ca2641f7327d5af1560db39` |

<!-- BODY-END -->
