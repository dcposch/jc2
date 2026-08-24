# Round 2 D root: `D-STATE-GATE`

**Date:** 2026-08-24 UTC  
**Verdict:** **`NO-TYPED-STATIONARITY`**  
**Independent replay:** **PASS**  
**Tier:** source-typing result only

## 1. Result

The corrected 30-input / 30-output pure-`y` source has a genuine six-band
structure through the exact banked window, but the current repository does
not type that structure for the full polynomial source.

At both registered primes, an unreduced rebuild at the banked D25 witness
proves all of the following through band 40:

- the 30 input residue ladders are disjoint six-step ladders with the recorded
  starts and `PIN42` exception;
- the corrected 30 output streams include the genuine `H_29` stream starting
  at band 36;
- the first-occurrence layers at bands 26, 32, and 38 are the exact shifted
  ten-row / ten-coordinate type;
- forgetting a new layer leaves every lower source row unchanged, so the
  registered truncation squares commute coefficientwise;
- the dual-source derivative equals a separately grouped differentiation of
  the written Euler product rule; and
- after simultaneous input/output relabeling by six, the three exact relative
  matrices obey

\[
M_{38}-2M_{32}+M_{26}=0.
\]

This is the expected Ore-affine law, not a recurrence fitted to the three
matrices: for fixed output label, source family, and offset `d=n-r`, the
unreduced product rule has the form `A_d+r B_d`, because

\[
\theta(t^rZ(u))=t^r(r+6\Theta)Z(u),\qquad u=t^6.
\]

The full-source gate nevertheless stops before a stationarity signal.  The
normalized polynomial factors begin

\[
U_f=1+\alpha_1t^{42}+\cdots,qquad
U_g=1+\beta_1t^{42}+\cdots,
\]

and

\[
\Phi_{\rm full}=U_f\Phi_y,qquad
\Gamma_{\rm full}=U_g\Gamma_y.
\]

Two independent exact coefficient derivations give

\[
\boxed{
[t^{42}]\mathcal E_{\rm full}
=[t^{42}]\mathcal E_y
+42S_MG_M(3\alpha_1-2\beta_1)p(\eta)^4p'(\eta).}
\]

Both `alpha_1` and `beta_1` partials are nonzero over the rationals and at
both registered primes.  Yet neither coordinate belongs to the registered
30 tail streams, and the present source constructor accepts no x-side
argument.  The repository explicitly leaves their status as one of:

1. held fixed for a proved source reason;
2. derived from the 30 tails with an exact chain rule; or
3. an independent filtered source coordinate.

No such classification, six-shift relabeling, or projection map is banked.
Choosing one here would invent the state map.  Hence the honest verdict is
`NO-TYPED-STATIONARITY`, rather than `SOURCE-MISMATCH`, `UNBOUNDED-STATE`, or
`STATIONARY-SOURCE-SIGNAL`.

## 2. Frozen candidate state and relabeling

With `u=t^6`, the repository candidate is

\[
X_y=\bigoplus_{q=1}^{30}t^{r_q}k[[u]],\qquad
Y^+=\bigoplus_{a=0}^{29}t^{s_a}k[[u]]e_a.
\]

The input families and residues are:

| families | residues |
|---|---|
| `tf1,tf2,tg1,tg2` | `0,1,2,3,4,5` each |
| `tg01,tg02` | `0,2,4` each |

Their starts are `r_rho=6+rho`, except `r_4=16`; their sum is 288.  The
output starts are

\[
s_a=6+2((a+1)\bmod3)\ (a\le28),\quad s_{28}=16,\quad s_{29}=36,
\]

with sum 276.  The frozen relabeling was

\[
T_X(f,r)=(f,r+6),\qquad T_Y(a,n)=(a,n+6),
\]

together with the Ore conjugacy `Theta -> Theta+1`.  This state and its
verdict taxonomy were preregistered before execution.  The old 29-output
state is not reconsidered: `H_29` already refuted it, and the present gate
keeps `H_29` explicitly.

## 3. Exact banked-row evidence

For each prime, the producer reconstructed the same promoted D25 witness used
by the reviewed transition, then invoked only the cyclic products and pristine
Euler expression.  No row reduction enters the source arrays.

| prime | source paths agree through 40 | layers | projection squares | Ore second difference |
|---:|---|---|---|---|
| 105337 | yes | 26, 32, 38: exact `10 x 10` types | exact | zero |
| 105673 | yes | 26, 32, 38: exact `10 x 10` types | exact | zero |

The band-26 coordinate layer is the reviewed one:

```text
tf1_53 tf2_53 tg1_53 tg2_53
tf1_58 tf2_58 tg1_58 tg2_58 tg01_58 tg02_58.
```

The next two validation layers are obtained by adding 6 to every displayed
absolute level.  They were not solved and make no nonemptiness statement.
A combined unit finite difference in each layer was rebuilt from source; it
was zero below that layer and equal to the exact source derivative at the
first band.

The residue-zero output layer has nine rows at band 30 and ten at band 36,
where `H_29` first enters.  This is a registered transient, not evidence
against the corrected state.

## 4. Two source derivations and independent replay

For the pure-`y` window, the producer compared the ordinary dual-number
product with the separately grouped four-term derivative of

\[
(\theta\Phi-12\Phi)\Gamma_\eta
-\Phi_\eta(\theta\Gamma-18\Gamma).
\]

For the first full-source interface, derivation I factored the product rule:

\[
\mathcal B(U_f\Phi_y,U_g\Gamma_y)
=U_fU_g\mathcal B(\Phi_y,\Gamma_y)
+U_g(\theta U_f)\Phi_y\Gamma_{y,\eta}
-U_f(\theta U_g)\Phi_{y,\eta}\Gamma_y.
\]

Derivation II directly extracted the four unreduced Euler terms at `t^42`
using

\[
F_0=S_Mp^2,\qquad G_0=G_Mp^3,
\]

before simplifying.  Both give the boxed identity above.

The independent replay imports neither producer routine nor its polynomial
engine.  It rebuilds both modular witnesses and the band-38 projection square,
recomputes all three matrix hashes and the Ore second difference, and uses a
separate sparse bivariate `(t,eta)` expansion to recover both x-side partials.
It also rehashes every provenance source and confirms that the current
constructor and 30 labels contain no typed x-side interface.

Producer core SHA-256:
`fa2e2ec2323306b8aa461b0ce7e850b4fe05f0c91d0ea08666d509c317aa8ef0`.

Independent core SHA-256:
`a43d99621955796dc35dd570904fbfe5bf70d39406d4fd9cc479a18fd11841dc`.

## 5. Interpretation and stop

The positive pure-`y` result is useful but not a full-source stationarity
theorem.  In particular it does not license the first syzygy/Spencer
obstruction, an Ore/Fitting object, or an inference about a compatible tail.
The D finite-shift route remains stopped until a source-derived x-side
classification supplies the missing arrows and the all-depth output typing is
closed.

This run did not emit, solve, or sample band 28; did not specialize a row-42
D43 point; and did not use D43, integral, p-adic, inverse-limit, germ, or
characteristic-zero claims.  The row-42 calculation is only the universal
coefficient identity identifying the first missing state interface.

## 6. Replay

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/dstate_gate.py \
  --output cases/round2_dstate_gate/results.json

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/replay.py \
  --input cases/round2_dstate_gate/results.json \
  --output cases/round2_dstate_gate/replay.json

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_dstate_gate/verify.py
```

`cases/round2_dstate_gate/MANIFEST.sha256` pins the preregistration,
provenance, both implementations, both JSON records, verifier, and this
report.  No shared top-level ledger was edited.

