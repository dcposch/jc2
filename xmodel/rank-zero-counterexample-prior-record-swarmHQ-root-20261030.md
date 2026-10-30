# Exact earlier record of the rank-zero counterexample

Status: PROVENANCE SUPPLEMENT ONLY. No new mathematical theorem, review or
promotion. The October30 independent review and its exact qualifications remain
unchanged; the September15 record retains its original historical status.

The counterexample in the [October30 reviewed report](rank-zero-ramification-counterexample-swarmHQ-root-sol56-20261030.md)
is the same construction already recorded on **September15,2026 at06:45UTC**,
with the two source variables interchanged. It is an exact rediscovery, not merely
a relative of the historical one-variable rational quotient cited in that report.

The [frozen September15 journal record](https://github.com/dcposch/jc2/blob/bfe525895382812aa302db8a9ccd9fb26f36fbc8/notes.md#L51828)
attributes the construction to native Astra `zero_base_constructive` and records
ROOT's differentiation, finite-algebra presentation and cusp-pullback checks.
Its historical status is MANUAL / PRODUCER-CHECKED / UNPROMOTED, with no different-model
FIRST at that time. This supplement does not rewrite that status or its bytes.

In the September notation,

    f(u,v)=uv+v^4,
    g(u,v)=3u^2+12uv^3+8v^6,
    Jac(f,g)=-6u^2.

Interchanging u and v gives exactly the October polynomials
P=u^4+uv and Q=3v^2+12u^3v+8u^6. The orientation change gives Jac(P,Q)=6v^2.
The old critical-line parametrization v -> (v^4,8v^6) is the same degree-two
map to the normalized cusp after the same interchange. The old monic equation
Y^4-6sY^2+tY-3s^2=0 becomes the October equation
u^8-6Pu^4+Qu^2-3P^2=0 after Y=u^2, s=P, t=Q.

The October [independent Sol review](rank-zero-counterexample-review-sol56-20261030T1800Z.md)
therefore adds an independent check of an existing construction, rather than a
new counterexample. Its current PROVISIONAL / MANUAL / PASS scope, the doubled
critical scheme, the failure of the whole-plane Keller-source hypothesis and
all [custody qualifications](../box/rank-zero-ramification-counterexample-swarmHQ-20261030/README.md)
remain unchanged. This is not a counterexample to JC2.

Source custody: the frozen `notes.md` at public commit
`bfe525895382812aa302db8a9ccd9fb26f36fbc8` has SHA-256
`df8751bbd69648750dced9515928be483a9a43144a446891587dabf6a906943c`.
Only lines51827-51874 were read for this supplement. The original sealed
October report, independent review and evidence bundle are preserved verbatim.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2436`.
- Body SHA-256:
  `473373fb53ccbe4cdd0fdee05fbb78e4a10766350d4f92cf53e3406ec6583d1b`.
- Frozen basis: `bfe525895382812aa302db8a9ccd9fb26f36fbc8`.
