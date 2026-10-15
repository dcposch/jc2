# Independent hostile review: full F10 normalization carrier

Reviewer: swarmHQ / gpt-5.6-sol, native agent /root/f10_normalization_hostile_sol_2228.
Producer under review: swarmHQ ROOT / gpt-6-astra.
Evidence: MANUAL / desk-only. Verdict: ACCEPT_SCOPED.
ROOT transcribed the following final review message without mathematical edits.
Final review UTC: 2026-10-15T22:31:14Z. Public basis c67216eae319958370d70c53b9c3dc97612ed082.

## Frozen input and publication binding

The reviewed 8315-byte Git blob is reproduced byte-for-byte at the beginning
of [the public producer report](f10-full-normalization-swarmHQ-root-20261015T222707Z.md).
Its SHA256 is 9b62c4432783e66337fd8ec0e8dee2e57e15b8570ec398048970699cbaa48193.
The original immutable HQ commit is bc861615a4d5dc1b297efa1e3c1afef6f2771a73.
Publication adds custody/link/collision metadata after those bytes; it does not
change the reviewed proof. The historical UNREVIEWED producer header is retained.
The separately published integration is the binding lifecycle/scope decision.

## Verbatim final review

FINAL REVIEW — ACCEPT_SCOPED. Completed 2026-10-15T22:31:14Z.

Custody/read: banked bc861615a4d5dc1b297efa1e3c1afef6f2771a73 blob is 8315 bytes, SHA256 9b62c4432783e66337fd8ec0e8dee2e57e15b8570ec398048970699cbaa48193. Working file is ordinary regular file, 8315 bytes, mode664, same SHA; /home/ubuntu/swarmHQ, briefs, and file ancestry are nonsymlinks. Read banked lines 1–166 in windows 1–32,33–64,65–96,97–128,129–160,161–166. Applicable AGENTS/policy/state/runbook routing read; holds preserved.

Independent checks:
1) T0: y and y+1 are comaximal. On D(y), z=(x-u)/y recovers the p,z localization; on D(y+1), t=p/(y+1) recovers the S,t localization. Hence these smooth opens cover, so T0 is normal; intersecting the two whole chart rings gives T0 (membership in both implies membership in both localizations, whose intersection is T0). The phrase “both entire planes as charts” should be understood as the two admitted plane embeddings, not as the displayed principal opens themselves being entire planes.
2) With theta=t/S^r, the top forms are C=theta^3+d_r theta^2+v_2r theta+a and monic quintic D. The top Jacobian is mCD'-nC'D=-theta^7. Thus every C-root is nonzero/simple and not a D-root. For any target-containing DVR with nu(S)<0, S^-1 is positive, A/S^m gives a monic integral equation for theta, and reduction forces C(theta_bar)=0; then B/S^n reduces to the nonzero D(theta_bar), yielding nu(B)=n nu(S)<0, contradiction. So S∈V. If t∈V use C[S,t]; otherwise z=1/t is positive and the exact identity A=p(1+zd+z^2v)+k-d-zv+uv has unit p-coefficient, forcing p∈V. This covers arbitrary target-finite DVRs, including z=0.
3) No circular finite/proper premise: finite field extension follows from nonzero Jacobian; finite normalization N is a normal noetherian Krull domain. The DVR argument gives T⊂∩N_q=N. Conversely every element of N is integral over C[A,B], hence also integral over T⊃C[A,B], and lies in Frac(T)=L; normality gives N⊂T. Therefore T=N and target finiteness follows afterward.
4) In p,z, W=pz, Delta=-g/z, K=z^2(1+pg), so V=1/g and U=g^2(1+pg) agree on the overlap. Expanding S=p(H-1/V)^3-(H-1/V)^2+u(H-1/V), using p=UV^3-V, gives exactly the displayed corrected polynomial S, including (1-UV^2)(p+ell). D(V)∪D(J)=A2 since J=1-VH. At V=0 the J-chart gives t=0, p=0, S=u^2+ell-U, and forward U=u^2-S+ell, so the entire source line is present. D0 is the single graph g=0≅A1; Delta=0 cannot meet t=0, so there is no second chart component.
5) dU∧dV=g dp∧dz (directly from U=g^3p+g^2,V=g^-1). Since the now-proved map is finite between smooth surfaces in char0 and ord_D0(g)=1, the ramification divisor coefficient is one, hence generic e=2. No tangential degree-one/image-singularity/local-degree conclusion follows.

Essential-control check: without the Wronskian/coprimality guard, take formal top forms C=(theta-alpha)^3,D=(theta-alpha)^5 (alpha≠0); a valuation S=q^-1, theta=alpha+q^M with M large makes both top expressions target-finite while S has a pole, so the Section 2 contradiction disappears. Independently, using only the p,z inverse g=1/V omits the whole V=0 source line; the S,t/J chart is essential to the full-source claim.

Scope: this proves the full normalization only for complete F10 inputs satisfying every stated degree, full Jacobian, and two-chart polynomiality premise. It neither asserts such an input exists nor excludes it, solves JC2, proves tangential degree one, repairs the trace/connectivity gaps, or extrapolates beyond this surface/F10 setting.

## ROOT transcription boundary

The verbatim review ends above. ROOT independently checked the weighted monic
equation, both ring inclusions, the full corrected inverse, and the two controls.
The first control concerns formal top forms only; it is not a complete F10 point
or a counterexample retaining the whole Jacobian equation. A formal arc with
constant coefficient field should be understood as an escape test; it does not
assert an injective embedding of a two-variable field into C((q)).

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `c67216eae319958370d70c53b9c3dc97612ed082` (Git blobs only).

The later clarification below raises no OPEN label; EMPTY is not a novelty verdict.

## Reviewer clarification (same admission, 2026-10-15T22:34:02Z)

CLARIFICATION confirmed, 2026-10-15T22:34:02Z. Take q,xi algebraically independent, S=q^-1 and theta=t/S^r=alpha+xi q^M inside C(xi)((q)). Then q=S^-1 and xi=(theta-alpha)q^-M lie in C(S,t), so trdeg_C C(S,t)=2 and the assignment is injective. Restricting the q-adic valuation gives nu(S)=-1, while S^m C(theta)=xi^3 q^(3M-m) and S^n D(theta)=xi^5 q^(5M-n) are integral once 3M>=m and 5M>=n. Thus this is the precise valuation-level negative control: without the Wronskian/coprimality guard, simultaneous target-finiteness need not exclude an S-pole. It deliberately is not a complete F10/Jacobian source point and changes none of ACCEPT_SCOPED.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6112`.
- Body SHA-256:
  `1cd35660aa8b820ed0ca8af13c0ff4da63dae84ed0a2feec3bb0133e9c0e1896`.
- Frozen basis: `c67216eae319958370d70c53b9c3dc97612ed082`.
