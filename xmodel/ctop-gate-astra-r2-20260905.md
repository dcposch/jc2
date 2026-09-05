Round 2 hostile gate — `ctop-gate-astra-r2-20260905`, Astra/Codex.
Frozen basis: `c4707ea87f919f408b354cb0e443779c62e2d91e`.

**Verdict: REFUTED as the submitted promotion argument for the 936-row kill.**
The arithmetic **936 / 174 / 310 is reproduced exactly**. The inference from
that arithmetic to impossible source data is not licensed. The decisive
unproved identification is the copied `V`, not the gcd calculation. At the
operative row

```
(n,m)=(180,120), M=(-120,132,150,178), V=(2,4,5),
```

the child's own characteristic expansion gives `M'=(-20,22,25)` and
`d'=(30,10,2,1)`, agreeing with the labels. But literal inversion of the
source's top root expansions gives a child split **15 + 15**, hence its own
`V'_3=1`, whereas `descend()` copies `V_3=4`. The own-child comparison is
`1<=2`, not the failing labelled comparison `4<=2`. The alternate parent
`V=(3,4,5)` has the same result. These rows survive **this proposed top
test**, in the precise conditional sense explained below.

**U-NEG licence: REFUTED as the claimed unconditional campaign licence.**
The elementary inequality for an actual child's own normalized root count
is CONFIRMED. Its application to the campaign's copied `V'_2=V_2` is still
`OPEN[CHILD-LEVEL2-IDENTIFICATION]`. Proposition 6.3 counts all child roots;
it does not identify the disc to which the copied integer belongs.

This is not an exhibited Keller counterexample. A census row is necessary
numerical data, not a supplied polynomial pair. All computations of “the
child” below mean: **if a source pair realizes that row, apply its actual
Proposition 6.3 transformation**. We compute the forced characteristic jet
and top inverse expansions of that child. We do not prove the source exists,
nor that it survives every other obstruction. Consequently the absolute
statement “some realizable source among the 936 survives” remains OPEN.
The promotion claim fails; the number of genuinely impossible rows is not
replaced by a conjectural count. In particular **484 is not a certified
mathematical residual** from this gate.

**1. Custody and independent replay.** The first operation built a manifest
mechanically from the receipt, then checked the frozen copies:

```
awk -F= '
/^charged_input_[0-9]+_sha256=/ {
  key=$1; sub(/_sha256$/, "", key); hash[key]=$2
}
/^charged_input_[0-9]+_basename=/ {
  key=$1; sub(/_basename$/, "", key); base[key]=$2
}
END {
  for (key in hash)
    print hash[key] "  /tmp/jc2-lane.yqyWvI/inputs/" base[key]
}' xmodel/ctop-gate-astra-r2-20260905.run.v2 > /tmp/ctop-gate-r2-manifest.sha256
sha256sum -c /tmp/ctop-gate-r2-manifest.sha256
```

Result: **7/7 OK**, including the charged round-one `enum-replay.json`.
The manifest is banked as `box/ctop-gate-20260905/r2-inputs.sha256`.
No digest was inferred from the supplied prose. The prior replay script,
text extracts and page images were not treated as verified evidence merely
because they survived the interrupted run. Relevant pages were freshly
rendered from the checked PDF; new extracts/renders have `r2-` prefixes.
In particular pp.150,154,170,174,179,194,196–199,207 were read from images;
the PDF text layer omits important formulas.

The new enumeration imports the charged `moh_skeleton_full.py`, with an assertion
that the operative Tree's own `B` import resolves to that exact module.
The operative Tree is the inspected campaign implementation
`box/centre-gate-20260903/opus5_probe.py`, SHA-256
`4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9`.
The frozen enumerator alone generates the larger (1)–(13) census.

`r2-enum-audit.py` enumerates `16<=n<=200`, `Kmin=2`, `full=True`.
Tree settings are `gate=False, ode=True, capacity=False, passport=False,
recenter=True`; `embeds(V)` is the operative predicate. Child labels are
rebuilt with exact rational scaling and independent prefix gcds. Neither
the old `descend()` nor cached rows generate the new results. Only after
regeneration is the charged replay loaded for comparison. Every one of
the **1,420 complete operative row dictionaries**, and both full summary
dictionaries, matches it exactly. Runtime of that replay was 22.484 seconds.

**2. What Definition 5.1 actually says.** On p.179 its opening is:

> A tower of major discs `D_s ⊇ D_{s-1} ⊇ ··· ⊇ D_r` satisfies the following
> four criteria with a sequence of integers `{V_i: i=(r+1,...,s+1)}`.

Criterion (2), transcribed from the image, is:

> the numbers `V_i` satisfy
> `V_{i+1} d_i/d_{i+1} ≥ V_i > d_i/(n-M_i)`
> for `i=r+1,...,s`, `V_{s+1}=d_{s+1}`.

It does **not** literally begin by imposing `V_i<=d_i` on arbitrary lists.
That upper bound follows for a genuine tower from the displayed comparison
and its top convention. At its top, `V_s<=d_s`. Iteration gives the lower
level bounds. Criterion (1) gives an even more direct interpretation:

> In the disc `D_i` the polynomials `g(y)` have precisely
> `(n/d_{i+1}) V_{i+1}` roots. `T_j^ψ(y)` has precisely
> `(-μ_j/d_{i+1}) V_{i+1}` roots for `j=1,...,i`.

Thus `V_{i+1}` is a normalized count in a specified disc. It is neither an
arbitrary multiplicity assigned to an approximate root nor part of the
p.150 definition of characteristic exponents. That definition determines
`M,d`; `V` belongs to a chosen root-configuration tower. This distinction
is essential to adversarial check (1).

Although labelled “Definition,” these criteria have geometric content.
The paragraph following Definition 5.1 cites Proposition 5.1 to establish
the initial all-roots disc, and Proposition 5.2 to extend it. The theorem
on p.200 constructs such towers under its stated source hypotheses.
A correctly identified source tower violating (2) would therefore be a
contradiction, not a harmless choice of notation. But if a numerical list
has never been shown to describe the actual tower, violation shows only
that **that list cannot describe it**. Relabelling a child's tower cannot
be excluded by applying a definition to inherited integers.

There is a second transfer issue. The surrounding theory uses the
constant-Jacobian source. Proposition 6.3(3) changes the child's Jacobian
to a monomial. Moh himself signals this on p.197. A literal application
of all four criteria to the child is therefore not automatic. For example,
the p.207 child `(16,12), M'_2=13` has printed `δ'_2=-1`, whereas literal
Definition 5.1(3) with those degrees gives `-1/(16-13-1)=-1/2`.
The campaign multiplies radii by `ell+1` to address this difference.
That observation alone does not disprove a generalized count inequality;
it does rule out claiming that the unchanged printed definition already
proves every child-tower identification.

**3. The gcd identity is true, with a raw/effective index correction.**
Use `h_0=s-1` for the raw retained list and reserve `s_c` for the child's
effective last index after any drop. Put `q=d_s`. Each of
`n,M_1,...,M_{s-1}` is divisible by `q`, and the quotients have gcd 1.
Writing these integers as `q a_0,...,q a_{s-1}` gives, without treating a
rational scaling as a gcd rule,

```
n'=u_s a_0,  M'_i=u_s a_i  (1<=i<s),
gcd(n',M'_1,...,M'_{h_0})
  =u_s gcd(a_0,...,a_{s-1})=u_s.
```

All raw prefix versions were checked on all **24,063** census rows.
Section 4 separately verifies the actual support on a failing row.

Moh p.150, literally, has

```
d_1=n,  d_{j+1}=gcd(n,M_1,...,M_j),
M_j=min{i: f_i(x) != 0, d_j does not divide i},  M_{h+1}=infinity.
```

The coefficient test is `!=0`; nonzero constants **do count**. Once an
actual characteristic gcd is 1, the next defining set is empty. At `u_s=1`
the raw retained characteristic chain therefore closes if its support
identification has been established. This does not itself determine any
`V`. Also, a finite list ending with gcd greater than 1 does not alone
prove another nondivisible coefficient exists: one must retain the
primitivity/source hypotheses. The charged claim about an automatically
existing next child pair at `u_s>=2` overstates what the gcd calculation
alone establishes.

The p.174 Definition–Remark says:

> The conclusion (1) implies that if `M_h=n-1`, then we should drop it from
> our own consideration. The “effective” characteristic pairs exclude
> `M_h` if `M_h=n-1`. The last effective characteristic pair is denoted by
> `M_s` in this article.

Exactly **90** operative rows have raw terminal `M'_{h_0}=n'-1`; all have
`u_s=1`. On every one, the raw terminal gcd is 1 but the **post-drop**
terminal gcd is greater than 1. Hence `d'_{s_c+1}=u_s=1` is false on these
90 rows. If the p.174 effective convention is available for the actual
child, its boundary value is the remaining gcd, not necessarily 1.
The child's monomial-Jacobian category still requires source justification.

A concrete rescue makes the index error visible:

```
parent (108,72), M=(-72,84,104,106), V=(8,8,3), u_s=1;
raw child (27,18), M'=(-18,21,26), d'=(27,9,3,1), V'=(8,8);
raw comparison 8<=3 fails;
drop 26=27-1: effective M'=(-18,21), d'=(27,9,3);
effective comparison 8<=9 passes; boundary V'_3=d'_3=3, not 1.
```

The named example of Section 4 has no dropped tail, so none of these
index issues is used to obtain its changed `V`.

**4. A child's own expansion at a labelled failure.** Choose the operative
row `(180,120), M=(-120,132,150,178), V=(2,4,5)`; the alternate `V_2=3`
works as well. Its source gcds are `(180,60,12,6,2)`. Thus `d_s=6`,
`u_s=1`, `v_s=5`, `ell=3`. Proposition 6.4 supplies the radius hypothesis
for Proposition 6.3. Write its actual transformed polynomials as
`F(γ,π),G(γ,π)` and put `H=T_2^ψ(F,G)`, `Q=T_3^ψ(F,G)`.
Their identification as the child's own approximate roots is not assumed.
Their coefficient ring is `k[γ,π]`, with characteristic-zero algebraically
closed `k`; `π` is the new polynomial/root variable. The prime in a label
is not differentiation.

From p.150, derive rather than assume the recurrence

```
μ_1=M_1,
μ_j=(d_{j-1}/d_j) μ_{j-1}+M_j-M_{j-1}.
```

It yields `μ_1=-120, μ_2=-108, μ_3=-522`. Proposition 6.3(2) therefore
gives the **exact** π-degrees

```
deg G=30, deg F=20, deg H=18, deg Q=87;
J(F,G)=c γ^3, c!=0.
```

Now hold `γ` fixed and set **the child's own** `η=G^(-1/30)`.
Normalize the nonzero leading constants to 1. Work in `k[γ]((η))`;
`G=η^-30`, `F=η^-20+...`. This is the p.150 recipe
in the new chart, not a termwise substitution into the parent's fixed-x
series. The canonical approximate-root relations (Proposition 3.1 and
its specialization, pp.157–159) retain the forms

```
H=F^3-c_1 G^2 + lower canonical terms of (20,30)-weight <60,
Q=H^5-c_2 G^3 + lower canonical terms of (20,30,18)-weight <90,
c_1,c_2 != 0.
```

Here the canonical F exponent is less than 3 and the H exponent less
than 5. The weight-90 monomial in that basis is uniquely `G^3`:
`20a+30b+18e=90`, `0<=a<3`, `0<=e<5` forces `(a,b,e)=(0,3,0)`.
Every canonical weight in the second relation is even. Proposition 6.3
multiplies every source canonical weight by 1/6, preserving strict lower
weight inequalities; no new bound on child coefficients is being assumed.

Let `A` be the root of `H(U,η^-30)=0` with leading term `η^-20`.
Formal Hensel recursion gives `A in k((η^10))` and
`ord_η H_U(A,G)=-40`. Since the actual `H(F,G)` has order `-18`,

```
F=A+a η^22+terms of order >22,  a!=0.
```

There is no earlier exponent not divisible by 10. For the next step put
`U=A+η^22 W` in `Q`. Its initial equation is a fifth-degree equation with
five nonzero simple roots. Since `ord Q=-87>-90`, its order -90 coefficient
vanishes, so `a` selects one of those roots. That root lifts to
`B in k((η^2))`. The leading derivative has order

```
ord_η Q_U = 4*(-18)+(-40)=-112.
```

Canonical lower terms have strictly later derivative order: differentiating
an H factor in a monomial of weight `w<90` gives order `-w-22>-112`;
differentiating an F factor is later still. Exact `ord_η Q(F,G)=-87`
therefore forces

```
F=B+b η^25+terms of order >25,  b!=0.
```

No odd exponent precedes 25. Applying the printed p.150 recipe to this
own-child expansion now gives, rather than merely recomputing a proposed
list's gcd,

```
M'_1=-20, d'_2=gcd(30,20)=10;
M'_2=22,  d'_3=gcd(10,22)=2;
M'_3=25,  d'_4=gcd(2,25)=1;  M'_4=infinity.
```

The chain-rule identity at fixed `η`, `F_γ|η=J(F,G)/G_π`, has first possible
order 29, since `G_π` has leading term `30η^-29`. Thus the coefficients
at 22 and 25 are nonzero constants, which p.150 explicitly retains.
This establishes the child's **own** `M,d` at this failing row.

For source accuracy, p.154's prose explains recovery from the degrees of
the quasi-approximate roots. Its printed recovery display has an apparent
denominator inconsistency with p.150. No result here relies on that
display: the recurrence was derived from the p.150 definitions, and the
two Hensel steps supply the required independent expansion calculation.

**5. The own-child top count is different.** The source radii are
`δ_3=1/6`, `δ_2=1/5`; `δ_1=2/3` for `V_2=2` and `1/2` for `V_2=3`.
The major disc `D_3` holds `(180/6)*5=150` roots of `g`. Since 150 exceeds
half of 180, its Galois conjugate must be the same disc: distinct equal-radius
conjugate discs would be disjoint and require too many roots. Its truncated
centre is consequently rational over `k((t))`, `t=x^-1`. After the source's
major slope is normalized to zero and a constant is translated away,
there is no integer exponent strictly between 0 and `1/6`. We may use
`y=ξ t^(1/6)` as its general point.

Proposition 4.6(1), p.170, gives the leading polynomials of `g,T_1,T_2`
as powers of a common `p(ξ)`:

```
deg p=V_4*d_3/d_4=5*12/6=10;
g_D3=p^15, (T_1)_D3=p^10, (T_2)_D3=p^9.
```

The selected next major branch has multiplicity `V_3=4` in `p`. The sixth
root of unity action puts nonzero coefficients at radius `1/6` in orbits
of six. A nonzero multiplicity-4 root would require degree at least 24.
It is therefore the zero root. The other six roots form one simple orbit:

```
p(ξ)=constant * ξ^4(ξ^6-a),  a!=0.
```

There are **90** source g-roots `y=C x^(-1/6)+...`, `C!=0`, and **60**
source g-roots with order greater than `1/6`. This is an exact count,
including multiplicity, not a floor or an assumed attained bound.

The actual coordinate map from pp.197–198, with different letters for
the coefficient and the constant centre, is

```
γ=y^-1,
z=A_0(γ)+πγ^5,       deg A_0<5,
z=y-βx-e,           β!=0,
x=(γ^-1-e-A_0(γ)-πγ^5)/β.
```

For an exiting branch write `x=s^-6`, `y=C s+...`. Inverting in the
physical place gives `x=C^6 y^-6+...`, hence

```
π=-β C^6 γ+terms of smaller γ-growth.
```

Six source conjugate **cover series** have the same `C^6` and become one
inverse series at this stage. If there is further ramification, the ratio
of projection degrees is still `1/6`; the calculation does not assume a
physical place equals a cover series. Therefore the 90 source roots give
exactly **90/6=15** child π-roots with a single nonzero coefficient `C_*γ`.
Roots with source order greater than `1/6` give smaller growth. The other
source tangent direction, `y~βx`, maps to `γ->0` and supplies no larger
growth at `γ->infinity`. Finite-x branches above `y=0` also give smaller growth. The
child is monic of degree 30, so its remaining **15** roots have coefficient
zero at γ. Thus its top G polynomial, after scaling `π=wγ`, is

```
constant * w^15(w-C_*)^15,   C_*!=0.
```

The other tower polynomials do not conceal a larger top disc. For `T_3`,
Proposition 4.6(2) gives source leading polynomial `p^41 q`, with
`deg q=25`, q squarefree and containing all roots of p. Galois invariance
makes q have the zero root and four nonzero six-orbits. After inversion,
the p-orbit contributes 42 Q-roots at `C_*`, three q-only orbits contribute
one each at three other nonzero coefficients, and the remaining
`87-42-3=42` Q-roots are at zero. F and H distribute with G. The full top
configuration has `p_child=w(w-C_*)` and a squarefree degree-5 `q_child`;
its radius is `δ'_3=-1`.

Either proper major child subdisc carrying G-roots contains 15, with the
corresponding H count 9. Its own normalized value is therefore

```
V'_3 = 15/(n'/d'_3) = 15/(30/2) = 1,
       also 9/((-μ'_2)/d'_3) = 9/(18/2) = 1.
```

The printed criterion on this genuine local count is satisfied:
`1<=2` (and `1>2/(30-25)`). The inherited label is **4**. Its alleged
60 roots in the child disc are actually a source count in another chart.
The reconstructed all-roots top permits `V'_4=d'_4=1` here; gcd closure
alone would not identify `V'_3`. **The copied top label is wrong.**

This is the requested first-principles stress test of a failing census row.
It establishes survival of the top comparison under the conditional child
construction, not existence of a source pair. The distinction matters
logically: from an inconsistent complete source specification any conditional
identity would be vacuous. We do not claim an actual-pair counterexample
to a universally quantified theorem; we reject promoting an exclusion
whose supposed data transfer conflicts with the computed local transition.

The charged `(96,72), M=(-72,36,78,94), V=(4,3,5)` example was also checked.
Its own expansion yields `M'=(-12,6,13)`, `d'=(16,4,2,1)`; inversion gives
an `8+8` G split and own top `V'_3=1`, not 3. However its next source layer
raises an additional cumulative Galois-stabilizer obstruction. It is not
a clean witness of source survival. The `(180,120)` example avoids that
immediate recorded-route problem. The auxiliary route diagnostics are
expressly not promoted as a further screen or as an existence theorem.

**6. U-NEG: exactly which one-line argument is valid.** Proposition 6.3(2)
says the transformed polynomials are “monic in π with π-degree”
`u_s n/d_s, u_s(-μ_1)/d_s,...`. Its proof on p.198 confirms exact degree.
Thus G has exactly `n'` roots over an algebraic closure of the relevant
coefficient field, counted with multiplicity. It does not assert that a
particular child major disc contains all of them. No such assertion is
needed for the valid elementary implication

```
if #roots(G in an actual D'_1)=(n'/d'_2) W_2,
then (n'/d'_2) W_2<=n', hence W_2<=d'_2=K'.
```

Here `W_2` is deliberately a new symbol. Replacing it by copied `V_2` is
the entire disputed step. The identity `n'/d'_2=n/d_2` proves equality
of two scaling factors; it does not prove equality of root counts.
The charged test that both counts equal `(n/d_2)V_2` simply assigns the
same V to both sides and verifies arithmetic consequences of the assignment.

The three relevant places/discs must be kept separate:

| object | coefficient parameter and limiting place | root variable / disc |
|---|---|---|
| source major tower | `t=1/x ->0` | y; source `D_1` and its specified centre/radius |
| disc used to polynomialize descent | `θ=1/y ->0`, `γ=θ^(1/u_s) ->0` | z; inverse of source **minor** `D*_{s-1}` |
| child's own infinity tower | `t'=1/γ ->0` | π; newly constructed `D'_1` |

Proposition 6.3's minor-disc hypothesis controls the second line. Its
statement does not provide the third line's centre, radius or count at
level 2. The concrete inversion above shows why this is substantive:
projection degrees change, so raw counts can change even where all
characteristic gcd labels are correct.

Moh p.207 supplies five particular transformed tables, with `u_s=1`,
and explicitly chooses child major/minor centres in the first case.
We re-read and checked all five. They support those cases; they do not
prove the same copied V describes every taller child's own tower.
The omitted `(99,66)` case has `u_s=3`, so Proposition 6.4 does not apply;
its omission is not a negative control proving that the raw child gcd
criterion is the reason for omission.

For the charged U-NEG example `(108,72)`, inherited `V'_2=11` with
`(n',m')=(18,12)` manufactures `3*11=33>18`. This establishes that **11
cannot be the actual normalized child-disc value**. It excludes the source
only after a theorem forces that identification. No centre/radius
identification was supplied by the one-liner. The old `shape.py` early
return, using `u=K-V_2` and `degx_h=u`, supplies none either. Accordingly
the claim that all 90 such rows are killed remains unlicensed by this
argument. The separate four-row split-radius calculation is not re-audited
here; even a correct proof forcing descent does not force copied level-2 V.

**7. Numerical partition and drop consistency.** The regenerated results:

| quantity | independently reproduced |
|---|---:|
| (1)–(13) census | 24,063 |
| operative population | 1,420 |
| `u_s=1` | 1,110 |
| raw labelled top failures in that block | 970 |
| effective labelled top failures | **936** |
| effective labelled top passes | **174** |
| `u_s>=2`, held outside proposed licence | **310** |
| C-TOP-only formal residual | **484** |

The `u_s` histogram is `{1:1110,2:265,3:34,4:9,5:2}`. All 90 dropped-tail
rows fail the raw comparison; 34 pass after the drop and 56 still fail.
They are disjoint from the 90 labelled U-NEG rows. All 84 `u_s=1` U-NEG
rows lie in the 936 labelled failures; six more lie in the `u_s>=2` block.
If both proposed licences were valid, the joint numerical residual would
therefore be **478**, not 484. These are conditional arithmetic counts.

The 174 passes have 46 parent degree pairs. Their published histogram
`{2:24,3:100,4:41,5:9}` is the **raw** child height. The corrected effective
height histogram is **`{2:48,3:86,4:31,5:9}`**. The 936 labelled failures
by effective height are `{3:244,4:565,5:127}`; none has effective height 2.
The 310 rows outside the proposed licence contain 225 further numerical
failures, which are not promoted here.

`scope_enum.py` records raw `s'=s-1`. `depth.py` explicitly drops terminal
`n'-1`, decrements the height and resets the boundary V. The reported
936 predicate uses that effective drop correctly; the prose gcd argument
and survivor-height histogram mix the two index conventions. Thus there
is a bookkeeping fix, but it cannot repair the mathematical V-transfer
problem. This is not a CONFIRMED-WITH-FIX kill.

**8. FALLACY-v2 and remaining typed statements.** No new exit-price claim
is made; no `charge_basis` declaration is appropriate. The source of the
root count is Moh's mathematics, not a prior validator. The audit keeps
the following separations explicit:

- Characteristic support `M,d`, chosen disc data V, a physical place and
  its conjugate cover series are different objects. The division by six
  in Section 5 is a projection-degree calculation, not a flag count.
- The exact degrees in Proposition 6.3 establish totals, not attainment
  in an unlocated disc. Parent and child roots are not the same multiset.
- The coordinate map specifies the coefficient ring, both variables,
  limiting places and nonzero constant. Equal names or equal normalizing
  factors do not establish images or counts.
- The source last index, raw retained index and child effective index are
  separate. Closing a gcd chain does not identify a chosen major branch.
- No quotient computation, saturation, Gröbner result, pole-price claim,
  second descent, merge-free hypothesis or new exit charge is used.

```
OPEN[CTOP-ACTUAL-EXCLUSION]
  The number of truly impossible source rows among the 936 labelled failures.
  The replay proves the predicate count only. This gate does not certify484.

OPEN[CHILD-LEVEL2-IDENTIFICATION]
  For each actual child, locate its D'_1 and compute its own normalized W_2.
  Prove a relation to parent data before applying U-NEG to copied V_2.
  Five printed examples do not settle arbitrary height or u_s>=2.

OPEN[SOURCE-REALIZATION-180-120]
  Existence of a source polynomial pair for either named180/120 row is unknown.
  The own-child top test passes conditionally; no Keller counterexample is
  constructed or asserted. Surviving a necessary screen is not realization.
```

Notes and reproducible artifacts are under `box/ctop-gate-20260905/`:
`r2-enum-audit.py/.json/.log/.md`, `r2-child-row180.md`,
`r2-child-firstprinciples.md`, source licence notes, fresh page renders,
and `r2-enum-routes*`/`r2-enum-stabilizer*` diagnostic artifacts. The latter
diagnose recorded routes only, with missing-centre-support caveats; their
counts are not new mathematical exclusions. The input manifest and final
artifact hash list accompany them. No charged input, old artifact, ledger,
`jc2-lean` file or `ideation-*` file was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24510`.
- Body SHA-256:
  `840d12aa45d0fd70efbf8a5855992601bdfcb89d389594d3f8442601a64d5934`.
- Frozen basis: `c4707ea87f919f408b354cb0e443779c62e2d91e`.
