# Round 2 D correctness: `P4P1-SOURCE-HONESTY`

**Date:** 2026-08-24 UTC  
**Verdict:** **`ORIGIN-ONLY`**  
**Independent replay:** **PASS**  
**Scope:** band-42 modular compiler interface on the registered `a00pp/I23`
cells at `p=105337,105673`

## 1. Decisive result

The band-42 `Xf_alpha` / `Xg_beta` correction is genuine source mathematics,
not an erroneous patch, and it is not zero modulo the registered base ideal.
It is harmless at the one named completion used by the D43 origin witness,
where `alpha=beta=0`; away from that completion it changes the source rows.

The exact identity is

\[
\boxed{\Delta [t^{42}]\mathcal E
=42S_MG_M(3\alpha-2\beta)p(\eta)^4p'(\eta).}
\]

The ten checkpoint rows contain no sidecar symbol.  The actual final assembler
adds exactly the boxed correction.  Reducing its coefficients through each
registered 509-element det23 Groebner basis leaves every coefficient
unchanged and nonzero.  At `(alpha,beta)=(0,0)` the correction is zero; at the
preregistered control `(1,0)` all ten rows change at both primes.  This is the
frozen `ORIGIN-ONLY` outcome.

Here `ORIGIN-ONLY` means *the omission is harmless only for the named origin
completion*.  It does not mean the polynomial has a one-point zero locus.  In
fact, over either registered field its sidecar zero locus is the line
`3 alpha-2 beta=0`.

## 2. Source derivation and actual assembly

Put

\[
\Phi_0=S_Mp^2,\qquad \Gamma_0=G_Mp^3,
\quad U_f=1+\alpha t^{42},\quad U_g=1+\beta t^{42}.
\]

The producer extracted the four terms of

\[
(\theta\Phi-12\Phi)\Gamma_\eta
-\Phi_\eta(\theta\Gamma-18\Gamma)
\]

directly at degree 42.  In units of `S_M G_M p^4 p'`, the alpha pieces are
`30*3` and `-2*(-18)`, totaling `126`; the beta pieces are `(-12)*3`
and `-2*(42-18)`, totaling `-84`.  Thus the multipliers are `42*(3,-2)`.

The independent replay instead used the factored product identity

\[
\mathcal B(U_f\Phi,U_g\Gamma)=U_fU_g\mathcal B(\Phi,\Gamma)
+U_g(\theta U_f)\Phi\Gamma_\eta
-U_f(\theta U_g)\Phi_\eta\Gamma.
\]

At degree zero, the first term has multiplier
`(-12)*3-2*(-18)=0`; the remaining two give `126 alpha-84 beta`.
The derivations therefore agree before modular specialization.

Separately, the producer exercised the actual
`d43_nf_certificate.rung_kernel` assembly branch.  On empty checkpoint input,
its ten returned deltas equal the source formula coefficient-for-coefficient.
On the complete real checkpoint row `h=29`, exact dictionary subtraction of
the final assembled row and checkpoint row again leaves precisely that delta,
while every pre-existing checkpoint group is unchanged.  The independent
replay parses both assembly implementations and verifies the same table and
`3,-2` multipliers.

The integer polynomial was recomputed rather than imported:

```text
h       2       5        8       11       14      17      20    23   26  29
P4P1 -23328  101088  -186624  191808  -120528  47952  -12096  1872 -162   6
```

The replay obtains the same table independently from
`z=eta^3`, `p=z^2-6z+6`, and `p'=6 eta^2(z-3)`.

## 3. Exact base-ideal reduction

For each prime, the checkpoint payload registers the same ordered base ring

```text
F_p[x68,x70,x71,x72,x73,x47,x52,x53,x54,x55,x57,x58,x59,x60,
    x62,x63,x65,x66,W1,W2,uW1,uW2].
```

The correction lies in its extension by the independent sidecar symbols.  In
each sidecar coefficient the base monomial is exactly `1`.  Both banked
det23 files parse as monic 509-element grevlex bases, and every leading
monomial has positive degree.  Therefore none can divide `1`.  The exact
normal-form runs have zero reduction steps and empty membership traces:
each nonzero scalar coefficient is already its own normal form.  This is an
identity certificate, not interpolation or point sampling.

| prime | checkpoint rows | checkpoint NF terms | sidecar hits | GB size | nonzero correction remainders |
|---:|---:|---:|---:|---:|---:|
| 105337 | 10 | 15,695,212 | 0 | 509 | 10/10 |
| 105673 | 10 | 15,695,214 | 0 | 509 | 10/10 |

For example, the `h=29` alpha/beta remainders are respectively
`96138,41245` at `p=105337` and `93734,78408` at `p=105673`.  All twenty
sidecar coefficients per prime are recorded in `results.json`.

## 4. What this resolves

There is no wrong band-42 source formula here.  The old checkpoint-to-final
gap was provenance and scope debt:

- the ten checkpoint normal forms genuinely omitted the two sidecar symbols;
- the final assembler genuinely added a nonzero source-derived correction;
- the correction itself is already in exact base normal form; and
- the named zero-sidecar origin completion is unchanged by adding it.

Accordingly, the earlier modular origin vanishing is not invalidated.  What
was unsafe was the unqualified slogan that every final assembled term was
covered by the old checkpoint source-to-NF traces.  The clean statement is:

> The checkpoint rows were source-to-NF traced modulo `I23`; final assembly
> adjoins the exact band-42 sidecar correction above.  That correction has
> empty base-reduction traces because its coefficients are nonzero constants,
> and it vanishes at the named `alpha=beta=0` completion.

This audit closes that correction's modular source-honesty gap only.  It does
not license an integral emitter, a new depth, D43 nonemptiness, a compatible
tail, a formal germ, characteristic zero, or a counterexample.

## 5. Replay and provenance

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_p4p1_honesty/p4p1_honesty.py \
  --output cases/round2_p4p1_honesty/results.json \
  --provenance-output cases/round2_p4p1_honesty/provenance.json

python3 cases/round2_p4p1_honesty/replay.py \
  --input cases/round2_p4p1_honesty/results.json \
  --output cases/round2_p4p1_honesty/replay.json

/opt/homebrew/opt/python@3.14/bin/python3.14 \
  cases/round2_p4p1_honesty/verify.py
```

Producer canonical-claim SHA-256:
`f147c46d55f46fd9eb009023a8beb104a93327612815c9f59d008e005d692334`.

Independent-core SHA-256:
`9245288b87d8bebd80af19de80e5798eb78716fa720dfbca12fbe10b26555b4d`.

`cases/round2_p4p1_honesty/MANIFEST.sha256` pins the preregistration,
provenance, producer, exact result, independent replay, verifier, and this
report.  No shared top-level ledger was edited.
