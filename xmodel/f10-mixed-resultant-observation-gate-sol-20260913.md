# Static FIRST: mixed-resultant observer

Sol, September 13, 2026. MANUAL / DIFFERENT-MODEL STATIC FIRST. Overall verdict: **CONDITIONAL STATIC CONFIRMED** for one bounded exploratory observation. No code was executed. This is not runtime qualification or mathematical acceptance of future output.

## 1. Formula fidelity — CONFIRMED

`truncated_power(s)` implements the literal multinomial coefficient of `u^n` in `(1+u+Xu^2+Yu^3)^s`: for counts `(a,j,k)`, `n=a+2j+3k`, `ell=a+j+k`, and the coefficient is the falling factorial `(s)_ell/(a!j!k!) X^jY^k`. It returns exactly indices 0 through 7. The inverse recurrence

```
q_n=-q_(n-1)-X q_(n-2)-Y q_(n-3)
```

is the coefficient recurrence for `1/phi`; convolution with `1+2Xu+3Yu^2` gives `phi'/phi` through index 14. Summing `logderivative[14-i-j]*T_(2t-1)[i]*T_(4-t)[j]` for `0<=i,j<=7` is precisely the stipulated coefficient `B=[u^14](phi'/phi)T_(2t-1)T_(4-t)`.

The displayed `U,V,K` match the charged compact normalization. The source forms
`P0=3V^2+(t-2)((6X+t-3)VU+KU^2)=(t-2)P`. For each actual nonzero monomial `t^iX^jY^k` of `B`, it forms `t^iX^j V^k U^(5-k)`, exactly `U^5B(t,X,V/U)`, and refuses support outside the imported bounds before indexing its power arrays. It then computes the ordered `Res_X(P0,G)` over `QQ[t]`, divides by the exact literal `(3t-5)^34`, requires zero remainder, reconstructs `R=Q(3t-5)^34`, and checks `Q(5/3)!=0`. The inverse `r=(2-t)/(3t-5)` is correct; every integer `r>=2` root is re-substituted into `t=(5r+2)/(3r+1)`.

All mathematical coefficients, monomial exponents, factor multiplicities, rational roots, and candidates cross JSON as decimal/rational strings. No float or native-number roundtrip carries those values. Verdict for the literal algebraic transcription: **CONFIRMED conditional on the curated accepted formulas and degree/support assertions.**

## 2. Static execution safety — CONFIRMED WITH BINDING QUALIFICATIONS

Only standard-library modules load before `guard`. The guard checks Linux/AWS DMI, explicit HQ exclusion, exact instance, registered tag, exact service cgroup, all real/effective/saved UID/GID values, environment, canonical output cwd, and runs before Sympy import or payload output creation. Mode parsing is closed; exclusive directory creation refuses reruns.

Checkpoint names and counts are finite. Each canonical JSON record is capped at 7 MiB, written with exclusive creation, file-fsynced, published by no-overwrite hard link, and directory-fsynced. Failure preserves a partial or already published final; traceback reaches the runner-owned durable phase stderr before the best-effort error checkpoint. Missing final observation is never classified as an empty candidate list. The accepted runner supplies one joint 840-second `RuntimeMaxSec` across both phases, per-file 8 MiB FSIZE, cgroup memory/CPU/task limits, background-member rejection, terminal receipt and lock-protected collection. Its per-file FSIZE is not an aggregate quota; the contract correctly leaves disk availability, exact worker identity, cgroup facts, archive comparison, retirement and retained EBS to ROOT.

The disabled JSON is genuinely unadmissible: wrong schema, extra `enabled`, null file pin and `UNBOUND` argv data. A future manifest is new frozen authority, not mutation of this template. Worker preflight and three causal guard refusals remain mandatory. For those refusals, “exact cause” must bind the actual terminal exception line (for example `ValueError: HQ forbidden`) or a precisely specified full traceback, not pretend the whole stderr is the bare phrase. This is a future binding detail, not a source blocker.

## 3. Sufficiency and trust boundary

**CONDITIONAL STATIC CONFIRMED** as a cheap single observation once the named worker package/native/import, identity, cgroup, credential, resource, output-space and retirement checks actually pass. The 60-second preflight plus one 840-second service is finite; failure or timeout is a preserved nondecision. Neither coefficient size below 7 MiB nor completion inside 840 seconds has been measured, so source acceptance gives no fit or successful-result promise.

The synthetic `(7t-12)(t^2+1)` smoke checks only classification and the exact corrupted-unit rejection. Factor-product reconstruction proves neither factor irreducibility nor that `R` is the true resultant; engine labels and every produced polynomial remain `OBSERVATION/UNREVIEWED`. Complete `R`, `Q`, remainder and raw factors are retained in the right order for a later independent check, but that prospective 186-point check is outside this FIRST. No absence of integer exceptions, scalar-unit theorem, full-array comparison, REG, source zero, all-F10 or JC2 conclusion can be promoted from this payload alone.

No load-bearing static defect was found and no repair or framework change is proposed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4876`.
- Body SHA-256:
  `31e07eaf3f88ab520e777680edeed61439c3fc6d5131cec2c0648a8da9ae221d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
