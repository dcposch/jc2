# RESUME lane (round 2 of graded-moh-astra-20260905, whose process died at 14:17Z on a backend "model at capacity" error after 30 min of real work — NOTHING mathematical was wrong): your round-1 draft is charged (report-draft-r1.md, 21KB): it PROVES the completed Moh chart ideal I is N²-homogeneous for deg z=(b, iK−a), deg c=(ℓ+1, D) (monic-block deficit grading; row x^b y^a h^j has degree (b+1, D−a−jK); h-adic and ordinary coefficient ideals agree) ⇒ V(I) is a CONE, and sets up the exact c=1 torus section and finite bidegree membership tests. Round 1 also left RUNS IN FLIGHT on a worker it launched: box/graded-moh-20260905/runs/*/status.json (fields host, pid, state; msolve slices at 420 GiB memory limit RUNNING at death; Singular slices FINISHED rc124 at 600 s) and box/graded-moh-20260905/{instrument,truncation,proof,validation,ops}/. TASK: (1) ADOPT, don't redo: locate your round-1 worker(s) via the status.json host fields and `sh ops/fleet/fleet.sh ips` (instances launched after 13:47Z today that are not 172.30.0.7/.18/.28 — those belong to other lanes); ssh in (~/.ssh/jc2-fleet), check whether the msolve slice runs are still alive or finished, harvest their outputs and status; (2) FINISH the mathematics of the draft: the cone statement, the c=1 torus section, the bidegree-truncated membership computation and its truncation bound (state exactly to which bidegree the computation must go to be a proof of c^N ∈ I, and whether that bound is reachable), the low-weight triangular subsystem test; (3) RUN the finite certificate computations on the four smallest fibres (77 / 111 / 129 / 136) as the draft planned, on the adopted worker (launch one more r7i.16xlarge only if needed); any exact-Q UNIT or rational identity is a class kill under the gate's §8 rule — full custody; (4) SEAL a complete report (the draft's disposition + final solver dispositions). TERMINATE every worker you or round 1 launched before sealing (`fleet.sh term <ID>`); never touch .7/.18/.28. FALLACY-v2 (modular UNIT = signal; exact-Q or a rational identity = certificate). ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Continue in box/graded-moh-20260905/.
Report: xmodel/graded-moh-astra-r2-20260905.md
Seal (<!-- BODY-END -->); 15-30KB; 150 min.
charged_input=box/graded-moh-20260905/report-draft-r1.md
charged_input=xmodel/graded-moh-astra-20260905.prompt.md
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/graded-moh-astra-r2-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
0c7237a34c50adf774e1ce973c38353108dc249e50653df5b5b14be6307a7bee  {{LANE_INPUTS}}/report-draft-r1.md
4fa79b3736378a9ab0df842ff54f158c3a1a9905bb5fd6bb1a86c4577da8e328  {{LANE_INPUTS}}/graded-moh-astra-20260905.prompt.md
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
c0ea96034bf12b7445aa123f00cf600baaca81751f36a91855987f44fd6311e3  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
