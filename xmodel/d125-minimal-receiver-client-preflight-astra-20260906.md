# D125 minimal receiver: six exact coefficient clients, prep only

Status: **PROVISIONAL PREP — NOT A PROMOTION OR PRODUCTION EXPORT.** Author `/root/model_productivity`, 2026-09-06. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

The full-face normalized coefficient contracts have **267, 293, 369 ring variables**, respectively, for the unequal, common-3, common-4 cases. These counts apply separately over Q and the quadratic field. They are exact parameter counts for these presentations, not dimensions, existence results, exclusions, term counts or timing predictions. Only small face polynomials, closed lattice sets and toy Jacobians were constructed. The code deliberately refuses production-sized row assembly.

## 1. Charged hypothesis and ring boundary

Read whole terminal composition `d125-minimal-monomial-receiver-composition-astra-20260906.md` and both terminal F2 predecessors listed in §7. The implication consumed provisionally is:

An actual polynomial standard (3,5) Keller pair of degrees 75/125 generating the specified F2 row, under the predecessor's named external and previously gated inputs, yields a polynomial receiver A,B of degrees 15/25 with `[A,B]=c gamma^2`, `c!=0`, in one of the three support cases below. The shear is `(i,j)->(i-j,j)` from the degree-30/50 polynomial receiver, with the full bracket-row bijection in the composition. This task does not reprove the F2 chain, its applicability to arbitrary degree-125 counterexamples, or the new composition gate.

The live `d125-minimal-receiver-gate-fable5-20260906` report, prompt, code, log and receipt were **not read**. No live lift contract was read or incorporated. This is complete for the **displayed receiver necessary family**, not a sufficient polynomial Keller-source contract. Inverse Laurent cuts still need polynomial cancellation and source checks. There is no Roy/Moh coefficient identification, old jet condition, source lift, or JC2 counterexample criterion here.

Take physical variables `(gamma,pi)` and convention `[A,B]=A_gamma B_pi-A_pi B_gamma`. After the normalization in §3 use coefficient field `L=Q` or `L=Q[rho]/(rho^2-3rho+1)`. Free coefficients range over an algebraically closed characteristic-zero extension, **not just L-rational points**. A golden row `a(z)+rho b(z)=0` is ONE equation over L; splitting it into `a=b=0` is forbidden. Both conjugates of rho are retained. An alternative rational-ring presentation would add rho as a variable and its one minimal-polynomial equation, not split receiver equations; this alternative is not implemented.

## 2. Literal six clients and complete faces

For each row take every closed-polygon lattice point as a coefficient slot, then apply exactly the fixed assignments below. Coordinates are gamma/pi exponents.

| case | allowed A polygon | allowed B polygon | inner normal |
|---|---|---|---|
| unequal | (0,0),(0,15),(9,6),(2,1) | (0,0),(0,25),(15,10),(1,0) | (5,-7) |
| common-3 | (0,0),(0,15),(9,6),(3,0) | (0,0),(0,25),(15,10),(5,0) | (1,-1) |
| common-4 | (0,0),(0,15),(9,6),(9,0) | (0,0),(0,25),(15,10),(15,0) | (1,0) |

Set `A_(0,0)=B_(0,0)=0`. The origin is then an allowed-support point, **not a claimed nonzero Newton vertex**. Thus the table describes the normalized support bounds with all six nonorigin vertices required; target translation need not preserve the origin as a literal vertex. This does not remove any geometric receiver orbit.

There are exactly two prescribed outer forms. Put `H=pi^2 S`, with

- rational: `S=pi^3+gamma^3`, `kappa=1`;
- golden: `S=(pi+gamma)(pi+(1-rho)gamma)^2`, `kappa=rho`.

In the golden case `S=pi^3+(3-2rho)gamma*pi^2+(2-rho)gamma^2*pi+rho*gamma^3`. In all six clients prescribe the **entire** total faces `A_15=H^3`, `B_25=H^5`. In particular the shared corner coefficients are `kappa^3,kappa^5` and the pi-axis leading coefficients are both one. Prescribed zero coefficients on these faces are fixed zero, never free or omitted source slots.

The entire inner faces, after §3's single remaining scale, are:

- unequal: `A_in=gamma^2*pi+kappa^3 gamma^9*pi^6`; `B_in=(5/(9kappa))gamma+(5kappa^2/3)gamma^8*pi^5+kappa^5 gamma^15*pi^10`; **fixed** `c=-5/(9kappa)`;
- common-3: `G=gamma(gamma*pi-1)^2`, `A_in=kappa^3 G^3`, `B_in=kappa^5 G^5`;
- common-4: `G=gamma^3(pi-1)^2`, `A_in=kappa^3 G^3`, `B_in=kappa^5 G^5`.

Every lattice slot on the specified inner line is assigned its displayed coefficient, including zero if any. Shared corner assignments agree exactly. Common cases retain a free scalar c and a separate variable z with the literal row `z*c-1`. There are no independent inner scalars or distinct A/B values of mu.

## 3. Necessity, invertibility and no extra scalar gauge

