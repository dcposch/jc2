# Registration — `(9,12)` order-three DZ20 stabilizer/valuation case

Date: `2026-08-24`  
Status: `PRODUCER-EXACT / HOSTILE DIFFERENT-MODEL REVIEW REQUIRED`

## Claim registered

Conditional on the exact coprime spectral input
`deg_z(g^3-f^4)=16`, the nontrivial order-three Kummer branch with
`k=mu=nu=0` has no rational trajectory. The proof classifies every possible
source stabilizer `e in {1,2,4}`, descends the scaling parameter, and combines
the resulting divisor congruences with the terminal ODE.

## Replay

From the repository root:

```sh
shasum -a 256 -c cases/max12_912_order3_dz20_stabilizer_valuation_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_dz20_stabilizer_valuation_20260824/replay.py \
  | diff -u cases/max12_912_order3_dz20_stabilizer_valuation_20260824/replay.json -
```

## Scope firewall

The registered claim does not consume a common-factor/noncoprime spectral
stratum, nonzero `k,mu,nu`, the order-one polynomial core, any Taylor-boundary
exclusion, `(8,12)`, maximum-twelve automorphy, a counterexample, or JC2.
