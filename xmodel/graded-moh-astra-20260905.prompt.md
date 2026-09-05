# STRUCTURE lane (make the source-complete Moh ≤100 charts COMPUTABLE by their grading; the (T) kills are now blocked only by memory — every full solve alloc-fails at 8–48 GiB, 17(rrrrrr)/(ssssss)/(uuuuuu) + the h-support gate): the h-support gate (frozen) PROVED the source-support theorem — final charts S_i=D_i∪G_i in box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes/ (12 fibres, 77–487 parameters; G_i class-uniform so exact-Q UNIT on ANY ONE completed fibre kills its class). Its own proof exhibits the STRUCTURE the solvers ignore: with x weight 1 and y weight d=−δ_s the pair is weighted-bounded (deg_x[y^a]F ≤ floor(d(L−a))), and the chart parameters carry a GRADING (weight of h_ba/A_i,ba/B_i,ba = the weight of the monomial they multiply, modulo the block); J(P,Q)=c·x^ℓ is then a quasi-homogeneous identity. TASK: (1) PROVE the chart ideal I (before adjoining Tc−1) is homogeneous for an explicit Z-grading (or Z²-grading: x-weight and y-weight separately, plus the torus (x,y)→(λx,μy) with P,Q rescaled) of the parameter ring, so V(I) is a CONE — hence (T)=UNIT(I+(Tc−1)) ⟺ c ∈ √I ⟺ the cone V(I) lies in {c=0}; (2) exploit it: a homogeneous ideal admits DEGREE-TRUNCATED computation (Hilbert-driven std / truncated Gröbner up to the degree where c^N ∈ I must appear; the K16 lanes' truncated-Fröberg/socle instrument 17(oooooo) is the same idea) and TORUS-QUOTIENT reduction (fix the torus gauge: set a nonzero-weight coordinate to 1 per torus factor, dropping 1–2 parameters and, more importantly, killing the cone's degenerate directions); also test whether the grading makes the LOW-weight subsystem (the equations of weight ≤ w₀ involve only the low-weight parameters — a triangular staged system, cf. staged_band_emitter 17(xxxxx)) already force c=0; (3) RUN it: smallest fibres first (m12_m2_5/V1_1_6: 77 params; 2_9/V3_8: 111; m15_14/V1_9: 129; 2_9/V1_8: 136) with msolve/Singular on a big-memory worker; any exact-Q UNIT (or c^N∈I with the identity) is a class kill under the gate's consumption rule (§8) — record with full custody (ring, generators, order, solver, rc, identity); (4) if still compute-bound, deliver the best STRUCTURAL reduction (the cone statement, the minimal weight w₀ at which c is forced, the truncation degree bound) as the instrument for the next push. FALLACY-v2 (a modular UNIT is a signal; exact-Q confirmation or a rational identity Σa_if_i=1 is the certificate; no cap/prefix specialization counts). FLEET: launch your own workers with `sh ops/fleet/fleet.sh launch 1 r7i.16xlarge` (512 GB; r7i.24xlarge=768 GB, x2idn.16xlarge=1 TB allowed) — `fleet.sh ips`, `ops/fleet/dispatch.sh run <IP> <CLASS> <STEM>` (detached, survives disconnect), `dispatch.sh poll`; workers carry Singular/msolve 0.10.1/qqideal/msolveio; TERMINATE every worker you launch before sealing (`fleet.sh term <ID>`); do not touch workers you did not launch. ≤ 180 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/graded-moh-20260905/.
Report: xmodel/graded-moh-astra-20260905.md
Seal (<!-- BODY-END -->); 15-30KB; 180 min.
charged_input=xmodel/moh-hsupport-gate-astra-20260905.md
charged_input=xmodel/moh14-fix-solve-opus5-20260905.md
charged_input=xmodel/moh-sprime3-compiler-grok46-20260905.md
charged_input=box/moh14-charts-20260905/sprime3_compiler.py
charged_input=box/moh14-charts-20260905/builder_fix.py
charged_input=box/lib/guided_gb.py
charged_input=box/lib/staged_band_emitter.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/graded-moh-astra-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354  {{LANE_INPUTS}}/moh-hsupport-gate-astra-20260905.md
2372687402bdb5b83a9ecd28d206f215abb834508f9a937b94c81350a54f42e2  {{LANE_INPUTS}}/moh14-fix-solve-opus5-20260905.md
1f0d61f2bfae72bbd818653c95f60ed913582c2bac4e47fb93627622c51cffe3  {{LANE_INPUTS}}/moh-sprime3-compiler-grok46-20260905.md
7e6cfeedcee999a0163df9a23fd03fea695ca55a5de64e2e85b883a2fd4e1833  {{LANE_INPUTS}}/sprime3_compiler.py
d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b  {{LANE_INPUTS}}/builder_fix.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
7c2f88430158fc01b2aa4e1bc2af1902f92168d10cd48ee5095506beb149dce8  {{LANE_INPUTS}}/staged_band_emitter.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
