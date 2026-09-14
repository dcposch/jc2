# ROOT intake: Keller dynamical-degree FIRST

2026-09-14 19:32 UTC, swarmHQ ROOT (Astra).
Basis 3bad66352ac2eb85af19a42f48ed8edd4dbafb46.

## Decision

KELLER-DYNAMICAL-DEGREE-1 is PROMOTED / MANUAL at the named-import
tier: for polynomial F:C2->C2 with constant determinant0<|c|<=1,
lambda1(F)>=generic degree d. This includes normalized JC2 and fresh
applications after determinant-one polynomial source/target automorphisms.
No invariance of lambda1 under independent changes is assumed.
For d>1 this excludes sqrt(d)<=lambda1<d, not equality or faster growth.
No inverse, properness, candidate, new classical degree bound or JC2 proof.

The imported Dinh--Nguyen--Truong Theorem1.1 and its equilibrium-measure
background are not proved from scratch here. Their primary statement
applies to dominant meromorphic compactifications, with no affine
properness assumption. Fable independently reconstructed all elementary
steps and controls and gave PASS, import-dependent. No novelty claim.

ROOT qualification: Fable's Urysohn function vanishing on H_infinity need
not have its SUPPORT contained in C2, contrary to its wording. Its positive
value at the selected point already suffices. For the producer's literal
compact-support formulation, take a compact K inside an affine ball with
mu(K)>0 and a cutoff equal1 on K, zero outside a larger affine ball;
extend by0 to P2. The resulting function is continuous and supplies exactly
the required positive affine sum. Thus the verdict is unchanged.
The lower sqrt(d) endpoint consumes standard dynamical log-concavity,
explicit in DNT's degree definitions. No unreviewed Lyapunov-exponent
alternative or suggested extension to |c|>1 is consumed.

## Custody and readback

Producer report: xmodel/keller-dynamical-degree-swarmHQ-root-20260914.md
full b492c9ca68c73e420aedf3169e94e24b673ad9bcf8df572c4e5e662dd9eeb432;
body affc812d62019f2cd3a5dbb9a170d38dca2a985f3666c229cb63a0259e0bd8a2;
manifest c6064ca9d025e8d3e460d948b4e00a53a6d4af22cf6e2caa483e0de6ab338ade.
ROOT transaction verified after final author write and after FIRST.

Different-model Fable5.1 report:
xmodel/keller-dynamical-degree-gate-fable51-20260914.md
0ee9edc9b00b97c1f11b9c22d5778496dad4d8d8b9be2d761d7f07d0709234b4.
Run receipt a42eab2363e9ffbd1bc3482341a6e3690fdfac8406961b1e15f0ae1d03cad603;
log cd7f9c6af92db2dccdbe1d82d7bb7556fee85f9caf2c8ca4341a40f85f3902b6.
Prompt 2d9f78891f1507adbd6b51e47ef526baf6cef93140abf1d00cc0c4368fd90f72.

Started19:20:44, ended19:30:13; DONE0, CLEAN, BODY_SEALED, ABSENT;
four charged inputs UNCHANGED. Actual model child was confirmed within
10seconds. Independent runtime cap19:30:44 was not reached; five-minute
target missed4m29. Terminal unit Main0/Control0/inactive/dead19:30:18,
then original1748379/1748561/1748562 all absent BEFORE receipt/pins/report.
All four current inputs and prompt/adapter/launcher/appendix/validator/seal
pins matched the receipt before whole report intake. Receipt hash remained
unchanged afterward. The exact composed prompt was independently rebuilt
from the retained prompt, recorded input-directory substitution, two LF
bytes and FALLACY-v2; its f03c46fa54ef0801877775e0c164f227796d8b0453a34f78bb91717eccb4cb96
hash matches pre/post. Ephemeral snapshots were cleaned by the launcher;
retained inputs and receipt checks are not a claim those deleted paths
were reread. Log HASH_ONLY; no independent full tool-log audit.

ROOT read the whole producer and FIRST reports. Primary scope: selected
introduction/Theorem1.1, degree definitions and section5 definitions plus
concluding construction, not the entire analytic proof. Fable's precise
primary read ranges and independent PDF-to-text match are in its report.
No scientific computation or process-policy modification occurred.

## Primary acquisition and preservation

The third-party paper is retained locally, not redistributed in this Git
bank. Fetch https://arxiv.org/pdf/1303.5992v1 to dnt-1303.5992v1.pdf;
expected SHA855f678593b0f58fa3df1d049d9a045106679292aa15517e0abfc85d15d43f6a.
Run pdftotext -layout with Poppler24.02.0 to dnt-1303.5992v1.txt;
expected SHAcac2f963b79e505d52e9e08e09ec5ead837ffb406e7295c374e24ded7abb93b9.
Both names live in this intake's directory. A replay must match these
hashes or stop; a later re-rendering is not the reviewed input.
The public prompt, report and run receipt retain the full input pins.

Resource delta569 Fable terminal lane-wall seconds; cumulative100789,
not tokens, credits, CPU seconds or billed usage. No AWS worker or model
successor. Global ranks/closing gaps unchanged; no full-round/sweep credit.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4618`.
- Body SHA-256:
  `433d67c87c031d995a43bc169d607dce08b597cfaebb51d9544c881cb764e250`.
- Frozen basis: `3bad66352ac2eb85af19a42f48ed8edd4dbafb46`.
