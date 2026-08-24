# Hostile different-model review — Hamiltonian kappa gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2`. The committed basis is
`c17bd2542b40f3178ec619ae4a73501550555336`; the producer artifacts are
frozen uncommitted additions on top of it.

Read in full:

- `xmodel/hamiltonian-kappa-gate-20260824.md`
- `cases/hamiltonian_kappa_20260824/README.md`
- `cases/hamiltonian_kappa_20260824/replay.py`

Frozen producer hashes:

- report: `1ce7ac73d117c8db403c702f35bc860c6318a2275e288a8212cee96d9a417709`
- replay: `a2711a21a6998d35034d02cc0f27eb7713682f3edf706f6d4a7e3c479f89c52b`
- README: `b68eafdc74f2a2845e7eafcd497b993ca4fa4337163519a7242fbd48ad9bc17d`

Independently rerun the replay and attack exactly these claims:

1. For a unimodular gradient `(P_x,P_y)`, the class
   `kappa(P)=[div V] in C[x,y]/D_P(C[x,y])` is well defined.
2. `kappa(P)=0` iff there is a polynomial `Q` with `[P,Q]=1`, including all
   signs in the divergence-free/Poincare-lemma argument.
3. Friedland 2001 already defines the same cokernel/Gauss--Manin operator and
   gives `M_GM(1)=kappa(P)`; Dimca--Saito type the class as
   `partial_t[dx wedge dy]`. Check only primary sources and flag any wording
   stronger than those sources.
4. Every displayed coordinate/Henon control has Jacobian one and zero class.
5. For every integer `n>=2`, `P_n=x+x^n y` has unimodular gradient with the
   displayed Bezout vector field and divergence.
6. The weight equation exhausts every monomial that could contribute to
   `[P_n,Q]=1`; the recurrence and terminal term therefore prove that no
   polynomial mate exists for every `n>=2`, not just to a tested degree.
7. The rational/formal slice has the claimed bracket and is nonpolynomial.
8. Scope: this is at most a scoped infinite-family theorem and a known-module
   identification. It supplies no universal receiver and proves neither JC2
   nor its negation.

Use exact arithmetic. Identify the smallest failing identity or missing
hypothesis if any. Do not widen the family or edit any producer/canonical
file.

Write exactly one file:

`xmodel/hamiltonian-kappa-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
the replay result and hashes, source/priority caveats, promotion advice, and
explicit scope exclusions.