First divide A and B by their nonzero pi-leading coefficients. This makes both monic and changes c by the product of the inverse target scalars. Subtract their constant coefficients; differentiation and all displayed faces are unchanged because each face has positive weight. Both operations have explicit inverse target rescalings/translations. They are same-field operations.

After monicity the admissible simultaneous scale is

`A_tau= tau^-15 A(tau*gamma,tau*pi)`, `B_tau=tau^-25 B(tau*gamma,tau*pi)`.

It fixes both complete outer forms. The chain rule gives `c_tau=c*tau^-36`; the inverse is the same formula with `tau^-1`. It preserves every nonzero nonorigin vertex and every support bound.

For the unequal face before the last scale, write its low A coefficient as a. The full inner bracket gives

`e=(5/3)a*kappa^2`, `d=(5/9)a^2/kappa`, `c=-(5/9)a^3/kappa`, with `a!=0`.

Taking `tau^12=a` gives `a_tau=1`, `d_tau=5/(9kappa)`, `e_tau=5kappa^2/3` and `c_tau=-5/(9kappa)`. This checks the proposed normalization exactly. **Do not also set c=1.** Existence of a nonzero twelfth root is geometric/algebraic-closure necessity, not a same-field rational isomorphism. Residual twelfth-root choices give possibly different normalized representatives; they are not omitted solution branches because every choice stays within this family and at least one exists. No uniqueness claim is made.

For common-3, `gamma(gamma*pi-mu)^2` transforms with `mu_tau=mu/tau^2`; take `tau^2=mu`, so `c_tau=c*mu^-18` remains free and nonzero. For common-4, `gamma^3(pi-mu)^2` transforms with `mu_tau=mu/tau`; take `tau=mu`, so `c_tau=c*mu^-36`. Here mu is nonzero and shared. The common-4 scaling itself is same-field when mu is in that field; the six-case normalization as a whole is not a same-field equivalence because the other cases require roots. No second scalar freedom is spent fixing c.

These arguments prove equivalence of the normalized receiver-orbit existence problem to the stated unnormalized receiver family **conditional on that family's source license**. They do not establish an inverse polynomial Keller lift. Choosing roots over the algebraic closure and retaining the golden field are essential to that quantifier statement.

## 4. Exact parameter quotient and guards

The code starts with all polygon slots and specializes only the origin and entire prescribed faces to field constants. Algebraically this is the quotient of the raw coefficient ring by exactly those affine coordinate assignments, canonically isomorphic to a polynomial ring on the remaining free slots. No free coefficient is removed; no variable-dependent face pivot or saturation division is used.

Outer faces contain 10 A and 16 B lattice points. The unequal inner faces contain 2 and 3 points; common inner faces contain 7 and 11. Each meets its outer face at one point. Origins are disjoint. Thus:

| case | raw A/B | fixed A/B, including constants | free A/B | ring variables | raw pair upper bound |
|---|---:|---:|---:|---:|---:|
| unequal | 83 / 215 | 12 / 19 | 71 / 196 | 267 | 17,845 |
| common-3 | 94 / 241 | 17 / 27 | 77 / 214 | 291+2=293 | 22,654 |
| common-4 | 115 / 296 | 17 / 27 | 98 / 269 | 367+2=369 | 34,040 |

These counts hold separately for each outer branch even where fixed coefficients vanish. Pair bounds are mere products of slot counts, not a full pair census or observed nonzero term count.

All six nonorigin vertices have explicitly nonzero **fixed** field values: the pi tops one, shared corners `kappa^3,kappa^5`, and the low endpoints one / `5/(9kappa)` in the unequal case or `kappa^3,kappa^5` in the common cases. The contract records every value and its exact inverse. Planned guard rows are `value*inverse-1` for all six vertices; these are certified zero rows over L, not silently omitted nonzero assumptions. The unequal c guard is similarly a fixed-unit row. Common cases use the genuine `z*c-1` row. No guard is attached to the origin. Exact total degrees 15 and 25 follow from the fixed pi tops, with the polygon upper bounds; the other exact vertices have their own guards.

## 5. Complete row contract and toy-only implementation

The formal ring is `L[free A slots, free B slots]` in the unequal case; common cases append `c,z`. Slot order is A first, then B, increasing `(gamma exponent,pi exponent)` lexicographically; variable ids are zero-based. Choose global graded reverse lexicographic order in that displayed variable order. This is a declared order, not an exercised CAS parser.

For every `0<=I<=23`, `0<=J`, `I+J<=38`, emit the coefficient of `gamma^I*pi^J` in `[A,B]-c*gamma^2`. These are **660** rows, including zeros. Completeness follows from `deg A=15`, `deg B=25`, and gamma degrees at most 9 and 15. Any nonzero differentiated pair has nonnegative exponents, gamma exponent at most 23 and total degree at most 38. The target `(2,0)` is explicitly required even if its derivative sum vanishes.

