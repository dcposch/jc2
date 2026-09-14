# Factored Jacobian representation pilot

Owner: `/root/nonemptiness_certificate`, 2026-09-06, assigned by root.
Scope: construction measurements and a complete exact presentation on the
frozen `(99,66), delta=2` source affine space. No Groebner/solve invocation.

- Actual total degrees: F=99, G=66, hence gcd=33>=16.
- Actual partial-y degrees: F=99, G=66, from fixed leading forms.
- Physical total support cap: h<=33, D<=34, C<=35; J<=99.
- This is not the historical unbounded-total `max12` frontier. No weighted
  degree is substituted for a total degree.
- Every source coefficient expression is polynomial over Q. Source map SHA:
  `778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea`.
- Reviewed physical reconstruction is in the completed Fable gate SHA
  `5fc61ae7f4f78e7d28cde6ac3eaa7c24e7ca98966ebf94de7cbaf5ea69fb059e`.
- Mechanical gate command: `python3 ops/frontier_gate.py --total-degrees 99 66
  --purpose frontier --tag factored-jacobian-pilot-astra-20260906`; its one
  gcd criterion does not close this degree pair.

Worker: newly launched owned `i-0da0cebfc97c9fd54`, `r7i.8xlarge`,
`172.30.0.56`, root `/home/ubuntu/factored-jacobian-pilot-20260906`.
The current EC2 Standard quota was read as 1920 vCPU before launch.
No pre-existing or protected worker was used.

The worker payload fails closed before importing FLINT unless Linux, Amazon
EC2 DMI, the exact allocated hostname, and the registered job environment all
match. Scalar preflights: 120 seconds / 2 GB each. Substituted full-modular
and exact-low tests: 600 seconds / 96 GB each. Lifted exact full construction
and export: 600 seconds / 64 GB each. All use the unchanged `run_capped.py`
exact-process-group supervisor. A three-second parent-and-64-MiB-child dummy
test observed 89,559,040 aggregate RSS bytes, validated process identity and
reported complete cleanup with no live descendant after TERM.

Root explicitly approved retention of this worker after terminal publication
for independent review/next measured work. Final custody is recorded separately
in `custody.json`; no remaining active writer may be charged as final.
No solver is authorized by this pilot. No source-coverage or T2/T3-equivalence
theorem is claimed. A unit in this source family would not resolve JC2.
