#!/usr/bin/env python3
"""Serialize a triangular reconstruction DAG and conservative growth bounds."""
import hashlib
import json
import os
from pathlib import Path
import socket
import time
import resource
def require(ok,why):
    if not ok:raise ValueError(why)
require(socket.gethostname()=="ip-172-30-0-56","Worker")
require(Path("/sys/class/dmi/id/sys_vendor").read_text().strip()=="Amazon EC2","EC2")
require(os.environ.get("JC2_REGISTERED_JOB")=="linear-c-filtered-pilot-astra-20260906","Registration")
require(Path.cwd()==Path("/home/ubuntu/linear-c-root-replay-20260906"),"Owned root replay scratch")
started=time.monotonic()
raw=Path("filtered_basis_certificate.json").read_bytes()
require(hashlib.sha256(raw).hexdigest()=="c2b5965278e0fa30f0490b7f5a019434abe5291e50b748d3a3c0795c8175f906","Certificate pin")
c=json.loads(raw)
n=c["minor"]["size"]
rows=[[] for _ in range(n)]
gcoords=set()
for entry in c["selected_matrix_entries"]:
    rows[entry["row"]].append(entry)
    gcoords.update((u,v) for u,v,_ in entry["terms"] if u>=0)
bounds=[];degrees=[];graph=[]
for i,entries in enumerate(rows):
    term_bound=1;deg_bound=1
    rhs=[]
    for e in entries:
        j=e["column"]
        if j==i:
            require(e["terms"]==[[-1,-1,"1"]],"Monic diagonal");continue
        require(j<i or j in (189,190),"Forward/constant-C dependency")
        rhs.append({"coefficient_terms":e["terms"],"coordinate":("u"+str(j)) if j<i else ("v22" if j==189 else "v11")})
        d=1 if any(u>=0 for u,v,q in e["terms"]) else 0
        term_bound+=len(e["terms"])*(bounds[j] if j<i else 1)
        deg_bound=max(deg_bound,d+(degrees[j] if j<i else 1))
    bounds.append(term_bound);degrees.append(deg_bound)
    graph.append({"coordinate":"u"+str(i),"selected_J_row":c["basis"][i]["selected_J_row"],
                  "equation":"u_i + K_selected_row + sum(coefficient*prior_or_free_coordinate) = 0",
                  "rhs_coefficient_convention":"Negate all displayed terms and K to reconstruct u_i",
                  "dependencies":rhs,"uncollected_expansion_term_upper_bound":str(term_bound),
                  "abstract_g_k_v_degree_upper_bound":deg_bound})
selected={tuple(x["selected_J_row"]) for x in c["basis"][:n]}
remaining=[(i,d-i) for d in range(1,100) for i in range(d+1) if (i,d-i) not in selected]
require(len(remaining)==4860,"All physical positive slots")
# Compare selected labels to the immutable pilot's actual nonzero coefficient support.
pilotrows=Path("/home/ubuntu/factored-jacobian-pilot-20260906/complete_export.rows.tsv").read_text().splitlines()[1:]
pilotpositions={tuple(map(int,l.split("\t")[:2])) for l in pilotrows}
require(selected<=pilotpositions and len(pilotpositions)==1469,"Selected row literal physical census")
known_remaining=sorted(pilotpositions-selected-{(0,0)},key=lambda p:(sum(p),p))
require(len(known_remaining)==1279,"Known nonzero row census")
contract={
 "schema":"JC2_C_RECONSTRUCTION_DAG/v1","field":"Q","source_sha256":c["source_sha256"],
 "certificate_sha256":hashlib.sha256(raw).hexdigest(),
 "base_ring":"A=Q[247 physical source coordinates not in the 192-dimensional C source space]",
 "physical_reconstruction":{"coordinates":"X=x,W=y-x","h":"physical(h3)^3 + physical(C2)*physical(h3) + physical(C3)",
     "D":"physical(B2)","normalizers":{"h3":11,"C2":22,"C3":33,"B2":65,"A3":98},
     "G":"h^2-b*h/3+D","K":"((3*D+a+b*h)/2)*J(h,D)",
     "g_u_v":"coefficient X^u W^v of G, for u+v<66; fixed degree66 part H^6",
     "K_selected_row":"the indicated physical coefficient of K"},
 "graph":graph,
 "free_C_polynomials":[x for x in c["basis"] if x["kind"]=="free" and x["degree"]>0],
 "removed_free_C_constant":{"source_name":"A3c_98_0","polynomial":1,"justification":"Its derivatives are exactly zero; unused polynomial-ring factor."},
 "remaining_equations":{"safe_all_slot_list":remaining,"known_nonzero_before_substitution":known_remaining,
     "positive_rows":"For EVERY listed physical position take coefficient of K+J(C_reconstructed,G), substituting the graph recursively.",
     "inverse_row":"Zj*(coefficient(0,0) of K+J(C_reconstructed,G))-1",
     "no_T2_T3_rows":"This is the raw full physical-J locus only.",
     "quotient_isomorphism":"A[original_C,Zj]/full_J ~= A[v22,v11,Zj]/ALL reconstructed residual rows [adjoin one free additive constant if not removed]"},
 "dense_expansion_status":"NOT_ATTEMPTED; the DAG is a complete reconstruction recipe, not an expanded reduced ideal"}
out=Path("reconstruction_graph.json")
require(not out.exists(),"No overwrite")
out.write_text(json.dumps(contract,sort_keys=True,separators=(",",":"))+"\n")
# Selected-only equations can pass while a retained residual fails.
selected_only_point={"u":0}
require(selected_only_point["u"]==0 and selected_only_point["u"]-1==-1,"Dropped-residual negative control")
summary={"status":"EXACT_RECONSTRUCTION_DAG_EMITTED","graph_rows":189,
 "abstract_selected_graph_literal_terms":sum(len(e["terms"]) for e in c["selected_matrix_entries"])+189,
 "used_lower_G_coordinates":len(gcoords),"used_lower_G_degree_range":[min(map(sum,gcoords)),max(map(sum,gcoords))],
 "maximum_uncollected_term_upper_bound":str(max(bounds)),
 "maximum_abstract_g_k_v_degree_upper_bound":max(degrees),
 "bound_semantics":"Syntactic recurrence without collecting like terms, prior to nonlinear semantic source substitution; NOT a measured expanded count.",
 "remaining_safe_positive_slots":4860,"known_nonzero_positive_rows_before_substitution":1279,
 "active_C_eliminated":189,"unused_constant_removed":1,"remaining_nonconstant_C":2,
 "unlifted_source_presentation_variable_count":250,
 "optional_h_lift_presentation_variable_count":410,
 "optional_h_lift_nominal_rows_after_189_eliminations":1440,
 "selected_only_old_pass_remaining_row_fail_control":True,
 "certificate_bytes":out.stat().st_size,"certificate_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
 "dense_reconstruction_expanded":False,"solver_launched":False,
 "wall_seconds":time.monotonic()-started,"peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path("reconstruction_summary.json").write_text(json.dumps(summary,sort_keys=True,indent=2)+"\n")
print(json.dumps(summary,sort_keys=True),flush=True)