For an A slot `(i,j)` and requested output `(I,J)`, the B index is forced to `(k,l)=(I+1-i,J+1-j)`. Add `(i*l-j*k)*A_ij*B_kl` when that slot exists and the determinant is nonzero. At `(2,0)` subtract c. In the unequal case this adds `+5/(9kappa)` to that residual row. Products remain literal bilinear/linear/constant coefficient polynomials over L; no h/circuit reinterpretation or coefficientwise field cut is permitted.

The planned full stream retains all raw slot-map records, then one fixed-assignment residual for each specialized slot (31 unequal, 44 common, already zero in the quotient), all 660 J rows, six vertex-unit guard rows and one c guard. Thus planned total rows are **698 / 711 / 711**. These are explicit conservative envelope counts, not a claim to have generated production rows. Degree guards are already among the fixed tops and vertex checks, not extra hidden constraints. A full future exporter must preserve the prescribed assignments in its slot map and verify their intersections before substituting.

`client.py` implements exact two-coordinate field arithmetic, all six deterministic slot contracts, and only a **toy-capped** forced-index row kernel. A field element is canonically `[[a_num,a_den],[b_num,b_den]]` for `a+b*rho`, with multiplication reduced by `rho^2=3rho-1`; inverse uses norm `a^2+3ab+b^2`. A literal term pairs one field element with its sorted coefficient-variable id tuple. Equal monomials are collected exactly.

The toy JSONL has a header, every declared row, and a complete footer with row/term/zero counts and SHA-256 of canonical prefix bytes. Strict full-file self-replay rejects omissions, target changes, noncanonical/truncated data and footer mismatch. It is not independent certification. Production slot-map/guard emission, a full-stream verifier and any Singular adapter remain **unimplemented**. `production_export()` always raises, and the toy row kernel rejects source-support products exceeding 64; no full receiver J was expanded.

## 6. Controls, readiness and stop condition

`test_client.py`: **52 controls PASS** under normal Python and `-O`; final normal arithmetic run 0.080 seconds / 21,120 KiB peak RSS. The process declares 30 wall seconds, 25 CPU seconds and 512 MiB address-space caps. These controls check all six small lattice/face contracts, every nonorigin vertex unit, golden arithmetic and its conjugate, exact one-scale unequal formulas, the full tiny unequal inner bracket/sign, and a 3-by-3 toy forced-index calculation against an independent pair-loop reference. The nonzero-J control `(A,B)=(gamma,gamma^2*pi)` gives the expected zero residuals. An unused toy target constant remains declared.

Changed objects actually rejected: a prescribed zero outer coefficient made free, a deleted free lattice slot, a zero required vertex, an illicit c=1 assignment, wrong target sign, missing target row, missing footer, and attempted production assembly. Separate final subprocess mutations for **target sign and fixed-zero face** exit 1 in both normal and optimized modes. Earlier preliminary receipts are retained: before final tests a missing reverse subtraction method was fixed; an external face-mutation switch was corrected to retain the actual face mutation rather than a later scalar mutation. The final source and all final receipts are pinned below. No correctness inference is made from those preliminary failures.

Future measured work requires root authorization **and** the mathematical gate. The smallest next implementation is the specified complete six-client stream/strict verifier, followed by one bounded construction/import pilot; not a solve automatically. No runtime advantage is inferred from the small parameter count. The separately proposed exact negative-power lift and fixed-diagonal B reconstruction may change the preferred client, but neither is consumed or implemented here. This baseline preserves the full bilinear receiver first.

No AWS, SSH, CAS, solver, full-system expansion, production pair census, shared ledger edit, or protected project read occurred. All test subprocesses and file writers are terminal; the agent stops after transactional publication. There is no automatic continuation or compute authority.

## 7. Immutable inputs and final owned evidence

Paths below are relative to the campaign root. Input SHA-256 values were rechecked:

- `xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md`: `7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413`.
- `xmodel/d125-published-chain-discriminator-astra-20260906.md`: `9b439af269c23e349615d3e404e0732c9c7f491a9342d5500e061aab91ad4e88`.
- `xmodel/d125-published-chain-gate-fable5-20260906.md`: `5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b`.

Owned directory `box/d125-minimal-receiver-client-preflight-20260906/`:

- `client.py`: `ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53`.
- `test_client.py`: `15d49bf7b4047ae0394379335a8614d53d083a38efd6042de4110cb9854de741`.
- `run_controls.py`: `447be5cb3f1b6fe165136ccd6f008cc21937bc895ead5a35928d0887cd934c6c`.
- `test-normal-final.json`: `3224d65757400bfee92d4021e87cb7d9e4555ed202eebf52bf8c1bcc0af66087`.
- `test-O-pass-final.json`: `55ffc84f3df0dc3ba37d964fb5d3e79af3db5eaaca80b456b9cc2da9247ad0c6`.
- `control-receipts-final.json`: `283730df293ca87ac15f438b46f68e7f3dca073d6708662b809a1e881911afbd`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15081`.
- Body SHA-256:
  `74a3768369a0b3b65c5676ed7a5ab682588975a10beeca79c7ed26935efde7c8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
