# Preregistration: `P4P1-SOURCE-HONESTY`

Frozen: 2026-08-24T03:11:17Z, before executing the gate.

## Scope and registered objects

This is a compiler-honesty micro-gate at band 42 only.  It consumes the
existing modular `a00pp` checkpoint banks at the two registered primes
`105337,105673`, the registered 22-variable det23 base ideals `I23_p`, and
the written full-source Euler expression

\[
\mathcal E=(\theta\Phi-12\Phi)\Gamma_\eta
 -\Phi_\eta(\theta\Gamma-18\Gamma)+42t^{20}.
\]

The checkpoint object is the ten rows in
`cases/d43red/d43red_p{p}_a00pp_band42.pkl`.  Its coefficient ring is the
22-variable base ring in the payload, extended by the recorded deep symbols.
The final-row object is exactly the row assembled by
`cases/d43_family2.py` / `cases/d43_nf_certificate.py`: after checkpoint
loading, adjoin independent sidecar symbols `Xf_alpha,Xg_beta` with

\[
C_h=42S_MG_M P4P1[h](3Xf_\alpha-2Xg_\beta)
\]

for the ten registered eta exponents
`h=2,5,8,11,14,17,20,23,26,29`.  No compatibility kernel, D43 solution,
or integral emitter is part of this gate.

The exact reduction ideal is the det23 ideal whose 509-element monic grevlex
bases are
`cases/directionb_det23_gb_p{p}.out.txt`, in the exact 22-variable order
stored by each checkpoint.  It is extended to the deep/sidecar polynomial
ring without adding relations in those symbols.

## Frozen tests

1. Recompute `P4P1=p(eta)^4 p'(eta)` over the integers from
   `p(eta)=eta^6-6eta^3+6`; do not import the table used by final assembly.
2. For both primes, load the ten checkpoint rows and prove by a complete
   monomial census that neither sidecar symbol occurs.
3. Independently reconstruct final assembly from the checkpoint and compare
   `final-checkpoint` byte-for-byte with the source-derived correction.
   Derive the correction a second way by direct four-term coefficient
   extraction from the written Euler expression with
   `U_f=1+alpha*t^42`, `U_g=1+beta*t^42`.
4. Parse and hash the registered 509-element Groebner basis at each prime.
   Reduce every base coefficient of the isolated correction by the exact
   reducer, retaining normal forms and membership traces.  Because sidecar
   monomials are external, reduction is coefficientwise in the 22 base
   variables.  A symbolic remainder, not samples, decides identity.
5. As controls only, evaluate the correction at the named completion
   `alpha=beta=0` and at the preregistered off-origin assignment
   `(alpha,beta)=(1,0)`.  The off-origin point is a compiler control, not a
   claimed D43 witness.
6. A separate replay must reparse the checkpoint and bases, recompute the
   integer polynomial and modular correction without importing the producer,
   and match the exact result and hashes.

## Frozen verdicts and first stop

- `SOURCE-ZERO`: all ten exact correction remainders vanish modulo `I23_p`
  at both primes.
- `ORIGIN-ONLY`: the exact correction remainder is nonzero, the named
  zero-sidecar completion is unchanged, and the preregistered off-origin
  control changes at least one row.  The label means *harmless only for the
  named origin completion*; it does not claim that the correction's full zero
  locus is the origin.
- `LOAD-BEARING`: the exact remainder is nonzero and changes a row at the
  registered origin completion (or is required for its recorded assembled
  vanishing).
- `INCONCLUSIVE`: any source/assembly mismatch, unavailable or invalid exact
  base reduction, inconsistent prime behavior, or independent-replay failure.

Stop immediately after the first decisive class.  Do not run an integral
emitter, solve or sample a new depth, infer D43 nonemptiness, consume D43 as a
premise for D-state work, or make a germ, inverse-limit, characteristic-zero,
or counterexample claim.  Do not edit a shared ledger.

## Cost cap

Two existing band-42 checkpoint files, two existing 509-element Groebner
bases, ten sparse linear sidecar corrections per prime, two fixed controls,
and one independent local replay.  No network, msolve, fleet job, support
expansion, or new source depth.
