# K7 B9 Q0 original long solve — terminal custody, INCONCLUSIVE

Coordinator root, 2026-09-07 04:40 UTC. Basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.
This is an operational terminal record, not a mathematical promotion.

## Outcome

All three original jobs started 2026-09-06 08:30:00 UTC and reached their
72,000-second wall limits. Each runner returned124, each watchdog recorded
running=false and rss_killed=false. No completed basis block, unit framing,
certificate or point was produced. Typed verdict: INCONCLUSIVE for every job.
No retry, extension, new CAS invocation or additional polynomial arithmetic.

| Original route | End UTC, September7 | Sampled peak RSS, KiB | Scope |
|---|---|---:|---|
| a_slimgb_dp | 04:30:01 | 6,719,240 | exact Q,72 variables,241 rows |
| b_std_wp | 04:30:03 | 63,069,140 | exact Q, frozen weighted order |
| c_tri_qv69_slimgb | 04:30:01 | 24,853,652 | Q(v69),71 variables |

Original RSS caps were73,400,320KiB per job, sampled every15seconds;
timeout TERM grace was120seconds. No swap was reported. The c output records
eight triangular substitutions and220 surviving generators, then stops during
slimgb; these printed diagnostics are not a new independently replayed theorem.
Even a hypothetical unit over Q(v69) would require denominator clearing and
reclosure with v69*v71-1 before an exact-Q claim. No such unit was returned.

## Terminal-first custody

Exact worker i-0e5c65e66b8dc4dfc,172.30.0.73, owner
k7-b9q0-longsolve-20260906; boot8b9dfc2b-8ec9-4d8b-953a-281dc56ee218.
Remote directory /home/ubuntu/k7-b9q0-longsolve.
Read-only collector first verified DMI/boot and absence of original outer
runner groups3446/3447/3448, inner groups3459/3460/3461, named PIDs and
matching directory argv. It then read terminal receipts before input/output
streams, checked pins, framed output without polynomial parsing, and rechecked
process absence. Status probes04:21 and04:29 returned LIVE_NO_ARTIFACT_READ.
The earlier live-only collector omitted outer runner groups; those groups
were added before terminal capture. No live output was consumed.

Terminal capture04:31:06.110205 UTC:
`box/k7-b9q0-terminal-harvest-20260907/terminal.json`, SHA256
`17fa99c8b8266324c532fa6b8384f8f08272e55572e5e2c825b867af95348460`.
Collector SHA256
`8c6911ac8198331fd79c2dee426ea23fe26c75ef942eff187d7b698c7316406b`.
All33 exact listed files,50,723,880bytes, were copied into that directory's
evidence/ tree and checked byte-length/SHA256 against the terminal manifest.
Copy receipt SHA256
`c0a01b87b92237edef00eac885c7db152c9d9c9b6450edf63acb4e815286b11e`;
the collector/copy dispatch took2.906303seconds. Root read both complete
receipts and collector/copy code. This is custody verification, not full-source
arithmetic or a certificate replay. Do not rerun harvest_once.py: it is an
exclusive one-shot collector and correctly refuses an existing terminal.json.

Original chart SHA256
`15b4b715767a72e152f340dda11354af380897f6670d6370f0542841cdb4c275`;
job hashes respectively
`308e6198ba6c9f8ec456be78dec500bed123af181709618f0afb754c18de3cfc`,
`4435caf9b8eb5f5eaf294dcb8fb884f7a545de39ee94d2d98bfe7245816d014d`,
`50dee16947b02f7c24379d06d07a8b2c4fe6a86e9a35163cec11349269428cea`.
All original runner/watchdog/generator pins also match the terminal manifest.

## Worker disposition and limits

Root fresh EC2 ownership/disk check and04:39:27 SSH DMI/boot/user-process
inventory confirmed the exact worker idle: only user-systemd,sd-pam and this
SSH diagnostic remained. Root then issued STOP for this exact instance.
At04:40 UTC EC2 still reported STOPPING; fresh04:41 EC2 confirms STOPPED.
No force-stop, termination or deletion was used.
EBSvol-01155d0dba3e3db78 remains attached; DeleteOnTermination=true, so do not
terminate casually. All full remote files and the verified local copies are
retained. No mathematical conclusion follows from resource exhaustion.

JC2 remains unresolved. No point, properness, chart exclusion, global125 bound,
or arbitrary-degree conclusion is established by this packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4062`.
- Body SHA-256:
  `f204df53fdadc34e3497db161d88b2e2af795600de571da0fe60e0aa585c7120`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
